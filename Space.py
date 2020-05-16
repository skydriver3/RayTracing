import Ray
import Antenna 
import Wall
from typing import List
import multiprocessing as mp 
from functools import partial
import Cam
import pygame
import numpy as np
import colorsys

def _predictLayerDecorator(space, t, trajectories): 
    def inner(r): 
        ray = t.Propagate(r._pos, space.Walls)
        if ray != None : 
            trajectories.append(ray)
            r.rays.append(ray)
    return inner
def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))
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
        self.cx, self.cy = 100, 180
    
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
    def Predict(self, Reflexions):
        transmitters = self.Tx 
        for _ in range(Reflexions) : 
            for t in transmitters : 
                for r in self.Rx : 
                    ray = t.Propagate(r._pos, self.Walls)
                    if ray != None : 
                        r.rays.append(ray)
                
            transmitters = self.CreateImagesFor_AllTx_AllWalls(transmitters)
                
    def Predict_MultiProcessing(self, Reflexions) : 
        transmitters = self.Tx
        for _ in range(Reflexions) :
            with mp.Pool(3) as p : 
                for t in transmitters : 
                    #print(t) 
                    #with mp.Pool(3) as p : 
                    f = partial(_predictLayer , t=t, walls = self.Walls)
                    self.Rx = p.map(f, self.Rx)

                #with mp.Pool(3) as p : 
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

        f= 35/z
        x,y = x*f,y*f
        return [self.cx+int(x), self.cy+int(y)]
  
       

    def Draw(self, screen, Clock, DrawRays = False): 

        radian = 0
                
        while True : 
            dt = Clock.tick()/6000
            radian+=dt
            for event  in pygame.event.get() : 
                if event.type == pygame.QUIT : pygame.quit();  sys.exit()
                
                #cam.events(event)
            screen.fill((255,255,255))
            '''
            pas = 4
            for i in range(60*pas + 1) :
                points  = []
                x, y = 16,  i/(np.power(2,pas)) 
                u = -22-i/pas
                z=0
                x-=self.cam.pos[0]
                y-=self.cam.pos[1]
                z-=self.cam.pos[2]
                f= 23/z
                x,y = x*f,y*f
                rangeC = 2/3
                b = -22
                n = -82
                if (u > b):
                        u = b
                if (u < n):
                        u = n
                
                coef = (u*rangeC)/((b-n)) + (-b*rangeC)/((b-n))
                couleur = hsv2rgb(-coef,1,1)
                pygame.draw.rect(screen,couleur, (self.cx+int(x)-1, self.cy+int(y)-1, f*1, f*0.25))
                if (u == -22):
                    font = pygame.font.SysFont("police/freestylescript.ttf", 15,False, True)
                    afficher = font.render(str("[dBm]"), 1, (0, 0, 0))
                    screen.blit(afficher, (self.cx+int(x)-1+(1.9*f), self.cy+int(y) - (0.1*f)))
                if (u == -22 or u == -32 or u == -42 or u == -52 or u == -62 or u == -72 or u == -82 ) :
                    variable = u
                    pygame.draw.line(screen, (0,0,0),(self.cx+int(x)-1+0.9*f, self.cy+int(y)-1), (self.cx+int(x)-1+1.0*f, self.cy+int(y)-1), 1)
                    font = pygame.font.SysFont("police/freestylescript.ttf", 15,False, True)
                    afficher = font.render(str(variable), 1, (0, 0, 0))
                    screen.blit(afficher, (self.cx+int(x)-1+(1.2*f),- (0.1*f) + self.cy+int(y)))
            '''
            pas = 4
            for i in range(38*pas + 1) :
                points  = []
                x, y = 12.2,  6+ -i/(np.power(2,pas)) 
                u = 54+(10*i/pas)
                #u = int((379/31)*u + (54+(82*379/31)))
                z=0
                x-=self.cam.pos[0]
                y-=self.cam.pos[1]
                z-=self.cam.pos[2]
                f= 50/z
                x,y = x*f,y*f
                rangeC = 2/3
                b = 433
                n = 54
                if (u > b):
                        u = b
                if (u < n):
                        u = n
                
                coef = (u*rangeC)/((b-n)) + (-b*rangeC)/((b-n))
                couleur = hsv2rgb(-coef,1,1)
                pygame.draw.rect(screen,couleur, (self.cx+int(x)-1, self.cy+int(y)-1, f*0.6, f*0.2))
                if (u == 433):
                    font = pygame.font.SysFont("police/freestylescript.ttf", 15,False, True)
                    afficher = font.render(str("[M B/s]"), 1, (0, 0, 0))
                    screen.blit(afficher, (self.cx+int(x)-1+(1.5*f), self.cy+int(y) - (0.1*f)))
                if (u == 54 or u ==104 or u == 154 or u == 204 or u == 254 or u == 304 or u == 354 or u == 404 or u == 433 ) :
                    variable = u
                    pygame.draw.line(screen, (0,0,0),(self.cx+int(x)-1+0.45*f, self.cy+int(y)-1), (self.cx+int(x)-1+0.6*f, self.cy+int(y)-1), 1)
                    font = pygame.font.SysFont("police/freestylescript.ttf", 15,False, True)
                    afficher = font.render(str(variable), 1, (0, 0, 0))
                    screen.blit(afficher, (self.cx+int(x)-1+(0.68*f),-(0.1*f) + self.cy+int(y)))

            # print("Drawing walls")
            
            
            # print("Drawing Rx")
            
            for r in self.Rx : 
                r.draw(screen, self.Distortion, [self.cx, self.cy], 20/(-self.cam.pos[2]))
                if DrawRays : 
                    for ray in r.rays : 
                        ray.draw(screen, self.Distortion)
            
            # print("Drawing Tx")
            for t in self.Tx : 
                t.draw(screen, self.Distortion)
            
            for w in self.Walls : 
                w.draw(screen, self.Distortion, (0,0,0))
                
            pygame.display.flip()
            key = pygame.key.get_pressed()
            self.cam.update(dt, key)

            


    

    

