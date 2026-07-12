from render import render, Model
import pygame, sys
pygame.init()
screen = pygame.display.set_mode((600, 600))
model = Model("res/axe.obj", texture_filename="res/axe.tga")
clock = pygame.time.Clock()
num = 0
while 1:
    pygame.display.set_caption('fps:' + str(round(clock.get_fps())))
    pygame_events = pygame.event.get()
    for event in pygame_events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

    screen.fill((255, 255, 255))
    render(
        model,
        height=600,
        width=600,
        filename="axe.png",
        screen=screen,
        angleX=0,
        angleY=num
    )
    pygame.display.flip()
    clock.tick(114514)
    num += 0.05
