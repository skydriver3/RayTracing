import numpy as np 
import pygame 

class Line : 
    def __init__(self, StartVec, EndVec) : 
        self.Vec1 = StartVec
        self.Vec2 = EndVec 
        self.Direction = self.Vec1 - self.Vec2
        self.Distance = np.linalg.norm(self.Direction)
        self.Direction = self.Direction / self.Distance
        self.angle = np.arccos(self.Direction[0])
        # self.slope = np.sqrt( 1 - (self.Direction[0] ** 2)) / self.Direction[0] # tan = sin / cos 
        # self.Y0 = self.Vec2[1] + self.Direction[1] * (- self.Vec2[0] / self.Direction[0])
    
    def MidPoint(self) : 
        return self.Vec2 + self.Direction * (self.Distance / 2) 

    def Contains(self, Point) : 
        # if(len(Point) > 2): 
        # P = (Point - self.Vec2)  
        # lamda = [P[i] / self.Direction[i] for i in range(len(P))] #Distance est une norme; quid [i], Direction plutot?
        # for i in range(len(lamda) - 1) : 
        #     if lamda[0] != lamda[i + 1] : 
        #         return False
        # if lamda[0] < 0 or lamda[0] > self.Distance : 
        #     return False 

        # else : 
        #     return True 

        IsFirstLamda = True 
        lamda = 0 
        P = (Point - self.MidPoint()) 
        for i in range(len(P)) : 
            if self.Direction[i] == 0: 
                if(P[i] != 0): 
                    return False  
            else : 
                if IsFirstLamda : 
                    lamda = round(P[i] / self.Direction[i], 6) 
                    IsFirstLamda = False
                    
                    if np.abs(lamda) > self.Distance / 2 : 
                        return False
                else : 
                    tmp = round(P[i] / self.Direction[i], 6) 
                    if lamda != tmp : 
                        return False 
        
        return True 

                
        # else : 
        #     if ( (Point[1] == self.Y0 + self.slope * Point[0]) and (np.linalg.norm(Point - self.Vec2) <= self.Distance)) : 
        #         return True
        #     else : 
        #         return False

    
    def draw(self, screen, funcDistortion, color): 
        pygame.draw.line(screen, color, funcDistortion(self.Vec1), funcDistortion(self.Vec2), 4)
    
    def Intersect(self, OtherLine : "Line") : 
        # x = ( self.Y0 - OtherLine.Y0 ) / ( OtherLine.slope - self.slope )
        # y = self.Y0 + self.slope * x 
        P= []
 
        num = (OtherLine.Direction[1] * (self.Vec1[0] - OtherLine.Vec1[0])) - (OtherLine.Direction[0] * (self.Vec1[1] - OtherLine.Vec1[1]))
        denom = self.Direction[1] * OtherLine.Direction[0] - self.Direction[0] * OtherLine.Direction[1]
        if(denom != 0 ):
            lamda = num / denom 
            P = self.Vec1 + self.Direction * lamda
        else : 
            return (False, None)

        #print(f"Printing intersection point : {P} ")
        if self.Contains(P) and OtherLine.Contains(P) : 
            return (True, P)  
        else : 
            return (False, None) 

    def Angle(self, OtherLine) : 
        '''
        Can be optimized for 2D cases ( no use of arccos )
        '''
        # angle = self.angle + OtherLine.angle ( + check depending on which angle it is )
        angle = np.arccos(np.dot(self.Direction, OtherLine.Direction))  
        if angle > ( np.pi / 2) : 
            return np.pi - angle 
        else : 
            return angle    

    def incidenceAngle(self, OtherLine ) : 
        '''
        Calculate the incidence angle on a wall
        '''
        # angle = self.angle + OtherLine.angle ( + check depending on which angle it is )
        angle = np.arccos(np.dot(self.Direction, OtherLine.Direction))  
        if angle > ( np.pi / 2) : 
            return angle - np.pi / 2     #On cherche l'angle entre la perpendiculaire du mur et notre rayon, cf loi de Snell p135
        else : 
            return np.pi / 2 - angle    

    
