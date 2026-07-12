import pygame,sys,random
from time import *
print('游戏：大鱼吃小鱼小轩A字版。')
sleep(1)
print('游戏背景：')
sleep(1)
print('你是一条爱探险、粉色的小鱼，来到一条"和谐海"，这里的大鱼不吃小鱼，靠神秘器官生活。')
sleep(1)
print('但，\n你要吃它们，\n否则无法生存。')
sleep(1)
print('刚开始，只能吃最小的小鱼，当你足够大时，能吃中鱼，更大时能吃大鱼。')
sleep(1)
print('当你碰到石头时，会死亡(以后关卡有石头)\n如碰到比你大的鱼，也死亡。')
sleep(1)
print('点开始后，赶紧把鼠标移到左上角，用鼠标控制移动。')
sleep(1)
print('通关要求：\n第一关：吃了所有小鱼。')
sleep(1)
pygame.init()

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("大鱼吃小鱼小轩A字版")

hero_size = 70
guan = 0
hero_x = -300
hero_y = -300
myFont = pygame.font.SysFont("kaiti", 40)
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
startImgs = pygame.image.load("START.png")
startRect = pygame.Rect(550, 400, 180, 50)

smallList = []
middleList = []
bigList = []

for i in range(50):
    smallRect = pygame.Rect(random.randint(100, 1100), random.randint(50, 750), 50, 50)
    smallList.append(smallRect)
for i in range(5):
    middleRect = pygame.Rect(random.randint(100, 1100), random.randint(50, 750), 140, 140)
    middleList.append(middleRect)
for i in range(2):
    bigRect = pygame.Rect(random.randint(100, 1100), random.randint(50, 750), 180, 180)
    bigList.append(bigRect)

while guan == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if startRect.collidepoint(event.pos):
                sleep(1)
                guan = 1
    screen.fill((0,230,0))
    screen.blit(startImgs,startRect)
    screen.blit(myText,(425,40))
    pygame.display.update()

myWord = '第一关'

while guan == 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            hero_x = event.pos[0]
            hero_y = event.pos[1]
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
            hero_size += 5
            heroImgs = pygame.transform.scale(heroImg, (hero_size, hero_size))
            if smallList == []:
                print('胜利！')
                myWord = '胜利！'
                sleep(1)
                guan = 2
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
                hero_size += 12
                heroImgs = pygame.transform.scale(heroImg, (hero_size, hero_size))
            elif hero_size*hero_size < 140*140:
                print("KO！")
                myWord = 'KO!'
                sleep(1)
                pygame.quit()
                sys.exit()
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
                hero_size += 40
                heroImgs = pygame.transform.scale(heroImg, (hero_size, hero_size))
            elif hero_size*hero_size < 180*180:
                print("KO！")
                pygame.quit()
                sys.exit()
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
