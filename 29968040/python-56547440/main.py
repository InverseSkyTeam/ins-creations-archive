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


import blur

pygame.transform.box_blur = blur.box_blur  # 逆天团队实现的 pygame-ce 均值模糊
pygame.transform.gaussian_blur = blur.gaussian_blur  # 逆天团队实现的 pygame-ce 高斯模糊
# 经测试，逆天团队实现版的速度已经和pygame-ce原版速度相差无几

pygame.init()
w, h = 700, 500
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("pygame 毛玻璃特效")

clock = pygame.time.Clock()

screen.fill((0x09, 0x19, 0x21))
pygame.draw.circle(screen, (0xff, 0xc1, 0x07), (int(w * 0.3), int(h * 0.2)), int(w * 0.2))
pygame.draw.circle(screen, (0xda, 0x00, 0xff), (int(w * 0.7), int(h * 0.9)), int(w * 0.2))

rect_surface = pygame.Surface((500, 400), pygame.SRCALPHA)
pygame.draw.rect(rect_surface, (255, 255, 255, int(255 * 0.05)), rect_surface.get_rect(), border_radius=6)
rect_surface_rect = rect_surface.get_rect(center=screen.get_rect().center)
screen.blit(rect_surface, rect_surface_rect)

blur_surface = pygame.transform.gaussian_blur(screen, 15).convert_alpha()
mask_surface = pygame.Surface(blur_surface.get_size(), pygame.SRCALPHA)
pygame.draw.rect(mask_surface, (255,) * 3, rect_surface_rect, border_radius=6)
blur_surface.blit(mask_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)

screen.blit(blur_surface, (0, 0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(114514)
