import Ray
import Antenna 
import Wall
from typing import List
import pygame 

class Space : 
    def __init__(self, Walls : List[Wall.wall], Tx : List[Antenna.Antenna], Rx : List[Antenna.Antenna]) : 
        self.Walls = Walls 
        self.Tx = Tx 
        self.Rx = Rx 
        self.canvas = pygame.display.set_mode((300, 300))
        self.canvas.fill((49,150,100))
        pygame.display.flip()
    
    def CreateImageFor_AllWalls(self, transmitter : Antenna.Antenna) : 
        Images = [] 
        for w in self.Walls : 
            if (transmitter.Wall != w ) : 
                Images.append(transmitter.CreateImage(w))
        
        return Images

    def CreateImagesFor_AllTx_AllWalls(self, Transmitters : List[Antenna.Antenna]) :
        Images = [] 
        for t in Transmitters : 
            Images.extend(self.CreateImageFor_AllWalls(t)) 
        
        return Images

    def Predict(self, Reflexions) : 
        transmitters = self.Tx
        trajectories = [] 
        for _ in range(Reflexions) : 
            print("\n\nlevel of relfection : " + str(_) + "\n################\n")
            for t in transmitters : 
                for r in self.Rx : 
                    ray = t.Propagate(r._pos, self.Walls)
                    if ray != None : 
                        trajectories.append(ray) 
            transmitters = self.CreateImagesFor_AllTx_AllWalls(transmitters)

        return trajectories

    def Draw(self, Trajectories : List[Ray.Ray]): 
        pass

    

    

