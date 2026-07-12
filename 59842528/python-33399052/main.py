import pygame,sys,time,tkinter,os,tkinter.messagebox
pygame.init()
screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("千万别动")
bg = pygame.image.load("bg.jpg").convert()
bg.set_alpha(65)
bg = pygame.transform.scale(bg,(700,500))
root=tkinter.Tk()
boom=pygame.transform.scale(pygame.image.load("boom.png"),(700,500))
new_fu=pygame.transform.scale(pygame.image.load("new_fu.png"),(700,500))
j1=pygame.transform.scale(pygame.image.load("j1.png"),(700,500))
bai=pygame.transform.scale(pygame.image.load("886.png"),(700,500))
x1=0
x2=640
herorect = pygame.Rect(x1, 435, 60, 60)
linerect1 = pygame.Rect(0, 495, 700, 5)
finalrect = pygame.Rect(x2, 435, 60, 60)
startrect = pygame.Rect(250, 280, 200, 60)
level=1
s=pygame.mixer.Sound("move1.wav")
f=pygame.mixer.Sound("over.wav")
try:
    ifont1=pygame.font.SysFont("kaiti",40)
    ifont2=pygame.font.SysFont("kaiti",30)
    ifont3=pygame.font.SysFont("kaiti",25)
except:
    ifont1=pygame.font.SysFont("kaittf",40)
    ifont2=pygame.font.SysFont("kaittf",30)
    ifont3=pygame.font.SysFont("kaittf",25)


itext1=ifont1.render("千万别动",True,(100,100,100))
itext2=ifont1.render("Don't move!",True,(100,100,100))
itext3=ifont3.render("小蓝碰到小粉及为获胜，进入下一关",True,(100,100,100))
itext4=ifont3.render("在这期间静心静气,不要碰鼠标和键盘",True,(100,100,100))
itext5=ifont2.render("START开始",True,(100,100,100))
ft1=ifont2.render("恭喜获得新皮肤",True,(100,100,100))
ft2=ifont2.render("按任意键以领取",True,(100,100,100))
ft3=ifont2.render("游戏结束                   就怪了！",True,(100,100,100))
ft4=ifont2.render("这次小蓝碰到小粉,游戏就真的结束!再见!",True,(100,100,100))#zyt
a=0
b=0
l3=0
count=0
bc=0
t2=0
t1=0
tx1=700
tx2=700
pygame.mixer.music.load("时代少年团-朱雀.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)
while True:
    screen = pygame.display.set_mode((700,500))
    screen.fill((224,245,225))
    screen.blit(bg,(0,0));
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    itext6=ifont3.render("LEVEL:"+str(level),True,(100,100,100))
    screen.blit(itext1,(270,50))
    screen.blit(itext2,(250,90))
    screen.blit(itext3,(170,130))
    screen.blit(itext4,(165,160))
    screen.blit(itext6,(310,210))
    herorect = pygame.Rect(x1, 435, 60, 60)
    finalrect = pygame.Rect(x2, 435, 60, 60)
    pygame.draw.rect(screen,(60,60,60),linerect1,0)
    pygame.draw.rect(screen,(255,185,206),finalrect,0)
    pygame.draw.rect(screen,(194,235,226),herorect,0)
    if a==0:
        pygame.draw.rect(screen,(141,233,213),startrect,0)
        screen.blit(itext5,(283, 295))
    if startrect.collidepoint(pygame.mouse.get_pos()):
        b=1
        if event.type==pygame.MOUSEBUTTONDOWN:
            a=1
    else:
        b=0

    if b==0 and a==0:
        startrect = pygame.Rect(250, 280, 200, 60)
        pygame.draw.rect(screen,(141,231,213),startrect,0)
        screen.blit(itext5,(283, 295))
        pygame.display.update()
    elif b==1 and a==0:
        startrect = pygame.Rect(250, 280, 200, 60)
        pygame.draw.rect(screen,(241,251,213),startrect,0)
        screen.blit(itext5,(283, 295))
        pygame.display.update()
    if a==0:
        continue
    bc+=1
    if level==1:
        x1+=0.25
        x2-=0.25
    if level==2:
        x1+=0.05
        x2-=0.05
    if level==3:
        count+=1
        if l3==1:
            x1+=0.05
            x2-=0.05
        if count%2500==0:
            count=0
            if l3==0:
                l3=1
            elif l3==1:
                l3=0
    if level==4:
        screen.blit(new_fu,(0,0))
        screen.blit(ft1,(400,220))
        screen.blit(ft2,(400,250))
        count+=1
        if l3==1:
            x1+=0.15
            x2-=0.15
        if count%2000==0:
            count=0
            if l3==0:
                l3=1
            elif l3==1:
                l3=0
    if level==5:

        count+=1
        if l3==1:
            x1+=0.04
            x2-=0.04
        if count%4000==0:
            os.system('new_html.html')
            count=0
            if l3==0:
                l3=1
            elif l3==1:
                l3=0
    if level==6:
        screen.fill((0,0,0));pygame.display.update()
        screen.fill((255,0,0));pygame.display.update()
        screen.fill((0,255,0));pygame.display.update()
        screen.fill((0,0,255));pygame.display.update()
        screen.fill((255,255,0));pygame.display.update()
        screen.fill((0,255,255));pygame.display.update()
        screen.fill((255,0,255));pygame.display.update()
        screen.fill((255,255,255));pygame.display.update()
        count+=1
        if l3==1:
            x1+=0.1
        if count%1000==0:
            pygame.mixer.music.load("h.mp3")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play(1)
            count=0
            if l3==0:
                l3=1
            elif l3==1:
                l3=0
    if level==7:

        count+=1
        if count%1500==0:
            screen.blit(j1,(0,0))
            pygame.display.update()
            count=0
            if l3==0:
                l3=1
            elif l3==1:
                l3=0
        if l3==1:
            x1+=0.02
            x2-=0.02
        else:
            screen.blit(j1,(0,0))
            pygame.display.update()
    if level==8:
        count+=1
        if count%1500==0:
            pygame.mixer.music.load("yin.mp3")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play(1)
            pygame.display.update()
            count=0
            if l3==0:
                l3=1
            elif l3==1:
                l3=0
        if l3==1:
            x1+=0.04
            x2-=0.04
        else:
            screen.blit(j1,(0,0))
            pygame.display.update()
    if level==9:
        screen.blit(ft3,(tx1,235))
        tx1-=0.04
        count+=1
        if count%1500==0 and tx1<-50:
            pygame.display.update()
            count=0
            if l3==0:
                l3=1
            elif l3==1:
                l3=0
        if l3==1:
            x1+=0.08
            x2-=0.08
        else:
            pygame.display.update()
    if level==10:
        screen.blit(ft4,(tx2,235))
        tx2-=0.5
        x1+=0.025
        x2-=0.025
        if tx2<-555:
            tx2=700
    if herorect.colliderect(finalrect):
        if level==10:
            screen.blit(bai,(0,0))
            pygame.display.update()
            time.sleep(2)
            pygame.quit()
            sys.exit()
        x1=0
        x2=640
        level+=1
        a=0
        bc=0
        count=0
        l3=0
        s.play()
    if (event.type==pygame.MOUSEMOTION or event.type==pygame.MOUSEBUTTONDOWN or event.type==pygame.KEYDOWN) and (bc>=120):
        x1=0
        x2=640
        level-=1
        a=0
        bc=0
        count=0
        l3=0
        if level<1:
            level=1
        f.play()
        screen.blit(boom,(0,0))
        pygame.display.update()

        time.sleep(2)
    pygame.display.update()