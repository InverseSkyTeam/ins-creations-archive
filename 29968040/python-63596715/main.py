def install_library():
    try:
        import pygame
        print("pygame当前版本：", pygame.version.vernum)
        if not (pygame.version.vernum.major >= 2 and pygame.version.vernum.minor >= 3):
            raise ValueError
    except ValueError:
        print("检测到环境尚未配置完全，正在自动配置（第一次运行常见）")
        import subprocess
        import sys
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', "--upgrade", "pygame"])
            print("\n环境配置成功！请重新运行程序\033[8m;")
            sys.exit(0)
        except subprocess.CalledProcessError:
            print("\n环境配置失败！\033[8m;")
            sys.exit(1)
    except ImportError:
        print("检测到环境尚未配置完全，正在自动配置（第一次运行常见）")
        import subprocess
        import sys
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', "pygame"])
            print("\n环境配置成功！请重新运行程序\033[8m;")
            sys.exit(0)
        except subprocess.CalledProcessError:
            print("\n环境配置失败！\033[8m;")
            sys.exit(1)


install_library()



import pygame
import sys
import time
import math
from data import BlockType, TextureManager, Block
from render import render_cube

pygame.init()
screen = pygame.display.set_mode((700, 500))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 20)

texture_manager = TextureManager()
iron = BlockType(texture_manager, {'all': 'iron_block'})
pumpkin = BlockType(texture_manager, {'y': 'pumpkin_top', 'x': 'pumpkin_side', 'back': 'pumpkin_side', 'front': 'carved_pumpkin'})


cube = [Block(pumpkin, (0, -1, 0)), Block(iron, (0, 0, 0)), Block(iron, (0, 1, 0)), Block(iron, (-1, 0, 0)), Block(iron, (1, 0, 0))]
angle_x = 0.0
angle_y = 0.0
mouse_dragging = False

pygame.mixer.music.load('music.ogg')
pygame.mixer.music.play(loops=-1)

while True:
    fps = f'fps: {clock.get_fps():.3f}'
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_dragging = True
        if event.type == pygame.MOUSEMOTION and mouse_dragging:
            angle_x += event.rel[1]/300
            angle_y += event.rel[0]/100
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            mouse_dragging = False
    screen.fill((255, 255, 255))
    
    t = (math.sin(time.time() * 6.5) + 1) / 2
    cube[1].z = cube[2].z = t
    cube[3].z = cube[4].z = 1 - t

    # pygame.draw.rect(screen, (255,0,0), (0,0,700,500),2)
    render_cube(screen, (700, 500), texture_manager, [angle_x, angle_y], cube)
    screen.blit(font.render(fps, True, (0, 0, 0)), (10, 10))
    pygame.display.update()
    clock.tick(114514)
