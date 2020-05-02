import Antenna 
import Wall 
import Space 
import Ray
import numpy as np
import random
# import map



if __name__ == "__main__" : 
    
    Walls = [  
        Wall.wall(0.3, 5, 1, 0.014, np.array([30, 0]), np.array([0, 0])),
        Wall.wall(0.3, 5, 1, 0.014, np.array([0, 0]), np.array([0, 15])),
        Wall.wall(0.3, 5, 1, 0.014, np.array([30, 0]), np.array([30, 15])),
        Wall.wall(0.3, 5, 1, 0.014, np.array([30, 15]), np.array([0, 15]))]
        
    Tx = [(Antenna.Antenna(np.array([12,14]), 0.1, []))]##,(Antenna.Antenna(np.array([6, 6]), 100, []))] 
    
    
    Rx = []
    x= 0
    for i in range(0,60):
       for j in range(0,6):
           for tx in Tx:
               if ([i/2,j/2] != list(tx._pos) ):
                   rx =  (Antenna.Antenna(np.array([i/2,j/2]), 0, []))
                   Rx.append(rx)
                   
           rx= 0
    #Rx = [(Antenna.Antenna(np.array([25, 5]), 0, []))] 
    
    env = Space.Space(Walls, Tx, Rx)
    env.Predict(4)
    env.Draw()
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
    

    
    
