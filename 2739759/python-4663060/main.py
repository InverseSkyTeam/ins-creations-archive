'''要求：
1. 字母从屏幕下方喷出，向上移动；
2. 字母碰到屏幕上方消失；
3. 通过敲击对应的按键可以消除字母；
附加题：可以考虑分数统计、5次机会和难度升级功能
'''
print("\033[3m给大敏！！！")
def dazi():
    import pygame,sys,random,time
    pygame.init()
    screen = pygame.display.set_mode((800,500))
    pygame.display.set_caption("打字游戏")
    bgimg = pygame.image.load("bg1.png")
    bgimg = pygame.transform.scale(bgimg,(800,500))
    myFont=pygame.font.SysFont(None,80)
    letterList = ["a", "b", "c", "d", "e", "f", "g", "h","i", 
        "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", 
        "u", "v", "w", "x", "y", "z","0","1","2","3","4","5","6"
        ,"7","8","9","shift","enter","ctrl","tab","CapsLK","backspace",
        "esc","Fn","Alt","up","down","left","right"]
    letterWait = []
    t1=time.time()
    
    letterSpeed = 1   # 字母下落速度
    try:
        import ntpath # 如果成功，那么是Windows
        myFont1 = pygame.font.SysFont("kaiti", 20)
        del ntpath
    except ImportError: # 如果失败，是MacOS
        myFont1 = pygame.font.SysFont("kaittf", 20)   #mac系统使用
    score = 0
    scoreText = "当前分数：0"
    red = (255,0,0)
    
    chance = 5    
    chanceText = "剩余机会：5" 
    green = (0,255,0)    
    
    levelText = "当前关卡：1"     # 设置关卡显示内容
    blue = (0,0,255)    # 设置颜色
    pygame.mixer.music.load("bgSound.wav")
    pygame.mixer.music.play(-1)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                for letter in letterWait:
                    # 计算分数，完成要求，补充48-50行代码
                    #要求：1.完成按键消除字母（使用ASCII码表示字母对应键盘事件）
                    # 2.从列表中移除该字典元素（用remove()函数）
                    # 3.完成分数的计算，每消除一个字母，score加一
                    
                    if letter["word"] == "shift":
                        letter1 = 303
                    elif letter["word"] == "enter":
                        letter1 = 13
                    elif letter["word"] == "ctrl":
                        letter1 = 305
                    elif letter["word"] == "tab":
                        letter1 = 9
                    elif letter["word"] == "CapsLK":
                        letter1 = 301
                    elif letter["word"] == "backspace":
                        letter1 = 8
                    elif letter["word"] == "Fn":
                        letter1 = 101
                    elif letter["word"] == "esc":
                        letter1 = 27
                    elif letter["word"] == "Alt":
                        letter1 = 308
                    elif letter["word"] == "up":
                        letter1 = 273
                    elif letter["word"] == "down":
                        letter1 = 274
                    elif letter["word"] == "left":
                        letter1 = 276
                    elif letter["word"] == "right":
                        letter1 = 275
                    else:
                        letter1 = ord(letter["word"])
                    if event.key == letter1:
                        letterWait.remove(letter)
                        score = score + 1
                        scoreText = "当前分数："+str(score)
        t2 = time.time()
        if t2 - t1 >= 2:
            t1 = t2
            l1 = random.choice(letterList)
            c1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) 
            #设置字母的x y坐标，补充61-64行代码完成要求
            #要求：1.x设置为画布内随机值（建议范围0-700）
            # 2.y设置固定值，完成字母从画布下方出现
            # 3.完成字典创建和把字典添加到列表中
            x1 =   random.randint(0,620)
            y1 =   440
            letterDict = {"word":l1,"x":x1,"y":y1,"color":c1}
            letterWait.append(letterDict)
        screen.fill((255, 255, 255))
        screen.blit(bgimg,(0,0))
        for letter in letterWait: # 绘制字母
            x2 = letter["x"]
            y2 = letter["y"]
            l2 = letter["word"]
            c2 = letter["color"]
            textImage = myFont.render(l2, True, c2)
            screen.blit(textImage, (x2, y2))
        # 字母上移
        for letter in letterWait:
            #补充77代码：完成字母上移（y值减去letterSpeed）
            letter["y"] = letter["y"] - letterSpeed
            #补充79-81行代码，当字母（y值）超出画布时，列表移除字母字典并chance减一
            if letter["y"] < 0:
                letterWait.remove(letter)
                chance = chance - 1
                chanceText = "剩余机会："+str(chance)
                # 退出：补充84-86行代码，当chance小于0时，退出游戏
                if chance <= 0:
                    pygame.quit()
                    sys.exit()
        # 难度晋级：补充89-91行代码，设置关卡，当score摩10等于0时进入下一关
        # 下一关可以用score整除10加一表示当前关卡数，并把字母速度设置为当前关卡数
        if score%10 == 0:
            letterSpeed = score//10
            level = letterSpeed
            levelText = "当前关卡："+str(level)
        # 显示信息
        sText = myFont1.render(scoreText,True,red)
        screen.blit(sText,(600,0))
        
        cText = myFont1.render(chanceText,True,green)
        screen.blit(cText,(600,25))
        
        lText = myFont1.render(levelText,True,blue)
        screen.blit(lText,(600,50))
        pygame.display.update()
        time.sleep(0.02)

import pygame,sys,random,time
pygame.init()
screen = pygame.display.set_mode((800,500))
pygame.display.set_caption("打字游戏")
x = 0
huarect = pygame.Rect(0,0,10,10)
screen.fill((255,255,255))
try:
    import ntpath # 如果成功，那么是Windows
    FONTNAME = "kaiti"
    del ntpath
except ImportError: # 如果失败，是MacOS
    FONTNAME = "kaittf"
myWord = """你好！欢迎来到打字游戏！"""
pos = 0,0
screen.blit(pygame.font.SysFont(FONTNAME,30).render(myWord,True,(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))),(pos))
pygame.display.update()
myWord = """1.你需要敲击对应按键来消除字符"""
pos = 0,30
screen.blit(pygame.font.SysFont(FONTNAME,30).render(myWord,True,(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))),(pos))
pygame.display.update()
myWord = """2.如果字符到达顶端会减掉生命值"""
pos = 0,60
screen.blit(pygame.font.SysFont(FONTNAME,30).render(myWord,True,(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))),(pos))
pygame.display.update()
myWord = """3.如果生命值为0会结束游戏"""
pos = 0,90
screen.blit(pygame.font.SysFont(FONTNAME,30).render(myWord,True,(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))),(pos))
pygame.display.update()
myWord = """4.字符会随着消除字符的数量改变移动速度"""
pos = 0,120
screen.blit(pygame.font.SysFont(FONTNAME,30).render(myWord,True,(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))),(pos))
pygame.display.update()
time.sleep(5)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            huarect.center = (event.pos[0],400) 
            pygame.display.update()
            if huarect.collidepoint(580,400):
                dazi()
    screen.blit(pygame.font.SysFont(FONTNAME,30).render(">>>滑动以解锁>>>",True,(0,0,0)),(280,400))
    pygame.display.update()