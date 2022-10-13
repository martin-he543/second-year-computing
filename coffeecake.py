"""
A module to investigate namespaces and scope.
C Paterson 30/9/2013
"""

a = "coffee"
b = "cake"

def func1():
    a = "drunk"
    b = "eaten"
    return a, b

def func2(a, b):
    a = "drunk"
    b = "eaten"
    return a, b

def func3():
    c = a
    return c

def func4():
    c = a
    return c
    a = c

def func5():
    global a
    a = "drunk"
    b = "eaten"
    return a, b

def func6():
    a = "drunk"
    return locals()

def func7():
    a = "empty"
    return globals()