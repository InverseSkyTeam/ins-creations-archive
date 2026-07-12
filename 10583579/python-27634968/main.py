import pygame,sys,time
pygame.init()
screen = pygame.display.set_mode((700,940))
pygame.display.set_caption("自动生成迷宫")
myImg = pygame.image.load("img1.png")
black = pygame.image.load("黑色.png")
yellow = pygame.image.load("黄色.png")
idea = pygame.image.load("提示.png")
import random
c = 10#墙块边长
row = 47#行数
column = 35#列数
ma = []#迷宫地图状态map
b = []#迷宫单元访问状态
row1 = 1#行号
column1 = 0#列号
stack = []#栈
no = []#未被访问单元列表
x = 0
y = 0
for i in range(row):
    column1 = 1
    for n in range(column):
        if column1%2 == 0 and row1%2 == 0:
            ma.append(0)
        else:
            ma.append(1)
        b.append(0)
        column1 += 1
    row1 += 1
start = 49#起点
stack.append(start)
this = 0#当前单元
that = 0#相邻单元
while len(stack) != 0:
    this = stack[-1]
    no = []
    n = this
    if n>(3*column) and n%column != 0 and n%column != 1:
        that = n - 2*column
        if b[that-1] == 0:
            no.append(that)
    if n<(row-2)*column:
        that = n + 2*column
        if b[that-1] == 0:
            no.append(that)
    if n%column > 3:
        that = n - 2
        if b[that-1] == 0:
            no.append(that)
    if n%column < column-2:
        that = n + 2
        if b[that-1] == 0:
            no.append(that)
    if len(no)>0:
        that = no[(random.randint(0,2000))%(len(no))]
        if this-that == 2*column:
            ma[this-column-1] = 0
        if that-this == 2*column:
            ma[this+column-1] = 0
        if this-that == 2:
            ma[this-2] = 0
        if that-this == 2:
            ma[this] = 0
        b[that-1] = 1
        stack.append(that)
    else:
        stack.pop()
screen.fill((0,255,127))
num = 1
for s in range(row):
    for q in range(column):
        if ma[num-1] == 1:
            screen.blit(black,(x,y))
        num += 1
        x += 2*c
    x = 0
    y += 2*c
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()