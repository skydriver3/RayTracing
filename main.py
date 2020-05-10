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
    screen  = pygame.display.set_mode((600,600))
    
    Clock = pygame.time.Clock()
    start = time.time()
    """
    Walls = [  
        Wall.wall(0.3, 5, 0.014, np.array([30, 0]), np.array([0, 0])),
        Wall.wall(0.3, 5, 0.014, np.array([0, 0]), np.array([0, 15])),
        Wall.wall(0.3, 5, 0.014, np.array([30, 0]), np.array([30, 15])),
        Wall.wall(0.3, 5, 0.014, np.array([30, 15]), np.array([0, 15])),
        Wall.wall(0.15, 5, 0.014, np.array([10, 0]), np.array([10, 6])),
        Wall.wall(0.15, 5, 0.014, np.array([10, 3]), np.array([13, 3])),
        Wall.wall(0.15, 5, 0.014, np.array([0, 6]), np.array([4, 6])),
        Wall.wall(0.15, 5, 0.014, np.array([7, 6]), np.array([13, 6])),
        Wall.wall(0.15, 5, 0.014, np.array([16, 6]), np.array([22, 6])),
        Wall.wall(0.15, 5, 0.014, np.array([24, 6]), np.array([30, 6])),
        Wall.wall(0.15, 5, 0.014, np.array([21, 0]), np.array([21, 11])),
        Wall.wall(0.15, 5, 0.014, np.array([21, 13]), np.array([21, 15]))]
    """   
    Walls = [
        Wall.wall(0.15, 5, 0.014, np.array([0, 0]), np.array([20, 0])),
        Wall.wall(0.15, 5, 0.014, np.array([20, 0]), np.array([20, 20])),
        Wall.wall(0.15, 5, 0.014, np.array([20, 20]), np.array([0, 20])),
        Wall.wall(0.15, 5, 0.014, np.array([0, 20]), np.array([0, 0])),
        Wall.wall(0.15, 5, 0.014, np.array([9, 8]), np.array([11, 8]))] #mur au-dessus du Tx
     
    Tx = [(Antenna.Antenna(np.array([10,10]), 0.1, []))] #centre de la pièce
    # Tx = [(Antenna.Antenna(np.array([12,14]), 0.1, []))]##,(Antenna.Antenna(np.array([6, 6]), 100, []))] 
    
    
    Rx = []
    x= 0
    size_x = 20
    #size_y = 
    resolution = 0.1 #pas de 0.1m

    nbr_it = int(size_x / resolution)
    
    for i in range(0,nbr_it):
        for j in range(0,nbr_it):
            vecPos = [0.1+i*resolution,0.1+j*resolution]
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
    env.Predict_MultiProcessing(1)
    #env.Predict(1)
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
