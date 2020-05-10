import numpy as np  
import Wall 
import Ray
import Line
from typing import Callable, Any, List
import colorsys
import pygame

def rotate_decorator(gain, wallAngle): 
    def rotated_gain(theta, phi) : 
        return gain( - theta + (2 * wallAngle), -phi + ( 2 * wallAngle))
    return rotated_gain

def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))

class Antenna : 
    def __init__(self, PosVec, EmittedPower, Gains, ImagedSource : "Antenna" = None, SymmetryWall : "Wall.wall" = None): 
        self._pos = PosVec 
        self._emittedPower = EmittedPower
        self.gains = Gains 
        self.Source = ImagedSource
        self.Wall = SymmetryWall
        self.rays = [] 

    def CreateImage(self, symWall : "Wall.wall") -> "Antenna" : 
        
        ################### Calcul position antenna ################################
        pos = []
        if (np.shape(symWall.Direction)[0]  == 3 ) : 
                ax1 = np.dot(symWall.Direction[:,0], self._pos - symWall.Vec2) * symWall.Direction[:, 0] + symWall.Vec2
                ax2 = np.dot(symWall.Direction[:,1], self._pos - symWall.Vec2) * symWall.Direction[:, 1] + symWall.Vec2
                pos = ax1 + ax2        
        else : 
            pos = np.dot(symWall.Direction, self._pos - symWall.Vec2) * symWall.Direction + symWall.Vec2
        pos += (pos - self._pos)
        ############################################################################


        return Antenna(pos, None, None, self, symWall)


    def Propagate(self, Rx_pos, Walls: List["Wall.wall"], ray : "Ray.Ray"  = None ): 
        
        #print("Called Propagate : the propagation wall is " + repr(self.Wall))
        #print(f"the image position : {self._pos}")
        gains = [] 
        line = Line.Line(Rx_pos, self._pos)
        P = self._pos
        IsReflexionWallHit = False
        for w in Walls :
            # print("going through walls")
            IsIntersected, intersectionPoint = line.Intersect(w) 
            if IsIntersected: 
                theta = line.incidenceAngle(w)
                if (w == self.Wall) : 
                    gains.append(w.ReflectionCoeffWall(theta)) 
                    IsReflexionWallHit = True
                    P = intersectionPoint
                    #print("Hit the reflective wall !!!")
                else : 
                    gains.append(w.TransmissionCoeffWall(theta))
        
        if(ray != None ): 
            # S'il n'y pas de source ca signifie que le transmitter actuel est un transmitter original et donc pas image 
            ray.add(Ray.Beam(Rx_pos, P, gains))
        else : 
            ray = Ray.Ray([Ray.Beam(Rx_pos, P, gains)])
        
        # le rayon emis doit passer par le mur de la reflection sinon le scenario n'est pas valide 
        if(IsReflexionWallHit) : 
            ray = self.Source.Propagate(P, Walls, ray) 

            return ray
        else : 
            if (self.Source == None): # si c'est une source initial c'est normale qu'il n'ai pas reflection
                return ray 
            else :
                #print("No Reflexion hit !!") 
                return None

    def getPower(self):        
        powers = [ray.allPowers() for ray in self.rays]
        powerTot = np.sum(powers)
        #transforme en dBm
        powerTot = 10*np.log10(powerTot / 0.001)
        return powerTot
    
    def MapPowerToColor(self, Power) : 
        if (Power > -22):
            Power = -22
        if (Power < -82): #dBm
            Power = -82
        
        #coef = 2*Power/(3*60) + 2*20/(3*60)
        coef = Power/(90) + 22/(90)

        couleur = hsv2rgb(-coef,1,1)
        return couleur


    def draw(self, screen, funcDistortion, CenterCoor = [], f = 1): 
        if(len(self.rays) == 0 ) : 
            pygame.draw.circle(screen, (0,255,0), funcDistortion(self._pos), 5)
        
        else : 
            x, y = funcDistortion(self._pos)
            pygame.draw.rect(screen,self.MapPowerToColor(self.getPower()), (CenterCoor[0]+int(x)-1, CenterCoor[1]+int(y)-1, f*0.5, f*0.5))

    def __repr__(self):
        return "I'm an Antenna"
