#coding:utf-8

import pygame
import sys
from time import sleep
from os import getcwd
from typing import Optional,Union,List,Tuple
from math import ceil
from traceback import format_exc
import json

# 弹窗类
class Window(pygame.Surface):
    def __init__(self, screen:Optional[pygame.Surface], color:Tuple[int,int,int], size:Union[Tuple[int,int], List[int], None] = (100,100),border_radius:Optional[int] = 10) -> None:
        self.screen = screen
        self.size = tuple(size)

        # 父类初始化
        super().__init__(self.size)

        # 高度 & 宽度
        self.width = self.size[0] # 弹窗宽度
        self.height = self.size[1] # 弹窗高度
        self.screen_width = self.screen.get_width() # pygame屏幕宽度
        self.screen_height = self.screen.get_height() # pygame屏幕高度

        # 位置
        self.x = (self.screen_width - self.width) // 2 
        self.y = (self.screen_height - self.height) // 2

        # 颜色
        self.color = color

        # 所在矩形
        self.rect = self.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        # 圆角
        self.border_radius = border_radius

        # 界面
        self.fill((255,255,255))
        pygame.draw.rect(self, self.color, (0,0,self.width, self.height), 0, border_radius=self.border_radius)
        self.set_colorkey(pygame.Color("white"))
    
    def gradient_appear(self) -> None:
        self.__screen = self.screen.copy()
        for alpha in range(0,181,5):
            self.set_alpha(alpha)
            self.screen.blit(self.__screen,(0,0))
            self.screen.blit(self,self.rect)
            pygame.display.update()
            pygame.time.delay(4)
    
    def fly_in_appear(self, side = "down") -> None:
        """
        :param side ->  up  表示从下往上飞入
                       down 表示从上往下飞入
        """
        try:
            self.__screen = screen.copy()
            if side == "down":
                y = self.y // 2
                sign = 1
            elif side == "up":
                y = self.screen_height - self.y // 2
                sign = -1
            for i in range(30):
                screen.blit(self.__screen,(0,0))
                screen.blit(self,(self.x,y+sign*i*round(abs(y-self.y)/30,1)))
                pygame.display.update()
                pygame.time.delay(4)
        except Exception as e:
            print(format_exc())
        
    def update(self) -> None:
        pygame.display.update(self.rect)

    def disappear(self) -> None:
        try:
            self.screen.blit(self.__screen,(0,0))
            pygame.display.update()
        except:
            raise pygame.error("the window has not appeared yet")



################
### 示例程序 ###
################

input("示例程序：pygame窗口打开后点击屏幕中央的设置按钮，重复三次即可观看三种不同的弹窗方式。\n\n按回车继续...")

volume = 50 #音量
fps = 100
FULLSCREEN = False

try:
    if getcwd().split("\\")[3] == "学而思直播":
        # 通过社区运行
        path = "../../联机游戏-疯狂六边形" # 缓存文件存放路径
    else:
        path = "./"
except:
    # 不是社区运行
    path = "./"

#检测系统
try:
    import ntpath # 用windows特有的ntpath库检测是否为windows
    FONTNAME = "kaiti" # 说明是windows
    del ntpath
except ImportError:
    FONTNAME = "kaittf" # 说明不是windows，字体应是kaittf

# 游戏初始化
pygame.init() # 窗口初始化
pygame.mixer.init() # 音乐初始化
screen = pygame.display.set_mode((1280,720)) # 初始化窗口大小
pygame.display.set_caption("联机游戏-疯狂六边形") # 初始化窗口标题

FontDict = {}

# 工具函数
def show_text(content:Optional[str],color:tuple,position:Union[list,tuple],size:int,master:pygame.Surface=screen,fontname = FONTNAME):
    global FontDict
    if f"font_{size}" in FontDict:
        master.blit(FontDict[f"font_{size}"].render(content,True,color),(position))
    else:
        FontDict[f"font_{size}"] = pygame.font.SysFont(fontname,size)
        show_text(content,color,position,size,master)

class setting: # 设置类
    # 类初始化
    def __init__(self):
        self.canvas = Window(screen,(50,50,50),(720,480),20) # 创建一个pygame的Surface对象作为画布
        self.Frame = pygame.Surface((720,450-20)) # 创建一个pygame的Surface对象作为下方区域
        self.Frame.fill((50,50,50)) # 将下方区域设置成指定颜色
        self.rect = pygame.Rect(280,120,720,480)
        self.close_rect = pygame.Rect(970,120,30,30)
        self.close_Surface = pygame.Surface((28,28))
        self.close_Surface.fill((230,0,0))
        self.close_Surface.set_alpha(0)
        self.music1_Surface = pygame.Surface((105,30))
        self.music1_Surface.fill((200,200,200))
        self.music2_Surface = pygame.Surface((105,30))
        self.music2_Surface.fill((200,200,200))
        self.music3_Surface = pygame.Surface((105,30))
        self.music3_Surface.fill((200,200,200))
        self.back_ground_music_list = [" 无 ","孤勇者","C418 "]
        self.back_ground_music = self.back_ground_music_list[0]
        self.choose_music_rect = pygame.Rect(635,203,15,15)
        self.music1_rect = pygame.Rect(550,195,105,30)
        self.music2_rect = pygame.Rect(550,226,105,30)
        self.music3_rect = pygame.Rect(550,257,105,30)
        self.zhankairect = pygame.Rect(550,195,105,93)
        self.zhankai_flag = 0
        self.set_volume_flag = 0
        self.set_volume_button_x = 420
        self.set_volume_button_y = 147
        self.set_volume_button_rect = pygame.Rect(self.set_volume_button_x+280,self.set_volume_button_y+150,6,33)
        self.set_FULLSCREEN_rect = pygame.Rect(268+280,247+150,30,30)
        self.set_FULLSCREEN_Surface = pygame.Surface((30,30))
        self.set_FULLSCREEN_Sprite = pygame.sprite.Sprite()
        self.set_FULLSCREEN_Sprite.image = self.set_FULLSCREEN_Surface
        self.set_FULLSCREEN_Sprite.rect = self.set_FULLSCREEN_rect
        self.set_FULLSCREEN_flag = 0
        self.set_fps_button_x = 370
        self.set_fps_button_y = 347
        self.set_fps_flag = 0
        self.set_fps_button_rect = pygame.Rect(self.set_fps_button_x+280,self.set_fps_button_y+150,6,33)
        
    # 显示界面
    def show(self,event):
        screen.blit(setting_A.canvas,(280,120)) # 绘制画布
        self.canvas.blit(self.Frame,(0,30))
        self.Frame.fill((50,50,50))
        screen.blit(self.close_Surface,(961,131))
        show_text("×",(120,120,120),(960,130),30)
        show_text("背景音乐",(200,200,200),(70,40),40,self.Frame)
        pygame.draw.rect(self.Frame,(200,200,200),((270,45),(105,30)),0)
        self.choose_music(event)
        if self.zhankai_flag:
            for i in self.back_ground_music_list:
                show_text(i,(50,50,50),(272,45+self.back_ground_music_list.index(i)*31),30,self.Frame)
        else:
            show_text(self.back_ground_music,(50,50,50),(272,45),30,self.Frame)
        show_text("设置音量",(200,200,200),(70,142),40,self.Frame)
        self.set_volume(event)
        self.set_FULLSCREEN(event)
        self.set_tick(event)
        pygame.display.update()
    
    def show_(self):
        self.Frame.fill((50,50,50))
        screen.blit(self.close_Surface,(681,11))
        show_text("×",(120,120,120),(960,130),30)
        show_text("背景音乐",(200,200,200),(70,40),40,self.Frame)
        pygame.draw.rect(self.Frame,(200,200,200),((270,45),(105,30)),0)
        show_text(self.back_ground_music,(50,50,50),(272,45),30,self.Frame)
        self.choose_music(None)
        show_text("设置音量",(200,200,200),(70,142),40,self.Frame)
        self.set_volume(None)
        self.set_FULLSCREEN(None)
        self.set_tick(None)
        self.canvas.blit(self.Frame,(0,30))
        self.update()
    
    # 更新界面
    def update(self):
        pygame.display.update(self.rect) # 只更新设置区域的画布
    
    # 选择音乐
    def choose_music(self,event):
        if not self.zhankai_flag:
            self.music2_Surface.fill((50,50,50))
            self.music3_Surface.fill((50,50,50))
            try:
                if self.music1_rect.collidepoint(event.pos):
                    self.music1_Surface.set_alpha(255)
                else:
                    self.music1_Surface.set_alpha(0)
            except:
                pass
            finally:
                self.Frame.blit(self.music1_Surface,(270,45))
                self.Frame.blit(self.music2_Surface,(270,76))
                self.Frame.blit(self.music3_Surface,(270,107))
                show_text("▼",(50,50,50),(355,53),15,self.Frame)
        else:
            try:
                if self.music1_rect.collidepoint(event.pos):
                    self.music1_Surface.fill((200,200,200))
                else:
                    self.music1_Surface.fill((150,150,150))
                if self.music2_rect.collidepoint(event.pos):
                    self.music2_Surface.fill((200,200,200))
                else:
                    self.music2_Surface.fill((150,150,150))
                if self.music3_rect.collidepoint(event.pos):
                    self.music3_Surface.fill((200,200,200))
                else:
                    self.music3_Surface.fill((150,150,150))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if not self.zhankairect.collidepoint(event.pos):
                        self.zhankai_flag = 0
                    if self.music1_rect.collidepoint(event.pos):
                        self.back_ground_music = self.back_ground_music_list[0]
                        try:
                            with open(path+"/data.json",'rb') as f:
                                last = eval(f.read())
                        except:
                            last = {}
                        with open(path+"/data.json",'wb') as f:
                            last["FULLSCREEN"]=FULLSCREEN
                            last["BACKGROUNDMUSIC"]="无"
                            last["VOLUME"]=volume
                            f.write(json.dumps(last).encode())
                        self.zhankai_flag = 0
                    elif self.music2_rect.collidepoint(event.pos):
                        pygame.mixer.music.load("./Music/孤勇者.mp3")
                        pygame.mixer.music.play(-1)
                        self.back_ground_music = self.back_ground_music_list[1]
                        try:
                            with open(path+"/data.json",'rb') as f:
                                last = eval(f.read())
                        except:
                            last = {}
                        with open(path+"/data.json",'wb') as f:
                            last["FULLSCREEN"]=FULLSCREEN
                            last["BACKGROUNDMUSIC"]="孤勇者.mp3"
                            last["VOLUME"]=volume
                            f.write(json.dumps(last).encode())
                        self.zhankai_flag = 0
                    elif self.music3_rect.collidepoint(event.pos):
                        pygame.mixer.music.load("./Music/C418.mp3")
                        pygame.mixer.music.play(-1)
                        self.back_ground_music = self.back_ground_music_list[2]
                        try:
                            with open(path+"/data.json",'rb') as f:
                                last = json.loads(f.read())
                        except:
                            last = {}
                        with open(path+"/data.json",'wb') as f:
                            last["FULLSCREEN"]=FULLSCREEN
                            last["BACKGROUNDMUSIC"]="C418.mp3"
                            last["VOLUME"]=volume
                            f.write(json.dumps(last).encode())
                        self.zhankai_flag = 0
            except:
                pass
            finally:
                self.Frame.blit(self.music1_Surface,(270,45))
                self.Frame.blit(self.music2_Surface,(270,76))
                self.Frame.blit(self.music3_Surface,(270,107))
                show_text("▲",(50,50,50),(355,53),15,self.Frame)
        try:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.choose_music_rect.collidepoint(event.pos):
                    sleep(0.05)
                    if self.zhankai_flag:
                        self.zhankai_flag = 0
                    else:
                        self.zhankai_flag = 1
        except:
            pass
    
    def set_volume(self,event):
        global volume
        pygame.draw.rect(self.Frame,(200,200,200),((270,160),(300,5)),0)
        pygame.draw.rect(self.Frame,(150,150,150),((self.set_volume_button_x,self.set_volume_button_y),(6,33)),0)
        # print(300/(self.set_volume_button_x-270)*100)
        # print(self.set_volume_button_x-270)
        show_text(str(int(ceil((self.set_volume_button_x-270)*100)/300))+'%',(200,200,200),(600,143),40,self.Frame)
        if self.set_volume_flag == 0:
            try:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.set_volume_button_rect.collidepoint(event.pos):
                        self.set_volume_flag = 1
            except:
                pass
        else:
            try:
                if event.type != pygame.MOUSEBUTTONUP:
                    if event.pos[0] <= 270+280:
                        self.set_volume_button_x = 270
                        self.set_volume_button_rect = pygame.Rect(self.set_volume_button_x+280,self.set_volume_button_y+150,6,33)
                        volume = int(ceil((self.set_volume_button_x-270)*100)/300)
                        pygame.mixer.music.set_volume(volume/100)
                    elif event.pos[0] >= 570+280:
                        self.set_volume_button_x = 570
                        self.set_volume_button_rect = pygame.Rect(self.set_volume_button_x+280,self.set_volume_button_y+150,6,33)
                        volume = int(ceil((self.set_volume_button_x-270)*100)/300)
                        pygame.mixer.music.set_volume(volume/100)
                    else:
                        self.set_volume_button_x = event.pos[0] - 280
                        self.set_volume_button_rect = pygame.Rect(self.set_volume_button_x+280,self.set_volume_button_y+150,6,33)
                        volume = int(ceil((self.set_volume_button_x-270)*100)/300)
                        pygame.mixer.music.set_volume(volume/100)
                else:
                    self.set_volume_flag = 0
            except:
                pass
        
    def set_FULLSCREEN(self,event):
        global FULLSCREEN
        show_text("全屏模式",(200,200,200),(70,242),40,self.Frame)
        show_text("按esc键退出全屏(有可能要多按几下才行)",(200,200,200),(318,252),20,self.Frame)
        pygame.draw.circle(self.Frame,(0,0,0),(283,262),15,2)
        mousex,mousey = pygame.mouse.get_pos()
        mouse_rect = pygame.Rect(mousex,mousey,5,5)
        mouse_Surface = pygame.Surface((5,5))
        mouse_Sprite = pygame.sprite.Sprite()
        mouse_Sprite.rect = mouse_rect
        mouse_Sprite.image = mouse_Surface
        if self.set_FULLSCREEN_flag:
            pygame.draw.ellipse(self.Frame,(0,0,0),(273,252,20,20))
        try:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.sprite.collide_circle(self.set_FULLSCREEN_Sprite,mouse_Sprite):
                    if self.set_FULLSCREEN_flag:
                        self.set_FULLSCREEN_flag = 0
                        pygame.display.set_mode((1280,720))
                        sleep(0.05)
                    else:
                        self.set_FULLSCREEN_flag = 1
                        pygame.display.set_mode((1280,720),flags=pygame.FULLSCREEN)
                        sleep(0.05)
                    pygame.display.update()
        except:
            pass
    def set_tick(self,event):
        global fps
        show_text("设置帧数",(200,200,200),(70,342),40,self.Frame)
        show_text(str(fps)+"帧",(200,200,200),(600,343),40,self.Frame)
        pygame.draw.rect(self.Frame,(200,200,200),((270,360),(300,5)),0)
        pygame.draw.rect(self.Frame,(150,150,150),((self.set_fps_button_x,self.set_fps_button_y),(6,33)),0)
        if self.set_fps_flag == 0:
            try:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.set_fps_button_rect.collidepoint(event.pos):
                        self.set_fps_flag = 1
            except:
                pass
        else:
            try:
                if event.type != pygame.MOUSEBUTTONUP:
                    if event.pos[0] <= 270+280:
                        self.set_fps_button_x = 270
                        self.set_fps_button_rect = pygame.Rect(self.set_fps_button_x+280,self.set_fps_button_y+150,6,33)
                        fps = int(ceil(self.set_fps_button_x-270))
                        clock.tick(fps)
                    elif event.pos[0] >= 570+280:
                        self.set_fps_button_x = 570
                        self.set_fps_button_rect = pygame.Rect(self.set_fps_button_x+280,self.set_fps_button_y+150,6,33)
                        fps = int(ceil(self.set_fps_button_x-270))
                        clock.tick(fps)
                    else:
                        self.set_fps_button_x = event.pos[0] - 280
                        self.set_fps_button_rect = pygame.Rect(self.set_fps_button_x+280,self.set_fps_button_y+150,6,33)
                        fps = int(ceil(self.set_fps_button_x-270))
                        clock.tick(fps)
                else:
                    self.set_fps_flag = 0
            except:
                pass

class Exit(Window):
    def __init__(self):
        self.fill((255,255,255))
        

# 导入图片
cover = pygame.image.load("./Image/封面.jpg").convert() # 导入封面图片
setting_image = pygame.image.load("./Image/设置.jpeg").convert_alpha() # 导入设置图片
setting_image = pygame.transform.scale(setting_image,(34,34)) # 调整图片大小

# 帧数
clock = pygame.time.Clock() # 初始化帧数变量

# 绘制初始界面
screen.blit(cover,(0,0)) # 绘制封面

pygame.draw.rect(screen,(60,100,255),((1230,10),(40,40)),0) # 绘制设置的矩形

screen.blit(setting_image,(1233,13)) # 绘制设置logo
show_text("设置",(255,255,255),(1230,50),20)

pygame.display.update() # 更新画布
running = True # 循环条件
times = 0
i = -1 # 循环变量，用于beta的展示
setting_A = setting() # 创建设置对象
shezhiflag = 0
shezhirect = pygame.Rect(620,340,40,40)
func = (setting_A.canvas.gradient_appear,lambda:setting_A.canvas.fly_in_appear("down"),lambda:setting_A.canvas.fly_in_appear("up"))
setting_A.show_()
while running:
    i+=1 # 循环一次+1，更新beta的旋转
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 如果按下'x'就结束
            pygame.quit()
            sys.exit()
    try:
        if event.type == pygame.MOUSEBUTTONDOWN: # 检测鼠标是否按下
            if not shezhiflag:
                if shezhirect.collidepoint(event.pos):
                    shezhiflag = 1
                    func[times%3]()
                    times += 1
            else:
                if setting_A.close_rect.collidepoint(event.pos):
                    shezhiflag = 0
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if setting_A.set_FULLSCREEN_flag:
                    screen = pygame.display.set_mode((1280,720))
                    setting_A.set_FULLSCREEN_flag = 0
                    pygame.display.update()
    except:
        continue
    screen.blit(cover,(0,0))
    if not shezhiflag:
        pygame.draw.rect(screen,(60,100,255),((620,340),(40,40)),0)
        screen.blit(setting_image,(623,343))
        show_text("设置",(255,255,255),(620,380),20)
        pygame.display.update()
        pygame.time.delay(70)
    else:
        try:
            if setting_A.close_rect.collidepoint(event.pos):
                setting_A.close_Surface.set_alpha(255)
            else:
                setting_A.close_Surface.set_alpha(0)
        except:
            pass
        finally:
            setting_A.show(event)
    clock.tick(fps)