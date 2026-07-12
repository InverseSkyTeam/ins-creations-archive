#请补充或修改53、92、111行代码。
# import mkpiano
import pygame, time, sys, random
# 可以使用下行代码对接近传感器进行校准
# mkpiano.piano.calibrate()

# pygame初始化、窗口设置
print("接近触感器调整上下，两个按钮中左边的发射子弹，给大米")
pygame.time.delay(1000)#大米，单位是毫秒
pygame.init()
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption("星球大战")

# 音效加载
pygame.mixer.music.load("Starwars.mp3") # 背景音乐
pygame.mixer.music.play(-1)
sound1 = pygame.mixer.Sound("eat.wav") # 吃到蚊虫音效
lose = pygame.mixer.Sound("fail.wav") # 游戏失败音效
win = pygame.mixer.Sound("success.wav") # 游戏胜利音效

# 图片加载
bg = pygame.image.load("stars.png") # 背景
bg = pygame.transform.scale(bg,(1000,600))
dragonfly = pygame.image.load("千年隼.png") # 蜻蜓
dragonfly = pygame.transform.scale(dragonfly,(200,90))
bug = pygame.image.load("星球大战钛战机.png") # 蚊虫
bug = pygame.transform.scale(bug,(131,70))
bird = pygame.image.load("子弹.png") # 小鸟
bird = pygame.transform.scale(bird,(50,18))
bird1 = pygame.image.load("子弹2.png") # 小鸟
bird1 = pygame.transform.scale(bird1,(50,18))
# 蜻蜓初始位置
dragonflyX = 0
dragonflyY = 300

# 蚊虫初始位置（随机）
bugX = 1000
bugY = random.randint(0,500)   

# 小鸟初始位置（随机）
birdX = 1000
birdY = bugY

bird1X = 0
bird1Y = dragonflyY
# 分数归0
score = 0

#设置字体和字号，window电脑字体是kaiti，苹果电脑字体是kaittf
try:
    import ntpath
    myFont = pygame.font.SysFont("kaiti", 50)
    del ntpath
except ImportError:
    myFont = pygame.font.SysFont("kaittf",50)# mac系统使用


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #######################################
    # 通过接近传感器控制蜻蜓上下移动
    # 补充代码，获取接近传感器的距离感应值
    # s = mkpiano.piano.get_distance()
    # if 50 <= s and s < 100:
    #     dragonflyY = dragonflyY - 3
    # if s<50:
    #     dragonflyY = dragonflyY + 3
    press = pygame.key.get_pressed()
    if press[pygame.K_UP]:
        dragonflyY = dragonflyY - 3
    if press[pygame.K_DOWN]:
        dragonflyY = dragonflyY + 3
    ########################################
    
    # 限制蜻蜓在窗口范围内移动
    if dragonflyY < 0:
        dragonflyY = 0
    if dragonflyY > 500:
        dragonflyY = 500    
    
    # 蚊虫左右移动
    bugX = bugX - 1
    if bugX < 0:
        bugX = 1000
        bugY = random.randint(0,500)      

    # 小鸟左右移动
    birdX = birdX - 2
    if birdX < 0:
        birdX = bugX
        birdY = bugY
    
    bird1X = bird1X + 3
    if bird1X > 1000 or press[pygame.K_SPACE]:
        bird1X = 0
        bird1Y = dragonflyY+50
    screen.blit(bg,(0,0))#绘制背景图
    
    # 创建矩形对象（蜻蜓、蚊虫、小鸟）
    b = pygame.Rect(dragonflyX,dragonflyY,200,90)
    s1 = pygame.Rect(bugX,bugY,131,70)
    j = pygame.Rect(birdX,birdY,50,18)
    j1 = pygame.Rect(bird1X,bird1Y,50,18)
    
    # 绑定矩形对象和图片（蜻蜓、蚊虫、小鸟）
    screen.blit(bird1, j1)
    screen.blit(dragonfly, b)
    screen.blit(bug, s1)
    screen.blit(bird, j)
    
    ########################################
    # 补充代码，检测蜻蜓是否吃到蚊子
    if   j1.colliderect(s1):
        sound1.play()
        bugX = 1000
        bugY = random.randint(0,500)
        score = score + 1
    ########################################
    
    # 检测蜻蜓是否碰到小鸟    
    if b.colliderect(j):
        myText = myFont.render("子弹打到了千年隼，游戏结束！",True, (255,190,0))
        screen.blit(myText,(150,250))
        pygame.display.update()
        lose.play()
        time.sleep(2)
        pygame.quit()
        sys.exit()     
    
    ########################################
    # 修改代码，设置游戏胜利的条件：蜻蜓要吃够几只蚊子才算胜利呢？
    if score == 7:
        myText = myFont.render("全部战机已消灭！",True, (255,190,0))
        screen.blit(myText,(300,250))
        pygame.display.update()
        win.play()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    ########################################
    
    # 显示更新
    myText = myFont.render("消灭 "+str(score)+" 只钛战机啦！",True,(255,190,0))
    screen.blit(myText,(0,20))
    pygame.display.update()
    time.sleep(0.001)
