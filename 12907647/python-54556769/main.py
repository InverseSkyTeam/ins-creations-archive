# 感谢数学好的同学[陈加禾]提供scratch版本地形生成大致思路。
# 感谢黄羿杰的三角函数旋转移动算法。
import random
import math

def move(x, y, steps, radians):
    x += steps * math.cos(radians)
    y += steps * -math.sin(radians)
    return (round(x, 12), round(y, 12))

def noise(basicx=0, basicy=0, times=1000, steep=40, amplitude1=105, amplitude2=105, rough=6):
    '''
    basic: 地基高度
    times: 至少操作次数（描点数量）
    steep: 陡峭程度限制（角度）
    amplitude1: 上振幅限制
    amplitude2: 下振幅限制
    rough: 粗糙度
    '''
    x = basicx
    y = basicy
    angle = 0

    l = []

    while times:
        if angle <= -random.randint(steep - 10, steep + 10) or y >= basicy + random.randint(amplitude1 - 5, amplitude1 + 10):
            angle += random.uniform(0, rough / 2)
        elif angle >= random.randint(steep - 10, steep + 10) or y <= basicy - random.randint(amplitude2 - 5, amplitude2 + 10):
            angle -= random.uniform(0, rough / 2)
        else:
            angle += random.uniform(-rough, rough)

        radians = math.radians(angle)
        x, y = move(x, y, 1, radians)

        l.append((round(x), round(y)))
        times -= 1
    
    return l

def connect_noise(length):
    line = []
    l = random.randint(256, 512)
    n = noise(0, -15, l, 15, 40, 40, 5)   # 平原
    line += n
    x, y = n[-1]
    while l < length:
        if y <= -30:
            nxt_w = random.randint(89, 256)
            n = noise(x, y, nxt_w, 30, 80, 10, 6)    # 低->高
        elif -30 <= y <= 10:
            nxt_w = random.randint(384, 1280)
            n = noise(x, y, nxt_w, 15, 40, 15, 5)    # 平原
        elif 11 <= y <= 52:
            nxt_w = random.randint(128, 1024)
            n = noise(x, y, nxt_w, 45, 85, 60, 6)    # 丘陵
        elif 88 <= y <= 130:
            nxt_w = random.randint(256, 832)
            n = noise(x, y, nxt_w, 25, 95, 35, 6)    # 高原
        elif 53 <= y <= 87:
            nxt_w = random.randint(128, 832)
            n = noise(x, y, nxt_w, 75, 135, 45, 8)   # 山地
        elif 66 <= y:
            nxt_w = random.randint(89, 256)
            n = noise(x, y, nxt_w, 60, 0, 150, 8)    # 高->低
        line += n
        x, y = n[-1]
        l += nxt_w
    return line

l = connect_noise(15000)



display = 1
if display:
    import pygame
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    r = pygame.Rect(0, 0, 1, 1)
    x = 0
    y = 0
    kr = 0
    ku = 0
    kl = 0
    kd = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    kr = 1
                if event.key == pygame.K_UP:
                    ku = 1
                if event.key == pygame.K_LEFT:
                    kl = 1
                if event.key == pygame.K_DOWN:
                    kd = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    kr = 0
                if event.key == pygame.K_UP:
                    ku = 0
                if event.key == pygame.K_LEFT:
                    kl = 0
                if event.key == pygame.K_DOWN:
                    kd = 0
        screen.fill((255, 255, 255))
        if kr:
            x -= 100
        if kl:
            x += 100
        if kd:
            y -= 100
        if ku:
            y += 100
        r.x = x
        for i in l:
            r.x = i[0] + x
            r.y = - i[1] + 300 + y
            pygame.draw.rect(screen, (0, 0, 0), r, 0)
        pygame.display.update()