from math import*
print("注意，得数会与真正的得数有较大差距")
def near(a,b):
    if b-a<=0.00000001:
        return 1
    else:
        return 0
def a(c):
    b=0
    for i in range(c*1000000000):
        if near(b*b,c)==1:
            print("平方根是：",i/100000000)
            print("与原数的差是：",i*i/10000000000000000-c)
            break
        b=b+0.00000001
d=int(input("请输入一个整数："))
a(d)