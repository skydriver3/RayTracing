import numpy as np 
import Line
from typing import List
from scipy.constants import c
import pygame

#everything below to remove and place it in the antenna
Gtx = 4*np.pi*0.13 
Ptx = 0.1
FREQ = 5e9
BETA = 2*np.pi*(FREQ) / c
H_EQ = -c / (FREQ * np.pi)
R_A = 73.45612758

class Beam(Line.Line) : #On y rajouterait pas l'antenne en parametre pour avoir Gtx et Ptx propre a l'antenne?
    def __init__(self, StartVec, EndVec, Gains : list) : 
        super(Beam, self).__init__(StartVec, EndVec)
        self.gains = Gains


    def __add__(self, otherRay : Beam ): 
        return Ray([self, otherRay])

    def elecFieldDirect(self, Gtx, Ptx, BETA): #parameters are properties of the antenna, add antenna to the Ray parameters
    #def elecFieldDirect(self, Antenna):
        """
        Returns the complex electric field for a direct path d
        """
        d = self.Distance
        elecFieldDirect = np.sqrt(60*(self*Gtx)*Ptx) * np.exp(-1j*BETA*d) / d #(8.77)

        return elecFieldDirect

    def averagePower(self, eField): #eField contient deja toutes les contributions
        """
        Returns the average power for a given electric field
        """
        power = 1/(8*R_A) * (np.linalg.norm(H_EQ * eField))**2
        return power


    def directPower(self, Walls): #angle issue, OtherLine?
        """
        Returns the average power of a direct ray joining Tx and Rx with (or not) transmission(s)
        """
        coeff = 1
        for i in range(len(Walls)): #si pas de mur, on ne rentre juste pas dans le for
            thetaI = self.incidenceAngle(Walls[i])
            coeff *= Walls[i].TransmissionCoeffWall(thetaI)

        eField = coeff * self.elecFieldDirect(Gtx, Ptx, BETA)
        power = self.averagePower(eField)

        return power

    def reflectionPower(self, Walls):
        """
        To do 
        """
        return 0

class Ray : 
    def __init__(self, beams : List[Beam]) : 
        '''
        beams : a list containing all the rays making up the whole trajectory ( rays for each reflexion )
        ''' 
        self.DistanceTraveled = 0 
        self.Coordinates = [] 
        self.Coefficients = [] 
        for b in beams : 
            self.add(b) 


    def add(self, beam : Beam): 
        self.DistanceTraveled += beam.Distance
        self.Coordinates.append([beam.Vec1, beam.Vec2])
        self.Coefficients.extend(beam.gains)
    
    def draw(self, canvas) : 
        for coor in self.Coordinates : 
            pygame.draw.line(canvas, (255, 0, 0), coor[0], coor[1])
            

