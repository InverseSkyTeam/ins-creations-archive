import pygame,sys,random
screen = pygame.display.set_mode(size = (1280,720),flags = pygame.FULLSCREEN)
pygame.display.set_caption("我的作品")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.quit()
                sys.exit()
    screen.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    pygame.display.update()