import pygame,sys,time,random


#迷宫基本参数设置
screenw=1500
screenh=600
mazesize=68
flong=40
ablesee=20

coin=pygame.transform.scale(pygame.image.load("Pic/coin.png"),(flong,flong))

#迷宫生成封装
from A import Maze
def newmaze(size):
    maze = Maze(size,size)
    maze.generate_matrix_dfs()
    maps = []
    for i in maze.print_matrix():
        maps.append(list(i))
    '''
    for i in range(size):
        for j in range(size):
            if int(random.randint(1,18))==6 and maps[i][j]==0:
                maps[i][j]=3#宝藏
    '''
    return maps
def newmazeofnpeople(size):
    mid = size/2
    maze = Maze(size,size)
    maze.generate_matrix_dfs()
    maps = []
    for i in maze.print_matrix():
        maps.append(list(i))
    for i in range(size):
        for j in range(size):
            if i-mid==1 or mid-i==1 or j-mid==1 or mid-j==1:
                maps[i][j]=0
            elif i==mid and j==mid:
                maps[i][j]=2 #终点
            #elif int(random.randint(1,12))==6 and maps[i][j]==0:
            #    maps[i][j]=3#宝藏
    return maps
    
wayx=[-1,1,0,0,-1,1,-1,1]
wayy=[0,0,-1,1,1,-1,-1,1]
#绘制x-x+w,y-y+w部分地图，每个格子大小为size
#其中绘制部分以nnx，nny为左上角坐标，mode=0时显示现在的位置,1时不显示
def apr(x,y,w,size,screen,nnx=0,nny=0,mode=0):
    global nx,ny,vstmap
    nnnx=nnx
    nnny=nny
    for i in range(x,x+w):
        nnnx=nnx
        for j in range(y,y+w):
            if i>=0 and i<mazesize and j>=0 and j<mazesize:
                #if map[i][j]==3:
                #   screen.blit(coin,(nx*flong,ny*flong))
                if i==nx and j==ny and mode==1:
                    pygame.draw.rect(screen,(100,120,150),pygame.Rect(nnnx,nnny,size,size),0)

                elif mode==1 and vstmap[i][j]==-3 and map[i][j]==0:
                    for m in range(len(wayx)):
                        sx,sy=i+wayx[m],j+wayy[m]
                        if sx>=0 and sx<mazesize and sy>=0 and sy<mazesize and map[sx][sy]==-1:
                            vstmap[sx][sy]=-3
                    pygame.draw.rect(screen,(253,249,238),pygame.Rect(nnnx,nnny,size,size),0)
                elif mode==1 and vstmap[i][j]==-3 and map[i][j]==-1:
                    pygame.draw.rect(screen,(107,84,85),pygame.Rect(nnnx,nnny,size,size),0)    
                elif map[i][j]==-1 and mode==0 :
                    pygame.draw.rect(screen,(107,84,85),pygame.Rect(nnnx,nnny,size,size),0)
                elif map[i][j]==0 and mode==0:
                    pygame.draw.rect(screen,(253,249,238),pygame.Rect(nnnx,nnny,size,size),0)
                
                nnnx+=size
        nnny+=size
#def setstartpos(size):


#生成地图
map=newmaze(mazesize)
vstmap=[]
for i in range(mazesize):
    vstmap.append([])
    for j in range(mazesize):
        vstmap[i].append(0)
#初始化
pygame.init()
screen = pygame.display.set_mode((screenw,screenh))
pygame.display.set_caption("逆天-竹|迷宫游戏")

#按钮
stroot=pygame.Rect(520,280,420,45)
stchoose1=pygame.Rect(420,280,200,45)
stchoose2=pygame.Rect(840,280,200,45)
stchoose3=pygame.Rect(420,335,200,45)
stchoose4=pygame.Rect(840,335,200,45)
#图片
mbck1=pygame.transform.scale(pygame.image.load("Pic/007.png"),(screenw,screenh))
mbck2=pygame.transform.scale(pygame.image.load("Pic/049.png"),(screenw,screenh))

#字体
mf1=pygame.font.Font("HYTiaoTiaoTiJ.ttf",50)
mf2=pygame.font.Font("HYTiaoTiaoTiJ.ttf",30)
mf3=pygame.font.Font("HYTiaoTiaoTiJ.ttf",20)
mt1=mf1.render("逆天-竹の迷宫游戏",True,(50,50,50))
mt2=mf2.render("开始你的迷宫游戏",True,(50,50,50))
mt3=mf2.render("缩略图",True,(50,50,50))
mt4=mf1.render("请选择您的游戏模式",True,(50,50,50))
cmode1=mf3.render("单人模式简单",True,(50,50,50))
cmode2=mf3.render("单人模式困难",True,(50,50,50))
cmode3=mf3.render("多人抢宝模式",True,(50,50,50))
cmode4=mf3.render("多人寻路模式",True,(50,50,50))
#重点开始


#迷宫图案相对坐标
x,y=0,0
#我的当前位置坐标
nx,ny=1,0
#我的rect当然后续也可以改成图片
arect = pygame.Rect(ny*flong+5,nx*flong+5,flong-10,flong-10)

#控制移动速度
countoftime=0

#界面变量
window=0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((240,236,232))
    
    
    if window==0:
        screen.blit(mbck1,(0,0))
        screen.blit(mt1,(520,200))
        if stroot.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen,(69,99,110),stroot,0)
            screen.blit(mt2,(610,285))
            if event.type==pygame.MOUSEBUTTONDOWN:
                window=1
        else:
            pygame.draw.rect(screen,(184,212,232),stroot,0)
            screen.blit(mt2,(610,285))
    if window==1:
        screen.blit(mbck2,(0,0))
        screen.blit(mt4,(520,200))
        if stchoose1.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen,(69,99,110),stchoose1,0)
            screen.blit(cmode1,(450,289))
            if event.type==pygame.MOUSEBUTTONDOWN:
                x,y=0,0
                nx,ny=1,0
                window=2
                mazesize=48
                flong=30
                ablesee=25
                map=newmaze(mazesize)
                vstmap=[]
                arect = pygame.Rect(ny*flong+5,nx*flong+5,flong-10,flong-10)
                for i in range(mazesize):
                    vstmap.append([])
                    for j in range(mazesize):
                        vstmap[i].append(0)
        else:
            pygame.draw.rect(screen,(184,212,232),stchoose1,0)
            screen.blit(cmode1,(450,289))
        
        if stchoose2.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen,(69,99,110),stchoose2,0)
            screen.blit(cmode2,(870,289))
            if event.type==pygame.MOUSEBUTTONDOWN:
                x,y=0,0
                nx,ny=1,0
                window=3
                mazesize=68
                flong=40
                ablesee=20
                arect = pygame.Rect(ny*flong+5,nx*flong+5,flong-10,flong-10)
                map=newmaze(mazesize)
                vstmap=[]
                for i in range(mazesize):
                    vstmap.append([])
                    for j in range(mazesize):
                        vstmap[i].append(0)
        else:
            pygame.draw.rect(screen,(184,212,232),stchoose2,0)
            screen.blit(cmode2,(870,289))
        
        if stchoose3.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen,(69,99,110),stchoose3,0)
            screen.blit(cmode3,(450,339))
            if event.type==pygame.MOUSEBUTTONDOWN:
                x,y=0,0
                nx,ny=1,0
                window=4
                mazesize=78
                flong=40
                ablesee=20
                arect = pygame.Rect(ny*flong+5,nx*flong+5,flong-10,flong-10)
                map=newmaze(mazesize)
                vstmap=[]
                for i in range(mazesize):
                    vstmap.append([])
                    for j in range(mazesize):
                        vstmap[i].append(0)
        else:
            pygame.draw.rect(screen,(184,212,232),stchoose3,0)
            screen.blit(cmode3,(450,339))
        if stchoose4.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen,(69,99,110),stchoose4,0)
            screen.blit(cmode4,(870,339))
            if event.type==pygame.MOUSEBUTTONDOWN:
                x,y=0,0
                nx,ny=1,0
                window=5
                mazesize=78
                flong=40
                ablesee=20
                arect = pygame.Rect(ny*flong+5,nx*flong+5,flong-10,flong-10)
                map=newmaze(mazesize)
                vstmap=[]
                for i in range(mazesize):
                    vstmap.append([])
                    for j in range(mazesize):
                        vstmap[i].append(0)
        else:
            pygame.draw.rect(screen,(184,212,232),stchoose4,0)
            screen.blit(cmode4,(870,339))
    elif window==2 or window==3 :
        if countoftime%10==0:
            countoftime=0
            vstmap[nx][ny]=-3
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and map[nx-1][ny]==0:
                    x-=1
                    nx-=1
                if event.key == pygame.K_DOWN and map[nx+1][ny]==0:
                    x+=1
                    nx+=1
                if event.key == pygame.K_LEFT and map[nx][ny-1]==0:
                    y-=1
                    ny-=1
                if event.key == pygame.K_RIGHT and map[nx][ny+1]==0:
                    y+=1
                    ny+=1
        vstmap[nx][ny]=-3
        #刷新画布和主迷宫
        screen.fill((240,236,232))
        pygame.draw.rect(screen,(218,218,216),pygame.Rect(ablesee*flong,0,6000,600),0)
        
        #绘制迷宫和缩略图
        screen.blit(mt3,(ablesee*flong+0.5*screenw-0.5*ablesee*flong-30,10))
        apr(x,y,ablesee,flong,screen)
        apr(0,0,mazesize,4,screen,ablesee*flong+0.5*screenw-0.5*ablesee*flong-6*ablesee,60,1)
        #绘制主角
        pygame.draw.rect(screen,(100,120,150),arect,0)
        pygame.display.update()
        
        
        countoftime+=1  
    elif window ==4:
        if countoftime%10==0:
            countoftime=0
            vstmap[nx][ny]=-3
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and map[nx-1][ny]!=-1:
                    x-=1
                    nx-=1
                if event.key == pygame.K_DOWN and map[nx+1][ny]!=-1:
                    x+=1
                    nx+=1
                if event.key == pygame.K_LEFT and map[nx][ny-1]!=-1:
                    y-=1
                    ny-=1
                if event.key == pygame.K_RIGHT and map[nx][ny+1]!=-1:
                    y+=1
                    ny+=1
        vstmap[nx][ny]=-3
        #刷新画布和主迷宫
        screen.fill((240,236,232))
        pygame.draw.rect(screen,(218,218,216),pygame.Rect(ablesee*flong,0,6000,600),0)
        
        #绘制迷宫和缩略图
        screen.blit(mt3,(ablesee*flong+0.5*screenw-0.5*ablesee*flong-30,10))
        apr(x,y,ablesee,flong,screen)
        apr(0,0,mazesize,4,screen,ablesee*flong+0.5*screenw-0.5*ablesee*flong-6*ablesee,60,1)
        #绘制主角
        pygame.draw.rect(screen,(100,120,150),arect,0)
        pygame.display.update()
        
        
        countoftime+=1  
    pygame.display.update()
