print("我只是一个六年级小学生，不知道这个程序做得对不对")

formula = input('目前支持函数图像：y=一个式子,只能含四则运算、括号和x，不能省略乘号，如2*(x+1)则输出y=2*(x+1)的图像\n英文输入法下输入对应图像开始计算')
dot_value = int(input('输入需要计算几个描点位置？（输入10-10000的任意数字即可，最好是偶数，其他则会不准）'))
xlist = []
ylist = []

for i in range(1,int(dot_value/2+1)):
    x = -i
    xlist.append(x)
    y = eval(formula.replace('x',str(x)))
    ylist.append(y)
for i in range(1,int(dot_value/2+1)):
    x = i
    xlist.append(x)
    y = eval(formula.replace('x',str(x)))
    ylist.append(y)

for i in range(0,len(xlist)):
    print('(x,y)坐标描点位置',i+1,'为(',xlist[i],',',ylist[i],')')