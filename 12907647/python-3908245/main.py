import pygame,sys,random #导库
from time import *
#初始化
pygame.init()
screen = pygame.display.set_mode((600, 1000))
pygame.display.set_caption("long")
#字母列表
letterList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
letterWait = []
#定义一些变量
score = 0
chance = 5
letterSpeed = 1
level = 1
clickNum = 0
ax = 80
rate = 0
wrong = 0
BLUE_T = (0,0,255)
GREEN_T = (0,255,0)
RED_T = (255,0,0)
scoreShow = ''
rateShow = ''
myFont1 = pygame.font.SysFont('stxihei',80)
myFont2 = pygame.font.SysFont('kaiti',15)
#计时器
t1 = time()
t3 = time()
#主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and len(letterWait) > 0:
            clickNum += 1
            for letter in letterWait:
                if event.key == ord(letter['word']):
                    letterWait.remove(letter)
                    score += 1
                    pygame.display.update()
                    break
                else:
                    score -= 3
                    letterSpeed -= 0.3
                    pygame.display.update()
                    break
    t2 = time() #计时器
    t4 = time()
    if t2 > t1 + 1:
        t1 = t2
        L1 = random.choice(letterList)
        C1 = (random.randint(0,255),random.randint(0,255),random.randint(0,150))
        X1 = random.randint(50,550)
        Y1 = -5
        letterDict = {'word':L1,'color':C1,'x':X1,'y':Y1}
        letterWait.append(letterDict)
    
    if int((t4-t3)%10) == 0 and int(t4-t3) != 0:
        ax += 10
        myFont1 = pygame.font.SysFont('stxihei',ax)
        print('真厉害！又坚持了10秒！')
        letterSpeed += 1
        sleep(1)
        
    if score <= -20:
        print('不会吧，你也太……垃圾了！')
        sleep(0.4)
        pygame.quit()
        sys.exit()
        
    if letterSpeed < 1:
        letterSpeed = 1
        
    for i in range(len(letterWait)):
        letterWait[i]['y'] += letterSpeed
        sleep(0.01)
        if letterWait[i]['y'] > 1000:
            chance -= 1
            letterSpeed -= 1
            letterWait.remove(letterWait[i])
            break
    #计分及退出
    if score % 10 == 0:
        level = int(score/10)+1
        letterSpeed = level
    pygame.display.update()
    if chance <= 0:
        chanceShow = myFont2.render('机会用完，886！最终得分：' + str(score),1,RED_T)
        screen.blit(chanceShow,(200,400))
        print('机会用完，886！最终得分：' + str(score))
        sleep(2)
        pygame.quit()
        sys.exit()
    #背景
    screen.fill((255,255,255))
    #绘制
    for i in range(len(letterWait)):   
        X2 = letterWait[i]['x']
        Y2 = letterWait[i]['y']
        L2 = letterWait[i]['word']
        C2 = letterWait[i]['color']
        TextImage_to_While = myFont1.render(L2,1,C2)
        screen.blit(TextImage_to_While,(X2,Y2))
    #显示
    chanceT = '剩余机会：' + str(chance)
    chanceShow = myFont2.render(chanceT,1,BLUE_T)
    screen.blit(chanceShow,(0,0))
    if clickNum > 0:
        rate = score/clickNum
        rateRound_asd = round(rate * 100,2)
        rateT = '正确率：' + str(rateRound_asd) + '%'
        rateShow = myFont2.render(rateT,1,GREEN_T)
        screen.blit(rateShow,(0,20))
    scoreT = '分数：' + str(score)
    scoreShow = myFont2.render(scoreT,1,RED_T)
    screen.blit(scoreShow,(0,40))
    levelT = '等级：' + str(level)
    levelShow = myFont2.render(levelT,1,BLUE_T)
    screen.blit(levelShow,(0,60))
    pygame.display.update()