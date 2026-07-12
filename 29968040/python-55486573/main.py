import pygame
import sys
from cubic_bezier import CubicBezier
import time

bezier_func = CubicBezier(0.25, 0.1, 0.25, 1).Solve

pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)

class AnimationExample:
    def __init__(self, func):
        self.func = func
        self.in_animation = False  # 动画是否在进行中
        
        self._class = None
        self._attr = None
        self.start_attr = None  # 动画开始前的数值
        self.target_attr = None  # 动画开始后的数值
        self.start_time = None  # 动画开始的时间
        self.duration = None  # 动画播放时长
    
    def new_animation(self, _class, _attr, target, duration):
        '''
        开始一个新动画
        :param _class._attr: 要进行动画的参数
        :param target: 动画结束后参数的值
        :param duration: 动画的播放时长
        '''
        if self.in_animation:
            return
        self._class, self._attr = _class, _attr
        self.start_attr = getattr(_class, _attr)
        self.target_attr = target
        self.in_animation = True
        self.start_time = time.time()
        self.duration = duration
    
    def update(self):
        if not self.in_animation:
            return
        t = (time.time() - self.start_time) / self.duration
        if t > 1:
            self.in_animation = False
        new_attr = self.start_attr + (self.target_attr - self.start_attr) * self.func(t)
        setattr(self._class, self._attr, new_attr)


class Square:  # 用于演示动画效果的正方形类
    def __init__(self):
        self.size = 200
        self.x, self.y = 30, 30
        
        self.animation = AnimationExample(bezier_func)
        self.start_x, self.end_x = 30, 570
    
    def start_animation(self):
        if self.x == self.start_x:
            self.animation.new_animation(self, 'x', self.end_x, 2)
        elif self.x == self.end_x:
            self.animation.new_animation(self, 'x', self.start_x, 2)
    
    def draw(self, screen):
        screen.fill((255, 0, 136), (self.x, self.y, self.size, self.size))  # 等同于 pygame.draw.rect
        self.animation.update()

clock = pygame.time.Clock()
square = Square()

while 1:
    FPS = str(round(clock.get_fps()))
    pygame.display.set_caption('fps:' + FPS)
    pygame_events = pygame.event.get()
    for event in pygame_events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            square.start_animation()

    screen.fill((255,)*3)
    square.draw(screen)

    pygame.display.flip()
    clock.tick(114514)
