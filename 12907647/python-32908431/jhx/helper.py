# helps for jhx
import pygame,sys
pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('INS jhx python-helpbook')

while 1:       # 代码显示了我的懒
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255,255,255))
    pygame.display.update()