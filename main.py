import Antenna 
import Wall 
import Space 
import Ray 
import numpy as np
import Line
import pickle
import pygame
from pygame.locals import *


def wait():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_y:
                return


if __name__ == "__main__" : 
    Walls = [  
        Wall.wall(20, 1, 1, 1, np.array([325, 300]), np.array([325, 600])), 
        Wall.wall(20, 1, 1, 1, np.array([550, 300]), np.array([550, 600])),
        Wall.wall(20, 1, 1, 1, np.array([300, 300]), np.array([600, 300])),
        Wall.wall(20, 1, 1, 1, np.array([300, 600]), np.array([600, 600]))] 
    Tx = [Antenna.Antenna(np.array([350, 400]), 100, [])] 
    Rx = [Antenna.Antenna(np.array([500, 500]), 0, [])] 

    
    env = Space.Space(Walls, Tx, Rx)
    env.Draw() 
    env.Predict(4)
    # env.Save()

    #env = pickle.load(open("save.pickle", "rb"))

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()

    # l1 = Line.Line(np.array([300, 300]), np.array([600, 300]))
    # for i in range(400) : 
    #     p = np.array([600 + i, 300])
    #     if l1.Contains(p) == False : 
    #         print(p)



