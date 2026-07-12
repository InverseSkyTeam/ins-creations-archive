#帮助小海龟收集宝石走到终点

from turtle import *

#请从bg1.png,bg2.png,bg3.png中选择一个地图
Screen().bgpic("bg2.png")

t = Turtle()
t.shape("turtle")
#请你帮助小海龟前进、左转、右转吧~
t.left(90)
t.forward(140)
t.right(90)
t.forward(65)
t.right(90)
t.forward(55)
t.left(90)
t.forward(80)
t.left(90)
t.forward(55)
t.right(90)
t.forward(130)
t.right(360)
t.left(360)
print(" __________________________")
print("|  0000000000000000000000  |")
print("|  00      礼物         00 |")
print("|  0000000000000000000000  |")
print(" __________________________")