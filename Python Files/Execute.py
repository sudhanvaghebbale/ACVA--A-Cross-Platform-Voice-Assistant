# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Execute.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import*
from PySide2.QtGui import*
from PySide2.QtCore import*
from stt import recognizer
from Text_to_Speech import tts
from Windows_Exec import windows
from Image import image1
import time, os

class Ui_ExecuteWindow(object):
    def label(self,str1):
        str2 = str1
        self.textEdit.append(" ")
        rect = self.textEdit.textCursor()
        rect.movePosition(QTextCursor.End,QTextCursor.MoveAnchor)
        rect.insertImage("Label/"+str2+"/label.png")
        #os.remove("Label/label.png")
    def execute0(self):#From Listening Window
        f = open("command.txt","r")
        data = f.readline()
        f.close()
        f1 = open("Commands.txt","r")
        com = f1.read()
        com = com.split("\n")
        f1.close()
        data = data.upper()
        data1 = None
        for line in com:
            if data == line:
                data1=line 
        if data == data1:
            self.textEdit.append(" ")
            QtGui.qApp.processEvents()
            print("Data:"+data)
            self.textEdit.append(data.title())
            winData = windows(data)
            print(data)
            if "AVENGERS" in data:
                value = "Avengers"
                image1(value)
                self.label("Avengers")
            elif "9" in data:
                image1("Calculate")
                self.label("Calculate")
            elif "USD" in data:
                image1("Convert")
                self.label("Convert")
            elif "SPANISH" in data:
                image1("Spanish")
                self.label("Spanish")
            elif "TIME" in data:
                image1("Time")
                self.label("Time")
            elif "BANGALORE" in data:
                image1("Bangalore")
                self.label("Bangalore")
            elif "RAIN" in data:
                image1("Rain")
                self.label("Rain")
            elif "UMBRELLA" in data:
                image1("Umbrella")
                self.label("Umbrella")
            elif "WEATHER" in data:
                image1("Weather")
                self.label("Weather")
            elif "GREET" in data:
                image1("Spanish_Greet")
                self.label("Spanish_Greet")    
            else:
                self.textEdit.append(winData)
            f = open("command.txt","w")
            f.write(" ")
            f.close()
        else:
            self.textEdit.append(" ")
            QtCore.QCoreApplication.processEvents()
            QtGui.qApp.processEvents()
            value = "Sorry I could not understand"
            tts(value)
            self.textEdit.append("Sorry I could not understand")
        #return
    def execute(self):#execute() and execute1() -> Only for Execute Window
        self.mic.hide()
        self.gif.show()
        QtGui.qApp.processEvents()
        QtCore.QCoreApplication.processEvents()
        value = recognizer()
        d = open("listen_data.txt","w")#Check if speech input is given
        d.write(value)
        d.close()
        d1 = open("command.txt","w")#Check in commands list
        d1.write(value)
        d1.close()
        #QtCore.QCoreApplication.processEvents()
        QtCore.QCoreApplication.flush()
        self.execute1()
    def execute1(self):
        self.gif.hide()
        self.mic.show()
        f = open("command.txt","r")
        data = f.readline()
        f.close()
        f1 = open("Commands.txt","r")
        com = f1.read()
        com = com.split("\n")
        f1.close()
        data = data.upper()
        data1 = None
        for line in com:
            if data == line:
                data1 = line 
        if data == data1:
            self.textEdit.append(" ")
            QtGui.qApp.processEvents()
            self.textEdit.append(data.title())
            winData = windows(data)
            if "AVENGERS" in data:
                value = "Avengers"
                image1(value)
                self.label("Avengers")
            elif "9" in data:
                image1("Calculate")
                self.label("Calculate")
            elif "USD" in data:
                image1("Convert")
                self.label("Convert")
            elif "SPANISH" in data:
                image1("Spanish")
                self.label("Spanish")
            elif "TIME" in data:
                image1("Time")
                self.label("Time")
            elif "BANGALORE" in data:
                image1("Bangalore")
                self.label("Bangalore")
            elif "RAIN" in data:
                image1("Rain")
                self.label("Rain")
            elif "UMBRELLA" in data:
                image1("Umbrella")
                self.label("Umbrella")
            elif "WEATHER" in data:
                image1("Weather")
                self.label("Weather")
            elif "GREET" in data:
                image1("Spanish_Greet")
                self.label("Spanish_Greet")  
            else:
                self.textEdit.append(winData)
            f = open("command.txt","w")
            f.write(" ")
            f.close()
        else:
            self.textEdit.append(" ")
            QtCore.QCoreApplication.processEvents()
            QtGui.qApp.processEvents()
            value = "Sorry I could not understand"
            tts(value)
            self.textEdit.append("Sorry I could not understand")
        return
    def setupUi(self, MainWindow):
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(12)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1001, 388)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/ACVA - LOGO.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color:rgb(255,255,255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.acva = QtWidgets.QLabel(self.centralwidget)
        self.acva.setGeometry(QtCore.QRect(0, 0, 1001, 141))
        self.acva.setText("")
        self.acva.setPixmap(QtGui.QPixmap("Images/ACVA_Voice.jpg"))
        self.acva.setAlignment(QtCore.Qt.AlignCenter)
        self.acva.setObjectName("acva")
        self.gif = QtWidgets.QLabel(self.centralwidget)
        self.gif.setGeometry(QtCore.QRect(430, 320, 121, 61))
        self.gif.setObjectName("gif")
        movie = QMovie("E:/BE/FINAL YEAR PROJECT/ACVA/Images/wave1.gif")
        self.gif.setMovie(movie)
        movie.start()
        self.gif.hide()
        self.mic = QtWidgets.QPushButton(self.centralwidget)
        self.mic.setGeometry(QtCore.QRect(480, 330, 41, 42))
        self.mic.setStyleSheet("border-image:url(E:/BE/FINAL YEAR PROJECT/Qt Designer/Images/mic2.png);")
        self.mic.setText("")
        self.mic.setObjectName("mic")
        self.mic.clicked.connect(self.execute)
        #self.mic.clicked.connect(self.gif.show)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 120, 1001, 201))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setPlaceholderText("")
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setAlignment(Qt.AlignCenter)
        self.textEdit.setFont(font)
        self.textEdit.setReadOnly(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.execute0()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " "))

class stt(QThread,Ui_ExecuteWindow):
    def run(self):
        value = recognizer()
        d = open("listen_data.txt","w")#Check if speech input is given
        d.write(value)
        d.close()
        d1 = open("command.txt","w")#Check in commands list
        d1.write(value)
        d1.close()
        quit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ExecuteWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
