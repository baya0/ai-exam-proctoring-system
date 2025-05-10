# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainMenuZjsAGD.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
from Custom_Widgets.Widgets import QCustomStackedWidget
import resources_rc
import resources_rc

class Ui_SecondWindow(object):
    def setupUi(self, SecondWindow):
        if not SecondWindow.objectName():
            SecondWindow.setObjectName(u"SecondWindow")
        SecondWindow.resize(982, 594)
        SecondWindow.setMaximumSize(QSize(982, 594))
        SecondWindow.setStyleSheet(u"*{\n"
"border:None;\n"
"border-radius:5px;\n"
"background-color: transparent;\n"
"background:transparent;\n"
"padding: 0;\n"
"margin :0;\n"
"color: #fff\n"
"}\n"
"#centralwidget{\n"
"background-color: rgb(40, 44, 52);\n"
"\n"
"}\n"
"#LeftMenuSubContainer , #rightMenuSubContainer{\n"
"  background-color: rgb(30, 33, 39); \n"
"}\n"
"QPushButton{\n"
"text-align: left;\n"
"padding: 2px 5px;\n"
"}\n"
"#leftMenuSubContainerQPushButton{\n"
"text-aligh:left;\n"
"padding:5px 10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"}\n"
"\n"
"#centerMenuSubContainer,  #rightMenuSubContainer{\n"
"background-color: rgb(44, 49, 58);\n"
"}\n"
"#frame_4, #frame_8 , #popupNotifiactionSubContainer{\n"
"background-color: rgb(30, 33, 39);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"#headerContainer {\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
" #footerContainer{\n"
"background-color: rgb(30, 33, 39);\n"
"}\n"
"/*/////page_profile/////////////*/\n"
"#rightMenuSubContainer{\n"
"border-radius:10px;\n"
"}\n"
""
                        "/*//////////////////////buttons///////////////////////////////////*/\n"
"#homeBtn:hover {  \n"
"  background-color: rgb(44, 49, 57);\n"
"  border-style: solid;\n"
"border-radius: 10px;\n"
"}\n"
"#homeBtn:pressed {\n"
"  background-color: rgb(23, 26, 30);\n"
"  border-style: solid;\n"
"  border-radius: 10px;\n"
"}\n"
"/*//////////////////////Files///////////////////////////////////*/\n"
"#FilesBtn:hover { \n"
"  background-color: rgb(44, 49, 57);\n"
"  border-style: solid;\n"
" border-radius: 10px;\n"
"}\n"
"#FilesBtn:pressed {\n"
" background-color: rgb(23, 26, 30);\n"
"  border-style: solid;\n"
"  border-radius: 10px;\n"
"}\n"
"/*//////////////////////Setting///////////////////////////////////*/\n"
"#SettingsBtn:hover { \n"
"  background-color: rgb(44, 49, 57);\n"
"  border-style: solid;\n"
" border-radius: 10px;\n"
"}\n"
"#SettignsBtn:pressed {\n"
" background-color: rgb(23, 26, 30);\n"
"  border-style: solid;\n"
"  border-radius: 10px;\n"
"}\n"
"/*//////////////////////help//////////////////////////////////"
                        "/*/\n"
"\n"
"#helpBtn:hover { \n"
"  background-color: rgb(44, 49, 57);\n"
"  border-style: solid;\n"
" border-radius: 10px;\n"
"}\n"
"#helpBtn:pressed {\n"
" background-color: rgb(23, 26, 30);\n"
"  border-style: solid;\n"
"  border-radius: 10px;\n"
"}\n"
"/*//////////////////////instructions///////////////////////////////////*/\n"
"#instructionsBtn:hover { \n"
"  background-color: rgb(44, 49, 57);\n"
"  border-style: solid;\n"
" border-radius: 10px;\n"
"}\n"
"#instructionsBtn:pressed {\n"
" background-color: rgb(23, 26, 30);\n"
"  border-style: solid;\n"
"  border-radius: 10px;\n"
"}\n"
"/*///////////////////////*/\n"
"\n"
"#closeBtn:hover { \n"
"  background-color: rgb(44, 49, 57);\n"
"  border-style: solid;\n"
" border-radius: 10px;\n"
"}\n"
"#closeBtn:pressed {\n"
" background-color: rgb(23, 26, 30);\n"
"  border-style: solid;\n"
"  border-radius: 10px;\n"
"}\n"
"/*/////////////////////page-home///////////////////*/\n"
"\n"
"#widget_home{\n"
"border-radius:40px;\n"
"border:1px; solid black;\n"
"background"
                        "-color: rgb(44, 49, 58);\n"
"}\n"
"#testinst{\n"
"color:rgba(255,255,255,255);\n"
"font: 300 12pt \"Cocon modified\";\n"
"background-color: rgba(215,210,210,20);\n"
"border-radius:10px;\n"
"border:1px; solid black;\n"
"}\n"
"#testlogo{\n"
"image: url(:/images/images/images/live-proctoring.png);\n"
"}\n"
"#testcode{\n"
"background-color: rgb(33, 37, 43);\n"
"border-radius:10px;\n"
"border:5px;\n"
"}\n"
"\n"
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
"     subcontrol-position: bott"
                        "om;\n"
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
""
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
"\n"
"/*///////////////page-file /////////*/\n"
"#examinfo {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"#examinfo::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"#examinfot::item:selected{\n"
""
                        "	\n"
"	background-color: rgb(101, 142, 45);\n"
"}\n"
"/*///////////////*/\n"
"#testverify{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(33, 37, 43, 100), stop:1 rgba(30, 33, 39, 255));\n"
" border-radius: 10px;}\n"
"\n"
"#testverify:pressed {\n"
"background-color: rgb(55, 63, 77);\n"
"}\n"
"#testverify:hover {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(33, 37, 43, 100), stop:1 rgba(61, 72, 61, 255));\n"
"}\n"
"\n"
"/* ////////////////////////QTableWidget///////////////////////////// */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(32, 37, 42);\n"
"	gridline-color: rgba(189, 195, 199,50);\n"
"	border-bottom: 1px solid rgb(32, 37, 42);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(32, 37, 42);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgba(189, 195, 199,100);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-col"
                        "or: rgb(101,142,45);\n"
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
"	background-color: rgb(32, 37, 42);\n"
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
        self.centralwidget = QWidget(SecondWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(982, 594))
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.LeftMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.LeftMenuContainer.setObjectName(u"LeftMenuContainer")
        self.LeftMenuContainer.setMaximumSize(QSize(45, 16777215))
        self.verticalLayout = QVBoxLayout(self.LeftMenuContainer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.LeftMenuSubContainer = QWidget(self.LeftMenuContainer)
        self.LeftMenuSubContainer.setObjectName(u"LeftMenuSubContainer")
        self.LeftMenuSubContainer.setStyleSheet(u"border-radius:7px;")
        self.verticalLayout_2 = QVBoxLayout(self.LeftMenuSubContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.LeftMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 6, 0, 0)
        self.menuBtn = QPushButton(self.frame)
        self.menuBtn.setObjectName(u"menuBtn")
        self.menuBtn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.menuBtn.setAutoFillBackground(False)
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.menuBtn, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignTop)

        self.frame_2 = QFrame(self.LeftMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.homeBtn = QPushButton(self.frame_2)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/cil-home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.homeBtn.setIcon(icon1)
        self.homeBtn.setIconSize(QSize(36, 36))

        self.verticalLayout_4.addWidget(self.homeBtn)

        self.FilesBtn = QPushButton(self.frame_2)
        self.FilesBtn.setObjectName(u"FilesBtn")
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/cil-file.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.FilesBtn.setIcon(icon2)
        self.FilesBtn.setIconSize(QSize(36, 36))

        self.verticalLayout_4.addWidget(self.FilesBtn)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignmentFlag.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.LeftMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.helpBtn = QPushButton(self.frame_3)
        self.helpBtn.setObjectName(u"helpBtn")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/cil-phone.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.helpBtn.setIcon(icon3)
        self.helpBtn.setIconSize(QSize(36, 36))

        self.verticalLayout_5.addWidget(self.helpBtn)

        self.instructionsBtn = QPushButton(self.frame_3)
        self.instructionsBtn.setObjectName(u"instructionsBtn")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-find-in-page.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.instructionsBtn.setIcon(icon4)
        self.instructionsBtn.setIconSize(QSize(36, 36))

        self.verticalLayout_5.addWidget(self.instructionsBtn)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout.addWidget(self.LeftMenuSubContainer)


        self.horizontalLayout.addWidget(self.LeftMenuContainer)

        self.centerMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.centerMenuContainer.setObjectName(u"centerMenuContainer")
        self.centerMenuContainer.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.centerMenuContainer)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.centerMenuSubContainer = QWidget(self.centerMenuContainer)
        self.centerMenuSubContainer.setObjectName(u"centerMenuSubContainer")
        self.centerMenuSubContainer.setMinimumSize(QSize(200, 0))
        self.centerMenuSubContainer.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.centerMenuSubContainer)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.frame_4 = QFrame(self.centerMenuSubContainer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 9, 0, 9)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.closeCenterMenuBtn = QPushButton(self.frame_4)
        self.closeCenterMenuBtn.setObjectName(u"closeCenterMenuBtn")
        self.closeCenterMenuBtn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-x-circle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeCenterMenuBtn.setIcon(icon5)
        self.closeCenterMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.closeCenterMenuBtn, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_7.addWidget(self.frame_4)

        self.centerMenuPages = QCustomStackedWidget(self.centerMenuSubContainer)
        self.centerMenuPages.setObjectName(u"centerMenuPages")
        self.page_help = QWidget()
        self.page_help.setObjectName(u"page_help")
        self.verticalLayout_9 = QVBoxLayout(self.page_help)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_3 = QLabel(self.page_help)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        self.label_3.setFont(font1)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_3)

        self.centerMenuPages.addWidget(self.page_help)
        self.page_inst = QWidget()
        self.page_inst.setObjectName(u"page_inst")
        self.verticalLayout_10 = QVBoxLayout(self.page_inst)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.scrollArea = QScrollArea(self.page_inst)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 325, 1536))
        self.scrollAreaWidgetContents_2.setStyleSheet(u"\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.verticalLayout_20 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_11 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(100, 1100))
        self.frame_11.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_11.setStyleSheet(u"")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_11)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_4 = QLabel(self.frame_11)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 1500))
        font2 = QFont()
        font2.setFamilies([u"Cocon modified"])
        font2.setPointSize(11)
        self.label_4.setFont(font2)
        self.label_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.label_4.setWordWrap(True)
        self.label_4.setMargin(3)

        self.verticalLayout_8.addWidget(self.label_4, 0, Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_20.addWidget(self.frame_11)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_10.addWidget(self.scrollArea)

        self.centerMenuPages.addWidget(self.page_inst)

        self.verticalLayout_7.addWidget(self.centerMenuPages)


        self.verticalLayout_6.addWidget(self.centerMenuSubContainer, 0, Qt.AlignmentFlag.AlignLeft)


        self.horizontalLayout.addWidget(self.centerMenuContainer)

        self.MainBodyContainer = QWidget(self.centralwidget)
        self.MainBodyContainer.setObjectName(u"MainBodyContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.MainBodyContainer.sizePolicy().hasHeightForWidth())
        self.MainBodyContainer.setSizePolicy(sizePolicy1)
        self.MainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_11 = QVBoxLayout(self.MainBodyContainer)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.MainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        self.horizontalLayout_4 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(6, 0, 0, 0)
        self.frame_5 = QFrame(self.headerContainer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setSpacing(9)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(35, 28))
        font3 = QFont()
        font3.setPointSize(15)
        self.label_5.setFont(font3)
        self.label_5.setPixmap(QPixmap(u":/images/images/images/log.png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.label_5)


        self.horizontalLayout_4.addWidget(self.frame_5, 0, Qt.AlignmentFlag.AlignLeft)

        self.frame_6 = QFrame(self.headerContainer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, -1)
        self.profileMenuBtn = QPushButton(self.frame_6)
        self.profileMenuBtn.setObjectName(u"profileMenuBtn")
        self.profileMenuBtn.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/cil-user.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.profileMenuBtn.setIcon(icon6)
        self.profileMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.profileMenuBtn)

        self.logoutBtn = QPushButton(self.frame_6)
        self.logoutBtn.setObjectName(u"logoutBtn")
        self.logoutBtn.setStyleSheet(u"image: url(:/icons/images/images/sign-out-svgrepo-com.svg);")
        self.logoutBtn.setIconSize(QSize(50, 50))

        self.horizontalLayout_5.addWidget(self.logoutBtn)


        self.horizontalLayout_4.addWidget(self.frame_6, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)

        self.frame_7 = QFrame(self.headerContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setEnabled(True)
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.minimizeBtn = QPushButton(self.frame_7)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        self.minimizeBtn.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        icon7 = QIcon()
        icon7.addFile(u":/icons/images/icons/cil-minus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeBtn.setIcon(icon7)
        self.minimizeBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.minimizeBtn)

        self.closeBtn = QPushButton(self.frame_7)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        icon8 = QIcon()
        icon8.addFile(u":/icons/images/icons/cil-x.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeBtn.setIcon(icon8)
        self.closeBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.closeBtn)


        self.horizontalLayout_4.addWidget(self.frame_7, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_11.addWidget(self.headerContainer, 0, Qt.AlignmentFlag.AlignTop)

        self.mainBodyContent = QWidget(self.MainBodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy2)
        self.mainBodyContent.setMinimumSize(QSize(576, 349))
        self.mainBodyContent.setStyleSheet(u"")
        self.horizontalLayout_7 = QHBoxLayout(self.mainBodyContent)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.mainContentsContainer = QWidget(self.mainBodyContent)
        self.mainContentsContainer.setObjectName(u"mainContentsContainer")
        self.verticalLayout_16 = QVBoxLayout(self.mainContentsContainer)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.mainPages = QCustomStackedWidget(self.mainContentsContainer)
        self.mainPages.setObjectName(u"mainPages")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.page_home.setStyleSheet(u"")
        self.horizontalLayout_13 = QHBoxLayout(self.page_home)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.widget_home = QWidget(self.page_home)
        self.widget_home.setObjectName(u"widget_home")
        self.widget_home.setStyleSheet(u"")
        self.verticalLayout_17 = QVBoxLayout(self.widget_home)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.testlogo = QLabel(self.widget_home)
        self.testlogo.setObjectName(u"testlogo")
        self.testlogo.setMinimumSize(QSize(298, 180))
        self.testlogo.setStyleSheet(u"image: url(:/images/images/images/live-proctoring.png);")

        self.verticalLayout_17.addWidget(self.testlogo)

        self.horizontalSpacer = QSpacerItem(40, 50, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_17.addItem(self.horizontalSpacer)

        self.testinst = QLabel(self.widget_home)
        self.testinst.setObjectName(u"testinst")
        sizePolicy.setHeightForWidth(self.testinst.sizePolicy().hasHeightForWidth())
        self.testinst.setSizePolicy(sizePolicy)
        self.testinst.setMinimumSize(QSize(130, 20))
        self.testinst.setMaximumSize(QSize(300, 35))
        font4 = QFont()
        font4.setFamilies([u"Cocon modified"])
        font4.setPointSize(12)
        font4.setWeight(QFont.Light)
        font4.setItalic(False)
        self.testinst.setFont(font4)
        self.testinst.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.testinst.setAutoFillBackground(False)
        self.testinst.setStyleSheet(u"")
        self.testinst.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_17.addWidget(self.testinst, 0, Qt.AlignmentFlag.AlignHCenter)

        self.testcode = QLineEdit(self.widget_home)
        self.testcode.setObjectName(u"testcode")
        self.testcode.setMinimumSize(QSize(20, 35))
        font5 = QFont()
        font5.setPointSize(12)
        self.testcode.setFont(font5)
        self.testcode.setMaxLength(8)
        self.testcode.setCursorPosition(0)

        self.verticalLayout_17.addWidget(self.testcode, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.testverify = QPushButton(self.widget_home)
        self.testverify.setObjectName(u"testverify")
        self.testverify.setMinimumSize(QSize(70, 35))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(10)
        self.testverify.setFont(font6)
        self.testverify.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.testverify.setAutoFillBackground(False)
        self.testverify.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.testverify.setIconSize(QSize(16, 16))
        self.testverify.setAutoDefault(False)
        self.testverify.setFlat(False)

        self.verticalLayout_17.addWidget(self.testverify, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.horizontalLayout_13.addWidget(self.widget_home)

        self.mainPages.addWidget(self.page_home)
        self.page_file = QWidget()
        self.page_file.setObjectName(u"page_file")
        self.verticalLayout_15 = QVBoxLayout(self.page_file)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.tableWidget = QTableWidget(self.page_file)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        font7 = QFont()
        font7.setFamilies([u"Open Sans"])
        font7.setPointSize(10)
        font7.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font7);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font7);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font7);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font7);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        font8 = QFont()
        font8.setFamilies([u"Open Sans"])
        font8.setPointSize(10)
        self.tableWidget.setFont(font8)
        self.tableWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.tableWidget.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)

        self.verticalLayout_15.addWidget(self.tableWidget)

        self.mainPages.addWidget(self.page_file)

        self.verticalLayout_16.addWidget(self.mainPages)


        self.horizontalLayout_7.addWidget(self.mainContentsContainer)

        self.rightMenuContainer = QCustomSlideMenu(self.mainBodyContent)
        self.rightMenuContainer.setObjectName(u"rightMenuContainer")
        self.rightMenuContainer.setMinimumSize(QSize(200, 0))
        self.rightMenuContainer.setMaximumSize(QSize(200, 331))
        self.verticalLayout_12 = QVBoxLayout(self.rightMenuContainer)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.rightMenuSubContainer = QWidget(self.rightMenuContainer)
        self.rightMenuSubContainer.setObjectName(u"rightMenuSubContainer")
        self.rightMenuSubContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_13 = QVBoxLayout(self.rightMenuSubContainer)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(5, 5, 5, 5)
        self.frame_8 = QFrame(self.rightMenuSubContainer)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_7 = QLabel(self.frame_8)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_7)

        self.closeRightMenuBtn = QPushButton(self.frame_8)
        self.closeRightMenuBtn.setObjectName(u"closeRightMenuBtn")
        self.closeRightMenuBtn.setIcon(icon5)
        self.closeRightMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.closeRightMenuBtn, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_13.addWidget(self.frame_8)

        self.rightMenuPages = QCustomStackedWidget(self.rightMenuSubContainer)
        self.rightMenuPages.setObjectName(u"rightMenuPages")
        self.page_profile = QWidget()
        self.page_profile.setObjectName(u"page_profile")
        self.page_profile.setStyleSheet(u"")
        self.verticalLayout_14 = QVBoxLayout(self.page_profile)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.profile_pic = QLabel(self.page_profile)
        self.profile_pic.setObjectName(u"profile_pic")
        self.profile_pic.setMinimumSize(QSize(0, 0))
        self.profile_pic.setMaximumSize(QSize(16777215, 16777215))
        self.profile_pic.setFont(font5)
        self.profile_pic.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.profile_pic)

        self.frame_12 = QFrame(self.page_profile)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_12)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_2 = QLabel(self.frame_12)
        self.label_2.setObjectName(u"label_2")
        font9 = QFont()
        font9.setBold(True)
        self.label_2.setFont(font9)

        self.verticalLayout_21.addWidget(self.label_2)

        self.profile_name = QLabel(self.frame_12)
        self.profile_name.setObjectName(u"profile_name")
        self.profile_name.setMaximumSize(QSize(16777215, 16777215))
        font10 = QFont()
        font10.setPointSize(9)
        font10.setBold(False)
        self.profile_name.setFont(font10)
        self.profile_name.setAutoFillBackground(False)
        self.profile_name.setStyleSheet(u"border:1px solid rgb(70, 79, 93);\n"
"border-radius:10px;")
        self.profile_name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_21.addWidget(self.profile_name)

        self.label_8 = QLabel(self.frame_12)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font9)

        self.verticalLayout_21.addWidget(self.label_8)

        self.profile_id = QLabel(self.frame_12)
        self.profile_id.setObjectName(u"profile_id")
        self.profile_id.setMaximumSize(QSize(16777215, 16777215))
        font11 = QFont()
        font11.setPointSize(9)
        self.profile_id.setFont(font11)
        self.profile_id.setStyleSheet(u"border:1px solid rgb(70, 79, 93);\n"
"border-radius:10px;\n"
"")
        self.profile_id.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_21.addWidget(self.profile_id)


        self.verticalLayout_14.addWidget(self.frame_12)

        self.rightMenuPages.addWidget(self.page_profile)

        self.verticalLayout_13.addWidget(self.rightMenuPages)


        self.verticalLayout_12.addWidget(self.rightMenuSubContainer)


        self.horizontalLayout_7.addWidget(self.rightMenuContainer, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_11.addWidget(self.mainBodyContent)

        self.footerContainer = QWidget(self.MainBodyContainer)
        self.footerContainer.setObjectName(u"footerContainer")
        self.footerContainer.setStyleSheet(u"")
        self.horizontalLayout_12 = QHBoxLayout(self.footerContainer)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.footerContainer)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_14 = QLabel(self.frame_10)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_10.addWidget(self.label_14)


        self.horizontalLayout_12.addWidget(self.frame_10)

        self.sizeGrip = QFrame(self.footerContainer)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(10, 10))
        self.sizeGrip.setMaximumSize(QSize(10, 10))
        self.sizeGrip.setStyleSheet(u"")
        self.sizeGrip.setFrameShape(QFrame.Shape.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.sizeGrip)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_15 = QLabel(self.sizeGrip)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_11.addWidget(self.label_15)


        self.horizontalLayout_12.addWidget(self.sizeGrip)


        self.verticalLayout_11.addWidget(self.footerContainer)


        self.horizontalLayout.addWidget(self.MainBodyContainer)

        SecondWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SecondWindow)

        self.centerMenuPages.setCurrentIndex(1)
        self.mainPages.setCurrentIndex(0)
        self.testverify.setDefault(False)


        QMetaObject.connectSlotsByName(SecondWindow)
    # setupUi

    def retranslateUi(self, SecondWindow):
        SecondWindow.setWindowTitle(QCoreApplication.translate("SecondWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("SecondWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.homeBtn.setToolTip(QCoreApplication.translate("SecondWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.homeBtn.setText(QCoreApplication.translate("SecondWindow", u"Home", None))
#if QT_CONFIG(tooltip)
        self.FilesBtn.setToolTip(QCoreApplication.translate("SecondWindow", u"Files", None))
#endif // QT_CONFIG(tooltip)
        self.FilesBtn.setText(QCoreApplication.translate("SecondWindow", u"Files", None))
#if QT_CONFIG(tooltip)
        self.helpBtn.setToolTip(QCoreApplication.translate("SecondWindow", u"Get more help", None))
#endif // QT_CONFIG(tooltip)
        self.helpBtn.setText(QCoreApplication.translate("SecondWindow", u"Help", None))
#if QT_CONFIG(tooltip)
        self.instructionsBtn.setToolTip(QCoreApplication.translate("SecondWindow", u"get instructions ", None))
#endif // QT_CONFIG(tooltip)
        self.instructionsBtn.setText(QCoreApplication.translate("SecondWindow", u"instructions", None))
        self.label.setText(QCoreApplication.translate("SecondWindow", u"More menu", None))
#if QT_CONFIG(tooltip)
        self.closeCenterMenuBtn.setToolTip(QCoreApplication.translate("SecondWindow", u"Close menu", None))
#endif // QT_CONFIG(tooltip)
        self.closeCenterMenuBtn.setText("")
        self.label_3.setText(QCoreApplication.translate("SecondWindow", u"Help ?", None))
        self.label_4.setText(QCoreApplication.translate("SecondWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">\u0627\u0644\u0627\u0631\u0634\u0627\u062f\u0627\u062a </span></p><p align=\"center\"><br/></p><p align=\"right\"><span style=\" font-size:12pt;\">\u062d\u0627\u0648\u0644 \u0627\u0646 \u064a\u0643\u0648\u0646 \u0627\u0644\u0648\u062c\u0647 \u0645\u0636\u0627\u0621 \u0628\u0634\u0643\u0644 \u0645\u062a\u0633\u0627\u0648\u064d \u060c \u0648\u064a\u062c\u0628 \u0639\u062f\u0645 \u062a\u0648\u062c\u064a\u0647 \u0645\u0635\u062f\u0631 \u0627\u0644\u0636\u0648\u0621 \u0646\u062d\u0648 \u0627\u0644\u0643\u0627\u0645\u064a\u0631\u0627 \u0623\u0648 \u0625\u0636\u0627\u0621\u0629 \u0646\u0635\u0641 \u0627\u0644\u0648\u062c\u0647 \u0641\u0642\u0637</span></p><p align=\"right\"><span style=\" font-size:12pt;\">\u0648 \u0623\u0644\u0627 \u064a\u0643\u0648\u0646 \u0647\u0646\u0627\u0643 \u0623\u064a \u0623\u0634\u062e\u0627\u0635 \u0622\u062e\u0631\u0648\u0646 \u0641\u064a \u0627\u0644\u063a\u0631\u0641\u0629</span></p><p align=\"right"
                        "\"><br/></p><p align=\"right\"><span style=\" font-size:12pt;\">\u064a\u062c\u0628 \u0623\u0644\u0627 \u062a\u0643\u0648\u0646 \u0647\u0646\u0627\u0643 \u0623\u0635\u0648\u0627\u062a \u0623\u0648 \u0636\u0648\u0636\u0627\u0621 \u0641\u064a \u0627\u0644\u062e\u0644\u0641\u064a\u0629 \u060c \u0648\u0645\u0646 \u0627\u0644\u0623\u0641\u0636\u0644 \u0625\u062c\u0631\u0627\u0621 \u0627\u0644\u0627\u062e\u062a\u0628\u0627\u0631 \u0641\u064a \u0635\u0645\u062a</span></p><p align=\"right\"><br/></p><p align=\"right\"><span style=\" font-size:12pt;\">\u062a\u062d\u0642\u0642 \u0645\u0646 \u0648\u062c\u0648\u062f \u0627\u062a\u0635\u0627\u0644 \u0627\u0646\u062a\u0631\u0646\u062a \u0643\u0627\u0641\u064a</span></p><p align=\"right\"><br/></p><p align=\"right\"><span style=\" font-size:12pt;\">\u0641\u064a \u062d\u0627\u0644 \u0627\u0643\u062a\u0634\u0627\u0641 \u0645\u062d\u0627\u0648\u0644\u0629 \u062e\u062f\u0627\u0639 \u0627\u0644\u0646\u0638\u0627\u0645 \u060c \u064a\u062a\u0645 \u0625\u0628\u0637\u0627\u0644 \u0646"
                        "\u062a\u0627\u0626\u062c \u0627\u0644\u0627\u0645\u062a\u062d\u0627\u0646</span></p><p align=\"right\"><br/></p><p align=\"right\"><span style=\" font-size:12pt;\">\u062d\u0627\u0641\u0638 \u0639\u0644\u0649 \u0628\u0642\u0627\u0621 \u0648\u062c\u0647\u0643 \u0641\u064a \u0645\u0631\u0643\u0632 \u0645\u062c\u0627\u0644 \u0631\u0624\u064a\u0629 \u0643\u0627\u0645\u064a\u0631\u0627 \u0627\u0644\u0648\u064a\u0628</span></p><p align=\"right\"><br/></p><p align=\"right\"><span style=\" font-size:12pt;\">\u0644\u0627 \u062a\u0642\u0645 \u0628\u0627\u064a \u0634\u0643\u0644 \u0645\u0646 \u0627\u0644\u0623\u0634\u0643\u0627\u0644 \u0628\u062a\u0633\u062c\u064a\u0644 \u0645\u062d\u062a\u0648\u064a\u0627\u062a \u0627\u0644\u0627\u0645\u062a\u062d\u0627\u0646 \u0627\u0648 \u0645\u0634\u0627\u0631\u0643\u062a\u0647\u0627 \u0645\u0639 \u0623\u064a \u0637\u0631\u0641 \u062b\u0627\u0644\u062b </span></p><p align=\"right\"><br/></p><p align=\"right\"><span style=\" font-size:12pt;\">\u0644\u0627 \u062a\u0642\u0645 \u0628\u0625"
                        "\u0631\u062a\u062f\u0627\u0621 \u0627\u0644\u0646\u0638\u0627\u0631\u0627\u062a \u0627\u0644\u0634\u0645\u0633\u064a\u0629 \u0641\u0642\u0637 \u064a\u0633\u0645\u062d \u0628\u0627\u0644\u0646\u0638\u0627\u0631\u0627\u062a \u0630\u0627\u062a \u0627\u0644\u0639\u062f\u0633\u0627\u062a \u0627\u0644\u0634\u0641\u0627\u0641\u0629 </span></p><p align=\"right\"><br/></p><p align=\"right\"><span style=\" font-size:12pt;\">\u0627\u0646\u062a\u0628\u0647 \u062d\u0627\u0648\u0644 \u0623\u0646 \u062a\u0643\u0648\u0646 \u0645\u0646\u0637\u0642\u0629 \u0627\u0644\u0648\u062c\u0647 \u0645\u0643\u0634\u0648\u0641\u0629 \u062a\u0645\u0627\u0645\u0627\u064b \u060c \u0644\u0627 \u062a\u0642\u0645 \u0628\u062a\u063a\u0637\u064a\u062a\u0647 \u0628\u0627\u0644\u0634\u0639\u0631 \u0627\u0648 \u0628\u0627\u0644\u064a\u062f\u064a\u0646 \u0627\u0648 \u0628\u0627\u0644\u0645\u0644\u0627\u0628\u0633 \u0627\u0648 \u0627\u064a \u0634\u064a\u0621 \u0622\u062e\u0631 </span></p><p align=\"right\"><br/></p><p align=\"right\"><span style=\" fon"
                        "t-size:12pt;\">\u0639\u0646\u062f \u0648\u062c\u0648\u062f \u0627\u064a \u0639\u0637\u0644 \u064a\u0631\u062c\u0649 \u062a\u0631\u0643 \u0645\u0644\u0627\u062d\u0638\u0629 \u0644\u0644\u0645\u0633\u0624\u0648\u0644\u064a\u0646</span></p><p align=\"right\"><br/></p><p align=\"right\"><span style=\" font-size:12pt;\">\u0628\u0639\u062f \u0627\u0646\u062a\u0647\u0627\u0621 \u0627\u0644\u0627\u0645\u062a\u062d\u0627\u0646 \u064a\u0645\u0643\u0646\u0643 \u0627\u0644\u062a\u062d\u0642\u0642 \u0645\u0646 \u0627\u0644\u0646\u062a\u064a\u062c\u0629 \u0641\u064a \u0627\u0644\u0635\u0641\u062d\u0629 \u0627\u0644\u0634\u062e\u0635\u064a\u0629</span></p><p align=\"right\"><span style=\" font-size:12pt;\">\u0627\u0644\u062e\u0627\u0635\u0629 \u0628\u0643 \u0644\u062a\u062a\u0645\u0643\u0646 \u0645\u0646 \u0627\u0644\u0648\u0635\u0648\u0644 \u0627\u0644\u064a\u0647\u0627 \u0641\u064a \u0623\u064a \u0648\u0642\u062a </span></p><p align=\"right\"><span style=\" font-size:12pt;\"><br/></span></p></body></html>", None))
        self.label_5.setText("")
#if QT_CONFIG(tooltip)
        self.profileMenuBtn.setToolTip(QCoreApplication.translate("SecondWindow", u"\u0627\u0644\u0635\u0641\u062d\u0629 \u0627\u0644\u0634\u062e\u0635\u064a\u0629", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.profileMenuBtn.setWhatsThis(QCoreApplication.translate("SecondWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.profileMenuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.logoutBtn.setToolTip(QCoreApplication.translate("SecondWindow", u"\u062a\u0633\u062c\u064a\u0644 \u0627\u0644\u062e\u0631\u0648\u062c", None))
#endif // QT_CONFIG(tooltip)
        self.logoutBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeBtn.setToolTip(QCoreApplication.translate("SecondWindow", u"\u062a\u0635\u063a\u064a\u0631", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate("SecondWindow", u"\u0627\u063a\u0644\u0627\u0642 ", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText("")
        self.testlogo.setText("")
        self.testinst.setText(QCoreApplication.translate("SecondWindow", u"         \u0623\u062f\u062e\u0644 \u0631\u0642\u0645 \u0627\u0644\u0627\u0645\u062a\u062d\u0627\u0646 \u0627\u0644\u0645\u0631\u0627\u062f \u0627\u062c\u0631\u0627\u0626\u0647:             ", None))
        self.testcode.setPlaceholderText(QCoreApplication.translate("SecondWindow", u"    \u0643\u0648\u062f \u0627\u0644\u0627\u0645\u062a\u062d\u0627\u0646", None))
        self.testverify.setText(QCoreApplication.translate("SecondWindow", u"    \u0623\u062f\u062e\u0644", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("SecondWindow", u"Exam Code", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("SecondWindow", u"Exam Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("SecondWindow", u"Exam Date", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("SecondWindow", u"Mark", None));
        self.label_7.setText(QCoreApplication.translate("SecondWindow", u"Right menu", None))
#if QT_CONFIG(tooltip)
        self.closeRightMenuBtn.setToolTip(QCoreApplication.translate("SecondWindow", u"Close menu", None))
#endif // QT_CONFIG(tooltip)
        self.closeRightMenuBtn.setText("")
        self.profile_pic.setText("")
        self.label_2.setText(QCoreApplication.translate("SecondWindow", u"\u0627\u0633\u0645 \u0627\u0644\u0645\u0633\u062a\u062e\u062f\u0645:", None))
        self.profile_name.setText(QCoreApplication.translate("SecondWindow", u"UserName", None))
        self.label_8.setText(QCoreApplication.translate("SecondWindow", u"\u0631\u0642\u0645 \u0627\u0644\u062a\u0639\u0631\u064a\u0641 :", None))
        self.profile_id.setText(QCoreApplication.translate("SecondWindow", u"ID", None))
        self.label_14.setText(QCoreApplication.translate("SecondWindow", u"Aman System v1.0.0", None))
        self.label_15.setText(QCoreApplication.translate("SecondWindow", u"TextLabel", None))
    # retranslateUi

