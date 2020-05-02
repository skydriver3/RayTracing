import Ray
import Antenna 
import Wall
from typing import List
import pygame 
import multiprocessing as mp 
import Cam

class Space : 
    def __init__(self, Walls : List[Wall.wall], Tx : List[Antenna.Antenna], Rx : List[Antenna.Antenna]) : 
        pygame.init()
        self.Walls = Walls 
        self.Tx = Tx 
        self.Rx = Rx 
        self.screen  = pygame.display.set_mode((600,600))
        self.Clock = pygame.time.Clock()
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

    def _predictLayerDecorator(self, t, trajectories): 
        def inner(r): 
            ray = t.Propagate(r._pos, self.Walls)
            if ray != None : 
                trajectories.append(ray)
                r.rays.append(ray)
        return inner

    def _predictLayer(self, t, trajectories, r): 
        ray = t.Propagate(r._pos, self.Walls)
        if ray != None : 
            trajectories.append(ray)
            r.rays.append(ray)

    def Predict(self, Reflexions) : 
        transmitters = self.Tx
        trajectories = [] 
        for _ in range(Reflexions) :
            for t in transmitters : 
                 with mp.Pool(3) as p : 
                     p.map(self._predictLayerDecorator(t, trajectories), self.Rx)

            transmitters = self.CreateImagesFor_AllTx_AllWalls(transmitters)
        
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
  
       

    def Draw(self): 
        radian = 0
                
        while True : 
            dt = Clock.tick()/6000
            radian+=dt
            for event  in pygame.event.get() : 
                if event.type == pygame.QUIT : pygame.quit();  sys.exit()
                
                #cam.events(event)
            self.screen.fill((255,255,255))
            
            for w in self.Walls : 
                w.draw(self.screen, self.Distortion, (255,0,250))
            
            for r in self.Rx : 
                r.draw(self.screen, self.Distortion, [self.cx, self.cy], 20/(-self.cam.pos[2]))
            
            for t in self.Tx : 
                t.draw(self.screen, self.Distortion)

            
            pygame.display.flip()
            key = pygame.key.get_pressed()
            self.cam.update(dt, key)

    

    

