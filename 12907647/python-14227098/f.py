def ff(a):
    import pygame
    pygame.init()
    p = 0
    screen = pygame.display.set_mode((1000,800))
    pygame.display.set_caption("我的作品")
    myImg = pygame.image.load(a)
    while p == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                p = 1
        screen.fill((255,255,255))
        screen.blit(myImg,(0,0))
        pygame.display.update()