import numpy as np  
import Wall 
import Ray
import Line
from typing import Callable, Any, List

def rotate_decorator(gain, wallAngle): 
    def rotated_gain(theta, phi) : 
        return gain( - theta + (2 * wallAngle), -phi + ( 2 * wallAngle))
    return rotated_gain


class Antenna : 
    def __init__(self, PosVec, EmittedPower, Gains, ImagedSource : "Antenna" = None, SymmetryWall : "Wall.wall" = None): 
        self._pos = PosVec 
        self._emittedPower = EmittedPower
        self.gains = Gains 
        self.Source = ImagedSource
        self.Wall = SymmetryWall

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
        
        print("Called Propagate : the propagation wall is " + repr(self.Wall))
        print(f"the image position : {self._pos}")
        gains = [] 
        line = Line.Line(Rx_pos, self._pos)
        P = self._pos
        IsReflexionWallHit = False
        for w in Walls :
            # print("going through walls")
            IsIntersected, intersectionPoint = line.Intersect(w) 
            if IsIntersected: 
                print("Intersection")
                theta = line.Angle(w)
                if (w == self.Wall) : 
                    gains.append(w.ReflectionCoeffWall(theta)) 
                    IsReflexionWallHit = True
                    P = intersectionPoint
                    print("Hit the reflective wall !!!")
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
                print("No Reflexion hit !!") 
                return None


