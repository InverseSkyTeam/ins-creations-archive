# 环境配置+资源解压
#{
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


import zipfile
with zipfile.ZipFile('./pvz_pak.zip', 'r') as zip_ref:
    zip_ref.extractall('./pvz_pak/')
#}

import pygame
import sys
from texture_manager import TextureManager
from reanim_file import ReanimFile
from animation_object import Item, Plant

pygame.init()

# TODO: 左键换动作，右键换僵尸
text_manager = TextureManager()

animation_object = [
    Plant(ReanimFile('Blover.reanim', text_manager), text_manager),
    Plant(ReanimFile('DoomShroom.reanim', text_manager), text_manager),
    Item(ReanimFile('CrazyDave.reanim', text_manager), text_manager),
    Item(ReanimFile('Zombie_boss.reanim', text_manager), text_manager),
    # Plant(ReanimFile('Cattail.reanim', text_manager), text_manager),
]
animation_index = 0

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
while True:
    pygame.display.set_caption('fps:' + str(round(clock.get_fps())))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                animation_object[animation_index].next_action()
            if event.button == 3:
                animation_index += 1
                animation_index %= len(animation_object)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i:
                _l = animation_object[animation_index].use_interpolation
                animation_object[animation_index].use_interpolation = not _l
    screen.fill((255, 254, 253))
    animation_object[animation_index].render(screen)
    pygame.display.update()
    clock.tick(114514)
