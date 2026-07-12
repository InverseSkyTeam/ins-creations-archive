from turtle import *
from time import *
shape('turtle')

def hst():          # 反复隐藏、显示海龟
    for i in range(3):
        sleep(0.5)
        ht()
        sleep(0.5)
        st()
    sleep(0.5)
    ht()

def circle66p():   # 画三分之二（66.6666%）的圆
    for i in range(100):
        right(2)
        forward(2)

def love():
    begin_fill()
    lt(140)
    forward(111.65)
    circle66p()
    lt(120)
    circle66p()
    goto(0,0)
    end_fill()
    lt(140)

def lovebox():
    up();goto(-100,-100);down()
    begin_fill()
    pensize(10)
    forward(240);rt(90)
    forward(80);rt(90)
    forward(240);rt(90)
    forward(80);rt(90)
    end_fill()
    up();goto(-50,-130);down()
    color('black','black')
    write('母亲节快乐！',font=['黑体',15,'normal'])
    up();goto(-80,-150);down()
    write('Happy Mother\'s Day!!!',font=['黑体',15,'normal'])
    st()
    pensize(50);sleep(1)
    up();goto(0,0);down();sleep(1)
    pensize(5)
    ht()

hst()
speed(0);color('red','pink')
love()
sleep(1)
lovebox()
up()
goto(-100,-300)
write('给个小赞！',font=['黑体',20,'normal'])
down()

















