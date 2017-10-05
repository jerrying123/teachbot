#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 20:44:45 2017

@author: Jerry Ng
"""

import pyglet

counter = 0
res_counter = 0
response_req = []
def counterincrement():
    global counter
    counter = counter + 1


def response_popper():
    global response_req
    response_req.pop(0)
    
def pyglabelmaker(string):
    textlabel = pyglet.text.Label(string,
                          font_name = 'Times New Roman',
                          font_size = 36,
                          x = 1000//2, y=1000//2,
                          width = 750,
                          anchor_x='center', anchor_y='center',
                          multiline = True)
    return textlabel;