from random import randint
import pygame


# 把 int 转换为指定长度的 str, 不足补 0
def int_to_str(num, length):
    return '0' * (length - len(str(num))) + str(num)


# 获取出生点、重生点的位置
def get_spwan_pos():
    pos = ((0, -65), (-34, -43), (0, 37), (66, 1), (-91, -68))
    index = randint(0, len(pos)-1)
    return pos[index][0], 7, pos[index][1]


def compare_versions(version1, version2):
    digits1 = version1.split('.')
    digits2 = version2.split('.')
    for i in range(max(len(digits1), len(digits2))):
        if i >= len(digits1):
            return -1
        if i >= len(digits2):
            return 1
        if int(digits1[i]) < int(digits2[i]):
            return -1
        if int(digits1[i]) > int(digits2[i]):
            return 1
    return 0


def scale_img(img, width, height):
    aspect_ratio = img.get_width() / img.get_height()
    target_ratio = width / height
    if aspect_ratio > target_ratio:
        new_height = height
        new_width = int(height * aspect_ratio) + 1
    else:
        new_width = width
        new_height = int(width / aspect_ratio) + 1
    resized_img = pygame.transform.smoothscale(img, (new_width, new_height))
    x_offset = (new_width - width) // 2
    y_offset = (new_height - height) // 2
    result_img = resized_img.subsurface((x_offset, y_offset, width, height))

    result_sf = pygame.Surface(result_img.get_size(), pygame.SRCALPHA)
    make_sf = pygame.Surface(result_img.get_size(), pygame.SRCALPHA)
    pygame.draw.rect(make_sf, (255, 255, 255, 255), pygame.Rect((0, 0), result_img.get_size()),
                     border_top_left_radius=8, border_top_right_radius=8)
    result_sf.blit(result_img, (0, 0))
    result_sf.blit(make_sf, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)
    return result_sf
