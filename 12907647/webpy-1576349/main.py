from turtle import *
from time import *
from random import *
shape('turtle')
penup()
goto(-110,-125)
pendown()
speed(7)
color("blue")
begin_fill()
forward(210)
speed(10)
right(65)
forward(190)
left(360-115)
forward(370)
speed(10)
right(360-65+360/2)
forward(190)
end_fill()
penup()
goto(0,-225)
pendown()
color("green")
dot(60)
penup()
goto(-10,-225)
color("white")
pendown()
write('1',font = ['微软雅黑',25,'normal'])
penup()
goto(-20,-130)
color("yellow")
begin_fill()
left(360-65+360/2+90*3)
pendown()
forward(200)
right(90)
forward(35)
right(90)
forward(200)
end_fill()
sleep(1.85)
clear()
print("闪烁灯")
write('闪烁灯',font = ['微软雅黑',40,'normal'])
h = ['red','blue','green','yellow','brown','glue','black','orange']
for a in range(25):
    penup()
    goto(0,180)
    color(choice(list(h)))
    pendown()
    dot(158)
    sleep(1.01999999990987575754524105463)
    clear()
    sleep(0.4)










