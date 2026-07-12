import time,sys
import webbrowser as wb
def ooO00OOoOo__():
    num=44231247#作品的pid
    num=int(num)
    try:
        OOooOo0Oo0=open(eval("b'\\x61\\x73\\x73\\x65\\x74'").decode()+'_info.json','r')#读取asset_info.json的内容
        OOooOo00o0=OOooOo0Oo0.read()
        OOooOo0Oo0.close()
        if int(OOooOo00o0[OOooOo00o0.find('"id":')+6:][:OOooOo00o0[OOooOo00o0.find('"id":')+6:].find(",")])!=num:#通过许多奇技淫巧代替re进行分析
            return int(OOooOo00o0)#如果是盗的作品，把输出函数改为一个错值，让程序报错，从而进入下面的excpet
        return sys.stdout#如果是原作，正常输出
    except:
        #输出提示信息
        print(chr(26816)+chr(27979)+chr(21040)+chr(36825)+chr(20010)+chr(20316)+chr(21697)+chr(26159)+chr(30423)+chr(21462)+chr(20182)+chr(20154)+chr(30340)+chr(20316)+chr(21697)+chr(65292)+chr(35831)+chr(21040)+chr(21407)+chr(20316)+chr(32773)+chr(32593)+chr(31449)+chr(19978)+chr(36816)+chr(34892))
        print(chr(51)+chr(31186)+chr(21518)+chr(33258)+chr(21160)+chr(36339)+chr(36716)+chr(33267)+chr(21407)+chr(20316)+chr(32773)+chr(32593)+chr(31449))
        time.sleep(2)
        #打开原作者网站
        wb.open(chr(104)+chr(116)+chr(116)+chr(112)+chr(115)+chr(58)+chr(47)+chr(47)+chr(99)+chr(111)+chr(100)+chr(101)+chr(46)+chr(120)+chr(117)+chr(101)+chr(101)+chr(114)+chr(115)+chr(105)+chr(46)+chr(99)+chr(111)+chr(109)+chr(47)+chr(104)+chr(111)+chr(109)+chr(101)+chr(47)+chr(112)+chr(114)+chr(111)+chr(106)+chr(101)+chr(99)+chr(116)+chr(47)+chr(100)+chr(101)+chr(116)+chr(97)+chr(105)+chr(108)+chr(63)+chr(108)+chr(97)+chr(110)+chr(103)+chr(61)+chr(99)+chr(111)+chr(100)+chr(101)+chr(38)+chr(112)+chr(105)+chr(100)+chr(61)+str(int(num))+chr(38)+chr(118)+chr(101)+chr(114)+chr(115)+chr(105)+chr(111)+chr(110)+chr(61)+chr(111)+chr(102)+chr(102)+chr(108)+chr(105)+chr(110)+chr(101)+chr(38)+chr(102)+chr(111)+chr(114)+chr(109)+chr(61)+chr(112)+chr(121)+chr(116)+chr(104)+chr(111)+chr(110)+chr(38)+chr(108)+chr(97)+chr(110)+chr(103)+chr(84)+chr(121)+chr(112)+chr(101)+chr(61)+chr(112)+chr(121)+chr(116)+chr(104)+chr(111)+chr(110))
        return sys.exit()

sys.stdout=ooO00OOoOo__()
print('',end='')

#现已将@范炜轩 的黑名单取消
import pygame
import tkinter as tk
#import aiohttp
#import asyncio
import threading as thr
class TextBox:
    def __init__(self, rect, font, text="", bgcolor=None, fgcolor=(255, 255, 255),head=0):
        self.rect = rect # 外部矩形
        #self.rect.width+=20
        #self.rect.height+=20
        #print(self.rect.size)
        self.font = font # 字体对象
        self.text = text # 文本内容
        self.bgcolor = bgcolor # 背景颜色
        self.fgcolor = fgcolor # 前景颜色
        
        self.lines = [] # 每行文本列表
        self._rendered_lines = [] # 已经渲染的行表面
        self._rendered_rects = [] # 已经渲染的行矩形
        
        self._scroll_x = 0 # 横向滚动值
        self._scroll_y = 0 # 纵向滚动值
        
        self._click_x = None
        self._click_y = None
        
        # 计算每行文本
        self._calculate_lines()
        self._render_lines()
        if head:
            self._scroll_x=self.get_last_max_scroll_x()
            self._scroll_y=self.get_max_scroll_y()
        self._render_lines()
    def _calculate_lines(self):
        """计算每行文本"""
        a=self.text
        words = a.split('\n')
        for word in words:
            self.lines.append(word)
    def _render_lines(self):
        """渲染每行文本"""
        self._rendered_lines = []
        self._rendered_rects = []
        
        x = 0 - self._scroll_x
        y = 0 - self._scroll_y
        line_height = self.font.get_linesize()
        for line in self.lines:
            #print(line)
            surface = self.font.render(line, True, self.fgcolor, self.bgcolor)
            self._rendered_lines.append(surface)
            rect = surface.get_rect(topleft=(x, y))
            self._rendered_rects.append(rect)
            y += line_height
        #print(self._rendered_lines)
    def _scroll(self, dx=0, dy=0):
        """滚动"""
        self._scroll_x += dx
        self._scroll_y += dy
        
        # 边界判断
        if self._scroll_x < 0:
            self._scroll_x = 0
        if self._scroll_x > self.get_max_scroll_x():
            self._scroll_x = self.get_max_scroll_x()
        if self._scroll_y < 0:
            self._scroll_y = 0
        if self._scroll_y > self.get_max_scroll_y():
            self._scroll_y = self.get_max_scroll_y()
        
        self._render_lines()

    def draw(self, screen):
        """绘制"""
        surface = pygame.Surface(self.rect.size)
        if self.bgcolor:
            surface.fill(self.bgcolor)
        
        # 鼠标拖动滚动条
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            mx, my = pygame.mouse.get_pos()
            if self._click_x is not None and self._click_y is not None:
                dx = mx - self._click_x
                dy = my - self._click_y
                if abs(dx) > abs(dy):
                    self._scroll(dx=-dx)
                else:
                    self._scroll(dy=-dy)
            self._click_x = mx
            self._click_y = my
        
        else:
            self._click_x = None
            self._click_y = None
        
        for i in range(len(self._rendered_lines)):
            #print(self._rendered_lines)
            surface.blit(self._rendered_lines[i], self._rendered_rects[i])
        
        # 绘制滚动条
        '''if self.get_max_scroll_x() > 0:
            pygame.draw.rect(surface, (200, 200, 200), (0, self.rect.height+0, self.rect.width+0, 10))
            pygame.draw.rect(surface, (100, 100, 100), (0, self.rect.height+0, self.rect.width+0, 10), 1)
            pygame.draw.rect(surface, (150, 150, 150), (0, self.rect.height+0, self._scroll_x/(self.get_max_scroll_x()+1)*(self.rect.width+0), 10))
        if self.get_max_scroll_y() > 0:
            pygame.draw.rect(surface, (200, 200, 200), (self.rect.width+0, 0, 10, self.rect.height+0))
            pygame.draw.rect(surface, (100, 100, 100), (self.rect.width+0, 0, 10, self.rect.height+0), 1)
            pygame.draw.rect(surface, (150, 150, 150), (self.rect.width+0, 0, 10, self._scroll_y/(self.get_max_scroll_y()+1)*(self.rect.height+0)))
        '''
        screen.blit(surface, self.rect.topleft)
    
    def get_max_scroll_x(self):
        """获取最大横向滚动值"""
        maxx=-1
        for r in self._rendered_rects:
            maxx=max(maxx,r.width)
        return max(0,maxx- self.rect.width)
        #return max(0, sum([r.width for r in self._rendered_rects]) - self.rect.width)
    def get_last_max_scroll_x(self):
        maxx=self._rendered_rects[-1].width
        return max(0,maxx- self.rect.width)
    def get_max_scroll_y(self):
        """获取最大纵向滚动值"""
        return max(0, sum([r.height for r in self._rendered_rects]) - self.rect.height)

pygame.init()
font = pygame.font.Font("方正达利体.ttf", 20)
txt=''#输入框文本
aitxt=''#gpt回答的文本
chat=0
video=1
textbox = TextBox(pygame.Rect(50,30,720-50-50,100), font,'我：'+txt,bgcolor=(0xad,0xbf,0x8f),fgcolor=(255,255,255))
aitextbox = TextBox(pygame.Rect(50,230,720-50-50,200), font,'ChatGPT：'+aitxt,bgcolor=(0x78,0x8c,0x57),fgcolor=(255,255,255),head=1)
clock = pygame.time.Clock()
root=tk.Tk()
root.title("请输入聊天的内容")
entry = tk.Text(root)
entry.pack()
ininit=True
# 创建确定按钮并将其与回调函数绑定
def on_button_click():
    global txt,chat,time,video,textbox
    txt = entry.get(1.0, tk.END)
    textbox=TextBox(pygame.Rect(50,30,720-50-50,100), font,'我：'+txt,bgcolor=(0xad,0xbf,0x8f),fgcolor=(255,255,255))
    root.withdraw()
    chat=1
    time=0
    if ininit:
        video=1
    else:
        video=0
button = tk.Button(root, text="确定", command=on_button_click)
button.pack()
import requests
def send_message(url, data,headers):
    global aitxt,aitextbox
    # 发送 HTTP POST 请求到 chatGPT API
    response = requests.post(url, headers=headers, json=data, stream = True)
    response.encoding = "utf-8"
    for chunk in response.iter_content(decode_unicode=True):
        aitxt+=chunk
        aitextbox = TextBox(pygame.Rect(50,230,720-50-50,200), font,'ChatGPT：'+aitxt,bgcolor=(0x78,0x8c,0x57),fgcolor=(255,255,255),head=1)
        print(chunk,end='')
def main(txt,id):
    id=str(id)
    url = 'https://api.binjie.fun/api/generateStream'
    data = {'prompt': txt, 
            'userld': '#/chat/'+id,
            'network':True,
            'system':"",
            'withoutContext':False,
            'stream':False,
    }
    url1='https://chat2.aichatos.top/#/chat/'+id
    headers = {
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,zh-TW;q=0.6,eo;q=0.5',
        'Connection': 'keep-alive',
        'Origin': url1,
        'Referer': url1,
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    }
    send_message(url, data,headers)
def gpt1(txt,id):
    global chat
    main(txt,id)
    print('\n')
    chat=0
def gpt():
    global aitxt,aitextbox
    txt=entry.get(1.0,tk.END)
    aitxt=''
    aitextbox = TextBox(pygame.Rect(50,230,720-50-50,200), font,'ChatGPT：'+aitxt,bgcolor=(0x78,0x8c,0x57),fgcolor=(255,255,255),head=1)
    id=1683974504108
    tt=thr.Thread(target=gpt1,args=(txt,id),name="T1")
    tt.start()
    

screen = pygame.display.set_mode((960/2*1.5,720/2*1.5))
pygame.display.set_caption("ChatGPT")
bg = pygame.image.load("bg.png")
#bg1 = pygame.image.load("bg.png")
sha = pygame.image.load("sha.png")
ku=pygame.image.load("ku.png")
title=pygame.image.load("title.png")
Long=pygame.image.load("Long.png")
shanum=352+68
shaalpha=0
kunum=68
kualpha=0
sha.set_alpha(0)
ku.set_alpha(0)
title.set_alpha(0)
aww=[]
def sc_to_pg(x,lon):
    return int((x+lon/2)/2*1.5)
def sc_to_long(lon):
    return int(lon/2*1.5)
awwx=-120
awwy=80
awwpic=0
awwx,awwy=sc_to_pg(awwx,480),sc_to_pg(awwy,360)
for i in range(1,3+1):
    awwy=sc_to_pg(80,360)
    for j in range(1,4+1):
        awwpic+=1
        image=pygame.image.load("aww"+str(awwpic)+".png")
        add=0
        if awwpic%4==1:
            #print(awwpic)
            add=int(image.get_width()/2)
            #add=1000
        if awwpic==1:
            add+=20
        aww.append([image,(awwx+add,awwy-image.get_height()),(awwx+add,600)])
        #print(sc_to_long(45))
        awwy+=70#sc_to_long(45)
        
    awwx+=190
#print(aww)
#canqita=0
aww_alpha=[0 for i in range(12)]
title_alpha=0
titlenum=150
#print(aww_alpha)
bgalpha=0
#bg1.set_alpha(0)
mouse_down=False
time=0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if pygame.mouse.get_pressed()[0] and mouse_down==False:
        #chat=1
        #canqita=1
        #time=0
        mouse_down=True
        entry.delete(1.0, tk.END)
        pygame.display.update()
        root.deiconify()
    screen.fill((255,255,255))
    screen.blit(bg,(0,0))
    #sha.set_alpha(0)
    screen.blit(sha,(0,shanum))
    screen.blit(ku,(0,kunum))
    ct=screen.get_rect().center[0]-title.get_width()/2
    screen.blit(title,(ct,titlenum))
    #screen.blit(aww1,(awwx+70/2,awwy-16))
    if '标题':
        if not chat:
            title_alpha+=17
            title_alpha=min(title_alpha,255)
            title.set_alpha(title_alpha)
            titlenum+=(90-titlenum)/4
        if chat:
            #print(titlenum)
            title_alpha-=17
            title_alpha=max(title_alpha,0)
            title.set_alpha(title_alpha)
            titlenum+=(-100-titlenum)/4
    if '其他':
        if not chat:
            for i in range(len(aww)):
                if time>=i*10:
                    #print(aww[i][1][1])
                    a12=(aww[i][1][1]-aww[i][2][1])/4
                    aww[i][2]=(aww[i][2][0],aww[i][2][1]+a12)
                    aww_alpha[i]+=17
                    aww_alpha[i]=min(aww_alpha[i],255)
                    aww[i][0].set_alpha(aww_alpha[i])
                    screen.blit(aww[i][0],aww[i][2])
        if chat:
            for i in range(len(aww)):
                if time>=i*10:
                    #print(aww[i][1][1])
                    a12=(-100-aww[i][2][1])/4
                    aww[i][2]=(aww[i][2][0],aww[i][2][1]+a12)
                    aww_alpha[i]-=17
                    aww_alpha[i]=max(aww_alpha[i],0)
                    #print('a'+str(i)+':',aww_alpha[i],aww[i][2][1])
                    aww[i][0].set_alpha(aww_alpha[i])
                    screen.blit(aww[i][0],aww[i][2])
                else:
                    screen.blit(aww[i][0],aww[i][2])
            if aww_alpha[-1]==0:
                #chat=1
                break
    if '输入框':
        mb=0
        if chat:
            mb=68
        else:
            mb=0
        kunum+=(mb-kunum)/4
        if not mb:
            kualpha+=17
            kualpha=min(kualpha,255)
        else:
            kualpha-=17
            kualpha=max(kualpha,0)
        ku.set_alpha(kualpha)
    if '阴影':
        shanum+=(352-shanum)/4
        shaalpha+=17
        shaalpha=min(shaalpha,255)
        sha.set_alpha(shaalpha)
    pygame.display.update()
    clock.tick(60)
    root.update()
    if mouse_down==False:
        root.withdraw()
    time+=10
Longnum_alpha=0
Longnum=700
time=0
ininit=False
Long.set_alpha(Longnum_alpha)
#print(video)
while True:
    mouse_pos=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
            if textbox.rect.collidepoint(mouse_pos):
                textbox._scroll(dy=-40)
            if aitextbox.rect.collidepoint(mouse_pos):
                aitextbox._scroll(dy=-40)
            
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
            if textbox.rect.collidepoint(mouse_pos):
                textbox._scroll(dy=40)
            if aitextbox.rect.collidepoint(mouse_pos):
                aitextbox._scroll(dy=40)
    screen.fill((255,255,255))
    screen.blit(bg,(0,0))
    screen.blit(sha,(0,352))
    
    if '输入文本' and video!=0:
        textbox.draw(screen)
        #textbox._scroll(dy=0)
    screen.blit(Long,(0,Longnum))
    screen.blit(ku,(0,kunum))
    if '输入框':
        #print(chat)
        mb=0
        #print(chat)
        if chat:
            mb=68
        else:
            mb=0
        #print(chat,mb,kunum)
        kunum+=(mb-kunum)/4
        if not mb:
            kualpha+=17
            kualpha=min(kualpha,255)
        else:
            kualpha-=17
            kualpha=max(kualpha,0)
        ku.set_alpha(kualpha)
    
    if video==0:
        #print(video,)
        Longnum+=(-50-Longnum)/6
        if round(Longnum)==-50 and Longnum_alpha==0:
            video=1
            Longnum=700
        Longnum_alpha-=10
        Longnum_alpha=max(Longnum_alpha,0)
        Long.set_alpha(Longnum_alpha)
    elif video==1:
        Longnum+=(180-Longnum)/6
        if round(Longnum)==180 and Longnum_alpha==255:
            video=2
            #chat=0
            gpt()
        Longnum_alpha+=10
        Longnum_alpha=min(Longnum_alpha,255)
        Long.set_alpha(Longnum_alpha)
    elif video==2 and chat==0:
        entry.delete(1.0,tk.END)
        root.deiconify()
        video=3
        #chat=0
        '''import time as ti
        ti.sleep(2)
        gpt2()'''
        #video=0
    #if not chat:
    if video==2 or video==3:
        aitextbox.draw(screen)
    root.update()
    pygame.display.update()
    clock.tick(60)
    time+=1