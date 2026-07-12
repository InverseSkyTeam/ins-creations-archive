print("本计算器只支持整数")
while True:
    a=input("请输入运算符号（/除法，*乘法，-减法，+加法，%变百分数，^求平方，0停止）")
    if a == "/":
        b=int(input("请输入被除数："))
        c=int(input("请输入除数："))
        print("结果是：",b/c)
    if a == "*":
        d=int(input("请输入因数："))
        e=int(input("请输入因数："))
        print("结果是：",d*e)
    if a == "-":
        f=int(input("请输入被减数："))
        g=int(input("请输入减数："))
        print("结果是：",f-g)
    if a == "+":
        h=int(input("请输入加数："))
        i=int(input("请输入加数："))
        print("结果是：",h+i)
    if a == "%":
        j=int(input("请输入要变百分数的数："))
        print("结果是：",(j*100),"%")
    if a == "^":
        k=int(input("请输入要变成平方数的数："))
        print("结果是：",k*k)
    if a == "0":
        break
    else:
        print("请输入正确的运算符号")