import Ray
import Antenna 
import Wall
from typing import List

class Space : 
    def __init__(self, Walls : List[Wall.wall], Tx : List[Antenna.Antenna], Rx : List[Antenna.Antenna]) : 
        self.Walls = Walls 
        self.Tx = Tx 
        self.Rx = Rx 
    
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

