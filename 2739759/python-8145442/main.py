#请补充23、28、29、30、31、41行代码。
#小极客们，利用指尖钢琴和 pygame 制作属于你的专属音效琴吧！
#你可以配置你喜欢的音效，还可以修改 pygame 窗口上键盘被敲击的图片效果哦 ~ 
#然后给你喜欢的歌曲，加上音效吧！
#记得拍视频将你的成果分享给其他的小朋友哦！
import mkpiano
import pygame,time,sys,random

pygame.init()    #pygame初始化                       
pygame.display.set_caption("校园小DJ")     #设置窗口名称
screen = pygame.display.set_mode((1200,500))     #设置窗口大小
bg = pygame.image.load("background.png")     #加载背景图
music1 = [0,1]
music2 = [0,2]
music3 = [0,3]
music4 = [0,4]
music5 = [0,5]
music6 = [0,6]
music7 = [0,7]
music8 = [0,8]
#加载音效按键图
b1 = pygame.image.load("button1.png")
b2 = pygame.image.load("button2.png")
b3 = pygame.image.load("button3.png")
b4 = pygame.image.load("button4.png")

###############################################
# 补充或修改以下代码，选择自己喜欢的背景音乐吧
# 还可以修改播放次数和音量呢~
pygame.mixer.music.load("BGM.wav") #加载背景音乐
pygame.mixer.music.play(-1) #播放背景音乐
pygame.mixer.music.set_volume(0.3) # 设置背景音乐音量
###############################################
# 补充或修改以下代码，选择自己喜欢的音效吧
tap1 = pygame.mixer.Sound("1.wav")   #定义音效1
tap2 = pygame.mixer.Sound("2.wav")   #定义音效2
tap3 = pygame.mixer.Sound("3.wav")   #定义音效3
tap4 = pygame.mixer.Sound("4.wav")   #定义音效4
tap5 = pygame.mixer.Sound("5.wav")   #定义音效1
tap6 = pygame.mixer.Sound("6.wav")   #定义音效2
tap7 = pygame.mixer.Sound("7.wav")   #定义音效3
tap8 = pygame.mixer.Sound("8.wav")   #定义音效4
tap9 = pygame.mixer.Sound("9.wav")   #定义音效1
tap10 = pygame.mixer.Sound("10.wav")   #定义音效2
tap11 = pygame.mixer.Sound("11.wav")   #定义音效3
tap12 = pygame.mixer.Sound("12.wav")   #定义音效4
###############################################
list = [[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],]
#————————————————————————————
soundList = ["BGM.wav","帝国进行曲.mp3","Starwars.mp3","Faded.mp3","遇见你的时候所有星星都落到我头上.mp3","黑人抬棺.mp3"]
nameList = ["默认音乐","帝国进行曲","Starwars","Faded","遇见你的时候所有星星都落到我头上","黑人抬棺"]
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
stopRect = pygame.Rect(848, 387, 40, 40)
playRect = pygame.Rect(672, 388, 40, 40)
unpauseRect = pygame.Rect(510, 387, 40, 40)
pauseRect = pygame.Rect(510, 387, 40, 40)
nextRect = pygame.Rect(877, 338, 40, 40)
lastRect = pygame.Rect(479, 338, 40, 40)
screen.blit(bgImg1, (0, 0))
img = bgImg1
img2 = pygame.transform.scale(pygame.image.load("CD.png"),(250,250))
img4 = pygame.transform.scale(pygame.image.load("CD.png"),(250,250))
img2rect = img2.get_rect()
angle= 0
img2rect.center = (700,250)
word1rect = pygame.Rect(1000,300,120,30)
word2rect = pygame.Rect(1000,330,120,30)
state = 1
state2 = 1
state3 = 2
y = 430
volumerect = pygame.Rect(1180,430,20,20)
vrect = pygame.Rect(1188,450,5,50)
vol = 50
y1 = 430
s = pygame.Rect(0,0,400,500)
s2 = pygame.Rect(400,0,800,500)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
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
                elif pauseRect.collidepoint(mPos) and flag == 1:
                    pygame.mixer.music.pause()
                    img = bgImg3
                    flag = 0
                # 继续播放（借助unpause和flag来实现，bgImg4）
                elif unpauseRect.collidepoint(mPos) and flag == 0:
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
                elif pauseRect.collidepoint(mPos) and flag ==0:
                    pygame.mixer.music.pause()
                    img = bgImg3
                    flag = 0
                # 继续播放（借助unpause和flag来实现，bgImg4）
                elif unpauseRect.collidepoint(mPos) and flag ==1:
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
            volumerect.center = (1190,y)
            vrect = pygame.Rect(1188,y,5,y)
            y1 = y
    ###############################################
    # 补充以下代码，当触摸1号琴键时，播放音效1
    if mkpiano.piano.is_touched(1):
        list = [[random.choice(music1),random.choice(music1),random.choice(music1),random.choice(music1),random.choice(music1),random.choice(music1),random.choice(music1),random.choice(music1)],
        [random.choice(music1),random.choice(music1),random.choice(music1),random.choice(music1),random.choice(music1),random.choice(music1),random.choice(music1),random.choice(music1)],
        [random.choice(music1),random.choice(music1),random.choice(music1),random.choice(music1),random.choice(music1),random.choice(music1),random.choice(music1),random.choice(music1)],
        [random.choice(music1),random.choice(music1),random.choice(music1),random.choice(music1),random.choice(music1),random.choice(music1),random.choice(music1),random.choice(music1)],
        [random.choice(music1),random.choice(music1),random.choice(music1),random.choice(music1),random.choice(music1),random.choice(music1),random.choice(music1),random.choice(music1)],
        [random.choice(music1),random.choice(music1),random.choice(music1),random.choice(music1),random.choice(music1),random.choice(music1),random.choice(music1),random.choice(music1)],
        [random.choice(music1),random.choice(music1),random.choice(music1),random.choice(music1),random.choice(music1),random.choice(music1),random.choice(music1),random.choice(music1)],
        [random.choice(music1),random.choice(music1),random.choice(music1),random.choice(music1),random.choice(music1),random.choice(music1),random.choice(music1),random.choice(music1)]]
        colour = (255,0,0)
        key = 1
        tap1 = pygame.mixer.Sound(str(random.randint(1,3))+".wav")
        tap1.play()             
        time.sleep(0.3)
    ###############################################
    if mkpiano.piano.is_touched(2):  #触摸琴键2
        list = [[random.choice(music2),random.choice(music2),random.choice(music2),random.choice(music2),random.choice(music2),random.choice(music2),random.choice(music2),random.choice(music2)],
        [random.choice(music2),random.choice(music2),random.choice(music2),random.choice(music2),random.choice(music2),random.choice(music2),random.choice(music2),random.choice(music2)],
        [random.choice(music2),random.choice(music2),random.choice(music2),random.choice(music2),random.choice(music2),random.choice(music2),random.choice(music2),random.choice(music2)],
        [random.choice(music2),random.choice(music2),random.choice(music2),random.choice(music2),random.choice(music2),random.choice(music2),random.choice(music2),random.choice(music2)],
        [random.choice(music2),random.choice(music2),random.choice(music2),random.choice(music2),random.choice(music2),random.choice(music2),random.choice(music2),random.choice(music2)],
        [random.choice(music2),random.choice(music2),random.choice(music2),random.choice(music2),random.choice(music2),random.choice(music2),random.choice(music2),random.choice(music2)],
        [random.choice(music2),random.choice(music2),random.choice(music2),random.choice(music2),random.choice(music2),random.choice(music2),random.choice(music2),random.choice(music2)],
        [random.choice(music2),random.choice(music2),random.choice(music2),random.choice(music2),random.choice(music2),random.choice(music2),random.choice(music2),random.choice(music2)]]
        colour = (255,170,0)
        key = 2
        tap1 = pygame.mixer.Sound(str(random.randint(4,6))+".wav")
        tap1.play()
        time.sleep(0.3)
    if mkpiano.piano.is_touched(3):  #触摸琴键3
        list = [[random.choice(music3),random.choice(music3),random.choice(music3),random.choice(music3),random.choice(music3),random.choice(music3),random.choice(music3),random.choice(music3)],
        [random.choice(music3),random.choice(music3),random.choice(music3),random.choice(music3),random.choice(music3),random.choice(music3),random.choice(music3),random.choice(music3)],
        [random.choice(music3),random.choice(music3),random.choice(music3),random.choice(music3),random.choice(music3),random.choice(music3),random.choice(music3),random.choice(music3)],
        [random.choice(music3),random.choice(music3),random.choice(music3),random.choice(music3),random.choice(music3),random.choice(music3),random.choice(music3),random.choice(music3)],
        [random.choice(music3),random.choice(music3),random.choice(music3),random.choice(music3),random.choice(music3),random.choice(music3),random.choice(music3),random.choice(music3)],
        [random.choice(music3),random.choice(music3),random.choice(music3),random.choice(music3),random.choice(music3),random.choice(music3),random.choice(music3),random.choice(music3)],
        [random.choice(music3),random.choice(music3),random.choice(music3),random.choice(music3),random.choice(music3),random.choice(music3),random.choice(music3),random.choice(music3)],
        [random.choice(music3),random.choice(music3),random.choice(music3),random.choice(music3),random.choice(music3),random.choice(music3),random.choice(music3),random.choice(music3)]]
        colour = (255,255,0)
        key = 3
        tap1 = pygame.mixer.Sound(str(random.randint(7,9))+".wav")
        tap1.play()
        time.sleep(0.3)
    if mkpiano.piano.is_touched(4):  #触摸琴键4
        list = [[random.choice(music4),random.choice(music4),random.choice(music4),random.choice(music4),random.choice(music4),random.choice(music4),random.choice(music4),random.choice(music4)],
        [random.choice(music4),random.choice(music4),random.choice(music4),random.choice(music4),random.choice(music4),random.choice(music4),random.choice(music4),random.choice(music4)],
        [random.choice(music4),random.choice(music4),random.choice(music4),random.choice(music4),random.choice(music4),random.choice(music4),random.choice(music4),random.choice(music4)],
        [random.choice(music4),random.choice(music4),random.choice(music4),random.choice(music4),random.choice(music4),random.choice(music4),random.choice(music4),random.choice(music4)],
        [random.choice(music4),random.choice(music4),random.choice(music4),random.choice(music4),random.choice(music4),random.choice(music4),random.choice(music4),random.choice(music4)],
        [random.choice(music4),random.choice(music4),random.choice(music4),random.choice(music4),random.choice(music4),random.choice(music4),random.choice(music4),random.choice(music4)],
        [random.choice(music4),random.choice(music4),random.choice(music4),random.choice(music4),random.choice(music4),random.choice(music4),random.choice(music4),random.choice(music4)],
        [random.choice(music4),random.choice(music4),random.choice(music4),random.choice(music4),random.choice(music4),random.choice(music4),random.choice(music4),random.choice(music4)]]
        colour = (0,255,0)
        key = 4
        tap1 = pygame.mixer.Sound(str(random.randint(10,12))+".wav")
        tap1.play()
        time.sleep(0.3)
    for i in range(len(list)):
        for j in range(len(list[i])):
            if list[i][j] == 1:
                color = (0,0,0)
            if list[i][j] == 2:
                color = (100,100,100)
            if list[i][j] == 3:
                color = (255,255,0)
            if list[i][j] == 4:
                color = (255,0,255)
            if list[i][j] == 5:
                color = (0,0,255)
            if list[i][j] == 6:
                color = (0,255,255)
            if list[i][j] == 7:
                color = (150,0,255)
            if list[i][j] == 8:
                color = (255,255,255)
            if list[i][j] == 0:
                color = (255,255,255)
            pygame.draw.rect(screen,(255,255,255),s,0)
            myText1 = myFont.render("动画展示区:",True, (0,0,0))
            screen.blit(myText1, (0,0))
            myText2 = myFont.render("背景音乐调整区",True, (255,255,255))
            screen.blit(myText2, (990,0))
            rect = pygame.Rect(j*50,i*50+100,50,50)
            pygame.draw.rect(screen,color,rect,0)
            pygame.display.update()
    pygame.draw.rect(screen,(0,0,0),s2,0)
    myText = myFont.render("当前背景音乐："+nameList[songNum],True, WHITE)
    screen.blit(myText, (400,0))
    if img == bgImg2:
        screen.blit(img,(401,11))
    else:
        screen.blit(img,(400,0))
    if flag == 1:
        angle = angle+2
    img4 = pygame.transform.rotate(img2,angle)
    img2rect.center = (700,250)
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
    screen.blit(pygame.font.SysFont("kaiti", 20).render("音量"+str(100-y1+400),True, WHITE),(1130,365))
    vol = y1-400
    vol = 100-vol
    vol = vol/100
    pygame.mixer.music.set_volume(vol)
    pygame.display.update()
            