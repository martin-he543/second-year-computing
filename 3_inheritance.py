# OOP2: Inheritance
import numpy as np

# EX 1: INHERITANCE EXAMPLE ("is a")
# Polymorphic behaviour between classes
class Animal:
    """ a made up class to act as a base class
    for a teaching example
    DJC- October 2013, Revised AMacK Oct 2016"""
    def breaths(self):
        return True
    def likes_to_eat(self):
        return "food"
    
class Carnivore(Animal):
    """A derived class which inherits from animal """
    def likes_to_eat(self):
        return "Meat!"
    def has_sharp_teeth(self):
        return True

class Herbivore(Animal):
    """ another derived class which inherits from animal """
    def likes_to_eat(self):
        return "plants"
    def has_flat_teeth(self):
        return True


#######################################################################
# EX 2: COMPOSITION EXAMPLE ("has a")

class Scientist:
    def __init__(self,name,field):
        self.__name = name
        self.__field = field
    def name(self):
        return self.__name
    def field(self):
        return self.__field

class Physicist(Scientist):
    def __init__(self,name):
        #Now the field is always "Physics"
        Scientist.__init__(self,name, "Physics")  
        # explicitly calling the Scientist constructor

#%% TASK 21 & 22
class Shape:
    def set(self, newColour):
        self.__colour = newColour
    def colour(self):
        return self.__colour

class Square(Shape):
    def __init__(self,length):
        self.__length = length
    def area(self):
        return self.__length*self.__length
    
class Triangle(Shape):
    def __init__(self,perpendicularHeight,baseLength):
        self.__ppHeight = perpendicularHeight
        self.__bLength = baseLength
    def area(self):
        return 0.5*self.__bLength*self.__ppHeight
    
class Circle(Shape):
    def __init__(self,radius):
        self.__radius = radius
    def area(self):
        return np.pi*self.__radius*self.__radius

s = Shape()
s.set('Blue')
print(s.colour())

t = Triangle(20,30)
t.set('Yellow')
print(t.colour())
print(t.area(),'cm²')

c = Circle(5)
t.set('Burgandy')
print(t.colour())
print(t.area(),'cm²')

sq = Square(69)
t.set('Blue')
print(t.colour())
print(t.area(),'cm²')


#%% TASK 23 - isinstance

print(isinstance(t,Square))
print(isinstance(sq,Square))
print(isinstance(t,Triangle))
print(isinstance(t,Shape)) # Accepts inheritance conditions

#%% TASK 24 
def checkType(variable):
    if isinstance(variable,Shape):
        variable.set('Red')
        print(variable,"is now",variable.colour())

checkType(sq)



#%% TASK 25 - Class Variables
class MyClass:
    # no need for dot notation
    class_var = 0

    def __init__(self, vv):
        self.inst_var = vv       # now need the dot notation
        MyClass.class_var += 1   # note that it is of MyClass not self
        
        
a = MyClass(4)
print(a.inst_var)
# Upon variable intialisation, the variable was incremented.
print(MyClass.class_var)
# This is discouraged practice, as can be overriden.
print(a.class_var)

b,c = MyClass(5), MyClass(4.3)
print(b.inst_var, c.inst_var)

print(MyClass.class_var)
print(a.class_var, b.class_var, c.class_var)
# %%
