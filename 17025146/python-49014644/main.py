from sympy import *
x,y = symbols("x,y")
f = x**4 - 2*x**2*y**2 + y ** 4
print(factor(f))