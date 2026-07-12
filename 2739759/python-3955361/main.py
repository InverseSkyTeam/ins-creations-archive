import pygame, sys, random, time
t1 = time.time()
a = 1
b = 5
t = 0
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("消灭新型冠状病毒！！！")
bgImg = pygame.image.load('室内.png')
bgImg = pygame.transform.scale(bgImg,(800,600))
gunImg = pygame.image.load('喷瓶1.png')
gunImg = pygame.transform.scale(gunImg,(100,100))
gunImg2 = pygame.image.load('喷瓶2.png')
gunImg2 = pygame.transform.scale(gunImg2,(200,100))
enemyImg = pygame.image.load('病毒.png')
enemyImg = pygame.transform.scale(enemyImg,(100,100))
gameoverImg = pygame.image.load('失败.png')
gameoverImg = pygame.transform.scale(gameoverImg,(800,600))
enemyX = 0
enemyY = 0
enemyRect = pygame.Rect(enemyX, enemyY, 100 ,100)
gunRect = pygame.Rect(0, 0, 100,100)
num = 0  # 击中敌人数量
pygame.mixer.music.load("希望.mp3")
pygame.mixer.music.play(-1)
gunSound = pygame.mixer.Sound("掉落.wav")
print("""\033[1;32m抵制不良游戏，杜绝盗版游戏
适度游戏健脑，沉迷游戏伤身
提示：
长按鼠标可以暂停病毒的移动""")
while True:
    screen.blit(bgImg, (0, 0))
    myWord = "勇士，欢迎您。由于人类捕杀蝙蝠导致一种新型冠状病毒出现，"
    myFont = pygame.font.SysFont("kaiti", 25)
    myNum = myFont.render(myWord, True, (255, 0, 0))
    screen.blit(myNum, (0, 140)) 
    myWord1 = "你需要用鼠标控制喷壶移动喷出酒精，在病毒逃出房间前杀死病毒"
    myNum1 = myFont.render(myWord1, True, (255, 0, 0)) 
    screen.blit(myNum1, (0, 170))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            x = event.pos[0]
            y = event.pos[1]
            gunRect.center = (x, y)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            screen.blit(gunImg2, gunRect)  
            pygame.display.update()
            if enemyRect.collidepoint(event.pos):
                gunSound.play()
                num = num + 1
                myWord = "杀灭病毒数:" + str(num)
                myFont = pygame.font.SysFont("kaiti", 30)
                myNum = myFont.render(myWord, True, (255, 0, 0))
                enemyX = random.randint(0, 200)
                enemyY = random.randint(0, 400)
                time.sleep(1)
    # 敌人移动    
        enemyX = enemyX + random.randint(a, b)
    if t < 40:
        a = 1
        b = 5
    elif t>=40:
        myWord1 = "感受病毒王的愤怒吧！！！"
        myNum1 = myFont.render(myWord1, True, (255, 0, 0))
        screen.blit(myNum1, (0, 200)) 
        a = 15
        b = 25
    elif t >= 60:
        screen.blit(gameoverImg, (0, 0))
        myWord1 = "一分钟内你杀死了"+str(num)+"个病毒"
        myNum1 = myFont.render(myWord1, True, (255, 0, 0))
        screen.blit(myNum1, (0, 300)) 
        print(myWord)
        pygame.time.delay(7000)
        pygame.quit()
        sys.exit()
    # 绘制相关元素
    enemyRect = pygame.Rect(enemyX, enemyY, 200, 200)
    screen.blit(enemyImg, enemyRect)
    screen.blit(gunImg, gunRect)
    myNum = myFont.render(myWord, True, (255, 0, 0))
    if t < 0 or enemyX > 800:
        myWord1 = "一分钟内你杀死了"+str(num)+"个病毒"
        myNum1 = myFont.render(myWord1, True, (255, 0, 0))
        screen.blit(myNum1, (0, 300)) 
        print(myWord1)
        screen.blit(gameoverImg, (0, 0))
        pygame.time.delay(7000)
        pygame.quit()
        sys.exit()
    t2 = time.time()
    t = t2-t1
    pygame.display.update()