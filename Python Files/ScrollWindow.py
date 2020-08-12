# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ScrollWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import*
from PySide2.QtGui import*
from PySide2.QtCore import*
import pyttsx3
from Text_to_Speech import tts
from stt import recognizer

class Ui_MainWindow(object):
    def listen(self):
        self.mic.hide()
        self.work = WorkerThread()
        self.work.start()
        self.gif.show()
    def command(self):
        f = open("command.txt","r")
        data = f.read()
        f.close()
        f1 = open("Commands.txt","r")
        com = f1.read()
        f1.close()
        if data in com:
            QtGui.qApp.processEvents()
            self.label.setText(data)
        else:
            QtGui.qApp.processEvents()
            self.label.setText("Sorry I cannot understand")
            self.work = WorkerThread()
            self.work.start()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(951, 366)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/ACVA - LOGO.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(255,255,255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.acva = QtWidgets.QLabel(self.centralwidget)
        self.acva.setGeometry(QtCore.QRect(0, 0, 941, 141))
        self.acva.setText("")
        self.acva.setPixmap(QtGui.QPixmap("Images/ACVA_Voice.jpg"))
        self.acva.setAlignment(QtCore.Qt.AlignCenter)
        self.acva.setObjectName("acva")
        self.gif = QtWidgets.QLabel(self.centralwidget)
        self.gif.setGeometry(QtCore.QRect(230,240,481,81))
        self.gif.setObjectName("gif")
        movie = QMovie("E:/BE/FINAL YEAR PROJECT/ACVA/Images/wave1.gif")
        self.gif.setMovie(movie)
        movie.start()
        self.gif.hide()
        self.mic = QtWidgets.QPushButton(self.centralwidget)
        self.mic.setGeometry(QtCore.QRect(450, 300, 41, 42))
        self.mic.setStyleSheet("border-image:url(E:/BE/FINAL YEAR PROJECT/Qt Designer/Images/mic2.png);")
        self.mic.setText("")
        self.mic.setObjectName("mic")
        self.mic.clicked.connect(self.listen)
        self.mic.clicked.connect(self.gif.show)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 128, 951, 151))
        self.label.setText("What is 6+2?")
        #self.command()
        self.label.setObjectName("label")
        ##############################
        ##############################
        #self.label.setText(self.val)
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        #self.image = QImage("E:/BE/FINAL YEAR PROJECT/ACVA/Images/1.png")
        #self.label.setPixmap(QPixmap.fromImage(self.image))
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 128, 951, 151))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 951, 151))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.label)

        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(250, 110, 331, 191))
        self.label1.setStyleSheet("border: 2px solid #38b6ff;\n"
"border-radius: 8px;")
        self.label1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label1.setText("")
        self.label1.setObjectName("label")
        #self.label1.hide()
        self.scrollArea.setWidget(self.label1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

class WorkerThread(QThread):
    def run(self):
        tts()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
