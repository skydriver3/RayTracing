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
    
    """Pièce carrée basique de 20x20, murs en béton + 1 mur 
    """
    Walls = [  
        #Wall.wall(0.3, 5, 0.014, np.array([0, 0]), np.array([20, 0])),
        #Wall.wall(0.3, 5, 0.014, np.array([20, 0]), np.array([20, 20])),
        #Wall.wall(0.3, 5, 0.014, np.array([20, 20]), np.array([0, 20])),
        #Wall.wall(0.3, 5, 0.014, np.array([0, 20]), np.array([0, 0])),
        Wall.wall(0.3, 5, 0.014, np.array([5, 8]), np.array([15, 8]))] #mur au-dessus du Tx
    Tx = [(Antenna.Antenna(np.array([10,10]), 0.1, []))] #centre de la pièce
    

    """# Maison de Leandro, murs en béton
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
        
    Tx = [(Antenna.Antenna(np.array([12,14]), 0.1, []))]##,(Antenna.Antenna(np.array([6, 6]), 100, []))] 
    """
    
    Rx = []
    x= 0
    size_x = 20
    #size_y = 
    resolution = 0.5 #pas de 0.5m
    nbr_it = int(size_x / resolution)
    
    # for i in range(0, nbr_it):
    #     for j in range(0, 20):
    #         vecPos = [0.01+i*resolution, 0.01+j*resolution]
            
    #         if CheckPosTx(vecPos, Tx) and CheckPosWall(vecPos, Walls) : 
    #            Rx.append(Antenna.Antenna(np.array(vecPos), 0, []))
    
    Rx.append(Antenna.Antenna(np.array([1.01, 1.01]), 0, []))
    print("Power of Rx = ", Rx[0].getPower())
            # for tx in Tx:
            #     #if ([0.1+i/2,0.1+j/2] != list(tx._pos) ):
            #     if (vecPos != list(tx._pos) ):

            #         for w in Walls : 
            #             if w.Contains(vecPos) == False: 
            #                 #rx =  (Antenna.Antenna(np.array([0.1+i/2,0.1+j/2]), 0, []))
            #                 rx =  (Antenna.Antenna(np.array(vecPos), 0, []))
            #                 Rx.append(rx)
                   
            #             rx= 0
    #Rx = [(Antenna.Antenna(np.array([25, 5]), 0, []))] 
    
    env = Space.Space(Walls, Tx, Rx)
    env.Predict_MultiProcessing(1)
    # for i in range(len(Rx) - 1000):
        # print("Power of Rx", i, " = ", Rx[i].getPower())

    #env.Predict(2)
    end = time.time()
    print(f"Finished Predict, Total time of the run : {int((end - start) / 60)}:{(end-start)%60}")
    
    for i in range(len(Rx)):
       print("Power of Rx", i, " = ", env.Rx[i].getPower())
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