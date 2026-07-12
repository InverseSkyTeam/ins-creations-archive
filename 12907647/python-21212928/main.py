import pygame,sys
pygame.init()
screen = pygame.display.set_mode((749,605))
myImg = pygame.image.load("logo4.png")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255,255,255))
    screen.blit(myImg,(0,0))
    pygame.display.update()