# utils.py
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

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