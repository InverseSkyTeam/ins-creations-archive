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
