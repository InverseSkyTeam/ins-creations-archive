import pygame,sys,random,time
heroy=480
homeworky=480
pygame.init()
screen = pygame.display.set_mode((600,600))
#图片
img = pygame.image.load("yzx.ico")
pygame.display.set_icon(img)
pygame.display.set_caption("Under The HomeWork")
bg = pygame.image.load("zuoye.jpg")
w = pygame.transform.scale(pygame.image.load("win.png"),(600,600))
f = pygame.transform.scale(pygame.image.load("fail.png"),(600,600))
bg=pygame.transform.scale(bg,(600,600)).convert()
bg.set_alpha(20)
#字体
try:
    ifont1=pygame.font.SysFont("kaiti",40)
    ifont2=pygame.font.SysFont("kaiti",30)
    ifont3=pygame.font.SysFont("kaiti",25)
except:
    ifont1=pygame.font.SysFont("kaittf",40)
    ifont2=pygame.font.SysFont("kaittf",30)
    ifont3=pygame.font.SysFont("kaittf",25)
#音乐
soundsuccess=pygame.mixer.Sound("success.wav")
soundfail=pygame.mixer.Sound("fail.wav")
soundtime=pygame.mixer.Sound("time.wav")
soundhit=pygame.mixer.Sound("boom.wav")
#字幕
itext1=ifont1.render("Under The HomeWork",True,(120,120,120))
itext2=ifont1.render("作业之下",True,(120,120,120))
itextbegin=ifont1.render("戳我开始",True,(120,120,120))
itexta=ifont2.render("按上下左右键躲避作业的攻击",True,(120,120,120))
itextb=ifont2.render("在躲避的同时 按空格键攻击作业",True,(120,120,120))
itextc=ifont2.render("在写(攻击)作业时 停止移动(玩耍)",True,(120,120,120))
itexthp=ifont2.render("h  p",True,(120,120,120))
#线条矩形
linerect1 = pygame.Rect(0, 135, 600, 5)
linerect2 = pygame.Rect(55, 135, 5, 460)
linerect3 = pygame.Rect(540, 135, 5, 460)
begin = pygame.Rect(225, 400, 160, 50)
#攻击列表
math=["math1st.png","math2nd.png","math3rd.png"]
english=["en1st.png","en2nd.png","en3rd.png"]
chinese=["ch1st.png","ch2nd.png"]
#攻击速度
mspeed=1
#BGM设置
pygame.mixer.music.load("Toby Fox - MEGALOVANIA.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
#基础变量设置
win=1
best=0
#移动变量
m_h=1
#主角类
class Hero():
    def __init__(self):
        self.hp = 480
        self.way = "left"
        self.image = pygame.transform.scale(pygame.image.load("h.png"),(75,75))
        self.rect = pygame.Rect(250, 350, 75, 75)

    def move(self, way, num):
        self.way = way
        if self.way == 'up':
            self.rect.y = self.rect.y - num -num
        elif self.way == 'down':
            self.rect.y = self.rect.y + num + num
        elif self.way == 'left':
            self.rect.x = self.rect.x - num -num
        elif self.way == 'right':
            self.rect.x = self.rect.x + num + num
        if self.rect.x<65:
            self.rect.x=65
        elif self.rect.x>465:
            self.rect.x=465
        if self.rect.y<146:
            self.rect.y=146
        elif self.rect.y>525:
            self.rect.y=525
    def show(self, screen):
        screen.blit(self.image, self.rect)
    #if self.rect.colliderect(rect):
            #self.hp-=5
#作业类
class Math():

    def __init__(self):
        self.image = pygame.transform.scale(pygame.image.load(random.choice(math)),(110,35))
        self.x=random.randrange(56,449,65)
        self.y=random.randrange(-200,115,65)
        self.rect = pygame.Rect(self.x,self.y, 110, 35)
    def show(self, screen):
        if self.rect.y>=145:
            screen.blit(self.image, self.rect)
        if self.rect.y>500:
            self.x=random.randrange(56,449,35)
            self.y=random.randrange(-160,115,35)
            self.rect = pygame.Rect(self.x,self.y, 110, 35)
            if self.rect.y>=145:
                screen.blit(self.image, self.rect)
    def move(self,num1):
        self.rect.y +=num1
    def hit(self,hero):
        if hero.rect.colliderect(self.rect):
            hero.hp-=0.17
            global heroy
            heroy-=0.17
            soundtime.play()
class Chinese():

    def __init__(self,hero):
        self.image = pygame.transform.scale(pygame.image.load(random.choice(chinese)),(600,35))
        self.x=random.randrange(-400,-220,2)
        self.y=random.choice([hero.rect.y+random.randint(40,70),hero.rect.y-random.randint(40,70)])
        self.rect = pygame.Rect(self.x,self.y, 600, 35)
    def show(self, screen):
        if self.rect.x>=65-155:
            screen.blit(self.image, self.rect)
        if self.rect.x>750:
            self.x=random.randrange(-400,-220,2)
            self.y=random.choice([hero.rect.y+random.randint(40,70),hero.rect.y-random.randint(40,70)])
            self.rect = pygame.Rect(self.x,self.y, 600, 35)
            if self.rect.x>=65-155:
                screen.blit(self.image, self.rect)
        if self.rect.y<=145:
            self.rect.y=145
    def move(self,num1):
        self.rect.x +=num1
    def hit(self,hero):
        if hero.rect.colliderect(self.rect):
            hero.hp-=0.175
            global heroy
            heroy-=0.175
            soundtime.play()
class English():

    def __init__(self):
        self.image = pygame.transform.scale(pygame.image.load(random.choice(english)),(70,70))
        self.x=random.randrange(56,449,65)
        self.y=random.randrange(-200,115,65)
        self.rect = pygame.Rect(self.x,self.y, 75, 75)
    def show(self, screen):
        if self.rect.y>=145:
            screen.blit(self.image, self.rect)
        if self.rect.y>500:
            self.x=random.randrange(56,449,35)
            self.y=random.randrange(-160,115,35)
            self.rect = pygame.Rect(self.x,self.y, 75, 75)
            if self.rect.y>=145:
                screen.blit(self.image, self.rect)
    def move(self,num1):
        self.rect.y +=num1
    def hit(self,hero):
        if hero.rect.colliderect(self.rect):
            hero.hp-=0.85
            global heroy
            heroy-=0.85
            soundtime.play()
#类初始化
hero=Hero()
mn = 4
mlist = []
cn = 1
clist = []
en=  2
elist = []
for i in range(mn):
    mlist.append(Math())
for i in range(cn):
    clist.append(Chinese(hero))
for i in range(en):
    elist.append(English())
#时间初始化
t1=round(time.time())
#状态变量和显示变量
a=0
herominus=0
homeworkminus=0
b=0
#主循环
while True:

    #血条处理
    bloodrect1 = pygame.Rect(545, 120+homeworkminus, 55,homeworky)
    bloodrect2 = pygame.Rect(0, 120+herominus, 55,heroy)
    #计时器
    t2=round(time.time())
    #血条处理
    herominus=500-heroy
    homeworkminus=500-homeworky
    heroy=500-herominus
    homeworky=500-homeworkminus
    #引导字体与矩形处理
    if a==0:
        t1=round(time.time())
        screen.fill((60,60,60))
        screen.blit(bg,(0,0))
        itext3=ifont2.render("hero hp:"+str(round(hero.hp)),True,(120,120,120))
        itext6=ifont2.render("homework hp:"+str(round(homeworky)),True,(120,120,120))
        if a==1:
            itext4=ifont2.render("time:"+str(round((t2-t1)*1)),True,(120,120,120))
        itext5=ifont2.render("best:"+str(best),True,(120,120,120))
        screen.blit(itext1,(135,50))
        screen.blit(itexta,(110,250))
        screen.blit(itextb,(80,300))
        screen.blit(itextc,(75,350))
        screen.blit(itext2,(225,90))
        screen.blit(itext3,(3,0))
        screen.blit(itext6,(370,3))
        screen.blit(itexthp,(0,100))
        screen.blit(itexthp,(540,100))
        if a==1:
            screen.blit(itext4,(5,30))
        screen.blit(itext5,(3,60))

        #划线
        pygame.draw.rect(screen,(60,60,60),linerect1,0)
        pygame.draw.rect(screen,(60,60,60),linerect2,0)
        pygame.draw.rect(screen,(60,60,60),linerect3,0)
        #血条
        pygame.draw.rect(screen,(150,60,60),bloodrect1,0)
        pygame.draw.rect(screen,(60,150,60),bloodrect2,0)
    #开始
    if a==0 and b==0:
        itextbegin=ifont1.render("戳我开始",True,(120,120,120))
        pygame.draw.rect(screen, (100,100,100), begin, 0)
        screen.blit(itextbegin,(225,403))
        itexta=ifont2.render("按上下左右键躲避作业的攻击",True,(120,120,120))
        itextb=ifont2.render("在躲避的同时 按空格键攻击作业",True,(120,120,120))
        itextc=ifont2.render("在写(攻击)作业时 停止移动(玩耍)",True,(120,120,120))
    if a==0 and b==1:
        itextbegin=ifont1.render("戳我开始",True,(190,210,220))
        pygame.draw.rect(screen,(140,190,190), begin, 0)
        screen.blit(itextbegin,(225,403))
        itexta=ifont2.render("按上下左右键躲避作业的攻击",True,(190,210,220))
        itextb=ifont2.render("在躲避的同时 按空格键攻击作业",True,(190,210,220))
        itextc=ifont2.render("在写(攻击)作业时 停止移动(玩耍)",True,(190,210,220))
    #始前判断
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if a==0:
            if begin.collidepoint(pygame.mouse.get_pos()):
                b=1
                if event.type==pygame.MOUSEBUTTONDOWN:
                    a=1
            else:
                b=0
    #始前刷新
    pygame.display.update()
    if a==0 :
        continue

    #背景及文字
    screen.fill((60,60,60))
    screen.blit(bg,(0,0))
    itext6=ifont2.render("homework hp:"+str(round(homeworky)),True,(120,120,120))
    itext3=ifont2.render("hp:"+str(round(hero.hp)),True,(120,120,120))
    if a==1:
        itext4=ifont2.render("time:"+str(round((t2-t1)*1)),True,(120,120,120))
    itext5=ifont2.render("best:"+str(best),True,(120,120,120))
    screen.blit(itext1,(135,30))
    screen.blit(itext2,(215,70))
    screen.blit(itext3,(3,0))
    if a==1:
        screen.blit(itext4,(3,30))
    screen.blit(itext5,(3,60))
    screen.blit(itext6,(370,3))
    screen.blit(itexthp,(0,100))
    screen.blit(itexthp,(540,100))
    #血条
    heroy=500-herominus
    homeworky=500-homeworkminus
    bloodrect1 = pygame.Rect(545, 120+homeworkminus, 55,homeworky)
    bloodrect2 = pygame.Rect(0, 120+herominus, 55,heroy)
    pygame.draw.rect(screen,(150,60,60),bloodrect1,0)
    pygame.draw.rect(screen,(60,150,60),bloodrect2,0)
    #划线
    pygame.draw.rect(screen,(60,60,60),linerect1,0)
    pygame.draw.rect(screen,(60,60,60),linerect2,0)
    pygame.draw.rect(screen,(60,60,60),linerect3,0)
    #移动
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_UP:
            m_h=0
            hero.move('up',1)
        elif event.key==pygame.K_DOWN:
            m_h=0
            hero.move('down',1)
        elif event.key==pygame.K_LEFT:
            m_h=0
            hero.move('left',1)
        elif event.key==pygame.K_RIGHT:
            m_h=0
            hero.move('right',1)
    #攻击作业
    if event.type==pygame.KEYDOWN and m_h==1:

        if event.key==pygame.K_SPACE:
            m_h=0
            homeworky-=0.135
            soundhit.play()
    else:
        m_h=1
    #学科类召唤
    for i in mlist:
        i.move(mspeed)
        i.show(screen)
        i.hit(hero)
    for i in elist:
        i.move(mspeed)
        i.show(screen)
        i.hit(hero)
    for i in clist:
        i.move(mspeed)
        i.show(screen)
        i.hit(hero)
        if i.rect.x>600:
            i.x=random.randrange(-400,-220,2)
            i.y=random.choice([hero.rect.y+random.randint(40,70),hero.rect.y-random.randint(40,70)])
            i.rect = pygame.Rect(i.x,i.y, 600, 35)
            if i.rect.x>=65-155:
                screen.blit(i.image, i.rect)
    #英雄类出场
    hero.show(screen)
    heroy=hero.hp
    #输赢判断
    if hero.hp<=0:
        a=0
        b=0
        heroy=480
        homeworky=480
        hero.hp=480
        hero.rect = pygame.Rect(250, 350, 75, 75)
        if round(t2)-round(t1)>best:
            best=round(t2)-round(t1)
        pygame.mixer.music.pause()
        screen.blit(f,(0,0))
        pygame.display.update()
        soundfail.play()
        pygame.display.update()
        time.sleep(3)
        pygame.mixer.music.unpause()
        m_h=1
    if homeworky<=0:
        a=0
        b=0
        heroy=480
        homeworky=480
        hero.hp=480
        hero.rect = pygame.Rect(250, 350, 75, 75)
        if round(t2)-round(t1)>best:
            best=round(t2)-round(t1)
        pygame.mixer.music.pause()
        screen.blit(w,(0,0))
        pygame.display.update()
        soundsuccess.play()
        pygame.display.update()
        time.sleep(3)
        pygame.mixer.music.unpause()
        m_h=1
    #换帧频率
    time.sleep(0.005)
    #主循环刷新
    pygame.display.update()