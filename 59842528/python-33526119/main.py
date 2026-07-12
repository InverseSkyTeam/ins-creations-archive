import pygame,sys,random,time,os
import webbrowser
webbrowser.open_new_tab("https://z-program.vercel.app/littleexe/DINO小恐龙轻量版.rar")
pygame.init()
jh1=0
jh2=0
jh3=0
jh4=0
jh5=0
jh_list=[
        "由于您2022年运气爆棚",
        "因此自动帮您加分到2022！:",
        "恭喜！",
        "再此，也祝大家在新的一年中，也能够顺顺利利，每天开心",
        "也祝各位在即将来临的考试中取得理想的成绩！"
        ]
screen = pygame.display.set_mode((1000,275))
pygame.display.set_caption("新春小恐龙")
pygame.display.set_icon(pygame.image.load("file/yzx.ico"))
bg=pygame.transform.scale(pygame.image.load("file/bg.png"),(1000,275))
ground=pygame.image.load("file/ground.png")
dp=pygame.transform.scale(pygame.image.load("file/dp.png"),(55,60))
dl=pygame.transform.scale(pygame.image.load("file/dl.png"),(55,60))
dr=pygame.transform.scale(pygame.image.load("file/dr.png"),(55,60))
speed=13
xground=0

keybd=pygame.mixer.Sound("file/kb.wav")
f=pygame.mixer.Sound("file/fail.wav")

footcount=0
jumpcount=0
score=0
high=0
confident=''
itf=pygame.font.Font("file/华康儿风体 Std W4.otf",35)
ft1=itf.render("SCORE:"+str(int(score)),True,(0,0,0))
itf2=pygame.font.Font("file/华康儿风体 Std W4.otf",37)
ft2=itf.render("目标2022",True,(0,0,0))
ft3=itf.render("G A M E   O V E R",True,(0,0,0))
ft4=itf2.render("新D春I小N恐O龙",True,(0,0,0))

ft5=itf.render("空格SPACE键以开始 Alt+F4关闭",True,(0,0,0))
ft11=itf.render("HIGH:"+str(int(high)),True,(0,0,0))
c1=itf.render("达成成就：小试牛刀",True,(0,0,0))
c2=itf.render("达成成就：初出茅庐",True,(0,0,0))
c22=itf.render("达成成就：锋芒毕露",True,(0,0,0))
c3=itf.render("达成成就：~6~6~6~年兽来袭 一会按下Y键试试",True,(0,0,0))
c4=itf.render("达成成就：~8~8~8~",True,(0,0,0))
c5=itf.render("达成成就：元旦烟花",True,(0,0,0))
c6=itf.render("达成成就：遇到年兽",True,(0,0,0))
c7=itf.render("达成成就：新年快乐(影藏彩蛋)",True,(0,0,0))
cloudlist=[]
big=0
def jhprt(string,x,y):
    global keybd,itf2
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    text = ""
    pygame.display.update()
    for i in range(len(string)):
        text += string[i]
        itext= itf2.render(text,True,((0,0,0)))
        screen.blit(itext,(x,y))
        pygame.display.update()
        keybd.play()
        pygame.display.update()
        pygame.time.wait(200)
        pygame.display.update()
class Text():
    def __init__(self):
        self.y=90
        self.x=1000
    def show(self,screen,x):
        screen.blit(x,(self.x,self.y))
    def move(self,speed):
        self.x-=speed
        if self.x<=-1000:
            self.x=-1000
text=Text()
class Cloud():
    def __init__(self):
        self.y=random.randint(0,120)
        self.x=random.randint(1000,2500)
        self.image=pygame.transform.scale(pygame.image.load("file/cloud.png"),(60,30))
    def show(self,screen):
        screen.blit(self.image,(self.x,self.y))
    def move(self,speed):
        self.x-=speed
        if self.x<-55:
            self.x=random.randint(1000,2500)
            self.y=random.randint(0,120)
for i in range(4):
    cloudlist=[]
    cloud=Cloud()
    cloudlist.append(cloud)
class Dino():
    def __init__(self):
        self.x=15
        self.y=180
        self.width=60
        self.height=65
        self.image1=pygame.transform.scale(pygame.image.load("file/dl.png"),(self.width,self.height))
        self.image2=pygame.transform.scale(pygame.image.load("file/dr.png"),(self.width,self.height))
        self.image3=pygame.transform.scale(pygame.image.load("file/dp.png"),(self.width,self.height))
        self.image4=pygame.transform.scale(pygame.image.load("file/dd1.png"),(self.width+20,self.height-5))
        self.image5=pygame.transform.scale(pygame.image.load("file/dd2.png"),(self.width+20,self.height-5))
        self.r1=pygame.Rect(self.x,self.y,self.width,self.height)
        self.r2=pygame.Rect(self.x,self.y,self.width,self.height)
        self.r3=pygame.Rect(self.x,self.y,self.width,self.height)
        self.r4=pygame.Rect(self.x,self.y+5,self.width+20,self.height-5)
        self.r5=pygame.Rect(self.x,self.y+5,self.width+20,self.height-5)
        self.cfd=''
        self.cj='c'#canjump
        self.jumpstep=4
        self.cd='c'#canjump
        self.died=0
    def show(self,screen,footcount):
        #显示部分
        if self.cj!='ing' and self.cd!='ing':
            if footcount//self.jumpstep%2==1:
                screen.blit(self.image2,self.r2)
                #pygame.time.wait(1)
            else:
                screen.blit(self.image1,self.r1)
        elif self.cj=='ing':
            screen.blit(self.image3,self.r3)
        elif self.cd=='ing':
            self.y=205
            if footcount//self.jumpstep%2==1:
                screen.blit(self.image4,self.r4)
                #pygame.time.wait(1)
            else:
                screen.blit(self.image5,self.r5)
        #每次重新绑定
        if self.y==180:
            self.cfd='walk'
            self.cj='c'
            self.cd='c'
        self.image1=pygame.transform.scale(pygame.image.load("file/dl.png"),(self.width,self.height))
        self.image2=pygame.transform.scale(pygame.image.load("file/dr.png"),(self.width,self.height))
        self.image3=pygame.transform.scale(pygame.image.load("file/dp.png"),(self.width,self.height))
        self.image4=pygame.transform.scale(pygame.image.load("file/dd1.png"),(self.width+20,self.height-5))
        self.image5=pygame.transform.scale(pygame.image.load("file/dd2.png"),(self.width+20,self.height-5))
        self.r1=pygame.Rect(self.x,self.y,self.width,self.height)
        self.r2=pygame.Rect(self.x,self.y,self.width,self.height)
        self.r3=pygame.Rect(self.x,self.y,self.width,self.height)
        self.r4=pygame.Rect(self.x,self.y+5,self.width+20,self.height-5)
        self.r5=pygame.Rect(self.x,self.y+5,self.width+20,self.height-5)

    def jump(self):
        if self.cj=='ing':
            self.cfd='jump'
            if self.y<=15:
                self.cj='n'
            elif self.y>=15:
                self.y-=38.125
                self.cj='ing'
    def down(self):
        if self.cd=='ing':
            self.cfd='down'
            self.y=205
        if self.cd=='c':
            self.y=180


dino=Dino()
is_down=0



class Dragon():
    def __init__(self):
        self.x=6800
        self.y=random.randint(138,140)
        self.width=65
        self.height=45
        self.image=pygame.transform.scale(pygame.image.load("file/dragon.png"),(self.width,self.height))
        self.r=pygame.Rect(self.x,self.y,self.width,self.height)
    def show(self,screen):
        screen.blit(self.image,self.r)
        self.image=pygame.transform.scale(pygame.image.load("file/dragon.png"),(self.width,self.height))
        self.r=pygame.Rect(self.x,self.y,self.width,self.height)
    def move(self,speed,f):
        self.x-=speed
        if self.x<-105:
             self.x=6800
             self.y=random.randint(138,140)

    def hit(self,hero):
        if hero.r1.colliderect(self.r) or hero.r2.colliderect(self.r) or hero.r3.colliderect(self.r) or hero.r4.colliderect(self.r) or hero.r5.colliderect(self.r):
            hero.died+=1
dragon=Dragon()

class Firecraker():
    def __init__(self):

        self.x=random.randint(1000,1200)
        self.y=170
        self.width=40
        self.height=80
        self.image=pygame.transform.scale(pygame.image.load("file/f.png"),(self.width,self.height))
        self.r=pygame.Rect(self.x,self.y,self.width-5,self.height)
    def show(self,screen):
        screen.blit(self.image,self.r)
        self.image=pygame.transform.scale(pygame.image.load("file/f.png"),(self.width,self.height))
        self.r=pygame.Rect(self.x,self.y,self.width-5,self.height)

    def move(self,speed):
        self.x-=speed
        if self.x<-105:

            self.x=random.randint(1000,1200)
    def hit(self,hero):
        if hero.r1.colliderect(self.r) or hero.r2.colliderect(self.r) or hero.r3.colliderect(self.r) or hero.r4.colliderect(self.r) or hero.r5.colliderect(self.r):
            hero.died+=1

firecraker=Firecraker()


class Nian():
    global ddd
    def __init__(self):
        self.x=1002
        self.y=0
        self.width=230
        self.height=280
        self.image=pygame.transform.scale(pygame.image.load("file/n.png"),(self.width,self.height))
        self.r=pygame.Rect(self.x,self.y,self.width-40,self.height)
        self.sh=0
    def show(self,screen):
        screen.blit(self.image,self.r)
        self.image=pygame.transform.scale(pygame.image.load("file/n.png"),(self.width,self.height))
        self.r=pygame.Rect(self.x,self.y,self.width,self.height)
    def move(self,speed):
        self.x-=speed

    def hit(self,hero):
        if hero.r1.colliderect(self.r) or hero.r2.colliderect(self.r) or hero.r3.colliderect(self.r) or hero.r4.colliderect(self.r) or hero.r5.colliderect(self.r):
            self.sh=1

nian=Nian()

pygame.mixer.music.load("file/fire.mp3")
pygame.mixer.music.play(-1)

dc=0
dcf=0
begin=0
ddd=0
sss=0
b=0
qqq=0
diednum=5
while True:
    a=dino.died
    is_down=0
    screen.fill((255,255,255))
    screen.blit(bg,(0,0))
    if b==0:
        screen.blit(ft4,(300,70))
        screen.blit(ft5,(320,150))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN :
                if event.key==pygame.K_y:
                    pygame.quit()
                    sys.exit()
                else:
                    b=1
                    print(b)
        continue

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN :
            if (event.key==pygame.K_SPACE or event.key==pygame.K_UP) and dino.cj=='c' and dino.cfd!='jump':
                dino.cj='ing'

            if event.key==pygame.K_DOWN:

                if dino.cfd!='jump':
                    if dino.cd=='c':
                        dino.cd='ing'
                        is_down=1

        if is_down==0 and dino.cd=='ing':
            dino.cd='c'
            dino.y=180
            dino.cfd='walk'

    if dino.y>=180:
        dino.y=180

    if dino.y<=15 :
        dino.y=15
        dino.cj='c'

    footcount+=1
    ft1=itf.render("SCORE:"+str(int(score)),True,(0,0,0))
    ft11=itf.render("HIGH:"+str(int(high)),True,(0,0,0))
    screen.blit(ft1,(800,0))
    screen.blit(ft11,(600,0))
    screen.blit(ft2,(100,0))
    if ddd==0:
        #GROUND
        xground-=speed
        if xground<= -1200:
            xground=0
        screen.blit(ground,(xground,245))
        screen.blit(ground,(xground+1200,245))
        #GROUND


        #CLOUD
        for i in cloudlist:
            i.show(screen)
            i.move(speed)
        #CLOUD

        #DRAGON
        dragon.show(screen)
        dragon.move(speed,firecraker)
        dragon.hit(dino)
        #DRAGON


        #DINO
        dino.y+=15
        dino.jump()
        dino.show(screen,footcount)
        #DINO

        #FIRECRACKERS

        firecraker.show(screen)
        firecraker.move(speed)
        firecraker.hit(dino)

        #FIRECRACKERS

        #SCORE
        score+=speed/50

        if int(score)>=720:
            nian.show(screen)
            nian.move(speed)
            nian.hit(dino)
        if nian.sh==1:
            ddd=1
            screen.blit(ft3,(375,120))
            pygame.display.update()
            f.play()
            time.sleep(8)
            screen.fill((255,255,255))
            screen.blit(bg,(0,0))
            if jh1==0:
                jhprt(jh_list[0],0,0)
                jh1=1
            else:
                jhprp(jh_list[0],0,0)
            if jh2==0 and jh1==1:
                jhprt(jh_list[1],0,45)
                jh2=1
            else:
                jhprp(jh_list[1],0,45)
            if jh3==0 and jh2==1:
                jhprt(jh_list[2],0,90)
                jh3=1
            else:
                jhprp(jh_list[2],0,90)
            if jh4==0 and jh3==1:
                jhprt(jh_list[3],0,135)
                jh4=1
            else:
                jhprp(jh_list[3],0,135)
            if jh5==0 and jh4==1:
                jhprt(jh_list[4],0,180)
                jh5=1
            else:
                jhprt(jh_list[4],0,180)
            sss=1
            qqq=1
            pygame.display.update()
    elif qqq!=1:
        screen.blit(ft3,(375,120))
        pygame.display.update()
        f.play()
        if score>high:
            high=score
        time.sleep(3)
        b=0
        dc=0
        dcf=0
        begin=0
        ddd=0
        sss=0
        qqq=0
        score=0
        speed=13
        diednum=6
        for i in range(4):
            cloudlist=[]
            cloud=Cloud()
            cloudlist.append(cloud)
        dino=Dino()
        is_down=0
        dragon=Dragon()
        firecraker=Firecraker()
        nian=Nian()
    else:
        if score>high:
            high=score
        time.sleep(3)
        b=0
        dc=0
        dcf=0
        begin=0
        ddd=0
        sss=0
        score=0
        speed=6
        diednum=6
        for i in range(4):
            cloudlist=[]
            cloud=Cloud()
            cloudlist.append(cloud)
        dino=Dino()
        is_down=0
        dragon=Dragon()
        firecraker=Firecraker()
        nian=Nian()
    if sss==0:
        if a-dino.died==-1:
            dcf+=1

        dc+=1
        if dc%diednum==0:
            dc=0
            if dcf>=diednum:
                ddd=1
            dcf=0


        if int(score)%50==0:
            speed+=0.1
            if dino.jumpstep-1>=1:
                dino.jumpstep-=0.5

        if score>=50 and score <150:
            if int(score)==50:
                text.x=1000
            text.show(screen,c1)
            text.move(7)

        if score>=150 and score<500:
            if int(score)==150:
                text.x=1000
            text.show(screen,c2)
            text.move(7)
        if score>=500 and score<666:
                    if int(score)==500:
                        text.x=1000
                    text.show(screen,c22)
                    text.move(7)
        if score>=666 and score<888:
            if int(score)==666:
                text.x=1000
            text.show(screen,c3)
            text.move(5)


        #SCORE
        if score>=200 and score <=400:
            diednum=4
        if score>=400 and score <=900:
            diednum=3
        if score>=900 and score <=1500:
            diednum=2
        if score>=1500 and score <=20000:
            diednum=1
        pygame.display.update()