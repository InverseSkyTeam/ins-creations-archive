import pygame
import random
import time
import sys

pygame.init()
font = {
    30: pygame.font.SysFont('kaiti', 30),
    40: pygame.font.SysFont('kaiti', 40),
}
def show_text(text, color=(0, 0, 0), pos=(0, 0), size=40):
    screen.blit(font[size].render((text), True, color), pos)

pygame.display.set_caption('∫insjhx 近期状况')
screen = pygame.display.set_mode((800, 600))

insjhx = pygame.image.load('insjhx.png')
clock = pygame.time.Clock()

class Actor:
    def __init__(self, img):
        self.standard_img = img
        self.rect = 0
        self.resize(self.standard_img.get_width(), self.standard_img.get_height())
    def resize(self, w, h):
        x, y = (0, 0)
        if self.rect:
            x, y = self.rect.x, self.rect.y
        self.img = pygame.transform.smoothscale(self.standard_img, (w, h))
        self.rect = self.img.get_rect()
        self.rect.x, self.rect.y = x, y
    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y
    def setp(self, x, y):
        self.rect.x = x
        self.rect.y = y
    def show_on(self, scr):
        scr.blit(self.img, self.rect)

insjhx = Actor(insjhx)
insjhx.resize(480, 1440)
insjhx.setp(160, 600)
startmovespeed = 15
now = 1



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if now in [2, 4, 5, 7, 9, 10]:
                    now += 1
                    if now == 8:
                        screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
                        insjhx.setp(-480, 100)
                        insjhx.resize(480, 1440)
                        startmovespeed = 10
                    if now == 11:
                        pygame.quit()
                        print('∫insjhx 有思想的不定积分逃离了窗口，他进入了互联网穿越去下一家玩了。')
                        sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == ord('r'):
                ...
    
    if now == 6:
        if insjhx.rect.x < 1160:
            insjhx.move(6, 0)
            screen = pygame.display.set_mode((max(insjhx.rect.x + 40, 800), max(600, insjhx.rect.x - 200)))
        else:
            screen = pygame.display.set_mode((1200, 800))
            now = 7
    
    screen.fill((255, 255, 255))
    if now == 3:
        screen.fill(((insjhx.rect.x - 100)*255/60, (insjhx.rect.x - 100)*255/60,(insjhx.rect.x - 100)*255/60))
    elif now in [4, 5, 6, 7, 8, 9]:
        screen.fill((0, 0, 0))
    insjhx.show_on(screen)
    
    # xes python3.7 不能用 match-case 差评！
    if now == 1:
        insjhx.move(0, -startmovespeed)
        startmovespeed *= 0.97
        if startmovespeed < 0.5:
            startmovespeed = 5
            now = 2
    elif now == 2:
        show_text('有思想的不定积分来了！[单击]继续', (0, 0, 0), (60, 50), 40)
    elif now == 3:
        if insjhx.rect.w > 40:
            insjhx.resize(insjhx.rect.w * 0.95, insjhx.rect.h * 0.95)
        else:
            insjhx.resize(40, 120)
        if insjhx.rect.x > 100:
            insjhx.move(-5, -startmovespeed)
            startmovespeed *= 0.95
        if insjhx.rect.size == (40, 120) and insjhx.rect.x <= 100:
            now = 4
    elif now == 4:
        show_text('看来终于还是有人来看我的作品了啊。', (255, 255, 255), (200, 50), 30)
        show_text('IDU来不及写，最近也没什么灵感。', (255, 255, 255), (200, 100), 30)
        show_text('要不就写点近期状况吧。[单击]继续', (255, 255, 255), (200, 150), 30)
    elif now == 5:
        show_text('说真的，这里实在有点窄。', (255, 255, 255), (200, 50), 30)
        show_text('我有点施展不开。', (255, 255, 255), (200, 100), 30)
    elif now == 7:
        show_text('好了，现在方便聊了。', (255, 255, 255), (10, 10), 30)
        show_text('最近精神状态还不错，基本上能保证6小时的睡眠了。', (255, 255, 255), (10, 40), 30)
        show_text('我也尽量找了不少事情干，', (255, 255, 255), (10, 70), 30)
        show_text('似乎确实比以前更丰富了。', (255, 255, 255), (10, 100), 30)
        show_text('我最近喜欢用一些富有表现力的东西来表现我的内心，或为一种情绪的释放。', (255, 255, 255), (10, 130), 30)
        show_text('吴宇航暑假指出我以前虚无主义的毛病，也得到了一些宽慰。', (255, 255, 255), (10, 160), 30)
        show_text('我在b站找到了一个up主，叫清竹莫叶，有很多存在主义的视频，还有些悬疑推理，很好看。', (255, 255, 255), (10, 190), 30)
        show_text('另外，我最近发现了一个叫略nd的up主，我倒是挺喜欢他画的人物。', (255, 255, 255), (10, 220), 30)
        show_text('这些大抵是属于一些精神上的帮助了，能够舒缓我的心情。', (255, 255, 255), (10, 250), 30)
        show_text('虽然回不到以前某个阶段的巅峰状态了，不过现在我可以依然说是实力不减。', (255, 255, 255), (10, 280), 30)
        show_text('我在现实和虚拟的世界中任意穿越，', (255, 255, 255), (10, 310), 30)
        show_text('体验不一样的经历。', (255, 255, 255), (10, 340), 30)
        show_text('这是我近期的精神状态。', (255, 255, 255), (10, 370), 30)
        show_text('另外，我打算写一部围绕我的人设的小说或者作品', (255, 255, 255), (10, 400), 30)
        show_text('不过纯文字信息量不够，如果有编程、绘画、音乐，那或许是一个具有宏大世界观的大作。', (255, 255, 255), (10, 430), 30)
        show_text('现在没时间，我只会编程，动画并不好做。所以至少要耽搁到寒假了。它或是真正的IDU吧。', (255, 255, 255), (10, 460), 30)
        show_text('不知道你们有没有看过：mc,ut,phigros,alan,cheems之类，我可能还会做一个视频大杂烩。', (255, 255, 255), (10, 490), 30)
        show_text('大概会在b站发一个关联这些和我的一些oc和一些常见鬼畜的混剪。', (255, 255, 255), (10, 520), 30)
        show_text('所以，一切还是很丰富的。', (255, 255, 255), (10, 550), 30)
    elif now == 8:
        insjhx.move(startmovespeed, 0)
        startmovespeed -= 0.1
        if insjhx.rect.x > 10:
            startmovespeed = 0
            now = 9
    elif now == 9:
        show_text('哈哈哈！', (255, 0, 0), (600, 100), 40)
        show_text('你的电脑', (255, 255, 255), (600, 150), 40)
        show_text('被我黑了', (0, 255, 0), (600, 200), 40)
        show_text('继续单击鼠标以对话。', (128, 128, 128), (600, 300), 30)
    elif now == 10:
        show_text('皮一下很开心。', (0, 0, 0), (600, 100), 40)
        show_text('祝你新年快乐！迎接那深不可测的2025吧！哈哈哈！', (0, 0, 0), (600, 150), 30)
        show_text('单击以关闭。', (0, 0, 0), (600, 200), 40)
        
    pygame.display.update()
    clock.tick(60)