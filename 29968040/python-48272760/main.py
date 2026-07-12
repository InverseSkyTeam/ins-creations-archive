import pygame
import os
import sys
from PgMarkdown import PygameMarkdown
try:#这个代码有3种情况 1、pygame版本<1.9.6,此时不支持pygame.version.vernum.major语法，直接报错
    #2、 1.9.6≤pygame版本<2.3，此时if语句成立，被强制报错
    #3、 2.3≤pygame版本 ,没有任何事情发生
    print("pygame当前版本：",pygame.version.vernum)
    if not (pygame.version.vernum.major>=2 and pygame.version.vernum.minor>=3):
        int('aaa')#强制报错
except:
    ans=input("你的pygame版本过低，是否更新？（回复“是”或“否”）")
    if ans=='是':
        os.system(sys.executable+" -m pip install --upgrade pygame --user")

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
