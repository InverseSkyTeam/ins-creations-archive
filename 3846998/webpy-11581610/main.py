from turtle import*
from random import*
while True:
    a=randint(-300,300)
    b=randint(-300,300)
    t=Turtle()
    t.penup()
    t.speed(0)
    t.goto(a,b)
    t.dot(50)
    print(a,b)