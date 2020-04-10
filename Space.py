import Ray
import Antenna 
import Wall

class Space : 
    def __init__(self, Walls : list[Wall.wall], Tx : list[Antenna.Antenna], Rx : list[Antenna.Antenna]) : 
        self.Walls = Walls 
        self.Tx = Tx 
        self.Rx = Rx 
    
    def CreateImageFor_AllWalls(self, transmitter : Antenna.Antenna) : 
        Images = [] 
        for w in self.Walls : 
            Images.append(transmitter.CreateImage(w))
        
        return Images

    def CreateImagesFor_AllTx_AllWalls(self, Transmitters : list[Antenna.Antenna]) :
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

