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


class Ui_MainWindow(object):
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
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 300, 41, 42))
        self.pushButton.setStyleSheet("border-image:url(E:/BE/FINAL YEAR PROJECT/Qt Designer/Images/mic2.png);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(14)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 128, 951, 151))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.setFont(font)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 128, 951, 151))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 951, 151))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.label)
        self.scrollArea.setStyleSheet('QSrcollBar{background-color:blue;}')

        n = 5
        y = 10
        for i in range(n):
            self.label.setText(" "*150+"Hi. How are you?")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
