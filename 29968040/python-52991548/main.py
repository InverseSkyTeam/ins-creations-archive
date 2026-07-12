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
import pygame
import threading as thr
import time

screen = pygame.display.set_mode((600, 600), pygame.RESIZABLE)
pygame.init()
clock = pygame.time.Clock()
font = pygame.font.SysFont('SimHei', 30)

import model
import IDU_undertale.main as IDU_undertale
window = model.Window(screen)
IS_COMPILE = False


def compile_thread():
    global IS_COMPILE
    window.initialize(452692)  # 生产地形
    model.compile_aot()  # 编译 numba 函数
    IS_COMPILE = True


def start_animation():
    tt = thr.Thread(target=compile_thread, args=(), name="T2")
    tt.start()

    logo = pygame.image.load('data/cube/logo.png')
    prompt = [font.render('代码正在编译中' + i * '.', True, (0,) * 3) for i in range(1, 4)]

    while not IS_COMPILE:
        FPS = str(round(clock.get_fps()))
        pygame.display.set_caption('fps:' + FPS)
        pygame_events = pygame.event.get()
        for event in pygame_events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((227, 255, 254))
        cx, cy = screen.get_rect().center
        _prompt = prompt[int(time.time() * 2) % 3]
        screen.blit(logo, logo.get_rect(center=(cx, cy - 30)))
        screen.blit(_prompt, _prompt.get_rect(center=(cx, cy + 170)))
        pygame.display.flip()
        clock.tick(60)


def main():
    while 1:
        FPS = str(round(clock.get_fps()))
        pygame.display.set_caption('fps:' + FPS)
        pygame_events = pygame.event.get()
        for event in pygame_events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((round(0.5*255), round(0.69*255), round(1.0*255)))
        mouse_pos_screen = window.hit_test_screen()
        IDU_undertale.next(pygame_events, mouse_pos_screen)
        window.handle_event(pygame_events, mouse_pos_screen)
        window.update()
        window.on_draw(IDU_undertale.screen)

        pygame.display.flip()
        clock.tick(114514)


if __name__ == '__main__':
    start_animation()
    main()
