# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\BE\FINAL YEAR PROJECT\ACVA\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

#from PyQt5 import QtCore, QtGui, QtWidgets
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import*
from PySide2.QtGui import*
import webbrowser
from selenium import webdriver
from Listening import Ui_ListenWindow
import time


class Ui_MainWindow(object):
    def closeEvent(self, event):
        print("Clicked X Button")
        event.accept()
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ListenWindow()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        QtGui.qApp.processEvents()
        self.window.show()
    def closeWindow(self):
        info = "1"
        f = open("close.txt", "w")
        f.write(info)
        f.close()
    def driveHome(self):
        url = "https://www.google.com/?#q=drive me home"
        webbrowser.open(url)
    def setTimer(self):
        url = "https://www.google.com/?#q=set a timer"
        webbrowser.open(url)
    def gamePac(self):
        driver = webdriver.Chrome("C:/Users/Shwetha_Lokesh/Desktop/chromedriver.exe")
        driver.get("https://www.google.com/search?q=play%20pacman")
        class_play = driver.find_element_by_class_name('nvce1')
        class_play.click()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(951, 366)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setWindowTitle(" ")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/ACVA - LOGO.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color:rgb(255,255,255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.acva_logo = QtWidgets.QLabel(self.centralwidget)
        self.acva_logo.setGeometry(QtCore.QRect(0, 0, 941, 141))
        self.acva_logo.setText("")
        self.acva_logo.setPixmap(QtGui.QPixmap("Images/ACVA_Voice.jpg"))
        self.acva_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.acva_logo.setObjectName("acva_logo")
        self.intro = QtWidgets.QLabel(self.centralwidget)
        self.intro.setGeometry(QtCore.QRect(270, 100, 411, 91))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.intro.setFont(font)
        self.intro.setAlignment(QtCore.Qt.AlignCenter)
        self.intro.setObjectName("intro")
        self.mic = QtWidgets.QPushButton(self.centralwidget)
        self.mic.setGeometry(QtCore.QRect(450, 300, 41, 41))
        self.mic.setStyleSheet("border-image:url(E:/BE/FINAL YEAR PROJECT/Qt Designer/Images/mic2.png);")
        self.mic.setText("")
        self.mic.setObjectName("mic")
        self.mic.clicked.connect(self.openWindow)
        self.mic.clicked.connect(self.closeWindow)
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button1.setGeometry(QtCore.QRect(140, 210, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.button1.setFont(font)
        self.button1.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 2px solid #0976CF;\n"
"}\n"
"QPushButton\n"
"{\n"
"    border: 2px solid #85C1E9;\n"
"    border-radius:8px;\n"
"    color: black;\n"
"}\n"
"")
        self.button1.setObjectName("button1")
        self.button1.clicked.connect(self.driveHome)
        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        self.button2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button2.setGeometry(QtCore.QRect(390, 210, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.button2.setFont(font)
        self.button2.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 2px solid #0976CF;\n"
"}\n"
"QPushButton\n"
"{\n"
"    border: 2px solid #85C1E9;\n"
"    border-radius:8px;\n"
"    color: black;\n"
"}\n"
"")
        self.button2.setObjectName("button2")
        self.button2.clicked.connect(self.gamePac)
        self.button3 = QtWidgets.QPushButton(self.centralwidget)
        self.button3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button3.setGeometry(QtCore.QRect(640, 210, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.button3.setFont(font)
        self.button3.setStyleSheet("QPushButton:hover\n"
"{\n"
"    border: 2px solid #0976CF;\n"
"}\n"
"QPushButton\n"
"{\n"
"    border: 2px solid #85C1E9;\n"
"    border-radius:8px;\n"
"    color: black;\n"
"}\n"
"")
        self.button3.setObjectName("button3")
        self.button3.clicked.connect(self.setTimer)
        MainWindow.setCentralWidget(self.centralwidget)

        '''
        self.var = QtWidgets.QDesktopWidget().screenGeometry()
        print("Var")
        print(self.var)
        MainWindow.move(500,500)
        '''

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.intro.setText(_translate("MainWindow", "Hi, how can I help you?"))
        self.button1.setText(_translate("MainWindow", "Drive me home"))
        self.button2.setText(_translate("MainWindow", "I\'m Bored"))
        self.button3.setText(_translate("MainWindow", "Set a timer"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
