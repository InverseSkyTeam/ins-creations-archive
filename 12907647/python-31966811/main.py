from math import *
import tkinter as tk
import pygame
import sys
import os

root = tk.Tk()
# root.geometry('1000x800')
root.configure(background='cyan')
root.title('函数图像模拟器')

dot_value = 20
formula = 'y=x'
xlist = []
ylist = []
dotlist = []
add = False
show = False

def setdot():
    global dot_value
    dot_value = int(ConfigEntry.get())
    if (dot_value % 2 == 1) or (not 5<dot_value<30001):
        print('描点个数设置失败，必须是偶数，且5<描点个数<30001')
    else:
        print('描点个数设置成功！')
        ShowLabel['text'] = '帮助\n描点设置格式:输入5<描点个数<30001    |    描点个数:'+str(dot_value)+'\n算式格式:y=算式|如:y=3*x\n目前支持四则运算/大中小括号\n由于技术不成熟，只能输入整数/小数\n而且乘号不得省略，如3x=3*x\n乘=*，除=/，幂=^(如10^3)\n根号下2*8表示成sqrt(2*8)*x'

def calculation():
    global dot_value,formula,xlist,ylist,show,add
    xlist = []
    ylist = []
    new_formula = InputEntry.get() \
              .replace(' ','') \
              .replace('（','(') \
              .replace('）',')') \
              .replace('[','(') \
              .replace(']',')') \
              .replace('{','(') \
              .replace('}',')') \
              .replace('^','**') \
              .split('=')[-1]
    i = 0
    for x in range(int(dot_value/2)):
        i += 0.1
        x = -i
        xlist.append(x)
        y = eval(new_formula.replace('x',str(x)))
        ylist.append(y)
    i = 0
    for x in range(int(dot_value/2)):
        i += 0.1
        x = i
        xlist.append(x)
        y = eval(new_formula.replace('x',str(x)))
        ylist.append(y)
    print('\033[2J\033[100A\033[3J\033[100A'*2)
    # for i in range(len(xlist)):
    #     print('(x,y)坐标描点位置',i+1,'为(',xlist[i],',',ylist[i],')')
    add = True

def save_file():
    global dot_value,formula,xlist,ylist
    print('\033[2J\033[100A\033[3J\033[100A'*2)
    print('保存中，请稍等...')
    with open('../../../../../desktop/二次函数图像分析结果报告-小轩二次函数图像模拟器细节分析器-文档存储-描点个数'+str(dot_value)+'个.txt','w',encoding='utf-8') as f:
        f.write(formula)
        f.write('\n')
        for i in range(len(xlist)):
            f.write('(x,y)坐标描点位置'+str(i+1)+'为('+str(xlist[i])+','+str(ylist[i])+')\n')
    f.close()
    print('保存成功，文档已安全关闭，请在桌面查看！')

ShowLabel = tk.Label(root,text='帮助\n描点设置格式:输入5<描点个数<30001    |    描点个数:20\n算式格式:y=算式|如:y=3*x\n目前支持四则运算/大中小括号\n由于技术不成熟，只能输入整数/小数\n而且乘号不得省略，如3x=3*x\n乘=*，除=/，幂=^(如10^3)\n根号下2*8表示成sqrt(2*8)*x',border=3,font=('楷体',15))
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

SaveButton = tk.Button(root,text='    |保存文件到桌面|    ',border=3,font=('楷体',20),bg='royalblue',command=save_file)
SaveButton.grid(row=3,column=0,columnspan=2)

DrawPaperFrame = tk.Frame(root,width = 700, height = 400)
DrawPaperFrame.grid(row=4,column=0,columnspan=2)

os.environ['SDL_WINDOWID'] = str(DrawPaperFrame.winfo_id())
pygame.init()
screen = pygame.display.set_mode((700,400),pygame.NOFRAME)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255,255,255))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(0,199,700,3),0)
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(349,0,3,400),0)
    if add:
        dotlist = []
        for i in range(len(xlist)):
            dotlist.append(pygame.Rect(xlist[i]+350,-ylist[i]+200,3,3))
        add = False
        show = True
    if show:
        for i in dotlist:
            pygame.draw.rect(screen,(0,255,0),i,0)
    pygame.display.update()
    try:root.update()
    except:sys.exit()