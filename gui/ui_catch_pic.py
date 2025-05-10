# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'catch_picvWxDaF.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)
import resources_rc,sys
from PySide6 import QtWidgets
from PySide6 import QtCore

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        Form.setEnabled(True)
        Form.resize(555, 623)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 10, 551, 611))
        self.widget.setStyleSheet(u"#widget{\n"
"background-color: rgb(40, 44, 52);\n"
"border: 1px solid rgb(75, 78, 84);  \n"
"border-style: solid;\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#frame QPushButton\n"
"{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 40, 47);\n"
"border: 1px solid rgb(75, 78, 84);\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"\n"
"}\n"
"#frame QPushButton:hover { \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(87, 98, 112, 226), stop:1  rgba(30, 33, 39, 140));\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"}\n"
"#frame QPushButton:pressed {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(87, 98, 112, 226), stop:1  rgba(166, 200, 53,91));\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"}\n"
"/*//////////////////////////////////*/\n"
"#info{\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/*///////////"
                        "/////////////////*/\n"
"\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
" \n"
"	background-color: rgb(75, 78, 84);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScro"
                        "llBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/*//////Horizonital*/\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"   background-color:rgb(75, 78, 84);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     back"
                        "ground: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"\n"
"\n"
"")
        self.info = QLabel(self.widget)
        self.info.setObjectName(u"info")
        self.info.setGeometry(QRect(90, 0, 361, 41))
        font = QFont()
        font.setFamilies([u"Hacen Liner Broadcast HD"])
        font.setPointSize(13)
        self.info.setFont(font)
        self.info.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.info.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.camerawidg = QWidget(self.widget)
        self.camerawidg.setObjectName(u"camerawidg")
        self.camerawidg.setGeometry(QRect(20, 40, 511, 511))
        self.camerav = QGraphicsView(self.camerawidg)
        self.camerav.setObjectName(u"camerav")
        self.camerav.setGeometry(QRect(0, 0, 511, 501))
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 550, 531, 51))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.cancelBtn = QPushButton(self.frame)
        self.cancelBtn.setObjectName(u"cancelBtn")
        self.cancelBtn.setMinimumSize(QSize(10, 35))
        self.cancelBtn.setMaximumSize(QSize(110, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Cocon modified"])
        font1.setPointSize(14)
        self.cancelBtn.setFont(font1)
        self.cancelBtn.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"# QPushButton {\n"
"border: 2px solid rgb(52, 59, 72);\n"
"border-radius: 5px; \n"
"background-color: rgb(52, 59, 72);\n"
"}\n"
"# QPushButton:hover {\n"
"background-color: rgb(57, 65, 80);\n"
"border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#QPushButton:pressed { \n"
"background-color: rgb(35, 40, 49);\n"
"border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.cancelBtn)

        self.horizontalSpacer = QSpacerItem(80, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.okBtn = QPushButton(self.frame)
        self.okBtn.setObjectName(u"okBtn")
        self.okBtn.setMinimumSize(QSize(10, 35))
        self.okBtn.setMaximumSize(QSize(110, 16777215))
        self.okBtn.setFont(font1)
        self.okBtn.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.okBtn)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.info.setText(QCoreApplication.translate("Form", u"     \u0627\u0646\u0638\u0631 \u0627\u0644\u0649 \u0627\u0644\u0643\u0627\u0645\u064a\u0631\u0627 \u0648 \u0642\u0645 \u0628\u0627\u0644\u062a\u0642\u0627\u0637 \u0635\u0648\u0631\u0629 \u0648\u0627\u0636\u062d\u0629 ! ", None))
        self.cancelBtn.setText(QCoreApplication.translate("Form", u"cancel", None))
        self.okBtn.setText(QCoreApplication.translate("Form", u"ok", None))
    # retranslateUi

