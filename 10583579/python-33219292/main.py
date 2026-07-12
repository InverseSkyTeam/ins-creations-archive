'''
请勿抄袭©
'''
import pygame
from tkinter.messagebox import showinfo
showinfo("温馨提示","本作品作者何嘉晨,请勿抄袭,可以改编,如果喜欢就给个赞吧~")
showinfo("温馨提示","本作品可以画出我的世界里的钻石套装，如有不足可以指出")
deep_red = (255,248,220)
red = (255,0,0)
light_red = (255,99,71)
brown = (139,69,19)
pink = (255,105,180)
deep_pink = (238,130,238)
purple = (138,43,226)
green = (124,252,0)
black = (0,0,0)
diamond_blue = (1,225,255)
cyan = (12,135,172)
from time import sleep
def diamond():
    global black,diamond_blue,cyan
    pygame.init()
    screen = pygame.display.set_mode((300,940))
    pygame.display.set_caption("钻石套装 作者:何嘉晨")
    screen.fill((255,255,255))
    pos_x = 50
    pos_y = 0
    dic = {0: (255,255,255),1: black,2: diamond_blue,3: cyan}
    lst = [0,0,1,1,1,1,1,1,0,0,0,1,2,2,2,2,2,3,1,0,1,2,0,0,2,2,2,3,3,1,1,2,0,2,2,2,3,3,3,1,1,2,2,2,2,2,3,3,3,1,1,2,2,1,1,1,1,3,3,1,1,2,1,1,1,1,1,1,3,1,1,2,1,1,1,1,1,1,3,1,1,2,1,1,1,1,1,1,3,1,0,1,1,0,0,0,0,1,1,0]
    for i in lst:
        pygame.draw.rect(screen, dic[i], ((pos_x, pos_y), (20, 20)), 0)
        pos_x += 20
        if pos_x == 250:
            pos_x = 50
            pos_y += 20
        pygame.display.update()
        sleep(0.05)
    lst1 = [0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,1,1,2,3,1,0,0,0,1,2,2,1,1,0,1,2,2,2,3,1,1,0,1,1,2,2,2,2,1,1,2,2,2,2,2,2,1,2,2,2,2,2,3,1,1,3,2,2,2,2,2,2,2,2,2,2,3,3,1,0,1,2,0,0,2,2,2,2,2,2,2,3,3,1,0,1,3,0,2,2,2,2,2,2,2,3,3,1,0,0,0,1,2,2,2,2,2,2,2,2,3,1,0,0,0,0,1,2,2,2,2,2,2,2,3,3,1,0,0,0,0,1,3,2,2,2,2,2,3,3,3,1,0,0,0,0,1,3,3,3,3,3,3,3,3,3,1,0,0,0,0,0,1,3,3,3,3,3,3,3,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0]
    pos_x = 0
    pos_y += 10
    for i in lst1:
        pygame.draw.rect(screen, dic[i], ((pos_x, pos_y), (20, 20)), 0)
        pos_x += 20
        if pos_x == 300:
            pos_x = 0
            pos_y += 20
        pygame.display.update()
        sleep(0.05)
    lst2 = [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2, 3, 1, 1, 2, 0, 0, 2, 2, 2, 2, 3, 1, 1, 2, 0, 3, 3, 3,3, 2, 3, 1, 1, 2, 3, 3, 1, 1, 3, 2, 3, 1, 1, 2, 3, 1, 0, 0, 1, 2, 3, 1, 1, 2, 3, 1, 0, 0, 1, 2, 3, 1, 1, 2,3, 1, 0, 0, 1, 2, 3, 1, 1, 2, 3, 1, 0, 0, 1, 2, 3, 1, 1, 2, 3, 1, 0, 0, 1, 2, 3, 1, 1, 3, 3, 1, 0, 0, 1, 3,3, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1]
    pos_x = 50
    pos_y += 10
    for i in lst2:
        pygame.draw.rect(screen, dic[i], ((pos_x, pos_y), (20, 20)), 0)
        pos_x += 20
        if pos_x == 250:
            pos_x = 50
            pos_y += 20
        pygame.display.update()
        sleep(0.05)
    lst3 = [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 2, 3, 1, 0, 0, 1, 3, 2, 1, 0, 0, 0, 0, 1, 0, 3, 1, 0, 0,1, 3, 0, 1, 0, 0, 0, 0, 1, 2, 3, 1, 0, 0, 1, 3, 2, 1, 0, 0, 0, 0, 1, 2, 3, 1, 0, 0, 1, 3, 2, 1, 0, 0, 0, 0,1, 2, 3, 1, 0, 0, 1, 3, 2, 1, 0, 0, 0, 1, 0, 2, 3, 1, 0, 0, 1, 3, 2, 2, 1, 0, 1, 2, 2, 3, 3, 1, 0, 0, 1, 3,3, 2, 2, 1, 1, 3, 3, 3, 1, 0, 0, 0, 0, 1, 3, 3, 3, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ]
    pos_x = 10
    pos_y += 10
    for i in lst3:
        pygame.draw.rect(screen, dic[i], ((pos_x, pos_y), (20, 20)), 0)
        pos_x += 20
        if pos_x == 290:
            pos_x = 10
            pos_y += 20
        pygame.display.update()
        sleep(0.05)
    print("绘制完毕")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
diamond()