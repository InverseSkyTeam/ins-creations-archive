from threading import *
import pygame
from time import *
from random import randint
from pickle import dump,load
flag1 = 0
k = 0
gameover = 0
time1 = 0
def migong():
    global flag1,k,gameover
    k = 0
    pygame.init()
    screen = pygame.display.set_mode((738,990))
    pygame.display.set_caption("自动生成迷宫")
    idea5 = pygame.image.load("范围.PNG")
    win = pygame.image.load("win.PNG")
    idea0 = pygame.image.load("提示.PNG")
    idea1 = pygame.image.load("idea1.PNG")
    idea2 = pygame.image.load("idea2.png")
    idea3 = pygame.image.load("idea3.PNG")
    idea4 = pygame.image.load("终点.PNG")
    sleep(5)
    screen.fill((255,255,255))
    screen.blit(idea0,(0,0))
    pygame.display.update()
    sleep(1)
    screen.blit(idea1,(0,0))
    pygame.display.update()
    sleep(1.2)
    screen.blit(idea2,(0,0))
    screen.blit(idea3,(0,0))
    pygame.display.update()
    sleep(1.5)
    sleep(1.5)
    screen.fill((255,255,255))
    screen.blit(idea4,(0,0))
    pygame.display.update()
    sleep(3)
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
    x1 = 0
    y1 = 0
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
            that = no[(randint(0,2000))%(len(no))]
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
    ma[33] = 0
    ma[34] = 3
    ma[35*46+1] = 2
    screen.fill((0,255,127))
    num = 1
    for s in range(row):
        for q in range(column):
            if ma[num-1] == 1:
                pygame.draw.rect(screen, (0,0,0), ((x,y), (21,21)), 0)
            if ma[num-1] == 3:
                pygame.draw.rect(screen, (255,0,0), ((x,y), (21,21)), 0)
            if ma[num-1] == 2:
                pygame.draw.rect(screen, (255,255,0), ((x,y), (21,21)), 0)
            num += 1
            x += 21
        x = 0
        y += 21
    pygame.display.update()
    sum1 = 35*46+1
    x = 0
    y = 0
    num = 1
    thread1 = Thread(target=time)
    thread1.start()
    while True:
        try:
            screen.fill((0,255,127))
        except:
            break
        for s in range(row):
            for q in range(column):
                if ma[num-1] == 1:
                    pygame.draw.rect(screen, (0,0,0), ((x,y), (21,21)), 0)
                if ma[num-1] == 3:
                    pygame.draw.rect(screen, (255,0,0), ((x,y), (21,21)), 0)
                if ma[num-1] == 2:
                    pygame.draw.rect(screen, (255,255,0), ((x,y), (21,21)), 0)
                num += 1
                x += 21
            x = 0
            y += 21
        x = 0
        y = 0
        num = 1
        pygame.display.update()
        if ma[34] == 2:
            print("You win")
            screen.fill((255,255,255))
            screen.blit(win,(160,400))
            pygame.display.update()
            k = 1
            sleep(1.5)
            print("本次用时:"+str(time1)+"秒")
            try:
                with open("time.pickle","rb") as f:
                    text = load(f)
                    text.append(time1)
                    print("最高记录"+str(min(text))+"秒")
            except:
                text = [time1]
                with open("time.pickle","wb") as f:
                    dump(text,f)
            break
        for event in pygame.event.get():
            if event.type ==  pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if ma[sum1-column] == 0:
                        sum1 -= column
                        ma[sum1] = 2
                    if ma[sum1-column] == 2:
                        ma[sum1] = 0
                        sum1 -= column
                if event.key == pygame.K_DOWN:
                    try:
                        if ma[sum1+column] == 0:
                            sum1 += column
                            ma[sum1] = 2
                        if ma[sum1+column] == 2:
                            ma[sum1] = 0
                            sum1 += column
                    except IndexError:
                        screen.fill((255,255,255))
                        screen.blit(idea5,(160,400))
                        pygame.display.update()
                        sleep(1.5)
                        break
                if event.key == pygame.K_LEFT:
                    if ma[sum1-1] == 0:
                        sum1 -= 1
                        ma[sum1] = 2
                    if ma[sum1-1] == 2:
                        ma[sum1] = 0
                        sum1 -= 1
                if event.key == pygame.K_RIGHT:
                    if ma[sum1+1] == 0 or ma[sum1+1] == 3:
                        sum1 += 1
                        ma[sum1] = 2
                        pygame.display.update()
                    if ma[sum1+1] == 2:
                        ma[sum1] = 0
                        sum1 += 1
            elif event.type == pygame.QUIT:
                break
    pygame.quit()
    if k == 1:
        return ["Victory",str(time1)]
    else:
        return ["gameover","time_out"]
def time():
    global k,time1,gameover
    while k != 1:
        if gameover != 1:
            time1 +=1
            sleep(1)
    if gameover == 1:
        time1 = "time out"
    return time1
migong()