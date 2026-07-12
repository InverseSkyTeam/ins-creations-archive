import pygame,sys,time,random
from PIL import*
pygame.init()
screen = pygame.display.set_mode((550,550))
pygame.display.set_caption("yzxの|迷-宫|")
bg=pygame.image.load("bt.jpg").convert()
zhu=pygame.image.load("zhu.jpg").convert()
zhubg=pygame.image.load("zhu.png").convert()

boom=pygame.transform.scale(pygame.image.load("boom.png"),(750,550))
bg.set_alpha(40)
zhubg.set_alpha(40)
def payin(url):
    import requests
    head = {
        "Referer": "https://icourse.xesimg.com",
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11",
    }
    response = requests.get(url, headers= head)

    file_name="飘向远方.mp3"
    with open(file_name,"wb") as file:
        file.write(response.content)
    return file_name
#https://2009yuanzixuan.github.io/About-Myself/static/music/%E9%A3%98%E5%90%91%E5%8C%97%E6%96%B9.mp3
t1=time.time()

pygame.mixer.music.load("飘向北方.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
t2=time.time()
print("You cost",round(t2-t1),"s to open the music")

l_1list=[
            [1,1,1,1,1,1,1,1,1,1,3],
            [1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1],
            [2,1,1,1,1,1,1,1,1,1,1]
        ]
l_2list=[
            [1,1,1,1,1,1,1,1,1,1,3],
            [1,1,1,1,1,1,1,1,1,1,1],
            [1,1,0,0,1,1,1,1,1,1,1],
            [1,1,0,0,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,0,0,1,1,1],
            [1,1,1,1,1,1,0,0,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1],
            [2,1,1,1,1,1,1,1,1,1,1]
        ]

l_3list=[
            [1,1,1,0,1,1,1,0,1,1,3],
            [1,0,1,0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0,1,0,1],
            [2,0,1,1,1,0,1,1,1,0,1]
        ]
l_4list=[
            [1,1,0,0,1,0,1,1,1,1,3],
            [1,1,1,1,1,0,1,0,0,1,1],
            [1,1,0,0,1,1,1,1,1,1,1],
            [1,1,1,1,1,0,1,0,0,1,1],
            [1,1,0,0,1,0,1,0,0,1,1],
            [1,1,1,1,1,1,1,1,1,1,1],
            [1,1,0,0,1,0,1,0,0,1,1],
            [1,1,1,1,1,0,1,1,1,1,1],
            [1,1,0,0,1,1,1,0,0,1,1],
            [1,1,1,1,1,0,1,0,0,1,1],
            [2,1,0,0,1,0,1,1,1,1,1]
        ]
l_5list=[
            [0,1,1,1,1,1,1,1,1,1,3],
            [1,0,1,0,1,1,0,1,1,0,1],
            [1,1,0,1,1,0,1,1,0,1,1],
            [1,0,1,1,0,1,1,0,1,1,1],
            [1,1,1,0,1,1,0,1,1,0,1],
            [1,1,0,1,1,0,1,1,0,1,1],
            [1,0,1,1,0,1,1,0,1,1,1],
            [1,1,1,0,1,1,0,1,1,0,1],
            [1,1,0,1,1,0,1,1,0,1,1],
            [1,0,1,1,0,1,1,0,1,0,1],
            [2,1,1,1,1,1,1,1,1,1,0]
        ]
l_6list=[
            [3,1,1,1,1,1,1,1,1,1,3],
            [0,0,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,0,1,1,1,1,0,0],
            [1,0,1,0,0,0,1,0,1,0,1],
            [1,0,1,1,1,1,1,0,1,1,1],
            [1,0,0,0,1,2,1,1,1,0,1],
            [1,0,1,0,1,1,1,0,0,0,1],
            [1,0,1,0,0,0,1,0,0,0,1],
            [1,1,1,1,1,0,1,1,1,0,1],
            [0,0,0,0,1,0,0,0,0,0,0],
            [3,1,1,1,1,1,1,1,1,1,3]
        ]

l_7list=[
            [1,1,1,1,1,0,1,1,1,1,3],
            [1,1,1,1,1,0,1,1,1,1,1],
            [1,1,1,1,1,0,1,1,1,1,1],
            [1,1,1,1,1,0,1,1,1,1,1],
            [1,1,1,1,1,0,1,1,1,1,1],
            [1,1,4,1,1,0,1,1,5,1,1],
            [1,1,1,1,1,0,1,1,1,1,1],
            [1,1,1,1,1,0,1,1,1,1,1],
            [1,1,1,1,1,0,1,1,1,1,1],
            [1,1,1,1,1,0,1,1,1,1,1],
            [2,1,1,1,1,0,1,1,1,1,1]
        ]
l_8list=[
            [1,1,1,1,1,0,1,1,1,0,3],
            [0,1,0,0,1,0,1,1,1,0,1],
            [0,5,0,0,1,0,1,0,1,0,1],
            [0,0,0,1,1,0,1,0,1,0,1],
            [0,5,0,0,1,0,1,0,1,0,1],
            [0,0,0,0,1,1,1,0,1,1,1],
            [0,5,0,0,1,0,1,0,1,0,1],
            [0,0,0,1,1,0,1,0,1,0,1],
            [4,1,4,0,1,0,1,0,1,0,1],
            [1,1,1,0,1,0,1,1,1,0,1],
            [2,1,4,0,1,0,1,1,1,0,3]
        ]
l_9list=[
            [6,6,6,6,6,6,6,6,6,6,3],
            [6,6,6,6,6,6,6,6,6,6,6],
            [6,6,6,6,6,6,6,6,6,6,6],
            [6,6,6,6,6,6,6,6,6,6,6],
            [6,6,6,6,6,6,6,6,6,6,6],
            [6,6,6,6,6,6,6,6,6,6,6],
            [6,6,6,6,6,6,6,6,6,6,6],
            [6,6,6,6,6,6,6,6,6,6,6],
            [6,6,6,6,6,6,6,6,6,6,6],
            [6,6,6,6,6,6,6,6,6,6,6],
            [2,6,6,6,6,6,6,6,6,6,6]
        ]
l_10list=[
            [1,1,1,1,1,2,1,1,1,1,1],
            [6,6,6,6,6,6,6,6,6,6,6],
            [6,6,6,6,6,6,6,6,6,6,6],
            [0,0,0,6,0,0,0,6,0,0,0],
            [6,6,6,6,6,6,6,6,6,6,6],
            [6,6,6,6,6,6,6,6,6,6,6],
            [0,6,0,0,0,6,0,0,0,6,0],
            [6,6,6,6,6,6,6,6,6,6,6],
            [6,6,6,6,6,6,6,6,6,6,6],
            [6,0,0,6,0,0,0,6,0,0,6],
            [6,6,6,6,6,3,6,6,6,6,6]
        ]
rect_restart = pygame.Rect(195,380,160,50)
rect_died = pygame.Rect(0,0,50,50)#|   0   |
recs_died = pygame.Rect(0,0,25,25)#|   0   |
rect_land = pygame.Rect(0,0,50,50)#|   1   |
recs_land = pygame.Rect(0,0,25,25)#|   1   |
rect_start = pygame.Rect(0,0,50,50)#|   2   |
recs_start = pygame.Rect(0,0,25,25)#|   2   |
rect_end = pygame.Rect(0,0,50,50)#|   3   |
recs_end = pygame.Rect(0,0,25,25)#|   3   |
rect_chuan = pygame.Rect(0,0,50,50)#|   4   |
recs_chuan = pygame.Rect(0,0,25,25)#|   4   |
rect_yue = pygame.Rect(0,0,50,50)#|   5   |
recs_yue = pygame.Rect(0,0,25,25)#|   5   |
rect_water = pygame.Rect(0,0,50,50)#|   6   |
recs_water = pygame.Rect(0,0,25,25)#|   6   |
xh=0
yh=500
level=1
count=0
try:
    ifont1=pygame.font.Font("font.ttf",40)
    ifont2=pygame.font.Font("font.ttf",30)
    ifont3=pygame.font.Font("font.ttf",25)
except:
    ifont1=pygame.font.SysFont("kaittf",40)
    ifont2=pygame.font.SysFont("kaittf",30)
    ifont3=pygame.font.SysFont("kaittf",25)
itext1=ifont1.render(" yzxの|迷-宫|",True,(100,100,100))
itext2=ifont2.render("绿色方块为起点,红色方块为终点",True,(100,100,100))
itext3=ifont2.render("蓝色方块为陆地,黄色方块为火山",True,(100,100,100))
itext6=ifont2.render("浅黄为穿越起点,深黄为穿越起点",True,(100,100,100))
itext7=ifont2.render("深蓝方块为旋涡,会自动下降一格",True,(100,100,100))
itext4=ifont2.render("戳我开始",True,(100,100,100))
itext5=ifont2.render("第"+str(level)+"关",True,(100,100,100))
ft4=ifont2.render("最后一关!再见!",True,(100,100,100))
s=0
zr=pygame.Rect(xh,yh,50,50)
count=0
l_6linshi=0
l_7linshi=(100,250,400,250)
l_8linshi=(50,300,50,200,50,100 , 0,400,100,400,100,500)
is_chuan=1
is_yue=1
suiji=[0,2,4]
l_9linshi=0
l_10linshi=0
t1=0
tx2=550
def ques(list,tuple=l_7linshi):
    global yh,xh,level,s,screen,is_yue,is_chuan,l_9linshi,count,l_10linshi,l_5linshi
    x=int(xh/50)
    y=int(yh/50)
    if list[y][x]==0:
        print("You die."+str(count))
        level-=1
        s=0
        xh=0
        if level==9:
            xh=250
            yh=0
        if level==5:
            xh=250
            yh=250
        yh=500
        screen.blit(boom,(-100,0))
        pygame.display.update()
        time.sleep(2)
    if list[y][x]==3:
        print("You win."+str(count))
        level+=1
        s=0
        xh=0
        yh=500
    if list[y][x]==4 and is_yue==1 and level==7:
        xh=tuple[2]
        yh=tuple[3]
        is_yue=1
    if list[y][x]==5 and is_chuan==1 and level==7:
        xh=tuple[0]
        yh=tuple[1]
        is_chuan=0
    if list[y][x]==4 and is_yue==1 and level==8:
        i_f=random.choice(suiji)
        xh=tuple[i_f]
        yh=tuple[i_f+1]
        is_yue=1
    if list[y][x]==5 and is_chuan==1 and level==8:
        i_f=random.choice(suiji)
        xh=tuple[i_f]
        yh=tuple[i_f+1]
        is_chuan=0
    if list[y][x]==6:
        count+=1
        a=time.perf_counter()
        if count%100==0:
            count=0
            yh+=50
def draw(list):
    global yh,xh
    for i in range(0,550,50):
        for j in range(0,550,50):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        xh-=50
                        if xh<=0:
                            xh=0
                        if xh>=500:
                            xh=500
                        if yh<=0:
                            yh=0
                        if yh>=500:
                            yh=500
                    if event.key==pygame.K_RIGHT:
                        xh+=50
                        if xh<=0:
                            xh=0
                        if xh>=500:
                            xh=500
                        if yh<=0:
                            yh=0
                        if yh>=500:
                            yh=500
                    if event.key==pygame.K_UP:
                        yh-=50
                        if xh<=0:
                            xh=0
                        if xh>=500:
                            xh=500
                        if yh<=0:
                            yh=0
                        if yh>=500:
                            yh=500
                    if event.key==pygame.K_DOWN:
                        yh+=50
                        if xh<=0:
                            xh=0
                        if xh>=500:
                            xh=500
                        if yh<=0:
                            yh=0
                        if yh>=500:
                            yh=500
            x=int(i/50)
            y=int(j/50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if list[y][x]==0:
                rect_died = pygame.Rect(i,j,50,50)
                recs_died = pygame.Rect(i+12.5,j+12.5,25,25)
                pygame.draw.rect(screen,(255,255,240),rect_died,1)
                pygame.draw.rect(screen,(245,245,230),recs_died,0)
            elif list[y][x]==1:
                rect_land = pygame.Rect(i,j,50,50)
                recs_land = pygame.Rect(i+12.5,j+12.5,25,25)
                pygame.draw.rect(screen,(240,248,255),rect_land,1)
                pygame.draw.rect(screen,(230,238,245),recs_land,0)
            elif list[y][x]==2:
                rect_start = pygame.Rect(i,j,50,50)
                recs_start = pygame.Rect(i+12.5,j+12.5,25,25)
                pygame.draw.rect(screen,(225,255,235),rect_start,1)
                pygame.draw.rect(screen,(215,245,225),recs_start,0)
            elif list[y][x]==3:
                rect_end = pygame.Rect(i,j,50,50)
                recs_end = pygame.Rect(i+12.5,j+12.5,25,25)
                pygame.draw.rect(screen,(255,245,235),rect_end,1)
                pygame.draw.rect(screen,(245,205,225),recs_end,0)
            elif list[y][x]==4:
                rect_chuan = pygame.Rect(i,j,50,50)
                recs_chuan = pygame.Rect(i+12.5,j+12.5,25,25)
                pygame.draw.rect(screen,(255,255,222),rect_chuan,1)
                pygame.draw.rect(screen,(255,242,212),recs_chuan,0)

            elif list[y][x]==5:
                rect_yue = pygame.Rect(i,j,50,50)
                recs_yue = pygame.Rect(i+12.5,j+12.5,25,25)
                pygame.draw.rect(screen,(251,239,202),rect_yue,1)
                pygame.draw.rect(screen,(241,229,192),recs_yue,0)
            elif list[y][x]==6:
                rect_water = pygame.Rect(i,j,50,50)
                recs_water = pygame.Rect(i+12.5,j+12.5,25,25)
                pygame.draw.rect(screen,(194,230,235),rect_water,1)
                pygame.draw.rect(screen,(194,230,235),recs_water,0)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((250,255,250))
    screen.blit(bg,(0,0))
    screen.blit(zhubg,(0,0))
    itext5=ifont2.render("第"+str(level)+"关",True,(100,100,100))
    zr=pygame.Rect(xh,yh,50,50)
    if level==11:
        itext4=ifont2.render("戳我关闭",True,(100,100,100))
    if s==0:
        if rect_restart.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen,(218,255,255),rect_restart,0)
            if event.type==pygame.MOUSEBUTTONDOWN:
                s=1
                if level==11:
                    time.sleep(2)
                    pygame.quit()
                    sys.exit()
        else:
            pygame.draw.rect(screen,(238,255,255),rect_restart,0)
    if s==0:
        screen.blit(itext1,(160,75))
        screen.blit(itext2,(60,150))
        screen.blit(itext3,(60,190))
        screen.blit(itext5,(235,330))
        screen.blit(itext4,(210,380))
        screen.blit(itext6,(60,230))
        screen.blit(itext7,(60,270))
    if s==0:
        pygame.display.update()
        continue
    if level==1:
        draw(l_1list)
        ques(l_1list)
    elif level==2:
        draw(l_2list)
        ques(l_2list)
    elif level==3:
        draw(l_3list)
        ques(l_3list)
    elif level==4:
        draw(l_4list)
        ques(l_4list)
    elif level==5:
        l_6linshi==0
        draw(l_5list)
        ques(l_5list)
    elif level==6:
        if l_6linshi==0:
            xh=250
            yh=250
            l_6linshi=1
        draw(l_6list)
        ques(l_6list)
    elif level==7:
        draw(l_7list)
        ques(l_7list)
    elif level==8:
        draw(l_8list)
        ques(l_8list,l_8linshi)
    elif level==9:
        l_10linshi==0
        draw(l_9list)
        ques(l_9list)

    elif level==10:
        if l_10linshi==0:
            xh=250
            yh=0
            l_10linshi=1
        draw(l_10list)
        ques(l_10list)
        screen.blit(ft4,(tx2,235))
        tx2-=0.5
        if tx2<-200:
            tx2=550
    elif level==11:
        itext4=ifont2.render("戳我关闭",True,(100,100,100))
        s=0
    screen.blit(zhu,zr)
    if xh<=0:
        xh=0
    if xh>=500:
        xh=500
    if yh<=0:
        yh=0
    if yh>=500:
        yh=500

    if level<=0:
        level=1
    pygame.display.update()