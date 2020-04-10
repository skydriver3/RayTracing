import numpy as np 
import Line
class wall (Line.Line): 
    def __init__(self, Width, epsilon, mu, StartVec, EndVec): 
        self._width = Width
        self._eps = epsilon 
        self._mu = mu 
        super(wall, self).__init__(StartVec, EndVec)


    def RelfexionGain(self, theta): 
        '''
        To Do 
        '''
        return 0 

    def TransmissionGain(self, theta) : 
        '''
        To Do 
        '''        
        return 0 
    
