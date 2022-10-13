import numpy as np
from scipy.constants import speed_of_light as speedol

class FourVector:    
    """
    Four Vector Class
    ________________________________
    Stores both time-like and space-like parameters.
    """
    def __init__(self, ct=0, x=0, y=0, z=0):
        self.__ct = ct
        self.__r = np.array([x,y,z])

        if x > 3:
            raise Exception("Error. The value of x is larger than 3.")
    
    # PRINT method - returns on variable submission
    def __repr__(self):
        return "FourVector(ct=" + str(self.__ct) + ", r=" + str(self.__r) + ")"

    # HUMAN PRINT method - returns on print statement
    def __str__(self):
        return "ct:" + str(self.__ct) + ", r:" + str(self.__r)

    # Returns the "ct" data attribute
    def ct(self):
        return self.__ct

    # Returns the "r" data attribute
    def r(self):
        return self.__r

    # Define a new "r" data attribute
    def setr(self, new_x, new_y, new_z):
        self.__r = np.array([new_x,new_y,new_z])

    # Define a new "ct" data attribute
    def setct(self, new_ct):
        self.__ct = new_ct

    # Define the copy function
    def copy(self):
        return FourVector(self.__ct, self.__r[0], self.__r[1],self.__r[2])

    # Implement the inner product
    def inner(self, other):
        return self.ct() * other.ct() - ((self.r()[0] * other.r()[0]) + (self.r()[1] * other.r()[1]) + (self.r()[2] * other.r()[2]))

    # Implement magnitude squared
    def magsquare(self):
        return (self.r()[0])**2 + (self.r()[1])**2 + (self.r()[2])**2 + (self.ct())**2

    # Implement Lorentz Boost in z-direction
    def boost(self,beta):
        gamma = 1/np.sqrt(1-beta**2)
        z_prime = gamma*(self.r()[2] - (beta*self.ct()))
        ct_prime = gamma*(self.ct() - beta*self.r()[2])
        x,y = self.r()[0], self.r()[1]
        return FourVector(ct_prime, x, y, z_prime)
        
    # Implement the + operator between objects
    def __add__(some, other):
        return FourVector(some.ct() + other.ct(), some.r()[0] + other.r()[0], some.r()[1] + other.r()[1], some.r()[2] + other.r()[2])
    
    # Implement the += operator between objects
    def __iadd__(self, other):
        return FourVector(self.ct() + other.ct(), self.r()[0] + other.r()[0], self.r()[1] + other.r()[1], self.r()[2] + other.r()[2])

    # Implement the - operator between objects
    def __sub__(some, other):
        return FourVector(some.ct() - other.ct(), some.r()[0] - other.r()[0], some.r()[1] - other.r()[1], some.r()[2] - other.r()[2])
    
    # Implement the -= operator between objects
    def __isub__(self, other):
        return FourVector(self.ct() - other.ct(), self.r()[0] - other.r()[0], self.r()[1] - other.r()[1], self.r()[2] - other.r()[2])