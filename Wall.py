import numpy as np 
import Line
from scipy.constants import c, mu_0, epsilon_0

EPS_AIR = epsilon_0
SIGMA_AIR = 0 #conductivity
FREQ = 5e9
BETA = 2*np.pi*FREQ / c

class wall (Line.Line): 
    def __init__(self, Width, epsilon, sigma, StartVec, EndVec): 
        self._width = Width #notee l dans le sylla
        self._eps = epsilon #s'assurer qu'on entre bien epsr*eps0 alors 
        self._sigma = sigma
        super(wall, self).__init__(StartVec, EndVec)


    def ReflectionCoeff(self, thetaI, c_eps1, c_eps2):
        """
        Returns the reflection coefficient for a perpendicular polarization 
        """
        Z1 = np.sqrt(mu_0/c_eps1)
        Z2 = np.sqrt(mu_0/c_eps2)
        thetaT = np.arcsin(np.sqrt(np.real(c_eps1) / np.real(c_eps2)) * np.sin(thetaI)) 
        coeff = (Z2*np.cos(thetaI) - Z1*np.cos(thetaT)) / (Z2*np.cos(thetaI) + Z1*np.cos(thetaT)) 
        return coeff


    def ReflectionCoeffWall(self, thetaI): 
        '''
        Returns the reflection coefficient of the wall for a given incident angle thetaI
        '''
        c_eps1 = EPS_AIR - 1j*SIGMA_AIR / (2*np.pi*FREQ)
        c_eps2 = self._eps - 1j*self._sigma / (2*np.pi*FREQ)
        thetaT = np.arcsin(np.sqrt(np.real(c_eps1) / np.real(c_eps2)) * np.sin(thetaI)) 
        reflCoeff = self.ReflectionCoeff(thetaI, c_eps1, c_eps2)
        gamma_m = 1j*2*np.pi*FREQ*np.sqrt(mu_0*c_eps2)
        s = self._width / np.cos(thetaT)
        exp_part = np.exp(-2*gamma_m*s + 1j*BETA*2*s*np.sin(thetaT)*np.sin(thetaI)) 
        coeff = reflCoeff + (1 - (reflCoeff**2)) * reflCoeff * exp_part / (1 - (reflCoeff**2) * exp_part)
        return coeff 


    def TransmissionCoeffWall(self, thetaI) : 
        '''
        Returns the transmission coefficient of the wall for a given incident angle thetaI
        '''        
        c_eps1 = EPS_AIR - 1j*SIGMA_AIR / (2*np.pi*FREQ)
        c_eps2 = self._eps - 1j*self._sigma / (2*np.pi*FREQ)
        thetaT = np.arcsin(np.sqrt(np.real(c_eps1) / np.real(c_eps2)) * np.sin(thetaI)) 
        reflCoeff = self.ReflectionCoeff(thetaI, c_eps1, c_eps2)
        gamma_m = 1j*2*np.pi*FREQ*np.sqrt(mu_0*c_eps2)
        s = self._width / np.cos(thetaT)
        exp_part = np.exp(-2*gamma_m*s + 1j*BETA*2*s*np.sin(thetaT)*np.sin(thetaI)) 
        coeff = (1 - (reflCoeff**2)) * np.exp(-gamma_m*s) / (1 - (reflCoeff**2) * exp_part)
        return coeff
    
