#要求同学们加载f1-f4.png,背景图为bg.png，完成福字的拼图
import pygame, sys
pygame.init()
def sd(printword,speed):
    for i in printword:
        print(i,end="")
        pygame.time.delay(speed)
    print("")
def pin():
    import pygame,sys,random,explore
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("福字拼图")
    
    #加载新年背景和福字图片
    bgImg = pygame.image.load("bg.png")
    imgNameList = ["f1.png", "f2.png", "f3.png","f4.png"]
    imgList = []
    rectList = []
    moveRect = ""
    #for循环加载图片
    for i in imgNameList:
        img = pygame.image.load(i)
        imgList.append(img)
    #for循环创建矩形块
    for i in range(4):
        x = random.randint(0, 600)
        y = random.randint(0, 400)
        rect = pygame.Rect(x,y,200,200)
        rectList.append(rect)
    music=pygame.mixer.music.load("我和我的祖国.mp3")
    pygame.mixer.music.play(-1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # 补全31-34行代码，当鼠标按下时进行碰撞检测（collidepoint），
            # 并设置moveRect
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in rectList:
                    if i.collidepoint(event.pos):
                        moveRect = i
            # 补全36-37代码，当鼠标抬起时moveRect设置为空字符串""
            elif event.type == pygame.MOUSEBUTTONUP:
                moveRect = ""
            # 补全40-42代码，当鼠标移动时（MOUSEMOTION），调整moveRect中心为鼠标位置
            # 注意判断 moveRect != ""
            elif event.type == pygame.MOUSEMOTION:
                if moveRect != "":
                    moveRect.center = event.pos
        screen.blit(bgImg, (0, 0))
        for i in range(4):
            screen.blit(imgList[i], rectList[i])
        explore.win(rectList)
        pygame.display.update()
def da():
    # 1.能够通过键盘控制大嘴怪的移动的代码
    # 2.当大嘴怪碰到食物时吃掉食物
    
    #初始化
    import pygame,sys,random
    pygame.init()
    render = 0
    screen = pygame.display.set_mode((700, 700))
    pygame.display.set_caption("贪吃大嘴怪")
    bgImg = pygame.image.load("bgPic.png")
    #设置变量、矩形
    times=60
    score=0
    num=1
    hero_x = 300
    hero_y = 300
    hero_size = 100
    hero_speed = 5
    hero1 = pygame.image.load("hero1.png")
    hero2 = pygame.image.load("hero2.png")
    hero3 = pygame.image.load("hero3.png")
    heroImg = [hero1, hero2, hero3]
    heroImgs = pygame.transform.scale(heroImg[random.randint(0, 2)], (hero_size, hero_size))
    #加载图片
    fruit1 = pygame.image.load("fruit1.png")
    fruit2 = pygame.image.load("fruit2.png")
    fruit3 = pygame.image.load("fruit3.png")
    fruit4 = pygame.image.load("fruit4.png")
    fruit5 = pygame.image.load("fruit5.png")
    fruitImg = [fruit1, fruit2, fruit3, fruit4, fruit5]
    fruitImgs = pygame.transform.scale(fruitImg[random.randint(0, 4)], (40, 40))
    fruitList = []
    print("\033[1;36m通过1、2、3、4、5键调整背景音乐（1是Faded，2是下山，3是我和我的祖国，4是青花瓷(纯音乐)，5是芒种）；上、下、左、右控制大嘴怪移动。倒计时三秒开始！")
    for i in range (3,0,-1):
        print(i)
        pygame.time.delay(1000)
    for i in range(10):
        fruitRect = pygame.Rect(random.randint(0,675),random.randint(0,675),40,40)
        fruitList.append(fruitRect)
    font = pygame.font.SysFont("kaiti",30)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                if score >=120:
                    print("\033[1;33m你吃了",score,"个水果，敲厉害，大神级！！！狂击999（666翻啦！）")
                elif score <120 and score >=100:
                    print("\033[1;33m你吃了",score,"个水果，厉害，大师级！！！")
                elif score < 100 and score >=80:
                    print("\033[1;33m你吃了",score,"个水果，中等偏上，黄金级")
                elif score < 80 and score >=60:
                    print("\033[1;33m你吃了",score,"个水果，中等，白银级")
                elif score < 60 and score >=40:
                    print("\033[1;33m你吃了",score,"个水果，中等偏下，青铜级")
                else:
                    print("\033[1;33m你吃了",score,"个水果，继续努力，石器级")
        press=pygame.key.get_pressed()
        if press[273]:
            hero_y=hero_y-hero_speed
        if press[274]:
            hero_y=hero_y+hero_speed
        if press[276]:
            hero_x=hero_x-hero_speed
        if press[275]:
            hero_x=hero_x+hero_speed
        if press[49]:
            music=pygame.mixer.music.load("Faded.mp3")
            pygame.mixer.music.play(-1)
        if press[50]:
            music=pygame.mixer.music.load("下山.mp3")
            pygame.mixer.music.play(-1)
        if press[51]:
            music=pygame.mixer.music.load("我和我的祖国.mp3")
            pygame.mixer.music.play(-1)
        if press[52]:
            music=pygame.mixer.music.load("青花瓷.mp3")
            pygame.mixer.music.play(-1)
        if press[53]:
            music=pygame.mixer.music.load("芒种.mp3")
            pygame.mixer.music.play(-1)
        heroRect = pygame.Rect(hero_x, hero_y, hero_size, hero_size)
        for n in fruitList:
            if heroRect.colliderect(n):
                fruitList.remove(n)
                print("\033[1;34m吃掉啦")
                soundList = ["1","2","3","4","5","6","7","8"]
                soundnum = random.choice(soundList)
                sound = pygame.mixer.Sound(soundnum+".wav")
                sound.play()
                score=score+1
                word = "共吃了"+str(score)+"个"
                r1 = font.render(word,True,(0,255,0))
                hero_speed = hero_speed + 0.1
        screen.blit(bgImg, (0, 0))
        for rect in fruitList:
            screen.blit(fruitImgs, rect)
        if len(fruitList) == 3 or len(fruitList) < 3:
            fruitImgs = pygame.transform.scale(fruitImg[random.randint(0, 4)], (40, 40))
            for i in range(10):
                fruitRect = pygame.Rect(random.randint(0,675),random.randint(0,675),40,40)
                fruitList.append(fruitRect)
            for rect in fruitList:
                screen.blit(fruitImgs, rect)
        num=num+1
        if times!=0:
            if num%50==0:
                print("\033[31m还剩"+str(times)+"秒")
                times=times-1
        if times == 0:
            if score >=80:
                print("\033[1;33m你吃了",score,"个水果，敲厉害，大神级！！！狂击999（666翻啦！）")
            elif score <80 and score >=70:
                print("\033[1;33m你吃了",score,"个水果，厉害，大师级！！！")
            elif score < 70 and score >=60:
                print("\033[1;33m你吃了",score,"个水果，中等偏上，黄金级")
            elif score < 60 and score >=50:
                print("\033[1;33m你吃了",score,"个水果，中等，白银级")
            elif score < 50 and score >=40:
                print("\033[1;33m你吃了",score,"个水果，中等偏下，青铜级")
            else:
                print("\033[1;33m你吃了",score,"个水果，继续努力，石器级")
            pygame.quit()
            sys.exit()
        screen.blit(heroImgs, heroRect)
        screen.blit(r1, (0,0))        
        pygame.display.update()
def xiao():
    import pygame, sys, random, time
    t1 = time.time()
    a = 1
    b = 5
    t = 0
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("消灭新型冠状病毒！！！")
    bgImg = pygame.image.load('室内.png')
    bgImg = pygame.transform.scale(bgImg,(800,600))
    gunImg = pygame.image.load('喷瓶1.png')
    gunImg = pygame.transform.scale(gunImg,(100,100))
    gunImg2 = pygame.image.load('喷瓶2.png')
    gunImg2 = pygame.transform.scale(gunImg2,(200,100))
    enemyImg = pygame.image.load('病毒.png')
    enemyImg = pygame.transform.scale(enemyImg,(100,100))
    enemyX = 0
    enemyY = 0
    enemyRect = pygame.Rect(enemyX, enemyY, 100 ,100)
    gunRect = pygame.Rect(0, 0, 100,100)
    num = 0  # 击中敌人数量
    pygame.mixer.music.load("下山.mp3")
    pygame.mixer.music.play(-1)
    gunSound = pygame.mixer.Sound("掉落.wav")
    print("""提示：
长按鼠标可以暂停病毒的移动""")
    while True:
        screen.blit(bgImg, (0, 0))
        myWord = "勇士，欢迎您。由于人类捕杀蝙蝠导致一种新型冠状病毒出现，"
        myFont = pygame.font.SysFont("kaiti", 25)
        myNum = myFont.render(myWord, True, (255, 0, 0))
        screen.blit(myNum, (0, 140)) 
        myWord1 = "你需要用鼠标控制喷壶移动喷出酒精，在病毒逃出房间前杀死病毒"
        myNum1 = myFont.render(myWord1, True, (255, 0, 0)) 
        screen.blit(myNum1, (0, 170))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                x = event.pos[0]
                y = event.pos[1]
                gunRect.center = (x, y)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                screen.blit(gunImg2, gunRect)  
                pygame.display.update()
                if enemyRect.collidepoint(event.pos):
                    gunSound.play()
                    num = num + 1
                    myWord = "杀灭病毒数:" + str(num)
                    myFont = pygame.font.SysFont("kaiti", 30)
                    myNum = myFont.render(myWord, True, (255, 0, 0))
                    enemyX = random.randint(0, 200)
                    enemyY = random.randint(0, 400)
                    time.sleep(1)
        # 敌人移动    
            enemyX = enemyX + random.randint(a, b)
        if t < 40:
            a = 1
            b = 5
        elif t>=40:
            myWord1 = "感受病毒王的愤怒吧！！！"
            myNum1 = myFont.render(myWord1, True, (255, 0, 0))
            screen.blit(myNum1, (0, 200)) 
            a = 15
            b = 25
        elif t >= 60:
            screen.blit(gameoverImg, (0, 0))
            myWord1 = "一分钟内你杀死了"+str(num)+"个病毒"
            myNum1 = myFont.render(myWord1, True, (255, 0, 0))
            screen.blit(myNum1, (0, 300)) 
            print(myWord)
            pygame.time.delay(7000)
            pygame.quit()
            sys.exit()
        # 绘制相关元素
        enemyRect = pygame.Rect(enemyX, enemyY, 200, 200)
        screen.blit(enemyImg, enemyRect)
        screen.blit(gunImg, gunRect)
        myNum = myFont.render(myWord, True, (255, 0, 0))
        if t < 0 or enemyX > 800:
            myWord1 = "一分钟内你杀死了"+str(num)+"个病毒"
            myNum1 = myFont.render(myWord1, True, (255, 0, 0))
            screen.blit(myNum1, (0, 300)) 
            print(myWord1)
            pygame.time.delay(7000)
            pygame.quit()
            sys.exit()
        t2 = time.time()
        t = t2-t1
        pygame.display.update() 
while True:
    sd("墙裂（强烈）要求给大敏老师！！！！！！！！！！",75)
    sd("""\033[1;36m欢迎来到pygame小游戏合集
有以下几个小游戏：
\033[1;33m1.福字拼图
2.贪吃大嘴怪
3.消灭新型冠状病毒""",75)
    a = input("选哪个？（输入序号）:")
    sd("""\033[1;32m抵制不良游戏，杜绝盗版游戏
适度游戏健脑，沉迷游戏伤身""",100)
    if a == "1":
        pin()
    if a == "2":
        da()
    if a == "3":
        xiao()