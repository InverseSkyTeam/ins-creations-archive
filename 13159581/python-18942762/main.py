from time import *
def a(n,x,y,z):
    if n == 1:
        print(x,"-->",z)
        sleep(0.2)
    else:
        a(n-1,x,z,y)
        sleep(0.02)
        print(x,"-->",z)
        sleep(0.02)
        a(n-1,y,x,z)
        sleep(0.02)
n = int(input("请输入汉诺塔的层数："))
a(n,'X','Y','Z')