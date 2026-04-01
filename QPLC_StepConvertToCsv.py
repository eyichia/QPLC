import os
import sys
import time
import csv
import math
import json
import struct
import pymcprotocol

from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QMenuBar, QMenu, QComboBox, QFileDialog)
from PySide6.QtCore import (QDateTime,QThread, Signal, Slot)
from PySide6.QtGui import (QIcon, QPixmap, QFont)

from QPLC_StepConvertToCsv_GUI_ui import Ui_MainWindow

# """取得資源絕對路徑，兼容開發與 PyInstaller 打包模式"""
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller 運行時的臨時資料夾路徑
        return os.path.join(sys._MEIPASS, relative_path)
    # 開啟開發模式下的路徑
    return os.path.join(os.path.abspath("."), relative_path)

# 背景 PLC 連線程式
class PLC1Worker(QThread):
    step_info = Signal(int, int)
    steps_data = Signal(list) # 如果需要傳回更多數據，可以使用 list 或 dict
    sm413_status = Signal(bool)
    error_occurred = Signal(str)

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

    def trigger_read_steps(self, start_addr, total_length):
        self.batch_start_addr = start_addr
        self.batch_size = total_length
        self.batch_read_trigger = True    

    def run(self):
        self.running = True # 確保每次 run 都從 True 開始
        plc = pymcprotocol.Type3E()
        plc.setaccessopt(commtype="binary")
        is_connected = False # 自定義一個旗標來紀錄連線狀態
        
        while self.running:
            try:
                # 如果尚未連線，則嘗試連線
                if not is_connected: # 假設有連線檢查
                    plc.connect(self.ip, self.port)
                    # 只讀取一次參數
                    res_total = plc.batchread_wordunits(headdevice=self.addr_total, readsize=1) #ZR是用16進制
                    res_len = plc.batchread_wordunits(headdevice=self.addr_len, readsize=1)
                    if res_total and res_len:
                        self.step_info.emit(res_total[0], res_len[0])
                        # --- 【關鍵修正 A】：連線成功且讀取完成，才設為 True ---
                        is_connected = True

                # 2. 正常讀取循環 (只有連線成功才執行)
                if is_connected:
                    _sm413_data = plc.batchread_bitunits(headdevice="SM413", readsize=1)
                    if _sm413_data:
                        self.sm413_status.emit(bool(_sm413_data[0]))
                # 讀取step數據
                if self.batch_read_trigger:
                    try:
                        results = plc.batchread_wordunits(
                            headdevice=self.batch_start_addr, 
                            readsize=self.batch_size
                        )
                        if results:
                            self.steps_data.emit(results)
                        else:
                            # 讀取結果為空，可以發送一個特定的警告給 UI
                            self.error_occurred.emit("讀取完成但無資料，請檢查位址範圍")
                    except Exception as e:
                        # 這裡的錯誤會被外層的大 except 捕捉，但我們確保觸發被關閉
                        raise e 
                    finally:
                        # --- 重點：不管成功或失敗，這次「任務」都算結束了 ---
                        self.batch_read_trigger = False        
                
                time.sleep(0.5) # 正常每 500ms 讀一次      
            except Exception as e:
                is_connected = False # 發生任何錯誤都視為連線失敗，重置旗標
                # 如果位址不存在，e 裡面通常會包含 PLC 回傳的十六進制錯誤碼
                error_msg = str(e)
                if "command error" in error_msg.lower() or "device" in error_msg.lower():
                    friendly_msg = f"位址無效或超出範圍: {self.addr_total}"
                else:
                    friendly_msg = f"通訊失敗: {error_msg}"
                print(friendly_msg) # 先在控制台印出錯誤訊息，方便除錯
                self.error_occurred.emit(friendly_msg)
                try: plc.close() # 發生錯誤先關閉舊連線
                except: pass
                time.sleep(2) # 等待 2 秒再重試，避免過度頻繁攻擊 PLC   
            
        # 只有當 self.running 變成 False (按下斷開按鈕) 才會跑到這裡
        try:
            plc.close()
            print("PLC 連線已安全關閉")
        except:
            pass

    def stop(self):
        self.running = False # 讓 run 裡的 while 迴圈結束
        self.wait()          # 等待執行緒完全停止
   



# 主畫面
class MainWindow(QMainWindow, Ui_MainWindow):
    version = " v1.1"
    Developer = " 江乙加 Eric Chiang"
    ver_date = " 2026-03-31"
    Copyright = f" 2026 {Developer}" #" 2026 " + Developer

# initial
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # --- 【核心修改】預載入 Logo 資源 ---
        self.logo_pixmap = QPixmap(resource_path("Assets/Mylogo.png"))
        self.style_pixmap = QPixmap(resource_path("Assets/Mystyle.png"))
        self.current_lang = "TW" # 開機語言

        self.worker = PLC1Worker() # 執行背景 PLC1 連線程
        
        self.init_ui_settings() # 設定圖示與預設圖
        self.set_default_value() # 預設值
        self.load_languages_json() #載入語言json檔案
        self.translate() #語言翻譯
        self.connect_signals() # 按鈕輸入訊號
# 設定視窗圖示
    def init_ui_settings(self):
        self.setWindowIcon(QIcon(self.style_pixmap)) #設定視窗圖示
        if hasattr(self, "Language"):
            self.Language.setIcon(QIcon(resource_path("Assets/Earth.png")))
            self.language_tc.setIcon(QIcon(resource_path("Assets/FlagTw.png")))
            self.language_sc.setIcon(QIcon(resource_path("Assets/FlagCn.png")))
            self.language_en.setIcon(QIcon(resource_path("Assets/FlagEn.png")))
# 預設值
    def set_default_value(self):
        self.server_ip_1.setValue(192)
        self.server_ip_2.setValue(168)
        self.server_ip_3.setValue(2)
        self.server_ip_4.setValue(140)
        self.port_no.setValue(1025)        
        self.total_step_address.setText("D680")
        self.step_length_address.setText("D681")
        self.start_address.setText("D2100")
        self.total_steps.setText("0")
        self.step_length.setText("0")
        self.PB_connect_plc.setEnabled(True)
        self.PB_deconnect_plc.setEnabled(False)
        self.label_connect_status.setText("--離線中--")
        self.step_no.setValue(1)
        for i in range(1, 11):
            self.findChild(QLabel, f"label_step_no_{i}").setText(f"{i}")
# 自動掃描 Languages 資料夾並載入所有 JSON
    def load_languages_json(self):
        self.languages = {}
        lang_dir = resource_path("Languages") # 你的語言包資料夾
        if not os.path.exists(lang_dir):
            os.makedirs(lang_dir)
            return

        for filename in os.listdir(lang_dir):
            if filename.endswith(".json"):
                lang_key = filename.replace(".json", "") # 例如 "en_US"
                try:
                    with open(os.path.join(lang_dir, filename), 'r', encoding='utf-8') as f:
                        self.languages[lang_key] = json.load(f)
                except Exception as e:
                    print(f"Error loading {filename}: {e}")
# 選單翻譯
    def translate_menu(self, menu_obj: QMenuBar | QMenu, lan_dict: dict):
        # 純文字切換版：只負責更新 QAction/QMenu 的文字內容。
        for action in menu_obj.actions():
            obj_name = action.objectName()
            submenu = action.menu()
            # 1. 處理 QAction 與 QMenu 的名稱連動偵測
            if not obj_name and submenu:
                obj_name = submenu.objectName()
            # 2. 匹配 JSON 並僅更新文字
            if obj_name in lan_dict:
                data = lan_dict[obj_name]
                # 相容兩種格式：如果是字典就拿 "text"，如果是純字串就直接用
                text = data["text"] if isinstance(data, dict) else data
                action.setText(text) # 更新 Action 文字
                if submenu:
                    submenu.setTitle(text) # 同步更新選單標題
                    self.translate_menu(submenu, lan_dict) # 遞迴翻譯子選單
# 語言翻譯
    def translate(self):
        if not self.languages: return
        lang = self.languages.get(self.current_lang, {})
        # 1. 視窗標題
        self.setWindowTitle(lang.get("Window_title", {}).get("Main", "編程編輯工具"))
        # 2. 選單列
        self.translate_menu(self.menuBar(), lang.get("Menubar", {}))
        # 3. 批次處理分類元件 (QLabel, QPushButton, QCombobox, Data1)
        t_default = lang.get("QLabel", {}).get("textFont", {"font_size": 14, "font_family": "Microsoft YaHei"})
        categories = ["QLabel", "QPushButton", "QCombobox", "QGroupBox"] #+ list(DATA_CONFIG.keys())
        for cat in categories:
            cat_data = lang.get(cat, {})
            for obj_name, data in cat_data.items():
                if obj_name == "textFont": continue # 跳過字體設定項
                
                widget = getattr(self, obj_name, None)
                if widget:
                    # 文字設定
                    content = data.get("text", "")
                    if isinstance(widget, QComboBox) and isinstance(content, list):
                        idx = widget.currentIndex()
                        widget.clear()
                        widget.addItems(content)
                        widget.setCurrentIndex(idx)
                    elif hasattr(widget, "setText"):
                        widget.setText(content)
                    elif hasattr(widget, "setTitle"):
                        widget.setTitle(content)

                    # 字體設定
                    f_size = data.get("font_size", t_default.get("font_size"))
                    f_family = data.get("font_family", t_default.get("font_family"))
                    widget.setFont(QFont(f_family, f_size))
# 繁簡英切換                
    def switch_language(self, new_lan):
        self.current_lang = new_lan
        self.translate()                                          
# 從當前語言包抓取訊息文字
    def get_msg(self, key, default=""):
        lang = self.languages.get(self.current_lang, {})
        return lang.get("Messages", {}).get(key, default)
# 從當前語言包抓取step文字 """
    def get_step(self, code, key):
        s_data = self.languages.get(self.current_lang, {})
        step_info = s_data.get("step", {}).get(str(code), {})
        default_val = "" if key == "text" else {} # 定義預設值：如果是拿 text 就給 ""，如果是拿 mode 就給 {}
        return step_info.get(key, default_val)
# get mode
    def get_mode_name(self, type, mode):
        mode_info = self.get_step(str(type), "mode")
        return mode_info.get(str(mode), "未知模式")
# 從當前語言包抓取step軸名稱
    def get_ax_name(self, ax_no):
        a_data = self.languages.get(self.current_lang, {})
        return a_data.get("Axis", {}).get(str(ax_no)) # 預設回傳原名稱，如果找不到對應的翻譯  
# 步序項目全部名稱
    def get_item_list(self, key):
        i_data = self.languages.get(self.current_lang, {})
        # 直接回傳該 key 對應的整個列表，找不到就回傳空列表 []
        return i_data.get("Item", {}).get(str(key), [])
# 步序項目單一名稱
    def get_item_name(self, key, idx=0):  
        i_data = self.languages.get(self.current_lang, {})
        item_list = i_data.get("Item", {}).get(str(key), [])
        if 0 <= idx < len(item_list):
            return item_list[idx]
        # 如果找不到，回傳一個辨識用的字串（方便除錯）
        return f"Unknown_{key}[{idx}]"   
# 轉字串
    def to_str(self, _data, _start, _stop, encoding='ascii'):
        label_words = _data[_start : _stop]
        byte_data = struct.pack(f'<{len(label_words)}H', *label_words)   
        # 增加 encoding 參數，預設還是 ascii 讀繁體中文 encoding='big5'
        _string = byte_data.decode(encoding, errors='ignore').strip('\x00')
        return _string    
# 按鈕輸入訊號
    def connect_signals(self):
        # menubar
        self.language_tc.triggered.connect(lambda: self.switch_language("TW"))
        self.language_sc.triggered.connect(lambda: self.switch_language("CN"))
        self.language_en.triggered.connect(lambda: self.switch_language("EN"))
        self.file_exit.triggered.connect(self.close)
        # HMI PB
        self.PB_connect_plc.clicked.connect(self.connect_plc)
        self.PB_deconnect_plc.clicked.connect(self.deconnect_plc)
        self.PB_read_step.clicked.connect(self.read_step_data)
        self.PB_export_csv.clicked.connect(self.export_summary_csv)
        # 連接 Worker 的數據回傳信號
        self.worker.step_info.connect(self.update_step_info)
        self.worker.error_occurred.connect(self.handle_error)
        self.worker.sm413_status.connect(self.update_sm413_status)
        self.worker.steps_data.connect(self.display_steps_data)
# 讀取step資料
    def read_step_data(self):
        self.connect_plc() # 確保已連線
        start_address = self.start_address.text().strip().upper()
        total_step_length = int(self.total_steps.text()) * int(self.step_length.text())
        self.worker.trigger_read_steps(start_address, total_step_length) 




# ----- PLC 連線與數據處理相關函式 -----        
# --- 【新增】更新 UI 數值的函式 ---
    @Slot(int, int)
    def update_step_info(self, total, length):
        self.total_steps.setText(str(total))
        self.step_length.setText(str(length))
        self.label_connect_status.setText("--連線成功且讀取完成--")
    @Slot(bool)
    def update_sm413_status(self, status):
        color = "green" if status else "yellow"
        self.SM413.setStyleSheet(f"""
            QLabel {{
                background-color: {color};
                border: 1px solid black;
                border-radius: 15px;
            }}
        """)  
    @Slot(list)
    def display_steps_data(self, data):
        # 這裡的 data 是從 Worker 傳回來的 PLC 數據列表
        # 你可以根據實際需求來處理這些數據，例如顯示在 UI 上或存成 CSV
        #self.step_data = data # 儲存到 MainWindow 的屬性，方便其他方法使用
        self.decode_step_data(data) # 呼叫解碼函式來處理數據
        #print("收到步驟數據:", data)
# --- 【新增】錯誤處理 ---
    def handle_error(self, err_msg):
        self.label_connect_status.setText(f"錯誤: {err_msg}")
        self.PB_connect_plc.setEnabled(True)
        self.PB_deconnect_plc.setEnabled(False)        
# 連接PLC
    def connect_plc(self):
        self.PB_connect_plc.setEnabled(False)
        self.PB_deconnect_plc.setEnabled(True)
        self.label_connect_status.setText("--連線中--")
        server_ip = f"{self.server_ip_1.value()}.{self.server_ip_2.value()}.{self.server_ip_3.value()}.{self.server_ip_4.value()}"
        port_no = self.port_no.value()
        # --- 【核心修改】將 UI 上的位址設定給 Worker ---
        self.worker.ip = server_ip
        self.worker.port = port_no
        self.worker.addr_total = self.total_step_address.text().strip().upper() #去除無用字元,轉大寫
        self.worker.addr_len = self.step_length_address.text().strip().upper()
        self.worker.start() # 呼叫 def run(self):
# 斷開PLC
    def deconnect_plc(self):
        self.PB_connect_plc.setEnabled(True)
        self.PB_deconnect_plc.setEnabled(False)
        self.label_connect_status.setText("--離線中--") 
        self.worker.stop() 
# 16bitTo32bit轉換
    def convert_16_to_32(self, low, high):
        # 將兩個 16-bit 數字合併成一個 32-bit 數字
        combined = (high << 16) | low
        # 如果最高位是 1，表示這是一個負數，進行符號擴展
        if combined & (1 << 31):
            combined -= (1 << 32)
        return combined  
# 16bit有符號轉換 (PLC裡的數字如果大於32767就代表是負數，要轉換成Python的負數表示法)      
    def convert_16bit_signed(self, value):
        # 如果大於 32767，代表在 PLC 裡是負數
        if value > 32767:
            return value - 65536
        return value    
# step data解碼        
    def decode_step_data(self, data):
        # 匯出csv時,每一行都必須是list[]格式,所以第一行也要放在list裡面["a","b",...]
        self.step_list = [["Step"]] 
        try:
            length = int(self.step_length.text())
            if length == 0: length = 20 # 防止除以 0
        except ValueError:
            length = 20 # 預設值，防止 UI 沒填數字當機

        _cylinderMap = ["1", "2", "3", "4"] # 有氣壓缸選項的步序類型
        # 開始解碼,每 length 個數據為一組，代表一個步序的完整資訊
        for i in range(0, len(data), length):
            step_num = (i // length) + 1 # 步序編號
            step_code = data[i] # 第1個字是動作類型
            step_name = self.get_step(step_code, "text")
            row = [f"{step_num}", step_name] # 先放入步驟編號和動作類型名稱

            item = self.get_item_list(step_code) # 取得模式項目名稱列表
            item_data = [] # 用來存 數據
            # 1~4軸運動控制
            if step_code in range(1, 5): 
                # 填入數據
                item_data.append(self.get_mode_name(step_code, data[i+1])) # ZR951
                id = 6
                for j in range(1, step_code + 1):
                    item_data.append(str(data[i + j + 1])) # ZR952~ZR955
                    pos = self.convert_16_to_32(data[i + id], data[i + id + 1]) #ZR956~ZR963
                    item_data.append(f"{float(pos) / 100:.2f}")
                    id += 2
            # 5繞線     
            elif step_code == 5:
                # 填入數據
                item_data.append(self.get_mode_name(step_code, data[i+1])) # ZR951
                #item_data.append(str(data[i+2])) # ZR952
                #item_data.append(str(data[i+3])) # ZR953
                item_data.extend([str(data[i+2]), str(data[i+3])])
                stop_angle = self.convert_16_to_32(data[i+6], data[i+7])
                item_data.append(f"{float(stop_angle) / 100:.2f}") # ZR956~ZR957
                #item_data.append(str(data[i+8])) # ZR958
                #item_data.append(str(data[i+10])) # ZR960
                #item_data.append(str(data[i+11])) # ZR961
                item_data.extend([str(data[i+8]), str(data[i+10]), str(data[i+11])])
            # 6繞線排線     
            elif step_code == 6:
                # 填入數據
                item_data.append(str(data[i+2])) # ZR952
                # ZR953 在 PLC 裡是有符號的，所以要轉換
                item_data.append(f"{float(self.convert_16bit_signed(data[i+3])) / 100:.2f}") # ZR953
                item_data.append(f"{float(data[i+4]) / 10:.1f}") # ZR954
                item_data.append(f"{float(self.convert_16bit_signed(data[i+5])) / 100:.2f}") # ZR955
                item_data.append(str(data[i+7])) # ZR957
                for offset in [8, 10, 12, 14]: # ZR958~ZR965 的四組角度數據
                    angle = self.convert_16_to_32(data[i+offset], data[i+offset+1])
                    item_data.append(f"{float(angle) / 100:.2f}") # ZR958~ZR965  
            # 7飛叉     
            elif step_code == 7:
                # 填入數據
                item_data.append(self.get_mode_name(step_code, data[i+1])) # ZR951
                stop_angle = self.convert_16_to_32(data[i+6], data[i+7]) #ZR956~ZR957
                item_data.append(f"{float(stop_angle) / 100:.2f}") # ZR956~ZR957
                item_data.append(str(data[i+8])) # ZR958
            # 8排線     
            elif step_code == 8:
                # 填入數據
                stop_angle = self.convert_16_to_32(data[i+6], data[i+7]) #ZR956~ZR957
                item_data.append(f"{float(stop_angle) / 100:.2f}") # ZR956~ZR957
            # 9轉槽     
            elif step_code == 9:
                # 填入數據
                item_data.append(self.get_mode_name(step_code, data[i+1])) # ZR951
                d8_slot = self.convert_16_to_32(data[i+8], data[i+9]) #ZR958~ZR959
                item_data.append(f"{d8_slot}") # ZR958~ZR959 
            # 10模寬     
            elif step_code == 10:
                # 填入數據
                item_data.append(self.get_mode_name(step_code, data[i+1])) # ZR951
                d6_pos = self.convert_16_to_32(data[i+6], data[i+7]) #ZR956~ZR957
                item_data.append(f"{float(d6_pos) / 100:.2f}") # ZR956~ZR957   
            # 11氣壓缸     
            elif step_code == 11:
                # 填入數據
                cylinder = self.convert_16_to_32(data[i+18], data[i+19])
                item_data.append(str(cylinder)) # ZR968~ZR969 的氣缸數值                      
            # 18等待     
            elif step_code == 18:
                d2_time = data[i+2] # ZR952
                item_data.append(f"{float(d2_time) / 10:.1f}") # ZR952   
            # 19暫停   
            elif step_code == 19:
                continue
                d2_time = data[i+2] # ZR952
                item_data.append(f"{float(d2_time) / 10:.1f}") # ZR952  
                d3_time = data[i+3] # ZR953
                item_data.append(f"{float(d3_time) / 10:.1f}") # ZR953
                item_data.append(str(data[i+4])) # ZR954
                d5_time = data[i+5] # ZR955
                item_data.append(f"{float(d5_time) / 10:.1f}") # ZR955 
                item_data.append(str(data[i+6])) # ZR956
            # 20~27跳躍
            elif step_code in range(20, 28):
                # 填入數據
                item_data.extend([str(data[i+2]), str(data[i+3]), str(data[i+4])]) # ZR952~ZR954
                label_string = self.to_str(data, i+6, i+16) # ZR956~ZR965 的數據切片[16-6=10個字]
                item_data.append(label_string) # ZR956~ZR965 的標籤數
            # 28 GOTO
            elif step_code == 28:
                label_string = self.to_str(data, i+6, i+16) # ZR956~ZR965 的數據切片[16-6=10個字]
                item_data.append(label_string) # ZR956~ZR965 的標籤數
            # 29 RET   
            elif step_code == 29:
                continue
            # 30~31副程式
            elif step_code in range(30, 32): 
                file_name = self.to_str(data, i+2, i+12) # ZR952~ZR961
                item_data.append(file_name) # ZR952~ZR961 的標籤數
            # 32 速度參數1
            elif step_code == 32:
                parameter_words = data[i+2 : i+10] # ZR952~ZR959
                # 使用 map 一次將所有數字轉成字串並加入 item_data
                item_data.extend(map(str, parameter_words))        
            # 33 速度參數2
            elif step_code == 33:
                parameter_words = data[i+2 : i+9] # ZR952~ZR958
                item_data.extend(map(str, parameter_words)) 
            # 40 標籤
            elif step_code == 40:
                label_string = self.to_str(data, i+2, i+12) # ZR952~ZR961 的數據切片[10個字]
                item_data.append(label_string)      
            # 41 註釋
            elif step_code == 41:
                comment_string = self.to_str(data, i+2, i+14) # ZR952~ZR963
                item_data.append(comment_string)     
    
            # 有氣壓缸選項的步序類型
            if str(step_code) in _cylinderMap:
                item_name = self.get_item_list(11) # 氣缸選項名稱
                item.append(item_name[0]) # 氣缸選項名稱
                cylinder = self.convert_16_to_32(data[i+18], data[i+19])
                item_data.append(str(cylinder)) # ZR968~ZR969 的氣缸數值

            # --- 【關鍵改善】留白處理 ---
            # 如果 Python 沒寫邏輯但 JSON 有標題，補空字串讓標題出現
            while len(item_data) < len(item):
                item_data.append("")

            for label, val in zip(item, item_data):
                row.extend([label, val]) # 使用 extend 效能略好於 += [] 
                     
            self.step_list.append(row)
            
        # 顯示在 TextEdit
        self.Process.clear()
        for r in self.step_list:
            self.Process.append(" | ".join(map(str, r)))
# UI單獨顯示步序            
    def ui_display_steps(self, data, length):   
        start_no = int(self.label_step_no_1.text()) # 從 UI 上的第一個步序編號開始 
        end_no = int(self.label_step_no_10.text()) # 從 UI 上的第一個步序編號開始
        for n in range(start_no, end_no+1):
            widget = getattr(self, f"label_step_no_{n}", None)
            if widget: 
                widget.clear()
                widget.setStyleSheet("background-color: #B5B5B5;")

        base_idx = (start_no - 1) * length
        for i in range(10):
            current_idx = base_idx + (i * length)
            step_name = data[idx+1] # 每個步序的第二個數據是 step_code
            line_edit = getattr(self, f"label_step_no_{start_no+i}", None)
            if line_edit:
                line_edit.setText(step_name)
                if not line_edit.text() == "": # 不=空白
                    line_edit.setStyleSheet("background-color: #FFFFFF;") # 有數據就變白色 


   




# """資料處理,路徑,資料夾,檔名,格式"""
    def data_processing(self, folder, filename, format, title, mode):
        # 1. 準備路徑與資料夾
        default_dir = os.path.join(os.getcwd(), folder)
        if not os.path.exists(default_dir): os.makedirs(default_dir)
        # 2. 準備過濾器
        filters = {
            "csv": "CSV Files (*.csv)",
            "xlsx": "xlsx Files (*.xlsx)",
            "txt": "Text Files (*.txt)",
            "pdf": "PDF Files (*.pdf)",
            "png": "Png Files (*.png)",
            "json": "JSON Files (*.json)"
        }
        file_filter = filters.get(format, "All Files (*)")
        # 3. 根據模式執行不同的對話框
        if mode == "save":
            # 儲存模式：自動生成帶時間戳的預設檔名
            default_filename = f"{filename}_{QDateTime.currentDateTime().toString('yyyyMMdd_HHmmss')}.{format}"
            initial_path = os.path.join(default_dir, default_filename)
            file_path, _ = QFileDialog.getSaveFileName(self, self.get_msg(title), initial_path, file_filter)
        else:
            # 開啟模式：直接打開資料夾，不需要預設檔名
            file_path, _ = QFileDialog.getOpenFileName(self, self.get_msg(title), default_dir, file_filter)
        # 4. 統一回傳檢查
        return file_path if file_path else None   
# """ 輸出橫向對比報表 (CSV 格式) """
    def export_summary_csv(self):
        if not hasattr(self, "step_list") or len(self.step_list) <= 1:
            print("沒有步驟數據可供匯出")
            return
        # 獲取存檔路徑 (利用你的萬用助手)
        file_path = self.data_processing("Reports", "Step_code", "csv", "report", "save")
        if not file_path: return
        #data_to_save = []
        #for item in self.step_list:
            #if isinstance(item, list):
                #data_to_save.append(item)
            #else:
                #data_to_save.append([item]) # 把 "Step" 變成 ["Step"]

        try:
            # newline='' 防止 Windows 存檔出現多餘空行
            # utf-8-sig 確保 Excel 開啟中文不會亂碼
            with open(file_path, 'w', newline='', encoding='utf-8-sig') as f:
                writer = csv.writer(f)
            
                # 3. 寫入所有資料
                writer.writerows(self.step_list)
            
            print(f"CSV 存檔成功！路徑：{file_path}")
        except Exception as e:
            print(f"存檔時發生錯誤: {e}")
           

        
        
      

# 關閉程式
    def closeEvent(self, event):
        # 關閉視窗時也要記得停止背景執行緒，避免程式卡在背景
        self.worker.stop() # 確保背景執行緒被正確停止
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    try:
        myWin = MainWindow()
        myWin.show()
        sys.exit(app.exec())
    except Exception as e:
        print(f"啟動失敗: {e}")        
