"""
import pygame,sys
pygame.init()
p = 0
screen = pygame.display.set_mode((800,500))
pygame.display.set_caption("滑动解锁")
x = 0
huarect = pygame.Rect(0,0,10,10)
screen.fill((255,255,255))
try:
    import ntpath # 如果成功，那么是Windows
    FONTNAME = "kaiti"
    del ntpath
except ImportError: # 如果失败，是MacOS
    FONTNAME = "kaittf"
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            p = 1
        elif event.type == pygame.MOUSEBUTTONUP:
            p = 0
        elif p == 1:
            if event.type == pygame.MOUSEMOTION:
                huarect.center = (event.pos[0],400) 
                pygame.display.update()
                if huarect.collidepoint(650,400):
                    
    screen.blit(pygame.font.SysFont(FONTNAME,30).render(">>>滑动以解锁>>>",True,(0,0,0)),(280,400))
    screen.blit(pygame.font.SysFont(FONTNAME,15).render("请长按鼠标后再滑动",True,(0,0,0)),(335,440))
    pygame.display.update()
"""
import pygame,sys
pygame.init()
p = 0
screen = pygame.display.set_mode((800,500))
pygame.display.set_caption("滑动解锁")
myImg = pygame.image.load("滑动解锁.PNG")
pygame.display.set_icon(myImg)
x = 0
huarect = pygame.Rect(0,0,10,10)
screen.fill((255,255,255))
try:
    import ntpath # 如果成功，那么是Windows
    FONTNAME = "kaiti"
    del ntpath
except ImportError: # 如果失败，是MacOS
    FONTNAME = "kaittf"
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            p = 1
        elif event.type == pygame.MOUSEBUTTONUP:
            p = 0
        elif p == 1:
            if event.type == pygame.MOUSEMOTION:
                huarect.center = (event.pos[0],400) 
                pygame.display.update()
                if huarect.collidepoint(650,400):
                    screen = pygame.display.set_mode((1,1))
                    pygame.display.set_caption("滑动解锁")
                    print("如何？复制2~33行可以使用滑动解锁，在30行编辑解锁后要运行的程序！不需要导出素材！！！我给你这么一个炫酷的开头方式，我只要你美丽的结尾和一个赞，O(∩_∩)O谢谢！！")
                    pygame.quit()
                    sys.exit()
    screen.blit(pygame.font.SysFont(FONTNAME,30).render(">>>滑动以解锁>>>",True,(0,0,0)),(280,400))
    screen.blit(pygame.font.SysFont(FONTNAME,15).render("请长按鼠标时滑动鼠标",True,(0,0,0)),(325,440))
    pygame.display.update()