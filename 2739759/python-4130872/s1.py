import pygame,sys,time,random
def rain(screen,t,h,n):
    try:
        import ntpath # 如果成功，那么是Windows
        FONTNAME = "kaiti"
        del ntpath
    except ImportError: # 如果失败，是MacOS
        FONTNAME = "kaittf"
    scene=1
    FONT_PX = 15
    font = pygame.font.SysFont("123.ttf", 25)
    bg_suface = pygame.Surface((800, 720), flags=pygame.SRCALPHA)
    bg_suface.fill(pygame.Color(0, 0, 0, 28))
    screen.fill((0, 0, 0))
    letter = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c',
              'v', 'b', 'n', 'm']
    texts = [
    font.render(str(letter[i]), True, (t,h,n)) for i in range(26)
    ]
    # 按屏幕的宽带计算可以在画板上放几列坐标并生成一个列表
    column = int(800 / FONT_PX)
    drops = [0 for i in range(column)]
    flag = False
    while scene==1:
        # 从队列中获取事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_q:
                #     flag = True
                scene=2
                break
        if scene==2:
            break
        # if scene==2 and flag == True:     
        #     pygame.quit()
        #     sys.exit()
        #     break
        # if scene==2 and flag == False:
        #     break

        # 将暂停一段给定的毫秒数
        pygame.time.delay(30)
     
        # 重新编辑图像第二个参数是坐上角坐标
        screen.blit(bg_suface, (0, 0))
     
        for i in range(len(drops)):
            text = random.choice(texts)
     
            # 重新编辑每个坐标点的图像
            screen.blit(text, (i * FONT_PX, drops[i] * FONT_PX))
     
            drops[i] += 1
            if drops[i] * 10 > 720 or random.random() > 0.95:
                drops[i] = 0
        screen.blit(pygame.font.SysFont(FONTNAME,30).render("按下任意键切换图片",True,(255,255,255)),(265,400))
        pygame.display.flip()
