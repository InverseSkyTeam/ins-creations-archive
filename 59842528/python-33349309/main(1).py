import pygame,sys,time,random
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("红包冲突3.2")
bg0 = pygame.image.load("bg.png")
bg = pygame.transform.scale(bg0,(600,600))
suc = pygame.image.load("success.png")
lose = pygame.image.load("fail.png")
pygame.mixer.music.load("bgsound.wav")
pygame.mixer.music.play(-1)
soundsuccess=pygame.mixer.Sound("success.wav")
soundfail=pygame.mixer.Sound("fail.wav")
soundeat=pygame.mixer.Sound("eat.wav")
soundboom=pygame.mixer.Sound("boom.wav")
ifont=pygame.font.SysFont("kaiti",40)
ifont2=pygame.font.SysFont("kaiti",80)
ifont3=pygame.font.SysFont("kaiti",25)
itext=ifont.render("单击以开始闯关",True,(255,255,255))
itext2=ifont2.render("红包冲突",True,(255,255,255))
itext3=ifont3.render("规则:1英雄：通过上下左右键移动",True,(255,255,255))
itext4=ifont3.render("     2敌人：通过碰撞英雄来消灭英雄",True,(255,255,255))                            
itext5=ifont3.render("     3红包：加分",True,(255,255,255))
itext6=ifont3.render("目标：存活指定秒并得到指定个红包获胜",True,(255,255,255))
score=0
level=1
itext7=ifont.render("第"+str(level)+"关",True,(255,255,255))
class Hero():
    def __init__(self):
        self.hp = 500
        self.way = "left"
        self.image = pygame.image.load("hero.png")
        self.rect = pygame.Rect(200, 400, 50, 50)

    def move(self, way, num):
        self.way = way
        if self.way == 'up':
            self.rect.y = self.rect.y - num
        elif self.way == 'down':
            self.rect.y = self.rect.y + num
        elif self.way == 'left':
            self.rect.x = self.rect.x - num
        elif self.way == 'right':
            self.rect.x = self.rect.x + num
    def show(self, screen):
        screen.blit(self.image, self.rect)
class Enemy():
    def __init__(self):
        self.people= random.choice(["p4.png", "p5.png", "p6.png"])
        self.way = random.choice(["up", "down", "left", "right"])
        self.image0 = pygame.image.load(self.people)
        self.image=pygame.transform.scale(self.image0,(65,65))
        x = random.randint(0, 450)
        y = random.randint(0, 450)
        self.rect = pygame.Rect(x, y,65, 65)

    def move(self, num):
        # 判断敌人的移动方向
        if self.way == 'up':
            self.rect.y = self.rect.y - num
            if self.rect.y < 0:
                self.way = "down"
        elif self.way == 'down':
            self.rect.y = self.rect.y + num
            if self.rect.y > 450:
                self.way = "up"
        elif self.way == 'left':
            self.rect.x = self.rect.x - num
            if self.rect.x < 0:
                self.way = "right"
        elif self.way == 'right':
            self.rect.x = self.rect.x + num
            if self.rect.x > 450:
                self.way = "left"

    def show(self, screen):
        screen.blit(self.image, self.rect)

    def hit(self, h,n):
        if self.rect.colliderect(h.rect):
            n.play()
            h.hp = h.hp - 10
class Redpacket():
    def __init__(self):
        self.image0 = pygame.image.load("hongbao.png")
        self.image=pygame.transform.scale(self.image0,(35,40))
        x1=random.randint(50,550)
        y1=random.randint(50,550)
        self.rect = pygame.Rect(x1, y1, 35, 40)
    def show(self, screen):
        screen.blit(self.image,self.rect)
    def jiafen(self,h,n):
        if self.rect.colliderect(h.rect):
            global score
            score = score +5
            n.play()
            self.rect = pygame.Rect(-660,-660, 35, 40)
         

hero=Hero()

# 批量创建敌人对象
enemiesNum = 10
enemiesList = []
hitEnemy = 0
for i in range(enemiesNum):
    enemy = Enemy()
    enemiesList.append(enemy)
#批量创建红包对象
redpacketNum = 22
redpacketList = []
for i in range(redpacketNum):
    redpacket = Redpacket()
    redpacketList.append(redpacket)
    
#标识变量“start”   
start=1
start1=1
x=0
#敌人速度
es=1
#时间
t=10
#达标分数
count=50
#红包个数
redpacketNum=8
#敌人个数
enemiesNum=8
while True:
    
    screen.blit(bg,(0,0))
    itext7=ifont.render("第"+str(level)+"关",True,(255,255,255))
    screen.blit(itext,(165,425))
    screen.blit(itext2,(150,100))
    screen.blit(itext3,(130,215))
    screen.blit(itext4,(130,260))
    screen.blit(itext5,(130,305))
    screen.blit(itext6,(130,350))
    screen.blit(itext7,(228,385))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # 记录游戏状态
        win = 2
        t1 = time.time()
        #开始
        
        if event.type==pygame.MOUSEBUTTONDOWN or start==0:
            pygame.display.update()
            pygame.mixer.music.play(-1)
            start=0   
            time.sleep(3)
            pygame.display.update()
            if event.type==pygame.MOUSEBUTTONDOWN or start1==0:
                pygame.display.update()
                screen.fill((255,255,255))
                screen.blit(bg,(0,0))
                start1=0
                pygame.display.update()    
                while True:
                    screen.blit(bg,(0,0))   
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                    font=pygame.font.SysFont("kaiti",40)
                    text=font.render("score:"+str(score),True,(255,255,255))
                    screen.blit(text,(0,0))
                    font=pygame.font.SysFont("kaiti",40)
                    text2=font.render("hp:"+str(hero.hp),True,(255,255,255))
                    screen.blit(text2,(0,30))
                    text3=font.render("level:"+str(level),True,(255,255,255))
                    screen.blit(text3,(0,60))
                    if x==0:
                        # 批量创建敌人对象
                        x=1
                        
                        enemiesNum = enemiesNum +2
                        enemiesList = []
                        hitEnemy = 0
                        for i in range(enemiesNum):
                            enemy = Enemy()
                            enemiesList.append(enemy)
                        #批量创建红包对象
                        
                        redpacketNum = redpacketNum+2
                        redpacketList = []
                        for i in range(redpacketNum):
                            redpacket = Redpacket()
                            redpacketList.append(redpacket)
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            hero.move("right", 50)
                        elif event.key == pygame.K_LEFT:
                            hero.move("left", 50)
                        elif event.key == pygame.K_UP:
                            hero.move("up", 50)
                        elif event.key == pygame.K_DOWN:
                            hero.move("down", 50)
                                
                    hero.show(screen)
                    redpacket.show(screen)
                    for m in enemiesList:
                        m.move(es)
                        m.show(screen)
                        m.hit(hero,soundboom)
                        time.sleep(0.003)
                    for n in redpacketList:
                        n.show(screen)
                        n.jiafen(hero,soundeat)
                        time.sleep(0.003)
                    #英雄失败的条件
                    if  hero.hp<=0:
                        pygame.display.update()
                        screen.blit(lose, (0, 0))
                        pygame.display.update()
                        pygame.mixer.music.stop()
                        soundfail.play()
                        time.sleep(5)
                        pygame.quit()
                        sys.exit()
                        
                    t2 = time.time()
                    t=int(t)
                    count=int(count)
                    #英雄下一关的条件
                    if t2 - t1 >=t  and score>=count:
                        pygame.mixer.music.stop()
                        soundsuccess.play()
                        time.sleep(3)
                        level=level+1
                        x=0
                        score=0
                        es=es+1
                        hero.hp=hero.hp+100
                        count=count+10
                        t=t+2
                        time.sleep(3)
                        break
                    #英雄胜利的条件
                    if level==10:
                        pygame.display.update()
                        screen.blit(suc, (0, 0))
                        pygame.display.update()
                        pygame.mixer.music.stop()
                        soundsuccess.play()
                        time.sleep(5)
                        pygame.quit()
                        sys.exit()
                    if t2 - t1 <= 5 and level<=3:
                        hero.hp=500
                    
                    pygame.display.update()
                    
    pygame.display.update()