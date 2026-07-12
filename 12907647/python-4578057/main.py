import pygame,sys,random,os,datetime,re,wx
from time import *
pygame.init()
print('游戏：大鱼吃小鱼小轩A字版。')
sleep(0.5)
print('游戏背景：')
print('你是一条爱探险、粉色的小鱼(坐着只找到这种颜色，他并不喜欢)，来到一条"和谐海"，这里的大鱼不吃小鱼，靠神秘器官生活。')
print('但，\n你要吃它们，\n否则无法生存。')
sleep(0.5)
print('刚开始，只能吃最小的小鱼，当你足够大时，能吃中鱼，更大时能吃大鱼。')
print('当你碰到石头时，会死亡(以后关卡有石头)\n如碰到比你大的鱼，也死亡。')
print('点开始后，赶紧把鼠标移到左上角，用鼠标控制移动。输了自动重来。')
sleep(0.5)
print('通关要求：\n吃了所有小鱼。')
sleep(0.5)
print('疑难解答：为什么程序响应不了？')
sleep(0.5)
print('不是你的问题，开始时如不响应，请点一下终端（右边黑色的部分→_→）。')
print('然后程序自动会最小化，先回答终端的问题（只要输入），共2个问题。')
print("回答完后程序设置为响应，那时你只要点击窗口让它出现就能开始——了！Let's go！")
sleep(1)
input('看完才能回车，否则你会后悔。')
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("大鱼吃小鱼小轩A字版")

xi_tong = input('输入你的系统：Windos或XP选1，Mac、iPhone、Mac Pro、Apple或其他选2')
hero_size = 70
guan = 0
part = 1
cl1 = 0
hero_x = -300
hero_y = -300
GoldQins = 0
while True:
    if xi_tong == '1':
        myFont = pygame.font.SysFont("kaiti", 40)
        break
    elif xi_tong == '2':
        myFont = pygame.font.SysFont(None, 40)
        break
    else:
        print('输入错误！')
        sleep(1)
        xi_tong = input('输入你的系统：Windos或XP选1    ，   Mac、iPhone、Mac Pro、Apple或其他选2')
RED = (255,0,0)
BLACK = (0,0,0)
GREEN = (0,255,0)
myText = myFont.render("大鱼吃小鱼小轩A字版", 1, BLACK)

heroImg = pygame.image.load("鱼hero.png")
heroImgs = pygame.transform.scale(heroImg, (hero_size, hero_size))


smallImg = pygame.image.load("小鱼.png")
smallImgs = pygame.transform.scale(smallImg, (50, 50))


middleImg = pygame.image.load("中鱼.png")
middleImgs = pygame.transform.scale(middleImg, (140, 140))


bigImg = pygame.image.load("大鱼.png")
bigImgs = pygame.transform.scale(bigImg, (180, 180))


getshangImg = pygame.image.load("商店.png")
getshangImgs = pygame.transform.scale(getshangImg, (125, 125))
getshangRect = pygame.Rect(375, 400, 125, 125)


startImg = pygame.image.load("START1.png")
startImgs = pygame.transform.scale(startImg, (180, 65))
startRect = pygame.Rect(550, 400, 180, 50)

while True:
    QA_line_lentofun_Music_AisJhxopen = input('再输入你要的音乐：1是 芒种    ，   其他是 Monsters。')
    if QA_line_lentofun_Music_AisJhxopen == '1':
        pygame.mixer.music.load('芒种.mp3')
        pygame.mixer.music.play(-1)
        break
    else:
        pygame.mixer.music.load('monsters.mp3')
        pygame.mixer.music.play(-1)
        break
while part == 1:
    wg = 0
    wgsm = 1
    while guan == wg:
        if cl1 == 0:
            Kword = '大鱼吃小鱼小轩A字版'
        else:
            Kword = '请再来试试！！！'
        myWord = Kword
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if startRect.collidepoint(event.pos):
                    sleep(1)
                    guan = wgsm
                elif getshangRect.collidepoint(event.pos):
                    print('商店下次开发！')
                    pass
        myText = myFont.render(myWord, 1, BLACK)
        screen.fill((0,230,0))
        screen.blit(startImgs,startRect)
        screen.blit(getshangImgs,getshangRect)
        screen.blit(myText,(425,40))
        pygame.display.update()
        
    hero_size = 70
    SW = 50
    MW = 5
    BW = 2
    Kword = '第一关'
    wg = 1
    wgsm = 2
    wen = 1
    smallList = []
    middleList = []
    bigList = []
    
    for i in range(SW):
        smallRect = pygame.Rect(random.randint(100, 1100), random.randint(50, 750), 50, 50)
        smallList.append(smallRect)
    for i in range(MW):
        middleRect = pygame.Rect(random.randint(100, 1100), random.randint(50, 750), 140, 140)
        middleList.append(middleRect)
    for i in range(BW):
        bigRect = pygame.Rect(random.randint(100, 1100), random.randint(50, 750), 180, 180)
        bigList.append(bigRect)
    
    myWord = Kword

    while guan == wg:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                hero_x = event.pos[0] - hero_size/2
                hero_y = event.pos[1] - hero_size/2
        heroRect = pygame.Rect(hero_x, hero_y, hero_size, hero_size)
        for n in smallList:
            n.x += random.randint(-1,3)
            if n.top < 0:
                n.top = 0
            if n.bottom > 800:
                n.bottom = 800
            if n.left < 0:
                n.left = 0
            if n.right > 1200:
                n.right = 0
            if heroRect.colliderect(n):    
                smallList.remove(n)
                print("吃掉了！")
                GoldQins += 1
                hero_size += 5
                heroImgs = pygame.transform.scale(heroImg, (hero_size, hero_size))
                if smallList == []:
                    print('胜利！')
                    myWord = '胜利！'
                    sleep(1)
                    guan = wgsm
                    part = wen
        for i in middleList:
            i.x += random.randint(-1,2)
            if i.top < 0:
                i.top = 0
            if i.bottom > 800:
                i.bottom = 800
            if i.left < 0:
                i.left = 0
            if i.right > 1200:
                i.right = 0
            if heroRect.colliderect(i):
                if hero_size*hero_size >= 140*140:
                    middleList.remove(i)
                    print("吃掉了！")
                    GoldQins += 1
                    hero_size += 12
                    heroImgs = pygame.transform.scale(heroImg, (hero_size, hero_size))
                elif hero_size*hero_size < 140*140:
                    print("KO！")
                    myWord = 'KO!'
                    sleep(1)
                    cl1 += 1
                    guan = 0
        for x in bigList:
            x.x += random.randint(-1,1)
            if x.top < 0:
                x.top = 0
            if x.bottom > 800:
                x.bottom = 800
            if x.left < 0:
                x.left = 0
            if x.right > 1200:
                x.right = 0
            if heroRect.colliderect(x):
                if hero_size*hero_size >= 180*180:
                    bigList.remove(x)
                    print("吃掉了！")
                    GoldQins += 1
                    hero_size += 40
                    heroImgs = pygame.transform.scale(heroImg, (hero_size, hero_size))
                elif hero_size*hero_size < 180*180:
                    print("KO！")
                    myWord = 'KO!'
                    sleep(1)
                    cl1 += 1
                    guan = 0
        screen.fill((0, 100, 250))
        screen.blit(heroImgs, heroRect)
        for rects in smallList:
            screen.blit(smallImgs, rects)
        for rectm in middleList:
            screen.blit(middleImgs, rectm)
        for rectb in bigList:
            screen.blit(bigImgs, rectb)
        myText = myFont.render(myWord, 1, GREEN)
        screen.blit(myText,(570,40))
        pygame.display.update()
    
    hero_size = 70
    SW = 100
    MW = 10
    BW = 3
    Kword = '第二关'
    wg = 2
    wgsm = 3
    wen = 1
    smallList = []
    middleList = []
    bigList = []
    
    for i in range(SW):
        smallRect = pygame.Rect(random.randint(100, 1100), random.randint(50, 750), 50, 50)
        smallList.append(smallRect)
    for i in range(MW):
        middleRect = pygame.Rect(random.randint(100, 1100), random.randint(50, 750), 140, 140)
        middleList.append(middleRect)
    for i in range(BW):
        bigRect = pygame.Rect(random.randint(100, 1100), random.randint(50, 750), 180, 180)
        bigList.append(bigRect)
    
    myWord = Kword

    while guan == wg:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                hero_x = event.pos[0] - hero_size/2
                hero_y = event.pos[1] - hero_size/2
        heroRect = pygame.Rect(hero_x, hero_y, hero_size, hero_size)
        for n in smallList:
            n.x += random.randint(-1,3)
            if n.top < 0:
                n.top = 0
            if n.bottom > 800:
                n.bottom = 800
            if n.left < 0:
                n.left = 0
            if n.right > 1200:
                n.right = 0
            if heroRect.colliderect(n):    
                smallList.remove(n)
                print("吃掉了！")
                GoldQins += 1
                hero_size += 5
                heroImgs = pygame.transform.scale(heroImg, (hero_size, hero_size))
                if smallList == []:
                    print('胜利！')
                    myWord = '胜利！'
                    sleep(1)
                    guan = wgsm
                    part = wen
        for i in middleList:
            i.x += random.randint(-1,2)
            if i.top < 0:
                i.top = 0
            if i.bottom > 800:
                i.bottom = 800
            if i.left < 0:
                i.left = 0
            if i.right > 1200:
                i.right = 0
            if heroRect.colliderect(i):
                if hero_size*hero_size >= 140*140:
                    middleList.remove(i)
                    print("吃掉了！")
                    GoldQins += 1
                    hero_size += 12
                    heroImgs = pygame.transform.scale(heroImg, (hero_size, hero_size))
                elif hero_size*hero_size < 140*140:
                    print("KO！")
                    myWord = 'KO!'
                    sleep(1)
                    cl1 += 1
                    guan = 0
        for x in bigList:
            x.x += random.randint(-1,1)
            if x.top < 0:
                x.top = 0
            if x.bottom > 800:
                x.bottom = 800
            if x.left < 0:
                x.left = 0
            if x.right > 1200:
                x.right = 0
            if heroRect.colliderect(x):
                if hero_size*hero_size >= 180*180:
                    bigList.remove(x)
                    print("吃掉了！")
                    GoldQins += 1
                    hero_size += 40
                    heroImgs = pygame.transform.scale(heroImg, (hero_size, hero_size))
                elif hero_size*hero_size < 180*180:
                    print("KO！")
                    myWord = 'KO!'
                    sleep(1)
                    cl1 += 1
                    guan = 0
        screen.fill((0, 100, 250))
        screen.blit(heroImgs, heroRect)
        for rects in smallList:
            screen.blit(smallImgs, rects)
        for rectm in middleList:
            screen.blit(middleImgs, rectm)
        for rectb in bigList:
            screen.blit(bigImgs, rectb)
        myText = myFont.render(myWord, 1, GREEN)
        screen.blit(myText,(570,40))
        pygame.display.update()
    
    hero_size = 70
    SW = 80
    MW = 5
    BW = 5
    Kword = '第三关'
    wg = 3
    wgsm = 4
    wen = 1
    smallList = []
    middleList = []
    bigList = []
    
    for i in range(SW):
        smallRect = pygame.Rect(random.randint(100, 1100), random.randint(50, 750), 50, 50)
        smallList.append(smallRect)
    for i in range(MW):
        middleRect = pygame.Rect(random.randint(100, 1100), random.randint(50, 750), 140, 140)
        middleList.append(middleRect)
    for i in range(BW):
        bigRect = pygame.Rect(random.randint(100, 1100), random.randint(50, 750), 180, 180)
        bigList.append(bigRect)
    
    myWord = Kword

    while guan == wg:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                hero_x = event.pos[0] - hero_size/2
                hero_y = event.pos[1] - hero_size/2
        heroRect = pygame.Rect(hero_x, hero_y, hero_size, hero_size)
        for n in smallList:
            n.x += random.randint(-1,3)
            if n.top < 0:
                n.top = 0
            if n.bottom > 800:
                n.bottom = 800
            if n.left < 0:
                n.left = 0
            if n.right > 1200:
                n.right = 0
            if heroRect.colliderect(n):    
                smallList.remove(n)
                print("吃掉了！")
                GoldQins += 1
                hero_size += 5
                heroImgs = pygame.transform.scale(heroImg, (hero_size, hero_size))
                if smallList == []:
                    print('胜利！')
                    myWord = '胜利！'
                    sleep(1)
                    guan = wgsm
                    part = wen
        for i in middleList:
            i.x += random.randint(-1,2)
            if i.top < 0:
                i.top = 0
            if i.bottom > 800:
                i.bottom = 800
            if i.left < 0:
                i.left = 0
            if i.right > 1200:
                i.right = 0
            if heroRect.colliderect(i):
                if hero_size*hero_size >= 140*140:
                    middleList.remove(i)
                    print("吃掉了！")
                    GoldQins += 1
                    hero_size += 12
                    heroImgs = pygame.transform.scale(heroImg, (hero_size, hero_size))
                elif hero_size*hero_size < 140*140:
                    print("KO！")
                    myWord = 'KO!'
                    sleep(1)
                    cl1 += 1
                    guan = 0
        for x in bigList:
            x.x += random.randint(-1,1)
            if x.top < 0:
                x.top = 0
            if x.bottom > 800:
                x.bottom = 800
            if x.left < 0:
                x.left = 0
            if x.right > 1200:
                x.right = 0
            if heroRect.colliderect(x):
                if hero_size*hero_size >= 180*180:
                    bigList.remove(x)
                    print("吃掉了！")
                    GoldQins += 1
                    hero_size += 40
                    heroImgs = pygame.transform.scale(heroImg, (hero_size, hero_size))
                elif hero_size*hero_size < 180*180:
                    print("KO！")
                    myWord = 'KO!'
                    sleep(1)
                    cl1 += 1
                    guan = 0
        screen.fill((0, 100, 250))
        screen.blit(heroImgs, heroRect)
        for rects in smallList:
            screen.blit(smallImgs, rects)
        for rectm in middleList:
            screen.blit(middleImgs, rectm)
        for rectb in bigList:
            screen.blit(bigImgs, rectb)
        myText = myFont.render(myWord, 1, GREEN)
        screen.blit(myText,(570,40))
        pygame.display.update()
    
    hero_size = 70
    SW = 80
    MW = 10
    BW = 5
    Kword = '第四关'
    wg = 4
    wgsm = 5
    wen = 1
    smallList = []
    middleList = []
    bigList = []
    
    for i in range(SW):
        smallRect = pygame.Rect(random.randint(100, 1100), random.randint(50, 750), 50, 50)
        smallList.append(smallRect)
    for i in range(MW):
        middleRect = pygame.Rect(random.randint(100, 1100), random.randint(50, 750), 140, 140)
        middleList.append(middleRect)
    for i in range(BW):
        bigRect = pygame.Rect(random.randint(100, 1100), random.randint(50, 750), 180, 180)
        bigList.append(bigRect)
    
    myWord = Kword

    while guan == wg:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                hero_x = event.pos[0] - hero_size/2
                hero_y = event.pos[1] - hero_size/2
        heroRect = pygame.Rect(hero_x, hero_y, hero_size, hero_size)
        for n in smallList:
            n.x += random.randint(-1,3)
            if n.top < 0:
                n.top = 0
            if n.bottom > 800:
                n.bottom = 800
            if n.left < 0:
                n.left = 0
            if n.right > 1200:
                n.right = 0
            if heroRect.colliderect(n):    
                smallList.remove(n)
                print("吃掉了！")
                GoldQins += 1
                hero_size += 5
                heroImgs = pygame.transform.scale(heroImg, (hero_size, hero_size))
                if smallList == []:
                    print('胜利！')
                    myWord = '胜利！'
                    sleep(1)
                    guan = wgsm
                    part = wen
        for i in middleList:
            i.x += random.randint(-1,2)
            if i.top < 0:
                i.top = 0
            if i.bottom > 800:
                i.bottom = 800
            if i.left < 0:
                i.left = 0
            if i.right > 1200:
                i.right = 0
            if heroRect.colliderect(i):
                if hero_size*hero_size >= 140*140:
                    middleList.remove(i)
                    print("吃掉了！")
                    GoldQins += 1
                    hero_size += 12
                    heroImgs = pygame.transform.scale(heroImg, (hero_size, hero_size))
                elif hero_size*hero_size < 140*140:
                    print("KO！")
                    myWord = 'KO!'
                    sleep(1)
                    cl1 += 1
                    guan = 0
        for x in bigList:
            x.x += random.randint(-1,1)
            if x.top < 0:
                x.top = 0
            if x.bottom > 800:
                x.bottom = 800
            if x.left < 0:
                x.left = 0
            if x.right > 1200:
                x.right = 0
            if heroRect.colliderect(x):
                if hero_size*hero_size >= 180*180:
                    bigList.remove(x)
                    print("吃掉了！")
                    GoldQins += 1
                    hero_size += 40
                    heroImgs = pygame.transform.scale(heroImg, (hero_size, hero_size))
                elif hero_size*hero_size < 180*180:
                    print("KO！")
                    myWord = 'KO!'
                    sleep(1)
                    cl1 += 1
                    guan = 0
        screen.fill((0, 100, 250))
        screen.blit(heroImgs, heroRect)
        for rects in smallList:
            screen.blit(smallImgs, rects)
        for rectm in middleList:
            screen.blit(middleImgs, rectm)
        for rectb in bigList:
            screen.blit(bigImgs, rectb)
        myText = myFont.render(myWord, 1, GREEN)
        screen.blit(myText,(570,40))
        pygame.display.update()
    
    hero_size = 70
    SW = 100
    MW = 20
    BW = 10
    Kword = '第五关'
    wg = 5
    wgsm = 0
    wen = 1
    smallList = []
    middleList = []
    bigList = []
    
    for i in range(SW):
        smallRect = pygame.Rect(random.randint(100, 1100), random.randint(50, 750), 50, 50)
        smallList.append(smallRect)
    for i in range(MW):
        middleRect = pygame.Rect(random.randint(100, 1100), random.randint(50, 750), 140, 140)
        middleList.append(middleRect)
    for i in range(BW):
        bigRect = pygame.Rect(random.randint(100, 1100), random.randint(50, 750), 180, 180)
        bigList.append(bigRect)
    
    myWord = Kword

    while guan == wg:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                hero_x = event.pos[0] - hero_size/2
                hero_y = event.pos[1] - hero_size/2
        heroRect = pygame.Rect(hero_x, hero_y, hero_size, hero_size)
        for n in smallList:
            n.x += random.randint(-1,3)
            if n.top < 0:
                n.top = 0
            if n.bottom > 800:
                n.bottom = 800
            if n.left < 0:
                n.left = 0
            if n.right > 1200:
                n.right = 0
            if heroRect.colliderect(n):    
                smallList.remove(n)
                print("吃掉了！")
                GoldQins += 1
                hero_size += 5
                heroImgs = pygame.transform.scale(heroImg, (hero_size, hero_size))
                if smallList == []:
                    print('胜利！')
                    myWord = '胜利！'
                    sleep(1)
                    guan = wgsm
                    part = wen
        for i in middleList:
            i.x += random.randint(-1,2)
            if i.top < 0:
                i.top = 0
            if i.bottom > 800:
                i.bottom = 800
            if i.left < 0:
                i.left = 0
            if i.right > 1200:
                i.right = 0
            if heroRect.colliderect(i):
                if hero_size*hero_size >= 140*140:
                    middleList.remove(i)
                    print("吃掉了！")
                    GoldQins += 1
                    hero_size += 12
                    heroImgs = pygame.transform.scale(heroImg, (hero_size, hero_size))
                elif hero_size*hero_size < 140*140:
                    print("KO！")
                    myWord = 'KO!'
                    sleep(1)
                    cl1 += 1
                    guan = 0
        for x in bigList:
            x.x += random.randint(-1,1)
            if x.top < 0:
                x.top = 0
            if x.bottom > 800:
                x.bottom = 800
            if x.left < 0:
                x.left = 0
            if x.right > 1200:
                x.right = 0
            if heroRect.colliderect(x):
                if hero_size*hero_size >= 180*180:
                    bigList.remove(x)
                    print("吃掉了！")
                    GoldQins += 1
                    hero_size += 40
                    heroImgs = pygame.transform.scale(heroImg, (hero_size, hero_size))
                elif hero_size*hero_size < 180*180:
                    print("KO！")
                    myWord = 'KO!'
                    sleep(1)
                    cl1 += 1
                    guan = 0
        screen.fill((0, 100, 250))
        screen.blit(heroImgs, heroRect)
        for rects in smallList:
            screen.blit(smallImgs, rects)
        for rectm in middleList:
            screen.blit(middleImgs, rectm)
        for rectb in bigList:
            screen.blit(bigImgs, rectb)
        myText = myFont.render(myWord, 1, GREEN)
        screen.blit(myText,(570,40))
        pygame.display.update()
    print('你的金币数：',GoldQins)