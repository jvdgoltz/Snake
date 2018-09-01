# -*- coding: utf-8 -*-
"""
Created on Thu May 16 16:22:27 2013

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

#snake velocity
V = 50
Vx = 50
Vy = 0

running = True
while running:
    pg.init()

    scr = pg.display.set_mode((800,600))   
    scr.fill(white)

    key = pg.key.get_pressed()   
    if key[pg.K_ESCAPE]:
        running = False
    t = pg.time.get_ticks()*0.001    
    dt = t - t0
    t0 = t
    
    
    xstep = Vx*dt
    ystep = Vy*dt
    endx = endcoord[0]
    endy = endcoord[1]
    endcoord = (endx+xstep, endy+ystep)
    
    # Snake control 
    if key[pg.K_UP] and Vx<>0:
        Vx = 0
        Vy = -V
    if key[pg.K_DOWN] and Vx<>0:
        Vx = 0
        Vy = V        
    if key[pg.K_LEFT] and Vy<>0:
        Vx = -V
        Vy = 0
    if key[pg.K_RIGHT] and Vy<>0:
        Vx = V
        Vy = 0
        
    
    
    startx = startcoord[0]
    starty = startcoord[1]

    startcoord = (startx+xstep, starty+ystep)
    
    
    
    pointlist = [startcoord,endcoord] 
    pg.draw.aalines(scr, black, False,pointlist, 0)
    pg.display.flip()

pg.quit()