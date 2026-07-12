import pygame,sys,random,os,datetime,re,wx;from time import *
pygame.init()

print('游戏：大鱼吃小鱼小轩A字版。')
sleep(0.5)
print('游戏背景：')
print('你是一条爱探险、粉色的小鱼(坐着只找到这种颜色，他并不喜欢)，来到一条"和谐海"，这里的大鱼不吃小鱼，靠神秘器官生活。')
print('但，\n你要吃它们，\n否则无法生存。')
sleep(0.5)
print('刚开始，只能吃最小的小鱼，当你足够大时，能吃中鱼，更大时能吃大鱼。')
print('当你碰到石头时，会死亡(以后关卡有石头)\n如碰到比你大的鱼，也死亡。')
print('点开始后，赶紧把鼠标移到左上角，用鼠标控制移动。输了自动重来。')
sleep(0.5)
print('通关要求：\n吃了所有小鱼。')
sleep(0.5)
print('疑难解答：为什么程序响应不了？')
sleep(0.5)
print('不是你的问题，\033[1;31m开始时 或 在商店买东西、登录时，\033[0m如不响应，请点一下终端（右边黑色的部分→_→）。')
print('然后程序自动会最小化，先回答终端的问题（只要输入），共2个问题。')
print("回答完后程序设置为响应，那时你只要点击窗口让它出现就能开始——了！Let's go！")
sleep(1)
input('看完才能回车，否则你会后悔。')
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("大鱼吃小鱼小轩A字版")

xi_tong = input('输入你的系统：Windos或XP选1，Mac、iPhone、Mac Pro、Apple或其他选2')
hero_size = 70
guan = 0
part = 1
VIP = 0
cl1 = 0
hero_x = -300
hero_y = -300
GoldQins = 0
while True:
    if xi_tong == '1':
        myFont = pygame.font.SysFont("kaiti", 40)
        myFont2 = pygame.font.SysFont("kaiti", 20)
        break
    elif xi_tong == '2':
        myFont = pygame.font.SysFont("kaittf", 40)
        myFont2 = pygame.font.SysFont("kaittf", 20)
        break
    else:
        print('输入错误！')
        sleep(1)
        xi_tong = input('输入你的系统：Windos或XP选1    ，   Mac、iPhone、Mac Pro、Apple或其他选2')
RED = (255,0,0)
BLACK = (0,0,0)
GREEN = (0,255,0)
myText = myFont.render("大鱼吃小鱼小轩A字版", 1, BLACK)

heroImg = pygame.image.load("鱼hero.png")
heroImgs = pygame.transform.scale(heroImg, (hero_size, hero_size))


smallImg = pygame.image.load("小鱼.png")
smallImgs = pygame.transform.scale(smallImg, (50, 50))


middleImg = pygame.image.load("中鱼.png")
middleImgs = pygame.transform.scale(middleImg, (140, 140))


bigImg = pygame.image.load("大鱼.png")
bigImgs = pygame.transform.scale(bigImg, (180, 180))


getshangImg = pygame.image.load("商店.png")
getshangImgs = pygame.transform.scale(getshangImg, (125, 125))
getshangRect = pygame.Rect(375, 400, 125, 125)


startImg = pygame.image.load("START1.png")
startImgs = pygame.transform.scale(startImg, (180, 65))
startRect = pygame.Rect(550, 400, 180, 65)


dlImg = pygame.image.load("登录.png")
dlImgs = pygame.transform.scale(dlImg, (180, 65))
dlRect = pygame.Rect(550, 300, 180, 65)


fanhuiImg = pygame.image.load("返回.png")
fanhuiImgs = pygame.transform.scale(fanhuiImg, (100, 30))
fanhuiRect = pygame.Rect(0, 0, 180, 65)


while True:
    QA_line_lentofun_Music_AisJhxopen = input('再输入你要的音乐：1是 芒种    ，   其他是 Monsters。')
    if QA_line_lentofun_Music_AisJhxopen == '1':
        pygame.mixer.music.load('芒种.mp3')
        pygame.mixer.music.play(-1)
        break
    else:
        pygame.mixer.music.load('monsters.mp3')
        pygame.mixer.music.play(-1)
        break

while True:
    while part == 1:
        wg = 0
        wgsm = 1
        guan = 0
        while guan == wg:
            if cl1 == 0:
                Kword = '大鱼吃小鱼小轩A字版'
            elif cl1 == 1:
                Kword = '请再来试试！！！'
            elif cl1 == 2:
                Kword = '主页'
            myWord = Kword
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if startRect.collidepoint(event.pos):
                        sleep(1)
                        guan = wgsm
                    elif getshangRect.collidepoint(event.pos):
                        print('商店加载中……')
                        sleep(1)
                        print('打开。')
                        part = 2
                        guan = 100
                    elif dlRect.collidepoint(event.pos):
                        password = input('请设置你的密码。(输入r退出)')
                        if password == 'r':
                            print('退出完毕！')
                            del password
                            break
                        password2 = input('请设置你的备用密码。')
                        print('好的，正在检测你的本机用户名……')
                        sleep(1.5)
                        yonghu = str(wx)[30:len(str(wx))-70]
                        print('爬取成功！是',yonghu)
                        FackName = input('请设置昵称：')
                        print('登录成功！')
                        break
                        
            myText = myFont.render(myWord, 1, BLACK)
            screen.fill((0,230,0))
            screen.blit(startImgs,startRect)
            screen.blit(getshangImgs,getshangRect)
            screen.blit(dlImgs,dlRect)
            screen.blit(myText,(425,40))
            pygame.display.update()
            
        hero_size = 70
        SW = 50
        MW = 5
        BW = 2
        Kword = '第一关'
        wg = 1
        wgsm = 2
        wen = 1
        smallList = []
        middleList = []
        bigList = []
        
        for i in range(SW):
            smallRect = pygame.Rect(random.randint(100, 1100), random.randint(50, 750), 50, 50)
            smallList.append(smallRect)
        for i in range(MW):
            middleRect = pygame.Rect(random.randint(100, 1100), random.randint(50, 750), 140, 140)
            middleList.append(middleRect)
        for i in range(BW):
            bigRect = pygame.Rect(random.randint(100, 1100), random.randint(50, 750), 180, 180)
            bigList.append(bigRect)
        
        myWord = Kword
    
        while guan == wg:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEMOTION:
                    hero_x = event.pos[0] - hero_size/2
                    hero_y = event.pos[1] - hero_size/2
            heroRect = pygame.Rect(hero_x, hero_y, hero_size, hero_size)
            for n in smallList:
                n.x += random.randint(-1,3)
                if n.top < 0:
                    n.top = 0
                if n.bottom > 800:
                    n.bottom = 800
                if n.left < 0:
                    n.left = 0
                if n.right > 1200:
                    n.right = 0
                if heroRect.colliderect(n):    
                    smallList.remove(n)
                    print("吃掉了！")
                    GoldQins += 1
                    hero_size += 5
                    heroImgs = pygame.transform.scale(heroImg, (hero_size, hero_size))
                    if smallList == []:
                        print('胜利！')
                        myWord = '胜利！'
                        sleep(1)
                        guan = wgsm
                        part = wen
            for i in middleList:
                i.x += random.randint(-1,2)
                if i.top < 0:
                    i.top = 0
                if i.bottom > 800:
                    i.bottom = 800
                if i.left < 0:
                    i.left = 0
                if i.right > 1200:
                    i.right = 0
                if heroRect.colliderect(i):
                    if hero_size*hero_size >= 140*140:
                        middleList.remove(i)
                        print("吃掉了！")
                        GoldQins += 1
                        hero_size += 12
                        heroImgs = pygame.transform.scale(heroImg, (hero_size, hero_size))
                    elif hero_size*hero_size < 140*140:
                        print("KO！")
                        myWord = 'KO!'
                        sleep(1)
                        cl1 = 1
                        guan = 0
            for x in bigList:
                x.x += random.randint(-1,1)
                if x.top < 0:
                    x.top = 0
                if x.bottom > 800:
                    x.bottom = 800
                if x.left < 0:
                    x.left = 0
                if x.right > 1200:
                    x.right = 0
                if heroRect.colliderect(x):
                    if hero_size*hero_size >= 180*180:
                        bigList.remove(x)
                        print("吃掉了！")
                        GoldQins += 1
                        hero_size += 40
                        heroImgs = pygame.transform.scale(heroImg, (hero_size, hero_size))
                    elif hero_size*hero_size < 180*180:
                        print("KO！")
                        myWord = 'KO!'
                        sleep(1)
                        cl1 = 1
                        guan = 0
            screen.fill((0, 100, 250))
            screen.blit(heroImgs, heroRect)
            for rects in smallList:
                screen.blit(smallImgs, rects)
            for rectm in middleList:
                screen.blit(middleImgs, rectm)
            for rectb in bigList:
                screen.blit(bigImgs, rectb)
            myText = myFont.render(myWord, 1, GREEN)
            screen.blit(myText,(570,40))
            pygame.display.update()
        
        hero_size = 70
        SW = 100
        MW = 10
        BW = 3
        Kword = '第二关'
        wg = 2
        wgsm = 3
        wen = 1
        smallList = []
        middleList = []
        bigList = []
        
        for i in range(SW):
            smallRect = pygame.Rect(random.randint(100, 1100), random.randint(50, 750), 50, 50)
            smallList.append(smallRect)
        for i in range(MW):
            middleRect = pygame.Rect(random.randint(100, 1100), random.randint(50, 750), 140, 140)
            middleList.append(middleRect)
        for i in range(BW):
            bigRect = pygame.Rect(random.randint(100, 1100), random.randint(50, 750), 180, 180)
            bigList.append(bigRect)
        
        myWord = Kword
    
        while guan == wg:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEMOTION:
                    hero_x = event.pos[0] - hero_size/2
                    hero_y = event.pos[1] - hero_size/2
            heroRect = pygame.Rect(hero_x, hero_y, hero_size, hero_size)
            for n in smallList:
                n.x += random.randint(-1,3)
                if n.top < 0:
                    n.top = 0
                if n.bottom > 800:
                    n.bottom = 800
                if n.left < 0:
                    n.left = 0
                if n.right > 1200:
                    n.right = 0
                if heroRect.colliderect(n):    
                    smallList.remove(n)
                    print("吃掉了！")
                    GoldQins += 1
                    hero_size += 5
                    heroImgs = pygame.transform.scale(heroImg, (hero_size, hero_size))
                    if smallList == []:
                        print('胜利！')
                        myWord = '胜利！'
                        sleep(1)
                        guan = wgsm
                        part = wen
            for i in middleList:
                i.x += random.randint(-1,2)
                if i.top < 0:
                    i.top = 0
                if i.bottom > 800:
                    i.bottom = 800
                if i.left < 0:
                    i.left = 0
                if i.right > 1200:
                    i.right = 0
                if heroRect.colliderect(i):
                    if hero_size*hero_size >= 140*140:
                        middleList.remove(i)
                        print("吃掉了！")
                        GoldQins += 1
                        hero_size += 12
                        heroImgs = pygame.transform.scale(heroImg, (hero_size, hero_size))
                    elif hero_size*hero_size < 140*140:
                        print("KO！")
                        myWord = 'KO!'
                        sleep(1)
                        cl1 = 1
                        guan = 0
            for x in bigList:
                x.x += random.randint(-1,1)
                if x.top < 0:
                    x.top = 0
                if x.bottom > 800:
                    x.bottom = 800
                if x.left < 0:
                    x.left = 0
                if x.right > 1200:
                    x.right = 0
                if heroRect.colliderect(x):
                    if hero_size*hero_size >= 180*180:
                        bigList.remove(x)
                        print("吃掉了！")
                        GoldQins += 1
                        hero_size += 40
                        heroImgs = pygame.transform.scale(heroImg, (hero_size, hero_size))
                    elif hero_size*hero_size < 180*180:
                        print("KO！")
                        myWord = 'KO!'
                        sleep(1)
                        cl1 = 1
                        guan = 0
            screen.fill((0, 100, 250))
            screen.blit(heroImgs, heroRect)
            for rects in smallList:
                screen.blit(smallImgs, rects)
            for rectm in middleList:
                screen.blit(middleImgs, rectm)
            for rectb in bigList:
                screen.blit(bigImgs, rectb)
            myText = myFont.render(myWord, 1, GREEN)
            screen.blit(myText,(570,40))
            pygame.display.update()
        
        hero_size = 70
        SW = 80
        MW = 5
        BW = 5
        Kword = '第三关'
        wg = 3
        wgsm = 4
        wen = 1
        smallList = []
        middleList = []
        bigList = []
        
        for i in range(SW):
            smallRect = pygame.Rect(random.randint(100, 1100), random.randint(50, 750), 50, 50)
            smallList.append(smallRect)
        for i in range(MW):
            middleRect = pygame.Rect(random.randint(100, 1100), random.randint(50, 750), 140, 140)
            middleList.append(middleRect)
        for i in range(BW):
            bigRect = pygame.Rect(random.randint(100, 1100), random.randint(50, 750), 180, 180)
            bigList.append(bigRect)
        
        myWord = Kword
    
        while guan == wg:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEMOTION:
                    hero_x = event.pos[0] - hero_size/2
                    hero_y = event.pos[1] - hero_size/2
            heroRect = pygame.Rect(hero_x, hero_y, hero_size, hero_size)
            for n in smallList:
                n.x += random.randint(-1,3)
                if n.top < 0:
                    n.top = 0
                if n.bottom > 800:
                    n.bottom = 800
                if n.left < 0:
                    n.left = 0
                if n.right > 1200:
                    n.right = 0
                if heroRect.colliderect(n):    
                    smallList.remove(n)
                    print("吃掉了！")
                    GoldQins += 1
                    hero_size += 5
                    heroImgs = pygame.transform.scale(heroImg, (hero_size, hero_size))
                    if smallList == []:
                        print('胜利！')
                        myWord = '胜利！'
                        sleep(1)
                        guan = wgsm
                        part = wen
            for i in middleList:
                i.x += random.randint(-1,2)
                if i.top < 0:
                    i.top = 0
                if i.bottom > 800:
                    i.bottom = 800
                if i.left < 0:
                    i.left = 0
                if i.right > 1200:
                    i.right = 0
                if heroRect.colliderect(i):
                    if hero_size*hero_size >= 140*140:
                        middleList.remove(i)
                        print("吃掉了！")
                        GoldQins += 1
                        hero_size += 12
                        heroImgs = pygame.transform.scale(heroImg, (hero_size, hero_size))
                    elif hero_size*hero_size < 140*140:
                        print("KO！")
                        myWord = 'KO!'
                        sleep(1)
                        cl1 = 1
                        guan = 0
            for x in bigList:
                x.x += random.randint(-1,1)
                if x.top < 0:
                    x.top = 0
                if x.bottom > 800:
                    x.bottom = 800
                if x.left < 0:
                    x.left = 0
                if x.right > 1200:
                    x.right = 0
                if heroRect.colliderect(x):
                    if hero_size*hero_size >= 180*180:
                        bigList.remove(x)
                        print("吃掉了！")
                        GoldQins += 1
                        hero_size += 40
                        heroImgs = pygame.transform.scale(heroImg, (hero_size, hero_size))
                    elif hero_size*hero_size < 180*180:
                        print("KO！")
                        myWord = 'KO!'
                        sleep(1)
                        cl1 = 1
                        guan = 0
            screen.fill((0, 100, 250))
            screen.blit(heroImgs, heroRect)
            for rects in smallList:
                screen.blit(smallImgs, rects)
            for rectm in middleList:
                screen.blit(middleImgs, rectm)
            for rectb in bigList:
                screen.blit(bigImgs, rectb)
            myText = myFont.render(myWord, 1, GREEN)
            screen.blit(myText,(570,40))
            pygame.display.update()
        
        hero_size = 70
        SW = 80
        MW = 10
        BW = 5
        Kword = '第四关'
        wg = 4
        wgsm = 5
        wen = 1
        smallList = []
        middleList = []
        bigList = []
        
        for i in range(SW):
            smallRect = pygame.Rect(random.randint(100, 1100), random.randint(50, 750), 50, 50)
            smallList.append(smallRect)
        for i in range(MW):
            middleRect = pygame.Rect(random.randint(100, 1100), random.randint(50, 750), 140, 140)
            middleList.append(middleRect)
        for i in range(BW):
            bigRect = pygame.Rect(random.randint(100, 1100), random.randint(50, 750), 180, 180)
            bigList.append(bigRect)
        
        myWord = Kword
    
        while guan == wg:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEMOTION:
                    hero_x = event.pos[0] - hero_size/2
                    hero_y = event.pos[1] - hero_size/2
            heroRect = pygame.Rect(hero_x, hero_y, hero_size, hero_size)
            for n in smallList:
                n.x += random.randint(-1,3)
                if n.top < 0:
                    n.top = 0
                if n.bottom > 800:
                    n.bottom = 800
                if n.left < 0:
                    n.left = 0
                if n.right > 1200:
                    n.right = 0
                if heroRect.colliderect(n):    
                    smallList.remove(n)
                    print("吃掉了！")
                    GoldQins += 1
                    hero_size += 5
                    heroImgs = pygame.transform.scale(heroImg, (hero_size, hero_size))
                    if smallList == []:
                        print('胜利！')
                        myWord = '胜利！'
                        sleep(1)
                        guan = wgsm
                        part = wen
            for i in middleList:
                i.x += random.randint(-1,2)
                if i.top < 0:
                    i.top = 0
                if i.bottom > 800:
                    i.bottom = 800
                if i.left < 0:
                    i.left = 0
                if i.right > 1200:
                    i.right = 0
                if heroRect.colliderect(i):
                    if hero_size*hero_size >= 140*140:
                        middleList.remove(i)
                        print("吃掉了！")
                        GoldQins += 1
                        hero_size += 12
                        heroImgs = pygame.transform.scale(heroImg, (hero_size, hero_size))
                    elif hero_size*hero_size < 140*140:
                        print("KO！")
                        myWord = 'KO!'
                        sleep(1)
                        cl1 = 1
                        guan = 0
            for x in bigList:
                x.x += random.randint(-1,1)
                if x.top < 0:
                    x.top = 0
                if x.bottom > 800:
                    x.bottom = 800
                if x.left < 0:
                    x.left = 0
                if x.right > 1200:
                    x.right = 0
                if heroRect.colliderect(x):
                    if hero_size*hero_size >= 180*180:
                        bigList.remove(x)
                        print("吃掉了！")
                        GoldQins += 1
                        hero_size += 40
                        heroImgs = pygame.transform.scale(heroImg, (hero_size, hero_size))
                    elif hero_size*hero_size < 180*180:
                        print("KO！")
                        myWord = 'KO!'
                        sleep(1)
                        cl1 = 1
                        guan = 0
            screen.fill((0, 100, 250))
            screen.blit(heroImgs, heroRect)
            for rects in smallList:
                screen.blit(smallImgs, rects)
            for rectm in middleList:
                screen.blit(middleImgs, rectm)
            for rectb in bigList:
                screen.blit(bigImgs, rectb)
            myText = myFont.render(myWord, 1, GREEN)
            screen.blit(myText,(570,40))
            pygame.display.update()
        
        hero_size = 70
        SW = 100
        MW = 20
        BW = 10
        Kword = '第五关'
        wg = 5
        wgsm = 0
        wen = 1
        smallList = []
        middleList = []
        bigList = []
        
        for i in range(SW):
            smallRect = pygame.Rect(random.randint(100, 1100), random.randint(50, 750), 50, 50)
            smallList.append(smallRect)
        for i in range(MW):
            middleRect = pygame.Rect(random.randint(100, 1100), random.randint(50, 750), 140, 140)
            middleList.append(middleRect)
        for i in range(BW):
            bigRect = pygame.Rect(random.randint(100, 1100), random.randint(50, 750), 180, 180)
            bigList.append(bigRect)
        
        myWord = Kword
    
        while guan == wg:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEMOTION:
                    hero_x = event.pos[0] - hero_size/2
                    hero_y = event.pos[1] - hero_size/2
            heroRect = pygame.Rect(hero_x, hero_y, hero_size, hero_size)
            for n in smallList:
                n.x += random.randint(-1,3)
                if n.top < 0:
                    n.top = 0
                if n.bottom > 800:
                    n.bottom = 800
                if n.left < 0:
                    n.left = 0
                if n.right > 1200:
                    n.right = 0
                if heroRect.colliderect(n):    
                    smallList.remove(n)
                    print("吃掉了！")
                    GoldQins += 1
                    hero_size += 5
                    heroImgs = pygame.transform.scale(heroImg, (hero_size, hero_size))
                    if smallList == []:
                        print('胜利！')
                        myWord = '胜利！'
                        sleep(1)
                        cl1 = 2
                        guan = wgsm
                        part = wen
            for i in middleList:
                i.x += random.randint(-1,2)
                if i.top < 0:
                    i.top = 0
                if i.bottom > 800:
                    i.bottom = 800
                if i.left < 0:
                    i.left = 0
                if i.right > 1200:
                    i.right = 0
                if heroRect.colliderect(i):
                    if hero_size*hero_size >= 140*140:
                        middleList.remove(i)
                        print("吃掉了！")
                        GoldQins += 1
                        hero_size += 12
                        heroImgs = pygame.transform.scale(heroImg, (hero_size, hero_size))
                    elif hero_size*hero_size < 140*140:
                        print("KO！")
                        myWord = 'KO!'
                        sleep(1)
                        cl1 = 1
                        guan = 0
            for x in bigList:
                x.x += random.randint(-1,1)
                if x.top < 0:
                    x.top = 0
                if x.bottom > 800:
                    x.bottom = 800
                if x.left < 0:
                    x.left = 0
                if x.right > 1200:
                    x.right = 0
                if heroRect.colliderect(x):
                    if hero_size*hero_size >= 180*180:
                        bigList.remove(x)
                        print("吃掉了！")
                        GoldQins += 1
                        hero_size += 40
                        heroImgs = pygame.transform.scale(heroImg, (hero_size, hero_size))
                    elif hero_size*hero_size < 180*180:
                        print("KO！")
                        myWord = 'KO!'
                        sleep(1)
                        cl1 = 1
                        guan = 0
            screen.fill((0, 100, 250))
            screen.blit(heroImgs, heroRect)
            for rects in smallList:
                screen.blit(smallImgs, rects)
            for rectm in middleList:
                screen.blit(middleImgs, rectm)
            for rectb in bigList:
                screen.blit(bigImgs, rectb)
            myText = myFont.render(myWord, 1, GREEN)
            screen.blit(myText,(570,40))
            pygame.display.update()
        print('你的金币数：',GoldQins)
    
    
    
    #------------------------------------------------------------
    
    
    
    while part == 2:
        guan = 0
        while guan == 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if fanhuiRect.collidepoint(event.pos):
                        part = 1
                        guan = 100
                elif event.type == pygame.KEYDOWN:
                    if event.key == 97:
                        guan = 1
                    elif event.key == 98:
                        guan = 2
                    elif event.key == 99:
                        guan = 3
            
            ###############一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一
            ##########一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一
            ###########一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一
            
            myWordTitle = 'shop'
            myWord = 'VIP可以免费，买VIP按a（5k金币），买换字体按b（10金币），买变大10*10按c（100金币），买'
            myWord2 = ''
            myWord3 = ''
            myWord4 = ''
            myWord5 = ''
            myWord6 = ''
            myWord7 = ''
            myTextTitle = myFont2.render(myWordTitle, 1, BLACK)
            myText = myFont2.render(myWord, 1, BLACK)
            myText2 = myFont2.render(myWord2, 1, BLACK)
            myText3 = myFont2.render(myWord3, 1, BLACK)
            myText4 = myFont2.render(myWord4, 1, BLACK)
            myText5 = myFont2.render(myWord5, 1, BLACK)
            myText6 = myFont2.render(myWord6, 1, BLACK)
            myText7 = myFont2.render(myWord7, 1, BLACK)
            screen.fill((255,255,255))
            screen.blit(fanhuiImgs,fanhuiRect)
            screen.blit(myTextTitle,(530,0))
            screen.blit(myText,(0,20))
            screen.blit(myText2,(0,20*2))
            screen.blit(myText3,(0,20*3))
            screen.blit(myText4,(0,20*4))
            screen.blit(myText5,(0,20*5))
            screen.blit(myText6,(0,20*6))
            screen.blit(myText7,(0,20*7))
            pygame.display.update()
        
        while guan == 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            try:
                password
            except:
                print('请先登录创建密码！！！')
                break
            plm = input('请输入密码：')
            if plm != password:
                print('密码错误！！！')
                break
            else:
                if GoldQins < 5000:
                    print('账户金币不足！')
                    break
                else:
                    print('支付成功！！！')
                    GoldQins -= 5000
                    VIP = 1
                    break
            pygame.display.update()
        
        while guan == 2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            try:
                password
            except:
                print('请先登录创建密码！！！')
                break
            plm = input('请输入密码：')
            if plm != password:
                print('密码错误！！！')
                break
            else:
                if VIP == 0:
                    if GoldQins < 10:
                        print('账户金币不足！')
                        break
                    else:
                        print('支付成功！！！')
                        GoldQins -= 10
                        ziti = input('你需要什么字体？1楷体（默认），2黑体，3微软雅黑，4行楷')
                        if xi_tong == '1':
                            if ziti == '1':
                                myFont = pygame.font.SysFont("kaiti", 40)
                                myFont2 = pygame.font.SysFont("kaiti", 20)
                            elif ziti == '2':
                                myFont = pygame.font.SysFont("stxihei", 40)
                                myFont2 = pygame.font.SysFont("stxihei", 20)
                            elif ziti == '3':
                                myFont = pygame.font.SysFont("Simhei", 40)
                                myFont2 = pygame.font.SysFont("Simihei", 20)
                            else:
                                myFont = pygame.font.SysFont("stxingkai", 40)
                                myFont2 = pygame.font.SysFont("stxingkai", 20)
                        else:
                            if ziti == '1':
                                myFont = pygame.font.SysFont("kaittf", 40)
                                myFont2 = pygame.font.SysFont("kaittf", 20)
                            elif ziti == '2':
                                myFont = pygame.font.SysFont("heittf", 40)
                                myFont2 = pygame.font.SysFont("heittf", 20)
                            elif ziti == '3':
                                myFont = pygame.font.SysFont(None, 40)
                                myFont2 = pygame.font.SysFont(None, 20)
                            else:
                                myFont = pygame.font.SysFont("xingkaittc", 40)
                                myFont2 = pygame.font.SysFont("xingkaittc", 20)
                        print('兑换成功。')
                        break
                else:
                    print('VIP直接不用钱拿走特效。。。')
                    ziti = input('你需要什么字体？1楷体（默认），2黑体，3微软雅黑，4行楷')
                    if xi_tong == '1':
                        if ziti == '1':
                            myFont = pygame.font.SysFont("kaiti", 40)
                            myFont2 = pygame.font.SysFont("kaiti", 20)
                        elif ziti == '2':
                            myFont = pygame.font.SysFont("stxihei", 40)
                            myFont2 = pygame.font.SysFont("stxihei", 20)
                        elif ziti == '3':
                            myFont = pygame.font.SysFont("Simhei", 40)
                            myFont2 = pygame.font.SysFont("Simihei", 20)
                        else:
                            myFont = pygame.font.SysFont("stxingkai", 40)
                            myFont2 = pygame.font.SysFont("stxingkai", 20)
                    else:
                        if ziti == '1':
                            myFont = pygame.font.SysFont("kaittf", 40)
                            myFont2 = pygame.font.SysFont("kaittf", 20)
                        elif ziti == '2':
                            myFont = pygame.font.SysFont("heittf", 40)
                            myFont2 = pygame.font.SysFont("heittf", 20)
                        elif ziti == '3':
                            myFont = pygame.font.SysFont(None, 40)
                            myFont2 = pygame.font.SysFont(None, 20)
                        else:
                            myFont = pygame.font.SysFont("xingkaittc", 40)
                            myFont2 = pygame.font.SysFont("xingkaittc", 20)
                    print('兑换成功。')
                    break
            pygame.display.update()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        