import pygame,sys,random,time
level=1
score=0
pygame.init()
a_a=600
screen = pygame.display.set_mode((a_a,a_a))
bg=pygame.image.load("色彩缤纷.jpg")
pygame.mixer.music.load("Ahrix - Evolving.mp3")
pygame.mixer.music.play(-1)
bg=pygame.transform.scale(bg,(a_a,a_a))
screen.blit(bg,(0,0))
pygame.display.set_caption("色彩游戏")
x1=100
x2=100
x3=100
x4=100
y1=100
y2=100
y3=100
y4=100
rect0 = pygame.Rect(a_a/3-100,a_a/3-100, y1,x1)
rect1 = pygame.Rect(a_a/3,a_a/3-100, y3,x3)
rect2 = pygame.Rect(a_a/3+100,a_a/3-100, y3,x3)
rect3 = pygame.Rect(a_a/3+200,a_a/3-100, y3,x3)

rect4 = pygame.Rect(a_a/3-100,a_a/3, y1,x1)
rect5 = pygame.Rect(a_a/3,a_a/3, y2,x2)
rect6 = pygame.Rect(a_a/3+100,a_a/3, y3,x3)
rect7 = pygame.Rect(a_a/3+200,a_a/3, y3,x3)

rect8 = pygame.Rect(a_a/3-100,a_a/3+100, y1,x1)
rect9 = pygame.Rect(a_a/3,a_a/3+100, y2,x2)
rect10 = pygame.Rect(a_a/3+100,a_a/3+100, y3,x3)
rect11 = pygame.Rect(a_a/3+200,a_a/3+100, y3,x3)

rect12 = pygame.Rect(a_a/3-100,a_a/3+200, y1,x1)
rect13 = pygame.Rect(a_a/3,a_a/3+200, y2,x2)
rect14 = pygame.Rect(a_a/3+100,a_a/3+200, y3,x3)
rect15 = pygame.Rect(a_a/3+200,a_a/3+200, y3,x3)

ifont=pygame.font.SysFont("kaiti",40)
ifont2=pygame.font.SysFont("kaiti",80)
ifont3=pygame.font.SysFont("kaiti",30)
su=pygame.mixer.Sound("success.wav")
fa=pygame.mixer.Sound("fail.wav")
r=random.randint(20,250)
g=random.randint(20,250)
b=random.randint(20,250)
a=1
n=30
t1=time.time()
while True:
    myText=ifont.render("任意键以开始闯关",True,(r,g,b))
    myText2=ifont2.render("色彩游戏",True,(g,r,b))
    myText3=ifont3.render("找出与众不同的色块，考验眼力的时候到了",True,(b,r,g))
    
    myText5=ifont.render("level:"+str(level),True,(b,r,g))
    myText6=ifont.render("score:"+str(score),True,(b,r,g))
    if a==1:
        screen.blit(myText, (150, 280))
        screen.blit(myText2, (140, 110))
        screen.blit(myText3, (20, 425))
        screen.blit(myText5, (0, 0))
        screen.blit(myText6, (0, 42))
        pygame.display.update()
    t2=time.time()
    
    if a==1:
        r=random.randint(20,255)
        g=random.randint(20,255)
        b=random.randint(20,255)
        list_a=[a_a/3-100,a_a/3-100,a_a/3,a_a/3-100,a_a/3+100,a_a/3-100,a_a/3+200,a_a/3-100,a_a/3-100,a_a/3,a_a/3,a_a/3,a_a/3+100,a_a/3,a_a/3+200,a_a/3,a_a/3-100,a_a/3+100,a_a/3,a_a/3+100,a_a/3+100,a_a/3+100,a_a/3+200,a_a/3+100,a_a/3-100,a_a/3+200,a_a/3,a_a/3+200,a_a/3+100,a_a/3+200,a_a/3+200,a_a/3+200]
        www=random.randint(0,31)
        print(www)
        if www%2==0:
            sss=list_a[www]
            bbb=list_a[www+1]
        if www%2==1:
            sss=list_a[www-1]
            bbb=list_a[www]
        if sss !=a_a/3  and bbb != a_a/3-100:
            
            rectn = pygame.Rect(sss,bbb, y2,x2)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if event.type != pygame.KEYDOWN and a==1:
        pass
        continue
    
    
        
    a=0
    pygame.display.update()
    screen.fill((255,255,255))
    screen.blit(bg,(0,0))
    
    pygame.draw.rect(screen, (r,g,b), rect0, 0)
    pygame.draw.rect(screen, (r,g,b), rect1, 0)
    pygame.draw.rect(screen, (r,g,b), rect2, 0)
    pygame.draw.rect(screen, (r,g,b), rect3, 0)
    
    pygame.draw.rect(screen, (r,g,b), rect4, 0)
    pygame.draw.rect(screen, (r,g,b), rect5, 0)
    pygame.draw.rect(screen, (r,g,b), rect6, 0)
    pygame.draw.rect(screen, (r,g,b), rect7, 0)
    
    pygame.draw.rect(screen, (r,g,b), rect8, 0)
    pygame.draw.rect(screen, (r,g,b), rect9, 0)
    pygame.draw.rect(screen, (r,g,b), rect10, 0)
    pygame.draw.rect(screen, (r,g,b), rect11, 0)
    
    pygame.draw.rect(screen, (r,g,b), rect12, 0)
    pygame.draw.rect(screen, (r,g,b), rect13, 0)
    pygame.draw.rect(screen, (r,g,b), rect14, 0)
    pygame.draw.rect(screen, (r,g,b), rect15, 0)
    
    pygame.draw.rect(screen, (r,g,b), rectn, 0)
        
    try:
        pygame.draw.rect(screen, (r-n,g-n,b-n), rectn, 0)
    except:
        r=r+25
        g=g+25
        b=b+25
    if event.type==pygame.MOUSEBUTTONDOWN:
        if rectn.collidepoint(pygame.mouse.get_pos()):
            if n<=1.85:
                h=random.randint(0,1)
                if h==0:
                    n=n-0.2
                if h==1:
                    n=n-0.1
                n=1.85
            else:
                n=n-2.125
            a=1
            su.play()
            
            screen.fill((b,g,b))
            time.sleep(1.35)
            screen.blit(bg,(0,0))
            level=level+1
            score=round((score+1)*1.3)
        else:
            a=1
            
            fa.play()
            screen.fill((b,g,b))
            time.sleep(1.35)
            screen.blit(bg,(0,0))
            level=level-1
            score=round((score-1)/1.3)
    pygame.display.update()