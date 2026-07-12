a=int(input("输入数的个数："))
c=0
4
for i in range(1,a+1):
    b=int(input("第"+str(i)+"个数："))
    if b>c:
        c=b
print("最大的数是：",c)