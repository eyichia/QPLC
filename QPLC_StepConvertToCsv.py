import os
import sys
import time
import csv
import math
import json
import pymcprotocol

from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QMenuBar, QMenu, QComboBox)
from PySide6.QtCore import (QThread, Signal, Slot)
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
    ver_date = " 2026-03-19"
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
        self.start_address.setText("D2200")
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
        """ 
        純文字切換版：只負責更新 QAction/QMenu 的文字內容。
        """
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
                    # 遞迴翻譯子選單
                    self.translate_menu(submenu, lan_dict)   
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
# 從當前語言包抓取step文字 """
    def get_step(self, m_code, text_mode):
        s_data = self.languages.get(self.current_lang, {})
        return s_data.get("step", {}).get(m_code, {}).get(text_mode, {})
# 從當前語言包抓取step軸名稱
    def get_ax_name(self, ax_no):
        a_data = self.languages.get(self.current_lang, {})
        return a_data.get("Axis", {}).get(ax_no) # 預設回傳原名稱，如果找不到對應的翻譯  
    
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
# 解碼步驟數據的函式
    #def decode_step_data(self, data):  



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
        print("收到步驟數據:", data)
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
        self.worker.addr_total = self.total_steps.text().strip().upper() #去除無用字元,轉大寫
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
# step data解碼        
def decode_step_data(self, data):
    self.step_list = []
    self.step_list.append("Step")
    try:
        length = int(self.step_length.text())
    except ValueError:
        length = 20 # 預設值，防止 UI 沒填數字當機

    length = int(self.step_length.text())
    _modeMap = ["1", "2", "3", "4", "5", "7", "8", "9", "10"]
    _axopMap = ["1", "2", "3", "4"]
    _cylinderMap = ["1", "2", "3", "4", "7", "8", "9", "10", "11"]

    for i in range(0, len(data), length):
        step_num = (i // length) + 1 # 步序編號
        motion_type = str(data[i]) # 第1個字是動作類型
        type_name = self.get_step(motion_type, "text")
        row = [f"Step {step_num}", type_name] # 先放入步驟編號和動作類型名稱
        
        #mode_name = "無"
        if motion_type in _modeMap:
            _mode_code = str(data[i+1])
            mode_info = self.get_step(motion_type, "mode")
            mode_name = mode_info.get(_mode_code, "未知模式")
            row += ["模式", mode_name] # 如果有模式資訊，再把模式名稱放入 row
        # --- 2. 處理軸資訊 
        ax_details = [] # 用來存 軸1, ax1, 軸2, ax2...
        if motion_type in _axopMap:
            ax_count = int(motion_type)
            for j in range(1, ax_count + 1):
                # 取得軸號位址：索引 i+2 開始往後推
                ax_no = str(data[i + 1 + j]) 
                ax_name = self.get_ax_name(ax_no)
                pos_low = data[i + 5 + j]
                pos_high = data[i + 6 + j]
                ax_pos = self.convert_16_to_32(pos_low, pos_high)
                # 直接把「軸序號」和「名稱」依序放入列表
                ax_details.append(f"軸選項{j}")
                ax_details.append(ax_name)
                ax_details.append(f"位置{j}")
                ax_details.append(str(float(ax_pos) / 100))
            row += ax_details # 如果有軸資訊，再把軸的詳細資料放入 row    
        cylinder_details = []
        if motion_type in _cylinderMap:
            cyl_low = data[i + 18]
            cyl_high = data[i + 19]            
            cylinder = self.convert_16_to_32(cyl_low, cyl_high)
            cylinder_details.append("氣缸選項")
            cylinder_details.append(str(cylinder))
            row += cylinder_details # 如果有氣缸資訊，再把氣缸的詳細資料放入 row

            self.step_list.append(row)


        
        
      

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
