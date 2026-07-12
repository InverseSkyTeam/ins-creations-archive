def a(n):
    if n == 1:
        return 1
    else:
        return n * a(n-1)
g = int(input("请输入一个正整数："))
result = a(g)
print("%d的阶乘是：%d" % (g,result))