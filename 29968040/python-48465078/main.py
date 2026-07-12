import numpy as np
import pygame
import sys
import pygame.surfarray
import game
pygame.init()
screenHeight = 650 + 2*30
screenWidth = 400 + 2*30
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()
main = game.main(1)

while True:
    pygame.display.set_caption('fps:' + str(round(clock.get_fps())))
    pygame_events = pygame.event.get()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()[0]
    for event in pygame_events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255, 255, 255))
    main.display(screen, pygame_events, mouse_x, mouse_y, mouse_pressed)
    pygame.display.flip()
    clock.tick(60)
