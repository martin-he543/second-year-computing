#%%     TASK 2

a = 100
b = a

a == b
# Equality checks if values are identical
print(a is b)

c = [1, 2, 3]
d = [1, 2, 3]
# Identity checks if point to same memory
print(c is d)

# %%    TASK 3

e = [1, 2, 3]
f = e

e[0] = 100
f[1] = 200

print(e, f)

# %%    TASK 4

g = [1, 2, 3]
h= g.copy()

g[0] = 100
h[1] = 200

print(g, h)

#%%     TASK 5 & 6

i = [1, 2, 3, [1, 2, 3]]
j = i.copy()

i[0] = 100
j[1] = 200
i[3].append(4)
j[3].append(5)

print(i, j)
print(i[3] is j[3])
# %%    TASK 7
from copy import deepcopy
k = [1, 2, 3, [1, 2, 3]]
l = deepcopy(k)
# Deepcopy properly copies a new version of the variable.

k[0] = 100
l[1] = 200
k[3].append(4)
l[3].append(5)

print(k, l)
print(k[3] is l[3])
# %%    TASK 8
import mymodule as mym

print(mym.fibo(10))
print(mym.fibo1(20))

# %%    TASK 9
# This is a comment

a = 12  # The rest of this line is a comment

def func():  # The rest of this line is a comment
    """
    Function doc string
    """
    return 12

# This is a long comment
# that spans multiple lines.

"""
This is a multiline
string literal
"""

#%%     TASK 10
print(mym.fibo1(20))
print(mym.fibo2(30))
print(mym.fibo(100))

# %%    TASK 11

import coffeecake as coca

# Prints out the Global A and Global B
# coca.func1()
# print(coca.a, coca.b)

# Prints out the Global A and Global B still
# coca.func2(coca.a, coca.b)
# print(coca.a, coca.b)

# Returns "coffee" as expected
# print(coca.func3())

# Error, as does not work
# print(coca.func4())

# Returns "drunk cake" as 'a' is made a global variable
coca.func5()
print(coca.a, coca.b)

# coca.func6() returns local variables
# coca.func7() returns global variables

# %%    TASK 12



# %%
