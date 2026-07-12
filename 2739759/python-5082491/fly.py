import pygame
import random
import time

t1 = time.time()
pygame.init()

bulletimg2 = pygame.image.load("bang.png")
bg_size = (480, 700)
bulletList = []
score = 0


def bullet(screen,hero_rect, speed):
    t2 = time.time()
    t = t2 - t1
    if int(t * 4) % 1 == 0 and t < int(t) + 0.1:
        bulletimg = pygame.image.load("bullet1.png")
        bullet_rect = bulletimg.get_rect()
        bullet = {
            "surface": bulletimg,
            "rect": pygame.Rect(hero_rect.x + (hero_rect.width-bullet_rect.width) / 2, hero_rect.y, \
                                bullet_rect.width, bullet_rect.height),
            "move_x": 0,
            "move_y": -speed * 3
        }
        bulletList.append(bullet)
    # 子弹移动
    for a1 in bulletList:
        a1["rect"].move_ip(a1["move_x"], a1["move_y"])
    for a2 in bulletList:
        if a2["rect"].top < 0:
            bulletList.remove(a2)
    for a3 in bulletList:
        screen.blit(a3["surface"], a3["rect"])


enemy1List = []
enemy2List = []
enemy3List = []


def enemy1(screen,which, level):  # 第一个参数which为飞机种类，第二个参数level为难度1-10，数字越大,敌机出现的越快
    t2 = time.time()
    t = t2 - t1
    n = 11 - level
    if n > 10:
        n = 10
    elif n < 1:
        n = 1
    if int(t * 2) % n == 0 and t < int(t) + 0.1:
        enemyImg = "enemy" + str(which) + ".png"
        enemyimg = pygame.image.load(enemyImg)
        enemy_rect = enemyimg.get_rect()
        enemy = {
            "surface": enemyimg,
            "rect": pygame.Rect(random.randint(0, bg_size[0]), random.randint(0, bg_size[1] / 5), \
                                enemy_rect.width, enemy_rect.height),
            "enemy_speed": 1
        }
        enemy1List.append(enemy)
    # 敌机移动
    for b1 in enemy1List:
        b1["rect"].y += b1["enemy_speed"]
    for b2 in enemy1List:
        if b2["rect"].top > bg_size[1]:
            enemy1List.remove(b2)
        screen.blit(b2["surface"], b2["rect"])

def enemy2(screen,which, level):  # 第一个参数which为飞机种类，第二个参数level为难度1-10，数字越大,敌机出现的越快
    t2 = time.time()
    t = t2 - t1
    n = 11 - level
    if n > 10:
        n = 10
    elif n < 1:
        n = 1
    if int(t * 2) % n == 0 and t < int(t) + 0.1:
        enemyImg = "enemy" + str(which) + ".png"
        enemyimg = pygame.image.load(enemyImg)
        enemyimg = pygame.transform.scale(enemyimg,(66,54))
        enemy_rect = enemyimg.get_rect()
        enemy = {
            "surface": enemyimg,
            "rect": pygame.Rect(random.randint(0, bg_size[0]), random.randint(0, bg_size[1] / 5), \
                                enemy_rect.width, enemy_rect.height),
            "enemy_speed": 1
        }
        enemy2List.append(enemy)
    # 敌机移动
    for b1 in enemy2List:
        b1["rect"].y += b1["enemy_speed"]
    for b2 in enemy2List:
        if b2["rect"].top > bg_size[1]:
            enemy2List.remove(b2)
        screen.blit(b2["surface"], b2["rect"])

def enemy3(screen,which, level):  # 第一个参数which为飞机种类，第二个参数level为难度1-10，数字越大,敌机出现的越快
    t2 = time.time()
    t = t2 - t1
    n = 11 - level
    if n > 10:
        n = 10
    elif n < 1:
        n = 1
    if int(t * 2) % n == 0 and t < int(t) + 0.1:
        enemyImg = "enemy" + str(which) + ".png"
        enemyimg = pygame.image.load(enemyImg)
        enemyimg = pygame.transform.scale(enemyimg,(76,64))
        enemy_rect = enemyimg.get_rect()
        enemy = {
            "surface": enemyimg,
            "rect": pygame.Rect(random.randint(0, bg_size[0]), random.randint(0, bg_size[1] / 5), \
                                enemy_rect.width, enemy_rect.height),
            "enemy_speed": 1
        }
        enemy3List.append(enemy)
    # 敌机移动
    for b1 in enemy3List:
        b1["rect"].y += b1["enemy_speed"]
    for b2 in enemy3List:
        if b2["rect"].top > bg_size[1]:
            enemy3List.remove(b2)
        screen.blit(b2["surface"], b2["rect"])

def fight(screen, hero_rect):
    # 击落敌机
    for c1 in enemyList:
        for c2 in bulletList:
            if c2["rect"].colliderect(c1["rect"]):
                bulletList.remove(c2)
                if c1 in enemyList:
                    enemyList.remove(c1)
                    score = score + 1
                screen.blit(bulletimg2, (c2["rect"].x-50,c2["rect"].y-50))
        # 控制英雄飞机不飞出屏幕
    if hero_rect.right >= bg_size[0]:
        hero_rect.right = bg_size[0]
    if hero_rect.left <= 0:
        hero_rect.left = 0
    if hero_rect.top <= 0:
        hero_rect.top = 0
    if hero_rect.bottom >= bg_size[1]:
        hero_rect.bottom = bg_size[1]
    return score
