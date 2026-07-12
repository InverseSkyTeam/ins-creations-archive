import pygame,sys,os,text_input_box as txt
from pygame.locals import *
#import pygame.scrap
import time
try:#这个代码有3种情况 1、pygame版本<1.9.6,此时不支持pygame.version.vernum.major语法，直接报错
    #2、 1.9.6≤pygame版本<2.3，此时if语句成立，被强制报错
    #3、 2.3≤pygame版本 ,没有任何事情发生
    print("pygame当前版本：",pygame.version.vernum)
    if not (pygame.version.vernum.major>=2 and pygame.version.vernum.minor>=3):
        int('aaa')#强制报错
except:
    print('这个程序的代码已经支持了pygame2.5.0，而且在2.5.0版本下你会获得更好的效果')
    print('风险提示：新版pygame2.5.0不会兼容pygame旧版的代码（至少在中国会这样）')
    print('    在使用pygame2.5.0运行旧版代码时，您需要把输入法调成英文，')
    print('    或者在旧版程序源代码前加上“pygame.key.stop_text_input()”')
    print('    具体原因详见官方文档：https://www.pygame.org/docs/ref/key.html#pygame.key.start_text_input ')
    ans=input("你的pygame版本过低，是否更新？（回复“是”或“否”）")
    if ans=='是':
        os.system(sys.executable+" -m pip install --upgrade pygame --user")

os.environ["SDL_IME_SHOW_UI"] = "1"

pygame.init()
WIDTH=700
HEIGHT=500
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("pygame代码编辑器（v0.4）")
txt1=txt.TextInput([20,20],'ttf.ttf',24,WIDTH,HEIGHT)
import os
pygame.key.start_text_input()
input_rect = pygame.Rect(80, 80, 320, 40)
pygame.key.set_text_input_rect(input_rect)#这个好像没用？
in_move=0
off_x=-1
off_y=-1
pygame.key.set_repeat(450, 25)
pygame.time.set_timer(USEREVENT, 500)

numm=True
show_index=None
while True:
    events=pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # 滚轮向上滚动
                txt1.in_rect_md=False
                txt1.show_rect=False
                txt1.pos[1]+=50
                txt1.pos[1]=min(20,txt1.pos[1])
                #print(txt1.pos[1])
            elif event.button == 5:
                txt1.in_rect_md=False
                txt1.show_rect=False
                txt1.pos[1]-=50
                txt1.pos[1]=min(max(HEIGHT-len(txt1.get_txt(0))*(txt1.font_size+3),txt1.pos[1]),20)
        elif event.type == WINDOWFOCUSLOST: #窗口失去焦点，隐藏输入光标
            show_index = False      
        elif event.type == WINDOWFOCUSGAINED: #窗口获取焦点，显示输入光标
            show_index = True
        elif event.type == USEREVENT:
            if show_index:
                numm=not numm
            else:
                numm=True
    screen.fill((255,255,255))
    if txt1.get_txt(0)==[''] and txt1.get_txt(1)=='':
        screen.blit(txt1.draw_one('在这里输入代码',(255//2,255//2,255//2),False),(20,20))
    txt1.render_txt(screen,numm,can_mouse=not in_move)
    maxy=min(HEIGHT-len(txt1.get_txt(0))*(txt1.font_size+3),20)
    if maxy!=20:
        #print((txt1.pos[1])/(20-maxy))
        scl_r=pygame.Rect(WIDTH-10,(HEIGHT-30)*((txt1.pos[1]-20)/(0-(20-maxy))),10,30)
        pygame.draw.rect(screen,(127-(in_move==1)*30,127-(in_move==1)*30,127-(in_move==1)*30),scl_r,  width=0, border_radius=30)
        if pygame.mouse.get_pressed()[0]:
            mpos=pygame.mouse.get_pos()
            if not in_move and scl_r.collidepoint(mpos):
                in_move=1
                off_y=mpos[1]-scl_r.y
            if in_move==1:
                scl_r.y=mpos[1]-off_y
                scl_r.y=min(max(scl_r.y,0),HEIGHT-30)
                txt1.pos[1]=20-abs(20-maxy)*(scl_r.y/(HEIGHT-30))
                #txt1.pos[1]=int(txt1.pos[1])
                #print((scl_r.y/(HEIGHT-30)))
        else:
            in_move=0
    if txt1.maxx>WIDTH:
        #print((abs(txt1.pos[0]-20)-WIDTH))
        sclx_r=pygame.Rect((WIDTH-40)*(abs(txt1.pos[0]-20)/(txt1.maxx-WIDTH)),HEIGHT-10,30,10)
        pygame.draw.rect(screen,(127-(in_move==2)*30,127-(in_move==2)*30,127-(in_move==2)*30),sclx_r,  width=0, border_radius=30)
        if pygame.mouse.get_pressed()[0]:
            mpos=pygame.mouse.get_pos()
            if not in_move and sclx_r.collidepoint(mpos):
                in_move=2
                off_x=mpos[0]-sclx_r.x
            if in_move==2:
                sclx_r.x=mpos[0]-off_x
                sclx_r.x=min(max(sclx_r.x,0),WIDTH-40)
                txt1.pos[0]=20-(txt1.maxx-WIDTH)*(sclx_r.x/(WIDTH-40))
        else:
            in_move=0
    #print(1,txt1.xz_pos)
    #print(pygame.event.get_keyboard_grab())
    txt1.update(events,can_mouse=not in_move)
    #print(2,txt1.xz_pos)
    pygame.display.update()
    pygame.time.Clock().tick(60)