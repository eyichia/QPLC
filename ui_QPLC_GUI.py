# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QPLC_GUI.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDoubleSpinBox, QLabel,
    QLineEdit, QSizePolicy, QSpinBox, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 600)
        font = QFont()
        font.setFamilies([u"Microsoft YaHei"])
        font.setPointSize(14)
        Form.setFont(font)
        Form.setStyleSheet(u"background-color: #B5B5B5;")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setGeometry(QRect(70, 30, 80, 30))
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label.setStyleSheet(u"background-color: transparent;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QRect(70, 80, 80, 30))
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_2.setStyleSheet(u"background-color: transparent;")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.PortNo = QSpinBox(Form)
        self.PortNo.setObjectName(u"PortNo")
        self.PortNo.setGeometry(QRect(155, 80, 120, 30))
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei"])
        font1.setPointSize(14)
        font1.setBold(False)
        self.PortNo.setFont(font1)
        self.PortNo.setStyleSheet(u"QSpinBox{\n"
"	border-style: solid;\n"
"	border-width: 1;\n"
"	background-color: white;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"}")
        self.PortNo.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.PortNo.setKeyboardTracking(True)
        self.PortNo.setMaximum(9999)
        self.PortNo.setSingleStep(3)
        self.PortNo.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.IP = QLineEdit(Form)
        self.IP.setObjectName(u"IP")
        self.IP.setGeometry(QRect(155, 30, 160, 30))
        self.IP.setFont(font)
        self.IP.setStyleSheet(u"QLineEdit{\n"
"	border-style: solid;\n"
"	border-width: 1;\n"
"	background-color: white;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"}")
        self.IP.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.D00200 = QDoubleSpinBox(Form)
        self.D00200.setObjectName(u"D00200")
        self.D00200.setGeometry(QRect(155, 130, 120, 30))
        self.D00200.setFont(font)
        self.D00200.setStyleSheet(u"QDoubleSpinBox{\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #B5B5B5;\n"
"	border-top-color: black;\n"
"	border-left-color: black;\n"
"	border-bottom-color: white;\n"
"	border-right-color: white;\n"
"}")
        self.D00200.setInputMethodHints(Qt.InputMethodHint.ImhFormattedNumbersOnly)
        self.D00200.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.D00200.setReadOnly(True)
        self.D00200.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.D00200.setDecimals(0)
        self.D00200.setMinimum(0.000000000000000)
        self.D00200.setMaximum(99999.000000000000000)
        self.D00200.setSingleStep(0.000100000000000)
        self.D00200.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.D00200.setValue(0.000000000000000)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QRect(70, 130, 80, 30))
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_3.setStyleSheet(u"background-color: transparent;")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"IP", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Port", None))
        self.IP.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"D200", None))
    # retranslateUi

