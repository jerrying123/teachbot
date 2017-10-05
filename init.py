#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 10:12:19 2017

run this script before running main script teachbot.py
This script creates all necessary mp3s 

@author: jerrying
"""

import os
import sys
from gtts import gTTS

reload(sys)
sys.setdefaultencoding('utf-8')
newpath = r'sounds'
if not os.path.exists(newpath): #makes folder for name sounds
    os.makedirs(newpath)

textfile = open("speech.txt")
lines = textfile.read().split('\n')

linepath = r'sounds/line'
for x in range(0,len(lines)-1):
    if not os.path.isfile(linepath +str(x) + '.mp3'):
        tts = gTTS(text = unicode(lines[x], errors ='ignore'), lang='en')
        tts.save("sounds/line" + str(x) + ".mp3")

textfile2 = open("response_req.txt")
response_req = textfile2.read().split('\n')

textfile3 = open("response_lines.txt")
response_lines = textfile3.read().split('\n')

def response_popper():
    global response_req
    response_req.pop(0)


#tts = gTTS(text = 'Good morning. My name is Teachbot. How are you?', lang='en')
#tts.save("sounds/line1.mp3")
#tts = gTTS(text = "I'm a robot meant to teach you robotics. Let me show you what I can do.", lang = 'en')
#tts.save("sounds/line2.mp3")
#tts = gTTS(text = "Want to know how I did that? Inside my arm I have a bunch of electronic things called actuators. Here, take a look.", lang='en')
#tts.save("sounds/line3.mp3")
#tts