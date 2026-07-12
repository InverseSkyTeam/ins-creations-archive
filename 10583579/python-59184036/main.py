import pygame,sys
from typing import Tuple

input("填一个很久之前挖下的坑，已经半年没有编程了\n该作品是由ELEVEN的一个scratch跑酷作品还原而成，花了半个下午搓的，证明pygame还是可以用sc的方法实现跑酷的，只不过不是用rect或者sprite硬套\n所有的评论大概率都不会回复，还有几个月中考，退站作\n上下左右操控，回车换行开始:)")
print("\n\n")
pygame.init()
pygame.display.set_caption("跑酷测试(python改编) 原scratch作品 by ELEVEN")
# 原版:480*360
screen = pygame.display.set_mode((960,720))
img_index = 0
img = pygame.image.load("./Image/0.png")

def next_background():
    global img_index,img,running
    img_index += 1
    if img_index == 20:
        pygame.quit()
        running = False
        print("结束了，只节选了其中前20关 感谢观看,建议支持一下sc版的原作者ELEVEN")
        sys.exit()
    img = pygame.image.load(f"./Image/{img_index}.png")

class Player:
    def __init__(self):
        self.x = 40*2
        self.y = (180+10)*2
        self.width = 48
        self.height= 48
        self.background = pygame.Surface((960,720))
        self.background.fill((255,255,255))
        self.background.blit(img,(0,720-img.get_height()))
        self.x_ = 0
        self.y_ = 0

    def collide(self,color:Tuple[int,int,int]):
        x = self.x
        y = self.y
        for _ in range(self.width-1):
            try:
                if self.background.get_at((x,y)) == color:
                    return True
            except:continue
            x += 1
        for _ in range(self.height-1):
            try:
                if self.background.get_at((x,y)) == color:
                    return True
            except:continue
            y += 1
        for _ in range(self.width-1):
            try:
                if self.background.get_at((x,y)) == color:
                    return True
            except:continue
            x -= 1
        for _ in range(self.height-1):
            try:
                if self.background.get_at((x,y)) == color:
                    return True
            except:continue
            y -= 1
        return False
        """
        -> -> ->
        |      |
        ^      v
        |      |
        <- <-<-v
        使用上图式巡逻方式
        实现 sc 中碰到颜色函数
        """
    def bind(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x_ -= 2
        if keys[pygame.K_RIGHT]:
            self.x_ += 2
        self.x_ *= 0.9
        self.x = round(self.x + self.x_)
        if self.x < 40:
            self.x = 40
        if self.collide((0,0,0)):
            self.y -= 2
            if self.collide((0,0,0)):
                self.y -= 2
                if self.collide((0,0,0)):
                    self.y -= 2
                    if self.collide((0,0,0)):
                        self.x = round(self.x - self.x_)
                    if keys[pygame.K_UP]:
                        if self.x_ > 0:
                            self.x_ = -10
                        else:
                            self.x_ = 10
                        self.y_ = -23
                    else:
                        self.x_ = 0
        self.y_ += 2
        self.y = round(self.y + self.y_)
        if self.y < 0:
            self.y = 0
        # elif self.y < 0:
        #     self.x = 80
        #     self.y = 380
        if self.collide((0,0,0)):
            self.y = round(self.y - self.y_)
            self.y_ = 0
        self.y += 2
        if self.collide((0,0,0)):
            if keys[pygame.K_UP]:
                self.y_ = -27
        self.y -= 2
        if self.x > 920:
            next_background()
            self.x = 40*2
            self.y = 190*2
            self.background.fill((255,255,255))
            self.background.blit(img,(0,720-img.get_height()))
        if keys[pygame.K_SPACE] or self.collide((255,0,0)):
            self.x = 40*2
            self.y = 190*2
        elif self.collide((51,255,0)):
            self.y_ = -40
        elif self.collide((51,0,255)):
            self.y_ = 40
    
    def blit(self):
        screen.blit(self.background,(0,0))
        pygame.draw.rect(screen,(128,128,128),(self.x,self.y,self.width,self.height))
        pygame.display.update()

p = Player()
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            print("结束了 感谢观看,建议支持一下sc版的原作者ELEVEN")
            sys.exit()
            running = False
    p.bind()
    p.blit()
    clock.tick(50)