import Ray
import Antenna 
import Wall
from typing import List
import multiprocessing as mp 
from functools import partial
import Cam

def _predictLayerDecorator(space, t, trajectories): 
    def inner(r): 
        ray = t.Propagate(r._pos, space.Walls)
        if ray != None : 
            trajectories.append(ray)
            r.rays.append(ray)
    return inner

def _predictLayer(r, t, walls): 
    ray = t.Propagate(r._pos, walls)
    if ray != None : 
        r.rays.append(ray)
    
    return r 

class Space : 
    def __init__(self, Walls : List[Wall.wall], Tx : List[Antenna.Antenna], Rx : List[Antenna.Antenna]) : 

        self.Walls = Walls 
        self.Tx = Tx 
        self.Rx = Rx 
        self.cam = Cam.Cam((0,0,-1))
        self.cx, self.cy = 0, 0
    
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
            for t in transmitters : 
                #print(t) 
                with mp.Pool(3) as p : 
                    f = partial(_predictLayer , t=t, walls = self.Walls)
                    self.Rx = p.map(f, self.Rx)

            with mp.Pool(3) as p : 
                f = partial(self.CreateImageFor_AllWalls)
                temp = p.map(f, transmitters)
                transmitters = [] 
                for t in temp : 
                    transmitters.extend(t) 
        
    def Distortion(self, vec) :
        x, y = vec 
        z=0
        x-=self.cam.pos[0]
        y-=self.cam.pos[1]
        z-=self.cam.pos[2]
        
        #x,z = rotate2d((x,z), cam.rot[1])
        #y,z = rotate2d((y,z), cam.rot[0])

        f= 20/z
        x,y = x*f,y*f
        return [self.cx+int(x), self.cy+int(y)]
  
       

    def Draw(self, screen, Clock): 
        
        for w in self.Walls : 
            w.draw(screen, self.Distortion, (255,0,250))
        
        for r in self.Rx : 
            r.draw(screen, self.Distortion, [self.cx, self.cy], 20/(-self.cam.pos[2]))
        
        for t in self.Tx : 
            t.draw(screen, self.Distortion)

            


    

    

