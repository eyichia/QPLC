import os
import sys
import time
import pymcprotocol

from PySide6.QtWidgets import (QApplication, QMainWindow)
from PySide6.QtCore import (QThread, Signal, Slot)
from PySide6.QtGui import (QIcon, QPixmap)



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
    data_ready = Signal(int, int)
    error_occurred = Signal(str)

    def __init__(self):
        super().__init__()
        self.ip = ""
        self.port = 0
        self.addr_total = ""
        self.addr_len = ""
        self.running = True # 控制迴圈開關

    def run(self):
        plc = pymcprotocol.Type3E()
        plc.setaccessopt(commtype="binary")
        
        try:
            # --- 第一階段：建立連線 ---
            plc.connect(self.ip, self.port) # 等PLC回應--成功往下--失敗執行except
            
            # --- 第二階段：只讀取一次 (放在迴圈外) ---
            res_total = plc.batchread_wordunits(headdevice=self.addr_total, readsize=1)
            res_len = plc.batchread_wordunits(headdevice=self.addr_len, readsize=1)
            
            if res_total and res_len:
                # 成功後立刻發送信號更新 UI
                self.data_ready.emit(res_total[0], res_len[0])
            
            # --- 第三階段：保持連線 (進入無窮迴圈) ---
            print("參數讀取完成，進入持續連線模式...")
            while self.running:
                # 這裡可以放一些簡單的連線檢查 (心跳)
                # 或者單純 sleep，讓執行緒不退出，連線就不會斷
                time.sleep(0.5) 
                
        except Exception as e:
            self.error_occurred.emit(str(e))
        finally:
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
        self.set_default_value() # 預設值
        self.connect_signals() # 按鈕輸入訊號
# """預設值"""
    def set_default_value(self):
        self.server_ip_1.setValue(192)
        self.server_ip_2.setValue(168)
        self.server_ip_3.setValue(1)
        self.server_ip_4.setValue(140)
        self.port_no.setValue(1026)        
        self.max_step_address.setText("D680")
        self.step_length_address.setText("D681")
        self.start_address.setText("D2200")
        self.total_steps.setText("0")
        self.step_length.setText("0")
        self.PB_connect_plc.setEnabled(True)
        self.PB_deconnect_plc.setEnabled(False)
        self.label_connect_status.setText("--離線中--")

# 按鈕輸入訊號
    def connect_signals(self):
        self.PB_connect_plc.clicked.connect(self.connect_plc)
        self.PB_deconnect_plc.clicked.connect(self.deconnect_plc)
        # --- 【新增】連接 Worker 的數據回傳信號 ---
        self.worker.data_ready.connect(self.update_initial_values)
        self.worker.error_occurred.connect(self.handle_error)
# --- 【新增】更新 UI 數值的函式 ---
    @Slot(int, int)
    def update_initial_values(self, total, length):
        self.total_steps.setText(str(total))
        self.step_length.setText(str(length))
        self.label_connect_status.setText("--連線成功且讀取完成--")
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
        self.worker.addr_total = self.max_step_address.text().strip()
        self.worker.addr_len = self.step_length_address.text().strip()
        self.worker.start() # 呼叫 def run(self):
# 斷開PLC
    def deconnect_plc(self):
        self.PB_connect_plc.setEnabled(True)
        self.PB_deconnect_plc.setEnabled(False)
        self.label_connect_status.setText("--離線中--") 
        self.worker.stop()               


if __name__ == "__main__":
    app = QApplication(sys.argv)
    try:
        myWin = MainWindow()
        myWin.show()
        sys.exit(app.exec())
    except Exception as e:
        print(f"啟動失敗: {e}")        
