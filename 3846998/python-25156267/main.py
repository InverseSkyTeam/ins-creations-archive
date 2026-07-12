print("计算两点之间的距离")
def jl(a,b):
    try:
        x1,y1=a
        x2,y2=b
        return(((x1-x2)**2+(y1-y2)**2)**0.5)
    except:
        return("错误！")
try:
    print("点1到点2的距离是：",jl(eval(input("请输入点1的坐标（格式是x,y）：")),eval(input("请输入点2的坐标："))))
except:
    pass