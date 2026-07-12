import zipfile, sys
with zipfile.ZipFile('./textures.zip', 'r') as zip_ref:
    zip_ref.extractall('.')


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


import pygame
import sys
import time
from game_window import Window
import options

pygame.init()
screen = pygame.display.set_mode((852, 480), pygame.RESIZABLE)
clock = pygame.time.Clock()
pygame.key.stop_text_input()

config = options.InternalConfig()
window = Window(852, 480, config)

last_time = time.time()
scale_ratio = 1

cross_hair = pygame.image.load('crosshair.png').convert_alpha()
new_screen = pygame.Surface((int(screen.get_width()*scale_ratio), int(screen.get_height()*scale_ratio)))
window.on_resize(new_screen.get_width(), new_screen.get_height())

while True:
    FPS = str(round(clock.get_fps()))
    pygame.display.set_caption('fps:' + FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            new_screen = pygame.Surface((int(screen.get_width() * scale_ratio), int(screen.get_height() * scale_ratio)))
            window.on_resize(new_screen.get_width(), new_screen.get_height())
        elif event.type == pygame.MOUSEBUTTONDOWN:
            window.on_mouse_press(event.button)
        elif event.type == pygame.MOUSEMOTION:
            window.on_mouse_motion(*event.rel)
        elif event.type == pygame.KEYDOWN:
            window.on_key_press(event.key)
        elif event.type == pygame.KEYUP:
            window.on_key_release(event.key)
    screen.fill((255, 255, 255))

    window.player.update_interpolation(delta_time=time.time()-last_time)
    window.update(delta_time=time.time()-last_time)
    last_time = time.time()

    window.on_draw(new_screen)
    screen.blit(pygame.transform.scale(new_screen, screen.get_size()), (0, 0))
    window.render_f3(screen)

    screen.blit(cross_hair, cross_hair.get_rect(center=screen.get_rect().center))

    pygame.display.update()
    clock.tick(114514)
