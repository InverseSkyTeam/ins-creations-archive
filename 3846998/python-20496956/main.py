print('计算器，支持小数')
def js(a,b,c):
    if a==1:
        return(b+c)
    elif a==2:
        return(b-c)
    elif a==3:
        return(b*c)
    elif a==4:
        return(b/c)
    elif a==5:
        return(b//c)
    elif a==6:
        return(b**c)
    elif a==7:
        return(b%c)
    elif a==8:
        return(b**0.5)
while 1:
    a=int(input('请输入要计算的类型，停止计算0，加法1，减法2，乘法3，除法4，整除5，乘方6，取余7，开平方8：'))
    if a==0:
        break
    if a==1:
        print('结果是：',js(a,float(input('加数：')),float(input("加数："))))
    if a==2:
        print('结果是：',js(a,float(input('被减数：')),float(input("减数："))))
    if a==3:
        print('结果是：',js(a,float(input('因数')),float(input("因数："))))
    if a==4:
        try:
            print('结果是：',js(a,float(input('被除数：')),float(input("除数："))))
        except:
            print("除数不能是0")
    if a==5:
        try:
            print('结果是：',js(a,float(input('被除数：')),float(input("除数："))))
        except:
            print("除数不能是0")
    if a==6:
        print('结果是：',js(a,float(input('底数：')),float(input("指数："))))
    if a==7:
        try:
            print('结果是：',js(a,float(input('被除数：')),float(input("除数："))))
        except:
            print("除数不能是0")
    if a==8:
        print('结果是：',js(a,float(input('要开平方的数：')),0))