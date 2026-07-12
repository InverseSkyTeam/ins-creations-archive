import pygame,sys,tkinter.filedialog,tkinter,tkinter.messagebox
from PIL import Image
from xes.tool import *
def game():
    pygame.init()
    # 初始化图片，rect
    screen = pygame.display.set_mode((1200,650))
    pygame.display.set_caption("制作像素画")
    # 开始创作
    startlist = [pygame.image.load("game_start_up.png"),pygame.image.load("game_start_down.png")]
    startlist[1] = pygame.transform.scale(startlist[1],(300,50))
    startlist[0] = pygame.transform.scale(startlist[0],(300,50))
    startrect = pygame.Rect(450,550,300,50)
    # 上传图片
    womenup = pygame.image.load("women.png")
    womenup = pygame.transform.scale(womenup,(400,125))
    womendown = pygame.image.load("women2.png")
    womendown = pygame.transform.scale(womendown,(400,125))
    womenRect = pygame.Rect(700,230,400,125)
    womanimgList = [womenup,womendown]
    b2 = womanimgList[0]
    # 导出二维链表
    menup = pygame.image.load("men.png")
    menup = pygame.transform.scale(menup,(200,70))
    mendown = pygame.image.load("men2.png")
    mendown = pygame.transform.scale(mendown,(200,70))
    menRect = pygame.Rect(990,400,200,70)
    manimgList = [menup,mendown]
    b1 = manimgList[0]
    # 再次创作
    women1up = pygame.image.load("women(1).png")
    women1up = pygame.transform.scale(women1up,(200,70))
    women1down = pygame.image.load("women2(1).png")
    women1down = pygame.transform.scale(women1down,(200,70))
    women1Rect = pygame.Rect(990,480,200,70)
    woman1imgList = [women1up,women1down]
    b21 = woman1imgList[0]
    # 下一步
    nextlist = [pygame.image.load("next2.png"),pygame.image.load("next.png")]
    nextlist[1] = pygame.transform.scale(nextlist[1],(300,70))
    nextlist[0] = pygame.transform.scale(nextlist[0],(300,70))
    nextrect = pygame.Rect(875,575,300,100)
    nextimg = nextlist[1]
    # 白色rect框架
    rect1 = pygame.Rect(700,230,20,20)
    rect2 = pygame.Rect(700,399,300,2)
    rect3 = pygame.Rect(650,0,550,650)
    rect4 = pygame.Rect(0,550,1200,100)
    # 滑动rect框架
    huarect = pygame.Rect(760,384.5,10,30)
    # 对勾
    quelist = [pygame.image.load("确定2.png"),pygame.image.load("确定.png")]
    quelist[0] = pygame.transform.scale(quelist[0],(100,100))
    quelist[1] = pygame.transform.scale(quelist[1],(100,100))
    querect = pygame.Rect(1100,550,100,100)
    queimg = quelist[0]
    # 定义变量
    x = 0
    huax=760
    p = 0
    x1=0
    y1=0
    flag = 0
    list1=[]
    list2=[]
    lenth1 = int((huax-700)/3)
    # 调整字体
    try:
        import ntpath # 如果成功，那么是Windows
        FONTNAME = "kaiti"
        del ntpath
    except ImportError: # 如果失败，是MacOS
        FONTNAME = "kaittf"
    # 主循环
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                x1 = event.pos[0]
                y1 = event.pos[1]
            # 控制开始创作按钮
            if startrect.collidepoint(x1,y1):
                startimg = startlist[1]
                screen.blit(startimg,startrect)
                pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button==1:
                        # 第二个界面的主循环
                        while True:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                                # 上传图片按钮
                                if event.type == pygame.MOUSEMOTION:
                                    x1 = event.pos[0]
                                    y1 = event.pos[1]
                                if womenRect.collidepoint(x1,y1):
                                    b2 = womanimgList[1]
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        if event.button==1:
                                            root = tkinter.Tk()
                                            root.withdraw() #隐藏Tk窗口
                                            selectFileName = tkinter.filedialog.askopenfilename(title='选择图片')
                                            img = pygame.image.load(selectFileName)
                                            flag=1
                                if not womenRect.collidepoint(x1,y1):
                                    b2 = womanimgList[0]
                                # 下一步按钮
                                if nextrect.collidepoint(x1,y1):
                                    nextimg = nextlist[1]
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        if event.button==1 and flag == 1:
                                            # 第三个界面主循环
                                            pygame.time.delay(1)
                                            while True:
                                                for event in pygame.event.get():
                                                    if event.type == pygame.QUIT:
                                                        pygame.quit()
                                                        sys.exit()
                                                    elif event.type == pygame.MOUSEBUTTONDOWN:
                                                        p = 1
                                                    elif event.type == pygame.MOUSEBUTTONUP:
                                                        p = 0
                                                    elif p == 1:
                                                        if event.type == pygame.MOUSEMOTION:
                                                            huax=event.pos[0]
                                                            if huax<700:
                                                                huax=700
                                                            if huax>1000:
                                                                huax=1000
                                                            huarect.center = (huax,400) 
                                                            rect1 = pygame.Rect(700,230,int((huax-700)/3),int((huax-700)/3))
                                                            lenth1 = int((huax-700)/3)
                                                            pygame.display.update()
                                                    if event.type == pygame.MOUSEMOTION:
                                                        x1 = event.pos[0]
                                                        y1 = event.pos[1]
                                                    if nextrect.collidepoint(x1,y1):
                                                        nextimg = nextlist[1]
                                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                                            if event.button==1 and flag == 1:
                                                                while True:
                                                                    for event in pygame.event.get():
                                                                        if event.type == pygame.QUIT:
                                                                            pygame.quit()
                                                                            sys.exit()
                                                                        if event.type == pygame.MOUSEMOTION:
                                                                            x1 = event.pos[0]
                                                                            y1 = event.pos[1]
                                                                        if querect.collidepoint(x1,y1):
                                                                            queimg = quelist[1]
                                                                            screen.blit(queimg,querect)
                                                                            pygame.display.update()
                                                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                                                if event.button==1:
                                                                                    lenth1 = int((huax-700)/3)
                                                                                    img1 = Image.open(selectFileName)
                                                                                    try:
                                                                                        for i in range(int(img1.size[1]/lenth1)):
                                                                                            for j in range(int(img1.size[0]/lenth1)):
                                                                                                i1 = screen.get_at((int(lenth1)*j,int(lenth1)*i))
                                                                                                list1.append(i1)
                                                                                            list2.append(list1)
                                                                                            list1 = []
                                                                                    except:
                                                                                        pass
                                                                                    while True:
                                                                                        for event in pygame.event.get():
                                                                                            if event.type == pygame.QUIT:
                                                                                                pygame.quit()
                                                                                                sys.exit()
                                                                                            if event.type == pygame.MOUSEMOTION:
                                                                                                x1 = event.pos[0]
                                                                                                y1 = event.pos[1]
                                                                                            if querect.collidepoint(x1,y1):
                                                                                                queimg = quelist[1]
                                                                                                screen.blit(queimg,querect)
                                                                                                pygame.display.update()
                                                                                                if event.type == pygame.MOUSEBUTTONDOWN:
                                                                                                    if event.button==1:
                                                                                                        if img1.size[0]>1200 and img1.size[1]>650:
                                                                                                            screen1 = screen
                                                                                                        if img1.size[0]>1200:
                                                                                                            screen1 = pygame.transform.chop(screen, (1200, img1.size[1],1200, 650))
                                                                                                        if img1.size[1]>650:
                                                                                                            screen1 = pygame.transform.chop(screen, (img1.size[0], 650,1200, 650))
                                                                                                        else:
                                                                                                            screen1 = pygame.transform.chop(screen, (img1.size[0], img1.size[1],1200, 650))
                                                                                                        pygame.image.save(screen1,"像素画.png")
                                                                                                        xopen()
                                                                                            else:
                                                                                                queimg = quelist[0]
                                                                                            if women1Rect.collidepoint(x1,y1):
                                                                                                b21 = woman1imgList[1]
                                                                                                if event.type == pygame.MOUSEBUTTONDOWN:
                                                                                                    if event.button==1:
                                                                                                        game()
                                                                                            if not women1Rect.collidepoint(x1,y1):
                                                                                                b21 = woman1imgList[0]
                                                                                            if menRect.collidepoint(x1,y1):
                                                                                                b1 = manimgList[1]
                                                                                                if event.type == pygame.MOUSEBUTTONDOWN:
                                                                                                    if event.button==1:
                                                                                                        with open("二维链表.txt","w",encoding = "utf-8")as file:
                                                                                                            file.write(str(list2))
                                                                                                            xopen()
                                                                                            if not menRect.collidepoint(x1,y1):
                                                                                                b1 = manimgList[0]
                                                                                        screen.fill((255,255,100))
                                                                                        screen.blit(b21,women1Rect)
                                                                                        screen.blit(b1,menRect)
                                                                                        screen.blit(queimg,querect)
                                                                                        for i in range(len(list2)):
                                                                                            for j in range(len(list2[i])):
                                                                                                myRect = pygame.Rect(j*lenth1,i*lenth1,lenth1,lenth1)
                                                                                                pygame.draw.rect(screen, list2[i][j], myRect, 0)
                                                                                        pygame.display.update()
                                                                        else:
                                                                            queimg = quelist[0]
                                                                    screen.fill((255,255,100))
                                                                    screen.blit(img,(0,0))
                                                                    screen.blit(queimg,querect)
                                                                    pygame.display.update()
                                                    if not nextrect.collidepoint(x1,y1):
                                                        nextimg = nextlist[0]
                                                # 显示图片
                                                screen.fill((255,255,100))
                                                screen.blit(img,(0,0))
                                                pygame.draw.rect(screen,(255,255,100),rect4,0)
                                                pygame.draw.rect(screen,(255,255,100),rect3,0)
                                                pygame.draw.rect(screen,(255,255,255),rect1,0)
                                                pygame.draw.rect(screen,(0,0,0),rect1,1)
                                                pygame.draw.rect(screen,(0,0,0),rect2,0)
                                                pygame.draw.rect(screen,(255,255,255),huarect,0)
                                                pygame.draw.rect(screen,(0,0,0),huarect,1)
                                                screen.blit(pygame.font.SysFont(FONTNAME,30).render("调整像素大小",True,(0,0,0)),(1000,382))
                                                screen.blit(nextimg,nextrect)
                                                pygame.display.update()
                                if not nextrect.collidepoint(x1,y1):
                                        nextimg = nextlist[0]
                            # 显示图片
                            screen.fill((255,255,100))
                            if flag == 1:
                                screen.blit(img,(0,0))
                            screen.blit(b2,womenRect)
                            screen.blit(pygame.font.SysFont(FONTNAME,30).render("图片过大会影响生成效果",True,(0,0,0)),(740,380))
                            screen.blit(nextimg,nextrect)
                            pygame.display.update()
            if not startrect.collidepoint(x1,y1):
                    startimg = startlist[0]
        # 显示图片
        screen.fill((255,255,100))
        screen.blit(pygame.font.SysFont(FONTNAME,150).render("制作像素画",True,(0,0,0)),(250,100))
        screen.blit(startimg,startrect)
        pygame.display.update()
game()