# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login3yotpCW.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)
import os,sys
from PySide6 import QtWidgets
from PySide6 import QtCore
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(662, 549)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(70, 30, 550, 500))
        self.widget.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"buttonlogin */\n"
"\n"
"QPushButton#loginBtn{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(44, 49, 58,189), stop:1 rgb(55, 62, 76));\n"
"	border-color: rgb(255, 255, 255);\n"
"\n"
"color:rgba(255,255,255,255);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#loginBtn:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(50, 60, 90,189), stop:1 rgb(50, 69, 96));\n"
"}\n"
"\n"
"QPushButton#loginBtn:pressed{\n"
" padding-left:5px;\n"
" padding-top:5px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(40, 44, 53,189), stop:1 rgb(49, 63, 98));\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
" ")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 30, 280, 430))
        self.label.setStyleSheet(u"border-image: url(:/images/images/images/login1.jpg);\n"
"border-top-left-radius : 50px;")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(260, 30, 240, 430))
        self.label_3.setStyleSheet(u"background-color: rgba(250,250,250,1);\n"
"border-bottom-right-radius: 50px;\n"
"")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(310, 80, 151, 40))
        font = QFont()
        font.setFamilies([u"Cocon modified"])
        font.setPointSize(17)
        font.setBold(False)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_4.setStyleSheet(u"color:rgba(0,0,0,200);\n"
"")
        self.idLine = QLineEdit(self.widget)
        self.idLine.setObjectName(u"idLine")
        self.idLine.setGeometry(QRect(295, 150, 190, 40))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        self.idLine.setFont(font1)
        self.idLine.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.idLine.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.idLine.setLocale(QLocale(QLocale.Arabic, QLocale.Egypt))
        self.passLine = QLineEdit(self.widget)
        self.passLine.setObjectName(u"passLine")
        self.passLine.setGeometry(QRect(295, 215, 190, 40))
        self.passLine.setFont(font1)
        self.passLine.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.passLine.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.loginBtn = QPushButton(self.widget)
        self.loginBtn.setObjectName(u"loginBtn")
        self.loginBtn.setGeometry(QRect(295, 295, 190, 40))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.loginBtn.setFont(font2)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(300, 350, 181, 16))
        font3 = QFont()
        font3.setFamilies([u"Cocon modified"])
        font3.setBold(False)
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"color:rgba(0,0,0,210);")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(90, 60, 121, 121))
        self.label_5.setStyleSheet(u"image: url(:/images/images/images/log.png);")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(80, 170, 131, 41))
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 300 13pt \"Cocon modified\";")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(130, 400, 41, 41))
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 300 15pt \"Cocon modified\";")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0633\u062c\u064a\u0644 \u0627\u0644\u062f\u062e\u0648\u0644", None))
        self.idLine.setText("")
        self.idLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0631\u0642\u0645 \u0627\u0644\u062a\u0639\u0631\u064a\u0641", None))
        self.passLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0643\u0644\u0645\u0629 \u0627\u0644\u0645\u0631\u0648\u0631", None))
        self.loginBtn.setText(QCoreApplication.translate("MainWindow", u"\u0633\u062c\u0644", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0633\u064a\u062a \u0643\u0644\u0645\u0629 \u0627\u0644\u0645\u0631\u0648\u0631\u061f", None))
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0631\u062d\u0628\u0627\u064b \u0628\u0643\u0645 \u0641\u064a \u0623\u0645\u0627\u0646 ", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"2024", None))
    # retranslateUi

