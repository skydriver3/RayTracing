import numpy as np 
import Line
from typing import List
from scipy.constants import c

BETA = 2*np.pi*(5e9) / c

class Ray(Line.Line) : #On y rajouterait pas l'antenne en parametre pour avoir Gtx et Ptx propre a l'antenne?
    def __init__(self, StartVec, EndVec, Gains : List[int]) : 
        super(Ray, self).__init__(StartVec, EndVec)
        self.gains = Gains


    def elecFieldDirect(self, Gtx, Ptx, BETA):
        """
        Returns the complex electric field for a direct path d
        """
        d = self.Distance
        elecFieldDirect = np.sqrt(60*(self*Gtx)*Ptx) * np.exp(-1j*BETA*d) / d #(8.77)

        return elecFieldDirect