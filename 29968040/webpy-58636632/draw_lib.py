import pygame
import pygame.transform


def scale_img(img, width, height):
    aspect_ratio = img.get_width() / img.get_height()
    target_ratio = width / height
    if aspect_ratio > target_ratio:
        new_height = height
        new_width = int(height * aspect_ratio) + 1
    else:
        new_width = width
        new_height = int(width / aspect_ratio) + 1
    resized_img = pygame.transform.scale(img, (new_width, new_height))
    return resized_img
    
