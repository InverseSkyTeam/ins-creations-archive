#本软件由J·hx公司开发，小轩创作！
#1.2.4
#版权所有，侵权必究！
#自己设计，绞尽脑汁！
#不看代码，抄袭拦截！
#请勿偷看，开开脑洞！
'''
66666
导库、初始化￥￥￥￥￥￥￥$$$$$￥￥￥￥￥￥￥
66666
'''
import pygame, sys
from time import *
while True:
    youxideng=input('输入：E=关闭/G=游戏/1=天气/2=中英文翻译')
    #1
    if youxideng == '1':
        print('查询天气中……')
        sleep(1.25)
        try:
            from xes.weather import *
            air1=input('你所在的城市，如：北京')
            try:
                print('今天'+str(air_temp(air1,0))+'° '),print('风速'+str(air_speed(air1,0))+'米/秒')
            except:
                print('输入错误！')
        except:
            print('你还没有安装学而思三大方库哦，\n快快安装吧！')
            sleep(2)
    #2
    elif youxideng == '2':
        try:
            from xes.AIspeak import *
            input('中-->英（输入1）/英-->中（输入2）')
            speakTrue = input('输入翻译内容：')
            amdf_sitvIhf_b = translate(speakTrue)
            sleep(0.4)
            print('翻译结果：',amdf_sitvIhf_b)
        except:
            print('你还没有安装学而思三大方库哦，\n快快安装吧！')
            sleep(2)
    #G
    elif youxideng == 'G':
        print('正在打开游戏……')
        sleep(1)
        print("请点开")
        pygame.init()
        #准备
        screen = pygame.display.set_mode((920, 600))
        pygame.display.set_caption("开宝箱！")
        bgImg = pygame.image.load('bg2.png')
        box1 = pygame.image.load('宝箱1.png')
        box1do = pygame.transform.scale(box1, (100, 100))
        box1Rect = pygame.Rect(10, 10, 100, 100)
        box2 = pygame.image.load('宝箱2.png')
        box2do = pygame.transform.scale(box2, (100, 100))
        box2Rect = pygame.Rect(10, 400, 100, 100)
        box3 = pygame.image.load('宝箱3.png')
        box3do = pygame.transform.scale(box3, (100, 100))
        box3Rect = pygame.Rect(50, 150, 100, 100)
        box4 = pygame.image.load('宝箱4.png')
        box4do = pygame.transform.scale(box4, (100, 100))
        box4Rect = pygame.Rect(160, 200, 100, 100)
        box5 = pygame.image.load('宝箱5.png')
        box5do = pygame.transform.scale(box5, (100, 100))
        box5Rect = pygame.Rect(300, 450, 100, 100)
        box6 = pygame.image.load('宝箱6.png')
        box6do = pygame.transform.scale(box6, (100, 100))
        box6Rect = pygame.Rect(200, 320, 100, 100)
        Gold = pygame.image.load('金子1.png')
        jin_zi____Img = pygame.transform.scale(Gold, (100, 100))
        GoldRect = pygame.Rect(200, 320, 100, 100)
        #变量初始化
        #设置字体、颜色、大小
        BLACK = (0,0,0)
        myFont = pygame.font.SysFont('kaiti',20)
        #文章
        myText1 = myFont.render('哪个箱子里有金子？信息：',True,BLACK)
        myText2 = myFont.render('1号箱说：金子不在我这儿,在4号箱。',True,BLACK)
        myText3 = myFont.render('2号箱说：金子在1号箱或3号箱内,6号箱没有金子。',True,BLACK)
        myText4 = myFont.render('3号箱说：1号箱说了假话,金子在我这儿。',True,BLACK)
        myText5 = myFont.render('4号箱说：6号箱确实没有金子,金子在我这儿。',True,BLACK)
        myText6 = myFont.render('5号箱说：金子在6号箱。前面4个箱子的话中都有假话。',True,BLACK)
        myText7 = myFont.render('6号箱说：金子在5号箱,它说了假话。',True,BLACK)
        myText_lan = myFont.render('+----------------------------------------------+',True,BLACK)
        myText8 = myFont.render('1个箱子说了真话；',True,BLACK)
        myText9 = myFont.render('2个箱子说了半真半假的话；',True,BLACK)
        myText10 = myFont.render('3个箱子说了假话。',True,BLACK)
        myText11 = myFont.render('单击左图的箱子：序号已经写在箱子上，点你认为的箱子。',True,BLACK)
        #---------------------------主循环-------------------------#
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if box1Rect.collidepoint(event.pos):
                        print("再好好想想。 ?  ")
                    if box2Rect.collidepoint(event.pos):
                        print("再好好想想。 ?  ")
                    if box3Rect.collidepoint(event.pos):
                        print("再好好想想。 ?  ")
                    if box4Rect.collidepoint(event.pos):
                        print("再好好想想。 ?  ")
                    if box5Rect.collidepoint(event.pos):
                        print("再好好想想。 ?  ")
                    if box6Rect.collidepoint(event.pos):
                        print("\033[32;45;4m对了！！！   ? ? \033[0m")
                        screen.blit(jin_zi____Img, GoldRect)
                        sleep(2)
                        pygame.quit()
                        sys.exit()
            screen.fill((50, 255, 180))
            screen.blit(bgImg, (0, 0))
            screen.blit(box1do, box1Rect)
            screen.blit(box2do, box2Rect)
            screen.blit(box3do, box3Rect)
            screen.blit(box4do, box4Rect)
            screen.blit(box5do, box5Rect)
            screen.blit(box6do, box6Rect)
            screen.blit(myText1, (400,0))
            screen.blit(myText_lan, (400,20))
            screen.blit(myText2, (400,40))
            screen.blit(myText3, (400,60))
            screen.blit(myText4, (400,80))
            screen.blit(myText5, (400,100))
            screen.blit(myText6, (400,120))
            screen.blit(myText7, (400,140))
            screen.blit(myText_lan, (400,160))
            screen.blit(myText8, (400,180))
            screen.blit(myText9, (400,200))
            screen.blit(myText10, (400,220))
            screen.blit(myText_lan, (400,240))
            screen.blit(myText11, (400,260))
            pygame.display.update()
    #Esc
    elif youxideng == 'G':
        pygame.quit()
        sys.exit()
        break
            
            
        





