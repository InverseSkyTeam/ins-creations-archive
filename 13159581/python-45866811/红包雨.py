import pygame,time,sys,random
pygame.init()
screen = pygame.display.set_mode((370, 600))
pygame.display.set_caption("红包雨来临")
    
#加载图片素材
bgImg = pygame.image.load("bg1.png")
hongbaoImg = pygame.image.load("hongbao1.png")
overImg = pygame.image.load("over1.png")
    
myFont = pygame.font.SysFont("kaiti", 23)    # windows系统字体
# myFont = pygame.font.SysFont("kaittf", 23) # mac系统字体
    
# 变量初始化
score = 0   # 初始分数
pos = (-100, -100)  # 鼠标初始位置
hongbaoRectList = []  # 红包列表
    
# 创建多个红包矩形对象
for i in range(6):
    x = random.randint(-10,315)
    y = random.randint(-600, -50)
    hongbaoRect = pygame.Rect(x, y, 40, 55)
    hongbaoRectList.append(hongbaoRect)
        
start = time.time()
    
while True:
        
    for event in pygame.event.get():
        # 退出事件
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # 鼠标位置
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
        else:
            pos = (-100, -100)
                
    # 绘制背景图
    screen.blit(bgImg, (0, 0))
    
    for n in hongbaoRectList:
        # 判断红包下落的位置
        if n.y > 600:
            n.x = random.randint(-10,315)
            n.y = random.randint(-600, -50)
            # 碰撞检测
        elif n.collidepoint(pos):
            score = score + 1
            n.x = random.randint(-10,315)
            n.y = random.randint(-600, -50)
                
        screen.blit(hongbaoImg, n)
        #控制红包速度
        n.y = n.y + 2
    
        # 显示红包数
        text2 = "score: " + str(score)
        scoreText = myFont.render(text2, True, (255, 255, 255))
        screen.blit(scoreText, (10, 10))
        
    now = time.time() # 当前时间
    interval =  30 - int(now-start)
    if interval <= 0:
        screen.blit(overImg, (0, 0))
        pygame.display.update()
        time.sleep(3)
        exit()
            
    # 显示时间
    text3 = "time: " + str(interval)
    timeText = myFont.render(text3, True, (255, 255, 255))
    screen.blit(timeText, (220, 10))
    
    pygame.display.update()
    time.sleep(0.009)
