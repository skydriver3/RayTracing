import Antenna 
import Wall 
import Space 
import Ray
import numpy as np
import random
import pygame
# import map
import time 
import Line 

def dis(v) : 
    
    return [v[0] * 5, v[1] * 5]  
    return v

if __name__ == "__main__": 
    
    pygame.init()
    screen  = pygame.display.set_mode((600,600))
    
    Clock = pygame.time.Clock()
    start = time.time()

    Walls = [  
        #Wall.wall(0.3, 5, 0.014, np.array([0, 0]), np.array([20, 0])),
        #Wall.wall(0.3, 5, 0.014, np.array([20, 0]), np.array([20, 20])),
        #Wall.wall(0.3, 5, 0.014, np.array([20, 20]), np.array([0, 20])),
        #Wall.wall(0.3, 5, 0.014, np.array([0, 20]), np.array([0, 0])),
        Wall.wall(0.3, 5, 0.014, np.array([5, 8]), np.array([15, 8]))] #mur au-dessus du Tx

    Tx = [Antenna.Antenna(np.array([10,10]), 0.1, [])] 
    Rx = [Antenna.Antenna(np.array([1.01, 1.01]), 0, [])]
    env = Space.Space(Walls, Tx, Rx)
    env.Predict(1)
    
    print(f"the power received by the antenna is {env.Rx[0].getPower()}") 
    print(f"length is {len(env.Rx[0].rays[0].Coefficients)}")
    env.Draw(screen, Clock, True)