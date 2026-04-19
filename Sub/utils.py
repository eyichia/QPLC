import struct
# utils.py
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

# 自訂視窗
def show_prompt_window(parent, _title, _text, _icon=None, _buttons=None, _theme="default", _font_size=14, _icon_size=80):
    """
    跨檔案使用的萬用對話框
    :param parent: 呼叫此對話框的父視窗 (通常是主視窗的 self)
    """
    msg = QMessageBox(parent) # 改用傳進來的 parent
    msg.setWindowTitle(_title)
    combined_text = f"""
        <div style = 'font-family: "Microsoft YaHei";
            font-size: {_font_size}pt;
            color: black;
            padding: 10px;'>
            {_text}
        </div>        
    """
    msg.setText(combined_text)

    # 圖示處理
    if isinstance(_icon, QPixmap):
        msg.setIconPixmap(_icon.scaled(_icon_size, _icon_size, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
    elif _icon:
        msg.setIcon(_icon)
    
    # 按鈕處理
    if _buttons:
        msg.setStandardButtons(_buttons)
    else:
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)

    # 樣式處理 (這裡可以根據你的需求繼續擴充)
    color_styles = {
        "default": "#B5B5B5", # 灰色
        "alarm": "#FFFF00",  # 黃色 (警告用)
        "success": "#CCFFCC"  # 淡綠色 (成功用)
    }
    bg_color = color_styles.get(_theme, "#B5B5B5")

    msg.setStyleSheet(f"""
        QMessageBox {{ 
            background-color: {bg_color};
            font-family: "Microsoft YaHei";
            font-size: {_font_size}pt;
            color: black;
        }}
        QLabel {{
            background-color: transparent; /* 確保所有文字和圖示標籤背景透明 */
        }}
        QPushButton {{ 
            border-style: solid; 
	        border-width: 1;
	        background-color: #B5B5B5;
	        border-top-color: white;
	        border-left-color: white;
	        border-bottom-color: black;
	        border-right-color: black;          
            font-family: "Microsoft YaHei";
            font-size: 14pt;
            min-width: 80px;
            height: 28px;
        }}
        QPushButton:pressed {{
	        border-style: solid; 
	        border-width: 1;
	        background-color: #999999;
	        border-top-color: black;
	        border-left-color: black;
	        border-bottom-color: white;
	        border-right-color: white;
        }}
    """)
    
    
    
    return msg.exec()
# 16bitTo32bit轉換
def convert_16_to_32(low, high):
    # 先轉16進制(無符號)
    low_u = low & 0xFFFF
    high_u = high & 0xFFFF
    # 將兩個 16-bit 數字合併成一個 32-bit 數字
    combined = (high_u << 16) | low_u
    # 如果最高位是 1，表示這是一個負數，進行符號擴展
    if combined >= 0x80000000:
        combined -= 0x100000000
    return combined  
# 16bit有符號轉換 (PLC裡的數字如果大於32767就代表是負數，要轉換成Python的負數表示法)      
def convert_16bit_signed(value):
    # 如果大於 32767，代表在 PLC 裡是負數
    if value > 32767:
        return value - 65536
    return value    
# 轉字串
def to_str(_data, _start, _stop, encoding='ascii'):
    label_words = _data[_start : _stop]
    byte_data = struct.pack(f'<{len(label_words)}H', *label_words)   
    # 增加 encoding 參數，預設還是 ascii 讀繁體中文 encoding='big5'
    _string = byte_data.decode(encoding, errors='ignore').strip('\x00')
    return _string    