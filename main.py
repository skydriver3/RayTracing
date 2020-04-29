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
import random
import map
if __name__ == "__main__" : 
    
    Walls = [  
        Wall.wall(20, 1, 1, 1, np.array([30, 0]), np.array([0, 0])), 
        Wall.wall(20, 1, 1, 1, np.array([0, 0]), np.array([0, 15])),
        Wall.wall(20, 1, 1, 1, np.array([30, 0]), np.array([30, 15])),
        Wall.wall(20, 1, 1, 1, np.array([30, 15]), np.array([0, 15]))]
        ##Wall.wall(20, 1, 1, 1, np.array([50, 85]), np.array([15, 50]))]
        
    Tx = [(Antenna.Antenna(np.array([10, 6]), 100, [])),(Antenna.Antenna(np.array([6, 6]), 100, []))] 
    Rx = []
    x= 0
    for i in range(300):
        for j in range(150):
           x= random.randint(1,11)
           rx =  (Antenna.Antenna(np.array([0.05+i/10,0.05+j/10]), 0, []))
           Rx.append(rx)
           rx= 0
    ##Rx = [(Antenna.Antenna(np.array([0.5, 0.5]), 2, [])),(Antenna.Antenna(np.array([16, 13]), 7, []))] 
    
    env = Space.Space(Walls, Tx, Rx)
    rays = env.Predict(2)
    Rayon = []
    listeRayon = []
    for ray in (rays) : 
         
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
    txs = []
    listeTx = []
    for tx in (Tx):
        txs = tx._pos
        listeTx += [txs]
        txs = []
    txs = []
    listeRx = []
    for rx in (Rx):
        rxs = [rx._pos, rx.getPower()]
        listeRx += [rxs]
        rxs = []
    
    
    print(listeRx[2])
    map.drawing(listeRayon, listeTx, listeRx, listWall)
