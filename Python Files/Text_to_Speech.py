# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 21:48:46 2019

@author: Shwetha Lokesh
"""
import pyttsx3

def tts(val):
	value = val
	engine = pyttsx3.init()
	rate = engine.getProperty('rate')
	engine.setProperty('rate', 150)
	voices = engine.getProperty('voices')
	engine.setProperty('voice', voices[1].id)
	engine.say("{}".format(value))
	engine.runAndWait()
