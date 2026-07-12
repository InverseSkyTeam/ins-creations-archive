print("本算法按本次弹跳为上次的1/2计算，并只支持整数")
n=int(input("请输入高度："))
b=int(input("请输入反弹次数："))
s=0
for i in range(b):
    s=s+n+n/2
    n=n/2
print("最后一次弹跳高度是：",str(n))
print("轨迹总长是：",str(s+n))