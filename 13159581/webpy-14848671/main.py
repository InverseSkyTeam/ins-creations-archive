#小极客，你有玩过游乐场的大摆锤项目嘛
#快来发挥你的编程技能，为自己设计一个吧~
from turtle import *
#请你补充第48行的代码，让大摆锤动起来吧~
sc = Screen()
sc.bgpic("windmill.png")
t = Turtle()
t.tracer(0)

for i in range(100000):
    t.clear()
    
    t.color("green")
    t.begin_fill()
    t.circle(120,180,3)
    t.end_fill()
    t.left(120)
    
    t.color("blue")
    t.begin_fill()
    t.circle(120,180,3)
    t.end_fill()
    t.left(120)
    
    t.color("purple")
    t.begin_fill()
    t.circle(120,180,3)
    t.end_fill()
    t.left(120)
    
    t.color("green")
    t.begin_fill()
    t.circle(120,180,3)
    t.end_fill()
    t.left(120)
    
    t.color("blue")
    t.begin_fill()
    t.circle(120,180,3)
    t.end_fill()
    t.left(120)
    
    t.color("purple")
    t.begin_fill()
    t.circle(120,180,3)
    t.end_fill()
    t.left(120)
 #在括号中补充旋转角度数，看看效果吧~   
    t.left(5)
    t.update()