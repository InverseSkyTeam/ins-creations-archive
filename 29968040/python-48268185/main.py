import pygame
import os
import sys
# os.system(sys.executable+" -m pip install --upgrade markdown --user")
from PgMarkdown import PygameMarkdown

pygame.init()
screenHeight = 650
screenWidth = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("INS-PGM")

md = PygameMarkdown.MarkdownRenderer()
md.set_markdown(mdfile_path="./活动.md")  # 加载markdown文件
y = 10
md.set_area(surface=screen, offset_x=50, offset_y=y, width=500, height=630)


while True:
    pygame_events = pygame.event.get()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    for event in pygame_events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((239, 239, 239))
    pygame.draw.rect(screen, (255, 255, 255), (50, 0, 500, 650))

    # 绘制
    md.set_area(surface=screen, offset_x=50, offset_y=y, width=500, height=630)
    y -= 1
    md.display(pygame_events, mouse_x, mouse_y, mouse_pressed)

    pygame.display.flip()
