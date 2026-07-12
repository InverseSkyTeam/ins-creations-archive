from ijlib import *
import threading
import tkinter as tk
import pygame
import math
import sys
import os

ig = insgui
insos = win_op_sys

# insos.explorer('down')

pygame.init()
screen = pygame.display.set_mode((1920,1080),flags=pygame.FULLSCREEN)

root = ig.INSroot(400,300,400,100,title='INSwindow 1.0')
root.change_attr('maxsize',(800,500))

mainrootlist = []
mainrootlist.append(root)

mainrunning = True



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainrunning = False
    
    if not mainrunning:
        mainrootlist.clear()
        pygame.quit()
        break
    
    screen.fill((0,255,111))
    pygame.display.update()
    
    rootindex = 0
    while rootindex < len(mainrootlist):
        try:
            mainrootlist[rootindex].update()
            rootindex += 1
        except:
            mainrootlist.remove(mainrootlist[rootindex])
            
# insos.explorer('up')
print('测试完成')
sys.exit()