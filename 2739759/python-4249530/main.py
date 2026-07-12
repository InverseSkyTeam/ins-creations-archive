# 据说穿越“时空隧道”就可以到达“过去”或“未来”，太神奇了！
# 目前科学家还没有找到“穿越时空的方法”。
# 但是我们可以用今天所学的知识模拟一下穿越时空的画面
# 要求：
# 1、用矩形框模拟“时空隧道”的形状
# 2、加载“飞行器”或“飞人”图片，模仿在隧道穿行的情景
# boat.png为飞船，hero.png为飞人
import pygame, sys, random, time, os
print("给大敏！！！！！！！！！！！！！！！！")
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("时空隧道")
heroImg = pygame.image.load("hero.png")
pygame.mixer.music.load("多来爱梦.mp3")
pygame.mixer.music.play(-1)
def drawRect(x, y, n):  # 参数为中心x,中心y,圈数
    for i in range(n):
        myRect = pygame.Rect(100, 100, 50 + i * 30, 50 + i * 30)
        myRect.center = (x, y)
        # 补全下列代码，设置随机的颜色值，范围为0-255
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        #填写23行给矩形框设置随机宽度，建议范围不要太大，参考（1-20）
        w = random.randint(1, 20)
        screen.blit(heroImg, (250, 150))
        #填写26行绘制矩形框的语句
        pygame.draw.rect(screen,(r,g,b),myRect,w)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            screen = pygame.display.set_mode((800, 600))
            pygame.display.set_caption("黑科技展示")
            screen.fill((255,255,255))
            import platform
            if platform.system()=='Windows':
                myFont = pygame.font.SysFont("kaiti", 20)
                word = "你是Windows系统"
                r1 = myFont.render(word,True,(0,0,20))
                screen.blit(r1,(0,0))
                pygame.display.update()
            elif platform.system()=='Mac':
                myFont = pygame.font.Sysfont("kaittf",20)
                word = "你是Mac系统"
                r1 = myFont.render(word,True,(0,0,0))
                screen.blit(r1,(0,0))
                pygame.display.update()
            else:
                print('其他系统无法使用')
                pygame.time.delay(3000)
                pygame.quit()
                sys.exit()
            pygame.time.delay(3000)
            screen.fill((255,255,255))
            word = "你猜猜我是如何知道你的系统的，惊不惊喜？意不意外？"
            r1 = myFont.render(word,True,(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)))
            screen.blit(r1,(0,0))
            pygame.display.update()
            pygame.time.delay(3000)
            word = "再来看这个"
            r1 = myFont.render(word,True,(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)))
            screen.blit(r1,(0,20))
            pygame.display.update()
            pygame.time.delay(3000)
            word = "访问网站"
            r1 = myFont.render(word,True,(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)))
            screen.blit(r1,(0,40))
            pygame.display.update()
            pygame.time.delay(3000)
            word = "访问百度官网,三秒后开始，给你10秒浏览官网，7秒后有提示音"
            r1 = myFont.render(word,True,(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)))
            screen.blit(r1,(0,60))
            pygame.display.update()
            pygame.time.delay(3000)
            os.system("start www.baidu.com")
            pygame.time.delay(7000)
            s1 = pygame.mixer.Sound(str(random.randint(1,8))+".wav")
            s1.play()
            pygame.time.delay(3000)
            word = "访问编程社区,三秒后开始，给你10秒浏览官网，7秒后有提示音"
            r1 = myFont.render(word,True,(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)))
            screen.blit(r1,(0,80))
            pygame.display.update()
            pygame.time.delay(3000)
            os.system("start https://code.xueersi.com")
            pygame.time.delay(7000)
            s1 = pygame.mixer.Sound(str(random.randint(1,8))+".wav")
            s1.play()
            pygame.time.delay(3000)
            word = "看一下终端"
            r1 = myFont.render(word,True,(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)))
            screen.blit(r1,(0,120))
            pygame.display.update()
            import this
            word = "这吗多东西只用一行代码哦！！！"
            r1 = myFont.render(word,True,(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)))
            screen.blit(r1,(0,140))
            pygame.display.update()
            pygame.time.delay(3000)
            word = "python世界有许多这样的黑科技，快来学而思编程学习吧！！！！"
            r1 = myFont.render(word,True,(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)))
            screen.blit(r1,(0,160))
            pygame.display.update()
            pygame.time.delay(3000)
            a = input("是否关机？（y/n）：")
            if a == "y":
                os.system("shutdown/s")
            if a == "n":
                word = "好吧"
                r1 = myFont.render(word,True,(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)))
                screen.blit(r1,(0,180))
                pygame.display.update()
                pygame.time.delay(3000)
                pygame.quit()
                sys.exit()
    screen.fill((0, 0, 0))
    #填写34行，调用drawRect(x,y,n)函数，在画布中(400,300)位置显示矩形框
    drawRect(400,300, 100)
    pygame.display.update()
    time.sleep(0.03)      # 用来调整闪动频率
