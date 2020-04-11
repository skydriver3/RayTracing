import numpy as np 

class Line : 
    def __init__(self, StartVec, EndVec) : 
        self.Vec1 = StartVec
        self.Vec2 = EndVec 
        self.Direction = self.Vec1 - self.Vec2
        self.Distance = np.linalg.norm(self.Direction)
        self.Direction /= self.Distance
        self.angle = np.arccos(self.Direction[0])
        self.slope = np.sqrt( 1 - (self.Direction[0] ** 2)) / self.Direction[0]
        self.Y0 = self.Vec2[1] + self.Direction[1] * (- self.Vec2[0] / self.Direction[0])
    
    def Contains(self, Point) : 
        if(len(Point) > 2): 
            P = (Point - self.Vec2)  
            lamda = [P[i] / self.Distance[i] for i in range(len(P))] #Distance est une norme; quid [i], Direction plutot?
            for i in range(len(lamda) - 1) : 
                if lamda[0] != lamda[i + 1] : 
                    return False
            if lamda[0] < 0 or lamda[0] > self.Distance : 
                return False 

            else : 
                return True 
        else : 
            if ( Point[1] == self.Y0 + self.slope * Point[0] and np.linalg.norm(Point - self.Vec2) <= self.Distance) : 
                return True


    
    def Intersect(self, OtherLine : Line) : 
        x = ( self.Y0 - OtherLine.Y0 ) / ( OtherLine.slope - self.slope )
        y = self.Y0 + self.slope * x 
        P = [x, y]
        if self.Contains(P) : 
            return (True, [x, y])  
        else : 
            return (False, [0, 0]) 

    def Angle(self, OtherLine : Line) : 
        '''
        Can be optimized for 2D cases ( no use of arccos )
        '''
        # angle = self.angle + OtherLine.angle ( + check depending on which angle it is )
        angle = np.arccos(np.dot(self.Direction, OtherLine.Direction))  
        if angle > ( np.pi / 2) : 
            return np.pi - angle 
        else : 
            return angle    

    def incidenceAngle(self, OtherLine : Line) : 
        '''
        Calculate the incidence angle on a wall
        '''
        # angle = self.angle + OtherLine.angle ( + check depending on which angle it is )
        angle = np.arccos(np.dot(self.Direction, OtherLine.Direction))  
        if angle > ( np.pi / 2) : 
            return angle - np.pi / 2     #On cherche l'angle entre la perpendiculaire du mur et notre rayon, cf loi de Snell p135
        else : 
            return np.pi / 2 - angle    

    
