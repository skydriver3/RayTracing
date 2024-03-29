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


    def Propagate(self, Rx_pos, Walls: List["Wall.wall"], ray : "Ray.Ray"  = None, previousSymWall = None ): 
        
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
                elif(w != previousSymWall) : 
                    gains.append(w.TransmissionCoeffWall(theta))
        
        if(ray != None ): 
            # S'il n'y pas de source ca signifie que le transmitter actuel est un transmitter original et donc pas image 
            ray.add(Ray.Beam(Rx_pos, P, gains))
        else : 
            ray = Ray.Ray([Ray.Beam(Rx_pos, P, gains)])
        
        # le rayon emis doit passer par le mur de la reflection sinon le scenario n'est pas valide 
        if(IsReflexionWallHit) : 
            ray = self.Source.Propagate(P, Walls, ray, self.Wall) 

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
        #print("POWER", powerTot)
        return powerTot
    
    def dBmToBinary(self):
        powers = [ray.allPowers() for ray in self.rays]
        powerTot = np.sum(powers)
        powerTot = 10*np.log10(powerTot / 0.001)
        Mbs = (379/31)*powerTot + (54+(82*379/31))
        return Mbs
    
    def MapMbsToColor(self, u) :
        rangeC = 2/3
        b = 433
        n = 54
        if (u > b):
            u = b
        if (u < n):
            u = n
                
        coef = (u*rangeC)/((b-n)) + (-b*rangeC)/((b-n))
        couleur = hsv2rgb(-coef,1,1)
        
        return couleur
    
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
            pygame.draw.circle(screen, (0,0,0), funcDistortion(self._pos), 1)
        
        else : 
            u, v = self._pos
            x, y = funcDistortion(self._pos)
            liste_power = [[-82,-82,-82,-82,-82,-82,-82,-82],[-82,-82,-82,-82,-82,-82,-82,-82],
                           [-82,-82,-82,-82,-82,-82,-82,-82],[-82,-82,-82,-82,-82,-82,-82,-82],
                           [-82,-82,-82,-82,-82,-82,-82,-82],[-82,-82,-82,-82,-82,-82,-82,-82],
                           [-82,-82,-82,-82,-82,-82,-82,-82],[-72,-64,-75,-77,-79,-75,-82,-82],
                           [-69,-60,-75,-79,-79,-78,-78,-79],[-56,-61,-79,-71,-75,-79,-78,-78],
                           [-60,-72,-81,-75,-77,-79,-72,-79],
                           [-23,-31,-35,-40,-42,-47, -47], [-24,-33,-37,-31,-43,-45, -45],
                           [-25,-31,-42,-42,-47,-48, -48],[-32,-43,-42,-44,-45,-50, -50],
                           [-43,-37,-40,-45,-46,-47, -47],[-49,-45,-48,-48,-50,-50, -50]]
            '''
            if (0 <= u <= 11):
                pygame.draw.rect(screen,self.MapPowerToColor(liste_power[int(u)][int(v)]), (int(x)-1, int(y)-1, f*2, f*2))
            else :
                pygame.draw.rect(screen,self.MapPowerToColor(liste_power[int(u)][int(v+5)]), (int(x)-1, int(y)-1, f*2, f*2))
            '''
            #print("power =",self.getPower(), "Mbs =",self.dBmToBinary() )
            #pygame.draw.rect(screen,self.MapPowerToColor(self.getPower()), (int(x)-1, int(y)-1, f*0.9, f*0.9))
            pygame.draw.rect(screen,self.MapMbsToColor(self.dBmToBinary()), (int(x)-1, int(y)-1, f*0.9, f*0.9))

    def __repr__(self):
        return "I'm an Antenna"
