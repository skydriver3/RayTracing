# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 11:14:31 2020

@author: leandro
"""


import Antenna 
import Wall 
import Space 
import Ray
import numpy as np
import map
if __name__ == "__main__" : 
    
    Walls = [  
        Wall.wall(20, 1, 1, 1, np.array([200, 0]), np.array([0, 0])), 
        Wall.wall(20, 1, 1, 1, np.array([0, 0]), np.array([0, 100])),
        Wall.wall(20, 1, 1, 1, np.array([200, 0]), np.array([200, 100])),
        Wall.wall(20, 1, 1, 1, np.array([200, 100]), np.array([0, 100])),
        Wall.wall(20, 1, 1, 1, np.array([85, 50]), np.array([50, 15])),
        Wall.wall(20, 1, 1, 1, np.array([50, 85]), np.array([15, 50]))]
        
    Tx = [Antenna.Antenna(np.array([30, 30]), 100, [])] 
    Rx = [Antenna.Antenna(np.array([133, 80]), 0, [])] 

    env = Space.Space(Walls, Tx, Rx)
    env.Predict(3)

    Rayon = []
    listeRayon = []
    for ray in Rx[0].rays : 
         
         Rayon = ray.Coordinates
         listeRayon+=(Rayon)
         Rayon = []
    wall = []
    listWall = []
    for mur in (Walls):
        wall = [mur.Vec1, mur.Vec2]
        listWall += [wall]
        wall = []
         
    map = map.map()
    Tx = [Tx[0]._pos]
    Rx = [Rx[0]._pos]
    
    
    map.drawing(listeRayon, Tx, Rx, listWall)
