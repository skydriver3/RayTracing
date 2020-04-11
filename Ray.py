import numpy as np 
import Line
from typing import List

class Ray(Line.Line) : 
    def __init__(self, StartVec, EndVec, Gains : List[int]) : 
        super(Ray, self).__init__(StartVec, EndVec)
        self.gains = Gains
    

