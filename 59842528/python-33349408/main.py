import time,random
import pygame,sys
pygame.init()
screen = pygame.display.set_mode((700,300))
pygame.display.set_caption("2021年兽跑酷")
pygame.mixer.music.load("fire.mp3")
pygame.mixer.music.play(-1)
soundsuccess=pygame.mixer.Sound("success.wav")
soundfail=pygame.mixer.Sound("fail.wav")
soundeat=pygame.mixer.Sound("eat.wav")
bg0= pygame.image.load("bg.png")
bg=pygame.transform.scale(bg0,(700,300))
suc0= pygame.image.load("success.png")
suc=pygame.transform.scale(suc0,(700,300))
lo0= pygame.image.load("fail.png")
lo=pygame.transform.scale(lo0,(700,300))
nianshou0= pygame.image.load("年兽.png")
b11 = pygame.image.load("1级鞭炮.png")
b22 = pygame.image.load("2级鞭炮.png")
b33 = pygame.image.load("3级鞭炮.png")
b44 = pygame.image.load("4级鞭炮.png")
nianshou=pygame.transform.scale(nianshou0,(100,100))
b1=pygame.transform.scale(b11,(30,60))
b2=pygame.transform.scale(b22,(31,62))
b3=pygame.transform.scale(b33,(32,64))
b4=pygame.transform.scale(b44,(33,66))
ifont=pygame.font.SysFont("kaiti",40)
itext=ifont.render("任意键以开始闯关",True,(255,255,255))
ifont1=pygame.font.SysFont("kaiti",60)
itext1=ifont1.render("2021年兽跑酷",True,(255,255,255))
ifont2=pygame.font.SysFont("kaiti",30)
itext2=ifont2.render("按任意键让年兽跳起来躲避鞭炮攻击(有彩蛋)",True,(255,255,255))

#主角的坐标
dX = 10
dY = 200
#b1和保的距离
d=random.randint(460,500)
d1=random.randint(4,6)
d2=random.randint(460,508)
#仙人掌的坐标
cX = 700
cY = 239
cX1=cX+d
cY1=239
cX2=cX1+d1
cY2=239
cX3=cX2+d2
cY3=239
score = 0
scorelist=[0]

#标识
biaoshi=0
start=1
t=1
t11=1
t22=1

y2=0
y3=0
y4=0

f2=0
f3=0
f4=0
f5=0

br1=0
br2=0
br3=0
br4=0
br5=0
br6=0
#速度
speed=4
while True:
    ssc=max(scorelist)
    screen.blit(bg,(0,0))
    screen.blit(itext,(200,250))
    screen.blit(itext1,(180,0))
    screen.blit(itext2,(65,100))
    itext3=ifont.render("最高分:"+str(ssc),True,(255,255,255))
    screen.blit(itext3,(285,180))
    if biaoshi==0:
        biaoshi==1
        br1=0
        br2=0
        br3=0
        br4=0
        br5=0
        br6=0
        f2=0
        f3=0
        f4=0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            start=0
        if start==0:

            t1=time.time()
            while True:

                screen.blit(bg,(0,0))

                #矩形
                rectn = pygame.Rect(dX, dY,30,60)
                rect1 = pygame.Rect(cX, cY,31,62)
                rect2 = pygame.Rect(cX, cY,32,64)
                rect3 = pygame.Rect(cX, cY,33,66)
                rect4 = pygame.Rect(cX, cY,34,68)
                rect11 = pygame.Rect(cX1, cY1,31,62)
                rect22 = pygame.Rect(cX1, cY1,32,64)
                rect33 = pygame.Rect(cX1, cY1,33,66)
                rect44 = pygame.Rect(cX1, cY1,34,68)
                rect111 = pygame.Rect(cX2, cY2,31,62)
                rect222 = pygame.Rect(cX2, cY2,32,64)
                rect333 = pygame.Rect(cX2, cY2,33,66)
                rect444 = pygame.Rect(cX2, cY2,34,68)
                rect1111 = pygame.Rect(cX3, cY3,31,62)
                rect2222 = pygame.Rect(cX3, cY3,32,64)
                rect3333 = pygame.Rect(cX3, cY3,33,66)
                rect4444 = pygame.Rect(cX3, cY3,34,68)
                t2=time.time()
                if t2-t1<=15:
                    bimage=b1
                    brect=rect1
                    brect1=rect11
                    brect2=rect111
                    brect3=rect1111
                    cY = 239


                elif t2-t1<=30:
                    bimage=b2
                    brect=rect2
                    brect1=rect22
                    brect2=rect222
                    brect3=rect2222
                    cY = 238

                    speed=speed+0.000000004
                elif t2-t1<=60:
                    bimage=b3
                    brect=rect3
                    brect1=rect33
                    brect2=rect333
                    brect3=rect3333
                    cY = 237

                    speed=speed+0.000004
                elif t2-t1<=120 or t2-t1>=120:
                    bimage=b4
                    brect=rect4
                    brect1=rect44
                    brect2=rect444
                    brect3=rect4444
                    cY = 236

                    speed=speed+0.00004



                #鞭炮的移动

                cX = cX - speed
                if cX <= -10:
                    cX = 700
                if t==0:
                    cX1 = cX1 - speed
                    if cX1 <= -10:
                        cX1 = 700
                if t11==0:
                    cX2 = cX2 - speed
                    if cX2 <= -10:
                        cX2 = 700
                if t22==0:
                    cX3 = cX3 - speed
                    if cX3 <= -10:
                        cX3 = 700
                #年兽的下落

                dY = dY + 3
                if dY > 200:
                      dY = 200
                #文字设置
                ifont0=pygame.font.SysFont("kaiti",40)
                itext0=ifont0.render("score:"+str(score),True,(255,255,255))


                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                #年兽上跳
                    if event.type==pygame.KEYDOWN and dY == 200:
                        for i in range(24):
                            dY = dY - 5
                #绘制主角

                screen.blit(nianshou,rectn)

                #绘制鞭炮
                screen.blit(bimage,brect)

                #分数增加
                score= score+2

                #文字

                screen.blit(itext0,(0,0))

                if score>=2021:
                    ifont2021=pygame.font.SysFont("kaiti",30)
                    itext2021=ifont2021.render("新年到了,祝您~666~好运滚滚来~888~财运滚滚来",True,(255,255,255))
                    screen.blit(itext2021,(35,60))
                    pygame.display.update()
                #记录时间

                if t2-t1>=10:
                    t=0

                    screen.blit(bimage,brect1)
                if t2-t1>=15:

                    t11=0
                    screen.blit(bimage,brect2)
                if t2-t1>=20:
                    t22=0

                    screen.blit(bimage,brect3)
                #加速
                speed=speed+0.0009
                #碰撞检测


                if rectn.colliderect(brect):
                    if f2==0:
                        soundfail.play()
                        f2=1

                    scorelist.append(score)
                    score=0
                    time.sleep(2)

                    #b1和保的距离
                    d=random.randint(460,508)
                    d1=random.randint(4,6)
                    d2=random.randint(460,508)
                    #仙人掌的坐标
                    cX = 700
                    cY = 239
                    cX1=cX+d
                    cY1=239
                    cX2=cX1+d1
                    cY2=239
                    cX3=cX1+d2
                    cY3=239

                    if br4==0:
                        br4=1
                        break
                if rectn.colliderect(brect1):
                    if f3==0:
                        soundfail.play()
                        f3=1

                    scorelist.append(score)
                    score=0
                    time.sleep(2)
                    #b1和保的距离
                    d=random.randint(460,508)
                    d1=random.randint(4,6)
                    d2=random.randint(460,508)
                    #仙人掌的坐标
                    cX = 700
                    cY = 239
                    cX1=cX+d
                    cY1=239
                    cX2=cX1+d1
                    cY2=239
                    cX3=cX2+d2
                    cY3=239

                    if br5==0:
                        br5=1
                        break
                if rectn.colliderect(brect2):
                    if f4==0:

                        soundfail.play()
                        f4=1

                    scorelist.append(score)
                    score=0
                    time.sleep(2)
                    #b1和保的距离
                    d=random.randint(460,508)
                    d1=random.randint(4,6)
                    d2=random.randint(460,508)
                    #仙人掌的坐标
                    cX = 700
                    cY = 239
                    cX1=cX+d
                    cY1=239
                    cX2=cX1+d1
                    cY2=239
                    cX3=cX1+d2
                    cY3=239
                    if br6==0:
                        br6=1
                        break
                if rectn.colliderect(brect3):
                    if f5==0:

                        soundfail.play()
                        f5=1

                    scorelist.append(score)
                    score=0
                    time.sleep(2)
                    #b1和保的距离
                    d=random.randint(460,508)
                    d1=random.randint(4,6)
                    d2=random.randint(460,508)
                    #仙人掌的坐标
                    cX = 700
                    cY = 239
                    cX1=cX+d
                    cY1=239
                    cX2=cX1+d1
                    cY2=239
                    cX3=cX2+d2
                    cY3=239
                    if br6==0:
                        br6=1
                        break

                time.sleep(0.05)
                pygame.display.update()
            pygame.display.update()
        pygame.display.update()
    pygame.display.update()