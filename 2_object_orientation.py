#       OOP 1: Classes & Objects
#%%     PRELIMINARY TASK 13

class MyComplex:
    """
    Another complex number class
    (WARNING: you probably want to use Python's built-in complex instead)
    """

    def __init__(self, re=0.0, im=0.0):
        self.real = re
        self.imag = im

c1 = MyComplex(42.0, 24.0)
print(c1.real, c1.imag)


#%%     TASK 13 & 14

from relativity import *
        
P0 = FourVector()
print(P0)

P2 = FourVector(ct=99.9, x=1, y=2, z=3)
print(P2)

    
#%%    TASK 15 & 16

# print(P0.__ct)

P0.setr(2,4,7)
P2.setct(91)

print(P0, P2)

print(P0.r())
print(P2.ct())

P0.copy()

#%%    TASK 17

# Verify that all the operators work as intended.
print(P0 + P2)
print(P0 - P2)

P0 += P2
print(P0)

P0 -= P2
print(P0)


#%%    TASK 18, 19, 20
print("inner product of P0 and P2", P0.inner(P2))
print("inner product of P2 and P0", P2.inner(P0))

print("boost of P2 by β = 0.8", P2.boost(0.8))

# Check square invariance. ERROR! not equivalent
print("len squared prior boost", P2.magsquare())
print("len squared after boost", (P2.boost(0.8)).magsquare())

