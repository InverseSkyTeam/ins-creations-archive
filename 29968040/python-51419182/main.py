import pygame,sys
import numpy as np
from PIL import Image, ImageFilter
pygame.init()
screen = pygame.display.set_mode((1200,600))

# 给画布高斯模糊
def blur_sf(sf, radius):
    arr = pygame.surfarray.pixels2d(sf)  # 不能用pixels3d，因为会丢失透明度
    arr_3d = np.zeros((*arr.shape, 4), dtype=np.uint8)  # 手动分离rgba
    arr_3d[:, :, 2] = arr[:, :] & 0xFF  # 等同于 arr[:, :] % 256
    arr_3d[:, :, 1] = (arr[:, :] >> 8) & 0xFF  # 等同于 arr[:, :] // 256 % 256
    arr_3d[:, :, 0] = (arr[:, :] >> 16) & 0xFF  # 等同于 arr[:, :] // 256 // 256 % 256
    arr_3d[:, :, 3] = (arr[:, :] >> 24) & 0xFF  # 等同于 arr[:, :] // 256 // 256 // 256 % 256
    pil_image = Image.fromarray(np.swapaxes(arr_3d, 0, 1))  # pygame和PIL存储方式是相反的，需要调换x、y轴
    img1 = pil_image.filter(ImageFilter.GaussianBlur(radius=radius))  # PIL执行高斯模糊
    return pygame.image.fromstring(img1.tobytes(), img1.size, 'RGBA')  # 再把PIL图转成pygame的Surface

clock = pygame.time.Clock()
while True:
    pygame.display.set_caption('fps:' + str(round(clock.get_fps())))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255,255,255))
    sf = pygame.Surface((200, 100), pygame.SRCALPHA)
    pygame.draw.rect(sf, (0, 0, 0, int(255*0.75)), (0, 0, 200, 100))
    #screen.blit(sf, (0, 0))
    x, y = 0, 100
    for y in range(0, 601, 100):
        for x in range(0, 1201, 200):
            screen.blit(blur_sf(sf, 10), (x, y))
    pygame.display.update()
    clock.tick(114514)