from moviepy.editor import *
def biao():
    import pygame,sys
    pygame.init()
    try:
        import ntpath # 如果成功，那么是Windows
        FONTNAME = "Simhei"
        del ntpath
    except ImportError: # 如果失败，是MacOS
        FONTNAME = "heititf"
    pygame.display.set_caption("大敏老师表情包")
    clip = VideoFileClip('logo.gif')
    clip= clip.resize(newsize=(800,600))
    clip.preview()
    screen = pygame.display.set_mode((800,600))
    logo = pygame.image.load("logo_img.png")
    logo = pygame.transform.scale(logo,(800,600))
    for i in range(300):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((255,255,255))
        screen.blit(logo,(-1,-1))
        screen.blit(pygame.font.SysFont(FONTNAME,50).render("Mac工作室",True,(0,0,0)),(289.5,450))
        screen.blit(pygame.font.SysFont(FONTNAME,20).render("极致、极爱、极简",True,(0,0,0)),(320,500))
        pygame.display.update()
    try:
        import ntpath # 如果成功，那么是Windows
        FONTNAME = "kaiti"
        del ntpath
    except ImportError: # 如果失败，是MacOS
        FONTNAME = "kaittf"
    # 以下是第二个界面主循环
    while True:
        import pygame, sys, time, random, s1
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("大敏老师表情包")
        screen.fill((0, 0, 0))
        picList = []
        for i in range(1,11):
            a = "大敏囧照"+str(i)+".PNG"
            picList.append(a)
        imgList = []
        for i in picList:
            # 补充17行代码，使用convert()加载图片
            myImage = pygame.image.load(i).convert()
            myImage = pygame.transform.scale(myImage,(800,600))
            imgList.append(myImage)
        b = 0
        imgNum = 0
        image = imgList[imgNum]
        a = 0
        pygame.mixer.music.load("遇见你的时候所有星星都落到我头上.mp3")
        pygame.mixer.music.play(-1)
        s1.rain(screen,255,255,0)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    a = 0
                    # 补充33-35行代码，实现按键换图，每按一次键，索引值加一，
                    # 当索引值大于等于列表长度时，设置索引值为0
                    imgNum = imgNum+1
                    if imgNum == len(picList):
                        imgNum = 0
            image = imgList[imgNum]        
            # 补充39-41行代码，使用set_alpha()设置图片透明度，并实现图片淡入的效果   
            if b == 0:
                a = a + 1
            if b == 1:
                a = a - 1
            if a >= 255:
                time.sleep(1)
                b = 1
            if a <= 0:
                b = 0
            image.set_alpha(a)
            screen.fill((0, 0, 0))
            screen.blit(image, (0, 0))
            pygame.display.update()
            time.sleep(0.01)
biao()