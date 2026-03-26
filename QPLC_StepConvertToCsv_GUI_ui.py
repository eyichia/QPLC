# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QPLC_StepConvertToCsv_GUI.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QFrame, QGroupBox,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpinBox, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 768)
        MainWindow.setStyleSheet(u"background-color: #B5B5B5;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.PB_read_step = QPushButton(self.centralwidget)
        self.PB_read_step.setObjectName(u"PB_read_step")
        self.PB_read_step.setGeometry(QRect(420, 80, 110, 40))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PB_read_step.sizePolicy().hasHeightForWidth())
        self.PB_read_step.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Microsoft YaHei"])
        font.setPointSize(14)
        font.setStyleStrategy(QFont.PreferDefault)
        self.PB_read_step.setFont(font)
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
        self.PB_export_csv = QPushButton(self.centralwidget)
        self.PB_export_csv.setObjectName(u"PB_export_csv")
        self.PB_export_csv.setGeometry(QRect(420, 460, 110, 40))
        sizePolicy.setHeightForWidth(self.PB_export_csv.sizePolicy().hasHeightForWidth())
        self.PB_export_csv.setSizePolicy(sizePolicy)
        self.PB_export_csv.setFont(font)
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
        self.PB_write_step = QPushButton(self.centralwidget)
        self.PB_write_step.setObjectName(u"PB_write_step")
        self.PB_write_step.setGeometry(QRect(420, 125, 110, 40))
        sizePolicy.setHeightForWidth(self.PB_write_step.sizePolicy().hasHeightForWidth())
        self.PB_write_step.setSizePolicy(sizePolicy)
        self.PB_write_step.setFont(font)
        self.PB_write_step.setStyleSheet(u"/*border-width	\u908a\u6846\u7c97\u7d30	1px, 5px\n"
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
        self.PB_import_csv = QPushButton(self.centralwidget)
        self.PB_import_csv.setObjectName(u"PB_import_csv")
        self.PB_import_csv.setGeometry(QRect(420, 505, 110, 40))
        sizePolicy.setHeightForWidth(self.PB_import_csv.sizePolicy().hasHeightForWidth())
        self.PB_import_csv.setSizePolicy(sizePolicy)
        self.PB_import_csv.setFont(font)
        self.PB_import_csv.setStyleSheet(u"/*border-width	\u908a\u6846\u7c97\u7d30	1px, 5px\n"
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
        self.step_groupBox = QGroupBox(self.centralwidget)
        self.step_groupBox.setObjectName(u"step_groupBox")
        self.step_groupBox.setGeometry(QRect(565, 80, 296, 466))
        self.step_groupBox.setStyleSheet(u"QGroupBox{\n"
"	background-color: transparent;\n"
"}")
        self.step_10 = QLineEdit(self.step_groupBox)
        self.step_10.setObjectName(u"step_10")
        self.step_10.setGeometry(QRect(55, 415, 220, 30))
        self.step_10.setStyleSheet(u"QLineEdit{\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #FFFFFF;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"}")
        self.label_step_no_3 = QLabel(self.step_groupBox)
        self.label_step_no_3.setObjectName(u"label_step_no_3")
        self.label_step_no_3.setEnabled(True)
        self.label_step_no_3.setGeometry(QRect(10, 135, 40, 30))
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei"])
        font1.setPointSize(14)
        self.label_step_no_3.setFont(font1)
        self.label_step_no_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_step_no_3.setStyleSheet(u"QLabel{\n"
"	border-style: solid; \n"
"}")
        self.label_step_no_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_step_no_4 = QLabel(self.step_groupBox)
        self.label_step_no_4.setObjectName(u"label_step_no_4")
        self.label_step_no_4.setEnabled(True)
        self.label_step_no_4.setGeometry(QRect(10, 175, 40, 30))
        self.label_step_no_4.setFont(font1)
        self.label_step_no_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_step_no_4.setStyleSheet(u"QLabel{\n"
"	border-style: solid; \n"
"}")
        self.label_step_no_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_step_no_6 = QLabel(self.step_groupBox)
        self.label_step_no_6.setObjectName(u"label_step_no_6")
        self.label_step_no_6.setEnabled(True)
        self.label_step_no_6.setGeometry(QRect(10, 255, 40, 30))
        self.label_step_no_6.setFont(font1)
        self.label_step_no_6.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_step_no_6.setStyleSheet(u"QLabel{\n"
"	border-style: solid; \n"
"}")
        self.label_step_no_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_step_no_8 = QLabel(self.step_groupBox)
        self.label_step_no_8.setObjectName(u"label_step_no_8")
        self.label_step_no_8.setEnabled(True)
        self.label_step_no_8.setGeometry(QRect(10, 335, 40, 30))
        self.label_step_no_8.setFont(font1)
        self.label_step_no_8.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_step_no_8.setStyleSheet(u"QLabel{\n"
"	border-style: solid; \n"
"}")
        self.label_step_no_8.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.step_8 = QLineEdit(self.step_groupBox)
        self.step_8.setObjectName(u"step_8")
        self.step_8.setGeometry(QRect(55, 335, 220, 30))
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
        self.step_7.setStyleSheet(u"QLineEdit{\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #FFFFFF;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"}")
        self.label_step_no_7 = QLabel(self.step_groupBox)
        self.label_step_no_7.setObjectName(u"label_step_no_7")
        self.label_step_no_7.setEnabled(True)
        self.label_step_no_7.setGeometry(QRect(10, 295, 40, 30))
        self.label_step_no_7.setFont(font1)
        self.label_step_no_7.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_step_no_7.setStyleSheet(u"QLabel{\n"
"	border-style: solid; \n"
"}")
        self.label_step_no_7.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_step_no_10 = QLabel(self.step_groupBox)
        self.label_step_no_10.setObjectName(u"label_step_no_10")
        self.label_step_no_10.setEnabled(True)
        self.label_step_no_10.setGeometry(QRect(10, 415, 40, 30))
        self.label_step_no_10.setFont(font1)
        self.label_step_no_10.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_step_no_10.setStyleSheet(u"QLabel{\n"
"	border-style: solid; \n"
"}")
        self.label_step_no_10.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_step_no_5 = QLabel(self.step_groupBox)
        self.label_step_no_5.setObjectName(u"label_step_no_5")
        self.label_step_no_5.setEnabled(True)
        self.label_step_no_5.setGeometry(QRect(10, 215, 40, 30))
        self.label_step_no_5.setFont(font1)
        self.label_step_no_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_step_no_5.setStyleSheet(u"QLabel{\n"
"	border-style: solid; \n"
"}")
        self.label_step_no_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.step_4 = QLineEdit(self.step_groupBox)
        self.step_4.setObjectName(u"step_4")
        self.step_4.setGeometry(QRect(55, 175, 220, 30))
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
        self.step_3.setStyleSheet(u"QLineEdit{\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #FFFFFF;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"}")
        self.label_step_no_1 = QLabel(self.step_groupBox)
        self.label_step_no_1.setObjectName(u"label_step_no_1")
        self.label_step_no_1.setEnabled(True)
        self.label_step_no_1.setGeometry(QRect(10, 55, 40, 30))
        self.label_step_no_1.setFont(font1)
        self.label_step_no_1.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_step_no_1.setStyleSheet(u"QLabel{\n"
"	border-style: solid; \n"
"}")
        self.label_step_no_1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_step_no_2 = QLabel(self.step_groupBox)
        self.label_step_no_2.setObjectName(u"label_step_no_2")
        self.label_step_no_2.setEnabled(True)
        self.label_step_no_2.setGeometry(QRect(10, 95, 40, 30))
        self.label_step_no_2.setFont(font1)
        self.label_step_no_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_step_no_2.setStyleSheet(u"QLabel{\n"
"	border-style: solid; \n"
"}")
        self.label_step_no_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.step_5 = QLineEdit(self.step_groupBox)
        self.step_5.setObjectName(u"step_5")
        self.step_5.setGeometry(QRect(55, 215, 220, 30))
        self.step_5.setStyleSheet(u"QLineEdit{\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #FFFFFF;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"}")
        self.label_step_no_9 = QLabel(self.step_groupBox)
        self.label_step_no_9.setObjectName(u"label_step_no_9")
        self.label_step_no_9.setEnabled(True)
        self.label_step_no_9.setGeometry(QRect(10, 375, 40, 30))
        self.label_step_no_9.setFont(font1)
        self.label_step_no_9.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_step_no_9.setStyleSheet(u"QLabel{\n"
"	border-style: solid; \n"
"}")
        self.label_step_no_9.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.step_9 = QLineEdit(self.step_groupBox)
        self.step_9.setObjectName(u"step_9")
        self.step_9.setGeometry(QRect(55, 375, 220, 30))
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
        self.label_step_no.setFont(font1)
        self.label_step_no.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_step_no.setStyleSheet(u"QLabel{\n"
"	border-style: solid; \n"
"}")
        self.label_step_no.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.step_no = QSpinBox(self.step_groupBox)
        self.step_no.setObjectName(u"step_no")
        self.step_no.setGeometry(QRect(55, 15, 100, 30))
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei"])
        font2.setPointSize(14)
        font2.setBold(False)
        self.step_no.setFont(font2)
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
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(470, 50, 10, 525))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.setting_groupBox = QGroupBox(self.centralwidget)
        self.setting_groupBox.setObjectName(u"setting_groupBox")
        self.setting_groupBox.setGeometry(QRect(20, 50, 365, 525))
        self.setting_groupBox.setStyleSheet(u"QGroupBox{\n"
"	background-color: transparent;\n"
"}")
        self.plc_setting_groupBox = QGroupBox(self.setting_groupBox)
        self.plc_setting_groupBox.setObjectName(u"plc_setting_groupBox")
        self.plc_setting_groupBox.setGeometry(QRect(50, 10, 266, 241))
        self.plc_setting_groupBox.setFont(font1)
        self.plc_setting_groupBox.setStyleSheet(u"QGroupBox{\n"
"	background-color: transparent;\n"
"}")
        self.plc_setting_groupBox.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_ip4 = QLabel(self.plc_setting_groupBox)
        self.label_ip4.setObjectName(u"label_ip4")
        self.label_ip4.setEnabled(True)
        self.label_ip4.setGeometry(QRect(25, 155, 120, 30))
        self.label_ip4.setFont(font1)
        self.label_ip4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_ip4.setStyleSheet(u"background-color: transparent;")
        self.label_ip4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_ip3 = QLabel(self.plc_setting_groupBox)
        self.label_ip3.setObjectName(u"label_ip3")
        self.label_ip3.setEnabled(True)
        self.label_ip3.setGeometry(QRect(25, 115, 120, 30))
        self.label_ip3.setFont(font1)
        self.label_ip3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_ip3.setStyleSheet(u"background-color: transparent;")
        self.label_ip3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.server_ip_4 = QSpinBox(self.plc_setting_groupBox)
        self.server_ip_4.setObjectName(u"server_ip_4")
        self.server_ip_4.setGeometry(QRect(150, 155, 100, 30))
        self.server_ip_4.setFont(font2)
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
        self.server_ip_2.setFont(font2)
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
        self.label_ip1.setFont(font1)
        self.label_ip1.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_ip1.setStyleSheet(u"background-color: transparent;")
        self.label_ip1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.port_no = QSpinBox(self.plc_setting_groupBox)
        self.port_no.setObjectName(u"port_no")
        self.port_no.setGeometry(QRect(150, 195, 100, 30))
        self.port_no.setFont(font2)
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
        self.label_port.setFont(font1)
        self.label_port.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_port.setStyleSheet(u"background-color: transparent;")
        self.label_port.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.server_ip_3 = QSpinBox(self.plc_setting_groupBox)
        self.server_ip_3.setObjectName(u"server_ip_3")
        self.server_ip_3.setGeometry(QRect(150, 115, 100, 30))
        self.server_ip_3.setFont(font2)
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
        self.server_ip_1.setFont(font2)
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
        self.label_ip2.setFont(font1)
        self.label_ip2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_ip2.setStyleSheet(u"background-color: transparent;")
        self.label_ip2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.step_setting_groupBox = QGroupBox(self.setting_groupBox)
        self.step_setting_groupBox.setObjectName(u"step_setting_groupBox")
        self.step_setting_groupBox.setGeometry(QRect(15, 260, 336, 161))
        self.step_setting_groupBox.setFont(font1)
        self.step_setting_groupBox.setStyleSheet(u"QGroupBox{\n"
"	background-color: transparent;\n"
"}")
        self.label_max_step = QLabel(self.step_setting_groupBox)
        self.label_max_step.setObjectName(u"label_max_step")
        self.label_max_step.setEnabled(True)
        self.label_max_step.setGeometry(QRect(25, 35, 120, 30))
        self.label_max_step.setFont(font1)
        self.label_max_step.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_max_step.setStyleSheet(u"background-color: transparent;")
        self.label_max_step.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_step_length = QLabel(self.step_setting_groupBox)
        self.label_step_length.setObjectName(u"label_step_length")
        self.label_step_length.setEnabled(True)
        self.label_step_length.setGeometry(QRect(25, 75, 120, 30))
        self.label_step_length.setFont(font1)
        self.label_step_length.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_step_length.setStyleSheet(u"background-color: transparent;")
        self.label_step_length.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_start_address = QLabel(self.step_setting_groupBox)
        self.label_start_address.setObjectName(u"label_start_address")
        self.label_start_address.setEnabled(True)
        self.label_start_address.setGeometry(QRect(25, 115, 120, 30))
        self.label_start_address.setFont(font1)
        self.label_start_address.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_start_address.setStyleSheet(u"background-color: transparent;")
        self.label_start_address.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.start_address = QLineEdit(self.step_setting_groupBox)
        self.start_address.setObjectName(u"start_address")
        self.start_address.setGeometry(QRect(150, 115, 100, 30))
        self.start_address.setFont(font1)
        self.start_address.setStyleSheet(u"QLineEdit{\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #FFFFFF;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"}")
        self.max_step_address = QLineEdit(self.step_setting_groupBox)
        self.max_step_address.setObjectName(u"max_step_address")
        self.max_step_address.setGeometry(QRect(150, 35, 100, 30))
        self.max_step_address.setFont(font1)
        self.max_step_address.setStyleSheet(u"QLineEdit{\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #FFFFFF;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"}")
        self.step_length_address = QLineEdit(self.step_setting_groupBox)
        self.step_length_address.setObjectName(u"step_length_address")
        self.step_length_address.setGeometry(QRect(150, 75, 100, 30))
        self.step_length_address.setFont(font1)
        self.step_length_address.setStyleSheet(u"QLineEdit{\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #FFFFFF;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"}")
        self.total_steps = QLabel(self.step_setting_groupBox)
        self.total_steps.setObjectName(u"total_steps")
        self.total_steps.setEnabled(True)
        self.total_steps.setGeometry(QRect(260, 35, 60, 30))
        self.total_steps.setFont(font1)
        self.total_steps.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.total_steps.setStyleSheet(u"QLabel{\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #B5B5B5;\n"
"	border-top-color: black;\n"
"	border-left-color: black;\n"
"	border-bottom-color: white;\n"
"	border-right-color: white;\n"
"}")
        self.total_steps.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.step_length = QLabel(self.step_setting_groupBox)
        self.step_length.setObjectName(u"step_length")
        self.step_length.setEnabled(True)
        self.step_length.setGeometry(QRect(260, 75, 60, 30))
        self.step_length.setFont(font1)
        self.step_length.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.step_length.setStyleSheet(u"QLabel{\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #B5B5B5;\n"
"	border-top-color: black;\n"
"	border-left-color: black;\n"
"	border-bottom-color: white;\n"
"	border-right-color: white;\n"
"}")
        self.step_length.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.PB_connect_plc = QPushButton(self.setting_groupBox)
        self.PB_connect_plc.setObjectName(u"PB_connect_plc")
        self.PB_connect_plc.setGeometry(QRect(25, 430, 150, 40))
        sizePolicy.setHeightForWidth(self.PB_connect_plc.sizePolicy().hasHeightForWidth())
        self.PB_connect_plc.setSizePolicy(sizePolicy)
        self.PB_connect_plc.setFont(font)
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
        self.PB_deconnect_plc.setGeometry(QRect(190, 430, 150, 40))
        sizePolicy.setHeightForWidth(self.PB_deconnect_plc.sizePolicy().hasHeightForWidth())
        self.PB_deconnect_plc.setSizePolicy(sizePolicy)
        self.PB_deconnect_plc.setFont(font)
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
        self.label_connect_status = QLabel(self.setting_groupBox)
        self.label_connect_status.setObjectName(u"label_connect_status")
        self.label_connect_status.setEnabled(True)
        self.label_connect_status.setGeometry(QRect(25, 480, 150, 30))
        self.label_connect_status.setFont(font1)
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
        self.label_sm413 = QLabel(self.setting_groupBox)
        self.label_sm413.setObjectName(u"label_sm413")
        self.label_sm413.setEnabled(True)
        self.label_sm413.setGeometry(QRect(190, 480, 70, 30))
        self.label_sm413.setFont(font1)
        self.label_sm413.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_sm413.setStyleSheet(u"background-color: transparent;")
        self.label_sm413.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.SM413 = QLabel(self.setting_groupBox)
        self.SM413.setObjectName(u"SM413")
        self.SM413.setEnabled(True)
        self.SM413.setGeometry(QRect(270, 480, 30, 30))
        self.SM413.setFont(font1)
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.setting_groupBox.raise_()
        self.line.raise_()
        self.PB_read_step.raise_()
        self.PB_export_csv.raise_()
        self.PB_write_step.raise_()
        self.PB_import_csv.raise_()
        self.step_groupBox.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1024, 21))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.PB_read_step.setText(QCoreApplication.translate("MainWindow", u"\u8b80\u53d6", None))
        self.PB_export_csv.setText(QCoreApplication.translate("MainWindow", u"Export .csv", None))
        self.PB_write_step.setText(QCoreApplication.translate("MainWindow", u"\u5beb\u5165", None))
        self.PB_import_csv.setText(QCoreApplication.translate("MainWindow", u"Import .csv", None))
        self.step_groupBox.setTitle("")
        self.label_step_no_3.setText(QCoreApplication.translate("MainWindow", u"999", None))
        self.label_step_no_4.setText(QCoreApplication.translate("MainWindow", u"999", None))
        self.label_step_no_6.setText(QCoreApplication.translate("MainWindow", u"999", None))
        self.label_step_no_8.setText(QCoreApplication.translate("MainWindow", u"999", None))
        self.label_step_no_7.setText(QCoreApplication.translate("MainWindow", u"999", None))
        self.label_step_no_10.setText(QCoreApplication.translate("MainWindow", u"999", None))
        self.label_step_no_5.setText(QCoreApplication.translate("MainWindow", u"999", None))
        self.label_step_no_1.setText(QCoreApplication.translate("MainWindow", u"999", None))
        self.label_step_no_2.setText(QCoreApplication.translate("MainWindow", u"999", None))
        self.label_step_no_9.setText(QCoreApplication.translate("MainWindow", u"999", None))
        self.label_step_no.setText(QCoreApplication.translate("MainWindow", u"step", None))
        self.setting_groupBox.setTitle("")
        self.plc_setting_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"PLC connection settings", None))
        self.label_ip4.setText(QCoreApplication.translate("MainWindow", u"Server  IP4", None))
        self.label_ip3.setText(QCoreApplication.translate("MainWindow", u"Server  IP3", None))
        self.label_ip1.setText(QCoreApplication.translate("MainWindow", u"Server  IP1", None))
        self.label_port.setText(QCoreApplication.translate("MainWindow", u"Port No", None))
        self.label_ip2.setText(QCoreApplication.translate("MainWindow", u"Server  IP2", None))
        self.step_setting_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Step format settings", None))
        self.label_max_step.setText(QCoreApplication.translate("MainWindow", u"Total steps", None))
        self.label_step_length.setText(QCoreApplication.translate("MainWindow", u"Step length", None))
        self.label_start_address.setText(QCoreApplication.translate("MainWindow", u"Start address", None))
        self.start_address.setText(QCoreApplication.translate("MainWindow", u"D2000", None))
        self.max_step_address.setText(QCoreApplication.translate("MainWindow", u"D680", None))
        self.step_length_address.setText(QCoreApplication.translate("MainWindow", u"D681", None))
        self.total_steps.setText(QCoreApplication.translate("MainWindow", u"999", None))
        self.step_length.setText(QCoreApplication.translate("MainWindow", u"999", None))
        self.PB_connect_plc.setText(QCoreApplication.translate("MainWindow", u"\u9023\u7dda", None))
        self.PB_deconnect_plc.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.label_connect_status.setText(QCoreApplication.translate("MainWindow", u"\u5df2\u9023\u7dda", None))
        self.label_sm413.setText(QCoreApplication.translate("MainWindow", u"SM413", None))
        self.SM413.setText("")
    # retranslateUi

