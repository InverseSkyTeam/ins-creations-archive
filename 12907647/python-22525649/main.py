from urllib import request
from tkinter import *
from time import *
import tkinter as tk
import urllib
import pygame
import sys
import os
import re

print('如虚拟系统模拟机体验中未显示说明书，请重新运行')
print('如您没看作品介绍和我的置顶评论，请去去再来！')
print('如您在做作品，请也保存再来！')
print('进入后先看说明书！里面有退出(Win+w救命键，移到底下的菜单栏救命动作，Alt+F4终极救命动作但是会关闭浏览器)、使用方法！另外，您在虚拟计算机系统中所做的一切也会在现实世界改掉！mac谨慎使用！')
xxx = input('输入体验：1.虚拟电脑中小型屏幕或大屏幕的虚拟感 2.win等电脑的大型屏幕的模拟世界')

root = tk.Tk()
root.title("")
if '2' in xxx:
    pgw = tk.Frame(root,width = 1650, height = 1000)
else:
    pgw = tk.Frame(root,width = 1200, height = 700)
pgw.pack()
os.environ['SDL_WINDOWID'] = str(pgw.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'


# pygame start‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍
pygame.init()
if '2' in xxx:
    screen = pygame.display.set_mode((1650,1000),pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode((1200,700),pygame.FULLSCREEN)
screen = pygame.display.set_mode(screen.get_size(),pygame.FULLSCREEN)

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
    show_text('可以开始操控了，如无法退出，按Win+w(mac后面有)，不行Alt+F4,Ctrl+w',pos=(11,11))
    show_text('黑屏因为运行慢。你可按上面组合后操控模拟机，注意模拟机上你做了啥就会真的改掉',pos=(11,41))
    show_text('是不是很牛？在评论区回复和点赞、3连，改编发现代码也不多',pos=(11,71))
    show_text('在虚拟机上点终止运行，你就和开始被黑色漩涡一样吸回现实',pos=(11,101))
    pygame.display.update()
    try:
        root.update()
    except:
        pass
# pygame pyend‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍





while True:
    pygame.display.update()
    root.update()