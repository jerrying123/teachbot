#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 16:31:29 2017

@author: jerrying
"""
from gtts import gTTS
from init import lines
from init import response_lines
from init import response_req
from mutagen.mp3 import MP3
from time import sleep
import pyglet
import helpers
import serial
import argparse
import thread

from time import sleep
from collections import deque
#from pyglet.window import key
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import speech_recognition as sr
#import os
#setup
r = sr.Recognizer() #voice recog
#creates a path to the sound files
pyglet.resource.path = ['/home/jerrying/teachbot']
pyglet.resource.reindex()
window = pyglet.window.Window(width = 1000, height = 1000, visible=True) #opens a window

#creates the text for the window
labels = [0 for x in range(0, len(lines)-1)]
voices = [0 for x in range(0, len(lines)-1)]
response_labels = [0 for x in range(0, len(response_req)-1)]
response_voices = [0 for x in range(0, len(response_req)-1)]

#label1 = helpers.pyglabelmaker("Good morning. My name is Teachbot. How are you?")
#label2 = helpers.pyglabelmaker("I'm a robot meant to teach you robotics. Let me show you what I can do.")
#label3 = helpers.pyglabelmaker("Want to know how I did that? Inside my arm I have a bunch of electronic things called actuators. Here, take a look.")

#labels.append(label1) #lists subtitles
#labels.append(label2)
#labels.append(label3)

for x in range(0,len(lines)-1):
    voices[x] = pyglet.resource.media('sounds/line' + str(x) + '.mp3', streaming = False)
    labels[x] = helpers.pyglabelmaker(unicode(lines[x], errors ='replace'))

for x in range(0,len(response_req)-1):
    response_labels[x] = helpers.pyglabelmaker(unicode(response_lines[x], errors ='replace'))

def pyglabelmaker(string):
    textlabel = pyglet.text.Label(string,
                          font_name = 'Times New Roman',
                          font_size = 36,
                          x = window.width//2, y=window.height//2,
                          width = 750,
                          anchor_x='center', anchor_y='center',
                          multiline = True)
    return textlabel;

@window.event #sets up window event for proceeding through code
def on_key_press(symbol, modifiers):
    window.clear()
    if symbol == pyglet.window.key.ENTER: #press enter to go through each subtitle and mp3
        if(helpers.counter == len(lines)-1):
            window.close()            
        else:
            window.clear()
            labels[helpers.counter].draw()
            voices[helpers.counter].play()
            helpers.counterincrement()
            """while(counter == response_req[0]):
                if(counter == 7):
                    print("okay")
                
                else:
                    with sr.Microphone() as source:
                        print("Say something!")
                        audio = r.listen(source) #listens for first phrase
                        
                        #putting together the response
                        response = response_labels[2*counter] + audio + response_labels[(2*counter)+1] 
                        tts = gTTS(text = unicode(response, errors ='ignore'), lang='en')
                        tts.save('sounds/response' + str(counter) + '.mp3')
                        response_voices[response_req[0]] = pyglet.resource.media('sounds/response' \
                                       + str(counter) + '.mp3')
                        response_labels[response_req[0]] = help.pyglabelmaker(
                                unicode(response),errors = 'replace')
                        
                        audio = MP3('sounds/response' + str(counter) + '.mp3') #finding length of response
                        
                        #executing the response
                        response_labels[response_req[0]].draw()
                        response_voices[response_req[0]].play()
                        time.sleep(audio.info.length)
                del response_req[0]                  

                    
               # try:
               #     print(r.recognize(audio))"""
               
    if symbol == pyglet.window.key.ESCAPE:
        window.close()
        
pyglet.app.run()
   