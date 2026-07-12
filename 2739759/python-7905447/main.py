#请补充26、61、72行代码。
# "海底两万里"：请编写程序
#用指尖钢琴控制潜艇在深海中完成打捞沉船的任务
#注意要躲避危险的鲨鱼哦！

import mkpiano
import pygame,sys,time,random
print("摇杆控制方向，两个按钮中左边的发射子弹，给大米")
pygame.time.delay(3000)#大米，单位是毫秒
pygame.init()
#设置窗口大小
screen = pygame.display.set_mode((500,790))
#设置窗口标题
pygame.display.set_caption("攻击死星")

#加载音效
pygame.mixer.music.load("Starwars.mp3") # 背景音乐
pygame.mixer.music.play(-1)
win = pygame.mixer.Sound("success.wav") # 顺利抵达飞艇音效
lose = pygame.mixer.Sound("fail.wav") # 失败音效

#加载海底图片
background = pygame.image.load("stars.png")
background = pygame.transform.scale(background,(500,790))
####################################################
#补充代码，加载潜艇的图片，潜艇的图片名字是 ship.png
ship = pygame.image.load("千年隼.png")
ship = pygame.transform.scale(ship,(150,60))
####################################################

#加载沉船的图片
boat = pygame.image.load("死星.png")
boat = pygame.transform.scale(boat,(100,100))
#加载鲨鱼图片
shark1 = pygame.image.load("星球大战钛战机.png")
shark1 = pygame.transform.scale(shark1,(111,70))
shark2 = pygame.image.load("星球大战钛战机.png")
shark2 = pygame.transform.scale(shark2,(111,70))
bullet = pygame.image.load("子弹2.png")
bullet = pygame.transform.scale(bullet,(50,18))
bullet = pygame.transform.rotate(bullet,90)
#定义潜艇初始坐标
shipX = 300
shipY = 50

#定义鲨鱼初始坐标
shark1X = 450
shark1Y = random.randint(250,790)

shark2X = 0
shark2Y = random.randint(250,790)

bX = shipX+75
bY = shipY
t1 = time.time()

#设置字体和字号，window电脑是kaiti，苹果电脑字体是kaittf
myFont  = pygame.font.SysFont("kaiti",30)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    if mkpiano.piano.is_joystick_left():
        shipX = shipX - 3
        
    ###################################
    #补充代码，控制飞艇向右移动
    if mkpiano.piano.is_joystick_right():
        shipX = shipX + 3
    ###################################
    
    if mkpiano.piano.is_joystick_up():
        shipY = shipY - 3
    if mkpiano.piano.is_joystick_down():
        shipY = shipY + 3
        
    ############################################
    #补充代码，让鲨鱼1向左移动，向左移动x坐标减小    
    shark1X = shark1X - 2
    ############################################
    
    if shark1X < 0:
        shark1X = 450
        shark1Y = random.randint(0,790)
    
    #让鲨鱼2的x坐标增加（向右移动）    
    shark2X = shark2X + 2
    if shark2X > 450:
        shark2X = 0
        shark2Y = random.randint(0,790)
    bY = bY + 3
    if bY > 790 or mkpiano.piano.is_pressed(1):
        bX = shipX+75
        bY = shipY+50
    
    #设置图片相对应的矩形对象
    s = pygame.Rect(shipX, shipY,150,60)
    b = pygame.Rect(200,690,100,100)
    s1 = pygame.Rect(shark1X, shark1Y,150,75)
    s2 = pygame.Rect(shark2X, shark2Y,150,75)
    br = pygame.Rect(bX,bY,18,50)
    
    #刷新背景
    screen.blit(background, (0, 0))
    #刷新潜艇位置
    screen.blit(ship,s)
    #刷新沉船位置
    screen.blit(boat,b)
    #刷新鲨鱼位置
    screen.blit(shark1,s1)
    screen.blit(shark2,s2)
    screen.blit(bullet,br)
    if br.colliderect(s1):
        shark1X = 0
        shark1Y = random.randint(0,500)
    
    if br.colliderect(s2):
        shark2X = 450
        shark2Y = random.randint(0,500)
    if s.colliderect(b):
        t2 = time.time()
        t = t2 - t1
        t = int(t)
        win.play()
        myText = myFont.render("你用了 "+str(t)+" 秒顺利摧毁死星！",True, (255,0,0))
        screen.blit(myText,(0,50))
        pygame.display.update()
        time.sleep(1)
        pygame.quit()
        sys.exit()
        
    if s.colliderect(s1) or s.colliderect(s2):
        lose.play()
        myText = myFont.render("千年隼碰到钛战机，游戏结束！",True, (255,0,0))
        screen.blit(myText,(0,50))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    
    if shipX > 350 or shipX <0 or shipY > 730 or shipY < 0:
        lose.play()
        myText = myFont.render("千年隼碰壁，游戏结束！",True, (255,0,0))
        screen.blit(myText,(0,50))
        pygame.display.update() 
        time.sleep(2)
        pygame.quit()
        sys.exit()
        
    pygame.display.update()
    time.sleep(0.01)