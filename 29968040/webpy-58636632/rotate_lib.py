import math
import pygame.transform


def _rotate(surf, angle):  # 对 webpy 的 rotate 的补丁
    # 摘自 pygame 的 C 代码
    radangle = angle * 0.01745329251994329
    sangle = math.sin(radangle)
    cangle = math.cos(radangle)
    x, y = surf.get_width(), surf.get_height()
    cx = cangle * x
    cy = cangle * y
    sx = sangle * x
    sy = sangle * y
    nxmax = int(max(abs(cx + sy), abs(cx - sy), abs(-cx + sy), abs(-cx - sy)))
    nymax = int(max(abs(sx + cy), abs(sx - cy), abs(-sx + cy), abs(-sx - cy)))

    new_surf = pygame.Surface((nxmax, nymax), pygame.SRCALPHA)  # 创建新画布
    new_surf.blit(surf, ((nxmax - x) // 2, (nymax - y) // 2))  # 相当于给原画布加上透明边框，保证旋转结果正确
    res = pygame.transform.rotate(new_surf, angle)  # 对加边框的画布进行旋转
    return res, nxmax, nymax  # 后两个参数是旋转后画布的大小，因为webpy的rotate会进行放大


def rotate(surf, angle):
    res = pygame.transform.rotate(surf, angle)
    return res, surf.get_width(), surf.get_height()

