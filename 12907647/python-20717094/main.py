'''
方便改编王们看
魔力钟表1.0      作者：小轩

1更----------------------------
V1.0
尺寸：a=长 b=宽
时针 a=180 b=3
分针 a=230 b=2
秒针 a=300 b=1
数字，math库
钟面 660*660
电子荧屏

2更----------------------------
V1.1
pygame,tk,os绑定
温度计，风速计，城市天气检测
'''
import pygame,sys,math,os
import tkinter as tk
from tkinter import *
from time import *
from pyfile.weather import *

temp1 = temp2 = temp3 = temp4 = temp5 = temp6 = temp7 = temp8 = temp9 = temp10 = '天气未知，请先输入城市名'
speed1 = speed2 = speed3 = speed4 = speed5 = speed6 = speed7 = speed8 = speed9 = speed10 = ''

root = tk.Tk()
root.title("魔力钟表")
# root.geometry('300x300')
pgw = tk.Frame(root,width = 1200, height = 700)
pgw.pack()
tkw = tk.Frame(root,width = 100, height = 100)
tkw.place(x=700,y=181)
os.environ['SDL_WINDOWID'] = str(pgw.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'
entry = tk.Entry(tkw,font=('楷体',25))
entry.pack()
def bc():
    global temp1,temp2,temp3,temp4,temp5,temp6,temp7,temp8,temp9,temp10,speed1,speed2,speed3,speed4,speed5,speed6,speed7,speed8,speed9,speed10
    tempdict = temp_get(entry.get())
    speedict = speed_get(entry.get())    # 介于连读原因，我把speed和dict的d融合了！
    temp1 = tempdict[1]
    temp2 = tempdict[2]
    temp3 = tempdict[3]
    temp4 = tempdict[4]
    temp5 = tempdict[5]
    temp6 = tempdict[6]
    temp7 = tempdict[7]
    temp8 = tempdict[8]
    temp9 = tempdict[9]
    temp10 = tempdict[10]
    speed1 = speedict[1]
    speed2 = speedict[2]
    speed3 = speedict[3]
    speed4 = speedict[4]
    speed5 = speedict[5]
    speed6 = speedict[6]
    speed7 = speedict[7]
    speed8 = speedict[8]
    speed9 = speedict[9]
    speed10 = speedict[10]
    
button = tk.Button(tkw,text='查询天气(点完请稍等)',font=('楷体',25),command=bc)
button.pack()




# pygame start‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍
pygame.init()
screen = pygame.display.set_mode((1200, 700))

si = pygame.image.load('image/秒针.png')
mi = pygame.image.load('image/分针.png')
hi = pygame.image.load('image/时针.png')
myclock = pygame.image.load('image/钟面.png')

slist = [pygame.transform.rotate(si,-i*6) for i in range(60)]
mlist = [pygame.transform.rotate(mi,-i*6) for i in range(60)]
hlist = [pygame.transform.rotate(hi,-i*30) for i in range(13)]

# 识别我们系统的字体~Mac优先，win随后（我更喜欢win，但是代码顺序只能这样。。。）
try:import ntpath
except:font = pygame.font.SysFont('kaittf', 30)
else:font = pygame.font.SysFont('kaiti', 30);del ntpath
def show_text(text,color=(0,0,0),pos=(0,0)):
    screen.blit(font.render((text),True,color),pos)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((100,255,255))
    nowh = localtime()[3]
    if nowh > 12:
        nowh -= 12
    nowm = localtime()[4]
    if nowm >= 10:
        nowm2 = str(nowm)
    else:
        nowm2 = '0'+str(nowm)
    nows = localtime()[5]
    if nows >= 10:
        nows2 = str(nows)
    else:
        nows2 = '0'+str(nows)
    wday = localtime()[6]
    if wday == 0:
        weekday = '星期一'
    elif wday == 1:
        weekday = '星期二'
    elif wday == 2:
        weekday = '星期三'
    elif wday == 3:
        weekday = '星期四'
    elif wday == 4:
        weekday = '星期五'
    elif wday == 5:
        weekday = '星期六'
    elif wday == 6:
        weekday = '星期日'
    else:
        weekday = '未知星期，请反馈作者'
    
    hrect = hlist[nowh].get_rect()
    mrect = mlist[nowm].get_rect()
    srect = slist[nows].get_rect()
    hrect.center = (350,350)
    mrect.center = (350,350)
    srect.center = (350,350)
    screen.blit(myclock,(20,20))
    screen.blit(hlist[nowh],hrect)
    screen.blit(mlist[nowm],mrect)
    screen.blit(slist[nows],srect)
    
    for i in range(1,13):
        angle = math.radians(30 * i - 90)
        x = math.cos(angle) * 310 - 10
        y = math.sin(angle) * 310 - 10
        show_text(str(i),pos=(350+x,350+y))
    show_text(str(localtime()[0])+'-'+str(localtime()[1])+'-'+str(localtime()[2])+' '+str(localtime()[3])+':'+nowm2+':'+nows2,color=(255,15,255),pos=(700,21))
    show_text(weekday+'   ▼东八区标准时间',color=(255,15,255),pos=(700,51))
    show_text('在下面输入你所在市（城市、县、区）',pos=(700,111))
    show_text('的名字,如:上海、北京,得到天气情况',pos=(700,141))
    for i in range(1,11):
        exec('show_text(temp'+str(i)+',pos=(700,'+str(251+i*30)+'))')
        exec('show_text(speed'+str(i)+',pos=(900,'+str(251+i*30)+'))')
    show_text('注：可以输入外国的城市，如：巴黎',color=(155,155,0),pos=(700,581))
    show_text('华盛顿，可以用英文或拼音',color=(155,155,0),pos=(700,611))
    show_text('可以检测10天内的温度',color=(155,155,0),pos=(700,641))
    pygame.display.update()
    try:
        root.update()
    except:
        sys.exit()
# pygame end‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍





while True:
    pygame.display.update()
    root.update()