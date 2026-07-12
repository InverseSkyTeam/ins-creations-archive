'''
自制打碟机！！！！添加喜爱的音乐和图片，完成
专属的打碟机！可以自己增加进度条哦
提示：利用drawRect来调整按钮对应的Rect对象的坐标
当然也可以print(pos)来确定Rect的坐标哦
'''
import pygame, sys,random
pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("音乐播放器")
soundList = ["下山.mp3","Faded.mp3","芒种.mp3","遇见你的时候所有星星都落到我头上.mp3","绿色.mp3","惊雷.mp3","火红的萨日朗.mp3","buttercup.mp3","fire.mp3","handclap.mp3","su.mp3"]
nameList = ["下山","Faded","芒种","遇见你的时候所有星星都落到我头上","绿色","惊雷","火红的萨日朗","buttercup","fire","handclap","su"]
songNum = 0
sound = pygame.mixer.music.load(soundList[songNum])
#添加自己喜欢的图片，可以从左侧列表选择也可以自己添加哦
bgImg1 = pygame.image.load("normal.png")
bgImg2 = pygame.image.load("last.png")
bgImg3 = pygame.image.load("pause.png")
bgImg4 = pygame.image.load("unpause.png")
bgImg5 = pygame.image.load("play.png")
bgImg6 = pygame.image.load("stop.png")
bgImg7 = pygame.image.load("next.png")
# Windows电脑使用"kaiti"，苹果用"kaittf"
myFont = pygame.font.SysFont("kaiti", 30) 
WHITE = (255, 255, 255)
myText = myFont.render(nameList[songNum], True, WHITE)
flag = 0  # 当前是播放状态，播放后1代表正在播放，0正在暂停
# 定义按键矩形区域
stopRect = pygame.Rect(448, 387, 40, 40)
playRect = pygame.Rect(272, 388, 40, 40)
unpauseRect = pygame.Rect(110, 387, 40, 40)
pauseRect = pygame.Rect(110, 387, 40, 40)
nextRect = pygame.Rect(477, 338, 40, 40)
lastRect = pygame.Rect(79, 338, 40, 40)
screen.blit(bgImg1, (0, 0))
img = bgImg1
img2 = pygame.transform.scale(pygame.image.load("CD.png"),(250,250))
img4 = pygame.transform.scale(pygame.image.load("CD.png"),(250,250))
img2rect = img2.get_rect()
angle= 0
img2rect.center = (300,250)
word1rect = pygame.Rect(600,300,120,30)
word2rect = pygame.Rect(600,330,120,30)
state = 1
state2 = 1
state3 = 2
y = 430
volumerect = pygame.Rect(780,430,20,20)
vrect = pygame.Rect(788,450,5,50)
vol = 50
y1 = 430
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mPos = event.pos
            if word1rect.collidepoint(mPos):
                state = 1
            if word2rect.collidepoint(mPos):
                state = 2
        if state == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mPos = event.pos
            # 播放
                if playRect.collidepoint(mPos):
                    pygame.mixer.music.play()
                    img = bgImg5
                    flag = 1
                # 停止播放（停止是stop，bgImg6）
                elif stopRect.collidepoint(mPos):
                    pygame.mixer.music.stop()
                    img = bgImg6
                    flag = 0
                # 暂停（暂停是pause，借助flag实现哦，bgImg3）
                elif pauseRect.collidepoint(mPos) and flag ==1:
                    pygame.mixer.music.pause()
                    img = bgImg3
                    flag = 0
                # 继续播放（借助unpause和flag来实现，bgImg4）
                elif unpauseRect.collidepoint(mPos) and flag ==0:
                    pygame.mixer.music.unpause()
                    img = bgImg4
                    flag = 1
                # 下一曲，bgImg7
                elif nextRect.collidepoint(mPos):
                    songNum = songNum + 1
                    if songNum > len(soundList) - 1:
                         songNum = 0
                    sound = pygame.mixer.music.load(soundList[songNum])
                    pygame.mixer.music.play()
                    img = bgImg7
                    flag = 1
                 # 上一曲（注意soundList的索引范围哦，bgImg2）
                elif lastRect.collidepoint(mPos):
                    songNum = songNum - 1
                    if songNum < 0:
                         songNum = len(soundList) - 1
                    sound = pygame.mixer.music.load(soundList[songNum])
                    pygame.mixer.music.play()
                    img = bgImg2
                    flag = 1
        if state ==2:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mPos = event.pos
            # 播放
                if playRect.collidepoint(mPos):
                    pygame.mixer.music.play()
                    img = bgImg5
                    flag = 1
                # 停止播放（停止是stop，bgImg6）
                elif stopRect.collidepoint(mPos):
                    pygame.mixer.music.stop()
                    img = bgImg6
                    flag = 0
                # 暂停（暂停是pause，借助flag实现哦，bgImg3）
                elif pauseRect.collidepoint(mPos) and flag ==1:
                    pygame.mixer.music.pause()
                    img = bgImg3
                    flag = 0
                # 继续播放（借助unpause和flag来实现，bgImg4）
                elif unpauseRect.collidepoint(mPos) and flag ==0:
                    pygame.mixer.music.unpause()
                    img = bgImg4
                    flag = 1
                # 下一曲，bgImg7
                elif nextRect.collidepoint(mPos):
                    songNum = random.randint(0,len(soundList) - 1)
                    sound = pygame.mixer.music.load(soundList[songNum])
                    pygame.mixer.music.play()
                    img = bgImg7
                    flag = 1
                 # 上一曲（注意soundList的索引范围哦，bgImg2）
                elif lastRect.collidepoint(mPos):
                    songNum = random.randint(0,len(soundList) - 1)
                    sound = pygame.mixer.music.load(soundList[songNum])
                    pygame.mixer.music.play()
                    img = bgImg2
                    flag = 1
        if event.type == pygame.MOUSEMOTION:
            if event.pos[1] > 400 and event.pos[1] < 500:
                y = event.pos[1]
        if event.type == pygame.MOUSEBUTTONDOWN:
            mPos = event.pos
            if volumerect.collidepoint(event.pos):
                state2 = 0
        if event.type == pygame.MOUSEBUTTONUP:
            state2 = 1
        if state2 == 0:
            volumerect.center = (790,y)
            vrect = pygame.Rect(788,y,5,y)
            y1 = y
    screen.fill((0,0,0))
    myText = myFont.render("当前音乐："+nameList[songNum],True, WHITE)
    screen.blit(myText, (0,0))
    if img == bgImg2:
        screen.blit(img,(1,11))
    else:
        screen.blit(img,(0,0))
    if flag == 1:
        angle = angle+2
    img4 = pygame.transform.rotate(img2,angle)
    img2rect.center = (300,250)
    img4rect = img4.get_rect(center = img2rect.center)
    screen.blit(img4,img4rect)
    if state == 1:
        pygame.draw.rect(screen,(255,0,0),word1rect,0)
    if state == 2:
        pygame.draw.rect(screen,(255,0,0),word2rect,0)
    screen.blit(myFont.render("顺序播放",True, WHITE),word1rect)
    screen.blit(myFont.render("随机播放",True, WHITE),word2rect)
    pygame.draw.rect(screen,(255,255,255),word1rect,1)
    pygame.draw.rect(screen,(255,255,255),word2rect,1)
    pygame.draw.rect(screen,(255,150,0),vrect,0)
    pygame.draw.ellipse(screen,(255,255,255),volumerect,0)
    screen.blit(pygame.font.SysFont("kaiti", 20).render("音量"+str(100-y1+400),True, WHITE),(730,365))
    vol = y1-400
    vol = 100-vol
    vol = vol/100
    pygame.mixer.music.set_volume(vol)
    pygame.display.update()