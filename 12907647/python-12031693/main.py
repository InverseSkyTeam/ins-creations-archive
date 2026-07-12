# 导库
import pygame,sys,os,tkinter as tk,random
from tkinter import messagebox as mbox
from time import *
from jhxFast import *
# 解说
pt('草稿：建立游戏1行代码',0.2)
pt('草稿2：建立游戏库')
pt('草稿3：建立游戏素材，其他')
pt('草稿4：建立加载图片算法')
pt('草稿5：迭代加载图片')
pt('草稿6：提纲+pygame+变量名+加载素材+加载条',1)
pt('草稿7：迭代加载图片、加载条+部分1')
pt('草稿8：迭代加载图片、加载条+总while，part2',1)
pt('游戏草稿：虚化背景、按钮+按钮点击')
pt('游戏草稿2：迭代按钮点击+绳子+字典items遍历+鼠标事件总会1',1.5)
pt('游戏草稿3：tkinter现身，os准备，tk按钮颜色和文字、函数',1.2)
pt('游戏草稿4：整体优化，出现这个解说')
pt('游戏草稿5：整体优化，第一关初始')
pt('游戏草稿6（保卫家园+植物大战僵尸+文明城市V0.0.1）：第一关完成',2)
pt('保卫家园V0.0.2：第二关完成')
pt('保卫家园V0.0.3：第三关完成')
pt('[本版]保卫家园V0.0.4：第四关完成')
pt('期待 保卫家园+植物大战僵尸+文明城市V0.0.5 的更新！')
# pygame初始化
pygame.init()
screen = pygame.display.set_mode((1200,800))
pygame.display.set_caption("我的作品")
bgImg = pygame.image.load("开始背景.png")
Falsification_bg = pygame.image.load("开始背景.png").convert()
Falsification_bg.set_alpha(40)

# 麻烦的东西,图片加载算法
Outside_main_buttons = [pygame.image.load("得分.png"),pygame.image.load("其他作品.png"),pygame.image.load("普通游戏.png")]

for i in range(len(Outside_main_buttons)):
    Outside_main_buttons[i] = pygame.transform.scale(Outside_main_buttons[i],(400,100))

Outside_main_buttons_rect = [pygame.image.load("得分.png"),pygame.image.load("其他作品.png"),pygame.image.load("普通游戏.png")]

for i in range(len(Outside_main_buttons_rect)):
    Outside_main_buttons[i] = pygame.transform.scale(Outside_main_buttons[i],(400,100))

for i in range(len(Outside_main_buttons_rect)):
    a = pygame.Rect(0,0,400,100)
    a.y = i*200+100
    a.x = 400
    Outside_main_buttons_rect[i] = a

Outside_main_buttons_dict = {}

for i in range(len(Outside_main_buttons)):
    for j in range(len(Outside_main_buttons_rect)):
        if i == j:
            Outside_main_buttons_dict[Outside_main_buttons[i]] = Outside_main_buttons_rect[j]

del Outside_main_buttons,Outside_main_buttons_rect
# 好了，OK了，这个鬼,下面弄个绳子
rope = pygame.Rect(450,0,25,500)
rope2 = pygame.Rect(725,0,25,500)

startImg = pygame.image.load("START1.png")
startRect = startImg.get_rect()
startRect.x = 500
startRect.y = 700

dian1 = pygame.image.load("点我1.png")
dian2 = pygame.image.load("点我2.png")
dian3 = pygame.image.load("点我3.png")
dian4 = pygame.image.load("点我4.png")
dr1 = dian1.get_rect()
dr2 = dian2.get_rect()
dr3 = dian3.get_rect()
dr4 = dian4.get_rect()

hand = pygame.image.load("手.png")
handR = hand.get_rect()
bao666 = pygame.image.load("宝石.png")
baohowmany666 = 0
bao666RList = []
for i in range(3):
    bao666R = bao666.get_rect()
    bao666R.x = random.randint(0, 1000)
    bao666R.y = random.randint(-400, -100)
    bao666RList.append(bao666R)

# 音效
dading2last_V = pygame.mixer.Sound('机灵.wav')

# 系统字体
try:import ntpath
except:osingxing = 'MacOs';font = pygame.font.SysFont('kaittf', 30);font2 = pygame.font.SysFont('kaittf', 20)
else:osingxing = 'Windows';font = pygame.font.SysFont('kaiti', 30);font2 = pygame.font.SysFont('kaiti', 20);del ntpath


load_times_a3pbm_0624 = 0 # 加载时的加载条加载次数，编号24
level = 1 # 等级
notUse = 0 # 垃圾
part = '开始' # 程序部分，减少缩进
Gold1 = 0
enemylife1 = 500
mylife1 = 500
guan2_collide = 0
mPos = (0,0)

计数器a = 0





# 万事俱备，开启while True!
while True:
    while part == '开始':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if startRect.collidepoint(event.pos):
                    part = '加载'
        screen.fill((255,255,255))
        screen.blit(bgImg,(0,0))
        screen.blit(startImg,startRect)
        pygame.display.update()
    
    # load
    while part == '加载':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if load_times_a3pbm_0624 >= 3:
            part = '主页'
        # 主要算法
        for i in range(20):
            screen.fill((255,255,255))
            screen.blit(Falsification_bg,(0,0))
            screen.blit(font.render((' '*19),True,(100,100,100),(100,100,100)),(400,50))
            screen.blit(font.render((' '*i),True,(0,255,255),(0,255,255)),(400,50))
            screen.blit(font.render(('正在玩命加载中'+'.'*(i%6)),True,(0,140,255)),(400,100))
            screen.blit(font.render(('%'+str(i*5)+' '*4+str(load_times_a3pbm_0624+1)+'/4'),True,(0,100,255)),(400,150))
            screen.blit(font.render(('加载'+random.choice(["服务器","数据包","素材","代码","堆栈","库","游戏资料","上传运行","机器识别","人工智能",'抽取资料','安全防护'])),True,(0,255,255)),(400,200))
            sleep(0.07)
            if i == 6:
                sleep(0.06)
            if i == 17:
                sleep(0.1)
            if i == 19:
                sleep(0.04)
            pygame.display.update()
        load_times_a3pbm_0624 += 1
    
    # 游戏主页
    while part == '主页':
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # 我严重怀疑这是一个累赘
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in Outside_main_buttons_dict: # 检测按钮，弹出tk
                    计数器a += 1
                    if 计数器a == 3:
                        if Outside_main_buttons_dict[i].collidepoint(event.pos):
                            root = tk.Tk()
                            root.geometry('300x400')
                            root.title('|宇宙|保卫家园-选关')
                            def Game1():
                                global part,timed1
                                part = '第一关'
                                timed1 = time()
                                root.destroy()
                            def Game2():
                                global part,guan2_collide
                                guan2_collide = 0
                                part = '第二关'
                                root.destroy()
                            def Game3():
                                global part,guan2_collide
                                guan2_collide = 0
                                part = '第三关'
                                root.destroy()
                            def Game4():
                                global part,baohowmany666,timed1,mPos
                                baohowmany666 = 0
                                mPos = (0,0)
                                timed1 = time()
                                part = '第四关'
                                root.destroy()
                            b1 = tk.Button(root,text='第一关',command=Game1)
                            b1.pack()
                            b2 = tk.Button(root,text='第二关',bg='skyblue',command=Game2)
                            b2.pack()
                            b3 = tk.Button(root,text='第三关',bg='blue',command=Game3)
                            b3.pack()
                            b4 = tk.Button(root,text='第四关',bg='green',command=Game4)
                            b4.pack()
                            root.mainloop()
                        计数器a = 0
        screen.fill((30,255,255))
        pygame.draw.rect(screen, (255,150,120), rope, 0)
        pygame.draw.rect(screen, (0,255,40), rope2, 0)
        for i in Outside_main_buttons_dict.items():
            screen.blit(i[0],i[1])
        screen.blit(font.render((str(level)),True,(255,0,0)),(525,130))
        screen.blit(font.render(str(notUse),True,(0,0,255)),(725,130))
        screen.blit(font.render("小程序，大算法，无敌有趣！",True,(0,150,0)),(400,600))
        pygame.display.update()
    
    while part == '第一关':
        timed2 = time()-timed1
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # 这绝对是一个。。。
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == ord('1'):
                    if Gold1 >= 2000:
                        enemylife1 -= 1
                        Gold1 -= 2000
                if event.key == ord('2'):
                    if Gold1 >= 6000:
                        enemylife1 -= 11
                        Gold1 -= 6000
                if event.key == ord('3'):
                    if Gold1 >= 10000:
                        enemylife1 -= 30
                        Gold1 -= 10000
                if event.key == ord('4'):
                    if Gold1 >= 15000:
                        enemylife1 -= 50
                        Gold1 -= 15000
        if timed2 >= 0.1:
            timed1 = timed2
            Gold1 += 10
            mylife1 -= 0.025
        if enemylife1 <= 0:
            notUse += 10
            enemylife1 = 500
            mylife1 = 500
            part = '主页'
        if mylife1 <= 0:
            enemylife1 = 500
            mylife1 = 500
            part = '主页'
        screen.fill((255,255,255))
        screen.blit(font.render('金币数:'+str(Gold1),True,(0,0,255)),(10,10))
        screen.blit(font.render('我方血量:'+str(int(mylife1)),True,(255,0,0)),(10,50))
        screen.blit(font.render('敌方血量:'+str(enemylife1),True,(255,0,0)),(10,90))
        screen.blit(font.render('按下1键，扣2000金币，敌方血量-1',True,(0,255,0)),(10,130))
        screen.blit(font.render('按下2键，扣6000金币，敌方血量-11',True,(0,255,0)),(10,170))
        screen.blit(font.render('按下3键，扣10000金币，敌方血量-30',True,(0,255,0)),(10,210))
        screen.blit(font.render('按下4键，扣15000金币，敌方血量-50',True,(0,255,0)),(10,250))
        screen.blit(font.render('快打！',True,(0,0,0)),(10,290))
        pygame.display.update()
    
    while part == '第二关':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if dr1.collidepoint(event.pos):
                    guan2_collide += 1
                    dading2last_V.play()
                    break
                if dr2.collidepoint(event.pos):
                    guan2_collide += 1
                    dading2last_V.play()
                    break
                if dr3.collidepoint(event.pos):
                    guan2_collide += 1
                    dading2last_V.play()
                    break
                if dr4.collidepoint(event.pos):
                    guan2_collide += 1
                    dading2last_V.play()
                    break
        screen.fill((0,255,255))
        if guan2_collide <= 20:
            screen.blit(dian1,dr1)
        if guan2_collide > 20 and guan2_collide <= 30:
            screen.blit(dian2,dr2)
        if guan2_collide > 30 and guan2_collide <= 60:
            screen.blit(dian3,dr3)
        if guan2_collide > 60 and guan2_collide <= 70:
            screen.blit(dian4,dr4)
        if guan2_collide > 70:
            notUse += 25
            part = '主页'
        pygame.display.update()
    
    while part == '第三关':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if dr1.collidepoint(event.pos):
                    guan2_collide += 1
                    dading2last_V.play()
                    break
                if dr2.collidepoint(event.pos):
                    guan2_collide += 1
                    dading2last_V.play()
                    break
                if dr3.collidepoint(event.pos):
                    guan2_collide += 1
                    dading2last_V.play()
                    break
                if dr4.collidepoint(event.pos):
                    guan2_collide += 1
                    dading2last_V.play()
                    break
        screen.fill((0,255,255))
        if guan2_collide <= 30:
            screen.blit(dian1,dr1)
        if guan2_collide > 30 and guan2_collide <= 50:
            screen.blit(dian2,dr2)
        if guan2_collide > 50 and guan2_collide <= 70:
            screen.blit(dian3,dr3)
        if guan2_collide > 70 and guan2_collide <= 80:
            screen.blit(dian4,dr4)
        if guan2_collide > 80:
            notUse += 30
            part = '主页'
        pygame.display.update()
    
    while part == '第四关':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                mPos = event.pos
        timed2 = time()-timed1
        screen.fill((60,120,208))
        handR.x = mPos[0]
        handR.y = mPos[1]
        screen.blit(hand,handR)
        for n in bao666RList:
            n.y += 1
            if n.y > 600:
                n.y = random.randint(-400,-100)
            elif n.colliderect(handR):
                baohowmany666 += 1
                n.y = random.randint(-400,-100)
            screen.blit(bao666,n)
        if timed2 >= 20:
            notUse += baohowmany666
            part = '主页'
        pygame.display.update()