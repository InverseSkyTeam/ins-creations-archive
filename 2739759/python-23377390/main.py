import pygame,sys
pygame.init()
screen = pygame.display.set_mode(size = (1600,900),flags = pygame.FULLSCREEN)
pygame.display.set_caption("我的作品")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()