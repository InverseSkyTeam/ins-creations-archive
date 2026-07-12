from drone import *
from teacher import *
from time import *
M = [ 1, 0, 0, 0, 1,
      1, 1, 0, 1, 1, 
      1, 0, 1, 0, 1,
      1, 0, 0, 0, 1,
      1, 0, 0, 0, 1 ] 
O = [ 0, 0, 1, 0, 0,
      0, 1, 0, 1, 0, 
      0, 1, 0, 1, 0,
      0, 1, 0, 1, 0,
      0, 0, 1, 0, 0 ] 
I = [ 0, 0, 1, 0, 0,
      0, 0, 1, 0, 0, 
      0, 0, 1, 0, 0,
      0, 0, 1, 0, 0,
      0, 0, 1, 0, 0 ] 
LOVE = [ 0, 1, 0, 1, 0,
         1, 0, 1, 0, 1, 
         1, 0, 0, 0, 1,
         0, 1, 0, 1, 0,
         0, 0, 1, 0, 0 ] 
U = [ 0, 1, 0, 1, 0,
      0, 1, 0, 1, 0, 
      0, 1, 0, 1, 0,
      0, 1, 0, 1, 0,
      0, 1, 1, 1, 0 ] 
for i in range(2):
    color("yellow")
    show(M)
    sleep(1)
    color("green")
    show(O)
    sleep(1)
    color("yellow")
    show(M)
    sleep(1)
    color("blue")
    show(I)
    sleep(1)
    color("red")
    show(LOVE)
    sleep(1)
    color("purple")
    show(U)
    sleep(1)
img("1.jpg")
m()