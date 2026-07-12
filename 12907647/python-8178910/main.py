# 宇宙工作室成立第一天
# 宇宙长度小游戏：来自宇宙工作室的|室长|小轩编程
# 导入库、变量的初始化、pygame等游戏设备初始化
import pygame,sys,random,tkinter as tk
from time import *

pygame.init()

screen = pygame.display.set_mode((400,750))
pygame.display.set_caption("|宇宙|长度小游戏")

# 检测系统
try:import ntpath
except:osingxing = 'MacOs';font = pygame.font.SysFont('kaittf', 30);font2 = pygame.font.SysFont('kaittf', 20)
else:osingxing = 'Windows';font = pygame.font.SysFont('kaiti', 30);font2 = pygame.font.SysFont('kaiti', 20);del ntpath

bgSound = pygame.mixer.music.load('我们不一样.mp3')
pygame.mixer.music.set_volume(0.35)
pygame.mixer.music.play(-1)

image1 = pygame.image.load('高度+.png')
Rect1 = image1.get_rect()
Rect1.x = 325
image2 = pygame.image.load('高度-.png')
Rect2 = image2.get_rect()
Rect2.x = 365
jumpimg = pygame.image.load('高度跳转.png')
jumpRect = jumpimg.get_rect()
jumpRect.x = 400 - 105
jumpRect.y = 40
startimg = pygame.image.load('START1.png')
StartRect = startimg.get_rect()
StartRect.x = 200 - StartRect.width / 2
StartRect.y = 750 / 2 - StartRect.height / 2

myWord = '宇宙长度小游戏'
myText = font.render(myWord,True,(0,150,30))
sky_color = 255
GreenSkyData = 200
part = '大厅'
speed = 1
Gao_du = 0
CDDW = 'm'
greatWord = ''
event_type = ''
midText = font2.render(greatWord,True,(0,150,30))

def JumpMain():
    global root,pygame,entry,entry2,button,Gao_du,CDDW,label
    root = tk.Tk()
    root.geometry('300x200')
    def jump_to_main():
        global root,pygame,entry,entry2,button,Gao_du,CDDW,label
        if entry2.get() in ['m','km','AU','ly']:
            try:
                Gao_du = int(entry.get())
                CDDW = entry2.get()
                entry.delete(0,tk.END)
                entry2.delete(0,tk.END)
            except:
                label['text']='输入有误！'
        else:
            label['text']='输入有误！'
    label = tk.Label(root,text='第一条输入框输入高度数字\n第二条输入框输入长度单位\n可以输入的长度单位有\nm,km,AU,ly(AU是天文单位,ly是光年)')
    label.pack()
    entry = tk.Entry(root,font=('微软雅黑',15),bd = 3)
    entry.pack()
    entry2 = tk.Entry(root,font=('微软雅黑',15),bd = 3)
    entry2.pack()
    button = tk.Button(root,text='跳转到此位置',command=jump_to_main)
    button.pack()
    root.mainloop()



while True:
    while part == '大厅':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if StartRect.collidepoint(event.pos):
                    part = '游戏主循环'
        screen.fill((0,200,255))
        screen.blit(startimg,StartRect)
        screen.blit(myText,(100,75))
        pygame.display.update()
        pygame.time.Clock().tick(60)
    
    while part == '游戏主循环':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                mousePos = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                try:
                    if Rect1.collidepoint(mousePos):
                        event_type = '高飞键'
                    elif Rect2.collidepoint(mousePos):
                        event_type = '低落键'
                    elif jumpRect.collidepoint(mousePos):
                        JumpMain()
                except:
                    pass
            if event.type == pygame.MOUSEBUTTONUP:
                event_type = 'STOP键'
        if event_type == '高飞键':
            Gao_du += speed
        if event_type == '低落键':
            Gao_du -= speed
        
        if CDDW == 'm':
            if Gao_du >= 9000:
                speed = 1
                Gao_du = 9
                CDDW = 'km'
            elif Gao_du > 3000 and Gao_du < 7000:
                Gao_du = 7000
            elif Gao_du > 1000 and Gao_du < 2590:
                speed = 2
                Gao_du = 2950
        elif CDDW == 'km':
            if Gao_du >= 150000000:
                speed = 1
                Gao_du = 2
                CDDW = 'AU'
            elif Gao_du >= 10000000 and Gao_du < 150000000:
                speed = 1000000
            elif Gao_du >= 5000 and Gao_du < 10000:
                Gao_du = 10000
                speed = 10000
            elif Gao_du >= 3005 and Gao_du < 3500:
                speed = 10
                Gao_du = 3500
            elif Gao_du < 9:
                speed = 2
                Gao_du = 8999
                CDDW = 'm'
        elif CDDW == 'AU':
            if Gao_du >= 63000:
                speed = 1
                Gao_du = 1
                CDDW = 'ly'
            elif Gao_du >= 10000 and Gao_du < 63000:
                speed = 1000
            elif Gao_du >= 800 and Gao_du < 10000:
                speed = 100
            elif Gao_du >= 350 and Gao_du < 800:
                speed = 10
            elif Gao_du < 2:
                speed = 1000000
                Gao_du = 140000000
                CDDW = 'km'
        elif CDDW == 'ly':
            if Gao_du >= 300000000000:
                part = '新'
            elif Gao_du >= 1000000000 and Gao_du < 100000000000:
                speed = 1000000000
            elif Gao_du >= 10000000 and Gao_du < 1000000000:
                speed = 10000000
            elif Gao_du >= 100000 and Gao_du < 10000000:
                speed = 100000
            elif Gao_du >= 600 and Gao_du < 100000:
                speed = 100
            elif Gao_du < 1:
                speed = 1000
                Gao_du = 62000
                CDDW = 'AU'
        
        if Gao_du >= 4 and Gao_du <= 6 and CDDW == 'm':
            greatWord = '长颈鹿是最高的动物'
        elif Gao_du >= 65 and Gao_du <= 67 and CDDW == 'm':
            greatWord = '海平面上升的极限位置'
        elif Gao_du >= 73 and Gao_du <= 75 and CDDW == 'm':
            greatWord = '牛津大学第一次现代蹦极的高度'
        elif Gao_du >= 110 and Gao_du <= 117 and CDDW == 'm':
            greatWord = '世界上最高的树"亥伯龙神"'
        elif Gao_du == 370 and CDDW == 'm':
            greatWord = '世界上最高的输电塔在浙江舟山'
        elif Gao_du == 443 and CDDW == 'm':
            greatWord = '帝国大厦的高度'
        elif Gao_du == 468 and CDDW == 'm':
            greatWord = '东方明珠电视塔的高度'
        elif Gao_du == 508 and CDDW == 'm':
            greatWord = '台北101的高度，高不高'
        elif Gao_du == 828 and CDDW == 'm':
            greatWord = '世界上最高的楼，迪拜哈利法塔'
        elif Gao_du >= 1000 and Gao_du <= 1500 and CDDW == 'm':
            greatWord = '孔明灯一般飘到这么高'
        elif Gao_du >= 3000 and Gao_du <= 3500 and CDDW == 'm':
            greatWord = '一般气球高度在这儿'
        elif Gao_du == 8844 and CDDW == 'm':
            greatWord = '珠穆朗玛峰的高度'
        elif Gao_du == 9 and CDDW == 'km':
            greatWord = '我们来到了平流层下界'
        elif Gao_du == 10 and CDDW == 'km':
            greatWord = '恭喜来到第2关哦'
        elif Gao_du == 40 and CDDW == 'km':
            greatWord = '不错啊，继续！'
        elif Gao_du == 50 and CDDW == 'km':
            greatWord = '我们来到了中间层下界'
        elif Gao_du == 60 and CDDW == 'km':
            greatWord = '流星！我的天啊！快快许愿！'
        elif Gao_du == 80 and CDDW == 'km':
            greatWord = '一飞到这里，你变为宇航员'
        elif Gao_du == 85 and CDDW == 'km':
            greatWord = '我们来到了热层下界'
        elif Gao_du == 90 and CDDW == 'km':
            greatWord = '这里空气稀少，声音无法传播'
        elif Gao_du == 100 and CDDW == 'km':
            greatWord = '我们来到了卡门线'
        elif Gao_du == 105 and CDDW == 'km':
            greatWord = '就是太空和地球大气层的分界线'
        elif Gao_du == 300 and CDDW == 'km':
            greatWord = '竟然是太空垃圾，快躲开！'
        elif Gao_du == 429 and CDDW == 'km':
            greatWord = '看到了人造卫星东方红'
        elif Gao_du == 800 and CDDW == 'km':
            greatWord = '我们来到了散逸层'
        elif Gao_du == 2639 and CDDW == 'km':
            greatWord = '你看见了我们的蓝色星球'
        elif Gao_du == 3000 and CDDW == 'km':
            greatWord = '正式进入外太空'
        elif Gao_du == 3700 and CDDW == 'km':
            greatWord = '不错，继续！'
        elif Gao_du == 350000 and CDDW == 'km':         # 35万
            greatWord = '看见Moon(月球)了！'
        elif Gao_du == 500000 and CDDW == 'km':
            greatWord = '已经很远、高了！'
        elif Gao_du >= 800000 and Gao_du <= 1000000 and CDDW == 'km':
            greatWord = '进入第3关！'
        elif Gao_du >= 1500000 and Gao_du <= 2000000 and CDDW == 'km':
            greatWord = '已经非常远、高了！'
        elif Gao_du >= 3000000 and Gao_du <= 3500000 and CDDW == 'km':
            greatWord = '已经特别远、高了！'
        elif Gao_du >= 5000000 and Gao_du <= 6000000 and CDDW == 'km':
            greatWord = '获得了第一枚奖章！'
        elif Gao_du >= 6500000 and Gao_du <= 7000000 and CDDW == 'km':
            greatWord = '奖章：航天高高高高高手'
        elif Gao_du == 7500000 and CDDW == 'km':
            greatWord = '我们得继续赶路了！'
        elif Gao_du == 41000000 and CDDW == 'km':       # 4千万
            greatWord = '金星！哇塞！真美！'
        elif Gao_du == 75000000 and CDDW == 'km':
            greatWord = '水星！我的小可爱啊！'
        elif Gao_du == 149000000 and CDDW == 'km':      # 1亿-km
            greatWord = '太阳热啊这个位置是1AU(天文单位)'
        elif Gao_du == 2 and CDDW == 'AU':
            greatWord = '火星！好可爱啊！'
        elif Gao_du == 6 and CDDW == 'AU':
            greatWord = '木星！大个子行星！'
        elif Gao_du == 10 and CDDW == 'AU':
            greatWord = '土星也不赖嘛！'
        elif Gao_du == 19 and CDDW == 'AU':
            greatWord = '天王星！霸气！'
        elif Gao_du == 29 and CDDW == 'AU':
            greatWord = '海王星！霸气！'
        elif Gao_du == 30 and CDDW == 'AU':
            greatWord = '冥王星！可怜！！！'
        elif Gao_du == 50 and CDDW == 'AU':
            greatWord = '进入第4关！获得第2个奖章'
        elif Gao_du == 100 and CDDW == 'AU':
            greatWord = '你看看奖章：'
        elif Gao_du == 125 and CDDW == 'AU':
            greatWord = '奖章名：666第一飞行高速人员'
        elif Gao_du == 150 and CDDW == 'AU':
            greatWord = '你是不是很开心？！'
        elif Gao_du == 200 and CDDW == 'AU':
            greatWord = '不过……'
        elif Gao_du == 210 and CDDW == 'AU':
            greatWord = '我们的太阳系宇宙之旅结束啦？'
        elif Gao_du == 212 and CDDW == 'AU':
            greatWord = '才怪！'
        elif Gao_du == 300 and CDDW == 'AU':
            greatWord = '好吧，马上加速！'
        elif Gao_du == 1 and CDDW == 'ly':
            greatWord = 'ly是光年'
        elif Gao_du == 5 and CDDW == 'ly':
            greatWord = '你已经比光速快好多倍！'
        elif Gao_du == 9 and CDDW == 'ly':
            greatWord = '有个天狼星！'
        elif Gao_du == 10 and CDDW == 'ly':
            greatWord = '第5关！'
        elif Gao_du == 20 and CDDW == 'ly':
            greatWord = '呀，奖章，第3枚！'
        elif Gao_du == 30 and CDDW == 'ly':
            greatWord = '奖章：光年王者'
        elif Gao_du == 50 and CDDW == 'ly':
            greatWord = '听着不错，是吧！'
        elif Gao_du == 53 and CDDW == 'ly':
            greatWord = '有个白矮星！'
        elif Gao_du == 100 and CDDW == 'ly':
            greatWord = '我们离地球太远太远了！'
        elif Gao_du == 120 and CDDW == 'ly':
            greatWord = '哇哇哇哇哇哇哇！'
        elif Gao_du >= 300 and Gao_du <= 350 and CDDW == 'ly':
            greatWord = '第6关！有奖章！第4枚'
        elif Gao_du >= 400 and Gao_du <= 450 and CDDW == 'ly':
            greatWord = '奖章：无敌宇航王者'
        elif Gao_du >= 500 and Gao_du <= 550 and CDDW == 'ly':
            greatWord = '天啊，你真牛！'
        elif Gao_du == 3300 and CDDW == 'ly':
            greatWord = '猫眼星云，去看看！'
        elif Gao_du == 3400 and CDDW == 'ly':
            greatWord = '天啊，这么多恒星！'
        elif Gao_du == 3500 and CDDW == 'ly':
            greatWord = '真繁密，比北京地铁挤……'
        elif Gao_du == 3600 and CDDW == 'ly':
            greatWord = '100亿倍！毫不夸张！'
        elif Gao_du == 25900 and CDDW == 'ly':
            greatWord = '银河系中心的大黑洞！'
        elif Gao_du == 30000 and CDDW == 'ly':
            greatWord = '你逃脱了！'
        elif Gao_du == 116000 and CDDW == 'ly':
            greatWord = '你离开了银河系'
        elif Gao_du == 200000 and CDDW == 'ly':
            greatWord = '继续赶路，兄怼'
        elif Gao_du == 300000 and CDDW == 'ly':
            greatWord = '我们的目标是离开宇宙'
        elif Gao_du == 2500000 and CDDW == 'ly':      # 250万
            greatWord = '比银河系大1倍的仙女星系'
        elif Gao_du == 3000000 and CDDW == 'ly':
            greatWord = '三角座星系'
        elif Gao_du == 5000000 and CDDW == 'ly':      # 500万，当50
            greatWord = '？《相对论》？'
        elif Gao_du == 3000000000 and CDDW == 'ly':   # 30亿，当3
            greatWord = '我们离开了本超星系团'
        elif Gao_du == 10000000000 and CDDW == 'ly':  # 100亿，当10
            greatWord = '这里乱得随机生成个大脑'
        elif Gao_du == 100000000000 and CDDW == 'ly':
            greatWord = '我们来到了宇宙光墙'
        elif Gao_du == 200000000000 and CDDW == 'ly':
            greatWord = '我们要成功了！'
        elif Gao_du == 300000000000 and CDDW == 'ly':
            greatWord = '哦哦哦哦哦哦哦哦哦哦！'
        else:
            greatWord = ''
        
        if Gao_du < 10 and CDDW == 'km' or Gao_du <= 8999 and CDDW == 'm':
            GreenSkyData = 200
            sky_color = 255
        if Gao_du >= 10 and CDDW == 'km':
            GreenSkyData = 180
        if Gao_du >= 30 and CDDW == 'km':
            GreenSkyData = 150
        if Gao_du >= 50 and CDDW == 'km':
            GreenSkyData = 100
        if Gao_du >= 85 and CDDW == 'km':
            GreenSkyData = 20
        if Gao_du >= 100 and CDDW == 'km':
            GreenSkyData = 0
            sky_color = 250
        if Gao_du >= 150 and CDDW == 'km':
            sky_color = 210
        if Gao_du >= 200 and CDDW == 'km':
            sky_color = 180
        if Gao_du >= 350 and CDDW == 'km':
            sky_color = 120
        if Gao_du >= 429 and CDDW == 'km':
            sky_color = 150
        if Gao_du >= 600 and CDDW == 'km':
            sky_color = 100
        if Gao_du >= 1000 and CDDW == 'km':
            sky_color = 40
        if Gao_du >= 1500 and CDDW == 'km':
            sky_color = 0
        
        screen.fill((0,GreenSkyData,sky_color))
        screen.blit(image1,Rect1)
        screen.blit(image2,Rect2)
        screen.blit(jumpimg,jumpRect)
        screen.blit(myText,(5,5))
        screen.blit(midText,(200-len(greatWord)*20/2,750/2-10))
        pygame.display.update()
        pygame.time.Clock().tick(100)
        sleep(0.05)
        myWord = str(Gao_du) + CDDW
        myText = font.render(myWord,True,(140,140,140))
        midText = font2.render(greatWord,True,(140,140,140))
    
    while part == '新':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        for i in range(256):
            screen.fill((i,i,i))
            screen.blit(font2.render("加油吧，少年！",True,(0,0,0)),(200-len(greatWord)*20/2,750/2-10))
            sleep(0.025)
            pygame.display.update()
        part = '大厅'

























