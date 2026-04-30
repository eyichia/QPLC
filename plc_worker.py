import time
import re
import pymcprotocol
from PySide6.QtCore import QThread, Signal

# 背景 PLC 連線程式
class PLC1Worker(QThread):
    step_info = Signal(int, int)
    steps_data = Signal(list) # 如果需要傳回更多數據，可以使用 list 或 dict
    sm413_status = Signal(bool)
    plc1_status = Signal(str, str, str)
# initial
    def __init__(self):
        super().__init__()
        self.ip = ""
        self.port = 0
        self.addr_total = ""
        self.addr_len = ""
        self.running = True # 控制迴圈開關
        self.batch_read_trigger = False 
        self.batch_start_addr = ""
        self.batch_size = 0
        self.status = "non"
        self.status_error = "non"
        self.status_msg = ""
# 觸發讀取step        
    def trigger_read_steps(self, start_addr, total_length):
        self.batch_start_addr = start_addr
        self.batch_size = total_length
        self.batch_read_trigger = True    
        self.status = "s10" # 正在讀取步驟數據
        print(f"已觸發讀取步驟數據: 起始位址={start_addr}, 總長度={total_length}") # 這行可以幫助確認觸發是否成功
# 【新增】必須加入這個位址遞增工具，否則分段讀取會當機
    def increment_address(self, addr, offset):
        # 拆分 D2100 -> prefix="D", number=2100
        match = re.match(r"([a-zA-Z]+)([0-9]+)", addr)
        if match:
            prefix = match.group(1)
            number = int(match.group(2))
            return f"{prefix}{number + offset}"
        return addr
# PLC 連線與讀取主迴圈        
    def run(self):
        self.running = True # 確保每次 run 都從 True 開始
        is_connected = False # 自定義一個旗標來紀錄連線狀態
        current_status = "non"
        current_error = "non"
        current_text = ""
        retry_count = 0
        max_retries = 10
        
        while self.running:
            try:
                # 如果尚未連線，則嘗試連線
                if not is_connected: # 假設有連線檢查
                    plc = pymcprotocol.Type3E()
                    plc.setaccessopt(commtype="binary")
                    self.status = "s1" # 連線中
                    plc.connect(self.ip, self.port)
                    # 只讀取一次參數
                    res_total = plc.batchread_wordunits(headdevice=self.addr_total, readsize=1) #ZR是用16進制
                    res_len = plc.batchread_wordunits(headdevice=self.addr_len, readsize=1)
                    if res_total and res_len:
                        self.step_info.emit(res_total[0], res_len[0])
                        is_connected = True # 連線成功且讀取完成，才設為 True
                        self.status = "s2" # 已連線
                        self.status_error = "non"
                        self.status_msg = ""    
                        retry_count = 0
                # 2. 正常讀取循環 (只有連線成功才執行)
                if is_connected:
                    _sm413_data = plc.batchread_bitunits(headdevice="SM413", readsize=1)
                    if _sm413_data:
                        self.sm413_status.emit(bool(_sm413_data[0]))
                # 讀取step數據
                #字元單位 (Word units)：單次讀取上限通常是 960 個字 (Words)
                #位元單位 (Bit units)：單次讀取上限是 7168 點
                if self.batch_read_trigger:
                    try:
                        all_results = []
                        current_addr = self.batch_start_addr
                        remaining_size = self.batch_size
                        MAX_CHUNK = 900 # 設定單次讀取上限為 900，保留一點安全邊際
                        while remaining_size > 0:
                            read_now = min(MAX_CHUNK, remaining_size)
                            #print(f"正在讀取位址: {current_addr}, 長度: {read_now}")
                            chunk_results = plc.batchread_wordunits(
                                headdevice = current_addr, 
                                readsize = read_now
                            )
                            if chunk_results:
                                all_results.extend(chunk_results) # 拼接數據
                                # 計算下一次的起始位址與剩餘長度
                                current_addr = self.increment_address(current_addr, read_now)
                                remaining_size -= read_now
                            else:
                                raise Exception("PLC 回傳空數據")
                        if all_results:
                            self.steps_data.emit(all_results) # 全部讀完後一次發送給 UI
                            self.status = "s11" # 讀取完成
                    except Exception as e:
                        self.status_error = "e800" # 讀取失敗
                        self.status_msg = str(e) # 如果位址不存在，e 裡面通常會包含 PLC 回傳的十六進制錯誤碼
                    finally:
                        self.batch_read_trigger = False
                
                time.sleep(0.5) # 正常每 500ms 讀一次      
            except Exception as e:
                if not self.running: 
                    break # 如果已經按下斷開，就直接結束，不要再廣播「timed out」的錯誤訊息
                is_connected = False # 發生任何錯誤都視為連線失敗，重置旗標
                retry_count += 1
                error_msg = str(e) # 如果位址不存在，e 裡面通常會包含 PLC 回傳的十六進制錯誤碼
                # 判斷是否超過最大重試次數
                if retry_count >= max_retries:
                    self.status = "non" # 正常顯示離線
                    self.status_error = "e801" # 超過重試次數上限
                    self.status_msg = ""
                    retry_count = 0
                    self.running = False # 強制停止 while 迴圈，執行緒將結束
                else:
                    if "command error" in error_msg.lower() or "device" in error_msg.lower():
                        self.status_error = "e802" # 位址無效或超出範圍
                        self.status_msg = ""
                    else:
                        self.status_error = "e803" # 其他通訊失敗
                        self.status_msg = str(error_msg)
                      
                try: 
                    plc.close() # 發生錯誤先關閉舊連線
                except: pass

                if self.running: # 如果還沒到 5 次，才等待 2 秒
                    self.status = "s3" # 正在重新連線
                    self.status_msg = str(retry_count)
                    time.sleep(3)

            if self.status != current_status or self.status_error != current_error or self.status_msg != current_text:
                current_status = self.status
                current_error = self.status_error
                current_text = self.status_msg
                self.plc1_status.emit(self.status, self.status_error, self.status_msg)
        # 只有當 self.running 變成 False (按下斷開按鈕) 才會跑到這裡
        try:
            plc.close()
            print("PLC 連線已安全關閉")
        except:
            pass

    def stop(self):
        self.running = False # 讓 run 裡的 while 迴圈結束
        # 注意：不要在這裡呼叫 self.wait()，否則會導致主畫面(UI)卡死