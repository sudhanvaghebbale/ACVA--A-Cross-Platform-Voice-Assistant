from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import*
from PySide2.QtGui import*
from PySide2.QtCore import*
import os, sys, time

def Main():
	os.system("python MainWindow1.py")
	f = open("listen_data.txt","r")
	data = f.read()
	f.close()
	if data != " ":
		os.system("python Execute.py")
		f = open("listen_data.txt","w")
		f.write(" ")
		f.close()

Main()