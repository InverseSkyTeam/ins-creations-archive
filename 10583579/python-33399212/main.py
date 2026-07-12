#!/usr/local/bin/python
# coding: utf-8

#倒库
import pygame
import re
import math
from tkinter.messagebox import *

running = True

def sqrt(num):
    return str(math.sqrt(num))[:13]

#颜色
light_blue = (182,222,237)
deep_white = (241,248,251)
grey_blue = (216,236,245)
blue = (114,182,229)


#初始化
pygame.init()
screen = pygame.display.set_mode((320,495))
pygame.display.set_caption("计算器/Calculator")
screen.fill(light_blue)
pygame.display.set_icon(pygame.image.load("计算器.png"))

#定义字体
font1 = pygame.font.SysFont('kaiti',25)
font2 = pygame.font.SysFont('kaiti',50)


#绘制文本
t0 = font1.render("0",True,(0,0,0))
t1 = font1.render("1",True,(0,0,0))
t2 = font1.render("2",True,(0,0,0))
t3 = font1.render("3",True,(0,0,0))
t4 = font1.render("4",True,(0,0,0))
t5 = font1.render("5",True,(0,0,0))
t6 = font1.render("6",True,(0,0,0))
t7 = font1.render("7",True,(0,0,0))
t8 = font1.render("8",True,(0,0,0))
t9 = font1.render("9",True,(0,0,0))
t10 = font1.render("=",True,(0,0,0))
t11 = font1.render(".",True,(0,0,0))
t12 = font1.render("+",True,(0,0,0))
t13 = font1.render("-",True,(0,0,0))
t14 = font1.render("×",True,(0,0,0))
t15 = font1.render("÷",True,(0,0,0))
t16 = font1.render("+/-",True,(0,0,0))
t17 = font1.render("清空",True,(0,0,0))
t18 = font1.render("%",True,(0,0,0))
t19 = font2.render("0",True,(0,0,0))

#导入图片
i1 = pygame.image.load("开方.PNG")
i2 = pygame.image.load("平方.PNG")
i3 = pygame.image.load("分式.PNG")
i4 = pygame.image.load("删除.PNG")


#定义矩形
r1 = pygame.Rect(2,292,78,48)
r2 = pygame.Rect(82,292,78,48)
r3 = pygame.Rect(162,292,78,48)
r4 = pygame.Rect(242,292,78,48)
r5 = pygame.Rect(2,342,78,48)
r6 = pygame.Rect(82,342,78,48)
r7 = pygame.Rect(162,342,78,48)
r8 = pygame.Rect(242,342,78,48)
r9 = pygame.Rect(2,392,78,48)
r10 = pygame.Rect(82,392,78,48)
r11 = pygame.Rect(162,392,78,48)
r12 = pygame.Rect(242,392,78,48)
r13 = pygame.Rect(2,442,78,48)
r14 = pygame.Rect(82,442,78,48)
r15 = pygame.Rect(162,442,78,48)
r16 = pygame.Rect(242,442,78,48)
r17 = pygame.Rect(2,242,78,48)
r18 = pygame.Rect(82,242,78,48)
r19 = pygame.Rect(162,242,78,48)
r20 = pygame.Rect(242,242,78,48)
r21 = pygame.Rect(2,192,78,48)
r22 = pygame.Rect(82,192,80,48)
r23 = pygame.Rect(162,192,78,48)
r24 = pygame.Rect(242,192,78,48)

def draw_calc(text):
    #申明全局变量
    global font2
    global i1
    global i2
    global i3
    global i4
    global t1
    global t2
    global t3
    global t4
    global t5
    global t6
    global t7
    global t8
    global t9
    global t10
    global t11
    global t12
    global t13
    global t14
    global t15
    global t16
    global t17
    global t18
    global t19
    global deep_white,grey_blue,blue,light_blue
    
    #调整字体大小
    if 14>len(text) >=12:
        font2 = pygame.font.SysFont('kaiti',38)
    if 16>len(text) >=14:
        font2 = pygame.font.SysFont('kaiti',30)
    if len(text)>=16:
        text = "溢出"
        font2 = pygame.font.SysFont('kaiti',80)
    
    screen.fill(light_blue)
    t19 = font2.render(text,True,(0,0,0))
    
    #绘制矩形
    pygame.draw.rect(screen, deep_white, ((2,292), (78,48)), 0)
    pygame.draw.rect(screen, deep_white, ((82,292), (78,48)), 0)
    pygame.draw.rect(screen, deep_white, ((162,292), (78,48)), 0)
    pygame.draw.rect(screen, grey_blue, ((242,292), (78,48)), 0)
    pygame.draw.rect(screen, deep_white, ((2,342), (78,48)), 0)
    pygame.draw.rect(screen, deep_white, ((82,342), (78,48)), 0)
    pygame.draw.rect(screen, deep_white, ((162,342), (78,48)), 0)
    pygame.draw.rect(screen, grey_blue, ((242,342), (78,48)), 0)
    pygame.draw.rect(screen, deep_white, ((2,392), (78,48)), 0)
    pygame.draw.rect(screen, deep_white, ((82,392), (78,48)), 0)
    pygame.draw.rect(screen, deep_white, ((162,392), (78,48)), 0)
    pygame.draw.rect(screen, grey_blue, ((242,392), (78,48)), 0)
    pygame.draw.rect(screen, blue, ((242, 442), (78,48)), 0)
    pygame.draw.rect(screen, deep_white, ((2,442), (78,48)), 0)
    pygame.draw.rect(screen, deep_white, ((82,442), (78,48)), 0)
    pygame.draw.rect(screen, deep_white, ((162,442), (78,48)), 0)
    pygame.draw.rect(screen, grey_blue, ((2,242), (78,48)), 0)
    pygame.draw.rect(screen, grey_blue, ((82,242), (78,48)), 0)
    pygame.draw.rect(screen, grey_blue, ((162,242), (78,48)), 0)
    pygame.draw.rect(screen, grey_blue, ((242,242), (78,48)), 0)
    pygame.draw.rect(screen, grey_blue, ((2,192), (78,48)), 0)
    pygame.draw.rect(screen, grey_blue, ((82,192), (80,48)), 0)
    pygame.draw.rect(screen, grey_blue, ((162,192), (78,48)), 0)
    pygame.draw.rect(screen, grey_blue, ((242,192), (78,48)), 0)
    
    screen.blit(t1,(35,303))
    screen.blit(t2,(115,303))
    screen.blit(t3,(195,303))
    screen.blit(t4,(35,353))
    screen.blit(t5,(115,353))
    screen.blit(t6,(195,353))
    screen.blit(t7,(35,403))
    screen.blit(t8,(115,403))
    screen.blit(t9,(195,403))
    screen.blit(t10,(275,453))
    screen.blit(t0,(115,453))
    screen.blit(t11,(195,453))
    screen.blit(t12,(275,403))
    screen.blit(t13,(275,353))
    screen.blit(t14,(268,303))
    screen.blit(t15,(268,253))
    screen.blit(t16,(25,453))
    screen.blit(t17,(135,203))
    screen.blit(t18,(35,203))
    screen.blit(t18,(35,203))
    screen.blit(t19,(10,10))
    screen.blit(i1,(184,245))
    screen.blit(i2,(104,248))
    screen.blit(i3,(24,248))
    screen.blit(i4,(268,203))
    
    pygame.display.update()
text = "0"
text1 = "0"
draw_calc('0')
numlist = []
flag = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if r1.collidepoint(event.pos):
                dakai = "1"
            elif r2.collidepoint(event.pos):
                dakai = "2"
            elif r3.collidepoint(event.pos):
                dakai = "3"
            elif r4.collidepoint(event.pos):
                text += "×"
                text1 += "*"
                draw_calc(text)
                continue
            elif r5.collidepoint(event.pos):
                dakai = "4"
            elif r6.collidepoint(event.pos):
                dakai = "5"
            elif r7.collidepoint(event.pos):
                dakai = "6"
            elif r8.collidepoint(event.pos):
                text += "-"
                text1+= '-'
                draw_calc(text)
                continue
            elif r9.collidepoint(event.pos):
                dakai = "7"
            elif r10.collidepoint(event.pos):
                dakai = "8"
            elif r11.collidepoint(event.pos):
                dakai = "9"
            elif r12.collidepoint(event.pos):
                text += "+"
                text1 += "+"
                draw_calc(text)
                continue
            elif r13.collidepoint(event.pos):
                text="-("+text+")"
                text1="-("+text1+")"
                draw_calc(text)
                continue
            elif r14.collidepoint(event.pos):
                dakai = "0"
            elif r15.collidepoint(event.pos):
                dakai = "."
            elif r16.collidepoint(event.pos):
                try:
                    text = str(eval(text1))
                    if "." in text and len(text)>=16:
                        text = text[:15]
                    text1 = text
                    draw_calc(text)
                    continue
                except Exception as e:
                    showerror("报错了","请仔细检查，输入错误\n终止代码:"+str(e))
                    continue
            elif r17.collidepoint(event.pos):
                text = "1÷"+str(eval(text1))
                text1 = "1/"+str(eval(text1))
                draw_calc(text)
                continue
            elif r18.collidepoint(event.pos):
                text = "pow("+text+")"
                text1 = "pow("+text1+",2)"
                draw_calc(text)
                continue
            elif r19.collidepoint(event.pos):
                text = "sqrt("+text+")"
                text1 = "sqrt("+text1+")"
                draw_calc(text)
                continue
            elif r20.collidepoint(event.pos):
                text += "÷"
                text1+= '/'
                draw_calc(text)
                continue
            elif r21.collidepoint(event.pos):
                dakai = "%"
                flag = 1
            elif r22.collidepoint(event.pos) or r23.collidepoint(event.pos):
                text = "0"
                text1 = "0"
                draw_calc(text)
                continue
            elif r24.collidepoint(event.pos):
                if len(text) != 1:
                    text = text[:-1]
                    text1 = text1[:-1]
                    draw_calc(text)
                    continue
                else:
                    text,text1 = "0","0"
                    draw_calc(text)
                    continue
            else:
                continue
            text = text+dakai
            text1 = text1 + dakai
            if flag == 1:
                text1 = text1[:-1]+"*0.01"
                flag = 0
            numlist = re.findall("\d+",text)
            if text[0] == ".":
                text = "0" + text
                text1 = "0" + text1
            for n in numlist:
                if text[text.find(n)-1] != "." and text.find(n) != 0:
                    text = text[:text.find(n)]+str(int(n))+text[text.find(n)+len(n):]
                    text1 = text1[:text1.find(n)]+str(int(n))+text1[text1.find(n)+len(n):]
            while len(text) != 1 and text[0] == "0":
                text = text[1:]
                text1 = text1[1:]
            draw_calc(text)
pygame.quit()