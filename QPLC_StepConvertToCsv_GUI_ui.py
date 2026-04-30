# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QPLC_StepConvertToCsv_GUI.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QGroupBox,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpinBox,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 768)
        MainWindow.setStyleSheet(u"background-color: #B5B5B5;")
        self.file_exit = QAction(MainWindow)
        self.file_exit.setObjectName(u"file_exit")
        font = QFont()
        font.setFamilies([u"Microsoft YaHei"])
        font.setPointSize(10)
        self.file_exit.setFont(font)
        self.language_tc = QAction(MainWindow)
        self.language_tc.setObjectName(u"language_tc")
        self.language_tc.setFont(font)
        self.language_sc = QAction(MainWindow)
        self.language_sc.setObjectName(u"language_sc")
        self.language_sc.setFont(font)
        self.language_en = QAction(MainWindow)
        self.language_en.setObjectName(u"language_en")
        self.language_en.setFont(font)
        self.about_version = QAction(MainWindow)
        self.about_version.setObjectName(u"about_version")
        self.about_version.setFont(font)
        self.about_manual = QAction(MainWindow)
        self.about_manual.setObjectName(u"about_manual")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.step_groupBox = QGroupBox(self.centralwidget)
        self.step_groupBox.setObjectName(u"step_groupBox")
        self.step_groupBox.setGeometry(QRect(480, 50, 470, 625))
        self.step_groupBox.setStyleSheet(u"QGroupBox{\n"
"	background-color: transparent;\n"
"}")
        self.step_10 = QLineEdit(self.step_groupBox)
        self.step_10.setObjectName(u"step_10")
        self.step_10.setGeometry(QRect(55, 415, 220, 30))
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei"])
        font1.setPointSize(12)
        self.step_10.setFont(font1)
        self.step_10.setStyleSheet(u"QLineEdit{\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #FFFFFF;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"}")
        self.step_8 = QLineEdit(self.step_groupBox)
        self.step_8.setObjectName(u"step_8")
        self.step_8.setGeometry(QRect(55, 335, 220, 30))
        self.step_8.setFont(font1)
        self.step_8.setStyleSheet(u"QLineEdit{\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #FFFFFF;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"}")
        self.step_7 = QLineEdit(self.step_groupBox)
        self.step_7.setObjectName(u"step_7")
        self.step_7.setGeometry(QRect(55, 295, 220, 30))
        self.step_7.setFont(font1)
        self.step_7.setStyleSheet(u"QLineEdit{\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #FFFFFF;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"}")
        self.step_4 = QLineEdit(self.step_groupBox)
        self.step_4.setObjectName(u"step_4")
        self.step_4.setGeometry(QRect(55, 175, 220, 30))
        self.step_4.setFont(font1)
        self.step_4.setStyleSheet(u"QLineEdit{\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #FFFFFF;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"}")
        self.step_1 = QLineEdit(self.step_groupBox)
        self.step_1.setObjectName(u"step_1")
        self.step_1.setGeometry(QRect(55, 55, 220, 30))
        self.step_1.setFont(font1)
        self.step_1.setStyleSheet(u"QLineEdit{\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #FFFFFF;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"}")
        self.step_2 = QLineEdit(self.step_groupBox)
        self.step_2.setObjectName(u"step_2")
        self.step_2.setGeometry(QRect(55, 95, 220, 30))
        self.step_2.setFont(font1)
        self.step_2.setStyleSheet(u"QLineEdit{\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #FFFFFF;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"}")
        self.step_3 = QLineEdit(self.step_groupBox)
        self.step_3.setObjectName(u"step_3")
        self.step_3.setGeometry(QRect(55, 135, 220, 30))
        self.step_3.setFont(font1)
        self.step_3.setStyleSheet(u"QLineEdit{\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #FFFFFF;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"}")
        self.step_5 = QLineEdit(self.step_groupBox)
        self.step_5.setObjectName(u"step_5")
        self.step_5.setGeometry(QRect(55, 215, 220, 30))
        self.step_5.setFont(font1)
        self.step_5.setStyleSheet(u"QLineEdit{\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #FFFFFF;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"}")
        self.step_9 = QLineEdit(self.step_groupBox)
        self.step_9.setObjectName(u"step_9")
        self.step_9.setGeometry(QRect(55, 375, 220, 30))
        self.step_9.setFont(font1)
        self.step_9.setStyleSheet(u"QLineEdit{\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #FFFFFF;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"}")
        self.step_6 = QLineEdit(self.step_groupBox)
        self.step_6.setObjectName(u"step_6")
        self.step_6.setGeometry(QRect(55, 255, 220, 30))
        self.step_6.setFont(font1)
        self.step_6.setStyleSheet(u"QLineEdit{\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #FFFFFF;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"}")
        self.label_step_no = QLabel(self.step_groupBox)
        self.label_step_no.setObjectName(u"label_step_no")
        self.label_step_no.setEnabled(True)
        self.label_step_no.setGeometry(QRect(10, 15, 40, 30))
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei"])
        font2.setPointSize(14)
        self.label_step_no.setFont(font2)
        self.label_step_no.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_step_no.setStyleSheet(u"QLabel{\n"
"	border-style: solid; \n"
"}")
        self.label_step_no.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.step_no = QSpinBox(self.step_groupBox)
        self.step_no.setObjectName(u"step_no")
        self.step_no.setGeometry(QRect(55, 15, 100, 30))
        font3 = QFont()
        font3.setFamilies([u"Microsoft YaHei"])
        font3.setPointSize(14)
        font3.setBold(False)
        self.step_no.setFont(font3)
        self.step_no.setStyleSheet(u"QSpinBox{\n"
"	border-style: solid;\n"
"	border-width: 1;\n"
"	background-color: white;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"}")
        self.step_no.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.step_no.setKeyboardTracking(True)
        self.step_no.setMaximum(600)
        self.step_no.setSingleStep(1)
        self.step_no.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.PB_step_up = QPushButton(self.step_groupBox)
        self.PB_step_up.setObjectName(u"PB_step_up")
        self.PB_step_up.setGeometry(QRect(285, 55, 40, 40))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PB_step_up.sizePolicy().hasHeightForWidth())
        self.PB_step_up.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setFamilies([u"Microsoft YaHei"])
        font4.setPointSize(14)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.PB_step_up.setFont(font4)
        self.PB_step_up.setStyleSheet(u"/*border-width	\u908a\u6846\u7c97\u7d30	1px, 5px\n"
"border-style	\u908a\u6846\u6a23\u5f0f	solid (\u5be6\u7dda), dashed (\u865b\u7dda), dotted (\u9ede\u7dda)\n"
"border-top-width	\u53ea\u8a2d\u5b9a\u4e0a\u65b9\u908a\u6846	2px\n"
"border-radius	\u5713\u89d2\u7a0b\u5ea6	15px (\u534a\u5f91)\n"
"font-family: \"Microsoft YaHei\";\n"
"font-size: 10; */ \n"
"/* \u5e73\u6642\u7684\u6a23\u5f0f */\n"
"QPushButton {\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #B5B5B5;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"}\n"
"\n"
"/* \u6ed1\u9f20\u79fb\u4e0a\u53bb\u6642 (:hover) */\n"
"/*QPushButton:hover {\n"
"    background-color: #e1f5fe;\n"
"}*/\n"
"\n"
"/* \u6309\u4e0b\u53bb\u7684\u77ac\u9593 (:pressed) */\n"
"QPushButton:pressed {\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #999999;\n"
"	border-top-color: black;\n"
"	border-left-color: black;\n"
"	border-bottom-color: white;\n"
"	bord"
                        "er-right-color: white;\n"
"}")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoUp))
        self.PB_step_up.setIcon(icon)
        self.PB_step_down = QPushButton(self.step_groupBox)
        self.PB_step_down.setObjectName(u"PB_step_down")
        self.PB_step_down.setGeometry(QRect(285, 405, 40, 40))
        sizePolicy.setHeightForWidth(self.PB_step_down.sizePolicy().hasHeightForWidth())
        self.PB_step_down.setSizePolicy(sizePolicy)
        self.PB_step_down.setFont(font4)
        self.PB_step_down.setStyleSheet(u"/*border-width	\u908a\u6846\u7c97\u7d30	1px, 5px\n"
"border-style	\u908a\u6846\u6a23\u5f0f	solid (\u5be6\u7dda), dashed (\u865b\u7dda), dotted (\u9ede\u7dda)\n"
"border-top-width	\u53ea\u8a2d\u5b9a\u4e0a\u65b9\u908a\u6846	2px\n"
"border-radius	\u5713\u89d2\u7a0b\u5ea6	15px (\u534a\u5f91)\n"
"font-family: \"Microsoft YaHei\";\n"
"font-size: 10; */ \n"
"/* \u5e73\u6642\u7684\u6a23\u5f0f */\n"
"QPushButton {\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #B5B5B5;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"}\n"
"\n"
"/* \u6ed1\u9f20\u79fb\u4e0a\u53bb\u6642 (:hover) */\n"
"/*QPushButton:hover {\n"
"    background-color: #e1f5fe;\n"
"}*/\n"
"\n"
"/* \u6309\u4e0b\u53bb\u7684\u77ac\u9593 (:pressed) */\n"
"QPushButton:pressed {\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #999999;\n"
"	border-top-color: black;\n"
"	border-left-color: black;\n"
"	border-bottom-color: white;\n"
"	bord"
                        "er-right-color: white;\n"
"}")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoDown))
        self.PB_step_down.setIcon(icon1)
        self.d150_step_no1 = QSpinBox(self.step_groupBox)
        self.d150_step_no1.setObjectName(u"d150_step_no1")
        self.d150_step_no1.setGeometry(QRect(5, 55, 45, 30))
        self.d150_step_no1.setFont(font3)
        self.d150_step_no1.setStyleSheet(u"QSpinBox{\n"
"	border-style: solid; \n"
"}")
        self.d150_step_no1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.d150_step_no1.setReadOnly(True)
        self.d150_step_no1.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.d150_step_no1.setKeyboardTracking(True)
        self.d150_step_no1.setMinimum(0)
        self.d150_step_no1.setMaximum(600)
        self.d150_step_no1.setSingleStep(1)
        self.d150_step_no1.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.d150_step_no1.setValue(0)
        self.d151_step_no2 = QSpinBox(self.step_groupBox)
        self.d151_step_no2.setObjectName(u"d151_step_no2")
        self.d151_step_no2.setGeometry(QRect(5, 95, 45, 30))
        self.d151_step_no2.setFont(font3)
        self.d151_step_no2.setStyleSheet(u"QSpinBox{\n"
"	border-style: solid; \n"
"}")
        self.d151_step_no2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.d151_step_no2.setReadOnly(True)
        self.d151_step_no2.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.d151_step_no2.setKeyboardTracking(True)
        self.d151_step_no2.setMaximum(600)
        self.d151_step_no2.setSingleStep(1)
        self.d151_step_no2.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.d152_step_no3 = QSpinBox(self.step_groupBox)
        self.d152_step_no3.setObjectName(u"d152_step_no3")
        self.d152_step_no3.setGeometry(QRect(5, 135, 45, 30))
        self.d152_step_no3.setFont(font3)
        self.d152_step_no3.setStyleSheet(u"QSpinBox{\n"
"	border-style: solid; \n"
"}")
        self.d152_step_no3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.d152_step_no3.setReadOnly(True)
        self.d152_step_no3.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.d152_step_no3.setKeyboardTracking(True)
        self.d152_step_no3.setMaximum(600)
        self.d152_step_no3.setSingleStep(1)
        self.d152_step_no3.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.d153_step_no4 = QSpinBox(self.step_groupBox)
        self.d153_step_no4.setObjectName(u"d153_step_no4")
        self.d153_step_no4.setGeometry(QRect(5, 175, 45, 30))
        self.d153_step_no4.setFont(font3)
        self.d153_step_no4.setStyleSheet(u"QSpinBox{\n"
"	border-style: solid; \n"
"}")
        self.d153_step_no4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.d153_step_no4.setReadOnly(True)
        self.d153_step_no4.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.d153_step_no4.setKeyboardTracking(True)
        self.d153_step_no4.setMaximum(600)
        self.d153_step_no4.setSingleStep(1)
        self.d153_step_no4.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.d154_step_no5 = QSpinBox(self.step_groupBox)
        self.d154_step_no5.setObjectName(u"d154_step_no5")
        self.d154_step_no5.setGeometry(QRect(5, 215, 45, 30))
        self.d154_step_no5.setFont(font3)
        self.d154_step_no5.setStyleSheet(u"QSpinBox{\n"
"	border-style: solid; \n"
"}")
        self.d154_step_no5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.d154_step_no5.setReadOnly(True)
        self.d154_step_no5.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.d154_step_no5.setKeyboardTracking(True)
        self.d154_step_no5.setMaximum(600)
        self.d154_step_no5.setSingleStep(1)
        self.d154_step_no5.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.d155_step_no6 = QSpinBox(self.step_groupBox)
        self.d155_step_no6.setObjectName(u"d155_step_no6")
        self.d155_step_no6.setGeometry(QRect(5, 255, 45, 30))
        self.d155_step_no6.setFont(font3)
        self.d155_step_no6.setStyleSheet(u"QSpinBox{\n"
"	border-style: solid; \n"
"}")
        self.d155_step_no6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.d155_step_no6.setReadOnly(True)
        self.d155_step_no6.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.d155_step_no6.setKeyboardTracking(True)
        self.d155_step_no6.setMaximum(600)
        self.d155_step_no6.setSingleStep(1)
        self.d155_step_no6.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.d156_step_no7 = QSpinBox(self.step_groupBox)
        self.d156_step_no7.setObjectName(u"d156_step_no7")
        self.d156_step_no7.setGeometry(QRect(5, 295, 45, 30))
        self.d156_step_no7.setFont(font3)
        self.d156_step_no7.setStyleSheet(u"QSpinBox{\n"
"	border-style: solid; \n"
"}")
        self.d156_step_no7.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.d156_step_no7.setReadOnly(True)
        self.d156_step_no7.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.d156_step_no7.setKeyboardTracking(True)
        self.d156_step_no7.setMaximum(600)
        self.d156_step_no7.setSingleStep(1)
        self.d156_step_no7.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.d157_step_no8 = QSpinBox(self.step_groupBox)
        self.d157_step_no8.setObjectName(u"d157_step_no8")
        self.d157_step_no8.setGeometry(QRect(5, 335, 45, 30))
        self.d157_step_no8.setFont(font3)
        self.d157_step_no8.setStyleSheet(u"QSpinBox{\n"
"	border-style: solid; \n"
"}")
        self.d157_step_no8.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.d157_step_no8.setReadOnly(True)
        self.d157_step_no8.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.d157_step_no8.setKeyboardTracking(True)
        self.d157_step_no8.setMaximum(600)
        self.d157_step_no8.setSingleStep(1)
        self.d157_step_no8.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.d158_step_no9 = QSpinBox(self.step_groupBox)
        self.d158_step_no9.setObjectName(u"d158_step_no9")
        self.d158_step_no9.setGeometry(QRect(5, 375, 45, 30))
        self.d158_step_no9.setFont(font3)
        self.d158_step_no9.setStyleSheet(u"QSpinBox{\n"
"	border-style: solid; \n"
"}")
        self.d158_step_no9.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.d158_step_no9.setReadOnly(True)
        self.d158_step_no9.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.d158_step_no9.setKeyboardTracking(True)
        self.d158_step_no9.setMaximum(600)
        self.d158_step_no9.setSingleStep(1)
        self.d158_step_no9.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.d159_step_no10 = QSpinBox(self.step_groupBox)
        self.d159_step_no10.setObjectName(u"d159_step_no10")
        self.d159_step_no10.setGeometry(QRect(5, 415, 45, 30))
        self.d159_step_no10.setFont(font3)
        self.d159_step_no10.setStyleSheet(u"QSpinBox{\n"
"	border-style: solid; \n"
"}")
        self.d159_step_no10.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.d159_step_no10.setReadOnly(True)
        self.d159_step_no10.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.d159_step_no10.setKeyboardTracking(True)
        self.d159_step_no10.setMaximum(600)
        self.d159_step_no10.setSingleStep(1)
        self.d159_step_no10.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.d159_step_no10.setValue(0)
        self.PB_read_step = QPushButton(self.step_groupBox)
        self.PB_read_step.setObjectName(u"PB_read_step")
        self.PB_read_step.setGeometry(QRect(335, 55, 110, 40))
        sizePolicy.setHeightForWidth(self.PB_read_step.sizePolicy().hasHeightForWidth())
        self.PB_read_step.setSizePolicy(sizePolicy)
        self.PB_read_step.setFont(font4)
        self.PB_read_step.setStyleSheet(u"/*border-width	\u908a\u6846\u7c97\u7d30	1px, 5px\n"
"border-style	\u908a\u6846\u6a23\u5f0f	solid (\u5be6\u7dda), dashed (\u865b\u7dda), dotted (\u9ede\u7dda)\n"
"border-top-width	\u53ea\u8a2d\u5b9a\u4e0a\u65b9\u908a\u6846	2px\n"
"border-radius	\u5713\u89d2\u7a0b\u5ea6	15px (\u534a\u5f91)\n"
"font-family: \"Microsoft YaHei\";\n"
"font-size: 10; */ \n"
"/* \u5e73\u6642\u7684\u6a23\u5f0f */\n"
"QPushButton {\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #B5B5B5;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"}\n"
"\n"
"/* \u6ed1\u9f20\u79fb\u4e0a\u53bb\u6642 (:hover) */\n"
"/*QPushButton:hover {\n"
"    background-color: #e1f5fe;\n"
"}*/\n"
"\n"
"/* \u6309\u4e0b\u53bb\u7684\u77ac\u9593 (:pressed) */\n"
"QPushButton:pressed {\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #999999;\n"
"	border-top-color: black;\n"
"	border-left-color: black;\n"
"	border-bottom-color: white;\n"
"	bord"
                        "er-right-color: white;\n"
"}")
        self.PB_export_csv = QPushButton(self.step_groupBox)
        self.PB_export_csv.setObjectName(u"PB_export_csv")
        self.PB_export_csv.setGeometry(QRect(335, 100, 110, 40))
        sizePolicy.setHeightForWidth(self.PB_export_csv.sizePolicy().hasHeightForWidth())
        self.PB_export_csv.setSizePolicy(sizePolicy)
        self.PB_export_csv.setFont(font4)
        self.PB_export_csv.setStyleSheet(u"/*border-width	\u908a\u6846\u7c97\u7d30	1px, 5px\n"
"border-style	\u908a\u6846\u6a23\u5f0f	solid (\u5be6\u7dda), dashed (\u865b\u7dda), dotted (\u9ede\u7dda)\n"
"border-top-width	\u53ea\u8a2d\u5b9a\u4e0a\u65b9\u908a\u6846	2px\n"
"border-radius	\u5713\u89d2\u7a0b\u5ea6	15px (\u534a\u5f91)\n"
"font-family: \"Microsoft YaHei\";\n"
"font-size: 10; */ \n"
"/* \u5e73\u6642\u7684\u6a23\u5f0f */\n"
"QPushButton {\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #B5B5B5;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"}\n"
"\n"
"/* \u6ed1\u9f20\u79fb\u4e0a\u53bb\u6642 (:hover) */\n"
"/*QPushButton:hover {\n"
"    background-color: #e1f5fe;\n"
"}*/\n"
"\n"
"/* \u6309\u4e0b\u53bb\u7684\u77ac\u9593 (:pressed) */\n"
"QPushButton:pressed {\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #999999;\n"
"	border-top-color: black;\n"
"	border-left-color: black;\n"
"	border-bottom-color: white;\n"
"	bord"
                        "er-right-color: white;\n"
"}")
        self.Process = QTextEdit(self.step_groupBox)
        self.Process.setObjectName(u"Process")
        self.Process.setGeometry(QRect(15, 455, 440, 156))
        self.Process.setFont(font)
        self.Process.setStyleSheet(u"QTextEdit{\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #B5B5B5;\n"
"	border-top-color: black;\n"
"	border-left-color: black;\n"
"	border-bottom-color: white;\n"
"	border-right-color: white;\n"
"}")
        self.setting_groupBox = QGroupBox(self.centralwidget)
        self.setting_groupBox.setObjectName(u"setting_groupBox")
        self.setting_groupBox.setGeometry(QRect(75, 50, 365, 625))
        self.setting_groupBox.setStyleSheet(u"QGroupBox{\n"
"	background-color: transparent;\n"
"}")
        self.plc_setting_groupBox = QGroupBox(self.setting_groupBox)
        self.plc_setting_groupBox.setObjectName(u"plc_setting_groupBox")
        self.plc_setting_groupBox.setGeometry(QRect(50, 10, 266, 241))
        self.plc_setting_groupBox.setFont(font2)
        self.plc_setting_groupBox.setStyleSheet(u"QGroupBox{\n"
"	background-color: transparent;\n"
"}")
        self.plc_setting_groupBox.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_ip4 = QLabel(self.plc_setting_groupBox)
        self.label_ip4.setObjectName(u"label_ip4")
        self.label_ip4.setEnabled(True)
        self.label_ip4.setGeometry(QRect(25, 155, 120, 30))
        self.label_ip4.setFont(font2)
        self.label_ip4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_ip4.setStyleSheet(u"background-color: transparent;")
        self.label_ip4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_ip3 = QLabel(self.plc_setting_groupBox)
        self.label_ip3.setObjectName(u"label_ip3")
        self.label_ip3.setEnabled(True)
        self.label_ip3.setGeometry(QRect(25, 115, 120, 30))
        self.label_ip3.setFont(font2)
        self.label_ip3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_ip3.setStyleSheet(u"background-color: transparent;")
        self.label_ip3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.server_ip_4 = QSpinBox(self.plc_setting_groupBox)
        self.server_ip_4.setObjectName(u"server_ip_4")
        self.server_ip_4.setGeometry(QRect(150, 155, 100, 30))
        self.server_ip_4.setFont(font3)
        self.server_ip_4.setStyleSheet(u"QSpinBox{\n"
"	border-style: solid;\n"
"	border-width: 1;\n"
"	background-color: white;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"}")
        self.server_ip_4.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.server_ip_4.setKeyboardTracking(True)
        self.server_ip_4.setMaximum(255)
        self.server_ip_4.setSingleStep(1)
        self.server_ip_4.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.server_ip_2 = QSpinBox(self.plc_setting_groupBox)
        self.server_ip_2.setObjectName(u"server_ip_2")
        self.server_ip_2.setGeometry(QRect(150, 75, 100, 30))
        self.server_ip_2.setFont(font3)
        self.server_ip_2.setStyleSheet(u"QSpinBox{\n"
"	border-style: solid;\n"
"	border-width: 1;\n"
"	background-color: white;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"}")
        self.server_ip_2.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.server_ip_2.setKeyboardTracking(True)
        self.server_ip_2.setMaximum(255)
        self.server_ip_2.setSingleStep(1)
        self.server_ip_2.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.label_ip1 = QLabel(self.plc_setting_groupBox)
        self.label_ip1.setObjectName(u"label_ip1")
        self.label_ip1.setEnabled(True)
        self.label_ip1.setGeometry(QRect(25, 35, 120, 30))
        self.label_ip1.setFont(font2)
        self.label_ip1.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_ip1.setStyleSheet(u"background-color: transparent;")
        self.label_ip1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.port_no = QSpinBox(self.plc_setting_groupBox)
        self.port_no.setObjectName(u"port_no")
        self.port_no.setGeometry(QRect(150, 195, 100, 30))
        self.port_no.setFont(font3)
        self.port_no.setStyleSheet(u"QSpinBox{\n"
"	border-style: solid;\n"
"	border-width: 1;\n"
"	background-color: white;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"}")
        self.port_no.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.port_no.setKeyboardTracking(True)
        self.port_no.setMinimum(1025)
        self.port_no.setMaximum(4999)
        self.port_no.setSingleStep(1)
        self.port_no.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.label_port = QLabel(self.plc_setting_groupBox)
        self.label_port.setObjectName(u"label_port")
        self.label_port.setEnabled(True)
        self.label_port.setGeometry(QRect(25, 195, 120, 30))
        self.label_port.setFont(font2)
        self.label_port.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_port.setStyleSheet(u"background-color: transparent;")
        self.label_port.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.server_ip_3 = QSpinBox(self.plc_setting_groupBox)
        self.server_ip_3.setObjectName(u"server_ip_3")
        self.server_ip_3.setGeometry(QRect(150, 115, 100, 30))
        self.server_ip_3.setFont(font3)
        self.server_ip_3.setStyleSheet(u"QSpinBox{\n"
"	border-style: solid;\n"
"	border-width: 1;\n"
"	background-color: white;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"}")
        self.server_ip_3.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.server_ip_3.setKeyboardTracking(True)
        self.server_ip_3.setMaximum(255)
        self.server_ip_3.setSingleStep(1)
        self.server_ip_3.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.server_ip_1 = QSpinBox(self.plc_setting_groupBox)
        self.server_ip_1.setObjectName(u"server_ip_1")
        self.server_ip_1.setGeometry(QRect(150, 35, 100, 30))
        self.server_ip_1.setFont(font3)
        self.server_ip_1.setStyleSheet(u"QSpinBox{\n"
"	border-style: solid;\n"
"	border-width: 1;\n"
"	background-color: white;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"}")
        self.server_ip_1.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.server_ip_1.setKeyboardTracking(True)
        self.server_ip_1.setMaximum(255)
        self.server_ip_1.setSingleStep(1)
        self.server_ip_1.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.label_ip2 = QLabel(self.plc_setting_groupBox)
        self.label_ip2.setObjectName(u"label_ip2")
        self.label_ip2.setEnabled(True)
        self.label_ip2.setGeometry(QRect(25, 75, 120, 30))
        self.label_ip2.setFont(font2)
        self.label_ip2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_ip2.setStyleSheet(u"background-color: transparent;")
        self.label_ip2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.PB_connect_plc = QPushButton(self.setting_groupBox)
        self.PB_connect_plc.setObjectName(u"PB_connect_plc")
        self.PB_connect_plc.setGeometry(QRect(25, 470, 150, 40))
        sizePolicy.setHeightForWidth(self.PB_connect_plc.sizePolicy().hasHeightForWidth())
        self.PB_connect_plc.setSizePolicy(sizePolicy)
        self.PB_connect_plc.setFont(font4)
        self.PB_connect_plc.setStyleSheet(u"/*border-width	\u908a\u6846\u7c97\u7d30	1px, 5px\n"
"border-style	\u908a\u6846\u6a23\u5f0f	solid (\u5be6\u7dda), dashed (\u865b\u7dda), dotted (\u9ede\u7dda)\n"
"border-top-width	\u53ea\u8a2d\u5b9a\u4e0a\u65b9\u908a\u6846	2px\n"
"border-radius	\u5713\u89d2\u7a0b\u5ea6	15px (\u534a\u5f91)\n"
"font-family: \"Microsoft YaHei\";\n"
"font-size: 10; */ \n"
"/* \u5e73\u6642\u7684\u6a23\u5f0f */\n"
"QPushButton {\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #B5B5B5;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"}\n"
"\n"
"/* \u6ed1\u9f20\u79fb\u4e0a\u53bb\u6642 (:hover) */\n"
"/*QPushButton:hover {\n"
"    background-color: #e1f5fe;\n"
"}*/\n"
"\n"
"/* \u6309\u4e0b\u53bb\u7684\u77ac\u9593 (:pressed) */\n"
"QPushButton:pressed {\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #999999;\n"
"	border-top-color: black;\n"
"	border-left-color: black;\n"
"	border-bottom-color: white;\n"
"	bord"
                        "er-right-color: white;\n"
"}")
        self.PB_deconnect_plc = QPushButton(self.setting_groupBox)
        self.PB_deconnect_plc.setObjectName(u"PB_deconnect_plc")
        self.PB_deconnect_plc.setEnabled(True)
        self.PB_deconnect_plc.setGeometry(QRect(190, 470, 150, 40))
        sizePolicy.setHeightForWidth(self.PB_deconnect_plc.sizePolicy().hasHeightForWidth())
        self.PB_deconnect_plc.setSizePolicy(sizePolicy)
        self.PB_deconnect_plc.setFont(font4)
        self.PB_deconnect_plc.setStyleSheet(u"/*border-width	\u908a\u6846\u7c97\u7d30	1px, 5px\n"
"border-style	\u908a\u6846\u6a23\u5f0f	solid (\u5be6\u7dda), dashed (\u865b\u7dda), dotted (\u9ede\u7dda)\n"
"border-top-width	\u53ea\u8a2d\u5b9a\u4e0a\u65b9\u908a\u6846	2px\n"
"border-radius	\u5713\u89d2\u7a0b\u5ea6	15px (\u534a\u5f91)\n"
"font-family: \"Microsoft YaHei\";\n"
"font-size: 10; */ \n"
"/* \u5e73\u6642\u7684\u6a23\u5f0f */\n"
"QPushButton {\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #B5B5B5;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"}\n"
"\n"
"/* \u6ed1\u9f20\u79fb\u4e0a\u53bb\u6642 (:hover) */\n"
"/*QPushButton:hover {\n"
"    background-color: #e1f5fe;\n"
"}*/\n"
"\n"
"/* \u6309\u4e0b\u53bb\u7684\u77ac\u9593 (:pressed) */\n"
"QPushButton:pressed {\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #999999;\n"
"	border-top-color: black;\n"
"	border-left-color: black;\n"
"	border-bottom-color: white;\n"
"	bord"
                        "er-right-color: white;\n"
"}")
        self.model_groupBox = QGroupBox(self.setting_groupBox)
        self.model_groupBox.setObjectName(u"model_groupBox")
        self.model_groupBox.setGeometry(QRect(15, 260, 336, 200))
        self.model_groupBox.setFont(font2)
        self.model_groupBox.setStyleSheet(u"QGroupBox{\n"
"	background-color: transparent;\n"
"}")
        self.label_model = QLabel(self.model_groupBox)
        self.label_model.setObjectName(u"label_model")
        self.label_model.setEnabled(True)
        self.label_model.setGeometry(QRect(15, 35, 120, 30))
        self.label_model.setFont(font2)
        self.label_model.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_model.setStyleSheet(u"background-color: transparent;")
        self.label_model.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.model = QComboBox(self.model_groupBox)
        self.model.setObjectName(u"model")
        self.model.setGeometry(QRect(140, 35, 120, 30))
        self.model.setStyleSheet(u"QComboBox{\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: white;\n"
"	border-top-color: black;\n"
"	border-left-color: black;\n"
"	border-bottom-color: white;\n"
"	border-right-color: white;\n"
"	font-family: \"Microsoft YaHei\";\n"
"	font-size: 14pt; \n"
"	color: black;\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u6e05\u55ae */\n"
"QComboBox QAbstractItemView {\n"
"    background-color: white; /* \u6e05\u55ae\u80cc\u666f\u6539\u70ba\u767d\u8272 */\n"
"    selection-background-color: #CCE8FF; /* \u9078\u4e2d\u6642\u8b8a\u6dfa\u85cd\u8272 */\n"
"	font-family: \"Microsoft YaHei\";\n"
"	font-size: 14pt;\n"
"    selection-color: black; /* \u9078\u4e2d\u6642\u6587\u5b57\u7dad\u6301\u9ed1\u8272 */\n"
"    border: 1px solid gray;\n"
"    outline: none;\n"
"}")
        self.model.setEditable(False)
        self.label_total_step = QLabel(self.model_groupBox)
        self.label_total_step.setObjectName(u"label_total_step")
        self.label_total_step.setEnabled(True)
        self.label_total_step.setGeometry(QRect(15, 75, 120, 30))
        self.label_total_step.setFont(font2)
        self.label_total_step.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_total_step.setStyleSheet(u"background-color: transparent;")
        self.label_total_step.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_step_length = QLabel(self.model_groupBox)
        self.label_step_length.setObjectName(u"label_step_length")
        self.label_step_length.setEnabled(True)
        self.label_step_length.setGeometry(QRect(15, 115, 120, 30))
        self.label_step_length.setFont(font2)
        self.label_step_length.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_step_length.setStyleSheet(u"background-color: transparent;")
        self.label_step_length.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.total_step_info = QLabel(self.model_groupBox)
        self.total_step_info.setObjectName(u"total_step_info")
        self.total_step_info.setEnabled(True)
        self.total_step_info.setGeometry(QRect(140, 75, 120, 30))
        self.total_step_info.setFont(font2)
        self.total_step_info.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.total_step_info.setStyleSheet(u"QLabel{\n"
"	background-color: transparent;\n"
"}")
        self.total_step_info.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.step_length_info = QLabel(self.model_groupBox)
        self.step_length_info.setObjectName(u"step_length_info")
        self.step_length_info.setEnabled(True)
        self.step_length_info.setGeometry(QRect(140, 115, 120, 30))
        self.step_length_info.setFont(font2)
        self.step_length_info.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.step_length_info.setStyleSheet(u"QLabel{\n"
"	background-color: transparent;\n"
"}")
        self.step_length_info.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_start_address = QLabel(self.model_groupBox)
        self.label_start_address.setObjectName(u"label_start_address")
        self.label_start_address.setEnabled(True)
        self.label_start_address.setGeometry(QRect(15, 155, 120, 30))
        self.label_start_address.setFont(font2)
        self.label_start_address.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_start_address.setStyleSheet(u"background-color: transparent;")
        self.label_start_address.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.start_address_info = QLabel(self.model_groupBox)
        self.start_address_info.setObjectName(u"start_address_info")
        self.start_address_info.setEnabled(True)
        self.start_address_info.setGeometry(QRect(140, 155, 120, 30))
        self.start_address_info.setFont(font2)
        self.start_address_info.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.start_address_info.setStyleSheet(u"QLabel{\n"
"	background-color: transparent;\n"
"}")
        self.start_address_info.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.response_ts_val = QLabel(self.model_groupBox)
        self.response_ts_val.setObjectName(u"response_ts_val")
        self.response_ts_val.setEnabled(True)
        self.response_ts_val.setGeometry(QRect(295, 75, 30, 30))
        self.response_ts_val.setFont(font)
        self.response_ts_val.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.response_ts_val.setStyleSheet(u"QLabel{\n"
"	background-color: transparent;\n"
"}")
        self.response_ts_val.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.response_sl_val = QLabel(self.model_groupBox)
        self.response_sl_val.setObjectName(u"response_sl_val")
        self.response_sl_val.setEnabled(True)
        self.response_sl_val.setGeometry(QRect(295, 115, 30, 30))
        self.response_sl_val.setFont(font)
        self.response_sl_val.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.response_sl_val.setStyleSheet(u"QLabel{\n"
"	background-color: transparent;\n"
"}")
        self.response_sl_val.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.SM413 = QLabel(self.model_groupBox)
        self.SM413.setObjectName(u"SM413")
        self.SM413.setEnabled(True)
        self.SM413.setGeometry(QRect(295, 160, 30, 30))
        self.SM413.setFont(font2)
        self.SM413.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.SM413.setStyleSheet(u"QLabel{\n"
"	border-style: solid; \n"
"	border-radius: 15px;       /* \u95dc\u9375\uff1a\u534a\u5f91\u8a2d\u70ba\u908a\u9577\u7684\u4e00\u534a */\n"
"	border-width: 1;\n"
"	background-color: #B5B5B5;\n"
"	border-top-color: black;\n"
"	border-left-color: black;\n"
"	border-bottom-color: white;\n"
"	border-right-color: white;\n"
"}")
        self.SM413.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_connect_status = QLabel(self.setting_groupBox)
        self.label_connect_status.setObjectName(u"label_connect_status")
        self.label_connect_status.setEnabled(True)
        self.label_connect_status.setGeometry(QRect(25, 520, 315, 91))
        self.label_connect_status.setFont(font)
        self.label_connect_status.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_connect_status.setStyleSheet(u"QLabel{\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #B5B5B5;\n"
"	border-top-color: black;\n"
"	border-left-color: black;\n"
"	border-bottom-color: white;\n"
"	border-right-color: white;\n"
"}")
        self.label_connect_status.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_pc_ip = QLabel(self.centralwidget)
        self.label_pc_ip.setObjectName(u"label_pc_ip")
        self.label_pc_ip.setEnabled(True)
        self.label_pc_ip.setGeometry(QRect(75, 10, 365, 30))
        self.label_pc_ip.setFont(font)
        self.label_pc_ip.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_pc_ip.setStyleSheet(u"background-color: transparent;")
        self.label_pc_ip.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.setting_groupBox.raise_()
        self.step_groupBox.raise_()
        self.label_pc_ip.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1024, 33))
        self.menubar.setFont(font)
        self.File = QMenu(self.menubar)
        self.File.setObjectName(u"File")
        self.File.setFont(font)
        self.Language = QMenu(self.menubar)
        self.Language.setObjectName(u"Language")
        self.Language.setFont(font)
        self.About = QMenu(self.menubar)
        self.About.setObjectName(u"About")
        self.About.setFont(font)
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.File.menuAction())
        self.menubar.addAction(self.About.menuAction())
        self.menubar.addAction(self.Language.menuAction())
        self.File.addAction(self.file_exit)
        self.Language.addAction(self.language_tc)
        self.Language.addAction(self.language_sc)
        self.Language.addAction(self.language_en)
        self.About.addAction(self.about_manual)
        self.About.addAction(self.about_version)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.file_exit.setText(QCoreApplication.translate("MainWindow", u"\u7d50\u675f(&X)", None))
#if QT_CONFIG(shortcut)
        self.file_exit.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+X", None))
#endif // QT_CONFIG(shortcut)
        self.language_tc.setText(QCoreApplication.translate("MainWindow", u"\u7e41\u9ad4\u4e2d\u6587", None))
        self.language_sc.setText(QCoreApplication.translate("MainWindow", u"\u7b80\u4f53\u4e2d\u6587", None))
        self.language_en.setText(QCoreApplication.translate("MainWindow", u"English", None))
        self.about_version.setText(QCoreApplication.translate("MainWindow", u"\u7248\u672c(&V)", None))
#if QT_CONFIG(shortcut)
        self.about_version.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+V", None))
#endif // QT_CONFIG(shortcut)
        self.about_manual.setText(QCoreApplication.translate("MainWindow", u"\u8aaa\u660e", None))
        self.step_groupBox.setTitle("")
        self.label_step_no.setText(QCoreApplication.translate("MainWindow", u"step", None))
        self.PB_step_up.setText("")
        self.PB_step_down.setText("")
        self.PB_read_step.setText(QCoreApplication.translate("MainWindow", u"\u8b80\u53d6", None))
        self.PB_export_csv.setText(QCoreApplication.translate("MainWindow", u"Export .csv", None))
        self.setting_groupBox.setTitle("")
        self.plc_setting_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"PLC connection settings", None))
        self.label_ip4.setText(QCoreApplication.translate("MainWindow", u"Server  IP4", None))
        self.label_ip3.setText(QCoreApplication.translate("MainWindow", u"Server  IP3", None))
        self.label_ip1.setText(QCoreApplication.translate("MainWindow", u"Server  IP1", None))
        self.label_port.setText(QCoreApplication.translate("MainWindow", u"Port No", None))
        self.label_ip2.setText(QCoreApplication.translate("MainWindow", u"Server  IP2", None))
        self.PB_connect_plc.setText(QCoreApplication.translate("MainWindow", u"\u9023\u7dda", None))
        self.PB_deconnect_plc.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.model_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Format setting", None))
        self.label_model.setText(QCoreApplication.translate("MainWindow", u"Model", None))
        self.model.setCurrentText("")
        self.label_total_step.setText(QCoreApplication.translate("MainWindow", u"Total steps", None))
        self.label_step_length.setText(QCoreApplication.translate("MainWindow", u"Step length", None))
        self.total_step_info.setText(QCoreApplication.translate("MainWindow", u": [D680 , 500]", None))
        self.step_length_info.setText(QCoreApplication.translate("MainWindow", u": [D681 , 20]", None))
        self.label_start_address.setText(QCoreApplication.translate("MainWindow", u"Start address", None))
        self.start_address_info.setText(QCoreApplication.translate("MainWindow", u": [D2200]", None))
        self.response_ts_val.setText(QCoreApplication.translate("MainWindow", u"500", None))
        self.response_sl_val.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.SM413.setText("")
        self.label_connect_status.setText(QCoreApplication.translate("MainWindow", u"\u5df2\u9023\u7dda", None))
        self.label_pc_ip.setText(QCoreApplication.translate("MainWindow", u"PC IP:", None))
        self.File.setTitle(QCoreApplication.translate("MainWindow", u"\u6a94\u6848", None))
        self.Language.setTitle(QCoreApplication.translate("MainWindow", u"\u8a9e\u8a00", None))
        self.About.setTitle(QCoreApplication.translate("MainWindow", u"\u95dc\u65bc", None))
    # retranslateUi

