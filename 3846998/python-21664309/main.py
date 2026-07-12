def js(a,b,c):
    return("结果是："+str({1:a+b,2:a-b,3:a*b,4:a/b,5:a//b,6:a**b,7:a%b}[c]))
print(js(int(input("请输入第一个数：")),int(input("请输入第二个数：")),int(input("请输入运算法则(1加2减3乘4除5整除6乘方7取余)："))))