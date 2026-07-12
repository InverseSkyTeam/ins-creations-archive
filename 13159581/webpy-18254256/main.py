#选择右侧图片中的任意一张，进行创作
from turtle import *
from random import *

#(1)选择一张图片。小狗："dog.jpg"  T恤："T-shirt.jpg"
Screen().bgpic("dog.jpg")

t = Turtle()
t.shape("circle")
t.speed(0)

#(2)补充完整for循环，设置点的数量
for i in range(50):
    #下列3行代码中，括号内数字可以修改，从而获得其他颜色
    a = randint(0,255) 
    b = randint(0,255)
    c = randint(0,255)
    t.color(a,b,c)
    
    t.penup()
    
    x = randint(-100,100) #修改横坐标，让画出的点不超出范围
    y = randint(-100,10) #修改竖坐标，让画出的点不超出范围
    #(3)移动到随机位置
    t.goto(x,y)
    
    r = randint(1,20)
    #(4)画出随机大小的点
    t.dot(r)
