# 我们最喜欢做的事情就是抢红包了！今天我们就来下一场红包雨吧！你准备好了吗？
# 要求：
#     1.通过鼠标事件移动“手”去接红包；
#     2.通过碰撞检测获得红包
#     3.每个红包5积分，计算最终获得积分数。
import pygame, sys, random, time

pygame.init()
t = 0
screen = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("红包雨")
bgImg = pygame.image.load('bg.png')
handImg = pygame.image.load('hand1.png')
hongbaoImg = pygame.image.load('hongbao.png')
gameoverImg = pygame.image.load('gameover.png')
handRect = pygame.Rect(0, 0, 200, 145)
score = 0
hongbaoRectList = []
speed = 5 
num = 0
myWord = "动手接红包，好运连连！"
myFont = pygame.font.SysFont("kaiti", 50)
myText = myFont.render(myWord, True, (0, 0, 255))
for i in range(10):
    x = random.randint(0, 1200)
    y = random.randint(-400, -50)
    hongbaoRect = pygame.Rect(x, y, 80, 80)
    hongbaoRectList.append(hongbaoRect)
screen.blit(bgImg,(0,0))
pygame.mixer.music.load("bgsound.wav")
pygame.mixer.music.play(-1)
t1 = time.time()
pygame.mixer.music.load("bgsound.wav")
pygame.mixer.music.play(-1)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            x = event.pos[0]
            handRect.center = (x,500)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # 在下面书写代码，用鼠标移动事件实现“手图片”跟随鼠标移动
            # 提示:用handRect.center进行中心对齐
        myFont = pygame.font.SysFont("kaiti", 25)
        myText = myFont.render(myWord, True, (0, 0, 255))
        screen.blit(myText, (100, 550))
    screen.blit(bgImg, (0, 0))
    for n in hongbaoRectList:
        # 补全下面代码实现红包下落，速度为speed
        # 当红包到达屏幕底端（y坐标大于600）时，重新随机（random.randint(x,y)）出现在屏幕上方
        # 超出画布范围应设置坐标值为负值，例如（-400，-50）
        if t<20:
            n.x = n.x+4
            n.y = n.y+speed
        if t>20 and t<30:
            n.x = n.x-4
            n.y = n.y+speed
        if t>30 and t<40:
            n.y = n.y+speed
        if t>40 and t<50:
            n.x = n.x+4
            n.y = n.y+speed
        if t>50 and t<60:
            n.x = n.x-4
            n.y = n.y+speed
        if t>60 and t<70:
            n.y = n.y+speed
        if t>70:
            print("\033[1;31m当前钱数:" + str(score))
            pygame.quit()
            sys.exit()
        if n.y >600 or n.x>1200 or n.x<0:
            n.x = random.randint(0,1200)
            n.y = -150
        # 补全49-51行代码，当手handRect接触红包时，积分score加5，红包重新下落
        if n.colliderect(handRect):
            n.x = random.randint(100,1100)
            n.y = -150
            score = score+5
            myWord = "成功收集一个红包，获得5元。当前钱数:" + str(score)
        screen.blit(hongbaoImg, n)
    screen.blit(handImg, handRect)
    myText = myFont.render(myWord, True, (0,0,255))
    screen.blit(myText, (100, 550))
    t2 = time.time()
    t = t2-t1
    pygame.display.update()