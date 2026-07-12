from xes.map import *
start = input("起点：")
end = input("终点：")
a = get_routes(start, end)
len1 = len(a)
for i in range(len1):
    print(i, "：",a[i])
num = input("请选择要搭乘的路线：")
b = get_sites(a,num)
print(b)