# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 14:10:21 2020

@author: leandro
"""
import pygame, sys, math
import numpy as np
class Cam : 
    def __init__(self,pos=(0,0,0), rot=(0,0)):
        self.pos = list(pos)
        self.rot = list(rot)

    def events(self,event):
        if event.type == pygame.MOUSEMOTION : 
            x,y = event.rel
            x/=200; y/=200
            self.rot[0] +=y; self.rot[1] += x
        
        
        
    def update(self, dt, key):
        s = dt*30
        if key[pygame.K_s]: self.pos[1] -=s
        if key[pygame.K_w]: self.pos[1] +=s
        if key[pygame.K_q]: self.pos[2] -=s
        if key[pygame.K_z]: self.pos[2] +=s
        if key[pygame.K_d]: self.pos[0] -=s
        if key[pygame.K_a]: self.pos[0] +=s


