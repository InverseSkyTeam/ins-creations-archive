from turtle import *
#1、补充for循环语句
#2、补充清空语句，实现清除的功能
#3、尝试修改风车旋转速度
sc = Screen()
sc.bgpic("windmill.png")
t = Turtle()
t.tracer(0)

#补充下一行的for循环语句，不要忘记冒号哦
for i in range(10000): 
#在下一行补充清空语句
    t.clear()
    
    #第一个扇叶
    t.color("orange")
    t.begin_fill()
    t.circle(100,360,3)
    t.end_fill()
    t.left(90)
    #第二个扇叶
    t.color("green")
    t.begin_fill()
    t.circle(100,360,3)
    t.end_fill()
    t.left(90)
    #第三个扇叶
    t.color("blue")
    t.begin_fill()
    t.circle(100,360,3)
    t.end_fill()
    t.left(90)
    t.color("yellow")
    t.begin_fill()
    t.circle(100,360,3)
    t.end_fill()
    t.left(90)
    
    #尝试修改风车速度
    t.left(10)
    sc.update()