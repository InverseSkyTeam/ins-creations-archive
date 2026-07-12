



































def feijidazhan():
    import pygame,sys,os,fly,time,random
    score = 0
    p = 0
    pygame.init()
    screen = pygame.display.set_mode((480, 700))
    pygame.display.set_caption("飞机大战")
    bgImg = pygame.image.load("background"+str(random.randint(1,2))+".png")
    heroImg = pygame.image.load("hero"+str(random.randint(1,3))+".png")
    gameoverImg = pygame.image.load("gameover.jpg")
    gameoverImg1 = pygame.transform.scale(gameoverImg,(480,700))
    hero_rect = pygame.Rect(210, 600, 66, 80)
    pygame.mixer.music.load("flysound.wav")
    bg_y1 = 0
    bg_y2 = -700
    try:
        import ntpath # 如果成功，那么是Windows
        FONTNAME = "kaiti"
        del ntpath
    except ImportError: # 如果失败，是MacOS
        FONTNAME = "kaittf"
    bulletimg2 = pygame.image.load("bang.png")
    bg_size = (480, 700)
    bulletList = []
    score = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                hero_rect.center = event.pos
        press=pygame.key.get_pressed()
        if press[273]:
            hero_rect.y = hero_rect.y - 5
        if press[274]:
            hero_rect.y = hero_rect.y + 5
        if press[276]:
            hero_rect.x = hero_rect.x - 5
        if press[275]:
            hero_rect.x = hero_rect.x + 5
        bg_y1 = bg_y1 + 30
        bg_y2 = bg_y2 + 30
        if bg_y1 >= 700:
            bg_y1 = -700
        if bg_y2 >= 700:
            bg_y2 = -700
        screen.blit(bgImg, (0, bg_y1))
        screen.blit(bgImg, (0, bg_y2))
        fly.enemy1(screen,3, 3)
        fly.enemy2(screen,2, 2)
        fly.enemy3(screen,1,1)
        fly.bullet(screen,hero_rect,10)
        for c1 in fly.enemy1List:
            for c2 in fly.bulletList:
                if c2["rect"].colliderect(c1["rect"]):
                    fly.bulletList.remove(c2)
                    if c1 in fly.enemy1List:
                        fly.enemy1List.remove(c1)
                        score = score + 1
                    screen.blit(bulletimg2, (c2["rect"].x-50,c2["rect"].y-50))
        for c1 in fly.enemy2List:
            for c2 in fly.bulletList:
                if c2["rect"].colliderect(c1["rect"]):
                    fly.bulletList.remove(c2)
                    if c1 in fly.enemy2List:
                        fly.enemy2List.remove(c1)
                        score = score + 2
                    screen.blit(bulletimg2, (c2["rect"].x-50,c2["rect"].y-50))
        for c1 in fly.enemy3List:
            for c2 in fly.bulletList:
                if c2["rect"].colliderect(c1["rect"]):
                    fly.bulletList.remove(c2)
                    if c1 in fly.enemy3List:
                        fly.enemy3List.remove(c1)
                        score = score + 3
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
        print(score)
        for enemy in fly.enemy1List:
            enemy_rect = enemy["rect"]
            if hero_rect.colliderect(enemy_rect):
                print("game over")
                screen.blit(gameoverImg1, (0,0))
                pygame.display.update()
                pygame.time.delay(1000)
                pygame.quit()
                sys.exit()
        for enemy in fly.enemy2List:
            enemy_rect = enemy["rect"]
            if hero_rect.colliderect(enemy_rect):
                print("game over")
                screen.blit(gameoverImg1, (0,0))
                pygame.display.update()
                pygame.time.delay(1000)
                pygame.quit()
                sys.exit()
        for enemy in fly.enemy3List:
            enemy_rect = enemy["rect"]
            if hero_rect.colliderect(enemy_rect):
                print("game over")
                screen.blit(gameoverImg1, (0,0))
                pygame.display.update()
                pygame.time.delay(1000)
                pygame.quit()
                sys.exit()
        screen.blit(heroImg, hero_rect)
        screen.blit(pygame.font.SysFont(FONTNAME,30).render("当前分数"+str(score),True,(255,255,255)),(0,0))
        pygame.display.update()
        
        
        
        
import pygame,sys,random
pygame.init()
print("支持鼠标和键盘两种模式")
startlist = [pygame.image.load("game_start_up.png"),pygame.image.load("game_start_down.png")]
startlist[1] = pygame.transform.scale(startlist[1],(300,50))
startlist[0] = pygame.transform.scale(startlist[0],(300,50))
startrect = pygame.Rect(90,550,300,50)
startimg = startlist[0]
screen = pygame.display.set_mode((480, 700))
pygame.display.set_caption("飞机大战")
bgImg = pygame.image.load("background"+str(random.randint(1,2))+".png")
x1 = 0
y1 = 0
bg_y1 = 0
bg_y2 = -700
try:
    import ntpath # 如果成功，那么是Windows
    FONTNAME = "kaiti"
    del ntpath
except ImportError: # 如果失败，是MacOS
    FONTNAME = "kaittf"
pygame.mixer.music.load("flysound.wav")
pygame.mixer.music.play(-1)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            x1 = event.pos[0]
            y1 = event.pos[1]
        if startrect.collidepoint(x1,y1):
            startimg = startlist[1]
            screen.blit(startimg,startrect)
            pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    feijidazhan()
        else:
            startimg = startlist[0]
    bg_y1 = bg_y1 + 30
    bg_y2 = bg_y2 + 30
    if bg_y1 >= 700:
        bg_y1 = -700
    if bg_y2 >= 700:
        bg_y2 = -700
    screen.blit(bgImg, (0, bg_y1))
    screen.blit(bgImg, (0, bg_y2))
    screen.blit(startimg,startrect)
    screen.blit(pygame.font.SysFont(FONTNAME,120).render("飞机大战",True,(255,255,0)),(0,150))
    pygame.display.update()