#补充第25、26行代码，让选手c不留痕迹地来到合适的起跑位置
#提示:左侧还有天空背景(bg3.png)和其他选手供你选择哦！
from turtle import *
from race import *
from random import *
Screen().bgpic("bg1.png")
as_ = randint(0,100)
a = Turtle()
Screen().register_shape("可多.png")
a.shape("可多.png")
bs = randint(0,100)
b = Turtle()
Screen().register_shape("兰朵.png")
b.shape("兰朵.png")

c = Turtle()
Screen().register_shape("海龟.png")
c.shape("海龟.png")

a.penup()
a.goto(0, 0)
b.penup()
b.goto(0, 60)
#补充下面2行代码，让选手c不留痕迹地来到合适的起跑位置
c.penup()
c.goto(0,120)
cs = randint(0,100)
set_speed(a,as_)
set_speed(b,bs)
set_speed(c,cs)

game_start(a,b,c)

Screen().bgpic("win.png")
game_result()