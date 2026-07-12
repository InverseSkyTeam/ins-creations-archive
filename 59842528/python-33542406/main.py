import pygame,sys,time
'''
from xes.tool import*
xopen()
'''
pygame.init()
screen = pygame.display.set_mode((900,720))
pygame.display.set_caption("の竹|文字游戏|[yzx]")
bg=pygame.image.load("bg.png").convert()

sw=pygame.image.load("sw.png").convert()

pg=pygame.image.load("pg.png").convert()

strec=pygame.Rect(340,500,200,60)
try:
    ifont1=pygame.font.Font("font.ttf",40)
    ifont2=pygame.font.Font("font.ttf",30)
    ifont3=pygame.font.Font("font.ttf",25)
    ifont4=pygame.font.Font("font.ttf",50)
    ht=pygame.font.Font("font.ttf",25)
except:
    ifont1=pygame.font.SysFont("kaittf",40)
    ifont2=pygame.font.SysFont("kaittf",30)
    ifont3=pygame.font.SysFont("kaittf",25)
    ifont4=pygame.font.SysFont("kaittf",50)
    ht=pygame.font.SysFont("kaittf",25)

tx1=ifont4.render("の竹|文字游戏|[yzx]",True,(100,100,100))
tx2=ifont4.render("The game of Chinese character",True,(100,100,100))
tx3=ifont1.render("上下左右移动,空格键与物体交互",True,(100,100,100))
tx4=ifont1.render("戳我开始",True,(100,100,100))
#|-1钥匙|
wall=ifont1.render("墙",True,(100,100,100))#|1墙|
hero=ifont1.render("我",True,(230,250,250))#|2我|
door=ifont1.render("门",True,(100,100,100))#|3门|
table=ifont1.render("桌",True,(100,100,100))#|4桌|
chair=ifont1.render("椅",True,(100,100,100))#|5椅|
sand=ifont1.render("沙",True,(100,100,100))#|6沙|
hair=ifont1.render("发",True,(100,100,100))#|7发|
electricity=ifont1.render("电",True,(100,100,100))#|8电|
look=ifont1.render("视",True,(100,100,100))#|9视|
machine=ifont1.render("机",True,(100,100,100))#|10机|
dog=ifont1.render("狗",True,(100,100,100))#|11狗|
tree=ifont1.render("树",True,(100,100,100))#|12树|
house=ifont1.render("房",True,(100,100,100))#|13房|
son=ifont1.render("子",True,(100,100,100))#|14子|
cat=ifont1.render("猫",True,(100,100,100))#|15猫|
home=ifont1.render("家",True,(100,100,100))#|16家|

dao=ifont1.render("倒",True,(100,100,100))#|17倒|
le=ifont1.render("了",True,(100,100,100))#|18了|
de=ifont1.render("的",True,(100,100,100))#|19的|
xian=ifont1.render("线",True,(100,100,100))#|20线|
gan=ifont1.render("杆",True,(100,100,100))#|21杆|
hx=100
hy=350
c_u=0
c_d=0
c_l=0
c_r=0
level=1
c=0
a=1
x1=0
y1=500
count=0
i=0
x=0
y=500
mb1=0

keybd=pygame.mixer.Sound("kb.wav")
#keybd.set_volume(0)
opdr=pygame.mixer.Sound("open the door.wav")

jh1=0
jh2=0
jh3=0
jh4=0
jh5=0

aa=0
ab=0

l_2linshi=0
jh_list=[
        "我：这是在哪里？",
        "我……好像失忆了。",
        "这……应该是我的家。",
        "桌子旁边好像有点东西。",
        ""
        ]
exception=  [
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            ]
#0-17 0-9
l_1list=[
            [1 ,1 ,1 ,1 ,1,1,1 ,1,1,1,1,1,1,1,1,1,1,1],
            [1 ,1 ,1 ,1 ,1,1,1 ,1,1,1,1,1,1,1,1,1,1,1],
            [1 ,1 ,0 ,0 ,6,7,6 ,7,0,0,0,5,5,0,0,0,1,1],
            [1 ,1 ,0 ,0 ,0,0,0 ,0,0,0,5,4,4,5,0,0,1,1],
            [1 ,1 ,0 ,0 ,0,0,0 ,0,0,0,5,4,4,5,0,0,1,1],
            [1 ,1 ,0 ,0 ,0,0,0 ,0,0,0,0,5,5,0,0,0,1,1],
            [1 ,1 ,0 ,0 ,0,0,0 ,0,0,0,0,0,0,0,0,0,1,1],
            [1 ,1 ,0 ,0 ,8,9,10,0,0,0,0,0,0,0,0,0,1,1],
            [1 ,1 ,1 ,1 ,1,1,1 ,1,1,1,1,1,1,1,3,1,1,1],
            [1 ,1 ,1 ,1 ,1,1,1 ,1,1,1,1,1,1,1,1,1,1,1]
        ]

l_2list=[
            [1 ,1 ,13,3 ,1 ,1 ,1 ,1 ,13,3 ,1 ,1 ,1 ,1 ,13,3 ,1 ,1],
            [1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1],
            [1 ,12,0 ,0 ,12,0 ,0 ,12,0 ,0 ,12,0 ,0 ,12,0 ,0 ,12,1],
            [1 ,-1,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1],
            [1 ,0 ,0 ,17,18,19,8 ,20,21,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1],
            [1 ,0 ,0 ,0 ,0 ,0 ,-3,0 ,0 ,0 ,0 ,0 ,0 ,0 ,15,0 ,0 ,1],
            [1 ,0 ,0 ,0 ,11,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1],
            [1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1],
            [12,0 ,-2,12,0 ,0 ,12,0 ,0 ,12,0 ,0 ,12,0 ,0 ,12,0 ,1],
            [1 ,13,14,1 ,13,14,1 ,13,14,1 ,16,3 ,1 ,13,14,1 ,13,1]
        ]
l_3list=[
            [1 ,1 ,13,3 ,1 ,1 ,1 ,1 ,13,3 ,1 ,1 ,1 ,1 ,13,3 ,1 ,1],
            [1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1],
            [1 ,12,0 ,0 ,12,0 ,0 ,12,0 ,0 ,12,0 ,0 ,12,0 ,0 ,12,1],
            [1 ,-1,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1],
            [1 ,0 ,0 ,17,18,19,8 ,20,21,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1],
            [1 ,0 ,0 ,0 ,0 ,0 ,-3,0 ,0 ,0 ,0 ,0 ,0 ,0 ,15,0 ,0 ,1],
            [1 ,0 ,0 ,0 ,11,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1],
            [1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1],
            [12,0 ,-2,12,0 ,0 ,12,0 ,0 ,12,0 ,0 ,12,0 ,0 ,12,0 ,1],
            [1 ,13,14,1 ,13,14,1 ,13,14,1 ,16,3 ,1 ,13,14,1 ,13,1]
        ]
catcount=0
dogcount=0
sh=0
def dm():
    global jh1,jh2,jh3,jh4,jh5,jh_list
    if jh1==0:
        jhprt(jh_list[0],0,500)
        jh1=1
    else:
        jhprp(jh_list[0],0,500)
    if jh2==0 and jh1==1:
        jhprt(jh_list[1],0,540)
        jh2=1
    else:
        jhprp(jh_list[1],0,540)
    if jh3==0 and jh2==1:
        jhprt(jh_list[2],0,580)
        jh3=1
    else:
        jhprp(jh_list[2],0,580)
    if jh4==0 and jh3==1:
        jhprt(jh_list[3],0,620)
        jh4=1
    else:
        jhprp(jh_list[3],0,620)
    if jh5==0 and jh4==1:
        jhprt(jh_list[4],0,660)
        jh5=1
    else:
        jhprp(jh_list[4],0,660)
def dc():
    global jh1,jh2,jh3,jh4,jh5,dm
    jh1=0
    jh2=0
    jh3=0
    jh4=0
    jh5=0
    dm()
    jh1=1
    jh2=1
    jh3=1
    jh4=1
    jh5=1
def cljh():
    global jh_list,dc
    jh_list[0]=""
    jh_list[1]=""
    jh_list[2]=""
    jh_list[3]=""
    jh_list[4]=""
    dc()
c_k_d=0
def draw(list):
    global catcount,sh,dogcount,hy,hx,screen,hreo,hx,hy

    for i in range(0,900,50):
        for j in range(0,500,50):
            x=i//50
            y=j//50
            if list[y][x]==1:
                screen.blit(wall,(i,j))
            if list[y][x]==2:
                if sh==0:
                    screen.blit(hero,(hx,hy))
                elif sh==1:
                    screen.blit(hero,(hx+8,hy+12))
            if list[y][x]==3:
                screen.blit(door,(i,j))
            if list[y][x]==4:
                screen.blit(table,(i,j))
            if list[y][x]==5:
                screen.blit(chair,(i,j))
            if list[y][x]==6:
                screen.blit(sand,(i,j))
            if list[y][x]==7:
                screen.blit(hair,(i,j))
            if list[y][x]==8:
                screen.blit(electricity,(i,j))
            if list[y][x]==9:
                screen.blit(look,(i,j))
            if list[y][x]==10:
                screen.blit(machine,(i,j))
            if list[y][x]==11:
                screen.blit(dog,(i,j))
            if list[y][x]==12:
                screen.blit(tree,(i,j))
            if list[y][x]==13:
                screen.blit(house,(i,j))
            if list[y][x]==14:
                screen.blit(son,(i,j))
            if list[y][x]==15:
                screen.blit(cat,(i,j))
            if list[y][x]==16:
                screen.blit(home,(i,j))
            if list[y][x]==17:
                screen.blit(dao,(i,j))
            if list[y][x]==18:
                screen.blit(le,(i,j))
            if list[y][x]==19:
                screen.blit(de,(i,j))
            if list[y][x]==20:
                screen.blit(xian,(i,j))
            if list[y][x]==21:
                screen.blit(gan,(i,j))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

key_count=0
ah=0;ac=0;ad=0;af=0;ag=0
def eventing(list):
    global hx,hy,c_u,c_d,c_l,c_r,jh1,jh2,jh3,jh4,jh5,mb1,sh,opdr,level,dc,screen,hreo,hx,hy
    global aa,ab,key_count,ac,ad,af,ag,ah

    x=hy//50
    y=hx//50

    if hx>0:
        if list[x][y-1]==1 or list[x][y-1]==4 or list[x][y-1]==5 or list[x][y-1]==6 or list[x][y-1]==7 or list[x][y-1]==8 or list[x][y-1]==9 or list[x][y-1]==10 or list[x][y-1]==11 or list[x][y-1]==12 or list[x][y-1]==13 or list[x][y-1]==14 or list[x][y-1]==15 or list[x][y-1]==16 or list[x][y-1]==17 or list[x][y-1]==18 or list[x][y-1]==19 or list[x][y-1]==20 or list[x][y-1]==21:
            c_l=1
        else:
            c_l=0
    if hx<850:
        if list[x][y+1]==1 or list[x][y+1]==4 or list[x][y+1]==5 or list[x][y+1]==6 or list[x][y+1]==7 or list[x][y+1]==8 or list[x][y+1]==9 or list[x][y+1]==10 or list[x][y+1]==11 or list[x][y+1]==12 or list[x][y+1]==13 or list[x][y+1]==14 or list[x][y+1]==15 or list[x][y+1]==16 or list[x][y+1]==17 or list[x][y+1]==18 or list[x][y+1]==19 or list[x][y+1]==20 or list[x][y+1]==21:
            c_r=1
        else:
            c_r=0
    if hy>0:
        if list[x-1][y]==1 or list[x-1][y]==4 or list[x-1][y]==5 or list[x-1][y]==6 or list[x-1][y]==7 or list[x-1][y]==8 or list[x-1][y]==9 or list[x-1][y]==10 or list[x-1][y]==11 or list[x-1][y]==12 or list[x-1][y]==13 or list[x-1][y]==14 or list[x-1][y]==15 or list[x-1][y]==16 or list[x-1][y]==17 or list[x-1][y]==18 or list[x-1][y]==19 or list[x-1][y]==20 or list[x-1][y]==21:
            c_u=1
        else:
            c_u=0
    if hy<450:
        if list[x+1][y]==1 or list[x+1][y]==4 or list[x+1][y]==5 or list[x+1][y]==6 or list[x+1][y]==7 or list[x+1][y]==8 or list[x+1][y]==9 or list[x+1][y]==10 or list[x+1][y]==11 or list[x+1][y]==12 or list[x+1][y]==13 or list[x+1][y]==14 or list[x+1][y]==15 or list[x+1][y]==16 or list[x+1][y]==17 or list[x+1][y]==18 or list[x+1][y]==19 or list[x+1][y]==20 or list[x+1][y]==21:
            c_d=1
        else:
            c_d=0
    if hy!=450 and hy!=0 and hx!=850 and hx!=0:
        if (list[x+1][y]==5 or list[x-1][y]==5 or list[x][y+1]==5 or list[x][y-1]==5) and level==1 and mb1==0 and event.type == pygame.KEYDOWN:
            if event.key==pygame.K_SPACE and ab==0:
                jh_list[0]="送给'我'的信：我们知道现在你已经失忆了"
                jh_list[1]="我们来告诉你的身份。你是一个平平无奇的平民,"
                jh_list[2]="叫做'我'，我们是你的爸妈'父'和'母'，文字世界被大"
                jh_list[3]="魔王打乱了。要是我们没有打败大魔王，就只能让"
                jh_list[4]="你来拯救世界了，记得拿到三件宝物………'啊！'"
                dc()
                mb1=1
                ab=1

        if list[x+1][y]==3 or list[x-1][y]==3 or list[x][y+1]==3 or list[x][y-1]==3 or list[x][y]==3:
            hero=ht.render("我",True,(100,100,100))
            sh=1
        else:
            hero=ifont1.render("我",True,(100,100,100))
            sh=0

    if (list[x][y]==-1 ) and level==2 and mb1==0 and event.type == pygame.KEYDOWN:
        if event.key==pygame.K_SPACE and ac==0:
            if key_count+1==3:
                cljh()
                key_count+=1
            else:
                key_count+=1
                jh_list[0]="恭喜找到第"+str(key_count)+"把钥匙"
                jh_list[1]="提示：1.[又进村来(打一字)]下面"
                jh_list[2]="          2.[名词]electricity 下面"
                jh_list[3]="          3. π=1+x x=? [?的英语的另一个意思的]上面"
                jh_list[4]=" "
            dc()
            ac=1
    if (list[x][y]==-2) and level==2 and mb1==0 and event.type == pygame.KEYDOWN:
        if event.key==pygame.K_SPACE and ad==0:
            if key_count+1==3:
                cljh()
                key_count+=1
            else:
                key_count+=1
                jh_list[0]="恭喜找到第"+str(key_count)+"把钥匙"
                jh_list[1]="提示：1.[又进村来(打一字)]下面"
                jh_list[2]="          2.[名词]electricity 下面"
                jh_list[3]="          3. π=1+x x=? [?的英语的另一个意思的]上面"
                jh_list[4]=" "
            dc()
            ad=1
    if (list[x][y]==-3) and level==2 and mb1==0 and event.type == pygame.KEYDOWN:
        if event.key==pygame.K_SPACE and af==0:
            if key_count+1==3:
                cljh()
                key_count+=1
            else:
                key_count+=1
                jh_list[0]="恭喜找到第"+str(key_count)+"把钥匙"
                jh_list[1]="提示：1.[又进村来(打一字)]下面"
                jh_list[2]="          2.[名词]electricity 下面"
                jh_list[3]="          3. π=1+x x=? [?的英语的另一个意思的]上面"
                jh_list[4]=" "
            dc()
            af=1
    if key_count==3 and ag==0:
        jh_list[0]="恭喜找到第3把钥匙"
        jh_list[1]="赶紧打开第一扇门，开启你的冒险之旅吧！"
        jh_list[2]=""
        jh_list[3]=""
        jh_list[4]=""
        dc()
        ag=1
        mb1=1
def jhprt(string,x,y):
    global keybd,screen,hreo,hx,hy

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    text = ""
    pygame.display.update()
    for i in range(len(string)):
        text += string[i]
        itext= ifont1.render(text,True,((235,250,240)))
        screen.blit(itext,(x,y))
        pygame.display.update()
        keybd.play()
        pygame.display.update()
        pygame.time.wait(80)
        pygame.display.update()
def jhprp(string,x,y):
    itext= ifont1.render(string,True,((235,250,240)))
    screen.blit(itext,(x,y))

pygame.mixer.music.load("破风.mp3")
pygame.mixer.music.play(-1)
#pygame.mixer.music.set_volume(0)



canin=0
s=0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            import webbrowser
            print("由于社区的bug我的所有作品消失，恳请大家看一下我的作品")
            time.sleep(1.5)
            webbrowser.open("https://code.xueersi.com/home/project/detail?lang=code&pid=33398998&version=offline&form=python&langType=python")
            pygame.quit()
            sys.exit()
        if strec.collidepoint(pygame.mouse.get_pos()) and canin==0:
            s=1
            if event.type == pygame.MOUSEBUTTONDOWN:
                canin=1
        elif canin==0:
            s=0
            pygame.display.update()
    pygame.display.update()
    if canin==0:
        screen.fill((255,255,255))
        screen.blit(pg,(0,0))

        if s==1:
            pygame.draw.rect(screen,(210,245,220),strec,0)
            pygame.draw.rect(screen,(224,248,224),strec,0)
            screen.blit(tx4,(357.5,500))
        else:
            pygame.draw.rect(screen,(230,250,240),strec,0)
            screen.blit(tx4,(357.5,500))

        screen.blit(tx1,(250,100))
        screen.blit(tx2,(170,160))
        screen.blit(tx3,(160,240))

    pygame.display.update()
    if canin==0:
        continue

    pygame.display.update()
    screen.fill((255,255,255))
    screen.blit(bg,(0,0))
    screen.blit(sw,(0,500))
    if canin==0:
        pygame.draw.rect(screen,(240,250,240),strec,0)
        screen.blit(tx4,(357.5,500))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        if event.type==pygame.KEYDOWN and c_k_d==0:
            if event.key==pygame.K_UP and c_u==0:
                hy-=50
                screen.blit(hero,(hx,hy))
            elif event.key==pygame.K_DOWN and c_d==0:
                hy+=50
                screen.blit(hero,(hx,hy))
            elif event.key==pygame.K_LEFT and c_l==0:
                hx-=50
                screen.blit(hero,(hx,hy))
            elif event.key==pygame.K_RIGHT and c_r==0:
                hx+=50
                screen.blit(hero,(hx,hy))
    c_k_d=0
    if hx<=0:
        hx=0
    if hx>=900:
        hx=900
    if hy<=0:
        hy=0
    if hy>=500:
        hy=500
    if level==2:
        draw(l_2list)
        eventing(l_2list)
        dm()
    if level==1:
        if l_1list[hy//50][hx//50]==3:
            draw(l_1list)
            eventing(l_1list)

            if mb1==1:
                level=2
                mb1=0
                hx=550
                hy=450
                opdr.play()
                pygame.time.wait(360)
                screen.fill((255,255,255))
                screen.blit(bg,(0,0))
                screen.blit(sw,(0,500))
                draw(l_2list)
                eventing(l_2list)
                pygame.display.update()
                jh_list[0]="门外硝烟弥漫...左边突然冒出一道金光。"
                jh_list[1]="在左边区域寻找三把钥匙(空格键确认)"
                jh_list[2]="提示：1.[又进村来(打一字)]下面"
                jh_list[3]="          2.[名词]electricity 下面"
                jh_list[4]="          3. π=1+x x=? [?的英语的另一个意思的]上面"
                dc()
                draw(exception)
            elif mb1==0 and ah==0:
                jh_list[0]="桌子旁边好像还有东西没看"
                jh_list[1]=""
                jh_list[2]=""
                jh_list[3]=""
                jh_list[4]=""
                dc()
                ah=1
        else:
            draw(l_1list)
            eventing(l_1list)
        dm()

    if sh==0:
        hero=ifont1.render("我",True,(100,100,100))
        screen.blit(hero,(hx,hy))
    elif sh==1:
        hero=ht.render("我",True,(100,100,100))
        screen.blit(hero,(hx+8,hy+12))

    pygame.display.update()