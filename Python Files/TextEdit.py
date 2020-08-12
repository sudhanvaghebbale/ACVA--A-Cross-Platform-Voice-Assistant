# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TextEdit.ui'
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
        MainWindow.resize(1067, 471)
        MainWindow.setStyleSheet("background-color:rgb(255,255,255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 110, 331, 191))
        self.label.setStyleSheet("border: 2px solid #38b6ff;\n"
"border-radius: 8px;")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.hide()
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(260, 140, 311, 20))
        self.line.setStyleSheet("border-bottom: 2px solid #38b6ff;\n"
"border-top:2px solid #ffffff")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line.hide()
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 125, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_2.hide()
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 180, 291, 91))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(22)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_3.hide()
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 80, 951, 311))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(14)

        self.textEdit.setFont(font)
        self.textEdit.setReadOnly(True)
        self.textEdit.setAlignment(Qt.AlignCenter)
        self.textEdit.setObjectName("textEdit")
        blueColor = QColor(168,168,168)
        self.textEdit.setTextColor(blueColor)
        self.textEdit.append("What is 6+8?")
        #self.textEdit.canInsertFromMimeData("Images/acva_text.png")
        self.textEdit.append(" ")
        rect1 = self.textEdit.cursorRect()
        print(rect1)
        rect = self.textEdit.textCursor()
        rect.movePosition(QTextCursor.End,QTextCursor.MoveAnchor)
        rect.insertImage("Images/label.png")
        print(rect)
        self.textEdit.overwriteMode()
        self.textEdit.append("Yaaaasssss")
        self.textEdit.append("Yaaaasssss")
        #cursor = self.textEdit.textCursor()
        #cursor.movePosition(cursor.Left, cursor.KeepAnchor,  0.5)
        #cursor.insertText("Yaaaasssss")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

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
