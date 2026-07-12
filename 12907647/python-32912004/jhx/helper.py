# helps for jhx
import pygame,sys
pygame.init()

screen = pygame.display.set_mode((1000,600))
pygame.display.set_icon(pygame.image.load('jhx/image/helpbookicon.png'))
pygame.display.set_caption('INS jhx python-helpbook')

try:import ntpath
except:exec("def show_text(text,color=(0,0,0),pos=(0,0),size=30):screen.blit(pygame.font.SysFont('kaittf', size).render((text),True,color),pos)")
else:exec("def show_text(text,color=(0,0,0),pos=(0,0),size=30):screen.blit(pygame.font.SysFont('kaiti', size).render((text),True,color),pos)")
finally:pass

bg = pygame.image.load('jhx/image/helpbookbg.png')

CVrect = pygame.Rect(250,100,500,50)
Helprect = pygame.Rect(250,200,500,50)
Exitrect = pygame.Rect(250,300,500,50)

y = 0
mp = (0,0)
part = '主界面'

while 1:       # 代码显示了我的懒
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # part = 'callback'
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            mp = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if CVrect.collidepoint(mp):
                    part = '库信息界面'
                if Helprect.collidepoint(mp):
                    part = '库教程界面'
                if Exitrect.collidepoint(mp):
                    part = 'callback'
    screen.fill((255,255,255))
    screen.blit(bg,(0,0))
    show_text('INS-jhx库帮助',(0,0,255),(11,11),40)
    show_text('(C)Copyright.INS逆天团队-小轩(2021,2022)所有',(0,0,0),(275,29),20)    # 如果x=271会显得过于紧凑，y=40-11=29
    show_text('(V)Version.版本|0.3.1',(0,0,0),(740,29),20)
    
    if CVrect.collidepoint(mp):pygame.draw.rect(screen,(0,255,0),CVrect,0)
    else:pygame.draw.rect(screen,(200,200,200),CVrect,0)
    pygame.draw.rect(screen,(0,0,0),CVrect,3)
    show_text('库 信 息',(0,0,0),(420,105),40)
    
    if Helprect.collidepoint(mp):pygame.draw.rect(screen,(0,111,255),Helprect,0)
    else:pygame.draw.rect(screen,(200,200,200),Helprect,0)
    pygame.draw.rect(screen,(0,0,0),Helprect,3)
    show_text('库 教 程',(0,0,0),(420,205),40)
    
    if Exitrect.collidepoint(mp):pygame.draw.rect(screen,(255,66,50),Exitrect,0)
    else:pygame.draw.rect(screen,(200,200,200),Exitrect,0)
    pygame.draw.rect(screen,(0,0,0),Exitrect,3)
    show_text('退    出',(0,0,0),(420,305),40)
    
    pygame.display.update()