import Antenna 
import Wall 
import Space 
import Ray
import numpy as np
import random
import map
if __name__ == "__main__" : 
    
    Walls = [  
        Wall.wall(0.3, 5, 1, 0.014, np.array([30, 0]), np.array([0, 0])),
        Wall.wall(0.3, 5, 1, 0.014, np.array([0, 0]), np.array([0, 15])),
        Wall.wall(0.3, 5, 1, 0.014, np.array([30, 0]), np.array([30, 15])),
        Wall.wall(0.3, 5, 1, 0.014, np.array([30, 15]), np.array([0, 15]))]
        
    Tx = [(Antenna.Antenna(np.array([12,14]), 0.1, []))]##,(Antenna.Antenna(np.array([6, 6]), 100, []))] 
    txs = []
    listeTx = []
    
    for tx in (Tx):
        txs = tx._pos
        listeTx += [txs]
        txs = []
    Rx = []
    x= 0
    for i in range(0,60):
       for j in range(0,6):
           for x in listeTx :
               if ([i/2,j/2] != [x[0],x[1]]):
                   rx =  (Antenna.Antenna(np.array([i/2,j/2]), 0, []))
                   Rx.append(rx)
                   
           rx= 0
    #Rx = [(Antenna.Antenna(np.array([25, 5]), 0, []))] 
    
    env = Space.Space(Walls, Tx, Rx)
    rays = env.Predict(4)
    #env.save();
    #env = pickle.load(open("save.pickle", "rb"))
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
    
    
    listeRx = []
    for rx in (Rx):
        try :
            power = rx.getPower()
            print((power), "power")
        except :
            print("\n\n\n###############\n\n\n")
        rxs = [rx._pos, power]
        listeRx += [rxs]
        rxs = []
    
    
    map.drawing(listeRayon, listeTx, listeRx, listWall, rays)
