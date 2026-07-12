import pygame,sys,time,random
# -*- coding: utf-8 -*-
pygame.init()
screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("手速-鼠标双击")
img=pygame.image.load("hnh.jpg").convert()
img.set_alpha(125)
img=pygame.transform.scale(img,(700,500))
try:
    mf=pygame.font.SysFont("kaiti",40)
except:
    mf=pygame.font.SysFont("kaittf",40)

mt=mf.render("手速测试",True,(125,125,125))
mt7=mf.render("-----鼠标双击",True,(125,125,125))
timesound=pygame.mixer.Sound("time.wav")
con=0
c=1
csyuanshi=125
s=10
t3=0
list=[0]
t1=time.time()
x=250
y=300
begin=0
timem=15
color=95
cc=0
list=[0]
pygame.mixer.music.load("时代少年团-朱雀.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.8)
while True:
    r=pygame.Rect(x,y,150,60)
    if begin==0:
        mt2=mf.render("戳我开始",True,(95,95,95))
    if begin==1:
        mt2=mf.render("戳我上分",True,(95,95,95))
    mt3=mf.render("当前双击次数："+str(con),True,(95,95,95))
    mt4=mf.render("倒计时："+str(timem),True,(color,95,95))
    mt5=mf.render("最高双击次数："+str(max(list)),True,(95,95,95))
    if begin==0:
        t2=time.time()
        color=95
    if csyuanshi!=75 and c==1:
        csyuanshi-=0.5
    else:
        c=2
    if csyuanshi!=250 and c==2:
        csyuanshi+=0.5
    else:
        c=1
    img.set_alpha(csyuanshi)
    if cc%2==0:
        txt=time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if r.collidepoint(pygame.mouse.get_pos())and event.type==pygame.MOUSEBUTTONDOWN:
            cc+=1
            xtx=time.time()
            if  cc%2==0 and round(xtx-txt)<1:

                cc=0
                begin=1
                con+=1
                r=pygame.Rect(x,y,140,50)
                x=random.randint(30,470)
                y=random.randint(200,370)
            if round(xtx-txt)>1:
                cc=0
        if  timem==0:
            cc=0
            con=0
            timem=15
    time.sleep(0.05)
    pygame.display.update()
    screen.blit(img,(0,0))
    screen.blit(mt,(240,120))
    screen.blit(mt7,(260,155))
    pygame.draw.rect(screen,(55,135,155),r,0)
    screen.blit(mt2,(x-5,y+10))
    screen.blit(mt3,(0,0))
    screen.blit(mt4,(6,35))
    screen.blit(mt5,(0,70))
    if  begin==0:
        continue
    t3=time.time()
    timem=15-(round(t3)-round(t2))

    if timem<=5:
        color=255
        timesound.play()

    if timem==0:
        list.append(con)

        pygame.display.update()
        time.sleep(1)
        screen.blit(img,(0,0))
        x=250
        y=300
        r=pygame.Rect(x,y,150,60)
        pygame.draw.rect(screen,(55,135,155),r,0)
        screen.blit(mt2,(x-5,y+10))
        mt4=mf.render("冷却期中",True,(color,95,95))
        screen.blit(mt4,(240,145))
        pygame.display.update()
        time.sleep(3)
        begin=0
    pygame.display.update()