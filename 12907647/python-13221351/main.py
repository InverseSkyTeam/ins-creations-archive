import pygame,sys
pygame.init()
screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("|小轩|爆字体！")
myImg = pygame.image.load("图片.png")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255,255,255))
    screen.blit(myImg,(0,0))
    pygame.display.update()