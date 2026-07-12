from turtle import*
from time import*
t=Turtle()
t.speed(0)
t.hideturtle()
def c(a,b,c,d,e):
    if e==1:
        t.goto(c,d)
        t.pendown()
        t.begin_fill()
        for i in range(a):
            t.fd(b)
            t.left(360/a)
        t.end_fill()
    elif e==0:
        t.goto(c,d)
        t.pendown()
        for i in range(a):
            t.fd(b)
            t.left(360/a)
a=200
for i in range(200):
    c(3,a,0,0,0)
    t.left(a)
    a=a-1
sleep(5)
t.clear()
a=200
for i in range(200):
    c(3,a,0,0,0)
    t.left(18)
    a=a-1