#这个代码是我初期的代码风格，有那么亿点点乱，现在我自己都看不懂了
import pygame
import sys
from gamedata import *
from game import *
pygame.init()
width,height=1200,674
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('纸中立方 (3^3 in cube)')
levelindex = 1
leveldata = gamedata(levelindex)
cube = Cube(leveldata,(0,0))
n_down = False
def go():
    num=0
    while 1:
        if num==30:
            return 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((0,0,0))
        x=10
        y=10
        show_text(screen,'原作者：小轩',color=(255,255,255),pos=(x,y),size=60)
        show_text(screen,'改编作者：黄羿杰',color=(255,255,255),pos=(x,y+80),size=60)
        show_text(screen,'注：本作部分图片素材来自ccw的POCO的《超阀》',color=(255,255,255),pos=(x,y+2*80),size=45)
        show_text(screen,'如有侵权请告知删除',color=(255,255,255),pos=(x,y+3*80),size=45)
        pygame.display.update()
        pygame.time.delay(10)
        num+=1
def gameinit():#主界面
    bg = pygame.image.load('./背景.png').convert_alpha()
    title=pygame.image.load('./标题.png').convert_alpha()
    zhengtu=pygame.image.load('./征途.png').convert_alpha()
    zhengtu2=pygame.image.load('./征途2.png').convert_alpha()
    bgx,bgy=0,0
    k=-1
    zt_rect=zhengtu.get_rect()
    zt_rect.x,zt_rect.y=616,253
    #print(zt_rect)
    ismode=0
    mode_alpha=0
    canmode=1
    iscancel=0
    draw_black=0
    alpha_black=0
    level=None
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        #print(bgx,bgy)
        pos=pygame.mouse.get_pos()
        bx,by=(pos[0]-600)*(-0.03),(pos[1]-674/2)*(-0.03)
        screen.blit(bg, (-25+bx,-14+by))
        screen.blit(title, (-56+bx,-75+by))
        if draw_black:
            alpha_black+=10
            draw_alpha_rect(screen,(29,83,0xbb),alpha_black,pygame.Rect(0,0,1200,674),0)
            if alpha_black>=255:
                alpha_black=0
                draw_black=0
                if level==0:
                    gethelp()
                    getlevel(1,1)
                else:
                    gethelp1()
                    getlevel(1,0)
            pygame.time.delay(10)
            pygame.display.update()
            continue
        if not pygame.mouse.get_pressed()[0]:
            iscancel=0
        if not iscancel and zt_rect.collidepoint(pos[0], pos[1]) and not ismode:
            zt_rect.y-=164
            zt_rect.x-=15
            screen.blit(zhengtu2, (zt_rect.x+bx,zt_rect.y+by))
            zt_rect.y+=164
            zt_rect.x+=15
            if not iscancel and pygame.mouse.get_pressed()[0] and not ismode:
                #modeinit()
                ismode=1
        else:
            screen.blit(zhengtu, (zt_rect.x+bx,zt_rect.y+by))
        
        if ismode:
            if canmode:
                mode_alpha+=10
            draw_alpha_rect(screen,(0,0,0),40,pygame.Rect(180+3,120+3,500,300),20)
            draw_alpha_rect(screen,(88,88,91),mode_alpha,pygame.Rect(180,120,500,300),20)
            if mode_alpha>=180:
                canmode=0
                show_text(screen,'是否开启作弊',pos=(400,270),size=40)
                show_text(screen,'是',pos=(400,410),size=40)
                show_text(screen,'否',pos=(700,410),size=40)
                show_text(screen,'X',color=(255,0,0),pos=(800,270),size=20)
                if pygame.mouse.get_pressed()[0] and pygame.Rect(800,270,20,20).collidepoint(pos[0], pos[1]):
                    ismode=0
                    canmode=1
                    mode_alpha=0
                    iscancel=1
                if pygame.mouse.get_pressed()[0] and pygame.Rect(400,410,40,40).collidepoint(pos[0], pos[1]):
                    ismode=0#是
                    canmode=1
                    mode_alpha=0
                    iscancel=1
                    draw_black=1
                    level=0
                if pygame.mouse.get_pressed()[0] and pygame.Rect(700,410,40,40).collidepoint(pos[0], pos[1]):
                    ismode=0#否
                    canmode=1
                    mode_alpha=0
                    iscancel=1
                    draw_black=1
                    level=1
            pygame.time.delay(10)
        pygame.display.update()
def draw_alpha_rect(window,color,alpha,rect,border_radius):
    rect_surface = pygame.Surface((rect.width+rect.x, rect.height+rect.y), flags=pygame.SRCALPHA)
    pygame.draw.rect(rect_surface, color, rect, border_radius=border_radius)
    rect_surface.set_alpha(alpha)
    window.blit(rect_surface, (rect.x, rect.y))
def draw_circle_alpha():
    surface = pygame.Surface((600, 600), pygame.SRCALPHA)
    rect = surface.get_rect(center=(350, 350))
    surface.fill((63,0xbb,0xd0))
    # 在 Surface 对象上画一个白色的圆
    pygame.draw.circle(surface, pygame.Color("white"), (300, 300), 150)
    
    # 设置 Surface 对象中圆的部分为透明
    surface.set_colorkey(pygame.Color("white"))
    
    # 将 Surface 对象绘制到屏幕上
    screen.blit(surface, rect)
def draw_mb_alpha():
    surface1 = pygame.Surface((1200, 700), pygame.SRCALPHA)
    rect = surface1.get_rect(center=(350, 350))
    surface1.fill((29,83,0xbb))
    draw_alpha_rect(surface1,(63,0xbb,0xd0),100,pygame.Rect(153,28,600,600),30)
    pygame.draw.rect(surface1, pygame.Color("white"), pygame.Rect(300, 50,600,600),border_radius=30)
    surface1.set_colorkey(pygame.Color("white"))
    screen.blit(surface1, rect)
def draw_line_fill(p1,llong,color):
    p2=(p1[0]+llong,p1[1])
    p3=(p1[0]+llong,p1[1]+llong)
    p4=(p1[0],p1[1]+llong)
    pygame.draw.polygon(screen,color,[p1,p2,p3,p4])
    pygame.draw.aalines(screen,(0,0,0),True,[p1,p2,p3,p4])
def draw_rect(cube,llong,x,y):
    data=cube.data
    for i in range(len(data['front'])):
        for j in range(len(data['front'][0])):
            draw_line_fill((y+j*llong,x+i*llong),llong,data['front'][i][j].color)
            show_text(screen,str(data['front'][i][j].number),pos=((y+j*llong+((llong-35)//2)) ,(x+i*llong+((llong-30)//2))),size=30)
            if i==cube.y and j==cube.x:
                pygame.draw.rect(screen,(29,83,0xbb),pygame.Rect(y+j*llong+20,x+i*llong+20,llong-40,llong-40))
def gethelp():
    npc=[]
    for i in range(1,10):
        npc.append(pygame.image.load('npc'+str(i)+'.png'))
    alpha_pic=255
    pic_num=0
    isalpha=0
    alpha_out=0
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        draw_alpha_rect(screen,(29,83,0xbb),255,pygame.Rect(0,0,1200,674),0)
        draw_alpha_rect(screen,(0,0,0),20,pygame.Rect(0,150,1200,200),0)
        show_text(screen,'纸中立方',pos=(300,60),color=(255,255,255),size=150)
        next_level=pygame.image.load('next.png').convert_alpha()
        screen.blit(next_level,(1000,360))
        next_rect=pygame.Rect(1000,350,75,75)
        show_text(screen,'点击跳过',(255,255,255),(1000,350+75+10),20)
        pos=pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if next_rect.collidepoint(pos[0],pos[1]):
                return
        if alpha_out:
            pygame.time.delay(20)
            alpha_out=0
            pic_num+=1
            isalpha=0
            alpha_pic=255
            if pic_num==9:
                return
        if isalpha and not alpha_out:
            alpha_pic-=8
            npc[pic_num].set_alpha(alpha_pic)
            screen.blit(npc[pic_num],(250,330))
            npc[pic_num].set_alpha(255)
            if alpha_pic-8<0:
                pygame.display.update()
                pygame.time.delay(10)
                alpha_out=1
            pygame.time.delay(10)
        if not isalpha:
            screen.blit(npc[pic_num],(250,330))
            if pygame.mouse.get_pressed()[0]:
                isalpha=1
        pygame.display.update()
def gethelp1():
    npc=[]
    for i in [1,2,3,4,5,8,9]:
        npc.append(pygame.image.load('npc'+str(i)+'.png'))
    alpha_pic=255
    pic_num=0
    isalpha=0
    alpha_out=0
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        draw_alpha_rect(screen,(29,83,0xbb),255,pygame.Rect(0,0,1200,674),0)
        draw_alpha_rect(screen,(0,0,0),20,pygame.Rect(0,150,1200,200),0)
        next_level=pygame.image.load('next.png').convert_alpha()
        show_text(screen,'纸中立方',pos=(300,60),color=(255,255,255),size=150)
        screen.blit(next_level,(1000,360))
        next_rect=pygame.Rect(1000,350,75,75)
        show_text(screen,'点击跳过',(255,255,255),(1000,350+75+10),20)
        pos=pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if next_rect.collidepoint(pos[0],pos[1]):
                return
        if alpha_out:
            pygame.time.delay(20)
            alpha_out=0
            pic_num+=1
            isalpha=0
            alpha_pic=255
            if pic_num==7:
                return
        if isalpha and not alpha_out:
            alpha_pic-=8
            npc[pic_num].set_alpha(alpha_pic)
            screen.blit(npc[pic_num],(250,330))
            npc[pic_num].set_alpha(255)
            if alpha_pic-8<0:
                pygame.display.update()
                pygame.time.delay(10)
                alpha_out=1
            pygame.time.delay(10)
        if not isalpha:
            screen.blit(npc[pic_num],(250,330))
            if pygame.mouse.get_pressed()[0]:
                isalpha=1
        pygame.display.update()
def getlevel(level,canzb):
    leveldata = gamedata(level)
    '''if level==0:
        cube=Cube(leveldata,(0,0))'''
    cube=Cube(leveldata,(0,0))
    move_block=None
    move_num=0
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and move_block==None:
                if event.key == pygame.K_LEFT:
                    move_block='left'
                elif event.key == pygame.K_RIGHT:
                    move_block='right'
                elif event.key == pygame.K_UP:
                    move_block='up'
                elif event.key == pygame.K_DOWN:
                    move_block='down'
                elif event.key == pygame.K_n:
                    if cube.get_mode()=='finish':
                        image=pygame.image.load('成功.png').convert_alpha()
                        draw_alpha_rect(screen,(0,0,0),180,pygame.Rect(100,50,800,400),30)
                        screen.blit(image,(200,15))
                        again=pygame.image.load('again.png').convert_alpha()
                        next_level=pygame.image.load('next.png').convert_alpha()
                        home=pygame.image.load('home.png').convert_alpha()
                        screen.blit(again,(800,150))
                        screen.blit(next_level,(800,270))
                        screen.blit(home,(800,270+120))
                        again_rect=pygame.Rect(800,150,75,75)
                        next_rect=pygame.Rect(800,270,75,75)
                        home_rect=pygame.Rect(800,270+120,75,75)
                        while 1:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                            pos=pygame.mouse.get_pos()
                            if pygame.mouse.get_pressed()[0]:
                                if again_rect.collidepoint(pos[0],pos[1]):
                                    leveldata=gamedata(level)
                                    cube=Cube(leveldata,(0,0))
                                    break
                                elif next_rect.collidepoint(pos[0],pos[1]):
                                    try:
                                        level+=1
                                        leveldata=gamedata(level)
                                        cube=Cube(leveldata,(0,0))
                                        break
                                        #print(leveldata)
                                    except:
                                        return 
                                elif home_rect.collidepoint(pos[0],pos[1]):
                                    return
                            pygame.display.update()
                    elif cube.get_mode()=='goto':
                        info = cube.data['front'][cube.y][cube.x].info#获取格子传送位置
                        if info[0] == 'behind':#传送到背面（相对当前面）
                            cube.rotate3d('up')
                            cube.rotate3d('up')
                        elif info[0] in ['left','right','up','down']:#传送到其他面
                            cube.rotate3d(info[0])#直接换面
                        cube.x, cube.y = info[1], info[2]    
        draw_alpha_rect(screen,(29,83,0xbb),255,pygame.Rect(0,0,1200,674),0)
        if move_block!=None:
            move_num+=50
            if move_num==200:
                move_num=0
                move_block=None
            if move_block=='left':
                if move_num<100:
                    cube.show(screen,move_num,0)
                elif move_num==100:
                    cube.show(screen,move_num,0)
                    cube.move('left')
                else:
                    cube.show(screen,-(200-move_num),0)
            elif move_block=='right':
                if move_num<100:
                    cube.show(screen,-move_num,0)
                elif move_num==100:
                    cube.show(screen,-move_num,0)
                    cube.move('right')
                else:
                    cube.show(screen,200-move_num,0)
            elif move_block=='up':
                if move_num<100:
                    cube.show(screen,0,move_num)
                elif move_num==100:
                    cube.show(screen,0,move_num)
                    cube.move('up')
                else:
                    cube.show(screen,0,-(200-move_num))   
            else:
                if move_num<100:
                    cube.show(screen,0,-move_num)
                elif move_num==100:
                    cube.show(screen,0,-move_num)
                    cube.move('down')
                else:
                    cube.show(screen,0,200-move_num)  
        else:
            cube.show(screen,0,0)
        draw_circle_alpha()
        draw_mb_alpha()
        ch={
            'left':'左',
            'right':'右',
            'behind':'背',
            'up':'上',
            'down':'下',
        }
        if cube.get_mode()=='goto':
            show_text(screen,"提示：按N键可以传送到"+ch[cube.get_data().info[0]]+"面",(255,255,255),(60,550),40)
        if cube.get_mode()=='finish':
            show_text(screen,"提示：按N键进入下一关",(255,255,255),(60,550),48)
        show_text(screen,"第"+str(level)+'关',(255,255,255),(60,60),48)
        again=pygame.image.load('again.png').convert_alpha()
        next_level=pygame.image.load('next.png').convert_alpha()
        home=pygame.image.load('home.png').convert_alpha()
        draw_alpha_rect(screen,(0xfc,0xaf,0x7b),100,pygame.Rect(350+3,280+3,420,95),border_radius=30)
        draw_alpha_rect(screen,(0xfc,0xaf,0x7b),255,pygame.Rect(350,280,420,95),border_radius=30)
        
        screen.blit(again,(750,570))
        screen.blit(next_level,(870,570))
        screen.blit(home,(870+120,570))
        again_rect=pygame.Rect(750,570,75,75)
        next_rect=pygame.Rect(870,570,75,75)
        home_rect=pygame.Rect(870+120,570,75,75)
        draw_alpha_rect(screen,(0x3b,0xc4,0xb1),100,pygame.Rect(350+3,30+3,420,480),border_radius=30)
        draw_alpha_rect(screen,(0x3b,0xc4,0xb1),255,pygame.Rect(350,30,420,480),border_radius=30)
        if canzb:
            show_text(screen,'作弊模式专享：',color=(255,255,255),pos=(730,100),size=36)
            if level==5:
                draw_rect(cube,70,170,750)
            else:
                draw_rect(cube,100,190,760)
        else:
            show_text(screen,'当前不是作弊模式',color=(255,255,255),pos=(730,100),size=30)
            show_text(screen,'所以无法使用',color=(255,255,255),pos=(730,143),size=30)
            show_text(screen,'但是可以点个赞支持一下吗？',color=(255,255,255),pos=(730,143+43),size=30)
            show_text(screen,'原作者：',color=(255,255,255),pos=(730,143+43+43),size=30)
            head_xx=pygame.image.load('friend.png').convert_alpha()
            head_my=pygame.image.load('my.png').convert_alpha()
            screen.blit(head_xx,(880,143+43+43))
            show_text(screen,'小轩',color=(255,255,255),pos=(880+30,143+43+43+100+10),size=20)
            show_text(screen,'改编作者：',color=(255,255,255),pos=(730,143+43+43+100+40),size=30)
            screen.blit(head_my,(880,143+43+43+100+40))
            show_text(screen,'黄羿杰',color=(255,255,255),pos=(880+20,143+43+43+100+40+100+10),size=20)
            show_text(screen,'部分图片素材来源于共创世界POCO的《超阀》',color=(255,255,255),pos=(730,143+43+293+28),size=18)
        pos=pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if again_rect.collidepoint(pos[0],pos[1]):
                pygame.time.delay(100)
                leveldata=gamedata(level)
                cube=Cube(leveldata,(0,0))
            elif next_rect.collidepoint(pos[0],pos[1]):
                pygame.time.delay(100)
                try:
                    level+=1
                    leveldata=gamedata(level)
                    cube=Cube(leveldata,(0,0))
                except:
                    return
            elif home_rect.collidepoint(pos[0],pos[1]):
                return
        
        pygame.display.update()
        if move_block!=None:
            pygame.time.delay(10)
go()
gameinit()
