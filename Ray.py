import numpy as np 
import Line

class Ray(Line.Line) : 
    def __init__(self, StartVec, EndVec, Gains : list[int]) : 
        super(Ray, self).__init__(StartVec, EndVec)
        self.gains = Gains
    

