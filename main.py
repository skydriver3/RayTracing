import Antenna 
import Wall 
import Space 
import Ray
import numpy as np
import random
import pygame
# import map
import time 

def CheckPosTx(vecPos, Tx): 
    for tx in Tx : 
        if vecPos == list(tx._pos) : 
            return False 
    return True

def CheckPosWall(vecPos, Walls) : 
    for w in Walls : 
        if w.Contains(vecPos) : 
            return False  
    return True 

if __name__ == "__main__" : 
    
    pygame.init()
    screen  = pygame.display.set_mode((1000,600))
    
    Clock = pygame.time.Clock()
    start = time.time()
    '''
    Walls = [
        Wall.wall(0.3, 5, 0.014, np.array([11, 0]), np.array([0, 0])),
        Wall.wall(0.3, 5, 0.014, np.array([0, 0]), np.array([0, 8])),
        Wall.wall(0.3, 5, 0.014, np.array([11, 0]), np.array([11, 8])),
        Wall.wall(0.3, 5, 0.014, np.array([11, 8]), np.array([0, 8])),
        Wall.wall(0.15, 5, 0.014, np.array([0, 3.5]), np.array([1.5, 3.5])),
        Wall.wall(0.15, 5, 0.014, np.array([2.5, 3.5]), np.array([4, 3.5])),
        Wall.wall(0.15, 5, 0.014, np.array([4, 0]), np.array([4, 3.5])),
        Wall.wall(0.15, 5, 0.014, np.array([4, 3.5]), np.array([4.5,3.5])),
        Wall.wall(0.15, 5, 0.014, np.array([5.5, 3.5]), np.array([7, 3.5])),
        Wall.wall(0.15, 5, 0.014, np.array([7, 0]), np.array([7, 4])),
        Wall.wall(0.15, 5, 0.014, np.array([7, 5]), np.array([7, 8])),        
        Wall.wall(0.15, 5, 0.014, np.array([8, 2]), np.array([11, 2]))]
    '''
    
    Walls = [  
        
        Wall.wall(0.3, 5, 0.014, np.array([11, 2]), np.array([17, 2])),
        Wall.wall(0.3, 5, 0.014, np.array([17, 2]), np.array([17, -5])),
        Wall.wall(0.3, 5, 0.014, np.array([17, -5]), np.array([11, -5])),
        Wall.wall(0.3, 5, 0.014, np.array([11, -5]), np.array([11, 0])),
        
        
        Wall.wall(0.3, 5, 0.014, np.array([11, 0]), np.array([0, 0])),
        Wall.wall(0.3, 5, 0.014, np.array([0, 0]), np.array([0, 8])),
        Wall.wall(0.3, 5, 0.014, np.array([11, 1]), np.array([11, 8])),
        Wall.wall(0.3, 5, 0.014, np.array([11, 8]), np.array([0, 8])),
        Wall.wall(0.15, 5, 0.014, np.array([0, 3.5]), np.array([1.5, 3.5])),
        Wall.wall(0.15, 5, 0.014, np.array([2.5, 3.5]), np.array([4, 3.5])),
        Wall.wall(0.15, 5, 0.014, np.array([4, 0]), np.array([4, 3.5])),
        Wall.wall(0.15, 5, 0.014, np.array([4, 3.5]), np.array([4.5,3.5])),
        Wall.wall(0.15, 5, 0.014, np.array([5.5, 3.5]), np.array([7, 3.5])),
        Wall.wall(0.15, 5, 0.014, np.array([7, 0]), np.array([7, 4])),
        Wall.wall(0.15, 5, 0.014, np.array([7, 5]), np.array([7, 8])),        
        Wall.wall(0.15, 5, 0.014, np.array([8, 2]), np.array([11, 2])),
        
        
        Wall.wall(0.01, 2.25, 0.04, np.array([7, 2]), np.array([8, 2])),
        Wall.wall(0.01, 2.25, 0.04, np.array([4.5, 3.5]), np.array([5.5, 3.5])),
        Wall.wall(0.01, 2.25, 0.04, np.array([7, 4]), np.array([7, 5])),
        Wall.wall(0.01, 2.25, 0.04, np.array([1.5, 3.5]), np.array([2.5, 3.5]))]
    
    '''
    Walls = [
        Wall.wall(0.15, 5, 0.014, np.array([0, 0]), np.array([10, 0])),
        Wall.wall(0.15, 5, 0.014, np.array([10, 0]), np.array([10, 10])),
        Wall.wall(0.15, 5, 0.014, np.array([10, 10]), np.array([0, 10])),
        Wall.wall(0.15, 5, 0.014, np.array([0, 10]), np.array([0, 0]))] 
    '''
    Tx = [(Antenna.Antenna(np.array([12.5, -4.5]), 0.1, []))] #centre de la pièce
    # Tx = [(Antenna.Antenna(np.array([12,14]), 0.1, []))]##,(Antenna.Antenna(np.array([6, 6]), 100, []))] 
    
    
    Rx = []
    
    x= 0
    size_x = 11
    size_y = 8
    resolution = 0.5 #pas de 0.1m

    nbr_it_x = int(size_x / resolution)
    nbr_it_y = int(size_y / resolution)
    for i in range(0,nbr_it_x):
        for j in range(0,nbr_it_y):
            vecPos = [0.1+i*resolution,0.1+j*resolution]
            checkPostx = CheckPosTx(vecPos, Tx)
            checkPoswall = CheckPosWall(vecPos, Walls) 
            if (checkPostx and checkPoswall) : 
                Rx.append(Antenna.Antenna(np.array(vecPos), 0, []))
    
    
    x= 0
    size_x = 6
    size_y = 7
    resolution = 0.5 #pas de 0.1m

    nbr_it_x = int(size_x / resolution)
    nbr_it_y = int(size_y / resolution)
    
    for i in range(0,nbr_it_x):
        for j in range(0,nbr_it_y):
            vecPos = [11 + 0.1+i*resolution,-5 + 0.1+j*resolution]
            checkPostx = CheckPosTx(vecPos, Tx)
            checkPoswall = CheckPosWall(vecPos, Walls) 
            if (checkPostx and checkPoswall) : 
                Rx.append(Antenna.Antenna(np.array(vecPos), 0, []))
    
    
    #Rx.append(Antenna.Antenna(np.array([10,7]), 0, []))


            # for tx in Tx:
            #     if ([0.1+i/2,0.1+j/2] != list(tx._pos) ):
            #         for w in Walls : 
            #             if w.Contains([0.1+i/2, 0.1+j/2]) == False: 
            #                 rx =  (Antenna.Antenna(np.array([0.1+i/2,0.1+j/2]), 0, []))
            #                 Rx.append(rx)
                   
            #             rx= 0
    #Rx = [(Antenna.Antenna(np.array([25, 5]), 0, []))] 
    env = Space.Space(Walls, Tx, Rx)
    env.Predict(4)
    #env.Predict_MultiProcessing(1)
    end = time.time()
    print(f"Finished Predict, Total time of the run : {int((end - start) / 60)}:{(end-start)%60}")
    
    env.Draw(screen, Clock)


    #env.save();
    #env = pickle.load(open("save.pickle", "rb"))
    
    
    
    
    # Rayon = []
    # listeRayon = []
    # for ray in (rays) : 
    #      Rayon = ray.Coordinates
    #      listeRayon+=(Rayon)
    #      Rayon = []
         

        
    
    
    # map = map.map()
    #map.drawing(listeRayon, listeTx, listeRx, listWall, rays)
