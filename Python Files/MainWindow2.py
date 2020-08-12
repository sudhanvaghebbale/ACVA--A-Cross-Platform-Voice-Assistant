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
from PySide2.QtCore import*
import webbrowser
from selenium import webdriver
from Execute import Ui_ExecuteWindow
from Text_to_Speech import tts
from stt import recognizer
import time
#QtCore.QCoreApplication.flush()

class Ui_MainWindow(object):
    def listenWindow(self):
        self.work1 = WorkerThread1()
        self.work1.start()
        self.mic.hide()
        self.button1.hide()
        self.button2.hide()
        self.button3.hide()
        self.intro.hide()
        self.listen.show()
        self.gif_listen.show()
    def ExecuteWindow(self):
        f = open("command.txt","r")
        data = f.read()
        f.close()
        if data == " ":
            self.listen.hide()
            self.gif_listen.hide()
            self.mic.show()
            self.button1.show()
            self.button2.show()
            self.button3.show()
            self.intro.show()
        else:
            self.openWindow()
    def continueWindow(self):
        self.label.hide()
        self.label_2.hide()
        self.label_3.hide()
        self.mic.show()
        self.button1.show()
        self.button2.show()
        self.button3.show()
        self.acva_logo.show()
        self.intro.show()
    def sleep(self):
        self.work = WorkerThread()
        self.work.start()
    def processOneThing(self):
        self.label.hide()
    def closeEvent(self, event):
        print("Clicked X Button")
        event.accept()
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ExecuteWindow()
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
        self.acva_logo.hide()
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
        self.intro.hide()
        self.mic = QtWidgets.QPushButton(self.centralwidget)
        self.mic.setGeometry(QtCore.QRect(450, 300, 41, 41))
        self.mic.setStyleSheet("border-image:url(E:/BE/FINAL YEAR PROJECT/Qt Designer/Images/mic2.png);")
        self.mic.setText("")
        self.mic.setObjectName("mic")
        #self.mic.clicked.connect(self.openWindow)
        #self.mic.clicked.connect(self.closeWindow)
        self.mic.hide()
        
        self.mic.clicked.connect(self.listenWindow)
        QtCore.QCoreApplication.processEvents
        self.mic.clicked.connect(self.ExecuteWindow)
        
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
        self.button1.hide()
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
        self.button2.hide()
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
        self.button3.hide()
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 80, 951, 161))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/acva_anim2.gif"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        movie = QMovie("Images/acva_anim2.gif")
        self.label.setMovie(movie)
        movie.start()
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 260, 301, 101))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_2.setText("Hi, I'm ACVA")
        self.label_3 = QtWidgets.QPushButton(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(650, 260, 121, 91))
        self.label_3.setStyleSheet("border-image:url(Images/arrow.png);")
        self.label_3.setObjectName("label_3")
        self.label_3.clicked.connect(self.continueWindow)
        self.sleep()
        self.listen = QtWidgets.QLabel(self.centralwidget)
        self.listen.setGeometry(QtCore.QRect(380, 150, 181, 71))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(14)
        self.listen.setFont(font)
        self.listen.setAlignment(QtCore.Qt.AlignCenter)
        self.listen.setObjectName("listen")
        self.listen.setText("Listening...")
        self.listen.hide()
        self.gif_listen = QtWidgets.QLabel(self.centralwidget)
        self.gif_listen.setGeometry(QtCore.QRect(230, 240, 481, 81))
        self.gif_listen.setText("")
        self.gif_listen.setPixmap(QtGui.QPixmap("E:/BE/FINAL YEAR PROJECT/ACVA/Images/acva_gif_1.gif"))
        self.gif_listen.setAlignment(QtCore.Qt.AlignCenter)
        self.gif_listen.setObjectName("gif_listen")
        movie = QMovie("E:/BE/FINAL YEAR PROJECT/ACVA/Images/wave1.gif")
        self.gif_listen.setMovie(movie)
        movie.start()
        self.gif_listen.hide()
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

class WorkerThread(QThread):
    def run(self):
        value = "Hi, I'm acva"
        tts(value)
        f = open("Anim.txt","w")
        f.write("1")
        f.close()
class WorkerThread1(QThread):
    def run(self):
        value = recognizer()
        print("Value:"+value)
        f = open("listen_data.txt","w")
        f.write(value)
        f.close()
        f = open("command.txt","w")
        f.write(value)
        f.close()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
