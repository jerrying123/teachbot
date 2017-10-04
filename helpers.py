#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 20:44:45 2017

@author: Jerry Ng
"""

import pyglet

window = pyglet.window.Window(width = 1000, height = 1000, visible=True) #opens a window

def counterincrement():
    global counter
    counter = counter + 1
    
def pyglabelmaker(string):
    textlabel = pyglet.text.Label(string,
                          font_name = 'Times New Roman',
                          font_size = 36,
                          x = window.width//2, y=window.height//2,
                          width = 750,
                          anchor_x='center', anchor_y='center',
                          multiline = True)
    return textlabel;