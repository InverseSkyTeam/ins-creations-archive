
import pygame, sys, random,time
#2021除旧鼠迎新牛1.3.5
pygame.init()
screen = pygame.display.set_mode((650, 660))
pygame.display.set_caption("2021除旧鼠迎新牛")
bgImg0= pygame.image.load('bg.png')
bgImg=pygame.transform.scale(bgImg0,(650,660))
handImg0= pygame.image.load('hand1.png')
handImg=pygame.transform.scale(handImg0,(100,80))
hongbaoImg0= pygame.image.load('牛牛.png')
hongbaoImg=pygame.transform.scale(hongbaoImg0,(60,60))
hongbaoImg1= pygame.image.load('牛.png')
hongbaoImg3=pygame.transform.scale(hongbaoImg1,(60,60))
ziImg1= pygame.image.load('鼠.png')
ziImg=pygame.transform.scale(ziImg1,(60,60))
success=pygame.mixer.Sound("success.wav")
fail=pygame.mixer.Sound("fail.wav")
eat=pygame.mixer.Sound("eat.wav")
boom=pygame.mixer.Sound("boom.wav")
hx=215
hy=580
handRect = pygame.Rect(hx,hy, 100, 80)
score = 0
hongbaoRectList = []
hongbaoRect1List = []
ziRectList = []
speed = 2
a=1
level=1
m=50
hp=15
lm=1
myFont = pygame.font.SysFont("kaiti", 45)
myFont1 = pygame.font.SysFont("kaiti", 60)
myFont2 = pygame.font.SysFont("kaiti", 52)
myFont3 = pygame.font.SysFont("kaiti", 35)
myText1 = myFont1.render("2021除旧鼠迎新牛", True, (255, 255, 255))
myText2 = myFont2.render("任意键以开始", True, (255, 255, 255))
myText5 = myFont3.render("左右键控制手接住“牛”字", True, (255, 255, 255))
myText6 = myFont3.render("躲避“鼠”字", True, (255, 255, 255))
myText7 = myFont3.render("“牛”字没接住,牛会生气的(减命)", True, (255, 255, 255))

pygame.mixer.music.load("bgsound.mp3")
pygame.mixer.music.play(-1)
for i in range(1):
    x = random.randint(0, 570)
    y = random.randint(-400, -50)
    x1 = random.randint(0, 570)
    y1 = random.randint(-400, -50)
    x2 = random.randint(0, 570)
    y2 = random.randint(-400, -50)
    x3 = random.randint(0, 570)
    y3 = random.randint(-400, -50)
    hongbaoRect = pygame.Rect(x, y, 60, 60)
    hongbaoRectList.append(hongbaoRect)
    hongbao1Rect = pygame.Rect(x1, y1, 60, 60)
    hongbaoRectList.append(hongbao1Rect)
    hongbao2Rect = pygame.Rect(x2, y2, 60, 60)
    hongbaoRectList.append(hongbao2Rect)
    hongbao3Rect = pygame.Rect(x3, y3, 60, 60)
    hongbaoRectList.append(hongbao3Rect)
for i in range(1):
    x = random.randint(0, 570)
    y = random.randint(-400, -50)
    x1 = random.randint(0, 570)
    y1 = random.randint(-400, -50)
    x2 = random.randint(0, 570)
    y2 = random.randint(-400, -50)
    x3 = random.randint(0, 570)
    y3 = random.randint(-400, -50)
    hongbaoRect = pygame.Rect(x, y, 60, 60)
    hongbaoRect1List.append(hongbaoRect)
    hongbao1Rect = pygame.Rect(x1, y1, 60, 60)
    hongbaoRect1List.append(hongbao1Rect)
    hongbao2Rect = pygame.Rect(x2, y2, 60, 60)
    hongbaoRect1List.append(hongbao2Rect)
    hongbao3Rect = pygame.Rect(x2, y2, 60, 60)
    hongbaoRect1List.append(hongbao3Rect)
for i in range(1):
    x = random.randint(0, 570)
    y = random.randint(-400, -50)
    x1 = random.randint(0, 570)
    y1 = random.randint(-400, -50)
    x2 = random.randint(0, 570)
    y2 = random.randint(-400, -50)
    x3 = random.randint(0, 570)
    y3 = random.randint(-400, -50)
    ziRect = pygame.Rect(x, y, 60, 60)
    ziRectList.append(ziRect)
    zi1Rect = pygame.Rect(x1, y1, 60, 60)
    ziRectList.append(zi1Rect)
    zi2Rect = pygame.Rect(x2, y2, 60, 60)
    ziRectList.append(zi2Rect)
    zi3Rect = pygame.Rect(x3, y3, 60, 60)
    ziRectList.append(zi3Rect)
screen.blit(bgImg, (0, 0))

while True:
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    myText = myFont.render("score:"+str(score), True, (0, 0, 255))
    myText3 = myFont2.render("第"+str(level)+"关", True, (255, 255, 255))
    myText4= myFont.render("hp:"+str(hp), True, (0, 0, 255))
    myText8= myFont.render("level:"+str(level), True, (0, 0, 255))
    myText9 = myFont3.render("达到"+str(m)+"分进入下一关", True, (255, 255, 255))

    if a==1:


        screen.blit(myText1, (100, 110))
        screen.blit(myText2, (170, 490))
        screen.blit(myText3, (250, 425))
        screen.blit(myText5, (130, 200))
        screen.blit(myText6, (200, 260))
        screen.blit(myText7, (80, 320))
        screen.blit(myText9, (160, 380))
        random.choice(hongbaoRectList)

    if event.type!=pygame.KEYDOWN and a==1:
        continue

    a=0
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_LEFT:
            hx=hx-10

        if event.key==pygame.K_RIGHT:
            hx=hx+10

        if x>=550:
            x=550
        if x<=0:
            x=0
    handRect = pygame.Rect(hx,hy, 100, 60)

    screen.blit(bgImg, (0, 0))
    for n in hongbaoRectList:

        random.choice(hongbaoRectList)
        n.y = n.y+speed
        if n.y>600:
            n.y=random.randint(-400,-50)

        if n.colliderect(handRect):
            score=score+5
            n.y=random.randint(-300,-50)
            eat.play()
        screen.blit(hongbaoImg, n)
    for n in hongbaoRect1List:

        random.choice(hongbaoRectList)
        n.y = n.y+speed
        if n.y>600:
            n.y=random.randint(-400,-50)
            hp=hp-1
        if n.colliderect(handRect):
            score=score+5
            eat.play()
            n.y=random.randint(-300,-50)
        screen.blit(hongbaoImg3, n)
    for n in ziRectList:

        random.choice(ziRectList)
        n.y = n.y+speed
        if n.y>600:
            n.y=random.randint(-400,-50)

        if n.colliderect(handRect):
            score=score-20
            boom.play()
            n.y=random.randint(-300,-50)

        screen.blit(ziImg, n)
    if score <=0:
        score=0
    if level==lm and score>=m:
        score=0
        level=level+1
        hp=15
        a=1
        lm=lm+1
        m=m+30
        success.play()
        time.sleep(2)
        screen.fill((255,255,255))
        screen.blit(bgImg, (0, 0))
    if hp<=0:
        score=0
        level=level-1
        a=1
        hp=15
        fail.play()
        time.sleep(2)
        screen.fill((255,255,255))
        screen.blit(bgImg, (0, 0))
    screen.blit(handImg, handRect)
    if a==0:
        screen.blit(myText,(0,0))
        screen.blit(myText4, (0, 50))
        screen.blit(myText8, (0, 100))
    if level==10:
        s0= pygame.image.load('bg.png')
        s=pygame.transform.scale(s0,(650,660))
        screen.blit(s,(0,0))
        time.sleep(5)
        pygame.quit()
        sys.exit()
    if level <1:
        level=1
    time.sleep(0.001)
    pygame.display.update()
