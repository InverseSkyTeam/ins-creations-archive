import pygame
import os
import sys
from show_main import Blog

pygame.init()

screenHeight = 650
screenWidth = 1200
bg_color = (247, 247, 247)

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("yzx-blog")
clock = pygame.time.Clock()
blog = Blog(screenWidth, screenHeight, bg_color)

while True:
    pygame.display.set_caption('fps:' + str(round(clock.get_fps())))
    pygame_events = pygame.event.get()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()[0]
    for event in pygame_events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            pass

    screen.fill(bg_color)
    blog.render(screen, (mouse_x, mouse_y), mouse_pressed, pygame_events)
    pygame.display.flip()
    clock.tick(120)
