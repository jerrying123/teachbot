# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a teachbot's main script file. Uses Python 2.7.12
Requires gTTS, pyglet and pyaudio packages.
Uses helpers.py for functions
@author: Jerry Ng
"""
from gtts import gTTS
import pyglet
import helpers
#from pyglet.window import key

import speech_recognition as sr
#import os

r = sr.Recognizer()

#voice that will be spoken
tts= gTTS(text = 'Good morning. My name is Teachbot. How are you?', lang='en')
tts.save("good.mp3")
tts= gTTS(text = "I'm a robot meant to teach you robotics. Let me show you \
           what I can do.", lang = 'en')
tts.save("letmeshowyou.mp3")
tts= gTTS(text = "Want to know how I did that? Inside my arm I have a bunch of electronic things called actuators. Here, take a look.", lang='en')
tts.save("line3.mp3")
#creates a path to the sound files
pyglet.resource.path = ['/home/jerrying/teachbot']
pyglet.resource.reindex()
window = pyglet.window.Window(width = 1000, height = 1000, visible=True) #opens a window

#creates the text for the window
labels = []
voices = []
label1 = pyglet.text.Label('Good morning. My name is Teachbot. How are you?',
                          font_name = 'Times New Roman',
                          font_size = 36,
                          x = window.width//2, y=window.height//2,
                          width = 750,
                          anchor_x='center', anchor_y='center',
                          multiline = True)

label2 = pyglet.text.Label("I'm a robot meant to teach you robotics. Let me show you what I can do.",
                          font_name = 'Times New Roman',
                          font_size = 36,
                          x = window.width//2, y=window.height//2,
                          width = 750,
                          anchor_x='center', anchor_y='center',
                          multiline = True)

label3 = pyglet.text.Label("Want to know how I did that? Inside my arm I have a bunch of electronic things called actuators. Here, take a look.",
                          font_name = 'Times New Roman',
                          font_size = 36,
                          x = window.width//2, y=window.height//2,
                          width = 750,
                          anchor_x='center', anchor_y='center',
                          multiline = True)
labels.append(label1) #lists subtitles
labels.append(label2)
labels.append(label3)

voice1 = pyglet.resource.media('good.mp3', streaming=False) #decoded in memory before used
voice2 = pyglet.resource.media('letmeshowyou.mp3', streaming=False)
voice3 = pyglet.resource.media('line3.mp3', streaming=False)

voices.append(voice1) #lists mp3 files
voices.append(voice2)
voices.append(voice3)

#@window.event   #sets up window event to change text
#def on_draw():
helpers.counter = 0
response_req = [0]
#def counterincrement():
   # global counter
   # counter = counter + 1
    
def pyglabelmaker(string):
    textlabel = pyglet.text.Label(string,
                          font_name = 'Times New Roman',
                          font_size = 36,
                          x = window.width//2, y=window.height//2,
                          width = 750,
                          anchor_x='center', anchor_y='center',
                          multiline = True)
    return textlabel;


@window.event #sets up window event to close window
def on_key_press(symbol, modifiers):
    window.clear()
    if symbol == pyglet.window.key.ENTER: #press enter to go through each subtitle and mp3
        if(helpers.counter == 3):
            window.close()            
        else:
            window.clear()
            labels[helpers.counter].draw()
            voices[helpers.counter].play()
            helpers.counterincrement()
           # if(counter == response_req[0]): 
              #  del response_req[0]
               # with sr.Microphone() as source:
               #     print("Say something!")
               #     audio = r.listen(source) #listens for first phrase

                    
               # try:
               #     r.recognize(audio)
    
pyglet.app.run() #puts text onto window








