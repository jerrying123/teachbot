#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 16:34:14 2017

@author: jerrying
"""

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
from init import response_req
from mutagen.mp3 import MP3
from time import sleep
import pyglet
import helpers
import serial
import argparse
import thread
import pygletfunc
from time import sleep
from collections import deque

#from pyglet.window import key
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import speech_recognition as sr
#import os
#setup

    
# plot class
class AnalogPlot:
  # constr
  def __init__(self, strPort, maxLen):
      # open serial port
      self.ser = serial.Serial(strPort, 38400)

      self.ax = deque([0.0]*maxLen)
      self.ay = deque([0.0]*maxLen)
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
      assert(len(data) == 2)
      self.addToBuf(self.ax, data[0])
      self.addToBuf(self.ay, data[1])

  # update plot
  def update(self, frameNum, a0, a1):
      try:
          line = self.ser.readline()
          data = [float(val) for val in line.split()]
          # print data
          if(len(data) == 2):
              self.add(data)
              a0.set_data(range(self.maxLen), self.ax)
              a1.set_data(range(self.maxLen), self.ay)
      except KeyboardInterrupt:
          print('exiting')
      
      return a0, 

  # clean up
  def close(self):
      # close serial
      self.ser.flush()
      self.ser.close()    
        
# main() function
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
a1, = ax.plot([], [])
anim = animation.FuncAnimation(fig, analogPlot.update, 
                                 fargs=(a0, a1), 
                                 interval=2)

# show plot
plt.show()
  
# clean up
analogPlot.close()
print('exiting.')
            


#voice1 = pyglet.resource.media('sound/line0.mp3', streaming=False) #decoded in memory before used
#voice2 = pyglet.resource.media('sound/line1.mp3', streaming=False)
#voice3 = pyglet.resource.media('sound/line2.mp3', streaming=False)

#voices.append(voice1) #lists mp3 files
#voices.append(voice2)
#voices.append(voice3)

#@window.event   #sets up window event to change text
#def on_draw():


