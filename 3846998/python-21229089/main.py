def yf(a,b):
    for i in range(2,a*b):
        while a%i==0 and b%i==0:
            a=a/i
            b=b/i
    return(a,b)
def tf(a,b):
    a1=a[0]
    a2=a[1]
    a=(a1,a2)
    a1,a2=a
    b1,b2=b
    a_1,a_2=a
    b_1,b_2=b
    a1=a1*b2
    a2=a2*b2
    b1=b1*a_2
    b2=b2*a_2
    return((a1,a2),(b1,b2))
def fssum(a,b):
    a,b=tf(a,b)
    return(a[0]+b[0],b[1])
def fsjf(a,b):
    a,b=tf(a,b)
    return(a[0]-b[0],b[1])
def fstime(a,b):
    return(a[0]*b[0],a[1]*b[1])
def fscf(a,b):
    return(a[0]*b[1],a[1]*b[0])
fslist=[]
while 1:
    print("0、停止程序\n1、创建一个分数\n2、分数计算（必须使用fslist里的分数）\n3、分数约分")
    a=int(input("请选择（输入序号）："))
    if a==1:
        b=int(input("请输入分子："))
        c=int(input("请输入分母："))
        if c!=0:
            fslist.append([b,c])
            print("您创建的分数已经存储在fslist，序号是：",len(fslist)-1)
        else:
            print("分母不能是0")
    if a==0:
        break
    if a==2 and len(fslist)>=2:
        print("分数列表如下：",fslist)
        print("1、加法\n2、减法\n3、乘法\n4、除法")
        a=int(input("请选择（输入序号）："))
        if a==1:
            b=int(input("请输入加数1（序号）："))
            c=int(input("请输入加数2（序号）："))
            d=[fssum(fslist[b],fslist[c])[0],fssum(fslist[b],fslist[c])[1]]
            fslist.append(d)
            print("结果是：",d,"，已存储在fslist，序号是：",len(fslist)-1)
        if a==2:
            b=int(input("请输入被减数（序号）："))
            c=int(input("请输入减数（序号）："))
            d=[fsjf(fslist[b],fslist[c])[0],fsjf(fslist[b],fslist[c])[1]]
            fslist.append(d)
            print("结果是：",d,"，已存储在fslist，序号是：",len(fslist)-1)
        if a==3:
            b=int(input("请输入乘数1（序号）："))
            c=int(input("请输入乘数2（序号）："))
            d=[fstime(fslist[b],fslist[c])[0],fstime(fslist[b],fslist[c])[1]]
            fslist.append(d)
            print("结果是：",d,"，已存储在fslist，序号是：",len(fslist)-1)
        if a==4:
            b=int(input("请输入被除数（序号）："))
            c=int(input("请输入除数（序号）："))
            d=[fscf(fslist[b],fslist[c])[0],fscf(fslist[b],fslist[c])[1]]
            fslist.append(d)
            print("结果是：",d,"，已存储在fslist，序号是：",len(fslist)-1)
    if a==2 and len(fslist)<2:
        print("fslist的项数不足两项，请继续创建分数")
        continue
    if a==3:
        b=int(input("请输入需要约分的分数（序号）"))
        c=yf(fslist[b][0],fslist[b][1])
        fslist[b]=[c[0],c[1]]
        print("结果是：",fslist[b],"，已经自动替换原分数")
    if a==3 and len(fslist)<1:
        print("fslist中没有分数，请继续创建")