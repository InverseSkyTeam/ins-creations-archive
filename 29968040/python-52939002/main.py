import os
import sys
def get_py_path():
    return sys.executable
def install_library():
    try:
        import numba
    except ImportError:
        print("检测到环境尚未配置完全，正在自动配置（第一次运行常见）")
        import subprocess
        try:
            subprocess.check_call([get_py_path(), '-m', 'pip', 'install', "numba==0.56.4"])
            print("\n环境配置成功！请重新运行程序\033[8m;")
            sys.exit(0)
        except subprocess.CalledProcessError:
            print("\n环境配置失败！\033[8m;")
            sys.exit(1)
install_library()
import numpy as np
import pygame

screen = pygame.display.set_mode((600, 600), pygame.RESIZABLE)
pygame.init()

import model

clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 11)

window = model.Window(screen)
import IDU_undertale.main as IDU_undertale
pygame.key.stop_text_input()

while 1:
    FPS = str(round(clock.get_fps()))
    pygame.display.set_caption('fps:' + FPS)
    pygame_events = pygame.event.get()
    for event in pygame_events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((round(0.5*255), round(0.69*255), round(1.0*255)))
    IDU_undertale.next(pygame_events)
    window.handle_event(pygame_events)
    window.update()
    window.on_draw(IDU_undertale.screen)

    pygame.display.flip()
    clock.tick(114514)
