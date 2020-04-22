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
    def __init__(self, PosVec, EmittedPower, Gains : List[Callable[Any]], ImagedSource : Antenna = None, SymmetryWall : Wall.wall = None): 
        self._pos = PosVec 
        self._emittedPower = EmittedPower
        self.gains = Gains 
        self.Source = ImagedSource
        self.Wall = SymmetryWall

    def CreateImage(self, symWall : Wall.wall) -> Antenna : 
        
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


    def Propagate(self, Rx_pos, Walls: List[Wall.wall], ray : Ray.Ray ): 
        
        gains = [] 
        line = Line.Line(Rx_pos, self._pos)
        P = [] 
        IsReflexionWallHit = False
        for w in Walls :
            IsIntersected, P = line.Intersect(w) 
            if IsIntersected: 
                theta = line.Angle(w)
                if (w == self.Wall) : 
                    gains.append(w.ReflectionCoeffWall(theta)) 
                    IsReflexionWallHit = True
                else : 
                    gains.append(w.TransmissionCoeffWall(theta))
        
        # le rayon emis doit passer par le mur de la reflection sinon le scenario n'est pas valide 
        if(IsReflexionWallHit) : 
            ray.add(Ray.Beam(Rx_pos, P, gains))
            # S'il n'y pas de source ca signifie que le transmitter actuel est un transmitter original et donc pas image 
            if (self.Source != None ) : 
                ray = self.Source.Propagate(P, Walls, ray)
            return ray
        else : 
            return None


