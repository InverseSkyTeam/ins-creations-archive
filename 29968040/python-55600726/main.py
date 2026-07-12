import pygame
import sys
from util import compare_versions


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


def install_library1():
    try:
        import websocket
        if compare_versions('1.6.1', websocket.__version__) == 1:
            raise ImportError
    except ImportError:
        print("检测到环境尚未配置完全，正在自动配置（第一次运行常见）")
        import subprocess
        try:
            subprocess.check_call([get_py_path(), '-m', 'pip', 'install', "websocket-client==1.6.1"])
            print("\n环境配置成功！请重新运行程序\033[8m;")
            sys.exit(0)
        except subprocess.CalledProcessError:
            print("\n环境配置失败！\033[8m;")
            sys.exit(1)


install_library()
install_library1()

from rooms import Rooms


pygame.init()
w, h = 700, 525
screen = pygame.display.set_mode((w, h), pygame.RESIZABLE)
clock = pygame.time.Clock()
pygame.key.stop_text_input()

rooms = Rooms(w, h)

while 1:
    FPS = str(round(clock.get_fps()))
    pygame.display.set_caption('fps:' + FPS)
    pygame_events = pygame.event.get()
    for event in pygame_events:
        if event.type == pygame.QUIT:
            rooms.exit()
            pygame.quit()
            sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            w, h = screen.get_size()

    rooms.update(pygame_events, w, h)
    rooms.draw(screen, w, h)

    pygame.display.flip()
    clock.tick(114514)
