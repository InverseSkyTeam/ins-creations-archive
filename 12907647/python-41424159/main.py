from turtle import *
speed(0)
# 内角和=(x-2)*180/x
# 则内角=180-360/x
# 则外角=360/x

print('绘制正x边形\n输入x:')
x = float(input())
if -1 <= x <= 1:
    raise SystemExit('此时这个图形的面积为无穷大，无法绘制')
print('请注意任务栏是否弹出窗口')
alpha = 360 / x

if int(x) == x:
    length = 500/x
else:
    length = 200

did = 0
while (distance(0,0) > 0.001) or (not did):   # 回到原点
    did = 1
    forward(length)
    right(alpha)

print('完成正',x,'变形的绘制')
done()