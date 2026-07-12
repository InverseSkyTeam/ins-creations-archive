'''
要求：
1. 设置BOSS的生命值、防御值；
2. 三个按键（比如A、S、D键）对应三种攻击技能，扣掉BOSS不同的血量；
3. BOSS的生命值小于等于0时，获得胜利。
'''
import pygame,sys
pygame.init()
def sd(printword,speed):
    for i in printword:
        print(i,end="")
        pygame.time.delay(speed)
    print("")
def  boss():
    import pygame, sys
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("BOSS大战")
    bgPic = pygame.image.load("bg.png")
    GREEN = (0, 255, 0)
    
    petPicList = ["monster1.png","monster2.png","monster3.png"]
    petList = []
    for i in petPicList: 
        monster = pygame.image.load(i)
        petList.append(monster)
    monster = petList[1]
    
    myword = "欢迎挑战，按下ASD键攻击BOSS"
    #myFont = pygame.font.SysFont("heittf", 50)   # 苹果电脑使用
    myFont = pygame.font.SysFont("simhei", 30)       # windows电脑使用
    
    life = 100 # 敌人生命
    attack = [10,20,30] # 英雄攻击力
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    monster = petList[0]
                    life = life-attack[0]
                    myword = "你用了招数a,对方掉血:"+str(attack[0])+" 对方剩余血量为:"+str(life)
                # 补全下面代码，当按下s\d按键时，敌人生命值减少相应值；
                # 实现发动攻击，改变敌人图片，使monster等于petList[1]/petList[2]
                # 文字显示对方掉血值和剩余血量
                elif event.key == pygame.K_s:
                    monster = petList[1]
                    life = life-attack[1]
                    myword = "你用了招数a,对方掉血:"+str(attack[1])+" 对方剩余血量为:"+str(life)
                elif event.key == pygame.K_d:
                    monster = petList[2]
                    life = life-attack[2]
                    myword = "你用了招数a,对方掉血:"+str(attack[2])+" 对方剩余血量为:"+str(life)
        # 补全50-51行代码，绘制背景（bgPic）和角色（monster）
        screen.blit(bgPic,(0,0))
        screen.blit(monster,(200,150))
        myText = myFont.render(myword, True, GREEN)
        screen.blit(myText, (30, 500))
        # 补全55-57行代码，当敌人血量（life）小于0时，加载并显示图片"win.png"
        if life <= 0:
            a = pygame.image.load("win.png")
            screen.blit(a, (0, 0))
        pygame.display.update()
def kou():
    import pygame, sys, random
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("口袋妖精大作战")
    bgPic = pygame.image.load("bg1.png")
    # 妖精图片
    petPicList = ["pet1.png", "pet11.png", "pet111.png","pet1111.png","pet11111.png", 
                  "pet2.png","pet22.png", "pet222.png","pet2222.png","pet22222.png"]
    petList = []   # 存放img对象
    for i in petPicList:
        img = pygame.image.load(i)
        petList.append(img)
    myPet = petList[0]
    enemyPet = petList[5]
    # 初始位置
    petX = 50
    petY = 100
    enemyX = 400
    enemyY = 100
    # 背景音乐
    pygame.mixer.music.load("bgSound1.mp3")
    pygame.mixer.music.play(-1)
    # 音效用于发招播放
    sounds = ["sound01.wav", "sound02.wav", "sound03.wav"]
    soundList = []
    for i in sounds:
        s = pygame.mixer.Sound(i)
        soundList.append(s)
    # 文字设置
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    textColor = BLUE
    myword = "欢迎挑战,英雄按ASD键发送技能,敌人按JKL键发送技能"
    # myFont = pygame.font.SysFont("heittf", 50)   # 苹果电脑使用
    myFont = pygame.font.SysFont("kaiti", 30)       # windows电脑使用
    # 英雄属性
    life = 100
    attack = [10,20,30]
    # 敌人属性
    life2 = 100
    attack2 = [10,20,30]
    # # 出招顺序：1代表玩家1，2代表玩家2，3代表战斗结束
    turn = random.randint(1, 2)
    sd("""\033[1;32m由于屏幕太小，提示写在这里：
\033[1;33m1.这是一个双人游戏，win表示玩家一胜，fail表示玩家二胜
2.玩家一按ASD攻击（攻击力：D>S>A）玩家二按JKL攻击（攻击力：L>K>J）""",50)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and turn == 1:                
                    life2 = life2-attack[0]
                    life = life-int(attack[0]/3)
                    myword = "你用了招数a,对方掉血:"+str(attack[0])+" 对方剩余血量为:"+str(life2)
                    textColor = RED
                    turn = 2
                    # 切换图片和声音
                    myPet = petList[1]
                    soundList[0].play()
                    enemyPet = petList[9]                
                elif event.key == pygame.K_s and turn == 1:                
                    life2 = life2-attack[1]
                    life = life-int(attack[1]/3)
                    myword = "你用了招数s,对方掉血："+str(attack[1])+" 对方剩余血量为:"+str(life2)
                    textColor = RED
                    turn = 2
                    # 切换图片和声音
                    myPet = petList[2]
                    soundList[1].play()
                    enemyPet = petList[9]
                #注意：补充下行代码，按下d键时并且turn等于1，完成出招
                elif event.key == pygame.K_d and turn == 1: 
                    #注意：补充下行代码，参考上文完成血量公式的计算
                    life2 = life2-attack[2]
                    life = life-int(attack[2]/3)
                    myword = "你用了招数d,对方掉血："+str(attack[2])+" 对方剩余血量为:"+str(life2)
                    textColor = RED
                    turn = 2
                    # 切换图片和声音
                    myPet = petList[3]
                    soundList[2].play()
                    enemyPet = petList[9]
                elif event.key == pygame.K_j and turn == 2:                
                    life = life-attack2[0]
                    life2 = life2-int(attack2[0]/3)
                    myword = "敌人用了招数j,你掉血："+str(attack2[0])+" 你剩余血量为:"+str(life)
                    textColor = GREEN
                    turn = 1
                    # 切换图片和声音
                    enemyPet = petList[6]
                    soundList[2].play()
                    myPet = petList[4]
                elif event.key == pygame.K_k and turn == 2:                
                    life = life-attack2[1]
                    life2 = life2-int(attack2[1]/3)
                    myword = "敌人用了招数k,你掉血："+str(attack2[1])+" 你剩余血量为:"+str(life)
                    textColor = GREEN
                    turn = 1
                    # 切换图片和声音
                    enemyPet = petList[7]
                    soundList[1].play()
                    myPet = petList[4]
                elif event.key == pygame.K_l and turn == 2:                
                    life = life-attack2[2]
                    life2 = life2-int(attack2[2]/3)
                    myword = "敌人用了招数l,你掉血："+str(attack2[2])+" 你剩余血量为:"+str(life)
                    textColor = GREEN
                    turn = 1
                    # 切换图片和声音
                    enemyPet = petList[8]
                    soundList[0].play()
                    myPet = petList[4]
    
        # 角色移动
        petX = petX + random.randint(-1, 1)
        if petX > 70 or petX < 30:
            petX = 50
        petY = petY + random.randint(-1, 1)
        if petY > 120 or petY < 80:
            petY = 100
        enemyX += random.randint(-1, 1)
        if enemyX > 420 or enemyX < 380:
            enemyX = 400
        enemyY += random.randint(-1, 1)
        if enemyY > 120 or enemyY < 80:
            enemyY = 100
        # 绘制背景和角色
        screen.blit(bgPic, (0, 0))
        screen.blit(myPet, (petX, petY))
        screen.blit(enemyPet, (enemyX, enemyY))
        myText = myFont.render(myword, True, textColor)
        screen.blit(myText, (60, 520))
        #显示血量
        lifeTxt = "血量：" + str(life)
        lifeText = myFont.render(lifeTxt, True, RED)
        screen.blit(lifeText, (30, 30))
        lifeTxt2 = "血量：" + str(life2)
        lifeText2 = myFont.render(lifeTxt2, True, RED)
        screen.blit(lifeText2, (640, 30))
        # 判断胜负
        if life <= 0:
            bgPic1 = pygame.image.load("fail.png")
            screen.blit(bgPic1, (0, 0))
            turn = 3
        elif life2 <= 0:
            bgPic2 = pygame.image.load("win2.png")
            screen.blit(bgPic2, (0, 0))
            turn = 3
        pygame.display.update()
def kou1():
    import pygame, sys, random
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("口袋妖精大作战")
    bgPic = pygame.image.load("bg1.png")
    # 妖精图片
    petPicList = ["pet1.png", "pet11.png", "pet111.png","pet1111.png","pet11111.png", 
                  "pet2.png","pet22.png", "pet222.png","pet2222.png","pet22222.png"]
    petList = []   # 存放img对象
    for i in petPicList:
        img = pygame.image.load(i)
        petList.append(img)
    myPet = petList[0]
    enemyPet = petList[5]
    # 初始位置
    petX = 50
    petY = 100
    enemyX = 400
    enemyY = 100
    # 背景音乐
    pygame.mixer.music.load("bgSound1.mp3")
    pygame.mixer.music.play(-1)
    # 音效用于发招播放
    sounds = ["sound01.wav", "sound02.wav", "sound03.wav"]
    soundList = []
    for i in sounds:
        s = pygame.mixer.Sound(i)
        soundList.append(s)
    # 文字设置
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    textColor = BLUE
    myword = "欢迎挑战,英雄按ASD键发送技能,敌人按JKL键发送技能"
    # myFont = pygame.font.SysFont("heittf", 50)   # 苹果电脑使用
    myFont = pygame.font.SysFont("kaiti", 30)       # windows电脑使用
    # 英雄属性
    life = 100
    attack = [10,20,30]
    # 敌人属性
    life2 = 100
    attack2 = [10,20,30]
    # # 出招顺序：1代表玩家1，2代表玩家2，3代表战斗结束
    turn = random.randint(1, 2)
    sd("""\033[1;32m由于屏幕太小，提示写在这里：
\033[1;33m1.这是一个双人游戏，win表示玩家一胜，fail表示玩家二胜
2.玩家一按ASD攻击（攻击力：D>S>A）玩家二按JKL攻击（攻击力：L>K>J）
3.最强攻击力会减血，其余攻击力会加血
4.按下W键会玩家一加血25，按下I键会玩家二加血25""",50)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and turn == 1:                
                    life2 = life2-attack[0]
                    life = life+int(attack[0]/3)
                    myword = "你用了招数a,对方掉血:"+str(attack[0])+" 对方剩余血量为:"+str(life2)
                    textColor = RED
                    turn = 2
                    # 切换图片和声音
                    myPet = petList[1]
                    soundList[0].play()
                    enemyPet = petList[9]                
                elif event.key == pygame.K_s and turn == 1:                
                    life2 = life2-attack[1]
                    life = life+int(attack[1]/3)
                    myword = "你用了招数s,对方掉血："+str(attack[1])+" 对方剩余血量为:"+str(life2)
                    textColor = RED
                    turn = 2
                    # 切换图片和声音
                    myPet = petList[2]
                    soundList[1].play()
                    enemyPet = petList[9]
                #注意：补充下行代码，按下d键时并且turn等于1，完成出招
                elif event.key == pygame.K_d and turn == 1: 
                    #注意：补充下行代码，参考上文完成血量公式的计算
                    life2 = life2-attack[2]
                    life = life-int(attack[2]/3)
                    myword = "你用了招数d,对方掉血："+str(attack[2])+" 对方剩余血量为:"+str(life2)
                    textColor = RED
                    turn = 2
                    # 切换图片和声音
                    myPet = petList[3]
                    soundList[2].play()
                    enemyPet = petList[9]
                elif event.key == pygame.K_w and turn == 1:
                    life = life+25
                    myPet = petList[0]
                    myword = "你用了招数W,你加血25,敌人剩余血量为:"+str(life)
                    textColor = GREEN
                    turn = 2
                elif event.key == pygame.K_j and turn == 2:                
                    life = life-attack2[0]
                    life2 = life2+int(attack2[0]/3)
                    myword = "敌人用了招数j,你掉血："+str(attack2[0])+" 你剩余血量为:"+str(life)
                    textColor = GREEN
                    turn = 1
                    # 切换图片和声音
                    enemyPet = petList[6]
                    soundList[2].play()
                    myPet = petList[4]
                elif event.key == pygame.K_k and turn == 2:                
                    life = life-attack2[1]
                    life2 = life2+int(attack2[1]/3)
                    myword = "敌人用了招数k,你掉血："+str(attack2[1])+" 你剩余血量为:"+str(life)
                    textColor = GREEN
                    turn = 1
                    # 切换图片和声音
                    enemyPet = petList[7]
                    soundList[1].play()
                    myPet = petList[4]
                elif event.key == pygame.K_l and turn == 2:                
                    life = life-attack2[2]
                    life2 = life2-int(attack2[2]/3)
                    myword = "敌人用了招数l,你掉血："+str(attack2[2])+" 你剩余血量为:"+str(life)
                    textColor = GREEN
                    turn = 1
                    # 切换图片和声音
                    enemyPet = petList[8]
                    soundList[0].play()
                    myPet = petList[4]
                elif event.key == pygame.K_i and turn == 2:
                    life2 = life2+25
                    enemyPet = petList[5]
                    myword = "敌人用了招数I,敌人加血25,你剩余血量为:"+str(life)
                    textColor = GREEN
                    turn = 1
    
        # 角色移动
        petX = petX + random.randint(-1, 1)
        if petX > 70 or petX < 30:
            petX = 50
        petY = petY + random.randint(-1, 1)
        if petY > 120 or petY < 80:
            petY = 100
        enemyX += random.randint(-1, 1)
        if enemyX > 420 or enemyX < 380:
            enemyX = 400
        enemyY += random.randint(-1, 1)
        if enemyY > 120 or enemyY < 80:
            enemyY = 100
        # 绘制背景和角色
        screen.blit(bgPic, (0, 0))
        screen.blit(myPet, (petX, petY))
        screen.blit(enemyPet, (enemyX, enemyY))
        myText = myFont.render(myword, True, textColor)
        screen.blit(myText, (60, 520))
        #显示血量
        lifeTxt = "血量：" + str(life)
        lifeText = myFont.render(lifeTxt, True, RED)
        screen.blit(lifeText, (30, 30))
        lifeTxt2 = "血量：" + str(life2)
        lifeText2 = myFont.render(lifeTxt2, True, RED)
        screen.blit(lifeText2, (640, 30))
        # 判断胜负
        if life <= 0:
            bgPic1 = pygame.image.load("fail.png")
            screen.blit(bgPic1, (0, 0))
            turn = 3
        elif life2 <= 0:
            bgPic2 = pygame.image.load("win2.png")
            screen.blit(bgPic2, (0, 0))
            turn = 3
        pygame.display.update()
from qrcode import *
print("\033[1;36m            欢迎来到二维码制造机")
x=input("请输入你想在二维码里面储存的文字：")
print("若想查看二维码，请返回桌面查看")
print("若没有看见二维码，请等待一会，此二维码制造机无bug")
print("关掉二维码后执行正经程序")
qr = QRCode()
qr.add_data(x)
img = qr.make_image()
img.show()
while True:
    sd("\033[0m墙裂（强烈）要求给大敏老师！！！！！！！！！！",75)
    sd("""\033[1;36m欢迎来到《口袋妖精大作战》小游戏合集
有以下几个小游戏：
\033[1;33m1.挑战BOSS
2.普通版
3.升级版""",75)
    a = input("选哪个？（输入序号）:")
    sd("""\033[1;32m抵制不良游戏，杜绝盗版游戏
适度游戏健脑，沉迷游戏伤身""",100)
    if a == "1":
        boss()
    if a == "2":
        kou()
    if a == "3":
        kou1()
    else:
        sd("暂时没有此游戏",25)
