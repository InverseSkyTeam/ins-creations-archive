import pygame
import player
import texture_manager
import world
import options
import keyboard_mouse
from collections import deque
import sys
import time

import zipfile
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


class InternalConfig:
    def __init__(self, _options):
        self.RENDER_DISTANCE = _options.RENDER_DISTANCE
        self.FOV = _options.FOV
        self.CHUNK_UPDATES = _options.CHUNK_UPDATES
        self.SMOOTH_LIGHTING = _options.SMOOTH_LIGHTING


class Window:
    def __init__(self, w, h):
        self.width, self.height = w, h

        # Options
        self.options = InternalConfig(options)

        # F3 Debug Screen

        self.show_f3 = True

        self.texture_manager = texture_manager.TextureManager(16, 16, 256)

        # create world

        self.world = world.World(None, self.texture_manager, self.options)

        # player stuff

        self.player = player.Player(self.world, self.width, self.height)
        self.world.player = self.player

        self.mouse_captured = False

        # misc stuff

        self.holding = 50

        # controls stuff
        self.controls = [0, 0, 0]

        # mouse and keyboard stuff
        self.keyboard_mouse = keyboard_mouse.Keyboard_Mouse(self)

        # GPU command syncs
        self.fences = deque()

        self.exclusive = False  # 是否隐藏鼠标

    def set_exclusive_mouse(self, exclusive):  # 设置鼠标是否隐藏
        pygame.event.set_grab(exclusive)
        pygame.mouse.set_visible(not exclusive)
        self.exclusive = exclusive

    def update(self, delta_time):
        """Every tick"""
        if not self.mouse_captured:
            self.player.input = [0, 0, 0]

        self.player.update(delta_time)
        self.world.tick(delta_time)

    def on_draw(self, _screen):
        self.player.update_matrices()

        self.world.prepare_rendering()
        self.world.draw(_screen)

    def on_resize(self, width, height):
        self.player.view_width = width
        self.player.view_height = height

    def on_mouse_press(self, button):
        pass

    def on_mouse_motion(self, delta_x, delta_y):
        pass

    def on_key_press(self, key):
        pass

    def on_key_release(self, key):
        pass


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((852, 480), pygame.RESIZABLE)
    window = Window(852, 480)
    clock = pygame.time.Clock()
    pygame.key.stop_text_input()
    last_time = time.time()
    cross_hair = pygame.image.load('crosshair.png').convert_alpha()
    while True:
        FPS = str(round(clock.get_fps()))
        pygame.display.set_caption('fps:' + FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                window.on_resize(screen.get_width(), screen.get_height())
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

        window.on_draw(screen)

        screen.blit(cross_hair, cross_hair.get_rect(center=screen.get_rect().center))

        pygame.display.update()
        clock.tick(114514)
