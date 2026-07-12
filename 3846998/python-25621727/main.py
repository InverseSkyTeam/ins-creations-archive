sym=["+","-","*","/","%","**","//"]
a=input("请直接输入一个只有一个运算符的算式：")
for i in sym:
    if i in a:
        a=a.split(i)
        a.append(i)
        break
def js(a,b,c):
    return({"+":a+b,"-":a-b,"*":a*b,"/":a/b,"%":a%b,"**":a**b,"//":a//b}[c])
try:
    print("结果是：",js(float(a[0]),float(a[1]),a[2]))
except:
    print("您输入的算式有问题！")