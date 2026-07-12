#请你使用for循环语句设计属于自己的徽章logo~
from turtle import *
Screen().bgpic("bg.png")
t = Turtle()
t.shape("turtle")
#设置画笔颜色：white白色、black黑色、red红色、yellow黄色、blue蓝色、orange橘色、green绿色
#修改括号中的单词可以改变画笔颜色哦~
t.color("orange")
t.speed(6)#设置画笔速度
t.width(2)#设置画笔粗细
#1、请你在第13行补充for循环语句
#2、修改for循环下面的语句或数值，设计与众不同的徽章~
for i in range(5):
    t.forward(200)
    t.right(144)
