# -*- coding: utf-8 -*-
"""
Created on Fri May 17 12:20:07 2013

@author: Julian
"""

import pygame as pg


#define colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0) 

#original snake start and end points

startcoord = (390,300)
endcoord = (410,300)
t0 = pg.time.get_ticks()*0.001


running = True
while running:
    pg.init()

    scr = pg.display.set_mode((800,600))   
    scr.fill(white)

    key = pg.key.get_pressed()   
    if key[pg.K_ESCAPE]:
        running = False