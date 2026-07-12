#补充完整第8行、第37行代码，制作果汁/蛋糕/冰棍吧！
from turtle import *
from food import *

#补充完整第8行代码，定义多参函数。
#函数名：juicer
#作答区域。
def juicer(f1,f2):
    s1 = get(f1,"酸")
    s2 = get(f2,"酸")
    s = s1 + s2
    #{
    t1 = get(f1,"甜")
    t2 = get(f2,"甜")
    t = t1 + t2

    k1 = get(f1,"苦")
    k2 = get(f2,"苦")
    k = k1 + k2

    l1 = get(f1,"辣")
    l2 = get(f2,"辣")
    l = l1 + l2

    x1 = get(f1,"咸")
    x2 = get(f2,"咸")
    x = x1 + x2
    #}
    num = s  + t  - k -  l - x

    print("果汁的美味系数：")
    print(num)
    
    #补充完整第37行代码，设置函数返回值num。
    #作答区域。
    return num

#榨果汁
Screen().setup(1200,900)
Screen().bgpic("01.jpg")
t = Turtle()
# t.speed(0)

show_foods()

#第1杯果汁
food1 = input("添加食物1：")
food2 = input("添加食物2：")

j1 = juicer(food1,food2)

if j1 > -100:
    print("倒入杯子，喝掉果汁")
    t.penup()
    t.goto(-40,-250)
    t.pendown()
    c1 = juice_color(j1)
    t.color(c1)
    t.begin_fill()
    for i in range(4):
        t.forward(85)
        t.right(90)
    t.end_fill()
else:
    print("不喝果汁")

show_foods()

#第2杯果汁
food3 = input("添加食物3：")
food4 = input("添加食物4：")

j2 = juicer(food3,food4)

if j2 > -10:
    print("倒入杯子，喝掉果汁")
    t.penup()
    t.goto(75,-250)
    t.pendown()
    c2 = juice_color(j2)
    t.color(c2)
    t.begin_fill()
    for i in range(4):
        t.forward(85)
        t.right(90)
    t.end_fill()
else:
    print("不喝果汁")

show_foods()

#第3杯果汁
food5 = input("添加食物5：")
food6 = input("添加食物6：")

j3 = juicer(food5,food6)

if j3 > -5:
    print("倒入杯子，喝掉果汁")
    t.penup()
    t.goto(195,-250)
    t.pendown()
    c3 = juice_color(j3)
    t.color(c3)
    t.begin_fill()
    for i in range(4):
        t.forward(85)
        t.right(90)
    t.end_fill()
else:
    print("不喝果汁")

show_foods()

#第4杯果汁
food7 = input("添加食物7：")
food8 = input("添加食物8：")

j4 = juicer(food7,food8)

if j4 > 0:
    print("倒入杯子，喝掉果汁")
    t.penup()
    t.goto(315,-250)
    t.pendown()
    c4 = juice_color(j4)
    t.color(c4)
    t.begin_fill()
    for i in range(4):
        t.forward(85)
        t.right(90)
    t.end_fill()
else:
    print("不喝果汁")

show_foods()

#第5杯果汁
food9 = input("添加食物9：")
food10 = input("添加食物10：")

j5 = juicer(food9,food10)

if j5 > 10:
    print("倒入杯子，喝掉果汁")
    t.penup()
    t.goto(435,-250)
    t.pendown()
    c5 = juice_color(j5)
    t.color(c5)
    t.begin_fill()
    for i in range(4):
        t.forward(85)
        t.right(90)
    t.end_fill()
else:
    print("不喝果汁")

# #制作蛋糕
# Screen().setup(1200,900)  
# Screen().bgpic("02.jpg")
# t = Turtle()
# t.speed(0)

# show_foods()

# #第一层蛋糕
# food1 = input("添加食物1：")
# food2 = input("添加食物2：")

# j1 = juicer(food1,food2)

# if j1 > -100:
#     print("第一层蛋糕制作成功")
#     t.penup()
#     t.goto(-142,-205)
#     t.pendown()
#     c1 = juice_color(j1)
#     t.color(c1)
#     t.begin_fill()
#     for i in range(2):
#         t.forward(230)
#         t.right(90)
#         t.forward(28)
#         t.right(90)
#     t.end_fill()
# else:
#     print("第一层蛋糕制作失败")

# show_foods()

# #第二层蛋糕
# food3 = input("添加食物3：")
# food4 = input("添加食物4：")

# j2 = juicer(food3,food4)

# if j2 > -10:
#     print("第二层蛋糕制作成功")
#     t.penup()
#     t.goto(-142,-177)
#     t.pendown()
#     c2 = juice_color(j2)
#     t.color(c2)
#     t.begin_fill()
#     for i in range(2):
#         t.forward(230)
#         t.right(90)
#         t.forward(28)
#         t.right(90)
#     t.end_fill()
# else:
#     print("第二层蛋糕制作失败")

# show_foods()

# #第三层蛋糕
# food5 = input("添加食物5：")
# food6 = input("添加食物6：")

# j3 = juicer(food5,food6)

# if j3 > -10:
#     print("第三层蛋糕制作成功")
#     t.penup()
#     t.goto(-142,-146)
#     t.pendown()
#     c3 = juice_color(j3)
#     t.color(c3)
#     t.begin_fill()
#     for i in range(2):
#         t.forward(230)
#         t.right(90)
#         t.forward(31)
#         t.right(90)
#     t.end_fill()
# else:
#     print("第三层蛋糕制作失败")

# #卡普喝果汁
# Screen().setup(1200,900)  
# Screen().bgpic("03.jpg")
# t = Turtle()
# t.speed(0)

# show_foods()

# #给卡普倒果汁
# food1 = input("添加食物1：")
# food2 = input("添加食物2：")

# j1 = juicer(food1,food2)

# if j1 > -100:
#     print("卡普说超级好喝")
#     t.penup()
#     t.goto(-285,-175)
#     t.pendown()
#     c1 = juice_color(j1)
#     t.color(c1)
#     t.begin_fill()
#     for i in range(4):
#         t.forward(48)
#         t.right(90)
#     t.end_fill()
# else:
#     print("卡普难喝哭了")


# #制作冰棍
# Screen().setup(1200,900)  
# Screen().bgpic("04.jpg")
# t = Turtle()
# t.speed(0)

# show_foods()

# food1 = input("添加食物1：")
# food2 = input("添加食物2：")

# j1 = juicer(food1,food2)

# if j1 > -100:
#     print("可多说超级好吃")
#     t.penup()
#     t.goto(115,60)
#     t.pendown()
#     c1 = juice_color(j1)
#     t.color(c1)
#     t.begin_fill()
#     for i in range(4):
#         t.forward(50)
#         t.right(90)
#     t.end_fill()
# else:
#     print("可多难吃哭了")