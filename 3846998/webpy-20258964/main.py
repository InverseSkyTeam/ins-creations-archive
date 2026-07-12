import turtle as t
import time as t2
t.speed(0)
lt=t.left
rt=t.rt
fd=t.forward
def ht(a):
    t.forward(a-a-a)
wi=t.width
d=t.pendown
u=t.penup
g=t.goto
w=10
x=0
y=0
f=1
x_=10
for i in range(10):
    fd(10)
    wi(w)
    w=w+1
u()
g(0,100)
d()
w=50
lt(270)
for i in range(20):
    wi(w)
    fd(10)
    w=w-1
lt(90)
u()
g(-120,-110)
w=20
d()
t.color("white")
for i in range(12):
    fd(10)
    wi(w)
    w=w-1
    t.color("black")
for i in range(12):
    fd(10)
    wi(w)
    w=w+1
t2.sleep(2)
t.clear()
u()
g(-120,120)
d()
w=20
for i in range(12):
    fd(10)
    wi(w)
    w=w-1
for i in range(12):
    fd(10)
    wi(w)
    w=w+1
u()
g(0,120)
lt(270)
d()
w=1
for i in range(20):
    wi(w)
    fd(10)
    w=w+1
u()
g(20,100)
lt(45)
w=0
d()
t.color("white")
for i in range(10):
    wi(w)
    fd(10)
    w=w+2
    t.color("black")