import pygame,sys,tkinter as tk,random,time
from moviepy.editor import *
pygame.init()

mouse_x = 0
mouse_y = 0
def vp():
    print({'主要编写':'胡锦辉','写帮助、修改':'小轩'})

def create_screen(width,height,name = "gameeasy",ico = 0):
    global screen
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption(name)
    if ico != 0:
        ico = pygame.image.load(ico)
        pygame.display.set_icon(ico)
    return width,height

def fill(color):
    screen.fill(color)

def exit():
    global event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def getevent():
    global event
    for i in pygame.event.get():
        event = i

def refresh():
    pygame.display.update()
    
def draw(img,pos):
    screen.blit(img,pos)

def load(img):
    image = pygame.image.load(img)
    return image
    
def resize(img,size):
    image = pygame.transform.scale(img,size)
    return image

def collide_image(img1,img2):
    collidestate = False
    x1 = img1.x
    y1 = img1.y
    x2 = img2.x
    y2 = img2.y
    img1_rect = img1.get_rect()
    img2_rect = img2.get_rect()
    img1_rect.x = x1
    img1_rect.y = y1
    img2_rect.x = x2
    img2_rect.y = y2
    if img1_rect.colliderect(img2_rect):
        collidestate = True
    else:
        collidestate = False
    return collidestate

def rotate_image(img,degree):
    image = pygame.transform.rotate(ing,degree)
    return image
    
def text(font = "楷体",size = 20,color = (0,0,0),word = "",pos = (0,0)):
    if font == "黑体":
        try:
            import ntpath # 如果成功，那么是Windows
            FONTNAME = "Simhei"
            del ntpath
        except ImportError: # 如果失败，是MacOS
            FONTNAME = "heititf"
    if font == "楷体":
        try:
            import ntpath # 如果成功，那么是Windows
            FONTNAME = "kaiti"
            del ntpath
        except ImportError: # 如果失败，是MacOS
            FONTNAME = "kaittf"
    screen.blit(pygame.font.SysFont(FONTNAME,size).render(word,True,color),pos)

def print_mouse_pos():
    global event
    if event.type == pygame.MOUSEBUTTONDOWN:
        print(event.pos)

def mouse_motion():
    global event
    flags1 = False
    if event.type == pygame.MOUSEMOTION:
        flags1 = True
    else:
        flags1 = False
    return flags1
    
def get_mouse_pos():
    global event,mouse_x,mouse_y
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x = event.pos[0]
        mouse_y = event.pos[1]
    
def mouse_button_down():
    global event
    flags1 = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        flags1 = True
    else:
        flags1 = False
    return flags1

def mouse_left_button_down():
    global event
    flags1 = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button==1:
            flags1 = True
    else:
        flags1 = False
    return flags1

def mouse_right_button_down():
    global event
    flags1 = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button==3:
            flags1 = True
    else:
        flags1 = False
    return flags1
    
def mouse_right_button_up():
    global event
    flags1 = False
    if event.type == pygame.MOUSEBUTTONUP:
        if event.button==3:
            flags1 = True
    else:
        flags1 = False
    return flags1
    
def mouse_left_button_up():
    global event
    flags1 = False
    if event.type == pygame.MOUSEBUTTONUP:
        if event.button==1:
            flags1 = True
    else:
        flags1 = False
    return flags1

def mouse_button_up():
    global event
    flags1 = False
    if event.type == pygame.MOUSEBUTTONUP:
        flags1 = True
    else:
        flags1 = False
    return flags1

def mouse_roller_up():
    global event
    flags1 = False
    if event.type == pygame.MOUSEBUTTONUP:
        if event.button==4:
            flags1 = True
            event.button = 0
    else:
        flags1 = False
    return flags1
    
def mouse_roller_down():
    global event
    flags1 = False
    if event.type == pygame.MOUSEBUTTONUP:
        if event.button==5:
            flags1 = True
            event.button = 0
    else:
        flags1 = False
    return flags1

def key_down():
    global event
    flags1 = False
    if event.type == pygame.KEYDOWN:
        flags1 = True
    else:
        flags1 = False
    return flags1
    
def key_up():
    global event
    flags1 = False
    if event.type == pygame.KEYUP:
        flags1 = True
    else:
        flags1 = False
    return flags1
    
def key_down_is():
    global event
    flags1 = False
    if event.type == pygame.KEYDOWN:
        flags1 = event.key
    else:
        flags1 = False
    return flags1
    
def key_up_is():
    global event
    flags1 = False
    if event.type == pygame.KEYUP:
        flags1 = event.key
    else:
        flags1 = False
    return flags1
    
def key(name):
    keyname = ord(name)
    return keyname

def play_bgmusic(bg):
    pygame.mixer.music.load(bg)
    pygame.mixer.music.play(-1)

def play_video(vedeo,size,name,time=0):
    pygame.display.set_caption(name)
    clip = VideoFileClip(vedeo)
    clip= clip.resize(newsize=size)
    clip.preview()
    pygame.time.delay(time*1000)

def collide_mouse(img1):
    collidestate = False
    x1 = img1.x
    y1 = img1.y
    img1_rect = img1.get_rect()
    img1_rect.x = x1
    img1_rect.y = y1
    if img1_rect.collidepoint(mouse_x,mouse_y):
        collidestate = True
    else:
        collidestate = False
    return collidestate

def creat_gui(name="gameeasy",size = (200,200)):
    import wxpython as wx                   #导入wx包
    app = wx.App()                          #创建应用程序对象
    win = wx.Frame(None,-1,name)            #创建窗体
    win.Show()                              #显示窗体
    app.MainLoop()  

def screen_shot(pos1,pos2,name):
    global width,height
    x1 = pos1[0]
    y1 = pos1[1]
    x2 = pos2[0]
    y2 = pos2[1]
    screen1 = pygame.transform.chop(screen1,(0, 0,x1, y1))
    screen1 = pygame.transform.chop(screen1,(x2, y2,width, height))
    pygame.image.save(screen1,name)
    
def draw_rect(pos,width,height,lenth,color):
    x = pos[0]
    y = pos[1]
    rect = pygame.Rect(x,y,width,height)
    pygame.draw.rect(screen,color,rect,lenth)

def helper():
    from main import gz
    gz.create_screen(1580,720,"gameeasy")
    img1 = gz.load("img/基本代码.png")
    img1 = gz.resize(img1,(570,150))
    img2 = gz.load("img/图像处理部分.png")
    img2 = gz.resize(img2,(570,280))
    img3 = gz.load("img/音乐处理部分.png")
    img3 = gz.resize(img3,(570,180))
    img4 = gz.load("img/基础代码2级.png")
    img4 = gz.resize(img4,(1000,280))
    img5 = gz.load("img/鼠标事件监测.png")
    img6 = gz.load("img/键盘事件.png")
    img7 = gz.load("img/初级代码.png")
    img8 = gz.load("img/举个栗子.png")
    r1 = pygame.Rect(0,60,105,25)
    r2 = pygame.Rect(105,60,165,25)
    y = 0
    y2 = 0
    page = 1
    while True:
        gz.exit()
        if gz.mouse_roller_down():
            if page == 1:
                y -= 80
                if y < -2700:
                    y = -2700
            else:
                y2 -= 80
                if y2 < -600:
                    y2 = -600
        if gz.mouse_roller_up():
            if page == 1:
                y += 80
                if y > 0:
                    y = 0
            else:
                y2 += 80
                if y2 > 0:
                    y2 = 0
        if gz.mouse_button_down():
            if r1.collidepoint(event.pos):page = 1
            if r2.collidepoint(event.pos):page = 2
        gz.print_mouse_pos()
        gz.fill((255,255,255))
        gz.draw_rect((0,85),1580,720,0,(220,220,220))
        if page == 1:
            gz.text(size = 23,word = "1.基本代码:",color = (0,0,0),pos = (0,90+y))
            gz.draw(img1,(0,120+y))
            gz.text(size = 23,word = "(1) 导入gameeasy库,并命名为gz  import gameeasy as gz",color = (255,0,0),pos = (395,120+y))
            gz.text(size = 23,word = "(2) 创建窗口  gz.creat_screen(宽度,高度,名称,图标(这个为选填参数，ico格式))",color = (255,0,0),pos = (565,152+y))
            gz.text(size = 23,word = "(3) 开启主循环 while True:",color = (255,0,0),pos = (225,182+y))
            gz.text(size = 23,word = "(4) 控制窗口在点击关闭按钮时关闭(如果不写这行代码则要写gz.get_event())  gz.exit()",color = (255,0,0),pos = (245,210+y))
            gz.text(size = 23,word = "(5) 刷新窗口  gz.refresh()",color = (255,0,0),pos = (284,240+y))
            
            gz.text(size = 23,word = "2.图像处理部分",color = (0,0,0),pos = (0,268+y))
            gz.draw(img2,(0,293+y))
            gz.text(size = 23,word = "(1) 加载图片  gz.load(图片名称.格式)  注意:双引号",color = (255,0,0),pos = (478,358+y))
            gz.text(size = 23,word = "(2) 更改图片大小  gz.resize(加载好的图片,大小)  注意:大小的结构是(长,宽)",color = (255,0,0),pos = (498,388+y))
            gz.text(size = 23,word = "(3) 旋转图片  gz.rotate_image(加载好的图片,旋转度数)",color = (255,0,0),pos = (498,418+y))
            gz.text(size = 23,word = "(4) 绘制图片  gz.draw(加载好的图片,位置)  注意:位置的结构是(横坐标,纵坐标)",color = (255,0,0),pos = (370,507+y))
            
            gz.text(size = 23,word = "3.音乐处理部分",color = (0,0,0),pos = (0,570+y))
            gz.draw(img3,(0,593+y))
            gz.text(size = 23,word = "(1) 播放音乐  gz.play_bgmusic(音乐名称.格式)",color = (255,0,0),pos = (420,660+y))
            
            gz.text(size = 23,word = "4.基础代码（2级）",color = (0,0,0),pos = (0,785+y))
            gz.draw(img4,(0,823+y))
            gz.text(size = 23,word = "(1) 当鼠标左键点击时，输出现在鼠标的坐标  gz.print_mouse_pos()",color = (255,0,0),pos = (420,950+y))
            gz.text(size = 23,word = " (2) 设置屏幕背景色  gz.fill((r,g,b)) r:red值 g:green值 b:blue值，光学三原色：红绿蓝",color = (255,0,0),pos = (420,980+y))
            gz.text(size = 23,word = "(第7行) 绘制矩形  gz.draw_rect((x坐标,y坐标),屏幕宽,屏幕高,绘制层数,(r,g,b)) ",color = (255,0,0),pos = (10,1110+y))
            gz.text(size = 23,word = "注意：屏幕宽高是和creat_screen中一样的，绘制层数如果为0，则填充颜色。括号很多请注意格式错误！！！",color = (255,0,0),pos = (10,1140+y))
            gz.text(size = 23,word = "(第8行) 显示文字  gz.text(font=字体（有黑体、楷体2种）,size=字体大小,word=文字,color=(r,g,b),pos=(x,y)) 温馨提示：会自动识别系统",color = (255,0,0),pos = (10,1170+y))
            gz.text(size = 23,word = "不用担心字体，默认值font楷体,size20,color(0,0,0)(黑色),word空,pos(0,0)",color = (255,0,0),pos = (10,1200+y))
            
            gz.text(size = 23,word = "5.鼠标事件",color = (0,0,0),pos = (0,1230+y))
            gz.text(size = 23,word = "如果你上面的都看懂了，那么就可以从这里开始深入学习了，注意鼠标事件返回值一般为True或False",color = (0,51,255),pos = (10,1260+y))
            gz.draw(img5,(0,1290+y))
            
            gz.text(size = 23,word = "6.键盘事件",color = (0,0,0),pos = (0,2000+y))
            gz.draw(img6,(0,2030+y))
            
            gz.text(size = 23,word = "7.初级代码（基础代码3级）",color = (0,0,0),pos = (0,2400+y))
            gz.text(size = 23,word = "感谢你看到这里~您已把目前更新的看完了，nb，gz.vp()查看版权~~~",color = (0,220,0),pos = (10,2430+y))
            gz.text(size = 23,word = "一个函数都不漏地介绍了，请点击菜单栏的“代码示范~~~~~”",color = (0,180,0),pos = (10,2460+y))
            gz.draw(img7,(0,2490+y))
            
            gz.draw_rect((0,85),1580,5,0,(220,220,220))
            gz.draw_rect((0,0),1580,85,0,(255,255,255))
            gz.text(size = 35,word = "欢迎来到gameeasy的世界!",color = (0,0,0))
            gz.text(word = "gameeasy教程",pos = (0,35))
            
            pygame.draw.rect(screen,(220,220,220),r1,0)
            pygame.draw.rect(screen,(175,175,175),r2,0)
        else:
            gz.text(size = 23,word = "代码示范（举个栗子）",color = (0,0,0),pos = (0,90+y2))
            gz.draw(img8,(0,120+y2))
            
            gz.draw_rect((0,85),1580,5,0,(220,220,220))
            gz.draw_rect((0,0),1580,85,0,(255,255,255))
            gz.text(size = 35,word = "欢迎来到gameeasy的世界!",color = (0,0,0))
            gz.text(word = "gameeasy教程",pos = (0,35))
            
            pygame.draw.rect(screen,(175,175,175),r1,0)
            pygame.draw.rect(screen,(220,220,220),r2,0)
        
        gz.text(size = 15,word = "游戏制作部分",color = (0,0,0),pos = (6,62))
        gz.text(size = 15,word = "代码示范（举个栗子）",pos = (111,62))
        
        gz.refresh()