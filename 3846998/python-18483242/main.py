from random import*
a=[[],[],[],[]]
e=1
f=1
h=1
def kdg(e,h):
    if h==1:
        for i in range(4):
            for j in range(6):
                c=randint(1,2)
                if c==1:
                    if e==1:
                        print("有",end=" ")
                        a[i].append(randint(100000,999999))
                else:
                    print("无",end=" ")
                    a[i].append(0)
            print()
    else:
        for i in range(4):
            for j in range(6):
                if a[i][j]!=0:
                    print("有",end=" ")
                else:
                    print("无",end=" ")
            print()
kdg(e,h)
h=h+1
f=f+1
while 1:    
    f=input("取件(1)还是寄件(2):")
    if f=="取件" or f=="1":
        b=int(input("快递位置(行):"))
        c=int(input("快递位置(列):"))
        if a[b-1][c-1]==0:
            print("这个位置没有快递")
        else:
            print("取件码是:",a[b-1][c-1])
            if int(input("取件码:"))==a[b-1][c-1]:
                print("取件码正确")
                a[b-1][c-1]=0
            else:
                print("取件码错误")
    elif f=="寄件" or f=="2":
        b=int(input("快递位置(行):"))
        c=int(input("快递位置(列):"))
        if a[b-1][c-1]!=0:
            print("这个位置已经有快递了")
        else:
            g=int(input("六位取件码是:"))
            a[b-1][c-1]=g
    else:
        break
    kdg(e,h)