import pygame
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

from render import Render
from control import Control
from stats import Stats
import time
from ad import AD

pygame.init()
w, h = 800, 600
screen = pygame.display.set_mode((w, h), pygame.RESIZABLE)
pygame.display.set_caption('pygame 3D地球仪')

# 广告{
a = time.time()
ad = AD()
while 1:
    pygame_events = pygame.event.get()
    for event in pygame_events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.VIDEORESIZE:
            w, h = screen.get_size()
    curv_time = time.time() - a
    if curv_time >= 5:
        break
    ad.render(screen, w, h)
    rect = pygame.Rect(20, 20, 40 * 2, 30)
    pygame.draw.rect(screen, (100,)*3, rect, border_radius=5)
    sf = pygame.font.SysFont('SimHei', 15).render('广告: ' + str(int(5 - curv_time))+'s', True, (255,)*3)
    screen.blit(sf, sf.get_rect(center=rect.center))
    pygame.display.flip()
# }

clock = pygame.time.Clock()

render = Render()
control = Control()
stats = Stats(clock)

while 1:
    pygame_events = pygame.event.get()
    for event in pygame_events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.VIDEORESIZE:
            w, h = screen.get_size()

    control.handle_event(pygame_events, w)
    control.update()

    screen.fill((255,)*3)
    render.render(screen, w, h)
    stats.render(screen)
    control.render(screen, w)

    pygame.display.flip()
    clock.tick(114514)
