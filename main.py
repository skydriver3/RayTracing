import Antenna 
import Wall 
import Space 
import Ray
import numpy as np
import random
import pygame
# import map



if __name__ == "__main__" : 
    
    pygame.init()
    screen  = pygame.display.set_mode((600,600))
    screen.fill((255,255,255))
    Clock = pygame.time.Clock()
    
    
    Walls = [  
        Wall.wall(0.3, 5, 1, 0.014, np.array([30, 0]), np.array([0, 0])),
        Wall.wall(0.3, 5, 1, 0.014, np.array([0, 0]), np.array([0, 15])),
        Wall.wall(0.3, 5, 1, 0.014, np.array([30, 0]), np.array([30, 15])),
        Wall.wall(0.3, 5, 1, 0.014, np.array([30, 15]), np.array([0, 15]))]
        
    Tx = [(Antenna.Antenna(np.array([12,14]), 0.1, []))]##,(Antenna.Antenna(np.array([6, 6]), 100, []))] 
    
    
    Rx = []
    x= 0
    for i in range(0,60):
        for j in range(0,30):
            for tx in Tx:
                if ([0.1+i/2,0.1+j/2] != list(tx._pos) ):
                    for w in Walls : 
                        if w.Contains([0.1+i/2, 0.1+j/2]) == False: 
                            rx =  (Antenna.Antenna(np.array([0.1+i/2,0.1+j/2]), 0, []))
                            Rx.append(rx)
                   
                        rx= 0
    #Rx = [(Antenna.Antenna(np.array([25, 5]), 0, []))] 
    
    env = Space.Space(Walls, Tx, Rx)
    env.Predict(4)
    env.Draw(screen, Clock)
    pygame.display.flip()

    while True : 
        pass
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
    

    
    
