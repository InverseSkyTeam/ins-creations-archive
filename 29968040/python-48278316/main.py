import pygame
import os
import sys
from PgMarkdown import PygameMarkdown
from pygments import highlight
from pygments.lexers import get_lexer_by_name, guess_lexer
from pygments.formatters import get_formatter_by_name
from pygments.util import ClassNotFound

pygame.init()
screenHeight = 650
screenWidth = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("INS-PGM")
clock = pygame.time.Clock()

md = PygameMarkdown.MarkdownRenderer()
md.set_markdown(mdfile_path="./cs.md")  # 加载markdown文件

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

    screen.fill((200, 200, 200))
    pygame.draw.rect(screen, (239, 239, 239), (0, 0, screenWidth, screenHeight))

    # 绘制
    md.display(pygame_events, mouse_x, mouse_y, mouse_pressed)

    pygame.display.flip()
    clock.tick(60)
