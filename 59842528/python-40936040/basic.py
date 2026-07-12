import pygame,sys,random,time,os
from moviepy.editor import *

XW=950
YW=600
FW =80
FWO = 80

pygame.init()



clip = VideoFileClip("./Media/zhufu.mp4",target_resolution=(YW,XW))



screen = pygame.display.set_mode((XW,YW))
pygame.display.set_caption("Flappy-Ribbit 翻滚的兔年")

keybd=pygame.mixer.Sound("./Media/kb.wav")
fail=pygame.mixer.Sound("./Media/fail.wav")
eat=pygame.mixer.Sound("./Media/eat.wav")
keybd.set_volume(0.1)
eat.set_volume(0.1)
fail.set_volume(0.1)

jh1=0
jh2=0
jh3=0
jh4=0
jh5=0
jh_list=[
        "由于您2023年运气爆棚",
        "因此一整年都会风调雨顺，家和万事兴:",
        "再此祝大家在新的一年中，一帆风顺，每天开心",
        "也祝各位在春节，能够无忧无虑，没有作业",
        "       ------By Yzx's Blog 袁梓轩"
        ]
def jhprt(string,x,y):
    global keybd,txfo2
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    text = ""
    pygame.display.update()
    for i in range(len(string)):
        text += string[i]
        itext= txfo2.render(text,True,((0,0,0)))
        screen.blit(itext,(x,y))
        pygame.display.update()
        keybd.play()
        pygame.display.update()
        pygame.time.wait(200)
        pygame.display.update()



ground = pygame.transform.scale(pygame.image.load("./IMAGE/ground.gif"),(XW,YW))
stgr = pygame.transform.scale(pygame.image.load("./IMAGE/stgr.gif"),(XW,YW))
grn = pygame.transform.scale(pygame.image.load("./IMAGE/grn.gif"),(XW,YW))

txfo = pygame.font.Font("./Fonts/FZquanfuti.ttf",30)
txfo2 = pygame.font.Font("./Fonts/华康儿风体 Std W4.otf",40)
blesstext=txfo.render("Blessing福气:",True,(255,255,255))


class Tiger:
    def __init__(self,speed):
        self.none = random.seed()
        self.base = pygame.image.load("./IMAGE/t.png")
        self.alpha = 0
        self.speed = speed
        self.zhuan = 1
        self.image = pygame.transform.scale(self.base,(FW,FW))
        self.mask = pygame.mask.from_surface(self.image)
        self.y = random.randrange(0,YW-FW,25)
        self.none = random.seed()
        self.x = random.randrange(XW,XW+600,10)
    def rotate(self):
        self.image = pygame.transform.rotate(pygame.transform.scale(self.base,(FW,FW)),self.alpha)
        self.mask = pygame.mask.from_surface(self.image)
        self.alpha+=self.zhuan
    def show(self,screen):
        screen.blit(self.image,(self.x,self.y))
        self.x -= self.speed
        if(self.x <= random.randint(-300,-70)):
            self.x = random.randint(XW,XW+900)
            self.y = random.randint(0,YW-FW)
        self.rotate()
    def go(self):
        self.x = random.randint(XW,XW+900)
        self.y = random.randint(0,YW-FW)
    def collide(self,mask,x,y):
        return self.mask.overlap(mask,(int(self.x-x),int(self.y-y)))!=None
class Carrot:
    def __init__(self,speed):
        self.none = random.seed()
        self.base = pygame.image.load("./IMAGE/c.png")
        self.alpha = 0
        self.speed = speed
        self.zhuan = 0.6
        self.image = pygame.transform.scale(self.base,(FW,FW))
        self.mask = pygame.mask.from_surface(self.image)
        self.y = random.randrange(0,YW-FW,25)
        self.none = random.seed()
        self.x = random.randrange(XW,XW+600,10)
    def rotate(self):
        self.image = pygame.transform.rotate(pygame.transform.scale(self.base,(FW,FW)),self.alpha)
        self.mask = pygame.mask.from_surface(self.image)
        self.alpha+=self.zhuan
    def show(self,screen):
        screen.blit(self.image,(self.x,self.y))
        self.x -= self.speed
        if(self.x <= random.randint(-300,-70)):
            self.x = random.randint(XW,XW+900)
            self.y = random.randint(0,YW-FW)
        self.rotate()
    def go(self):
        self.x = random.randint(XW,XW+900)
        self.y = random.randint(0,YW-FW)
    def collide(self,mask,x,y):
        return self.mask.overlap(mask,(int(self.x-x),int(self.y-y)))!=None
class Fbig:
    def __init__(self,speed):
        self.none = random.seed()
        self.base = pygame.image.load("./IMAGE/big.png")
        self.alpha = 0
        self.speed = speed
        self.zhuan = 0.6
        self.image = pygame.transform.scale(self.base,(FW,FW))
        self.mask = pygame.mask.from_surface(self.image)
        self.y = random.randrange(0,YW-FW,25)
        self.none = random.seed()
        self.x = random.randrange(XW+900,XW+2000,10)
    def rotate(self):
        self.image = pygame.transform.rotate(pygame.transform.scale(self.base,(FW,FW)),self.alpha)
        self.mask = pygame.mask.from_surface(self.image)
        self.alpha+=self.zhuan
    def show(self,screen):
        screen.blit(self.image,(self.x,self.y))
        self.x -= self.speed
        if(self.x <= random.randint(-300,-70)):
            random.randrange(XW+900,XW+1900,10)
            self.y = random.randint(0,YW-FW)
        self.rotate()
    def go(self):
        self.x = random.randint(XW,XW+900)
        self.y = random.randint(0,YW-FW)
    def collide(self,mask,x,y):
        return self.mask.overlap(mask,(int(self.x-x),int(self.y-y)))!=None
class Speeden:
    def __init__(self,speed):
        self.none = random.seed()
        self.base = pygame.image.load("./IMAGE/s+.png")
        self.alpha = 0
        self.speed = speed
        self.zhuan = 0.6
        self.image = pygame.transform.scale(self.base,(FW,FW))
        self.mask = pygame.mask.from_surface(self.image)
        self.y = random.randrange(0,YW-FW,25)
        self.none = random.seed()
        self.x = random.randrange(XW+900,XW+2000,10)
    def rotate(self):
        self.image = pygame.transform.rotate(pygame.transform.scale(self.base,(FW,FW)),self.alpha)
        self.mask = pygame.mask.from_surface(self.image)
        self.alpha+=self.zhuan
    def show(self,screen):
        screen.blit(self.image,(self.x,self.y))
        self.x -= self.speed
        if(self.x <= random.randint(-300,-70)):
            random.randrange(XW+900,XW+1900,10)
            self.y = random.randint(0,YW-FW)
        self.rotate()
    def go(self):
        self.x = random.randint(XW,XW+900)
        self.y = random.randint(0,YW-FW)
    def collide(self,mask,x,y):
        return self.mask.overlap(mask,(int(self.x-x),int(self.y-y)))!=None
class Rabbit:
    def __init__(self):
        self.base = pygame.image.load("./IMAGE/r.png")
        self.alpha = 0
        self.speed = random.randint(15,35)/100
        self.zhuan = 1
        self.image = pygame.transform.scale(self.base,(FWO,FWO))
        self.mask = pygame.mask.from_surface(self.image)
        self.y = (YW+FW)/2
        self.pre = 0
        self.x = 20
    def rotate(self):
        random.seed()
        self.image = pygame.transform.rotate(pygame.transform.scale(self.base,(FWO,FWO)),360-self.alpha)
        self.mask = pygame.mask.from_surface(self.image)
        if (self.alpha+self.zhuan<=360):
            self.alpha+=self.zhuan
        else:
            self.alpha=0
    
    def show(self,screen):
        random.seed()
        screen.blit(self.image,(self.x,self.y))
        self.pre  *=0.8
        self.y += (0.9+self.pre)
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
            self.pre-=0.6
        if(self.y <= 0):
            self.y =0
        if(self.y >= YW-FW):
            self.y = YW-FW
            return False   
        self.rotate()
        return True


tl = []
cl = []
rab = Rabbit()
lists = [15,18,21,24,42,45,48,51,54,57,60,27,30,33,36,39]

biggen = Fbig(0.5)
biggenisopen = False
biggencount = 0 

speeden = Speeden(0.4)
speedenisopen = False
speedencount = 0 
isgo =False

for i in range(10):
    random.seed()
    tl.append(Tiger(lists[i]/100.0))
    if i>0:
        while tl[i].mask.overlap(tl[i-1].mask,(int(tl[i].x-tl[i-1].x),int(tl[i].y-tl[i-1].y)))!=None:
            tl[i] = Tiger(lists[i]/100)
for i in range(10):
    random.seed()
    cl.append(Carrot(lists[i]/100.0))

blessing = 2022.665

windows = 0

stbu = pygame.transform.scale(pygame.image.load("./IMAGE/r.png"),(190,190))
burec = pygame.Rect(340,320,190,190)

pygame.mixer.music.load("./Media/waiting for love.mp3")
pygame.mixer.music.set_volume(0.08)
pygame.mixer.music.play(-1)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255,255,255))

    if windows == 0:
        screen.blit(stgr,(0,0))
        screen.blit(pygame.font.Font("./Fonts/FZquanfuti.ttf",50).render("旋转的兔年",True,(255,255,255)),(333,50))
        screen.blit(pygame.font.Font("./Fonts/FZquanfuti.ttf",30).render("兔子通过按上键控制向上，躲避老虎，采集萝卜收集福气",True,(255,255,255)),(100,120))
        screen.blit(pygame.font.Font("./Fonts/FZquanfuti.ttf",30).render("放大镜会放大兔子，电池可以加速兔子，福气达到2023有惊喜",True,(255,255,255)),(73,160))
        screen.blit(pygame.font.Font("./Fonts/FZquanfuti.ttf",70).render("当前福气值："+str(round(blessing,3)),True,(255,255,255)),(143,210))
        if burec.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.ellipse(screen,(207,56,73),burec,0)
            screen.blit(pygame.font.Font("./Fonts/FZquanfuti.ttf",50).render("START",True,(255,255,255)),(373,380))
            if event.type == pygame.MOUSEBUTTONDOWN:
                windows=1
        else:
            screen.blit(stbu,(340,320))
            
            
    if windows == 1:
        screen.blit(ground,(0,0))
        for t in tl:
            t.show(screen)
            if t.collide(rab.mask,rab.x,rab.y) and speedenisopen==False:
                fail.play()
                windows = 0
                
                biggen = Fbig(0.5)
                biggenisopen = False
                biggencount = 0 

                speeden = Speeden(0.4)
                speedenisopen = False
                speedencount = 0 

                tl = []
                cl = []
                FWO = 80
                for i in range(10):
                    random.seed()
                    tl.append(Tiger(lists[i]/100.0))
                    if i>0:
                        while tl[i].mask.overlap(tl[i-1].mask,(int(tl[i].x-tl[i-1].x),int(tl[i].y-tl[i-1].y)))!=None:
                            tl[i] = Tiger(lists[i]/100)
                for i in range(10):
                    random.seed()
                    cl.append(Carrot(lists[i]/100.0))
        for c in cl:
            c.show(screen)
            if c.collide(rab.mask,rab.x,rab.y):
                blessing+=0.005
                eat.play()
                c.go()
        biggen.show(screen)
        speeden.show(screen)
        if biggen.collide(rab.mask,rab.x,rab.y):
            eat.play()
            biggen.go()
            biggenisopen =True
            FWO = 120
        if speeden.collide(rab.mask,rab.x,rab.y):
            eat.play()
            speeden.go()
            speedenisopen =True
            for i in tl:
                i.speed +=1.8
            for i in cl:
                i.speed +=1.8
            rab.base = pygame.image.load("./IMAGE/safer.png")
        if speedenisopen:
            biggenisopen = True
            FWO = 120
            speedencount+=1
            if(speedencount==1200):
                for i in tl:
                    i.speed -=1.8
                for i in cl:
                    i.speed -=1.8
            if(speedencount>=1400):
                speedencount=0
                speedenisopen =False
                rab.base = pygame.image.load("./IMAGE/r.png")
        if biggenisopen:
            biggencount+=1
            if(biggencount>=800):
                biggencount=0
                biggenisopen =False
                FWO = 80
        rab.show(screen)
        blesstext=txfo.render("Blessing福气: "+str(round(blessing,4)),True,(255,255,255))
        screen.blit(blesstext,(XW-300,10))
        if blessing >=2023 and isgo == False:
            windows = 3
            isgo = True
        

    if windows == 3:
        screen.fill((206,56,73))
        screen.blit(grn,(0,0))
        if jh1==0:
            jhprt(jh_list[0],100,80) 
            jh1=1
        else:
            jhprt(jh_list[0],100,80)
        if jh2==0 and jh1==1:
            jhprt(jh_list[1],100,140) 
            jh2=1
        else:
            jhprt(jh_list[1],100,140)
        if jh3==0 and jh2==1:
            jhprt(jh_list[2],100,200) 
            jh3=1
        else:
            jhprt(jh_list[2],100,200)
        if jh4==0 and jh3==1:
            jhprt(jh_list[3],100,260) 
            jh4=1
        else:
            jhprt(jh_list[3],100,260)
        if jh5==0 and jh4==1:
            jhprt(jh_list[4],100,320) 
            jh5=1
        else:
            jhprt(jh_list[4],100,320)
        pygame.display.update()
        time.sleep(3)
        
        clip.preview()
        clip.close()
        pygame.mixer.music.load("./Media/waiting for love.mp3")
        pygame.mixer.music.set_volume(0.08)
        pygame.mixer.music.play(-1)
        windows = 0
        
    pygame.display.update()