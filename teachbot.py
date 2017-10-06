# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a teachbot's main script file. Uses Python 2.7.12
Requires gTTS, pyglet and pyaudio packages.
Uses helpers.py for functions
@author: Jerry Ng
"""
from gtts import gTTS
from init import lines
from init import response_lines
from init import response_req, response_popper
from mutagen.mp3 import MP3
from time import sleep
import pyglet
import helpers
import serial
import argparse
import threading

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
response_labels = [0 for x in range(0, 4)]
response_voices = [0 for x in range(0, 4)]

#label1 = helpers.pyglabelmaker("Good morning. My name is Teachbot. How are you?")
#label2 = helpers.pyglabelmaker("I'm a robot meant to teach you robotics. Let me show you what I can do.")
#label3 = helpers.pyglabelmaker("Want to know how I did that? Inside my arm I have a bunch of electronic things called actuators. Here, take a look.")

#labels.append(label1) #lists subtitles
#labels.append(label2)
#labels.append(label3)

for x in range(0,len(lines)-1):
    voices[x] = pyglet.resource.media('sounds/line' + str(x) + '.mp3', streaming = False)
    labels[x] = helpers.pyglabelmaker(unicode(lines[x], errors ='replace'))

for x in range(0,4):
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

        
# main() function
class myThread1 (threading.Thread):
    global data
    def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
    def run(self):
        
          # create parser
          parser = argparse.ArgumentParser(description="LDR serial")
          # add expected arguments
          parser.add_argument('--port', dest='/dev/ttyACM0', required=False)
          
          # parse args
          args = parser.parse_args()
          
          #strPort = '/dev/tty.usbserial-A7006Yqh'
          strPort = '/dev/ttyACM0'
        
          print('reading from serial port %s...' % strPort)
        
          # plot parameters
          analogPlot = AnalogPlot(strPort, 100)
        
          print('plotting data...')
        
          # set up animation
          fig = plt.figure()
          ax = plt.axes(xlim=(0, 100), ylim=(0, 360))
          a0, = ax.plot([], [])
          #a1, = ax.plot([], [])
          anim = animation.FuncAnimation(fig, analogPlot.update, 
                                         fargs=(a0,), #,a1), 
                                         interval=1)

          # show plot
          plt.show()
          
          # clean up
          analogPlot.close()
        
          print('exiting.')
      
class myThread2 (threading.Thread):
    def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
    def run(self):
        pyglet.app.run()

# plot class
class AnalogPlot:
  # constr
  def __init__(self, strPort, maxLen):
      # open serial port
      self.ser = serial.Serial(strPort, 38400)

      self.ax = deque([0.0]*maxLen)
      #self.ay = deque([0.0]*maxLen)
      self.maxLen = maxLen

  # add to buffer
  def addToBuf(self, buf, val):
      if len(buf) < self.maxLen:
          buf.append(val)
      else:
          buf.pop()
          buf.appendleft(val)

  # add data
  def add(self, data):
      assert(len(data) == 1)
      self.addToBuf(self.ax, data[0])
      #self.addToBuf(self.ay, data[1])

  # update plot
  def update(self, frameNum, a0):#, a1):
      try:
          line = self.ser.readline()
          global data
          data = [float(val) for val in line.split()]
          # print data
          if(len(data) == 1):
              self.add(data)
              a0.set_data(range(self.maxLen), self.ax)
              #a1.set_data(range(self.maxLen), self.ay)
      except KeyboardInterrupt:
          print('exiting')
      
      return a0, 

  # clean up
  def close(self):
      # close serial
      self.ser.flush()
      self.ser.close()    
   
@window.event #sets up window event for proceeding through code
def on_key_press(symbol, modifiers):
    window.clear()
    if symbol == pyglet.window.key.ENTER: #press enter to go through each subtitle and mp3
        if(helpers.counter == len(lines)-1):
            window.close() 
            
        elif(helpers.counter == 7):
            pos2 = data[0]
            global pos1
            diffangle = pos2 - pos1
            if(diffangle>0):
                net_response = response_lines[2] + " " + str(diffangle)  \
                      + " " + response_lines[4]
                labels[helpers.counter]= helpers.pyglabelmaker(unicode(net_response, errors = 'ignore'))
                tts = gTTS(text=unicode(net_response, errors = 'ignore'), lang='en')
                tts.save('sounds/line' + str(helpers.counter) + '.mp3')
                voices[helpers.counter] = pyglet.resource.media('sounds/line' + str(helpers.counter) + '.mp3')
            elif(diffangle<=0):
                net_response = response_lines[2] + " " + str(diffangle)  \
                      + " " + response_lines[3]
                labels[helpers.counter]= helpers.pyglabelmaker(net_response)
                tts = gTTS(text=unicode(net_response, errors = 'ignore'), lang='en')
                tts.save('sounds/line' + str(helpers.counter) + '.mp3')
                voices[helpers.counter] = pyglet.resource.media('sounds/line' + str(helpers.counter) + '.mp3')
            labels[helpers.counter].draw()
            voices[helpers.counter].play()
        
        else:
            labels[helpers.counter].draw()
            voices[helpers.counter].play()
            audio = MP3('sounds/line' + str(helpers.counter) + '.mp3')
            print(str(response_req[0]) + "," + str(helpers.counter))
            """if(str(helpers.counter) == str(response_req[0])):
                if(helpers.counter == 0):
                    with sr.Microphone() as source:
                        print("Say something!")
                        phrase = r.listen(source) #listens for first phrase
                        txtphrase = r.recognize_google(phrase)
                        #putting together the response
                        response = response_lines[0] + " " + str(txtphrase)+ response_lines[1] 
                        tts = gTTS(text = unicode(response, errors ='ignore'), lang='en')
                        tts.save('sounds/response' + str(helpers.counter) + '.mp3')
                        response_voices[0] = pyglet.resource.media(
                                'sounds/response' + str(helpers.counter) + '.mp3')
                        response_labels[0] = helpers.pyglabelmaker(
                                unicode((response),errors = 'replace'))
                        
                        audio = MP3('sounds/response' + str(helpers.counter) + '.mp3') #finding length of response
                        
                        #executing the response
                        response_labels[0].draw()
                        response_voices[0].play()
                        sleep(audio.info.length)"""
            if(helpers.counter == 0):
                    pos1 = data[0]             
                    
            response_popper()               

                    
               # try:
               #     print(r.recognize(audio))"""
               
        if symbol == pyglet.window.key.ESCAPE:
                   window.close()
        helpers.counterincrement()

#voice1 = pyglet.resource.media('sound/line0.mp3', streaming=False) #decoded in memory before used
#voice2 = pyglet.resource.media('sound/line1.mp3', streaming=False)
#voice3 = pyglet.resource.media('sound/line2.mp3', streaming=False)

#voices.append(voice1) #lists mp3 files
#voices.append(voice2)
#voices.append(voice3)

#@window.event   #sets up window event to change text
#def on_draw():

global counter
counter = 0
#def counterincrement():
   # global counter
   # counter = counter + 1



thread1 = myThread1(1, "Thread-1", 1)
thread2 = myThread2(2, "Thread-2", 2)

#start threads
thread1.start()
thread2.start()











