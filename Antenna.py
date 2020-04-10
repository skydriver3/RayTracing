import numpy as np  
import Wall 
import Ray

def rotate_decorator(gain, wallAngle): 
    def rotated_gain(theta, phi) : 
        return gain( - theta + (2 * wallAngle), -phi + ( 2 * wallAngle))
    return rotated_gain


class Antenna : 
    def __init__(self, PosVec, EmittedPower, Gains : list[Callable[Any]], ImagedSource : Antenna = None, SymmetryWall : Wall.wall = None): 
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


    def Propagate(self, Rx_pos, Walls: list[Wall.wall], trajectory ): 
        
        ray = Ray.Ray(Rx_pos, self._pos, [])
        P = [] 
        for w in Walls :
            IsIntersected, P = ray.Intersect(w) 
            if IsIntersected: 
                theta = ray.Angle(w)
                if (w == self.Wall) : 
                    ray.gains.append(w.ReflexionGain(theta)) 

                else : 
                    ray.gains.append(w.TransmissionGain(theta))
        
        trajectory.append(ray)
        if (self.Source != None ) : 
            trajectory = self.Source.Propagate(P, Walls, trajectory)
        return trajectory


