import sys
import time
import pymcprotocol

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QThread, Signal, Slot
from QPLC_StepConvertToCsv_GUI_ui import Ui_Form

class PLCWorker(QThread):
    """
    背景執行緒處理 PLC 連線及讀取，避免阻塞主介面
    """
    data_ready = Signal(float)

    def __init__(self):
        super().__init__()
        self.ip = ""
        self.port = 0
        self.running = True

    def run(self):
        plc = None
        current_ip = ""
        current_port = 0

        while self.running:
            if not self.ip or self.port <= 0:
                time.sleep(1)
                continue

            # 如果 IP 或 Port 改變，重新連線
            if current_ip != self.ip or current_port != self.port:
                if plc is not None:
                    try:
                        plc.close()
                    except:
                        pass
                
                plc = pymcprotocol.Type3E()
                plc.setaccessopt(commtype="binary")
                
                current_ip = self.ip
                current_port = self.port
                
                try:
                    # 嘗試與 PLC 進行連線
                    plc.connect(current_ip, current_port)
                except Exception as e:
                    plc = None
                    print(f"Connection failed: {e}")
                    time.sleep(0.1)
                    continue

            # 若有成功連線，則進行資料讀取
            if plc is not None:
                try:
                    # 讀取 D200 暫存器 (Batch read from head device)
                    # readsize=1 代表讀取 1 個 word
                    values = plc.batchread_wordunits(headdevice="D200", readsize=1)
                    if values:
                        self.data_ready.emit(float(values[0]))
                except Exception as e:
                    print(f"Read error: {e}")
                    try:
                        plc.close()
                    except:
                        pass
                    plc = None
            
            # 每 100ms 輪詢一次
            time.sleep(0.1)

    def stop(self):
        self.running = False
        self.wait()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 設定背景執行緒
        self.worker = PLCWorker()
        self.worker.data_ready.connect(self.update_d200)
        
        # 綁定 UI 的事件：當文字或數值改變時，將設定同步給 worker
        self.ui.IP.textChanged.connect(self.update_connection_info)
        self.ui.PortNo.valueChanged.connect(self.update_connection_info)
        
        # 初始同步一下當前輸入框的值
        self.update_connection_info()
        
        # 啟動背景執行緒
        self.worker.start()

    @Slot()
    def update_connection_info(self):
        self.worker.ip = self.ui.IP.text().strip()
        self.worker.port = self.ui.PortNo.value()

    @Slot(float)
    def update_d200(self, val):
        self.ui.D00200.setValue(val)

    def closeEvent(self, event):
        """
        關閉視窗時也要記得停止背景執行緒，避免程式卡在背景
        """
        self.worker.stop()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
