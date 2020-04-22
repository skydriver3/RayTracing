import Ray
import Antenna 
import Wall
import pygame
from typing import List

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
        for r in Reflexions : 
            for t in transmitters : 
                for r in self.Rx : 
                    trajectories.append(t.Propagate(r._pos, self.Walls, []))
            transmitters = self.CreateImagesFor_AllTx_AllWalls(transmitters)

        return trajectories

    def Draw(self, Trajectories : List[Ray.Ray]): 
        
        for r in Trajectories : 
            r.draw()
        pygame.display.flip()

    

    

