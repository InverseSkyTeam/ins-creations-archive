import pygame
from pygame.locals import*
from sys import exit
from random import randint

class Star(object):     #类
    def __init__(self,x,y,speed):    #重载
        self.x = x
        self.y = y
        self.speed = speed

def run():      #函数   
    pygame.init()       #pygame初始化
    width,height = 640,400      #设置屏幕分辨率
    screen = pygame.display.set_mode((width,height),0,32)     
    Fullscreen = False
    stars = []
    for n in range(200):    #在第一帧画上一些星星
        x = float(randint(0,639))
        y = float(randint(0,399))
        speed = float(randint(10,300))
        stars.append(Star(x,y,speed))

    clock = pygame.time.Clock()     #Clock对象
    white = (255,255,255)
    #设置背景音效
    
    while True:       
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == KEYDOWN:
                if event.key == K_f:    # F键控制是否全屏
                    Fullscreen = not Fullscreen
                    if Fullscreen :
                        screen = pygame.display.set_mode((width,height),FULLSCREEN | HWSURFACE,32)    #全屏+硬件加速
                    else:
                        screen = pygame.display.set_mode((width,height),0,32)
                        
        y = float(randint(0,399))   #增加一颗新的星星
        speed = float(randint(10,300))
        star = Star(640,y,speed)
        stars.append(star)

        time_passed = clock.tick()
        time_passed_seconds = time_passed/1000      #单位毫秒,需转换

        screen.fill((0,0,0))
        for star in stars:      #绘制所有星星
            new_x = star.x - time_passed_seconds*star.speed
            pygame.draw.aaline(screen,white,(new_x,star.y),(star.x+1,star.y))
            star.x = new_x
        def on_screen(star):
            return star.x > 0
        stars = list(filter(on_screen,stars))     #星星跑出画面就删除
        pygame.display.update()
        
if __name__ == "__main__":
    run()