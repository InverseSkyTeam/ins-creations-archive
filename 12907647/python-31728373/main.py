print("我只是一个六年级小学生，不知道这个程序做得对不对")

numc = int(input('目前支持函数图像：(1)y=2x   (2)y=0.5x   (3)y=x (垃圾玩意儿)输入对应图像序号开始计算'))
xlist = []
ylist = []

if numc == 1:
    for i in range(1,int(10/2+1)):
        x = -i
        xlist.append(x)
        y = 2*x
        ylist.append(y)
    for i in range(1,int(10/2+1)):
        x = i
        xlist.append(x)
        y = 2*x
        ylist.append(y)
    

if numc == 2:
    for i in range(1,int(10/2+1)):
        x = -i
        xlist.append(x)
        y = 0.5*x
        ylist.append(y)
    for i in range(1,int(10/2+1)):
        x = i
        xlist.append(x)
        y = 0.5*x
        ylist.append(y)
    

if numc == 3:
    for i in range(1,int(10/2+1)):
        x = -i
        xlist.append(x)
        y = x
        ylist.append(y)
    for i in range(1,int(10/2+1)):
        x = i
        xlist.append(x)
        y = x
        ylist.append(y)
    

for i in range(len(xlist)):
    print('(x,y)坐标描点位置',i,'为(',xlist[i],',',ylist[i],')')