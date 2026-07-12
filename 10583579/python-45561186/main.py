import pygame
from typing import Any, Optional,Tuple,Union,List
import sys
from time import sleep

print("点击屏幕打开弹窗")

pygame.init()
pygame.display.set_caption("弹窗测试")
screen = pygame.display.set_mode((1280,720))

try:
    import ntpath
    del ntpath
    FONTNAME = "kaiti"
except:
    FONTNAME = "kaittf"

FontDict = {}

def show_text(content:Optional[str],color:tuple,position:Union[list,tuple],size:int,master:pygame.Surface=screen,fontname = FONTNAME):
    if f"font_{size}" in FontDict:
        master.blit(FontDict[f"font_{size}"].render(content,True,color),(position))
    else:
        FontDict[f"font_{size}"] = pygame.font.SysFont(fontname,size)
        show_text(content,color,position,size,master)

def get_font(size,fontname=FONTNAME):
    if f"font_{size}" not in FontDict:
        FontDict[f"font_{size}"] = pygame.font.SysFont(fontname,size)
    return FontDict[f"font_{size}"]

background = pygame.image.load("背景.jpg")
background = pygame.transform.scale(background,(1280,720))

# 弹窗类
class Window(pygame.Surface):
    def __init__(self, screen:Optional[pygame.Surface], color:Tuple[int,int,int], size:Union[Tuple[int,int], List[int], None] = (100,100),border_radius:Optional[int] = 10,alpha=200) -> None:
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

        # 透明度
        self.alpha = alpha

        # 界面
        self.fill((255,255,255))
        pygame.draw.rect(self, self.color, (0,0,self.width, self.height), 0, border_radius=self.border_radius)
        self.set_colorkey(pygame.Color("white"))
        self.__screen = self.screen.copy()
        self.closed = False

    def gradient_appear(self) -> None:
        self.closed = False
        for alpha in range(0,150):
            self.set_alpha(int(Window.linear(0,self.alpha+1,Window.nonlinear(alpha/150))))
            self.screen.blit(self.__screen,(0,0))
            self.screen.blit(self,self.rect)
            pygame.display.update()
            pygame.time.delay(1)

    def fly_in_appear(self, side = "down",command = None) -> None:
        """
        :param side ->  up  表示从下往上飞入
                       down 表示从上往下飞入
        """
        self.closed = False
        self.set_alpha(self.alpha)
        if side == "down":
            y = self.y // 0.5
        elif side == "up":
            y = self.screen_height - self.y // 0.5
        for i in range(150):
            screen.blit(self.__screen,(0,0))
            if command:
                command(self.x,self.y-Window.linear(y,0,Window.nonlinear(i/150)))
            screen.blit(self,(self.x,self.y-Window.linear(y,0,Window.nonlinear(i/150))))
            pygame.display.update()
            pygame.time.delay(1)

    def update(self) -> None:
        pygame.display.update()

    def disappear(self) -> None:
        try:
            self.screen.blit(self.__screen,(0,0))
            pygame.display.update()
        except:
            raise pygame.error("the window has not appeared yet")

    @staticmethod
    def nonlinear(x:Union[int,float]) -> int:
        return x**3 * (6 * x**2 - 15 * x + 10)

    @staticmethod
    def linear(y1,y2,w) -> int:
        return y1 + (y2 - y1) * w

class MC_Style_Window(Window):
    def __init__(self,screen:pygame.Surface) -> None:
        super().__init__(screen,(255,255,255),(700,500),6,255)
        self.close_rect = pygame.Rect(463+self.x,17+self.y,20,20)
        self.background = screen.subsurface(pygame.Rect(self.x+15,self.y+48,self.width-31,self.height-71))
        pygame.draw.rect(self, (91,91,91), pygame.Rect(2,2, self.width-4, self.height-4), width=4, border_radius=self.border_radius-2)
        pygame.draw.rect(self,(0,0,0),pygame.Rect(0,0,self.width,self.height),width=2,border_radius=self.border_radius)
        pygame.draw.rect(self,(242,250,250),pygame.Rect(2,2,self.width-8,self.height-8),border_top_left_radius=self.border_radius)
        pygame.draw.rect(self,(198,198,198),pygame.Rect(6,6,self.width-12,self.height-12),width=0,border_top_left_radius=3)
        show_text("×",(113,107,109),(self.width-37,17),20,self)
        pygame.display.update()
    
    def on_button_down(self,event):
        if not self.closed:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.close_rect.collidepoint(event.pos):
                    self.screen.blit(self._Window__screen,(0,0))
                    self.closed = True
    
    def update(self,x,y):
        if y+48 < 0:
            self.background = self._Window__screen.subsurface(pygame.Rect(x+15,0,self.width-31,self.height-71+y+48))
            self.blit(self.background,(15,-y))
            self.imformation_area = pygame.Surface((self.width-31,self.height-71+y+48),pygame.SRCALPHA)
            self.imformation_area.fill(pygame.Color(0,0,0,180))
            self.blit(self.imformation_area,(15,-y))
            pygame.draw.rect(self,(252,252,252),pygame.Rect(self.width-18,48,2,self.height-71),width=0)
            pygame.draw.rect(self,(125,128,129),pygame.Rect(self.width-18,48,2,3),width=0)
            pygame.draw.rect(self,(252,252,252),pygame.Rect(15,self.height-25,self.width-32,2),width=0)
            pygame.draw.rect(self,(125,128,129),pygame.Rect(15,self.height-25,3,2),width=0)
        else:
            self.background = self._Window__screen.subsurface(pygame.Rect(x+15,y+48,self.width-31,self.height-71))
            self.blit(self.background,(15,48))
            self.imformation_area = pygame.Surface((self.width-31,self.height-71),pygame.SRCALPHA)
            self.imformation_area.fill(pygame.Color(0,0,0,180))
            self.blit(self.imformation_area,(15,48))
            pygame.draw.rect(self,(252,252,252),pygame.Rect(self.width-18,48,2,self.height-71),width=0)
            pygame.draw.rect(self,(125,128,129),pygame.Rect(self.width-18,48,2,3),width=0)
            pygame.draw.rect(self,(252,252,252),pygame.Rect(15,self.height-25,self.width-32,2),width=0)
            pygame.draw.rect(self,(125,128,129),pygame.Rect(15,self.height-25,3,2),width=0)

screen.blit(background,(0,0))
mc_window = MC_Style_Window(screen)
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not mc_window.close_rect.collidepoint(event.pos):
                mc_window.fly_in_appear(command=mc_window.update)
    mc_window.on_button_down(event)
    pygame.display.update()
    clock.tick(60)