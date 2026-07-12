import tkinter as tk

root = tk.Tk()
root.geometry('800x600')
root.configure(background='cyan')
root.title('函数图像模拟器')

dot_value = 20
formula = 'y=x'
xlist = []
ylist = []

def setdot():
    global dot_value
    dot_value = int(ConfigEntry.get())
    if dot_value % 2 == 1:
        print('描点个数设置失败，必须是偶数')
    else:
        print('描点个数设置成功！')

def calculation():
    global dot_value,formula,xlist,ylist
    xlist = []
    ylist = []
    formula = InputEntry.get() \
              .replace(' ','') \
              .replace('（','(') \
              .replace('）',')') \
              .replace('[','(') \
              .replace(']',')') \
              .replace('{','(') \
              .replace('}',')') \
              .split('=')[-1]
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
    print('\033[2J\033[100A\033[3J\033[100A'*2)
    for i in range(0,len(xlist)):
        print('(x,y)坐标描点位置',i+1,'为(',xlist[i],',',ylist[i],')')

ShowLabel = tk.Label(root,text='帮助\n描点设置格式:输入7<描点个数<15001\n算式格式:y=算式|如:y=3*x\n目前支持四则运算/大中小括号\n由于技术不成熟，只能输入整数/小数\n而且乘号不得省略，如3x=3*x\n乘=*，除=/',border=3,font=('楷体',15))
ShowLabel.grid(row=0,column=0,columnspan=2)

stringvar = tk.StringVar()
stringvar.set('y=x')
stringvar2 = tk.StringVar()
stringvar2.set('20')
ConfigEntry = tk.Entry(root,border=8,bg='#FFEFD5',font=('楷体',20),width=35,textvariable=stringvar2)
ConfigEntry.grid(row=1,column=0)
ConfigButton = tk.Button(root,text='  |描点个数设定|  ',border=3,font=('楷体',20),bg='lightgreen',command=setdot)
ConfigButton.grid(row=1,column=1)

InputEntry = tk.Entry(root,border=8,bg='#FFEFD5',font=('楷体',20),width=35,textvariable=stringvar)
InputEntry.grid(row=2,column=0)
CalculationButton = tk.Button(root,text='  |开始模拟计算|  ',border=3,font=('楷体',20),bg='lightgreen',command=calculation)
CalculationButton.grid(row=2,column=1)

root.mainloop()