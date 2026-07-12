import pygame
import os
import sys
from PgMarkdown import PygameMarkdown, Load

pygame.init()
screenHeight = 650
screenWidth = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("INS-PGM")
clock = pygame.time.Clock()

md = PygameMarkdown.MarkdownRenderer()
md.load_data(Load.load("./markdown文档.py"))  # 加载 markdown 文件

md.set_area(surface=screen, offset_x=50, offset_y=10, width=500, height=630)

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

    screen.fill((200, 200, 200))
    pygame.draw.rect(screen, (239, 239, 239), (0, 0, screenWidth, screenHeight))

    # 绘制
    md.display(pygame_events, mouse_x, mouse_y, mouse_pressed)

    pygame.display.flip()
    clock.tick(120)
