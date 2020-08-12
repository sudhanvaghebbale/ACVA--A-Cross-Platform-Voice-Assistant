# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Listening.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import*
from PySide2.QtGui import*
from PySide2.QtCore import*
import speech_recognition as sr
from stt import recognizer


class Ui_ListenWindow(object):
    def setupUi(self, ListenWindow):
        self.work = WorkerThread()
        self.work.start()
        ListenWindow.setObjectName("ListenWindow")
        ListenWindow.resize(951, 366)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/ACVA - LOGO.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ListenWindow.setWindowIcon(icon)
        ListenWindow.setStyleSheet("background-color: rgb(255,255,255);")
        self.centralwidget = QtWidgets.QWidget(ListenWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.acva_logo = QtWidgets.QLabel(self.centralwidget)
        self.acva_logo.setGeometry(QtCore.QRect(0, 0, 941, 141))
        self.acva_logo.setText("")
        self.acva_logo.setPixmap(QtGui.QPixmap("Images/ACVA_Voice.jpg"))
        self.acva_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.acva_logo.setObjectName("acva_logo")
        self.gif = QtWidgets.QLabel(self.centralwidget)
        self.gif.setGeometry(QtCore.QRect(230, 240, 481, 81))
        self.gif.setText("")
        self.gif.setPixmap(QtGui.QPixmap("E:/BE/FINAL YEAR PROJECT/ACVA/Images/acva_gif_1.gif"))
        self.gif.setAlignment(QtCore.Qt.AlignCenter)
        self.gif.setObjectName("gif")
        movie = QMovie("E:/BE/FINAL YEAR PROJECT/ACVA/Images/wave1.gif")
        self.gif.setMovie(movie)
        movie.start()
        self.listen = QtWidgets.QLabel(self.centralwidget)
        self.listen.setGeometry(QtCore.QRect(380, 150, 181, 71))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(14)
        self.listen.setFont(font)
        self.listen.setAlignment(QtCore.Qt.AlignCenter)
        self.listen.setObjectName("listen")
        ListenWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ListenWindow)
        self.statusbar.setObjectName("statusbar")
        ListenWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ListenWindow)
        QtCore.QMetaObject.connectSlotsByName(ListenWindow)

    def retranslateUi(self, ListenWindow):
        _translate = QtCore.QCoreApplication.translate
        ListenWindow.setWindowTitle(_translate("ListenWindow", "MainWindow"))
        self.listen.setText(_translate("ListenWindow", "Listening..."))

class WorkerThread(QThread):
    def run(self):
        value = recognizer()
        print("Value:"+value)
        f = open("listen_data.txt","w")
        f.write(value)
        f.close()
        f = open("command.txt","w")
        f.write(value)
        f.close()
        quit()
        #QtCore.QCoreApplication.instance().quit


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ListenWindow = QtWidgets.QMainWindow()
    ui = Ui_ListenWindow()
    ui.setupUi(ListenWindow)
    ListenWindow.show()
    sys.exit(app.exec_())
