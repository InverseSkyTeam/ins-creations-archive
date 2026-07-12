import pygame,sys,tkinter.filedialog,tkinter,tkinter.messagebox,tkinter.colorchooser,os
from PIL import Image
from xes.tool import *
def game():
    pygame.init()
    # 调整字体
    try:
        import ntpath # 如果成功，那么是Windows
        FONTNAME = "kaiti"
        del ntpath
    except ImportError: # 如果失败，是MacOS
        FONTNAME = "kaittf"
    # 初始化图片，rect
    screen = pygame.display.set_mode(size = (1200,650))
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
    # 全选
    qlist = [pygame.image.load("q1.png"),pygame.image.load("q2.png")]
    qlist[1] = pygame.transform.scale(qlist[1],(300,70))
    qlist[0] = pygame.transform.scale(qlist[0],(300,70))
    qrect = pygame.Rect(875,450,300,100)
    qimg = qlist[1]
    # 白色rect框架
    rect1 = pygame.Rect(700,220,20,20)
    rect2 = pygame.Rect(700,389,300,2)
    rect3 = pygame.Rect(650,0,550,650)
    rect4 = pygame.Rect(0,550,1200,100)
    rect6 = pygame.image.load("black.png").convert()
    rect6 = pygame.transform.scale(rect6,(1200,650))
    rect6.set_alpha(200)
    rect7 = pygame.image.load("white.png").convert()
    rect7 = pygame.transform.scale(rect7,(100,100))
    rect7.set_alpha(100)
    # 选择颜色
    red = pygame.Rect(700,450,50,50)
    orange = pygame.Rect(760,450,50,50)
    yellow = pygame.Rect(820,450,50,50)
    green = pygame.Rect(880,450,50,50)
    blue = pygame.Rect(940,450,50,50)
    purple = pygame.Rect(1000,450,50,50)
    white = pygame.Rect(700,510,50,50)
    black = pygame.Rect(760,510,50,50)
    r = pygame.Rect(0,0,0,0)
    cc = pygame.font.SysFont(FONTNAME,48).render("自定义颜色",True,(0,0,0))
    cc_rect= cc.get_rect()
    cc_rect.x = 820
    cc_rect.y = 510
    # 框选rect
    lenth_x = 100
    lenth_y = 100
    rect5 = pygame.Rect(10,10,lenth_x,lenth_y)
    c1 = pygame.Rect(rect5.x-5,rect5.y-5,10,10)
    c2 = pygame.Rect(rect5.x-5,rect5.y-5+lenth_y,10,10)
    c3 = pygame.Rect(rect5.x-5+lenth_x,rect5.y-5+lenth_y,10,10)
    c4 = pygame.Rect(rect5.x-5+lenth_x,rect5.y-5,10,10)
    c5 = pygame.Rect(c3.x,c3.y,50,50)
    # 滑动rect框架
    huarect = pygame.Rect(760,374.5,10,30)
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
    flag1 = 0
    flag2 = 0
    color = (255,255,100)
    list1=[]
    list2=[]
    lenth1 = int((huax-700)/3)
    # 主循环
    new_list = [pygame.image.load("new2.png"),pygame.image.load("new1.png")]
    new_list[1] = pygame.transform.scale(new_list[1],(300,100))
    new_list[0] = pygame.transform.scale(new_list[0],(300,100))
    new_img = new_list[0]
    new_rect = pygame.Rect(450,420,300,100)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                x1 = event.pos[0]
                y1 = event.pos[1]
            if new_rect.collidepoint(x1,y1):
                new_img = new_list[1]
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button==1:
                        os.system("movie.mp4")
            else:
                new_img = new_list[0]
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
                                            try:
                                                root = tkinter.Tk()
                                                root.withdraw() #隐藏Tk窗口
                                                selectFileName = tkinter.filedialog.askopenfilename(title='选择图片')
                                                img = pygame.image.load(selectFileName)
                                                img1 = Image.open(selectFileName)
                                                flag=1
                                            except:
                                                pass
                                if not womenRect.collidepoint(x1,y1):
                                    b2 = womanimgList[0]
                                # 下一步按钮
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
                                                    if nextrect.collidepoint(x1,y1):
                                                        nextimg = nextlist[1]
                                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                                            if event.button==1:
                                                                img = pygame.transform.chop(img,(0,0,rect5.x,rect5.y))
                                                                img = pygame.transform.chop(img,(c3.x,c3.y,1200,650))
                                                                r = img.get_rect()
                                                                # 第三个界面主循环
                                                                pygame.time.delay(1)
                                                                lenth1 = int((huax - 700) / 3)
                                                                img1 = Image.open(selectFileName)
                                                                try:
                                                                    for i in range(int(r.h/ lenth1)):
                                                                        for j in range(int(r.w/ lenth1)):
                                                                            i1 = screen.get_at((int(lenth1) * j, int(lenth1) * i))
                                                                            list1.append(i1)
                                                                        list2.append(list1)
                                                                        list1 = []
                                                                except:
                                                                    # pygame.display.iconify()
                                                                    tkinter.messagebox.showerror('错误', '您的图片过大定点击确定重试')
                                                                    game()
                                                                while True:
                                                                    for event in pygame.event.get():
                                                                        if event.type == pygame.QUIT:
                                                                            pygame.quit()
                                                                            sys.exit()
                                                                        if event.type == pygame.MOUSEMOTION:
                                                                            x1 = event.pos[0]
                                                                            y1 = event.pos[1]
                                                                        if cc_rect.collidepoint(x1,y1):
                                                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                                                if event.button==1:
                                                                                    try:
                                                                                        colors = tkinter.colorchooser.askcolor()
                                                                                        color = (int(colors[0][0]),int(colors[0][1]),int(colors[0][2])) 
                                                                                    except:
                                                                                        pass
                                                                                    
                                                                        if red.collidepoint(x1,y1):
                                                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                                                if event.button==1:
                                                                                    color = (255,0,0)
                                                                                    
                                                                        if orange.collidepoint(x1,y1):
                                                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                                                if event.button==1:
                                                                                    color = (255,180,0)
                                                                                    
                                                                        if yellow.collidepoint(x1,y1):
                                                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                                                if event.button==1:
                                                                                    color = (255,255,100)
                                                                                    
                                                                        if green.collidepoint(x1,y1):
                                                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                                                if event.button==1:
                                                                                    color = (0,255,0)
                                                                                    
                                                                        if blue.collidepoint(x1,y1):
                                                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                                                if event.button==1:
                                                                                    color = (0,0,255)
                                                                                    
                                                                        if purple.collidepoint(x1,y1):
                                                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                                                if event.button==1:
                                                                                    color = (180,0,255)
                                                                        
                                                                        if white.collidepoint(x1,y1):
                                                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                                                if event.button==1:
                                                                                    color = (255,255,255)
                                                                        
                                                                        if black.collidepoint(x1,y1):
                                                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                                                if event.button==1:
                                                                                    color = (0,0,0)
                                                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                                                            p = 1
                                                                        if event.type == pygame.MOUSEBUTTONUP:
                                                                            p = 0
                                                                        if p == 1:
                                                                            if event.type == pygame.MOUSEMOTION:
                                                                                huax=event.pos[0]
                                                                                if huax<703:
                                                                                    huax=703
                                                                                if huax>1000:
                                                                                    huax=1000
                                                                                huarect.center = (huax,390) 
                                                                                rect1 = pygame.Rect(700,220,int((huax-700)/3),int((huax-700)/3))
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
                                                                                                        list2 = []
                                                                                                        try:
                                                                                                            for i in range(int(r.h/lenth1)):
                                                                                                                for j in range(int(r.w/lenth1)):
                                                                                                                    i1 = screen.get_at((int(lenth1)*j,int(lenth1)*i))
                                                                                                                    list1.append(i1)
                                                                                                                list2.append(list1)
                                                                                                                list1 = []
                                                                                                        except:
                                                                                                            # pygame.display.iconify()
                                                                                                            tkinter.messagebox.showerror('错误','您的图片过大定点击确定重试')
                                                                                                            game()
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
                                                                                                                                screen1 = pygame.transform.chop(screen, (1200, r.h-lenth1,1200, 650))
                                                                                                                            if img1.size[1]>650:
                                                                                                                                screen1 = pygame.transform.chop(screen, (r.w-lenth1, 650,1200, 650))
                                                                                                                            else:
                                                                                                                                screen1 = pygame.transform.chop(screen, (r.w-lenth1, r.h-lenth1,1200, 650))
                                                                                                                            pygame.image.save(screen1,tkinter.filedialog.askdirectory(title = "保存文件")+"\像素画.png")
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
                                                                                        pygame.draw.rect(screen,color,r,0)
                                                                                        screen.blit(img,(0,0))
                                                                                        screen.blit(queimg,querect)
                                                                                        pygame.display.update()
                                                                        if not nextrect.collidepoint(x1,y1):
                                                                            nextimg = nextlist[0]
                                                                    # 显示图片
                                                                    screen.fill((255,255,100))
                                                                    pygame.draw.rect(screen,color,r,0)
                                                                    screen.blit(img,(0,0))
                                                                    list1 = []
                                                                    list2 = []
                                                                    lenth1 = int((huax - 700) / 3)
                                                                    try:
                                                                        for i in range(int(r.h / lenth1)):
                                                                            for j in range(int(r.w / lenth1)):
                                                                                i1 = screen.get_at((int(lenth1) * j,int(lenth1) * i))
                                                                                list1.append(i1)
                                                                            list2.append(list1)
                                                                            list1 = []
                                                                    except:
                                                                        # pygame.display.iconify()
                                                                        tkinter.messagebox.showerror('错误','您的图片过大定点击确定重试')
                                                                        game()
                                                                    for i in range(len(list2)):
                                                                        for j in range(len(list2[i])):
                                                                            myRect = pygame.Rect(j * lenth1, i * lenth1, lenth1, lenth1)
                                                                            pygame.draw.rect(screen, list2[i][j],myRect, 0)
                                                                    pygame.draw.rect(screen,(255,255,100),rect4,0)
                                                                    pygame.draw.rect(screen,(255,255,100),rect3,0)
                                                                    pygame.draw.rect(screen,(255,255,255),rect1,0)
                                                                    pygame.draw.rect(screen,(0,0,0),rect1,1)
                                                                    pygame.draw.rect(screen,(0,0,0),rect2,0)
                                                                    pygame.draw.rect(screen,(255,255,255),huarect,0)
                                                                    pygame.draw.rect(screen,(0,0,0),huarect,1)
                                                                    
                                                                    pygame.draw.rect(screen,(255,0,0),red,0)
                                                                    pygame.draw.rect(screen,(255,180,0),orange,0)
                                                                    pygame.draw.rect(screen,(255,255,100),yellow,0)
                                                                    pygame.draw.rect(screen,(0,255,0),green,0)
                                                                    pygame.draw.rect(screen,(0,0,255),blue,0)
                                                                    pygame.draw.rect(screen,(180,0,255),purple,0)
                                                                    pygame.draw.rect(screen,(255,255,255),white,0)
                                                                    pygame.draw.rect(screen,(0,0,0),black,0)
                                                                    
                                                                    pygame.draw.rect(screen,(0,0,0),red,1)
                                                                    pygame.draw.rect(screen,(0,0,0),orange,1)
                                                                    pygame.draw.rect(screen,(0,0,0),yellow,1)
                                                                    pygame.draw.rect(screen,(0,0,0),green,1)
                                                                    pygame.draw.rect(screen,(0,0,0),blue,1)
                                                                    pygame.draw.rect(screen,(0,0,0),purple,1)
                                                                    pygame.draw.rect(screen,(0,0,0),white,1)
                                                                    pygame.draw.rect(screen,(0,0,0),black,1)
                                                                    
                                                                    pygame.draw.rect(screen,color,cc_rect,0)
                                                                    pygame.draw.rect(screen,(0,0,0),cc_rect,1)
                                                                    screen.blit(pygame.font.SysFont(FONTNAME,30).render("选择背景颜色(用于圆角图片)",True,(0,0,0)),(700,412))
                                                                    screen.blit(pygame.font.SysFont(FONTNAME,30).render("调整像素大小",True,(0,0,0)),(1000,372))
                                                                    screen.blit(cc,cc_rect)
                                                                    screen.blit(nextimg,nextrect)
                                                                    pygame.display.update()
                                                    if not nextrect.collidepoint(x1,y1):
                                                        nextimg = nextlist[0]
                                                    if c5.collidepoint(x1,y1):
                                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                                            flag2 = 1
                                                    if not c5.collidepoint(x1,y1):
                                                        flag2 = 0
                                                    if flag2 == 1:
                                                        c3.center = x1,y1
                                                        lenth_x = x1-rect5.x
                                                        lenth_y = y1-rect5.y
                                                        rect5 = pygame.Rect(rect5.x,rect5.y,lenth_x,lenth_y)
                                                        c1 = pygame.Rect(rect5.x-5,rect5.y-5,10,10)
                                                        c2 = pygame.Rect(rect5.x-5,rect5.y-5+lenth_y,10,10)
                                                        c4 = pygame.Rect(rect5.x-5+lenth_x,rect5.y-5,10,10)
                                                        c3 = pygame.Rect(c3.x,c3.y,10,10)
                                                        c5 = pygame.Rect(c3.x,c3.y,50,50)
                                                        rect7 = pygame.transform.scale(rect7,(lenth_x,lenth_y))
                                                        if event.type == pygame.MOUSEBUTTONUP:
                                                            flag2 = 0
                                                    if not c4.collidepoint(x1,y1):
                                                        if rect5.collidepoint(x1,y1):
                                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                                flag1 = 1
                                                        if not rect5.collidepoint(x1,y1):
                                                            flag1 = 0
                                                        if flag1 == 1:
                                                            rect5.center = x1,y1
                                                            if rect5.x<0:
                                                                rect5.x = 0
                                                            if rect5.y<0:
                                                                rect5.y = 0
                                                            if rect5.x+lenth_x>img1.size[0]:
                                                                rect5.x = img1.size[0]-lenth_x
                                                            if rect5.y+lenth_y>img1.size[1]:
                                                                rect5.y = img1.size[1]-lenth_y
                                                            rect5 = pygame.Rect(rect5.x,rect5.y,lenth_x,lenth_y)
                                                            c1 = pygame.Rect(rect5.x-5,rect5.y-5,10,10)
                                                            c2 = pygame.Rect(rect5.x-5,rect5.y-5+lenth_y,10,10)
                                                            c3 = pygame.Rect(rect5.x-5+lenth_x,rect5.y-5+lenth_y,10,10)
                                                            c4 = pygame.Rect(rect5.x-5+lenth_x,rect5.y-5,10,10)
                                                            c5 = pygame.Rect(c3.x,c3.y,50,50)
                                                            if event.type == pygame.MOUSEBUTTONUP:
                                                                flag1 = 0
                                                    if qrect.collidepoint(x1,y1):
                                                        qimg = qlist[1]
                                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                                            if event.button==1:
                                                                lenth_x = img1.size[0]
                                                                lenth_y = img1.size[1]
                                                                rect5 = pygame.Rect(0,0,img1.size[0],img1.size[1])
                                                                c1 = pygame.Rect(rect5.x-5,rect5.y-5,10,10)
                                                                c2 = pygame.Rect(rect5.x-5,rect5.y-5+lenth_y,10,10)
                                                                c3 = pygame.Rect(rect5.x-5+lenth_x,rect5.y-5+lenth_y,10,10)
                                                                c4 = pygame.Rect(rect5.x-5+lenth_x,rect5.y-5,10,10)
                                                                c5 = pygame.Rect(c3.x,c3.y,50,50)
                                                                rect7 = pygame.transform.scale(rect7,(lenth_x,lenth_y))
                                                    if not qrect.collidepoint(x1,y1):
                                                        qimg = qlist[0]            
                                                screen.fill((255,255,100))
                                                screen.blit(img,(0,0))
                                                screen.blit(rect6,(0,0))
                                                screen.blit(rect7,(rect5.x,rect5.y))
                                                newimg = pygame.transform.chop(img, (0, 0, rect5.x, rect5.y))
                                                newimg = pygame.transform.chop(newimg, (rect5.w, rect5.h, 1200, 650))
                                                screen.blit(newimg, (rect5.x, rect5.y))
                                                pygame.draw.rect(screen,(255,255,255),rect5,1)
                                                pygame.draw.ellipse(screen,(255,255,255),c1,0)
                                                pygame.draw.ellipse(screen,(255,255,255),c2,0)
                                                pygame.draw.ellipse(screen,(255,0,0),c3,0)
                                                pygame.draw.ellipse(screen,(255,255,255),c4,0)
                                                screen.blit(nextimg,nextrect)
                                                screen.blit(qimg,qrect)
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
        screen.blit(new_img,new_rect)
        screen.blit(pygame.font.SysFont(FONTNAME,150).render("制作像素画",True,(0,0,0)),(250,100))
        screen.blit(startimg,startrect)
        pygame.display.update()
game()