from turtle import *
from random import *


sc = Screen()
sc.bgpic("sea3.png")
sc.register_shape("fish1.png")
sc.register_shape("fish2.png")

sc.register_shape("fish3.png")
sc.register_shape("fish4.png")

x1 = randint(-500,-300)
y1 = randint(-300,300)

x2 = randint(-500,-300)
y2 = randint(-300,300)


t1 = Turtle()
t1.penup()
t1.goto(x1, y1)

t2 = Turtle()
t2.penup()
t2.goto(x2, y2)


for i in range(1000000):
    t1.shape("fish1.png")
    t2.shape("fish3.png")
    
    for i in range(150):
        t1.forward(5)
        t2.forward(5)

        
    t1.right(180)
    t2.right(180)
    
    t1.shape("fish2.png")
    t2.shape("fish4.png")
    

    
    for i in range(150):
        t1.forward(5)
        t2.forward(5)

    t1.right(180) 
    t2.right(180)