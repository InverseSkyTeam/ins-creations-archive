from turtle import*
hideturtle()
penup()
c=int(input("位置(x坐标)"))
d=int(input("位置(y坐标)"))
goto(c,d)
pendown()
a=int(input("边长"))
b=int(input("边数"))
for i in range(b):
    fd(a)
    rt(360/b)