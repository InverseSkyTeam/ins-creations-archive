from turtle import *
#1、修改两个扇叶的颜色以及风车大小
#2、补充代码，画出第3个扇叶

sc = Screen()
sc.bgpic("windmill.png")
t = Turtle()
t.shape("turtle")
#修改颜色以及风车扇叶大小
t.color("red")
t.begin_fill()
t.circle(100,360,3)
t.end_fill()
t.left(120)

#修改颜色以及风车扇叶大小
t.color("blue")
t.begin_fill()
t.circle(100,360,3)
t.end_fill()
t.left(120)

#在下面补充代码，画出第3个扇叶
t.color("orange")
t.begin_fill()
t.circle(100,360,3)
t.end_fill()
t.left(120)
