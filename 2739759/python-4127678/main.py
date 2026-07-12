import pygame,sys,os,secret
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("字幕雨")
secret.rain(screen)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()