from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import*
from PySide2.QtGui import*
from PySide2.QtCore import*
import os, sys

def Main():
	os.system("python MainWindow.py")
	f = open("listen_data.txt","r")
	data = f.read()
	f.close()
	print("Data:"+data)
	if data == " ":
		Main1()
	else:
		End()
		f = open("listen_data.txt","w")
		f.write(" ")
		f.close()
		
def Main1():
	os.system("python MainWindow.py")
	f = open("listen_data.txt","r")
	data = f.read()
	f.close()
	print("Data:"+data)
	if data == " ":
		Main()
	else:
		End()
		f = open("listen_data.txt","w")
		f.write(" ")
		f.close()

def End():
	os.system("python Execute.py")

def Combine():
	Main()

Combine()