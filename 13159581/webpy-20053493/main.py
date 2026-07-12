from turtle import *
from random import *
t = Turtle()
t.speed(0)

Screen().bgpic("L1V1/18a.png")

colorList = ["lightgreen", "forestgreen", "limegreen", "darkgreen", "green", "lime"]
for i in range(200):
    t.penup()
    x = randint(-400, 400)
    y = randint(-200, 0)
    t.goto(x, y)
    t.pendown()
    col = choice(colorList)
    t.color(col)
    t.begin_fill()
    t.circle(y/5)
    t.end_fill()

colorList=["deeppink","hotpink","crimson","pink","lightpink"]
for i in range(50):
    t.penup()
    x = randint(-400, 400)
    y = randint(-200, -50)
    t.goto(x, y)
    t.pendown()
    col = choice(colorList)
    t.color(col)
    #请添加代码，绘制荷花（正八边形）
    t.begin_fill()
    t.circle(25,360,8)
    t.end_fill()
#为你的创作命名
t.penup()
t.goto(-250,250)
t.color("black")
t.pendown()
t.write("陈锦奕的荷塘月色", font=["黑体",40, "normal"])
