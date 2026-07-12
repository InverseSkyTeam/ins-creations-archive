from turtle import*
hideturtle()
a=int(input("边长"))
b=int(input("边数"))
for i in range(b):
    fd(a)
    rt(360/b)