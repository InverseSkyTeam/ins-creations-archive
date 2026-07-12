from time import*
print("本系统运行流程图如下：")
print("↗------→命令发出←---------↖")
print("|          ||              |")
print("|         _||_             |")
print("|         \  /             |")
print("|          \/      是      |")  
print("|         驳回？----------↗   ")
print("|          ||")
print("|         _||_否")
print("|         \  /")
print("|          \/")
print("↖------命令执行(计算)")
sleep(5)
from random import*
def fc():
    a=randint(1,4)
    b=randint(1,10)
    c=randint(1,10)
    print("命令已发出")
    return(a,b,c)
def bh():
    if randint(0,9)==0:
        print("命令被驳回")
        return(0)
    else:
        print("命令已被接受")
        return(1)
def zx():
    bh()
def czx(a,b,c):
    print("命令正在执行")
    if a==1:
        print(a,"乘",b,"=",a*b)
    elif a==2:
        print(a,"除",b,"=",a/b)
    elif a==3:
        print(a,"加",b,"=",a+b)
    elif a==4:
        print(a,"减",b,"=",a-b)
while 1:
    a,b,c=fc()
    d=bh()
    if d==0:
        continue
    zx()
    czx(a,b,c)