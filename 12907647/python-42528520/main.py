import tkinter as tk
import pygame
import sys
import os

input('''准备就绪。
小轩电脑1.0+(https://code.xueersi.com/home/project/detail?lang=code&pid=31078655&version=offline&form=python&langType=python)
是小轩编写的一款模拟操作系统，已经有了基础的功能
这一次将会重新制作，更进一步，超越上次的创作
上次用tkinter/pygame结合，用os句柄结合，不支持非windows系统
这次将会换一种方法:pygame全屏显示作为桌面，tkinter弹窗显示在它上面
多亏了pygame2.1.0社区终于开始用了，pygame的sdl渲染更方便，不用强制init
甚至可以绘制圆角矩形了，对我这个系统的支持更好
我甚至还会做一些系统配置、文件配置，慢慢写大作，只是看弃坑是不是问题
新版本:新框架
回车进入框架:''')

pygame.init()
screen = pygame.display.set_mode((1920,1080),flags=pygame.FULLSCREEN)

root = tk.Tk()
root.attributes('-topmost',True)

pygame.ACTIVITIES = [pygame.MOUSEBUTTONUP,pygame.MOUSEBUTTONDOWN,pygame.ACTIVEEVENT,]

class TitleBar:
    def __init__(self,icon,title,length,*cfgs):
        self.icon = icon
        self.title = title
        self.size = [length,20]
    def draw(self):
        ...

class WindowBody:
    def __init__(self,size,*cfgs):
        self.size = size
    def draw(self):
        ...
    
class Window:
    def __init__(self,wid,icon,title,size,*cfgs):
        self.wid = wid
        self.mode = 'normal'   # 最小化、普通化、最大化
        self.icon = icon
        self.title = title
        self.size = list(size)
        self.configs = list(cfgs)
        self.titlebar = TitleBar(self.icon,self.title,self.size[1])
        self.body = WindowBody(self.size)
    def get_id(self):
        return self.wid
    def get_title(self):
        return self.title
    def draw(self):
        self.titlebar.draw()
        self.body.draw()

desktop = Window(0,'test-icon','desktop',[1920,1080],'cfg1','cfg2','cfg3',...)
windows = [desktop,root]



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            root.destroy()
            pygame.quit()
            sys.exit()
            # raise SystemError('程序结束。')
        if event.type in pygame.ACTIVITIES:
            root.attributes('-topmost',True)
    screen.fill((0,255,111))
    pygame.display.update()
    root.update()