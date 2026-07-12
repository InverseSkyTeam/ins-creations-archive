import pygame.transform
import math
from rotate_lib import rotate, _rotate


Image = []


def add(img):
    Image.append(img)


def draw_img(screen, img):
    w, h, angle = img.width, img.height, img.rotate
    if w == 0 or h == 0:
        return
    if not img.transform:
        surf = img.source
        screen.blit(surf, (img.pointX - w // 2, img.pointY - h // 2)) 
    elif w in img.cache_sf:
        surf = img.cache_sf[w]
        surf, _w, _h = rotate(surf, angle)
        screen.blit(surf, (img.pointX - _w // 2, img.pointY - _h // 2)) 
    else:
        surf = pygame.transform.scale(img.source, (w, h))
        surf, _w, _h = _rotate(surf, angle)
        screen.blit(surf, (img.pointX - _w // 2, img.pointY - _h // 2)) 
    

def draw(screen):
    for i in Image:
        draw_img(screen, i)


def remove(img):
    Image.remove(img)
