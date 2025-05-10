# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AdminGui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpinBox, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QWidget)
import resources_rc
from PySide6 import QtCore


class Ui_AdminWindow(object):
    def setupUi(self, AdminWindow):
        if not AdminWindow.objectName():
            AdminWindow.setObjectName(u"AdminWindow")
        AdminWindow.resize(651, 562)
        AdminWindow.setMinimumSize(QSize(651, 562))
        AdminWindow.setMaximumSize(QSize(651, 562))
        AdminWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        AdminWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        AdminWindow.setStyleSheet(u"*{\n"
"border:none;\n"
"background-color: transparent;\n"
"background:transparent;\n"
"padding: 0;\n"
"margin :0;\n"
"color: #fff\n"
"}\n"
"QPushButton{\n"
"padding: 2px 5px;}\n"
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
"	background-color: rgba(115, 164, 37,200);\n"
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
""
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
"	border-radius: 0px;\n"
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
"	bo"
                        "rder-top-left-radius: 4px;\n"
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
"/*////////////*/\n"
"#statusbar{\n"
"	background-color: rgb(30, 34, 40);\n"
"\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 8px;\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
""
                        "	border-radius: 5px;\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(135, 158, 51);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"\n"
"\n"
"#closeBtn ,#minimizeBtn  {\n"
"    padding: 2px 5px;\n"
"}\n"
"#closeBtn:hove"
                        "r {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(67, 77, 88, 150), stop:1 rgba(62, 72, 83, 80)); \n"
" 	border: 1px solid rgba(93, 93, 91,100);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"#minimizeBtn:hover {\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(67, 77, 88, 150), stop:1 rgba(62, 72, 83, 80)); \n"
" border: 1px solid rgba(93, 93, 91,100);\n"
"border-radius:10px;\n"
"}\n"
" #closeBtn:pressed {	\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(108, 152, 48, 200), stop:1 rgba(98, 142, 43, 90)); \n"
" 	border: 1px solid rgba(93, 93, 91,100);\n"
"border-radius:10px;\n"
"}\n"
"#minimizeBtn:pressed {	\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(108, 152, 48, 200), stop:1 rgba(98, 142, 43, 90)); ;\n"
" 	border: 1px solid rgba(93, 93, 91,100);\n"
"border-radius:10px;\n"
"}\n"
"/* ////////////////////////QTableWidget///////////////////////////// *"
                        "/\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertica"
                        "l\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.menu_01_01 = QAction(AdminWindow)
        self.menu_01_01.setObjectName(u"menu_01_01")
        self.menu_01_02 = QAction(AdminWindow)
        self.menu_01_02.setObjectName(u"menu_01_02")
        self.menu_02_01 = QAction(AdminWindow)
        self.menu_02_01.setObjectName(u"menu_02_01")
        self.menu_03_01 = QAction(AdminWindow)
        self.menu_03_01.setObjectName(u"menu_03_01")
        self.menu_04_01 = QAction(AdminWindow)
        self.menu_04_01.setObjectName(u"menu_04_01")
        self.menu_05_01 = QAction(AdminWindow)
        self.menu_05_01.setObjectName(u"menu_05_01")
        self.menu_05_02 = QAction(AdminWindow)
        self.menu_05_02.setObjectName(u"menu_05_02")
        self.menu_05_03 = QAction(AdminWindow)
        self.menu_05_03.setObjectName(u"menu_05_03")
        self.menu_05_04 = QAction(AdminWindow)
        self.menu_05_04.setObjectName(u"menu_05_04")
        self.menu_06_01 = QAction(AdminWindow)
        self.menu_06_01.setObjectName(u"menu_06_01")
        self.centralwidget = QWidget(AdminWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"\n"
"background-color: rgb(30, 34, 40);\n"
"")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 120, 671, 441))
        self.tabWidget.setMaximumSize(QSize(700, 600))
        font = QFont()
        font.setFamilies([u"Poppins"])
        font.setBold(False)
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"QTabWidget::pane{ /* The tab widget frame */\n"
"    border-top: -1px ;\n"
"	border-left: 0px solid lightgray; \n"
"	border-right: 1px solid lightgray; \n"
"	border-bottom: 1px solid lightgray; \n"
"}\n"
"QWidget {\n"
"\n"
"	background-color: rgb(30, 34, 40);\n"
"\n"
"}\n"
"QTabBar::tab {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(64, 71, 88, 150), stop:1 rgba(44, 49, 58, 200)); \n"
"    color: rgb(255, 255, 255);\n"
"    padding:12px;\n"
"    border-radius: 10px; \n"
"    margin-bottom: -5px;\n"
"    margin-left:1px;\n"
"    border:1px solid rgb(26, 29, 34);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(166, 200, 52, 90), stop:1 rgba(98, 142, 43, 90)); \n"
"    margin-bottom: -2px;\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(67, 77, 88, 150), stop:1 rgba(62, 72, 83, 80)); \n"
" margin-bottom: -1px;\n"
""
                        "\n"
"}\n"
"")
        self.tabWidget.setTabBarAutoHide(False)
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.tab_1.setStyleSheet(u"#btn10,#btn11,#btn12{\n"
"	background-color: transparent;\n"
"    border: 1px solid rgba(93, 93, 91,100);\n"
"    border-radius:10px;\n"
"}\n"
"#btn10:hover{\n"
"	background-color: rgb(72, 76, 83);\n"
"}\n"
"\n"
"#btn11:hover{\n"
"	background-color: rgb(72, 76, 83);\n"
"}\n"
"#btn10:pressed{\n"
"	background-color: rgb(28, 31, 36);\n"
"}\n"
"\n"
"#btn11:pressed{\n"
"	background-color: rgb(28, 31, 36);\n"
"}\n"
"\n"
"#btn12:hover{\n"
"	background-color: rgb(72, 76, 83);\n"
"}\n"
"#btn12:pressed{\n"
"	background-color: rgb(28, 31, 36);\n"
"}")
        self.label_13 = QLabel(self.tab_1)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(110, 50, 251, 29))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setKerning(True)
        self.label_13.setFont(font1)
        self.label_13.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_13.setStyleSheet(u"")
        self.label_13.setScaledContents(True)
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_12 = QLabel(self.tab_1)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(110, 20, 251, 29))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setKerning(True)
        self.label_12.setFont(font2)
        self.label_12.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_12.setScaledContents(True)
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_11 = QLabel(self.tab_1)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(30, 20, 61, 61))
        self.label_11.setStyleSheet(u"image: url(:/images/images/images/prof12.png);")
        self.label_11.setPixmap(QPixmap(u"../../../.designer/src/student.png"))
        self.label_11.setScaledContents(True)
        self.tb10 = QLineEdit(self.tab_1)
        self.tb10.setObjectName(u"tb10")
        self.tb10.setGeometry(QRect(130, 100, 171, 31))
        font3 = QFont()
        font3.setFamilies([u"Poppins Medium"])
        font3.setPointSize(10)
        self.tb10.setFont(font3)
        self.tb10.setStyleSheet(u"")
        self.label_15 = QLabel(self.tab_1)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(40, 150, 81, 31))
        font4 = QFont()
        font4.setFamilies([u"Open Sans"])
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setKerning(True)
        self.label_15.setFont(font4)
        self.label_15.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_15.setStyleSheet(u"")
        self.label_15.setScaledContents(True)
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.line = QFrame(self.tab_1)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(320, 140, 20, 181))
        self.line.setStyleSheet(u"")
        self.line.setFrameShadow(QFrame.Shadow.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QFrame.HLine)
        self.label_17 = QLabel(self.tab_1)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(60, 250, 41, 31))
        self.label_17.setFont(font4)
        self.label_17.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_17.setStyleSheet(u"")
        self.label_17.setScaledContents(True)
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.cb10 = QComboBox(self.tab_1)
        self.cb10.addItem("")
        self.cb10.addItem("")
        self.cb10.setObjectName(u"cb10")
        self.cb10.setGeometry(QRect(130, 250, 171, 31))
        font5 = QFont()
        font5.setFamilies([u"Open Sans"])
        font5.setPointSize(10)
        self.cb10.setFont(font5)
        self.cb10.setStyleSheet(u"")
        self.label_16 = QLabel(self.tab_1)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(40, 200, 81, 31))
        self.label_16.setFont(font4)
        self.label_16.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_16.setStyleSheet(u"")
        self.label_16.setScaledContents(True)
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tb11 = QLineEdit(self.tab_1)
        self.tb11.setObjectName(u"tb11")
        self.tb11.setGeometry(QRect(130, 150, 171, 31))
        self.tb11.setFont(font3)
        self.tb11.setStyleSheet(u"")
        self.tb12 = QLineEdit(self.tab_1)
        self.tb12.setObjectName(u"tb12")
        self.tb12.setGeometry(QRect(130, 200, 171, 31))
        self.tb12.setFont(font3)
        self.tb12.setStyleSheet(u"")
        self.label_14 = QLabel(self.tab_1)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(40, 100, 81, 31))
        self.label_14.setFont(font4)
        self.label_14.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_14.setStyleSheet(u"")
        self.label_14.setScaledContents(True)
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_18 = QLabel(self.tab_1)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(350, 130, 81, 31))
        self.label_18.setFont(font4)
        self.label_18.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_18.setStyleSheet(u"")
        self.label_18.setScaledContents(True)
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_19 = QLabel(self.tab_1)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(350, 180, 81, 31))
        self.label_19.setFont(font4)
        self.label_19.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_19.setStyleSheet(u"")
        self.label_19.setScaledContents(True)
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tb13 = QLineEdit(self.tab_1)
        self.tb13.setObjectName(u"tb13")
        self.tb13.setGeometry(QRect(450, 130, 171, 31))
        self.tb13.setFont(font3)
        self.tb13.setStyleSheet(u"")
        self.tb14 = QLineEdit(self.tab_1)
        self.tb14.setObjectName(u"tb14")
        self.tb14.setGeometry(QRect(450, 180, 171, 31))
        self.tb14.setFont(font3)
        self.tb14.setStyleSheet(u"")
        self.label_191 = QLabel(self.tab_1)
        self.label_191.setObjectName(u"label_191")
        self.label_191.setGeometry(QRect(350, 300, 91, 31))
        self.label_191.setFont(font4)
        self.label_191.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_191.setStyleSheet(u"")
        self.label_191.setScaledContents(True)
        self.label_191.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btn10 = QPushButton(self.tab_1)
        self.btn10.setObjectName(u"btn10")
        self.btn10.setGeometry(QRect(520, 300, 75, 31))
        font6 = QFont()
        font6.setFamilies([u"Open Sans"])
        font6.setBold(True)
        self.btn10.setFont(font6)
        self.btn10.setStyleSheet(u"")
        self.btn11 = QPushButton(self.tab_1)
        self.btn11.setObjectName(u"btn11")
        self.btn11.setGeometry(QRect(500, 30, 111, 41))
        font7 = QFont()
        font7.setFamilies([u"Open Sans"])
        font7.setPointSize(10)
        font7.setBold(True)
        self.btn11.setFont(font7)
        self.btn11.setStyleSheet(u"")
        self.filenamelabel = QLabel(self.tab_1)
        self.filenamelabel.setObjectName(u"filenamelabel")
        self.filenamelabel.setGeometry(QRect(430, 340, 171, 21))
        font8 = QFont()
        font8.setFamilies([u"Myriad Pro Light"])
        font8.setBold(True)
        self.filenamelabel.setFont(font8)
        self.filenamelabel.setStyleSheet(u"border-radius:3px;\n"
"border:1px solid rgb(63, 70, 87);")
        self.label_192 = QLabel(self.tab_1)
        self.label_192.setObjectName(u"label_192")
        self.label_192.setGeometry(QRect(380, 340, 41, 21))
        self.label_192.setStyleSheet(u"image: url(:/images/images/images/picture-svgrepo-com.svg);")
        self.label_193 = QLabel(self.tab_1)
        self.label_193.setObjectName(u"label_193")
        self.label_193.setGeometry(QRect(350, 230, 81, 31))
        self.label_193.setFont(font4)
        self.label_193.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_193.setStyleSheet(u"")
        self.label_193.setScaledContents(True)
        self.label_193.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tb15 = QLineEdit(self.tab_1)
        self.tb15.setObjectName(u"tb15")
        self.tb15.setGeometry(QRect(450, 230, 171, 31))
        self.tb15.setFont(font3)
        self.tb15.setStyleSheet(u"")
        self.label_194 = QLabel(self.tab_1)
        self.label_194.setObjectName(u"label_194")
        self.label_194.setGeometry(QRect(30, 300, 101, 31))
        self.label_194.setFont(font4)
        self.label_194.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_194.setStyleSheet(u"")
        self.label_194.setScaledContents(True)
        self.label_194.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btn12 = QPushButton(self.tab_1)
        self.btn12.setObjectName(u"btn12")
        self.btn12.setGeometry(QRect(210, 300, 71, 31))
        self.btn12.setFont(font6)
        self.btn12.setStyleSheet(u"")
        self.label_195 = QLabel(self.tab_1)
        self.label_195.setObjectName(u"label_195")
        self.label_195.setGeometry(QRect(60, 340, 41, 21))
        self.label_195.setStyleSheet(u"image: url(:/images/images/images/picture-svgrepo-com.svg);")
        self.filenamelabel_4 = QLabel(self.tab_1)
        self.filenamelabel_4.setObjectName(u"filenamelabel_4")
        self.filenamelabel_4.setGeometry(QRect(110, 340, 191, 21))
        self.filenamelabel_4.setFont(font8)
        self.filenamelabel_4.setStyleSheet(u"border-radius:3px;\n"
"border:1px solid rgb(63, 70, 87);")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setStyleSheet(u"#btn20,#btn21,#btn22,#btn23{\n"
"	background-color: transparent;\n"
"    border: 1px solid rgba(93, 93, 91,100);\n"
"    border-radius:10px;\n"
"}\n"
"#btn20:hover{\n"
"	background-color: rgb(72, 76, 83);\n"
"}\n"
"\n"
"#btn21:hover{\n"
"	background-color: rgb(72, 76, 83);\n"
"}\n"
"#btn22:hover{\n"
"	background-color: rgb(72, 76, 83);\n"
"}\n"
"#btn20:pressed{\n"
"	background-color: rgb(28, 31, 36);\n"
"}\n"
"\n"
"#btn21:pressed{\n"
"	background-color: rgb(28, 31, 36);\n"
"}\n"
"#btn22:pressed{\n"
"	background-color: rgb(28, 31, 36);\n"
"}\n"
"#btn23:hover{\n"
"	background-color: rgb(72, 76, 83);\n"
"}\n"
"#btn23:pressed{\n"
"	background-color: rgb(28, 31, 36);\n"
"}")
        self.line_2 = QFrame(self.tab_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(320, 140, 20, 181))
        self.line_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_2.setFrameShadow(QFrame.Shadow.Plain)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QFrame.HLine)
        self.label_20 = QLabel(self.tab_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(30, 20, 61, 61))
        self.label_20.setStyleSheet(u"image: url(:/images/images/images/prof13.png);")
        self.label_20.setPixmap(QPixmap(u"../../../.designer/src/student-edit.png"))
        self.label_20.setScaledContents(True)
        self.label_21 = QLabel(self.tab_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(110, 20, 211, 61))
        self.label_21.setFont(font2)
        self.label_21.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_21.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_21.setScaledContents(True)
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.btn20 = QPushButton(self.tab_2)
        self.btn20.setObjectName(u"btn20")
        self.btn20.setGeometry(QRect(500, 30, 111, 41))
        self.btn20.setFont(font7)
        self.btn20.setStyleSheet(u"")
        self.btn21 = QPushButton(self.tab_2)
        self.btn21.setObjectName(u"btn21")
        self.btn21.setGeometry(QRect(520, 100, 81, 31))
        self.btn21.setFont(font7)
        self.btn21.setStyleSheet(u"")
        self.cb20 = QComboBox(self.tab_2)
        self.cb20.setObjectName(u"cb20")
        self.cb20.setGeometry(QRect(150, 100, 171, 31))
        font9 = QFont()
        font9.setFamilies([u"Poppins SemiBold"])
        font9.setPointSize(10)
        self.cb20.setFont(font9)
        self.cb20.setStyleSheet(u"")
        self.label_23 = QLabel(self.tab_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(30, 100, 81, 31))
        self.label_23.setFont(font4)
        self.label_23.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_23.setStyleSheet(u"")
        self.label_23.setScaledContents(True)
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_24 = QLabel(self.tab_2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(30, 150, 81, 31))
        self.label_24.setFont(font4)
        self.label_24.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_24.setStyleSheet(u"")
        self.label_24.setScaledContents(True)
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_25 = QLabel(self.tab_2)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(30, 200, 81, 31))
        self.label_25.setFont(font4)
        self.label_25.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_25.setStyleSheet(u"")
        self.label_25.setScaledContents(True)
        self.label_25.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_26 = QLabel(self.tab_2)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(50, 250, 41, 31))
        self.label_26.setFont(font4)
        self.label_26.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_26.setStyleSheet(u"")
        self.label_26.setScaledContents(True)
        self.label_26.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.cb21 = QComboBox(self.tab_2)
        self.cb21.addItem("")
        self.cb21.addItem("")
        self.cb21.setObjectName(u"cb21")
        self.cb21.setGeometry(QRect(150, 250, 171, 31))
        self.cb21.setFont(font9)
        self.cb21.setStyleSheet(u"")
        self.tb20 = QLineEdit(self.tab_2)
        self.tb20.setObjectName(u"tb20")
        self.tb20.setGeometry(QRect(150, 150, 171, 31))
        self.tb20.setFont(font3)
        self.tb20.setStyleSheet(u"")
        self.tb21 = QLineEdit(self.tab_2)
        self.tb21.setObjectName(u"tb21")
        self.tb21.setGeometry(QRect(150, 200, 171, 31))
        self.tb21.setFont(font3)
        self.tb21.setStyleSheet(u"")
        self.tb22 = QLineEdit(self.tab_2)
        self.tb22.setObjectName(u"tb22")
        self.tb22.setGeometry(QRect(450, 150, 171, 31))
        self.tb22.setFont(font3)
        self.tb22.setStyleSheet(u"")
        self.label_27 = QLabel(self.tab_2)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(350, 150, 81, 31))
        self.label_27.setFont(font4)
        self.label_27.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_27.setStyleSheet(u"")
        self.label_27.setScaledContents(True)
        self.label_27.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_28 = QLabel(self.tab_2)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(340, 200, 101, 31))
        self.label_28.setFont(font4)
        self.label_28.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_28.setStyleSheet(u"")
        self.label_28.setScaledContents(True)
        self.label_28.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tb23 = QLineEdit(self.tab_2)
        self.tb23.setObjectName(u"tb23")
        self.tb23.setGeometry(QRect(450, 200, 171, 31))
        self.tb23.setFont(font3)
        self.tb23.setStyleSheet(u"")
        self.label_29 = QLabel(self.tab_2)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(360, 310, 111, 31))
        self.label_29.setFont(font4)
        self.label_29.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_29.setStyleSheet(u"")
        self.label_29.setScaledContents(True)
        self.label_29.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btn22 = QPushButton(self.tab_2)
        self.btn22.setObjectName(u"btn22")
        self.btn22.setGeometry(QRect(540, 310, 81, 31))
        self.btn22.setFont(font6)
        self.btn22.setStyleSheet(u"")
        self.label_291 = QLabel(self.tab_2)
        self.label_291.setObjectName(u"label_291")
        self.label_291.setGeometry(QRect(410, 350, 41, 21))
        self.label_291.setStyleSheet(u"image: url(:/images/images/images/picture-svgrepo-com.svg);")
        self.filenamelabel_2 = QLabel(self.tab_2)
        self.filenamelabel_2.setObjectName(u"filenamelabel_2")
        self.filenamelabel_2.setGeometry(QRect(450, 350, 171, 21))
        font10 = QFont()
        font10.setFamilies([u"Segoe UI"])
        font10.setPointSize(5)
        font10.setBold(True)
        self.filenamelabel_2.setFont(font10)
        self.filenamelabel_2.setStyleSheet(u"border-radius:3px;\n"
"border:1px solid rgb(63, 70, 87);\n"
"\n"
"")
        self.label_292 = QLabel(self.tab_2)
        self.label_292.setObjectName(u"label_292")
        self.label_292.setGeometry(QRect(340, 250, 101, 31))
        self.label_292.setFont(font4)
        self.label_292.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_292.setStyleSheet(u"")
        self.label_292.setScaledContents(True)
        self.label_292.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tb24 = QLineEdit(self.tab_2)
        self.tb24.setObjectName(u"tb24")
        self.tb24.setGeometry(QRect(450, 250, 171, 31))
        self.tb24.setFont(font3)
        self.tb24.setStyleSheet(u"")
        self.label_294 = QLabel(self.tab_2)
        self.label_294.setObjectName(u"label_294")
        self.label_294.setGeometry(QRect(20, 310, 111, 21))
        self.label_294.setFont(font4)
        self.label_294.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_294.setStyleSheet(u"")
        self.label_294.setScaledContents(True)
        self.label_294.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btn23 = QPushButton(self.tab_2)
        self.btn23.setObjectName(u"btn23")
        self.btn23.setGeometry(QRect(260, 310, 61, 31))
        self.btn23.setFont(font6)
        self.btn23.setStyleSheet(u"")
        self.scrollArea = QScrollArea(self.tab_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(99, 349, 221, 71))
        font11 = QFont()
        font11.setPointSize(5)
        self.scrollArea.setFont(font11)
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 221, 71))
        self.filenamelabel_3 = QLabel(self.scrollAreaWidgetContents)
        self.filenamelabel_3.setObjectName(u"filenamelabel_3")
        self.filenamelabel_3.setGeometry(QRect(20, 0, 201, 21))
        font12 = QFont()
        font12.setPointSize(3)
        self.filenamelabel_3.setFont(font12)
        self.filenamelabel_3.setStyleSheet(u"border-radius:3px;\n"
"border:1px solid rgb(63, 70, 87);\n"
"")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_293 = QLabel(self.tab_2)
        self.label_293.setObjectName(u"label_293")
        self.label_293.setGeometry(QRect(70, 350, 41, 21))
        self.label_293.setStyleSheet(u"image: url(:/images/images/images/picture-svgrepo-com.svg);")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tab_3.setStyleSheet(u"#btn30,#btn31,#btn32,#btn33{\n"
"	background-color: transparent;\n"
"    border: 1px solid rgba(93, 93, 91,100);\n"
"    border-radius:10px;\n"
"}\n"
"#btn30:hover{\n"
"	background-color: rgb(72, 76, 83);\n"
"}\n"
"#btn31:hover{\n"
"	background-color: rgb(72, 76, 83);\n"
"}\n"
"#btn32:hover{\n"
"	background-color: rgb(72, 76, 83);\n"
"}\n"
"#btn33:hover{\n"
"	background-color: rgb(72, 76, 83);\n"
"}\n"
"#btn30:pressed{\n"
"	background-color: rgb(28, 31, 36);\n"
"}\n"
"#btn31:pressed{\n"
"	background-color: rgb(28, 31, 36);\n"
"}\n"
"#btn32:pressed{\n"
"	background-color: rgb(28, 31, 36);\n"
"}\n"
"#btn33:pressed{\n"
"	background-color: rgb(28, 31, 36);\n"
"}")
        self.groupBox = QGroupBox(self.tab_3)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 10, 281, 391))
        font13 = QFont()
        font13.setFamilies([u"Poppins Black"])
        font13.setPointSize(10)
        font13.setBold(True)
        self.groupBox.setFont(font13)
        self.groupBox.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_30 = QLabel(self.groupBox)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(20, 10, 251, 29))
        font14 = QFont()
        font14.setFamilies([u"Segoe UI"])
        font14.setPointSize(13)
        font14.setBold(True)
        font14.setItalic(False)
        font14.setKerning(True)
        self.label_30.setFont(font14)
        self.label_30.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_30.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_30.setScaledContents(True)
        self.label_30.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.btn30 = QPushButton(self.groupBox)
        self.btn30.setObjectName(u"btn30")
        self.btn30.setGeometry(QRect(20, 340, 75, 31))
        self.btn30.setFont(font7)
        self.btn30.setStyleSheet(u"")
        self.label_31 = QLabel(self.groupBox)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(10, 80, 81, 31))
        self.label_31.setFont(font4)
        self.label_31.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_31.setStyleSheet(u"")
        self.label_31.setScaledContents(True)
        self.label_31.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_32 = QLabel(self.groupBox)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(30, 120, 51, 31))
        self.label_32.setFont(font4)
        self.label_32.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_32.setStyleSheet(u"")
        self.label_32.setScaledContents(True)
        self.label_32.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.cb30 = QComboBox(self.groupBox)
        self.cb30.setObjectName(u"cb30")
        self.cb30.setGeometry(QRect(100, 120, 171, 31))
        self.cb30.setFont(font9)
        self.cb30.setStyleSheet(u"")
        self.label_33 = QLabel(self.groupBox)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(10, 240, 81, 31))
        self.label_33.setFont(font4)
        self.label_33.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_33.setStyleSheet(u"")
        self.label_33.setScaledContents(True)
        self.label_33.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tb31 = QLineEdit(self.groupBox)
        self.tb31.setObjectName(u"tb31")
        self.tb31.setGeometry(QRect(100, 240, 171, 31))
        self.tb31.setFont(font3)
        self.tb31.setStyleSheet(u"")
        self.tb30 = QLineEdit(self.groupBox)
        self.tb30.setObjectName(u"tb30")
        self.tb30.setGeometry(QRect(100, 80, 171, 31))
        self.tb30.setFont(font3)
        self.tb30.setStyleSheet(u"")
        self.btn30.raise_()
        self.label_30.raise_()
        self.label_31.raise_()
        self.label_32.raise_()
        self.cb30.raise_()
        self.label_33.raise_()
        self.tb31.raise_()
        self.tb30.raise_()
        self.groupBox_2 = QGroupBox(self.tab_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(310, 10, 321, 391))
        self.groupBox_2.setFont(font13)
        self.groupBox_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_34 = QLabel(self.groupBox_2)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(50, 10, 221, 31))
        self.label_34.setFont(font14)
        self.label_34.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_34.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_34.setScaledContents(True)
        self.label_34.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.btn32 = QPushButton(self.groupBox_2)
        self.btn32.setObjectName(u"btn32")
        self.btn32.setGeometry(QRect(80, 340, 131, 31))
        self.btn32.setFont(font7)
        self.btn32.setStyleSheet(u"")
        self.btn31 = QPushButton(self.groupBox_2)
        self.btn31.setObjectName(u"btn31")
        self.btn31.setGeometry(QRect(100, 180, 171, 31))
        font15 = QFont()
        font15.setFamilies([u"Open Sans"])
        font15.setPointSize(9)
        font15.setBold(True)
        self.btn31.setFont(font15)
        self.btn31.setStyleSheet(u"")
        self.btn33 = QPushButton(self.groupBox_2)
        self.btn33.setObjectName(u"btn33")
        self.btn33.setGeometry(QRect(230, 340, 81, 31))
        self.btn33.setFont(font7)
        self.btn33.setStyleSheet(u"")
        self.label_35 = QLabel(self.groupBox_2)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(10, 80, 81, 31))
        self.label_35.setFont(font4)
        self.label_35.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_35.setStyleSheet(u"")
        self.label_35.setScaledContents(True)
        self.label_35.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_36 = QLabel(self.groupBox_2)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(30, 120, 51, 31))
        self.label_36.setFont(font4)
        self.label_36.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_36.setStyleSheet(u"")
        self.label_36.setScaledContents(True)
        self.label_36.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.cb31 = QComboBox(self.groupBox_2)
        self.cb31.setObjectName(u"cb31")
        self.cb31.setGeometry(QRect(100, 120, 171, 31))
        self.cb31.setFont(font9)
        self.cb31.setStyleSheet(u"")
        self.label_37 = QLabel(self.groupBox_2)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(10, 240, 81, 31))
        self.label_37.setFont(font4)
        self.label_37.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_37.setStyleSheet(u"")
        self.label_37.setScaledContents(True)
        self.label_37.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tb33 = QLineEdit(self.groupBox_2)
        self.tb33.setObjectName(u"tb33")
        self.tb33.setGeometry(QRect(100, 240, 171, 31))
        self.tb33.setFont(font3)
        self.tb33.setStyleSheet(u"")
        self.tb32 = QLineEdit(self.groupBox_2)
        self.tb32.setObjectName(u"tb32")
        self.tb32.setGeometry(QRect(100, 80, 171, 31))
        self.tb32.setFont(font3)
        self.tb32.setStyleSheet(u"")
        self.btn32.raise_()
        self.btn31.raise_()
        self.btn33.raise_()
        self.label_35.raise_()
        self.label_36.raise_()
        self.cb31.raise_()
        self.label_37.raise_()
        self.tb33.raise_()
        self.label_34.raise_()
        self.tb32.raise_()
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.tab_6.setStyleSheet(u"#btn60{\n"
"	background-color: transparent;\n"
"    border: 1px solid rgba(93, 93, 91,100);\n"
"    border-radius:10px;\n"
"}\n"
"#btn60:hover{\n"
"	background-color: rgb(72, 76, 83);\n"
"}\n"
"\n"
"#btn60:pressed{\n"
"	background-color: rgb(28, 31, 36);\n"
"}")
        self.label_60 = QLabel(self.tab_6)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setGeometry(QRect(170, 10, 111, 31))
        self.label_60.setFont(font5)
        self.label_61 = QLabel(self.tab_6)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setGeometry(QRect(530, 60, 91, 31))
        self.label_61.setFont(font5)
        self.cb60 = QComboBox(self.tab_6)
        self.cb60.setObjectName(u"cb60")
        self.cb60.setGeometry(QRect(30, 10, 131, 31))
        font16 = QFont()
        font16.setPointSize(8)
        self.cb60.setFont(font16)
        self.textEdit = QTextEdit(self.tab_6)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(30, 60, 531, 151))
        self.label_62 = QLabel(self.tab_6)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setGeometry(QRect(20, 230, 61, 20))
        self.label_63 = QLabel(self.tab_6)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setGeometry(QRect(20, 260, 61, 20))
        self.label_64 = QLabel(self.tab_6)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setGeometry(QRect(20, 290, 61, 20))
        self.label_65 = QLabel(self.tab_6)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setGeometry(QRect(20, 320, 61, 20))
        self.label_691 = QLabel(self.tab_6)
        self.label_691.setObjectName(u"label_691")
        self.label_691.setGeometry(QRect(20, 360, 91, 16))
        self.cb61 = QComboBox(self.tab_6)
        self.cb61.addItem("")
        self.cb61.addItem("")
        self.cb61.addItem("")
        self.cb61.addItem("")
        self.cb61.setObjectName(u"cb61")
        self.cb61.setGeometry(QRect(120, 360, 161, 21))
        font17 = QFont()
        font17.setFamilies([u"Open Sans"])
        font17.setPointSize(9)
        font17.setBold(False)
        self.cb61.setFont(font17)
        self.btn60 = QPushButton(self.tab_6)
        self.btn60.setObjectName(u"btn60")
        self.btn60.setGeometry(QRect(520, 10, 101, 31))
        self.btn60.setFont(font7)
        self.tb60 = QLineEdit(self.tab_6)
        self.tb60.setObjectName(u"tb60")
        self.tb60.setGeometry(QRect(100, 230, 431, 22))
        self.tb61 = QLineEdit(self.tab_6)
        self.tb61.setObjectName(u"tb61")
        self.tb61.setGeometry(QRect(100, 260, 431, 22))
        self.tb62 = QLineEdit(self.tab_6)
        self.tb62.setObjectName(u"tb62")
        self.tb62.setGeometry(QRect(100, 290, 431, 22))
        self.tb63 = QLineEdit(self.tab_6)
        self.tb63.setObjectName(u"tb63")
        self.tb63.setGeometry(QRect(100, 320, 431, 22))
        self.label_67 = QLabel(self.tab_6)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setGeometry(QRect(540, 230, 41, 21))
        self.label_67.setFont(font5)
        self.label_68 = QLabel(self.tab_6)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setGeometry(QRect(540, 260, 41, 21))
        self.label_68.setFont(font5)
        self.label_69 = QLabel(self.tab_6)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setGeometry(QRect(540, 290, 41, 21))
        self.label_69.setFont(font5)
        self.label_690 = QLabel(self.tab_6)
        self.label_690.setObjectName(u"label_690")
        self.label_690.setGeometry(QRect(540, 320, 41, 21))
        self.label_690.setFont(font5)
        self.sp60 = QSpinBox(self.tab_6)
        self.sp60.setObjectName(u"sp60")
        self.sp60.setGeometry(QRect(590, 230, 88, 22))
        self.sp61 = QSpinBox(self.tab_6)
        self.sp61.setObjectName(u"sp61")
        self.sp61.setGeometry(QRect(590, 260, 88, 22))
        self.sp62 = QSpinBox(self.tab_6)
        self.sp62.setObjectName(u"sp62")
        self.sp62.setGeometry(QRect(590, 290, 88, 22))
        self.sp63 = QSpinBox(self.tab_6)
        self.sp63.setObjectName(u"sp63")
        self.sp63.setGeometry(QRect(590, 320, 88, 22))
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.tab_7.setStyleSheet(u"#btn70{\n"
"	background-color: transparent;\n"
"    border: 1px solid rgba(93, 93, 91,100);\n"
"    border-radius:10px;\n"
"}\n"
"#btn70:hover{\n"
"	background-color: rgb(72, 76, 83);\n"
"}\n"
"\n"
"#btn70:pressed{\n"
"	background-color: rgb(28, 31, 36);\n"
"}")
        self.label_70 = QLabel(self.tab_7)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setGeometry(QRect(180, 10, 121, 31))
        self.label_70.setFont(font5)
        self.cb70 = QComboBox(self.tab_7)
        self.cb70.setObjectName(u"cb70")
        self.cb70.setGeometry(QRect(30, 10, 141, 31))
        self.label_71 = QLabel(self.tab_7)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setGeometry(QRect(500, 50, 131, 31))
        font18 = QFont()
        font18.setFamilies([u"Open Sans"])
        font18.setPointSize(11)
        font18.setBold(False)
        font18.setUnderline(False)
        self.label_71.setFont(font18)
        self.listWidget_2 = QListWidget(self.tab_7)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setGeometry(QRect(20, 90, 611, 281))
        self.btn70 = QPushButton(self.tab_7)
        self.btn70.setObjectName(u"btn70")
        self.btn70.setGeometry(QRect(540, 10, 91, 31))
        self.btn70.setFont(font15)
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.label_40 = QLabel(self.tab_4)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(40, 10, 61, 61))
        self.label_40.setStyleSheet(u"image: url(:/icons/images/images/person-feedback-svgrepo-com (1).svg);")
        self.label_40.setPixmap(QPixmap(u"../../../.designer/src/reports.png"))
        self.label_40.setScaledContents(True)
        self.label_41 = QLabel(self.tab_4)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(90, 20, 181, 51))
        font19 = QFont()
        font19.setFamilies([u"Myriad Pro Light"])
        font19.setPointSize(16)
        font19.setBold(True)
        font19.setKerning(True)
        self.label_41.setFont(font19)
        self.label_41.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_41.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_41.setScaledContents(True)
        self.label_41.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.notestable = QTableWidget(self.tab_4)
        if (self.notestable.columnCount() < 5):
            self.notestable.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.notestable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.notestable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.notestable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.notestable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.notestable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.notestable.setObjectName(u"notestable")
        self.notestable.setGeometry(QRect(20, 70, 611, 311))
        font20 = QFont()
        font20.setFamilies([u"Open Sans"])
        self.notestable.setFont(font20)
        self.notestable.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.notestable.setStyleSheet(u"/* ////////////////////////QTableWidget///////////////////////////// */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(32, 37, 42);\n"
"	gridline-color: rgba(189, 195, 199,50);\n"
"	border-bottom: 1px solid rgb(32, 37, 42);\n"
"\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(32, 37, 42);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgba(189, 195, 199,100);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(101,142,45);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(41, 51, 61);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(32, 37, 42);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgba(41, 51, 61,100);\n"
"	background-color: rgb(32, 37, 42);"
                        "\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"     background-color: rgb(32, 37, 42);\n"
"     	padding: 3px;\n"
"}\n"
"")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.listWidget = QListWidget(self.tab_5)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(20, 70, 611, 301))
        self.label_50 = QLabel(self.tab_5)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(370, 20, 81, 31))
        self.label_50.setFont(font4)
        self.label_50.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_50.setStyleSheet(u"")
        self.label_50.setScaledContents(True)
        self.label_50.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cb50 = QComboBox(self.tab_5)
        self.cb50.setObjectName(u"cb50")
        self.cb50.setGeometry(QRect(460, 20, 171, 31))
        self.cb50.setFont(font9)
        self.cb50.setStyleSheet(u"")
        self.label_51 = QLabel(self.tab_5)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(30, 20, 171, 31))
        self.label_51.setFont(font2)
        self.label_51.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_51.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_51.setScaledContents(True)
        self.label_51.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.tabWidget.addTab(self.tab_5, "")
        self.label_1 = QLabel(self.centralwidget)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(20, 30, 101, 61))
        self.label_1.setStyleSheet(u"image: url(:/images/images/images/log.png);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 40, 111, 51))
        font21 = QFont()
        font21.setFamilies([u"Cocon\u00ae Next Arabic"])
        font21.setPointSize(18)
        self.label_2.setFont(font21)
        self.frame_7 = QFrame(self.centralwidget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setEnabled(True)
        self.frame_7.setGeometry(QRect(500, 0, 151, 51))
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.minimizeBtn = QPushButton(self.frame_7)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        self.minimizeBtn.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.minimizeBtn.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon)
        self.minimizeBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.minimizeBtn)

        self.closeBtn = QPushButton(self.frame_7)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.closeBtn.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon1)
        self.closeBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.closeBtn)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 90, 571, 51))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.logout_btn = QPushButton(self.centralwidget)
        self.logout_btn.setObjectName(u"logout_btn")
        self.logout_btn.setGeometry(QRect(520, 50, 101, 41))
        font22 = QFont()
        font22.setFamilies([u"Open Sans"])
        font22.setPointSize(10)
        font22.setBold(True)
        font22.setItalic(False)
        self.logout_btn.setFont(font22)
        self.logout_btn.setStyleSheet(u"    #logout_btn{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(166, 200, 52, 90), stop:1 rgba(98, 142, 43, 90)); \n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px; \n"
"    border:1px solid rgb(26, 29, 34);\n"
"}\n"
"#logout_btn:hover{\n"
"	background-color: rgb(72, 76, 83);\n"
"}\n"
"\n"
"#logout_btn:pressed{\n"
"	background-color: rgb(28, 31, 36);\n"
"}")
        AdminWindow.setCentralWidget(self.centralwidget)
        self.frame.raise_()
        self.tabWidget.raise_()
        self.label_1.raise_()
        self.label_2.raise_()
        self.frame_7.raise_()
        self.logout_btn.raise_()
        self.statusbar = QStatusBar(AdminWindow)
        self.statusbar.setObjectName(u"statusbar")
        AdminWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AdminWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AdminWindow)
    # setupUi

    def retranslateUi(self, AdminWindow):
        AdminWindow.setWindowTitle(QCoreApplication.translate("AdminWindow", u"MainWindow", None))
        self.menu_01_01.setText(QCoreApplication.translate("AdminWindow", u"Add New Student", None))
        self.menu_01_02.setText(QCoreApplication.translate("AdminWindow", u"Edit / Delete Student", None))
        self.menu_02_01.setText(QCoreApplication.translate("AdminWindow", u"Add / Edit / Delete Marks", None))
        self.menu_03_01.setText(QCoreApplication.translate("AdminWindow", u"Add / Edit / Delete", None))
        self.menu_04_01.setText(QCoreApplication.translate("AdminWindow", u"Add / Edit / Delete", None))
        self.menu_05_01.setText(QCoreApplication.translate("AdminWindow", u"Students Reports", None))
        self.menu_05_02.setText(QCoreApplication.translate("AdminWindow", u"Marks Reports", None))
        self.menu_05_03.setText(QCoreApplication.translate("AdminWindow", u"Attendance Reports", None))
        self.menu_05_04.setText(QCoreApplication.translate("AdminWindow", u"Fees Reports", None))
        self.menu_06_01.setText(QCoreApplication.translate("AdminWindow", u"Logout", None))
        self.label_13.setText(QCoreApplication.translate("AdminWindow", u"\u0627\u062f\u062e\u0644 \u0645\u0639\u0644\u0648\u0645\u0627\u062a \u0627\u0644\u0637\u0627\u0644\u0628", None))
        self.label_12.setText(QCoreApplication.translate("AdminWindow", u"\u0627\u0636\u0627\u0641\u0629 \u0637\u0627\u0644\u0628 \u062c\u062f\u064a\u062f", None))
        self.label_11.setText("")
        self.tb10.setText("")
        self.label_15.setText(QCoreApplication.translate("AdminWindow", u"\u0627\u0644\u0627\u0633\u0645 \u0627\u0644\u0623\u0648\u0644", None))
        self.label_17.setText(QCoreApplication.translate("AdminWindow", u"\u0627\u0644\u062c\u0646\u0633", None))
        self.cb10.setItemText(0, QCoreApplication.translate("AdminWindow", u"M", None))
        self.cb10.setItemText(1, QCoreApplication.translate("AdminWindow", u"F", None))

        self.label_16.setText(QCoreApplication.translate("AdminWindow", u"\u0627\u0644\u0627\u0633\u0645 \u0627\u0644\u062b\u0627\u0646\u064a", None))
        self.tb11.setText("")
        self.tb12.setText("")
        self.label_14.setText(QCoreApplication.translate("AdminWindow", u"\u0631\u0642\u0645 \u0627\u0644\u062a\u0639\u0631\u064a\u0641", None))
        self.label_18.setText(QCoreApplication.translate("AdminWindow", u"\u0631\u0642\u0645 \u0627\u0644\u0647\u0627\u062a\u0641", None))
        self.label_19.setText(QCoreApplication.translate("AdminWindow", u"\u0627\u0644\u0628\u0631\u064a\u062f \u0627\u0644\u0627\u0644\u0643\u062a\u0631\u0648\u0646\u064a", None))
        self.tb13.setText("")
        self.tb14.setText("")
        self.label_191.setText(QCoreApplication.translate("AdminWindow", u"\u0627\u0644\u0635\u0648\u0631\u0629 \u0627\u0644\u0634\u062e\u0635\u064a\u0629", None))
        self.btn10.setText(QCoreApplication.translate("AdminWindow", u"\u062a\u0635\u0641\u062d", None))
        self.btn11.setText(QCoreApplication.translate("AdminWindow", u"\u062d\u0641\u0638 \u0627\u0644\u062a\u063a\u064a\u0631\u0627\u062a", None))
        self.filenamelabel.setText("")
        self.label_192.setText("")
        self.label_193.setText(QCoreApplication.translate("AdminWindow", u"\u0643\u0644\u0645\u0629 \u0627\u0644\u0645\u0631\u0648\u0631", None))
        self.tb15.setText("")
        self.label_194.setText(QCoreApplication.translate("AdminWindow", u"\u0635\u0648\u0631 \u0627\u0644\u0637\u0627\u0644\u0628", None))
        self.btn12.setText(QCoreApplication.translate("AdminWindow", u"\u062a\u0635\u0641\u062d", None))
        self.label_195.setText("")
        self.filenamelabel_4.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("AdminWindow", u"\u062a\u0633\u062c\u064a\u0644", None))
        self.label_20.setText("")
        self.label_21.setText(QCoreApplication.translate("AdminWindow", u"\u062a\u0639\u062f\u064a\u0644 \u0645\u0639\u0644\u0648\u0645\u0627\u062a \u0627\u0644\u0637\u0627\u0644\u0628", None))
        self.btn20.setText(QCoreApplication.translate("AdminWindow", u"\u062d\u0641\u0638 \u0627\u0644\u062a\u063a\u064a\u0631\u0627\u062a", None))
        self.btn21.setText(QCoreApplication.translate("AdminWindow", u"\u062d\u0630\u0641", None))
        self.label_23.setText(QCoreApplication.translate("AdminWindow", u"\u0631\u0642\u0645 \u0627\u0644\u062a\u0639\u0631\u064a\u0641", None))
        self.label_24.setText(QCoreApplication.translate("AdminWindow", u"\u0627\u0644\u0627\u0633\u0645 \u0627\u0644\u0627\u0648\u0644", None))
        self.label_25.setText(QCoreApplication.translate("AdminWindow", u"\u0627\u0644\u0627\u0633\u0645 \u0627\u0644\u0627\u062e\u064a\u0631", None))
        self.label_26.setText(QCoreApplication.translate("AdminWindow", u"\u0627\u0644\u062c\u0646\u0633", None))
        self.cb21.setItemText(0, QCoreApplication.translate("AdminWindow", u"M", None))
        self.cb21.setItemText(1, QCoreApplication.translate("AdminWindow", u"F", None))

        self.tb20.setText("")
        self.tb21.setText("")
        self.tb22.setText("")
        self.label_27.setText(QCoreApplication.translate("AdminWindow", u"\u0631\u0642\u0645 \u0627\u0644\u0647\u0627\u062a\u0641", None))
        self.label_28.setText(QCoreApplication.translate("AdminWindow", u"\u0627\u0644\u0628\u0631\u064a\u062f \u0627\u0644\u0627\u0644\u0643\u062a\u0631\u0648\u0646\u064a", None))
        self.tb23.setText("")
        self.label_29.setText(QCoreApplication.translate("AdminWindow", u"\u0627\u0644\u0635\u0648\u0631\u0629 \u0627\u0644\u0634\u062e\u0635\u064a\u0629", None))
        self.btn22.setText(QCoreApplication.translate("AdminWindow", u"\u062a\u0635\u0641\u062d", None))
        self.label_291.setText("")
        self.filenamelabel_2.setText("")
        self.label_292.setText(QCoreApplication.translate("AdminWindow", u"\u0643\u0644\u0645\u0629 \u0627\u0644\u0645\u0631\u0648\u0631", None))
        self.tb24.setText("")
        self.label_294.setText(QCoreApplication.translate("AdminWindow", u"\u0635\u0648\u0631 \u0627\u0644\u0637\u0627\u0644\u0628", None))
        self.btn23.setText(QCoreApplication.translate("AdminWindow", u"\u062a\u0635\u0641\u062d", None))
        self.filenamelabel_3.setText("")
        self.label_293.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("AdminWindow", u"\u062a\u0639\u062f\u064a\u0644 \u0627\u0644\u0645\u0639\u0644\u0648\u0645\u0627\u062a", None))
        self.groupBox.setTitle("")
        self.label_30.setText(QCoreApplication.translate("AdminWindow", u"\u0627\u062f\u062e\u0644 \u0627\u0644\u0639\u0644\u0627\u0645\u0627\u062a :", None))
        self.btn30.setText(QCoreApplication.translate("AdminWindow", u"\u062d\u0641\u0638", None))
        self.label_31.setText(QCoreApplication.translate("AdminWindow", u"\u0631\u0642\u0645 \u0627\u0644\u062a\u0639\u0631\u064a\u0641", None))
        self.label_32.setText(QCoreApplication.translate("AdminWindow", u"\u0627\u0644\u0627\u0645\u062a\u062d\u0627\u0646", None))
        self.label_33.setText(QCoreApplication.translate("AdminWindow", u"\u062a\u0639\u062f\u064a\u0644 \u0627\u0644\u0639\u0644\u0627\u0645\u0629", None))
        self.tb31.setText("")
        self.tb30.setText("")
        self.groupBox_2.setTitle("")
        self.label_34.setText(QCoreApplication.translate("AdminWindow", u"\u062a\u0639\u062f\u064a\u0644 \u0627\u0644\u0639\u0644\u0627\u0645\u0627\u062a :", None))
        self.btn32.setText(QCoreApplication.translate("AdminWindow", u"\u062d\u0641\u0638 \u0627\u0644\u062a\u063a\u064a\u064a\u0631\u0627\u062a", None))
        self.btn31.setText(QCoreApplication.translate("AdminWindow", u"\u0627\u0644\u062d\u0635\u0648\u0644 \u0639\u0644\u0649 \u0627\u0644\u0639\u0644\u0627\u0645\u0629", None))
        self.btn33.setText(QCoreApplication.translate("AdminWindow", u"\u062d\u0630\u0641", None))
        self.label_35.setText(QCoreApplication.translate("AdminWindow", u"\u0631\u0642\u0645 \u0627\u0644\u062a\u0639\u0631\u064a\u0641", None))
        self.label_36.setText(QCoreApplication.translate("AdminWindow", u"\u0627\u0644\u0627\u0645\u062a\u062d\u0627\u0646", None))
        self.label_37.setText(QCoreApplication.translate("AdminWindow", u"\u062a\u0639\u062f\u064a\u0644 \u0627\u0644\u0639\u0644\u0627\u0645\u0629", None))
        self.tb33.setText("")
        self.tb32.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("AdminWindow", u"\u0627\u0644\u0639\u0644\u0627\u0645\u0627\u062a", None))
        self.label_60.setText(QCoreApplication.translate("AdminWindow", u"\u0627\u062f\u062e\u0644 \u0627\u0633\u0645 \u0627\u0644\u0627\u0645\u062a\u062d\u0627\u0646", None))
        self.label_61.setText(QCoreApplication.translate("AdminWindow", u"\u0627\u0644\u0633\u0624\u0627\u0644:", None))
        self.label_62.setText(QCoreApplication.translate("AdminWindow", u"Option A:", None))
        self.label_63.setText(QCoreApplication.translate("AdminWindow", u"Option B:", None))
        self.label_64.setText(QCoreApplication.translate("AdminWindow", u"Option C:", None))
        self.label_65.setText(QCoreApplication.translate("AdminWindow", u"Option D:", None))
        self.label_691.setText(QCoreApplication.translate("AdminWindow", u"\u0627\u0644\u062c\u0648\u0627\u0628 \u0627\u0644\u0635\u062d\u064a\u062d", None))
        self.cb61.setItemText(0, QCoreApplication.translate("AdminWindow", u"A", None))
        self.cb61.setItemText(1, QCoreApplication.translate("AdminWindow", u"B", None))
        self.cb61.setItemText(2, QCoreApplication.translate("AdminWindow", u"C", None))
        self.cb61.setItemText(3, QCoreApplication.translate("AdminWindow", u"D", None))

        self.btn60.setText(QCoreApplication.translate("AdminWindow", u"\u0627\u062f\u062e\u0644 \u0627\u0644\u0633\u0624\u0627\u0644", None))
        self.label_67.setText(QCoreApplication.translate("AdminWindow", u"\u0627\u0644\u0639\u0644\u0627\u0645\u0629", None))
        self.label_68.setText(QCoreApplication.translate("AdminWindow", u"\u0627\u0644\u0639\u0644\u0627\u0645\u0629", None))
        self.label_69.setText(QCoreApplication.translate("AdminWindow", u"\u0627\u0644\u0639\u0644\u0627\u0645\u0629", None))
        self.label_690.setText(QCoreApplication.translate("AdminWindow", u"\u0627\u0644\u0639\u0644\u0627\u0645\u0629", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("AdminWindow", u"\u0627\u0646\u0634\u0627\u0621 \u0627\u0644\u0627\u0645\u062a\u062d\u0627\u0646", None))
        self.label_70.setText(QCoreApplication.translate("AdminWindow", u"\u0627\u062f\u062e\u0644 \u0627\u0633\u0645 \u0627\u0644\u0627\u0645\u062a\u062d\u0627\u0646", None))
        self.label_71.setText(QCoreApplication.translate("AdminWindow", u"\u0642\u0648\u0627\u0644\u0628 \u0627\u0644\u0627\u0633\u0626\u0644\u0629:", None))
        self.btn70.setText(QCoreApplication.translate("AdminWindow", u"\u062d\u0630\u0641 \u0627\u0644\u0633\u0624\u0627\u0644", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("AdminWindow", u"\u0627\u0644\u0646\u0645\u0627\u0630\u062c", None))
        self.label_40.setText("")
        self.label_41.setText(QCoreApplication.translate("AdminWindow", u"\u0645\u0644\u0627\u062d\u0638\u0627\u062a \u0627\u0644\u0637\u0644\u0627\u0628", None))
        ___qtablewidgetitem = self.notestable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AdminWindow", u"\u0631\u0642\u0645 \u0627\u0644\u062a\u0639\u0631\u064a\u0641", None));
        ___qtablewidgetitem1 = self.notestable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AdminWindow", u"\u0627\u0644\u0627\u0633\u0645", None));
        ___qtablewidgetitem2 = self.notestable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("AdminWindow", u"\u0627\u0645\u062a\u062d\u0627\u0646", None));
        ___qtablewidgetitem3 = self.notestable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("AdminWindow", u"\u0627\u0644\u062a\u0627\u0631\u064a\u062e", None));
        ___qtablewidgetitem4 = self.notestable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("AdminWindow", u"\u0627\u0644\u0645\u0644\u0627\u062d\u0638\u0629", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("AdminWindow", u"\u0627\u0644\u0645\u0644\u0627\u062d\u0638\u0627\u062a", None))
        self.label_50.setText(QCoreApplication.translate("AdminWindow", u"\u0631\u0642\u0645 \u0627\u0644\u062a\u0639\u0631\u064a\u0641", None))
        self.label_51.setText(QCoreApplication.translate("AdminWindow", u"\u0633\u062c\u0644 \u0627\u0644\u0641\u064a\u062f\u064a\u0648\u0647\u0627\u062a ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("AdminWindow", u"\u0633\u062c\u0644 \u0627\u0644\u0641\u064a\u062f\u064a\u0648\u0647\u0627\u062a", None))
        self.label_1.setText("")
        self.label_2.setText(QCoreApplication.translate("AdminWindow", u" \u0646\u0638\u0627\u0645 \u0623\u0645\u0627\u0646 ", None))
#if QT_CONFIG(tooltip)
        self.minimizeBtn.setToolTip(QCoreApplication.translate("AdminWindow", u"Minimize Window", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate("AdminWindow", u"Close Window", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText("")
        self.logout_btn.setText(QCoreApplication.translate("AdminWindow", u"\u062a\u0633\u062c\u064a\u0644 \u0627\u0644\u062e\u0631\u0648\u062c", None))
    # retranslateUi

