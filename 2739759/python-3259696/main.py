import pygame,sys,random,os
pygame.init()
screen = pygame.display.set_mode((600,800))
pygame.display.set_caption("双旦小游戏")
def sd(printword,speed):
    for i in printword:
        print(i,end="")
        pygame.time.delay(speed)
    print()
bird_x = 100
bird_rect = pygame.Rect(bird_x,490,50,35)
text = pygame.font.SysFont("仿宋",106)
text = text.render("Merry Christmas",1,(255,69,0))
tree = pygame.image.load("圣诞树.jpg")
tree = pygame.transform.scale(tree,(150,250))
star = pygame.image.load("小心心.jpg")
start = pygame.image.load("开始.png")
start = pygame.transform.scale(start,(150,50))
hat = pygame.image.load("圣诞帽.jpg")
hat = pygame.transform.scale(hat,(50,50))
bird = pygame.image.load("小鸟.png")
bird = pygame.transform.scale(bird,(50,35))
bug = pygame.image.load("虫子.png")
bug = pygame.transform.scale(bug,(25,50))
bug_rect = pygame.Rect(500,490,25,50)
bgmusic = pygame.mixer.music.load("圣诞快乐.mp3")
pygame.mixer.music.play(-1)
bgpic = pygame.image.load("bgpic.png")
bgpic = pygame.transform.scale(bgpic,(600,800))
bgpic1 = pygame.image.load("bg2.png")
bgpic1 = pygame.transform.scale(bgpic1,(600,800))
santa = pygame.image.load("圣诞老人.jpg")
santa = pygame.transform.scale(santa,(100,100))
screen.fill((0,162,232))
screen.blit(tree,(0,500))
screen.blit(tree,(450,500))
screen.blit(start,(225,500))
screen.blit(text,(1,200))
screen.blit(hat,(1,150))
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sd("\033[1;32m好玩吗？记得点亮小心心哦！！！",150)
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            screen.blit(bgpic,(0,0))
            screen.blit(bug,bug_rect)
            num = 100
            while True:
                a = random.randint(1,4)
                screen.blit(bgpic,(0,0))
                screen.blit(bug,bug_rect)
                bird_x = bird_x+a
                bird_rect = pygame.Rect(bird_x,490,50,35)
                screen.blit(bird,bird_rect)
                screen.blit(bug,bug_rect)
                pygame.time.delay(random.randint(1,100))
                text3 = pygame.font.SysFont("仿宋",50)
                text3 = text3.render("loading...",1,(255,255,255))
                screen.blit(text3,(100,200))
                pygame.display.update()
                if bird_rect.colliderect(bug_rect):
                    break
            screen.blit(bgpic1,(0,0))   
            screen.blit(santa,(100,100)) 
            sd("\033[1;31m你好，我叫圣诞老人！我来给大家送礼物，可是礼物撒了一地你来帮我捡吧！",50)
            text = pygame.font.SysFont("仿宋",50)
            text = text.render("Hello, my name is Santa Claus! ",1,(255,69,0))
            text1 = pygame.font.SysFont("仿宋",27)
            text1 = text1.render("I'll give you gifts, but the gifts have scattered all over the floor. ",1,(255,69,0))
            text2 = pygame.font.SysFont("仿宋",50)
            text2 = text2.render("Please help me pick them up.",1,(255,69,0))
            screen.blit(text,(1,200))
            screen.blit(text1,(1,243))
            screen.blit(text2,(1,265))
            pygame.display.update()
            pygame.time.delay(5000)
            #初始化
            import pygame,sys,random
            pygame.init()
            screen = pygame.display.set_mode((700, 700))
            pygame.display.set_caption("双旦小游戏")
            bgImg = pygame.image.load("bg2.png")
            bgImg = pygame.transform.scale(bgImg,(700,700))
            #设置变量、矩形
            times=60
            score=0
            num=1
            hero_x = 300
            hero_y = 300
            hero_size = 100
            hero_speed = 5
            heroImgs = pygame.transform.scale(santa, (hero_size, hero_size))
            #加载图片
            bgmusic = pygame.mixer.music.load("极地特快.mp3")
            pygame.mixer.music.play(-1)
            fruit1 = pygame.image.load("礼物1.jpg")
            fruit2 = pygame.image.load("礼物2.jpg")
            fruit3 = pygame.image.load("礼物3.jpg")
            fruit4 = pygame.image.load("礼物4.jpg")
            fruit5 = pygame.image.load("礼物.jpg")
            fruitImg = [fruit1, fruit2, fruit3, fruit4, fruit5]
            fruitImgs = pygame.transform.scale(fruitImg[random.randint(0, 4)], (40, 40))
            fruitList = []
            print("\033[1;36m通过上、下、左、右键控制圣诞老人移动。倒计时三秒开始！")
            for i in range (3,0,-1):
                print(i)
                pygame.time.delay(1000)
            for i in range(10):
                fruitRect = pygame.Rect(random.randint(0,675),random.randint(0,675),40,40)
                fruitList.append(fruitRect)
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sd("\033[1;32m好玩吗？记得点亮小心心哦！！！",150)
                        pygame.quit()
                        sys.exit()
                press=pygame.key.get_pressed()
                if press[273]:
                    hero_y=hero_y-hero_speed
                if press[274]:
                    hero_y=hero_y+hero_speed
                if press[276]:
                    hero_x=hero_x-hero_speed
                if press[275]:
                    hero_x=hero_x+hero_speed
                heroRect = pygame.Rect(hero_x, hero_y, hero_size, hero_size)
                for n in fruitList:
                    if heroRect.colliderect(n):
                        fruitList.remove(n)
                        print("\033[1;34m捡到啦")
                        score=score+1
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
                        print("\033[31m还剩",times,"秒")
                        times=times-1
                if times == 0:
                    if score >=80:
                        print("\033[1;33m你捡了",score,"个礼物，敲厉害，大神级！！！狂击999（666翻啦！）")
                    elif score <80 and score >=70:
                        print("\033[1;33m你捡了",score,"个礼物，厉害，大师级！！！")
                    elif score < 70 and score >=60:
                        print("\033[1;33m你捡了",score,"个礼物，中等偏上，黄金级")
                    elif score < 60 and score >=50:
                        print("\033[1;33m你捡了",score,"个礼物，中等，白银级")
                    elif score < 50 and score >=40:
                        print("\033[1;33m你捡了",score,"个礼物，中等偏下，青铜级")
                    else:
                        print("\033[1;33m你捡了",score,"个礼物，继续努力，石器级")
                    sd("\033[1;31mO(∩_∩)O谢谢你，我要去送礼物啦886！！！",100)
                    sd("\033[1;32m好玩吗？记得点亮小心心哦！！！",150)
                    pygame.quit()
                    sys.exit()
                screen.blit(heroImgs, heroRect)
                pygame.display.update()