import os
import sys
import time
import csv
import math
import json
# import struct
import socket
# import pymcprotocol
# import re

from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QLabel, QSpinBox, QMenuBar, QMenu, QComboBox, QFileDialog,
                               QListView)
from PySide6.QtCore import (Qt, QDateTime,QThread, Signal, Slot)
from PySide6.QtGui import (QIcon, QPixmap, QFont)

from QPLC_StepConvertToCsv_GUI_ui import Ui_MainWindow
from plc_worker import PLC1Worker # PLC通訊程式
from Sub.utils import data_processing, show_prompt_window, convert_16_to_32, convert_16bit_signed, to_str # 工具程式

# """取得資源絕對路徑，兼容開發與 PyInstaller 打包模式"""
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller 運行時的臨時資料夾路徑
        return os.path.join(sys._MEIPASS, relative_path)
    # 開啟開發模式下的路徑
    return os.path.join(os.path.abspath("."), relative_path)

# 主畫面
class MainWindow(QMainWindow, Ui_MainWindow):
    VERSION = " v1.1"
    DEVELOPER = " 江乙加 Eric Chiang"
    VER_DATE = " 2026-03-31"
    COPYRIGHT = f" 2026 {DEVELOPER}" #" 2026 " + DEVELOPER
    # 格式檔名
    FORMAT_NAME_LIST = ["C1M", "C1K", "C1J", "SW7B"]

# initial
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # --- 【核心修改】預載入 Logo 資源 ---
        self.logo_pixmap = QPixmap(resource_path("Assets/Mylogo.png"))
        self.style_pixmap = QPixmap(resource_path("Assets/Mystyle.png"))
        self.current_lang = "TW" # 開機語言
        self.current_model = "C1M" #預設機型
        self.worker = PLC1Worker() # 執行背景 PLC1 連線程
        # 初始設定
        self.init_ui_settings() # 1.設定圖示與預設圖
        self.init_combobox_data() # 2.設定清單元件
        self.connect_signals() # 3.按鈕輸入訊號
        self.load_languages_json() # 4.載入語言json檔案
        self.translate() # 5.語言翻譯
        self.load_model_json() # 6.自動掃描 Model 資料夾並載入 JSON
        self.set_default_value() # 7.預設值
        # 預設IP後 自動讀取 IP
        pc_ip = self.get_local_ip()
        self.label_pc_ip.setText(f"PC IP: {pc_ip}")
# get pc ip        
    def get_local_ip(self):
        try:
            # 獲取所有 IP 列表
            hostname = socket.gethostname()
            ip_list = [info[4][0] for info in socket.getaddrinfo(hostname, None, socket.AF_INET)]
            ips = " | ".join(ip_list)
            plc_ip = f"{self.server_ip_1.value()}.{self.server_ip_2.value()}.{self.server_ip_3.value()}"
            # 優先尋找 192.168.2 開頭的 IP
            for ip in ip_list:
                if ip.startswith(plc_ip):
                    return ips
            # 如果找不到，回傳第一個非迴路 IP
            for ip in ip_list:
                if ip != "127.0.0.1":
                    return ips
                
            return "127.0.0.1"
        except:
            return "127.0.0.1" 
# 設定視窗圖示
    def init_ui_settings(self):
        self.setWindowIcon(QIcon(self.style_pixmap)) #設定視窗圖示
        if hasattr(self, "Language"):
            self.Language.setIcon(QIcon(resource_path("Assets/Earth.png")))
            self.language_tc.setIcon(QIcon(resource_path("Assets/FlagTw.png")))
            self.language_sc.setIcon(QIcon(resource_path("Assets/FlagCn.png")))
            self.language_en.setIcon(QIcon(resource_path("Assets/FlagEn.png")))
# 設定清單元件內容
    def init_combobox_data(self):
        """" 多個清單
        all_combobox = [self.model, .., ..] # 所有清單
        for combo in all_combobox: 
            combo.setView(QListView()) # 統一設定View，確保 QSS 生效

        for combo in [self.model,.. ,..]: # 設定元件屬性
            combo.setEditable(True)             # 必須先設為可編輯
            combo.lineEdit().setReadOnly(True)  # 設為唯讀，防止使用者亂打字
            combo.lineEdit().setAlignment(Qt.AlignLeft) # 真正的靠左對齊！
        """
        self.model.setView(QListView())
        self.model.setEditable(True)
        self.model.lineEdit().setReadOnly(True)
        self.model.lineEdit().setAlignment(Qt.AlignLeft)
        self.model.clear()
        self.model.addItems(self.FORMAT_NAME_LIST) # 格式檔案名稱
# 按鈕輸入訊號
    def connect_signals(self):
        # menubar
        self.language_tc.triggered.connect(lambda: self.switch_language("TW"))
        self.language_sc.triggered.connect(lambda: self.switch_language("CN"))
        self.language_en.triggered.connect(lambda: self.switch_language("EN"))
        self.file_exit.triggered.connect(self.close)
        # 變更HMI step no
        self.step_no.editingFinished.connect(self.step_no_enter)
        self.PB_step_up.clicked.connect(lambda: self.step_up_down(-10))
        self.PB_step_down.clicked.connect(lambda: self.step_up_down(10))
        # HMI PB
        self.PB_connect_plc.clicked.connect(self.connect_plc)
        self.PB_deconnect_plc.clicked.connect(self.deconnect_plc)
        self.PB_export_csv.clicked.connect(self.export_summary_csv)
        self.model.currentIndexChanged.connect(self.load_model_json)
        # PLC 相關
        self.PB_read_step.clicked.connect(self.read_step_data) # 讀取步序
        self.worker.steps_data.connect(self.display_steps_data) # 回應步序
        # 連接 Worker 的數據回傳信號
        self.worker.step_info.connect(self.update_step_info)
        self.worker.error_occurred.connect(self.handle_error)
        self.worker.sm413_status.connect(self.update_sm413_status)
        self.worker.plc1_status.connect(self.display_plc_status)
        
# --- 【多國語言切換】 ---
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
        self.format_dic = self.model_format.get(self.current_lang, {}) 
        self.decode_step_data(self.current_plc_data)
# 從當前語言包抓取訊息文字
    def get_msg(self, key, default=""):
        lang = self.languages.get(self.current_lang, {})
        return lang.get("Messages", {}).get(key, default)
# 抓取PLC訊息文字
    def get_plc_status_msg(self, key, default=""):
        lang = self.languages.get(self.current_lang, {})
        return lang.get("plc_status", {}).get(key, default)    
# 自動掃描 Model 資料夾並載入 JSON
    def load_model_json(self):
        #self.model_format = {}
        model_dir = resource_path("Model") # 你的語言包資料夾
        model_key = self.model.currentText()
        model_name = f"{model_key}.json"
        if not os.path.exists(model_dir):
            os.makedirs(model_dir)
            return

        try:
            with open(os.path.join(model_dir, model_name), 'r', encoding='utf-8') as f:
                self.model_format = json.load(f)
                self.load_step_format() # 讀取步序基本資料
        except Exception as e:
            print(f"Error loading {model_name}: {e}")
# 讀取步序基本資料
    def load_step_format(self):
        # 這是最乾淨的寫法，前提是 JSON 格式必須 100% 吻合
        # self.total_steps_addr = self.model_format["Format"]["total_step"][0]
        # 這是最保險的寫法，即便檔案損壞也不會閃退[有預設值]
        # self.total_steps_addr = self.model_format.get("Format", {}).get("total_step", ["D680"])
        target = self.model_format.get("Format", {})

        ts_data = target.get("total_step", ["D680", 500])
        self.total_steps_addr = ts_data[0]
        self.total_steps_val = ts_data[1]
        ts_info = f"[{self.total_steps_addr} , {self.total_steps_val}]"
        self.total_step_info.setText(ts_info)    

        sl_data = target.get("step_length", ["D681", 20])
        self.step_length_addr = sl_data[0]
        self.step_length_val = sl_data[1]
        sl_info = f"[{self.step_length_addr} , {self.step_length_val}]"
        self.step_length_info.setText(sl_info)

        self.start_addr = target.get("start_address", "D2200")
        self.start_address_info.setText(f"[{self.start_addr}]")
        # 讀取對應語言步序內容
        self.format_dic = {}
        self.format_dic = self.model_format.get(self.current_lang, {})       
# 預設值
    def set_default_value(self):
        self.server_ip_1.setValue(192)
        self.server_ip_2.setValue(168)
        self.server_ip_3.setValue(2)
        self.server_ip_4.setValue(140)
        self.port_no.setValue(1025)
        self.response_ts_val.clear()
        self.response_sl_val.clear()
        #self.PB_connect_plc.setEnabled(True)
        #self.PB_deconnect_plc.setEnabled(False)
        self.display_plc_status(-1)
        self.step_no.setValue(1)
        for i in range(1, 11):
            self.findChild(QSpinBox, f"d15{i-1}_step_no{i}").setValue(i)
# get mode
    def get_mode(self, code, mode):
        mode_info = self.format_dic.get("mode", {}).get(str(code), [])[mode]
        return mode_info
# 讀取step資料
    def read_step_data(self):
        start_address = self.start_addr.strip().upper()
        total_step_length = self.total_steps_val * self.step_length_val
        self.worker.trigger_read_steps(start_address, total_step_length)
# step go up or down
    def step_up_down(self, offset):
        no = self.d150_step_no1.value() + offset
        self.change_step_no(no)
# 輸入步序 no
    def step_no_enter(self):
        self.change_step_no(self.step_no.value())
# 變更step no <翻頁>
    def change_step_no(self,offset):
        try:
            # 1. 取得總步數，並確保至少為 10 
            total = self.total_steps_val
            # 計算最大起始編號 (例如總共 100 步，最後一頁起點是 91)
            max_no = max(1, total - 9)
            # 2. 限制起始編號範圍：不可小於 1，也不可大於 max_no
            if offset > max_no:
                first_no = 1
            elif offset < 1:
                first_no = max_no
            else:
                first_no = offset   
                   
            #first_no = max(1, offset if offset <= max_no else max_no)
            # 3. 更新 UI 上的 10 個編號標籤 (QLabel)
            for i in range(1, 11):
                current_spin = self.findChild(QSpinBox, f"d15{i-1}_step_no{i}")
                if current_spin:
                    current_spin.setValue(first_no + i - 1)


            # 4. 【重要】編號改變後，必須重新呼叫顯示函式來更新動作名稱
            # 假設你已經將讀回來的 PLC 資料存在 self.current_plc_data
            if hasattr(self, "current_plc_data"):
                length = self.step_length_val
                self.ui_display_steps(self.current_plc_data, length)
                
        except ValueError:
            pass # 防止總步數還沒讀到時出錯                    

# step data解碼        
    def decode_step_data(self, data):
        # 匯出csv時,每一行都必須是list[]格式,所以第一行也要放在list裡面["a","b",...]
        self.step_list = [["Step"]] 
        try:
            length = self.step_length_val
            if length == 0: length = 20 # 防止除以 0
        except ValueError:
            length = 20 # 預設值，防止 UI 沒填數字當機

        # 開始解碼,每 length 個數據為一組，代表一個步序的完整資訊
        for i in range(0, len(data), length):
            step_num = (i // length) + 1 # 步序編號
            step_code = data[i] # 第1個字是動作類型
            step_name = self.format_dic.get("code", {}).get(str(step_code))
            row = [f"{step_num}", step_name] # 先放入步驟編號和動作類型名稱

            item = self.format_dic.get("item", {}).get(str(step_code), [[],[]]) # 取得模式項目
            item_list = item[0] # 名稱列表
            item_format = item[1] # 數據格式
    
            for j in range(len(item_list)):
                label = item_list[j]
                fmt = item_format[j] if j < len(item_format) else "non"
                parts = fmt.split(';') # 使用分號';'進行拆分

                if label == "non" and parts[0] == "non":
                    continue

                try: # 拆解格式 json(["2;STR;20"])
                    if parts[0] != "non":
                        id = int(parts[0]) # 偏移量
                        ty = parts[1]        # 型態 (U, S, UD, SD, STR)
                        rmk = parts[2] if len(parts) > 2 else "0" # 備註或小數位

                        val = 0
                        result = ""
                        if ty == "STR":
                            str_len = math.ceil(int(rmk) / 2)
                            result = to_str(data, i+id, i+id+str_len)
                        elif rmk == "mode": # 模式參數
                            result = self.get_mode(step_code, data[i+id])
                            #item_data.append(self.get_mode(step_code, data[i+id]))
                        elif rmk == "axis": # 軸選項參數   
                            result = self.format_dic.get("axis", {}).get(str(data[i+id]))
                            #item_data.append(self.format_dic.get("axis", {}).get(str(data[i+id])))    
                        else: # 數值,字串等參數
                            if ty == "S":
                                val = convert_16bit_signed(data[i+id])
                            elif ty == "U":
                                val = data[i+id]                                                       
                            elif ty == "UD":
                                val = convert_16_to_32(data[i+id], data[i+id+1], signed=False)
                            else:
                                val = convert_16_to_32(data[i+id], data[i+id+1], signed=True)

                            # 處理小數點 (rmk 此時為數字字串)
                            if rmk.isdigit():
                                prec = int(rmk)
                                divisor = 10 ** prec
                                result = f"{float(val) / divisor:.{prec}f}"
                            else:
                                result = str(val)

                        if label == "non":
                            row.append(result)
                        else:
                            row.extend([label, result])

                except Exception as e:
                    print(f"解析步序 {step_num} 項目 {label} 失敗: {e}")

            self.step_list.append(row)
            
        # 顯示在 TextEdit
        self.Process.clear()
        for r in self.step_list:
            self.Process.append(" | ".join(map(str, r)))

        self.ui_display_steps(data, length)    
# UI單獨顯示步序            
    def ui_display_steps(self, data, length):   
        try:
            start_no = self.d150_step_no1.value() # 從 UI 上的第一個步序編號開始 
            end_no = self.d159_step_no10.value() # 從 UI 上的第一個步序編號開始
            for n in range(1, 11):
                widget = getattr(self, f"step_{n}", None)
                if widget: 
                    widget.clear()
                    widget.setStyleSheet("background-color: #B5B5B5;")

            base_idx = (start_no - 1) * length
            for i in range(10):
                current_idx = base_idx + (i * length)
                # 防呆：確保 index 沒超出 data 長度
                if current_idx < len(data):
                    # 取得動作代碼
                    step_code = data[current_idx] 
                    # 【核心修正】轉換為中文名稱，例如 "1軸運動控制"
                    step_name = self.format_dic.get("code", {}).get(str(step_code)) 
                    
                    # 取得對應的 QLineEdit (step_1 ~ step_10)
                    line_edit = getattr(self, f"step_{i+1}", None)
                    if line_edit:
                        line_edit.setText(step_name)
                        if step_code != 0 :
                            line_edit.setStyleSheet("background-color: #FFFFFF;") # 有數據就變白色 
        except Exception as e:
            print(f"UI 顯示失敗: {e}") 
# """ 輸出橫向對比報表 (CSV 格式) """
    def export_summary_csv(self):
        if not hasattr(self, "step_list") or len(self.step_list) <= 1:
            print("沒有步驟數據可供匯出")
            return
        # 獲取存檔路徑 (利用你的萬用助手)
        file_path = data_processing(
            parent=self,
            folder="Reports",
            filename="Step_code",
            format="csv",
            title=self.get_msg("report"),
            mode="save"
        )
        if not file_path: return

        try:
            # newline='' 防止 Windows 存檔出現多餘空行
            # utf-8-sig 確保 Excel 開啟中文不會亂碼
            with open(file_path, 'w', newline='', encoding='utf-8-sig') as f:
                writer = csv.writer(f)
            
                # 寫入所有資料
                processed_data = []
                for row in self.step_list:
                    new_row = []
                    for cell in row:
                        # CSV 檔案中看到超過 15 位的純數字時，會自動把它當成「數值」處理
                        # 檢查是否為長度超過 12 位的純數字字串
                        if isinstance(cell, str) and cell.isdigit() and len(cell) > 12:
                            # 轉成 Excel 的文字公式格式： ="123456..."
                            new_row.append(f'="{cell}"')
                        else:
                            new_row.append(cell)
                    processed_data.append(new_row)
                
                    # 寫入處理過的資料
                writer.writerows(processed_data)

            title, text = self.get_msg("success"), f"{self.get_msg('csv_save_ok', 'CSV 數據已存至：')}{file_path}"
            icon, buttons = self.logo_pixmap, QMessageBox.StandardButton.Ok
            theme, font_size, icon_size = "default", 12, 64
            show_prompt_window(self, title, text, icon, buttons, theme, font_size, icon_size)
        except Exception as e:
            title, text = self.get_msg("fail"), f"{self.get_msg('csv_save_fail', 'CSV 儲存失敗')}{str(e)}"
            icon, buttons = QMessageBox.Icon.Warning, QMessageBox.StandardButton.Close
            theme, font_size, icon_size = "default", 12, 64
            show_prompt_window(self, title, text, icon, buttons, theme, font_size, icon_size)
           

        
        
# ----- PLC 連線與數據處理相關函式 -----
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
        self.worker.addr_total = self.total_steps_addr.strip().upper() #去除無用字元,轉大寫
        self.worker.addr_len = self.step_length_addr.strip().upper()
        self.worker.start() # 呼叫 def run(self):
# 斷開PLC
    def deconnect_plc(self):
        #self.PB_connect_plc.setEnabled(True)
        #self.PB_deconnect_plc.setEnabled(False)
        #self.label_connect_status.setText("--離線中--")
        self.worker.stop()         
# --- 【新增】更新 UI 數值的函式 ---
    @Slot(int, int)
    def update_step_info(self, total, length):
        self.response_ts_val.setText(str(total))
        self.response_sl_val.setText(str(length))
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
        self.current_plc_data = data
        self.decode_step_data(data) # 呼叫解碼函式來處理數據
        #print("收到步驟數據:", data)
    @Slot(int)
    def display_plc_status(self,status):
        if status == 0:
            status_text = self.get_plc_status_msg(str(status), "離線中")
            self.PB_connect_plc.setEnabled(True)
            self.PB_deconnect_plc.setEnabled(False)
        elif status == 1:
            status_text = self.get_plc_status_msg(str(status), "連線中")    
            self.PB_connect_plc.setEnabled(False)
            self.PB_deconnect_plc.setEnabled(True)
        elif status == 2:
            status_text = self.get_plc_status_msg(str(status), "已連線")    
            self.PB_connect_plc.setEnabled(False)
            self.PB_deconnect_plc.setEnabled(True)    
        else:
            status_text = self.get_plc_status_msg("non", "")
            self.PB_connect_plc.setEnabled(True)
            self.PB_deconnect_plc.setEnabled(False)    

        self.label_connect_status.setText(status_text)
# --- 【新增】錯誤處理 ---
    def handle_error(self, err_msg):
        self.label_connect_status.setText(f"錯誤: {err_msg}")
        self.PB_connect_plc.setEnabled(True)
        self.PB_deconnect_plc.setEnabled(False)              
# 關閉程式
    def closeEvent(self, event):
        title = self.get_msg("close_title", "警告: 關閉程式")
        text = self.get_msg("close_text", "您確定要關閉程式嗎？")
        icon = QMessageBox.Icon.Question
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        theme = "default"
        font_size = 14
        icon_size = 80
        result = show_prompt_window(self, title, text, icon, buttons, theme, font_size, icon_size)
        if result == QMessageBox.StandardButton.Yes or result == QMessageBox.StandardButton.Ok:
            # 關閉視窗時也要記得停止背景執行緒，避免程式卡在背景
            self.worker.stop() # 確保背景執行緒被正確停止
            event.accept()
        else:
            event.ignore()  # 忽略關閉事件，回到程式    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    try:
        myWin = MainWindow()
        myWin.show()
        sys.exit(app.exec())
    except Exception as e:
        print(f"啟動失敗: {e}")        
