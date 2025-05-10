# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'doexammBzSip.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QGridLayout,
    QLCDNumber, QLabel, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_examwidgete(object):
    def setupUi(self, examwidgete):
        if not examwidgete.objectName():
            examwidgete.setObjectName(u"examwidgete")
        examwidgete.resize(870, 559)
        examwidgete.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        examwidgete.setStyleSheet(u"/*/////////widget////////////////////////*/\n"
"*{\n"
"background-color: rgb(40, 44, 52);\n"
"color:(255,255,255);\n"
"}\n"
"#lcdNumber{\n"
"background-color: rgb(55, 63, 77);\n"
"border-radius:10px; }\n"
"\n"
"   #submitBtn{\n"
"color:(255,255,255);\n"
"	background-color: transparent;\n"
"    border: 1px solid rgba(93, 93, 91,100);\n"
"    border-radius:10px;\n"
"}\n"
"\n"
" #submitBtn:hover { \n"
"color:(255,255,255);\n"
"  background-color: rgb(44, 49, 57);\n"
"  border-style: solid;\n"
" border-radius: 10px;\n"
"}\n"
" #submitBtn:pressed {\n"
"color:(255,255,255);\n"
" background-color: rgb(23, 26, 30);\n"
"	background-color: rgba(100, 140, 44,150);\n"
"  border-style: solid;\n"
"  border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"/* /////////////////////////////////////ScrollBars */\n"
"\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"  \n"
"	background-color"
                        ": rgba(115, 164, 37,200);\n"
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
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/*//////Horizonital*/\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-ra"
                        "dius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: rgba(115, 164, 37,200);\n"
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
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"\n"
"")
        self.gridLayout = QGridLayout(examwidgete)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(10, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.scrollArea_2 = QScrollArea(examwidgete)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"background-color: rgb(44, 49, 58);\n"
"border:1px solid rgb(40, 44, 52 );")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 850, 212))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea_2, 5, 0, 1, 3)

        self.noteBtn = QPushButton(examwidgete)
        self.noteBtn.setObjectName(u"noteBtn")
        self.noteBtn.setMinimumSize(QSize(60, 30))
        self.noteBtn.setMaximumSize(QSize(60, 16777215))
        font = QFont()
        font.setFamilies([u"Open Sans"])
        font.setPointSize(9)
        font.setBold(True)
        self.noteBtn.setFont(font)
        self.noteBtn.setStyleSheet(u"\n"
" #noteBtn{\n"
"color:(255,255,255);\n"
"	background-color: transparent;\n"
" border: 1px solid rgba(93, 93, 91,100);\n"
"    border-radius:7px;\n"
"}\n"
"\n"
" #noteBtn:hover { \n"
"color:(255,255,255);\n"
"  background-color: rgb(44, 49, 57);\n"
"  border-style: solid;\n"
" border-radius:7px;\n"
"}\n"
" #noteBtn:pressed {\n"
"color:(255,255,255);\n"
" background-color: rgb(55, 63, 77);\n"
"  border-style: solid;\n"
"  border-radius: 7px;\n"
"}")

        self.gridLayout.addWidget(self.noteBtn, 0, 2, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.frame = QFrame(examwidgete)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(30, 30))
        self.frame.setStyleSheet(u"\n"
"\n"
"border:1px solid rgb(40, 44, 52);\n"
"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lcdNumber = QLCDNumber(self.frame)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setMaximumSize(QSize(100, 30))
        font1 = QFont()
        font1.setPointSize(12)
        self.lcdNumber.setFont(font1)
        self.lcdNumber.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.verticalLayout.addWidget(self.lcdNumber)


        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.note_edit = QTextEdit(examwidgete)
        self.note_edit.setObjectName(u"note_edit")
        self.note_edit.setMaximumSize(QSize(300, 160))
        self.note_edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.note_edit.setStyleSheet(u"\n"
"border:1px solid rgb(59, 64, 72);\n"
"border-radius:10px;\n"
"background-color: rgb(35, 38, 45);")
        self.note_edit.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.gridLayout.addWidget(self.note_edit, 3, 2, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.camera_label = QGraphicsView(examwidgete)
        self.camera_label.setObjectName(u"camera_label")
        self.camera_label.setMaximumSize(QSize(300, 300))
        self.camera_label.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.camera_label.setStyleSheet(u"border-radius:10px;\n"
"border:1px solid rgb(59, 64, 72);")
        self.camera_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)

        self.gridLayout.addWidget(self.camera_label, 1, 0, 3, 1)

        self.frame_2 = QFrame(examwidgete)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setMaximumSize(QSize(150, 16777215))
        self.frame_2.setStyleSheet(u"border:1px solid rgb(40, 44, 52);")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.submitBtn = QPushButton(self.frame_2)
        self.submitBtn.setObjectName(u"submitBtn")
        self.submitBtn.setMinimumSize(QSize(30, 38))
        font2 = QFont()
        font2.setFamilies([u"Open Sans"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.submitBtn.setFont(font2)
        self.submitBtn.setStyleSheet(u" border: 1px solid rgba(93, 93, 91,100);\n"
"\n"
"\n"
"")

        self.verticalLayout_2.addWidget(self.submitBtn)


        self.gridLayout.addWidget(self.frame_2, 6, 0, 1, 1)

        self.note_label = QLabel(examwidgete)
        self.note_label.setObjectName(u"note_label")
        self.note_label.setMaximumSize(QSize(240, 16777215))
        self.note_label.setFont(font)

        self.gridLayout.addWidget(self.note_label, 2, 2, 1, 1)

        self.warnlabel = QLabel(examwidgete)
        self.warnlabel.setObjectName(u"warnlabel")
        font3 = QFont()
        font3.setPointSize(16)
        self.warnlabel.setFont(font3)

        self.gridLayout.addWidget(self.warnlabel, 3, 1, 1, 1)


        self.retranslateUi(examwidgete)

        QMetaObject.connectSlotsByName(examwidgete)
    # setupUi

    def retranslateUi(self, examwidgete):
        examwidgete.setWindowTitle(QCoreApplication.translate("examwidgete", u"Form", None))
        self.noteBtn.setText(QCoreApplication.translate("examwidgete", u"\u0623\u0631\u0633\u0644", None))
        self.submitBtn.setText(QCoreApplication.translate("examwidgete", u"\u0627\u0644\u0627\u0646\u062a\u0647\u0627\u0621", None))
        self.note_label.setText(QCoreApplication.translate("examwidgete", u"\u0627\u0630\u0627 \u0643\u0627\u0646 \u0644\u062f\u064a\u0643 \u0645\u0644\u0627\u062d\u0638\u0627\u062a... \u0642\u0645 \u0628\u0625\u0639\u0644\u0627\u0645\u0646\u0627 \u0647\u0646\u0627 :", None))
        self.warnlabel.setText("")
    # retranslateUi

