import pygame
import pygame.gfxdraw
import move
import time,sys
import webbrowser as wb
def ooO00OOoOo__():
    num=44777015#作品的pid
    num=int(num)
    try:
        OOooOo0Oo0=open(eval("b'\\x61\\x73\\x73\\x65\\x74'").decode()+'_info.json','r')#读取asset_info.json的内容
        OOooOo00o0=OOooOo0Oo0.read()
        OOooOo0Oo0.close()
        if int(OOooOo00o0[OOooOo00o0.find('"id":')+6:][:OOooOo00o0[OOooOo00o0.find('"id":')+6:].find(",")])!=num:#通过许多奇技淫巧代替re进行分析
            return int(OOooOo00o0)#如果是盗的作品，把输出函数改为一个错值，让程序报错，从而进入下面的excpet
        return sys.stdout#如果是原作，正常输出
    except:
        #输出提示信息
        print(chr(26816)+chr(27979)+chr(21040)+chr(36825)+chr(20010)+chr(20316)+chr(21697)+chr(26159)+chr(30423)+chr(21462)+chr(20182)+chr(20154)+chr(30340)+chr(20316)+chr(21697)+chr(65292)+chr(35831)+chr(21040)+chr(21407)+chr(20316)+chr(32773)+chr(32593)+chr(31449)+chr(19978)+chr(36816)+chr(34892))
        print(chr(51)+chr(31186)+chr(21518)+chr(33258)+chr(21160)+chr(36339)+chr(36716)+chr(33267)+chr(21407)+chr(20316)+chr(32773)+chr(32593)+chr(31449))
        time.sleep(2)
        #打开原作者网站
        wb.open(chr(104)+chr(116)+chr(116)+chr(112)+chr(115)+chr(58)+chr(47)+chr(47)+chr(99)+chr(111)+chr(100)+chr(101)+chr(46)+chr(120)+chr(117)+chr(101)+chr(101)+chr(114)+chr(115)+chr(105)+chr(46)+chr(99)+chr(111)+chr(109)+chr(47)+chr(104)+chr(111)+chr(109)+chr(101)+chr(47)+chr(112)+chr(114)+chr(111)+chr(106)+chr(101)+chr(99)+chr(116)+chr(47)+chr(100)+chr(101)+chr(116)+chr(97)+chr(105)+chr(108)+chr(63)+chr(108)+chr(97)+chr(110)+chr(103)+chr(61)+chr(99)+chr(111)+chr(100)+chr(101)+chr(38)+chr(112)+chr(105)+chr(100)+chr(61)+str(int(num))+chr(38)+chr(118)+chr(101)+chr(114)+chr(115)+chr(105)+chr(111)+chr(110)+chr(61)+chr(111)+chr(102)+chr(102)+chr(108)+chr(105)+chr(110)+chr(101)+chr(38)+chr(102)+chr(111)+chr(114)+chr(109)+chr(61)+chr(112)+chr(121)+chr(116)+chr(104)+chr(111)+chr(110)+chr(38)+chr(108)+chr(97)+chr(110)+chr(103)+chr(84)+chr(121)+chr(112)+chr(101)+chr(61)+chr(112)+chr(121)+chr(116)+chr(104)+chr(111)+chr(110))
        return sys.exit()

sys.stdout=ooO00OOoOo__()
print('',end='')
if '使用帮助':
    move_help='''
    这个非线性移动使用了贝塞尔曲线，模仿了css的cubic-bezier
    move.cubic_bezier([x,y,x1,y1],time)
    ！！！特别说明，为了保证一定的精度，所有控制的坐标为css原属性对应坐标的100倍
    x:第二个控制点的x坐标（0-100）
    y:第二个控制点的y坐标（0-100）
    x1:第三个控制点的x坐标（0-100）
    y1:第三个控制点的y坐标（0-100）
    time:在任务执行的百分比（0-100）
    返回在当前 任务执行的百分比 下对应的非线性百分比（返回值在0-100之间，若想变成百分数需要除以100）
    比如线性移动时，过去了总移动时间的10%，那么就移动了总移动距离的10%
    而非线性移动，则会让此时的移动距离不是总移动距离的10%，从而达到变速效果
    示例伪代码（部分）：
    import move
    起始位置=...
    结束位置=...
    当前位置=起始位置
    for time in range(0,100+1):
        移动总距离=结束位置-起始位置
        当前移动距离=移动总距离*move.cubic_bezier(x,y,x1,y1,time)/100
        绘制图形（位置=起始位置+当前移动距离）
        刷新屏幕
    '''

# 定义常量
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 初始化pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#初始化字体
try:import ntpath
except:
    exec("def show_text(text,color=(0,0,0),pos=(0,0),size=30,ag=0):screen.blit(pygame.transform.rotate(pygame.font.SysFont('kaittf', size).render((text),True,color),ag),pos)")
    #这里提前把“非线性”的文字加载，进一步减少延迟
    txt=pygame.font.SysFont('kaittf', 20).render(('非'),True,(255,255,255))
    txt1=pygame.font.SysFont('kaittf', 20).render(('线性'),True,(255,255,255))
else:
    exec("def show_text(text,color=(0,0,0),pos=(0,0),size=30,ag=0):screen.blit(pygame.transform.rotate(pygame.font.SysFont('kaiti', size).render((text),True,color),ag),pos)")
    txt=pygame.font.SysFont('kaiti', 20).render(('非'),True,(255,255,255))
    txt1=pygame.font.SysFont('kaiti', 20).render(('线性'),True,(255,255,255))
finally:pass

#初始化图片
main_bezier=move.bezier(20,300+150-20,90,402,150,60,300,150)#初始化主贝塞尔曲线
bezier_bg=pygame.image.load('image/bezier_bg.jpg')#主贝塞尔曲线背景
bezier_bg=pygame.transform.scale(bezier_bg, (main_bezier.x3-main_bezier.x0,main_bezier.x3-main_bezier.x0))#调整背景大小到主贝塞尔曲线的宽高
bg_rect=pygame.Rect(main_bezier.x0,main_bezier.y3,main_bezier.x3-main_bezier.x0,main_bezier.x3-main_bezier.x0)#设置背景的rect
#print(bezier_bg.get_rect())
shadow=[pygame.transform.scale(pygame.image.load('image/shadow_up.png').convert_alpha(),(main_bezier.x3-main_bezier.x0,50)),pygame.transform.scale(pygame.image.load('image/shadow_down.png').convert_alpha(),(main_bezier.x3-main_bezier.x0,50))]#初始化主贝塞尔曲线旁边的两个阴影

#全局flag
isgo=False#是否在预览过程中

#转换函数
def ins_to_xy(main_bezier,data):#把控制点相对位置转换为全局xy
    #main_bezier：对应的贝塞尔绘制区域    data:四个控制点位置
    a,b,c,d=data[0],data[1],data[2],data[3]
    num=main_bezier.x3-main_bezier.x0#贝塞尔曲线区域的长宽
    a,b,c,d=a*num/100,(100-b)*num/100,c*num/100,(100-d)*num/100#因为相对位置的y轴正半轴是朝上的，所以对应纵坐标先转换再按比例放大
    a,b,c,d=main_bezier.x0+a,main_bezier.y3+b,main_bezier.x0+c,main_bezier.y3+d#把放大后的相对坐标加上贝塞尔曲线到窗口边缘的距离，从而转换为绝对的坐标
    return [a,b,c,d]
[main_bezier.x1,main_bezier.y1,main_bezier.x2,main_bezier.y2]=ins_to_xy(main_bezier,move.data['ease'])#把初始的坐标设为ease
def text_render(data):#获取文字渲染长度
    res=[[0,0],[0,0],[0,0],[0,0]]
    for i in range(4):
        res[i][0]=str(data[i])
        res[i][1]=len(res[i][0])*18
        
    return res



#常用贝塞尔曲线的绘制区域设置

#常用贝塞尔曲线的rect
ease=pygame.Rect(330,110,100,100)
ease_in=pygame.Rect(450,110,100,100)
ease_out=pygame.Rect(570,110,100,100)
ease_in_out=pygame.Rect(330,240,100,100)
linear=pygame.Rect(450,240,100,100)

#初始化对应的贝塞尔曲线绘制区域
bezier_ease=move.bezier(ease.x+20,ease.y+ease.height-20,None,None,None,None,ease.x+ease.width-20,ease.y+20)
bezier_ease_in=move.bezier(ease_in.x+20,ease_in.y+ease_in.height-20,None,None,None,None,ease_in.x+ease_in.width-20,ease_in.y+20)
bezier_ease_out=move.bezier(ease_out.x+20,ease_out.y+ease_out.height-20,None,None,None,None,ease_out.x+ease_out.width-20,ease_out.y+20)
bezier_ease_in_out=move.bezier(ease_in_out.x+20,ease_in_out.y+ease_in_out.height-20,None,None,None,None,ease_in_out.x+ease_in_out.width-20,ease_in_out.y+20)
bezier_linear=move.bezier(linear.x+20,linear.y+linear.height-20,None,None,None,None,linear.x+linear.width-20,linear.y+20)

#把这些贝塞尔曲线的控制点设为对应名称的控制点
[bezier_ease.x1,bezier_ease.y1,bezier_ease.x2,bezier_ease.y2]=ins_to_xy(bezier_ease,move.data['ease'])
[bezier_ease_in.x1,bezier_ease_in.y1,bezier_ease_in.x2,bezier_ease_in.y2]=ins_to_xy(bezier_ease_in,move.data['ease-in'])
[bezier_ease_out.x1,bezier_ease_out.y1,bezier_ease_out.x2,bezier_ease_out.y2]=ins_to_xy(bezier_ease_out,move.data['ease-out'])
[bezier_ease_in_out.x1,bezier_ease_in_out.y1,bezier_ease_in_out.x2,bezier_ease_in_out.y2]=ins_to_xy(bezier_ease_in_out,move.data['ease-in-out'])
[bezier_linear.x1,bezier_linear.y1,bezier_linear.x2,bezier_linear.y2]=ins_to_xy(bezier_linear,move.data['linear'])

#把这些参数整合为一个列表，方便使用
other_bezier=[bezier_ease,bezier_ease_in,bezier_ease_out,bezier_ease_in_out,bezier_linear]
other_rect=[ease,ease_in,ease_out,ease_in_out,linear]
other_grad=[0,0,0,0,0]
other_end=[0,100,0,0,0]

#滚动条
max_pos=280#最大滚动长度（像素）
scroll_start_pos=350#最小滚动的绝对x坐标
scroll_end=320+300#最大滚动的绝对x坐标
scroll_pos=24#初始化滚动条相对x坐标
in_mouse=0#滚动条是否在拖动中
head=pygame.image.load('image/bz1.png').convert_alpha()#滚动条头部的圆球
time=round(scroll_pos/281*100)#把滚动条相对位置按比例分配给time_num列表
#这里打表是因为浮点的精度无法确定
time_num=['0.1','0.2','0.3','0.4','0.5','0.6','0.7','0.8','0.9','1.0','1.1','1.2','1.3','1.4','1.5','1.6','1.7','1.8','1.9','2.0','2.1','2.2','2.3','2.4','2.5','2.6','2.7','2.8','2.9','3.0','3.1','3.2','3.3','3.4','3.5','3.6','3.7','3.8','3.9','4.0','4.1','4.2','4.3','4.4','4.5','4.6','4.7','4.8','4.9','5.0','5.1','5.2','5.3','5.4','5.5','5.6','5.7','5.8','5.9','6.0',' 6.1','6.2','6.3','6.4','6.5','6.6','6.7','6.8','6.9','7.0','7.1','7.2','7.3','7.4','7.5','7.6','7.7','7.8','7.9','8.0','8.1','8.2','8.3','8.4','8.5','8.6','8.7','8.8','8.9','9.0','9.1','9.2','9.3','9.4','9.5','9.6','9.7','9.8','9.9','10.0']
step=0#预览的步长，即每一帧的任务需要执行总任务的百分比

#背景图片
screen_png=None#在预览里，会直接把预览前的样子截图保存，不进行主贝塞尔曲线和按钮的单独渲染，否则延迟会很长

#开始计数器
t=0
num=0
start_bz=330#预览时方块的起始位置
end_bz=700#预览时方块的结束位置
y=470#预览时方块的坐标

while True:
    # 处理游戏事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            import os
            try:
                os.remove('screen.png')
            except:
                pass
            pygame.quit()
            exit()
    if not isgo:
        screen.fill((255,255,255))
        if '贝塞尔曲线主窗口':
            screen.blit(shadow[0],(main_bezier.x0,main_bezier.y3-50))
            screen.blit(shadow[1],(main_bezier.x0,main_bezier.y0))
            screen.blit(bezier_bg,bg_rect)
            pygame.draw.line(screen,(153,153,153),(main_bezier.x0,main_bezier.y0),(main_bezier.x3,main_bezier.y0),2)
            pygame.draw.line(screen,(153,153,153),(main_bezier.x0,main_bezier.y0),(main_bezier.x0,main_bezier.y3),2)
            show_text('时间',(153,153,153),(main_bezier.x0,main_bezier.y0+5),15)
            show_text('任务进度',(153,153,153),(main_bezier.x0-15-3,main_bezier.y0-15*4),15,90)
            main_bezier.draw(screen,5,(0,0,0),3,(96,96,96),10,(255,255,255),10,(0xff,0x0,0x88),(0x0,0xaa,0xbb),1,not isgo)
        if '文字显示':
            start=100
            show_text('move.cubic_bezier(',(0,0,0),(start,20),30)
            text=text_render(main_bezier.get_bezier_point())
            show_text(text[0][0],(0xff,0x0,0x88),(start+30*9,20),30)
            show_text(',',(0,0,0),(start+30*9+text[0][1],20),30)
            show_text(text[1][0],(0xff,0x0,0x88),(start+30*9+text[0][1]+9,20),30)
            show_text(',',(0,0,0),(start+30*9+text[0][1]+9+text[1][1],20),30)
            show_text(text[2][0],(0x0,0xaa,0xbb),(start+30*9+text[0][1]+9+text[1][1]+18,20),30)
            show_text(',',(0,0,0),(start+30*9+text[0][1]+9+text[1][1]+text[2][1]+18,20),30)
            show_text(text[3][0],(0x0,0xaa,0xbb),(start+30*9+text[0][1]+9+text[1][1]+text[2][1]+27,20),30)
            show_text(')',(0,0,0),(start+30*9+text[0][1]+9+text[1][1]+text[2][1]+27++text[3][1],20),30)
            #print(main_bezier.get_bezier_point())
        if '常用函数窗口':
            show_text('常用的非线性移动：',(0,0,0),(320,70),30)
            pygame.draw.rect(screen,move.grad_data[other_grad[0]],ease,border_radius=10)
            pygame.draw.rect(screen,move.grad_data[other_grad[1]],ease_in,border_radius=10)
            pygame.draw.rect(screen,move.grad_data[other_grad[2]],ease_out,border_radius=10)
            pygame.draw.rect(screen,move.grad_data[other_grad[3]],ease_in_out,border_radius=10)
            pygame.draw.rect(screen,move.grad_data[other_grad[4]],linear,border_radius=10)
            for i in range(5):
                if other_grad[i]!=other_end[i]:
                    if other_end[i]==100:
                        other_grad[i]+=20
                    else:
                        other_grad[i]-=20
                    if other_grad[i]>100:
                        other_grad[i]=100
                    if other_grad[i]<0:
                        other_grad[i]=0
            for i in range(5):
                if other_rect[i].collidepoint(pygame.mouse.get_pos()):
                    other_end[i]=100
                    if pygame.mouse.get_pressed()[0] and not isgo:
                        [main_bezier.x1,main_bezier.y1,main_bezier.x2,main_bezier.y2]=ins_to_xy(main_bezier,move.data1[i])
                else:
                    other_end[i]=0
            for i in other_bezier:
                i.draw1(screen,2,(0,0,0),1,(153,153,153),2,(0,0,0),2,(153,153,153),(153,153,153),0,0)
            show_text('ease',(153,153,153),(358,210),20)
            show_text('ease-in',(153,153,153),(463,210),20)
            show_text('ease-out',(153,153,153),(580,210),20)
            show_text('ease-in-out',(153,153,153),(325,340),20)
            show_text('linear',(153,153,153),(472,340),20)
            #177,210,214
        if '预览&比较（滚动条）':
            show_text('预览 & 比较：',(0,0,0),(320,370),30)
            show_text('时间：',(153,153,153),(330,410),15)
            pygame.draw.rect(screen,(0xee,0xee,0xee),pygame.Rect(330,430,300,20),border_radius=30)
            pygame.draw.rect(screen,(255,204,231),pygame.Rect(330,430,20+scroll_pos,20),border_radius=30)
            pygame.draw.rect(screen,(0xdd,0xdd,0xdd),pygame.Rect(328,428,304,24),2,border_radius=30)
            head_rect=pygame.Rect(scroll_start_pos+scroll_pos-20,430,20,20)
            screen.blit(head,head_rect)
            if main_bezier.move:
                in_mouse=0
            if pygame.mouse.get_pressed()[0] and not isgo:
                if head_rect.collidepoint(pygame.mouse.get_pos()) and not in_mouse:
                    in_mouse=1
                elif in_mouse:
                    mouse_x=pygame.mouse.get_pos()[0]
                    scroll_pos=mouse_x-scroll_start_pos
                    scroll_pos=max(scroll_pos,0)
                    scroll_pos=min(scroll_pos,280)
            else:
                in_mouse=0
            time=round(scroll_pos/282*100)
            show_text(time_num[time]+'秒',(153,153,153),(650,427),20)
        if '开始按钮':
            button_rect=pygame.Rect(530,370,40,30)
            button_color=(0xcc,0xcc,0xcc)
            if not isgo and not in_mouse:
                if button_rect.collidepoint(pygame.mouse.get_pos()):
                    button_color=(0xff,0x0,0x88)
                    if pygame.mouse.get_pressed()[0]:
                        isgo=1
            pygame.draw.rect(screen,button_color,button_rect,border_radius=5)
            show_text('GO!',(255,255,255),(535,373),22)
            if isgo:
                pygame.draw.rect(screen,(0xcc,0xcc,0xcc),button_rect,border_radius=5)
                show_text('GO!',(255,255,255),(535,373),22)
                #pygame.display.flip()
                pygame.image.save(screen,'screen.png')#保存背景
                screen_png=pygame.image.load('screen.png')
                step=100/60/float(time_num[time])
                flag=0
                if t:
                    start_bz,end_bz=end_bz,start_bz
                    flag=1
                t=0
                continue
    else:#开始
        screen.blit(screen_png,(0,0))
        #pygame.draw.rect(screen,(0xff,0x0,0x88),pygame.Rect(start_bz+((end_bz-start_bz)*num/100),y,50,50),border_radius=10)
        if t>100:
            t=100
            isgo=0
        num=move.cubic_bezier(main_bezier.get_bezier_point(),t)
        t+=step
    #print(start+(end-start)*num/100)
    pygame.draw.rect(screen,(0xff,0x0,0x88),pygame.Rect(start_bz+((end_bz-start_bz)*num/100),y,50,50),border_radius=10)
    screen.blit(txt,(start_bz+((end_bz-start_bz)*num/100)+15,y+5))
    screen.blit(txt1,(start_bz+((end_bz-start_bz)*num/100)+5,y+23))
    #print((t-step)/100)
    pygame.draw.rect(screen,(0x0,0xaa,0xbb),pygame.Rect(start_bz+(end_bz-start_bz)*(t-step)/100,y+70,50,50),border_radius=10)
    screen.blit(txt1,(start_bz+(end_bz-start_bz)*(t-step)/100+5,y+13+70))
    pygame.display.flip()
    #import time
    #time.sleep(0.03)
    # 控制游戏帧率
    pygame.time.Clock().tick(60)
