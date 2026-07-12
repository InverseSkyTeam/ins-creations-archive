import zipfile, sys

import pygame
import os

def get_py_path():
    return sys.executable
def install_library():
    try:
        print("pygame当前版本：",pygame.version.vernum)
        if not (pygame.version.vernum.major>=2 and pygame.version.vernum.minor>=3):
            int('aaa')#强制报错
    except:
        print("检测到环境尚未配置完全，正在自动配置（第一次运行常见）")
        import subprocess
        try:
            subprocess.check_call([get_py_path(), '-m', 'pip', 'install', "--upgrade", "pygame"])
            print("\n环境配置成功！请重新运行程序\033[8m;")
            sys.exit(0)
        except subprocess.CalledProcessError:
            print("\n环境配置失败！\033[8m;")
            sys.exit(1)
install_library()

with zipfile.ZipFile('./assest.zip', 'r') as zip_ref:
    zip_ref.extractall('.')

import sys
from PgMarkdown import PygameMarkdown, Load


pygame.init()
screenWidth = 800
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("INS-PGM")
clock = pygame.time.Clock()

md = PygameMarkdown.MarkdownRenderer()
md.load_data(Load.load("./example.md"))

md.set_area(screen, pygame.Rect(50, 10, 700, 580), False)

while True:
    pygame.display.set_caption('fps:' + str(round(clock.get_fps())))
    pygame_events = pygame.event.get()
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()[0]
    for event in pygame_events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            pass

    screen.fill((200, 200, 200))
    pygame.draw.rect(screen, (236,)*3, (0, 0, screenWidth, screenHeight))
    pygame.draw.rect(screen, (255,)*3, md.rect.inflate(20, 0))

    # 绘制
    md.display(pygame_events, mouse_pos, mouse_pressed)

    pygame.display.flip()
    clock.tick(114514)
