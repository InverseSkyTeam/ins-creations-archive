def youxi():
    import pygame,sys,random
    pygame.init()
    num2 = 0
    mousesound = pygame.mixer.Sound("1.wav")
    mousesound.set_volume(0.2)
    try:
        import ntpath # 如果成功，那么是Windows
        FONTNAME = "kaiti"
        del ntpath
    except ImportError: # 如果失败，是MacOS
        FONTNAME = "kaittf"
    s = 0
    q = 0
    x1 = 0
    y1 = 0
    imgy = 650
    xingbie = "nan"
    startlist = [pygame.image.load("game_start_up.png"),pygame.image.load("game_start_down.png")]
    startlist[1] = pygame.transform.scale(startlist[1],(300,50))
    startlist[0] = pygame.transform.scale(startlist[0],(300,50))
    startrect = pygame.Rect(450,550,300,50)
    def sdpygame(word,delaytime,wordx,wordy):
        x4 = wordx
        for i in word:
            if x4 > 1120:
                x4 = wordx
                wordy = wordy+50
            screen.blit(pygame.font.SysFont(FONTNAME,30).render(i,True,(255,100,200)),(x4,wordy))
            x4 = x4 + 30
            screen.blit(queimg,querect)
            screen.blit(beijingList[num1],(beijingx,0))
            screen.blit(body,(bodyx,50))
            screen.blit(b1,(b1x,150))
            screen.blit(f1,(f1x,250))
            screen.blit(d1,(d1x,210))
            screen.blit(c1,(c1x,190))
            if yn == "y":
                screen.blit(e1,(e1x,205))
            if xingbie == "nan":
                screen.blit(a1,(a1x,90))
            if xingbie == "nv":
                screen.blit(a1,(a1x,80))
            pygame.display.update()
            if i == "!":
                break
            pygame.display.update()
            pygame.time.delay(delaytime)
    screen = pygame.display.set_mode((1200,650))
    pygame.display.set_caption("捏脸小游戏")
    pygame.display.set_icon(pygame.image.load("男.png"))
    musiclist = ["遇见你的时候所有星星都落到我头上","芒种","绿色"]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                x1 = event.pos[0]
                y1 = event.pos[1]
            if startrect.collidepoint(x1,y1):
                startimg = startlist[1]
                screen.blit(startimg,startrect)
                pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button==1:
                        womenup = pygame.image.load("women.png")
                        womenup = pygame.transform.scale(womenup,(400,150))
                        womendown = pygame.image.load("women2.png")
                        womendown = pygame.transform.scale(womendown,(400,150))
                        womenRect = pygame.Rect(700,345,400,133)
                        menup = pygame.image.load("men.png")
                        menup = pygame.transform.scale(menup,(400,150))
                        mendown = pygame.image.load("men2.png")
                        mendown = pygame.transform.scale(mendown,(400,150))
                        menRect = pygame.Rect(700,145,400,133)
                        womanimgList = [womenup,womendown]
                        manimgList = [menup,mendown]
                        a2 = manimgList[0]
                        b2 = womanimgList[1]
                        man = pygame.image.load("男.png")
                        woman = pygame.image.load("女.png")
                        nextlist = [pygame.image.load("next2.png"),pygame.image.load("next.png")]
                        nextlist[1] = pygame.transform.scale(nextlist[1],(300,70))
                        nextlist[0] = pygame.transform.scale(nextlist[0],(300,70))
                        nextrect = pygame.Rect(875,575,300,100)
                        man = pygame.transform.scale(man,(675,675))
                        woman = pygame.transform.scale(woman,(675,675))
                        img = man
                        nextimg = nextlist[0]
                        while True:
                            screen.fill((255,255,100))
                            if imgy > 0:
                                imgy = imgy - 5
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                                if event.type == pygame.MOUSEMOTION:
                                    x1 = event.pos[0]
                                    y1 = event.pos[1]
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    if event.button==1:
                                        if menRect.collidepoint(event.pos):
                                            a2 = manimgList[0]
                                            b2 = womanimgList[1]
                                            xingbie = "nan"
                                            if img == woman:
                                                imgy = 650
                                                img = man
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    if event.button==1:
                                        if womenRect.collidepoint(event.pos):
                                            b2 = womanimgList[0]
                                            a2 = manimgList[1]
                                            xingbie = "nv"
                                            if img == man:
                                                imgy = 650
                                                img = woman
                                if nextrect.collidepoint(x1,y1):
                                    nextimg = nextlist[1]
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        if event.button==1:
                                            import pygame,sys,random
                                            pygame.init()
                                            p = 0
                                            x2 = 400
                                            blitnum = 0
                                            num = 0
                                            bodyx = 1200
                                            if xingbie == "nv":
                                                a1x = 1205
                                            if xingbie == "nan":
                                                a1x = 1230
                                            yn = "n"
                                            b1x = 1250
                                            c1x = 1275
                                            d1x = 1275
                                            e1x = 1255
                                            f1x = 1278
                                            beijingList = []
                                            for i in range(1,5):
                                                a = pygame.image.load("背景"+str(i)+".png")
                                                a = pygame.transform.scale(a,(540,650))
                                                beijingList.append(a)
                                            faxingnan = []
                                            for i in range(1,9):
                                                a = pygame.image.load("发型-男"+str(i)+".png")
                                                faxingnan.append(a)
                                            faxingnv = []
                                            for i in range(1,9):
                                                a = pygame.image.load("发型-女"+str(i)+".png")
                                                faxingnv.append(a)
                                            lianxing = []
                                            for i in range(1,7):
                                                a = pygame.image.load("脸型"+str(i)+".png")
                                                lianxing.append(a)
                                            meimao = []
                                            for i in range(1,15):
                                                a = pygame.image.load("眉毛"+str(i)+".png")
                                                meimao.append(a)
                                            body = pygame.image.load("body.png")
                                            body = a = pygame.transform.scale(body,(265,450))
                                            tubiao = []
                                            tubiaoming = ["嘴巴","发型","脸型","眉毛","眼睛","眼镜"]
                                            for i in tubiaoming :
                                                a = pygame.image.load(i+"图标.png")
                                                tubiao.append(a)
                                            tubiaoxuanzhong = []
                                            tubiaoxuanzhongming = ["嘴巴","头发","脸型","眉毛","眼睛","眼镜"]
                                            for i in tubiaoxuanzhongming :
                                                a = pygame.image.load(i+"选中.png")
                                                a = pygame.transform.scale(a,(100,100))
                                                tubiaoxuanzhong.append(a)
                                            yanjing1 = []
                                            for i in range(1,15):
                                                a = pygame.image.load("眼睛"+str(i)+".png")
                                                yanjing1.append(a)
                                            yanjing2 = []
                                            for i in range(1,7):
                                                a = pygame.image.load("眼镜"+str(i)+".png")
                                                yanjing2.append(a)
                                            buxuanweixuanzhong = pygame.image.load("不选择图标.png")
                                            buxuanweixuanzhong = pygame.transform.scale(buxuanweixuanzhong,(100,100))
                                            buxuanweixuanzhongRect = pygame.Rect(600,320,100,100)
                                            buxuanxuanzhong = pygame.image.load("不选择选中.png")
                                            buxuanxuanzhong = pygame.transform.scale(buxuanxuanzhong,(100,100))
                                            buxuanxuanzhongRect = pygame.Rect(600,320,100,100)
                                            zuiba = []
                                            for i in range(1,15):
                                                a = pygame.image.load("嘴巴"+str(i)+".png")
                                                zuiba.append(a)
                                            
                                            if xingbie == "nan":
                                                a1 = pygame.image.load("发型-男1.png")
                                                a1 = pygame.transform.scale(a1,(190,150))
                                            if xingbie == "nv":
                                                a1 = pygame.image.load("发型-女1.png")
                                                a1 = pygame.transform.scale(a1,(240,270))
                                            b1 = pygame.image.load("脸型1.png")
                                            b1 = pygame.transform.scale(b1,(150,150))
                                            c1 = pygame.image.load("眉毛1.png")
                                            c1 = pygame.transform.scale(c1,(100,30))
                                            d1 = pygame.image.load("眼睛1.png")
                                            d1 = pygame.transform.scale(d1,(100,30))    
                                            e1 = pygame.image.load("眼镜1.png")
                                            e1 = pygame.transform.scale(e1,(140,50))
                                            f1 = pygame.image.load("嘴巴1.png")
                                            f1 = pygame.transform.scale(f1,(100,30))
                                            
                                            
                                            faxingnanDic = {}
                                            def blit_faxingnan(height,length):
                                                oldx = 600
                                                x = 600
                                                y = 100
                                                for i in faxingnan:
                                                    b = pygame.Rect(x,y,height,length)
                                                    faxingnanDic[i] = b
                                                    i = pygame.transform.scale(i,(height,length))
                                                    screen.blit(i,b)
                                                    x = x+length+10
                                                    if x >= 1010:
                                                        x = oldx
                                                        y = y+height+10
                                            faxingnvDic = {}
                                            def blit_faxingnv(height,length):
                                                oldx = 600
                                                x = 600
                                                y = 100
                                                for i in faxingnv:
                                                    b = pygame.Rect(x,y,height,length)
                                                    faxingnvDic[i] = b
                                                    i = pygame.transform.scale(i,(height,length))
                                                    screen.blit(i,b)
                                                    x = x+length+10
                                                    if x >= 1010:
                                                        x = oldx
                                                        y = y+height+10
                                            lianxingDic = {}
                                            def blit_lianxing(height,length):
                                                oldx = 600
                                                x = 600
                                                y = 100
                                                for i in lianxing:
                                                    b = pygame.Rect(x,y,height,length)
                                                    lianxingDic[i] = b
                                                    i = pygame.transform.scale(i,(height,length))
                                                    screen.blit(i,b)
                                                    x = x+length+10
                                                    if x >= 1010:
                                                        x = oldx
                                                        y = y+height+10
                                            meimaoDic = {}
                                            def blit_meimao(height,length):
                                                oldx = 600
                                                x = 600
                                                y = 100
                                                for i in meimao:
                                                    b = pygame.Rect(x,y,height,length)
                                                    meimaoDic[i] = b
                                                    i = pygame.transform.scale(i,(height,length))
                                                    screen.blit(i,b)
                                                    x = x+length+120
                                                    if x >= 1010:
                                                        x = oldx
                                                        y = y+height+10
                                            yanjing1Dic = {}
                                            def blit_yanjing1(height,length):
                                                oldx = 600
                                                x = 600
                                                y = 100
                                                for i in yanjing1:
                                                    b = pygame.Rect(x,y,height,length)
                                                    yanjing1Dic[i] = b
                                                    i = pygame.transform.scale(i,(height,length))
                                                    screen.blit(i,b)
                                                    x = x+length+120
                                                    if x >= 1010:
                                                        x = oldx
                                                        y = y+height+10
                                            yanjing2Dic = {}
                                            def blit_yanjing2(height,length):
                                                oldx = 600
                                                x = 600
                                                y = 100
                                                for i in yanjing2:
                                                    b = pygame.Rect(x,y,height,length)
                                                    yanjing2Dic[i] = b
                                                    i = pygame.transform.scale(i,(height,length))
                                                    screen.blit(i,b)
                                                    x = x+length+120
                                                    if x >= 1010:
                                                        x = oldx
                                                        y = y+height+10
                                            zuibaDic = {}
                                            def blit_zuiba(height,length):
                                                oldx = 600
                                                x = 600
                                                y = 100
                                                for i in zuiba:
                                                    b = pygame.Rect(x,y,height,length)
                                                    zuibaDic[i] = b
                                                    i = pygame.transform.scale(i,(height,length))
                                                    screen.blit(i,b)
                                                    x = x+length+120
                                                    if x >= 1010:
                                                        x = oldx
                                                        y = y+height+10
                                            tubiaoRectList = []
                                            def blit_tubiao(height,length):
                                                oldx = 400
                                                x = 400
                                                y = 0
                                                for i in tubiao:
                                                    zuibaRect = pygame.Rect(x,y,height,length)
                                                    tubiaoRectList.append(zuibaRect)
                                                    zuiba = pygame.transform.scale(i,(height,length))
                                                    screen.blit(zuiba,zuibaRect)
                                                    x = x+length+30
                                                if x >= 1200:
                                                    x = oldx
                                                    y = y+height+10
                                            screen.fill((255,255,100))
                                            blit_tubiao(100,100)
                                            screen.blit(tubiaoxuanzhong[num],(x2,0))
                                            while True:
                                                x3 = x2 + 130*num
                                                if bodyx > 90:
                                                    screen.blit(tubiaoxuanzhong[0],(x3,0))
                                                if b1x > 140:
                                                    x3 = x2 + 130*num
                                                    screen.blit(tubiaoxuanzhong[0],(x3,0))
                                                if bodyx > 90:
                                                    bodyx = bodyx - 5
                                                    screen.fill((255,255,100))
                                                    blit_zuiba(100,30)
                                                    blit_tubiao(100,100)
                                                    x3 = x2 + 130*num
                                                    screen.blit(tubiaoxuanzhong[0],(x3,0))
                                                if b1x > 140:
                                                    b1x = b1x - 5
                                                    screen.fill((255,255,100))
                                                    blit_zuiba(100,30)
                                                    blit_tubiao(100,100)
                                                    x3 = x2 + 130*num
                                                    screen.blit(tubiaoxuanzhong[0],(x3,0))
                                                if f1x > 170:
                                                    f1x = f1x - 5
                                                    screen.fill((255,255,100))
                                                    blit_zuiba(100,30)
                                                    blit_tubiao(100,100)
                                                    x3 = x2 + 130*num
                                                    screen.blit(tubiaoxuanzhong[0],(x3,0))
                                                if d1x > 165:
                                                    d1x = d1x - 5
                                                    screen.fill((255,255,100))
                                                    blit_zuiba(100,30)
                                                    blit_tubiao(100,100)
                                                    x3 = x2 + 130*num
                                                    screen.blit(tubiaoxuanzhong[0],(x3,0))
                                                if c1x > 165:
                                                    c1x = c1x - 5
                                                    screen.fill((255,255,100))
                                                    blit_zuiba(100,30)
                                                    blit_tubiao(100,100)
                                                    x3 = x2 + 130*num
                                                    screen.blit(tubiaoxuanzhong[0],(x3,0))
                                                if e1x > 145:
                                                    e1x = e1x - 5
                                                    screen.fill((255,255,100))
                                                    blit_zuiba(100,30)
                                                    blit_tubiao(100,100)
                                                    x3 = x2 + 130*num
                                                    screen.blit(tubiaoxuanzhong[0],(x3,0))
                                                if xingbie == "nv":
                                                    if a1x > 95:
                                                        a1x = a1x - 5
                                                        screen.fill((255,255,100))
                                                        blit_zuiba(100,30)
                                                        blit_tubiao(100,100)
                                                        x3 = x2 + 130*num
                                                        screen.blit(tubiaoxuanzhong[0],(x3,0))
                                                if xingbie == "nan":
                                                    if a1x > 120:
                                                        a1x = a1x - 5
                                                        screen.fill((255,255,100))
                                                        blit_zuiba(100,30)
                                                        blit_tubiao(100,100)
                                                        x3 = x2 + 130*num
                                                        screen.blit(tubiaoxuanzhong[0],(x3,0))
                                                for event in pygame.event.get():
                                                    if event.type == pygame.QUIT:
                                                        pygame.quit()
                                                        sys.exit()
                                                    
                                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                                        if event.button==1:
                                                            for num in range(len(tubiaoRectList)):
                                                                if tubiaoRectList[num].collidepoint(event.pos):
                                                                    x3 = x2 + 130*num
                                                                    if num == 0:
                                                                        blitnum = num
                                                                        blit_tubiao(100,100)
                                                                        screen.blit(tubiaoxuanzhong[0],(x3,0))
                                                                        num = 0
                                                                    if num == 1:
                                                                        blitnum = num
                                                                        blit_tubiao(100,100)
                                                                        screen.blit(tubiaoxuanzhong[1],(x3,0))
                                                                        num = 1
                                                                    if num == 2:
                                                                        blitnum = num
                                                                        blit_tubiao(100,100)
                                                                        screen.blit(tubiaoxuanzhong[2],(x3,0))
                                                                        num = 2
                                                                    if num == 3:
                                                                        blitnum = num
                                                                        blit_tubiao(100,100)
                                                                        screen.blit(tubiaoxuanzhong[3],(x3,0))
                                                                        num = 3
                                                                    if num == 4:
                                                                        blitnum = num
                                                                        blit_tubiao(100,100)
                                                                        screen.blit(tubiaoxuanzhong[4],(x3,0))
                                                                        num = 4
                                                                    if num == 5:
                                                                        blitnum = num
                                                                        blit_tubiao(100,100)
                                                                        screen.blit(tubiaoxuanzhong[5],(x3,0))
                                                                        num = 5
                                                    x3 = x2 + 130*blitnum
                                                    if blitnum == 1 and xingbie == "nan":
                                                        screen.fill((255,255,100))
                                                        blit_faxingnan(150,150)
                                                        blit_tubiao(100,100)
                                                        screen.blit(tubiaoxuanzhong[1],(x3,0))
                                                        blitnum = 1
                                                        for i,j in faxingnanDic.items():
                                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                                if event.button==1:
                                                                    if j.collidepoint(event.pos):
                                                                        screen.fill((255,255,100))
                                                                        a1 = pygame.transform.scale(i,(190,150))
                                                                        blit_tubiao(100,100)
                                                                        x3 = x2 + 130*blitnum
                                                                        screen.blit(tubiaoxuanzhong[1],(x3,0))
                                                                        blit_faxingnan(150,150)
                                                                        pygame.display.update()
                                                                        j = ""
                                                    if blitnum == 1 and xingbie == "nv":
                                                        screen.fill((255,255,100))
                                                        blit_faxingnv(150,150)
                                                        blit_tubiao(100,100)
                                                        screen.blit(tubiaoxuanzhong[1],(x3,0))
                                                        blitnum = 1
                                                        for i,j in faxingnvDic.items():
                                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                                if event.button==1:
                                                                    if j.collidepoint(event.pos):
                                                                        screen.fill((255,255,100))
                                                                        a1 = pygame.transform.scale(i,(240,270))
                                                                        blit_tubiao(100,100)
                                                                        x3 = x2 + 130*blitnum
                                                                        screen.blit(tubiaoxuanzhong[1],(x3,0))
                                                                        blit_faxingnv(150,150)
                                                                        pygame.display.update()
                                                                        j = ""
                                                    if blitnum == 2:
                                                        screen.fill((255,255,100))
                                                        blit_lianxing(150,150)
                                                        blit_tubiao(100,100)
                                                        screen.blit(tubiaoxuanzhong[2],(x3,0))
                                                        blitnum = 2
                                                        for i,j in lianxingDic.items():
                                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                                if event.button==1:
                                                                    if j.collidepoint(event.pos):
                                                                        screen.fill((255,255,100))
                                                                        b1 = pygame.transform.scale(i,(150,150))
                                                                        blit_tubiao(100,100)
                                                                        x3 = x2 + 130*blitnum
                                                                        screen.blit(tubiaoxuanzhong[2],(x3,0))
                                                                        blit_lianxing(150,150)
                                                                        pygame.display.update()
                                                                        j = ""
                                                    if blitnum == 3:
                                                        screen.fill((255,255,100))
                                                        blit_meimao(100,30)
                                                        blit_tubiao(100,100)
                                                        screen.blit(tubiaoxuanzhong[3],(x3,0))
                                                        blitnum = 3
                                                        for i,j in meimaoDic.items():
                                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                                if event.button==1:
                                                                    if j.collidepoint(event.pos):
                                                                        screen.fill((255,255,100))
                                                                        c1 = pygame.transform.scale(i,(100,30))
                                                                        blit_tubiao(100,100)
                                                                        x3 = x2 + 130*blitnum
                                                                        screen.blit(tubiaoxuanzhong[3],(x3,0))
                                                                        blit_meimao(100,30)
                                                                        pygame.display.update()
                                                                        j = ""
                                                    if blitnum == 4:
                                                        screen.fill((255,255,100))
                                                        blit_yanjing1(100,30)
                                                        blit_tubiao(100,100)
                                                        screen.blit(tubiaoxuanzhong[4],(x3,0))
                                                        blitnum = 4
                                                        for i,j in yanjing1Dic.items():
                                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                                if event.button==1:
                                                                    if j.collidepoint(event.pos):
                                                                        screen.fill((255,255,100))
                                                                        d1 = pygame.transform.scale(i,(100,30))      
                                                                        blit_tubiao(100,100)
                                                                        x3 = x2 + 130*blitnum
                                                                        screen.blit(tubiaoxuanzhong[4],(x3,0))
                                                                        blit_yanjing1(100,30)
                                                                        pygame.display.update()
                                                                        j = ""
                                                    if blitnum == 5:
                                                        screen.fill((255,255,100))
                                                        blit_yanjing2(150,50)
                                                        screen.blit(buxuanweixuanzhong,buxuanweixuanzhongRect)
                                                        blit_tubiao(100,100)
                                                        screen.blit(tubiaoxuanzhong[5],(x3,0))
                                                        blitnum = 5
                                                        for i,j in yanjing2Dic.items():
                                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                                if event.button==1:
                                                                    if j.collidepoint(event.pos):
                                                                        screen.fill((255,255,100))
                                                                        e1 = pygame.transform.scale(i,(140,50))    
                                                                        blit_tubiao(100,100)
                                                                        x3 = x2 + 130*num
                                                                        screen.blit(tubiaoxuanzhong[5],(x3,0))
                                                                        blit_yanjing2(150,50)
                                                                        pygame.display.update()
                                                                        j = ""
                                                                        yn = "y"
                                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                                if event.button==1:
                                                                    if buxuanweixuanzhongRect.collidepoint(event.pos):
                                                                        screen.blit(buxuanxuanzhong,buxuanxuanzhongRect)
                                                                        yn = "n"
                                                                    else:
                                                                        screen.blit(buxuanweixuanzhong,buxuanweixuanzhongRect)
                                                    if blitnum == 0:
                                                        screen.fill((255,255,100))
                                                        blit_zuiba(100,30)
                                                        blit_tubiao(100,100)
                                                        screen.blit(tubiaoxuanzhong[0],(x3,0))
                                                        blitnum = 0
                                                        for i,j in zuibaDic.items():
                                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                                if event.button==1:
                                                                    if j.collidepoint(event.pos):
                                                                        screen.fill((255,255,100))
                                                                        blit_tubiao(100,100)
                                                                        screen.blit(tubiaoxuanzhong[0],(x3,0))
                                                                        f1 = pygame.transform.scale(i,(100,30))
                                                                        
                                                                        x3 = x2 + 130*num
                                                                        blit_zuiba(100,30)
                                                                        pygame.display.update()
                                                                        j = ""
                                                    if event.type == pygame.MOUSEMOTION:
                                                        x1 = event.pos[0]
                                                        y1 = event.pos[1]
                                                    if nextrect.collidepoint(x1,y1):
                                                        nextimg = nextlist[1]
                                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                                            if event.button==1:
                                                                import pygame,sys
                                                                pygame.init()
                                                                num1 = 0
                                                                while True:
                                                                    if bodyx < 485:
                                                                        bodyx = bodyx + 5
                                                                        screen.fill((255,255,100))
                                                                    if b1x < 535:
                                                                        b1x = b1x + 5
                                                                        screen.fill((255,255,100))
                                                                    if f1x < 560:
                                                                        f1x = f1x + 5
                                                                        screen.fill((255,255,100))
                                                                    if d1x < 560:
                                                                        d1x = d1x + 5
                                                                        screen.fill((255,255,100))
                                                                    if c1x < 560:
                                                                        c1x = c1x + 5
                                                                        screen.fill((255,255,100))
                                                                    if e1x < 540:
                                                                        e1x = e1x + 5
                                                                        screen.fill((255,255,100))
                                                                    if xingbie == "nv":
                                                                        if a1x < 490:
                                                                            a1x = a1x + 5
                                                                            screen.fill((255,255,100))
                                                                    if xingbie == "nan":
                                                                        if a1x < 515:
                                                                            a1x = a1x + 5
                                                                            screen.fill((255,255,100))
                                                                    for event in pygame.event.get():
                                                                        if event.type == pygame.QUIT:
                                                                            pygame.quit()
                                                                            sys.exit()
                                                                        if event.type == pygame.KEYDOWN:
                                                                            if event.key == pygame.K_RIGHT:
                                                                                num1 = num1 + 1
                                                                                if num1 > 4:
                                                                                    num1 = 0
                                                                            if event.key == pygame.K_LEFT:
                                                                                num1 = num1 - 1
                                                                                if num1 < 0:
                                                                                    num1 = 4
                                                                        if event.type == pygame.MOUSEMOTION:
                                                                            x1 = event.pos[0]
                                                                            y1 = event.pos[1]
                                                                        if nextrect.collidepoint(x1,y1):
                                                                            nextimg = nextlist[1]
                                                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                                                if event.button==1:
                                                                                    import pygame
                                                                                    pygame.init()
                                                                                    quelist = [pygame.image.load("确定2.png"),pygame.image.load("确定.png")]
                                                                                    quelist[0] = pygame.transform.scale(quelist[0],(100,100))
                                                                                    quelist[1] = pygame.transform.scale(quelist[1],(100,100))
                                                                                    querect = pygame.Rect(1100,550,100,100)
                                                                                    queimg = quelist[0]
                                                                                    beijingx = 345
                                                                                    while True:
                                                                                        if bodyx > 140:
                                                                                            bodyx = bodyx - 5
                                                                                            screen.fill((255,255,100))
                                                                                        if b1x > 190:
                                                                                            b1x = b1x - 5
                                                                                            screen.fill((255,255,100))
                                                                                        if f1x > 215:
                                                                                            f1x = f1x - 5
                                                                                            screen.fill((255,255,100))
                                                                                        if d1x > 215:
                                                                                            d1x = d1x - 5
                                                                                            screen.fill((255,255,100))
                                                                                        if c1x > 215:
                                                                                            c1x = c1x - 5
                                                                                            screen.fill((255,255,100))
                                                                                        if e1x > 195:
                                                                                            e1x = e1x - 5
                                                                                            screen.fill((255,255,100))
                                                                                        if xingbie == "nv":
                                                                                            if a1x > 145:
                                                                                                a1x = a1x - 5
                                                                                                screen.fill((255,255,100))
                                                                                        if xingbie == "nan":
                                                                                            if a1x > 170:
                                                                                                a1x = a1x - 5
                                                                                                screen.fill((255,255,100))
                                                                                        if beijingx > 0:
                                                                                            beijingx = beijingx - 5
                                                                                            screen.fill((255,255,100))
                                                                                        if beijingx <= 0:
                                                                                            sdpygame(printword,0,600,100)
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
                                                                                                                import pygame,sys,os,platform,time,tkinter,tkinter.filedialog
                                                                                                                # from PIL import ImageGrab
                                                                                                                # import qrcode
                                                                                                                # pygame.init()
                                                                                                                # fileDir="捏脸成品.png"
                                        
                                                                                                                # screen2 = tkinter.Tk()
                                                                                                                # current_w = screen2.winfo_screenwidth()
                                                                                                                # current_h = screen2.winfo_screenheight()
                                                                                                                
                                                                                                                # S1=(current_w/2)-600
                                                                                                                # S2=(current_h/2)-315
                                                                                                                # ImageGrab.grab((S1,S2,S1+1200,S2+650)).save(fileDir)
                                                                                                                
                                                                                                                # userPlatform=platform.system()
                                                                                                                # if userPlatform == 'Darwin':	# Mac
                                                                                                                #     subprocess.call(['open', fileDir])
                                                                                                                # elif userPlatform == 'Linux':	# Linux
                                                                                                                #     subprocess.call(['xdg-open', fileDir])
                                                                                                                # else:							# Windows
                                                                                                                #     os.startfile(fileDir)
                                                                                                                root = tkinter.Tk()
                                                                                                                root.withdraw()
                                                                                                                pygame.image.save(screen,tkinter.filedialog.askdirectory(title = "保存文件")+"/捏脸成品.png")
                                                                                                    else:
                                                                                                        queimg = quelist[0]
                                                                                                screen.blit(queimg,querect)
                                                                                                screen.blit(beijingList[num1],(beijingx,0))
                                                                                                screen.blit(body,(bodyx,50))
                                                                                                screen.blit(b1,(b1x,150))
                                                                                                screen.blit(f1,(f1x,250))
                                                                                                screen.blit(d1,(d1x,210))
                                                                                                screen.blit(c1,(c1x,190))
                                                                                                if yn == "y":
                                                                                                    screen.blit(e1,(e1x,205))
                                                                                                if xingbie == "nan":
                                                                                                    screen.blit(a1,(a1x,90))
                                                                                                if xingbie == "nv":
                                                                                                    screen.blit(a1,(a1x,80))
                                                                                                pygame.display.update()
                                                                                        screen.fill((255,255,100))
                                                                                        screen.blit(queimg,querect)
                                                                                        screen.blit(beijingList[num1],(beijingx,0))
                                                                                        screen.blit(body,(bodyx,50))
                                                                                        screen.blit(b1,(b1x,150))
                                                                                        screen.blit(f1,(f1x,250))
                                                                                        screen.blit(d1,(d1x,210))
                                                                                        screen.blit(c1,(c1x,190))
                                                                                        if yn == "y":
                                                                                            screen.blit(e1,(e1x,205))
                                                                                        if xingbie == "nan":
                                                                                            screen.blit(a1,(a1x,90))
                                                                                        if xingbie == "nv":
                                                                                            screen.blit(a1,(a1x,80))
                                                                                        pygame.display.update()
                                                                        else:
                                                                            nextimg = nextlist[0]
                                                                    screen.fill((255,255,100))
                                                                    screen.blit(nextimg,nextrect)
                                                                    if num1 > len(beijingList)-1:
                                                                        num1 = 0
                                                                    if num1 < 0:
                                                                        num1 = len(beijingList)-1
                                                                    screen.blit(beijingList[num1],(345,0))
                                                                    screen.blit(pygame.font.SysFont(FONTNAME,30).render("按下左/右移键切换背景",True,(0,0,0)),(455,600))
                                                                    screen.blit(body,(bodyx,50))
                                                                    screen.blit(b1,(b1x,150))
                                                                    screen.blit(f1,(f1x,250))
                                                                    screen.blit(d1,(d1x,210))
                                                                    screen.blit(c1,(c1x,190))
                                                                    if yn == "y":
                                                                        screen.blit(e1,(e1x,205))
                                                                    if xingbie == "nan":
                                                                        screen.blit(a1,(a1x,90))
                                                                    if xingbie == "nv":
                                                                        screen.blit(a1,(a1x,80))
                                                                    pygame.display.update()
                                                                    
                                                    else:
                                                        nextimg = nextlist[0]
                                                screen.blit(nextimg,nextrect)
                                                screen.blit(body,(bodyx,50))
                                                screen.blit(b1,(b1x,150))
                                                screen.blit(f1,(f1x,250))
                                                screen.blit(d1,(d1x,210))
                                                screen.blit(c1,(c1x,190))
                                                if yn == "y":
                                                    screen.blit(e1,(e1x,205))
                                                if xingbie == "nan":
                                                    screen.blit(a1,(a1x,90))
                                                if xingbie == "nv":
                                                    screen.blit(a1,(a1x,80))
                                                pygame.display.update()
                                else:
                                    nextimg = nextlist[0]
                            screen.blit(a2,menRect)
                            screen.blit(nextimg,nextrect)
                            screen.blit(b2,womenRect)
                            screen.blit(img,(0,imgy))
                            pygame.display.update()
            else:
                startimg = startlist[0]
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    num2 = num2 + 1
                    if num2 > 2:
                        num2 = 0
                    s = 1
                    screen.blit(startimg,startrect)
                    pygame.display.update()
                    pygame.mixer.music.load(musiclist[num2]+".mp3")
                    pygame.mixer.music.play(-1)
                if event.key == pygame.K_RIGHT:
                    num2 = num2 - 1
                    if num2 < 0:
                        num2 = 2
                    s = 1
                    screen.blit(startimg,startrect)
                    pygame.display.update()
                    pygame.mixer.music.load(musiclist[num2]+".mp3")
                    pygame.mixer.music.play(-1)
            screen.fill((255,255,100))
            screen.blit(pygame.font.SysFont(FONTNAME,150).render("捏脸小游戏",True,(0,0,0)),(250,100))
            screen.blit(pygame.font.SysFont(FONTNAME,30).render("按下左/右移键切换背景音乐",True,(0,0,0)),(415,420))
            if s == 1:
                screen.blit(pygame.font.SysFont(FONTNAME,20).render("当前音乐："+musiclist[num2],True,(0,0,0)),(415,470))
            else:
                screen.blit(pygame.font.SysFont(FONTNAME,20).render("当前音乐：无",True,(0,0,0)),(415,470))
            screen.blit(startimg,startrect)
            pygame.display.update()
while True:
    print("""欢迎来到捏脸小游戏！
P.S.：1.如果有卡顿或屏幕闪烁属于正常现象
      2.不要移动窗口，因为要截屏
      3.图片移动时不要操作，否则会有bug
      4.文字可能有问题，请见谅
      5.本游戏由锦辉（鹦鹉）工作室创作（其实就我一个人，所以是否有小组里我填了否）
    抵制不良游戏，杜绝盗版游戏
    适度游戏健脑，沉迷游戏伤身""")
    yourname = input("\033[1;32m请输入你的名字:（点击方框后开始输入，按下回车输入）")
    itname = input("\033[1;36m请输入你将要绘制的人的名字:")
    guanxi = input("\033[1;33m请输入你是他的（1.学生 2.朋友 3.仇人 4.老师 5.同学 6.其他 请输入序号）")
    if guanxi == "1":
        printword = itname+"您好，我是您的学生"+yourname+"，因为有了您，我的世界才会变得如此美丽，混沌之中，才有了指路的明灯，迷茫的夜空，才有了永恒的北斗。您的严格让我懂得分寸，您的关怀使我成长。在期盼中送我远走，在辛苦中架起又一座桥梁，辛勤的汗水是您无私的奉献，桃李满天下是您最高的荣誉。愿您天天开心事事如意！！！"
        youxi()
    elif guanxi == "4":
        printword = itname+"同学好，我是您的老师"+yourname+"，因为有了您，我的世界才会变得如此美丽，混沌之中，才有了指路的明灯，迷茫的夜空，才有了永恒的北斗。您的认真让我感动，您的好奇使我沉思。在期盼中送您远走，从你的进步，让我看到希望的曙光，辛勤的汗水是您求知的脚步，高高在上的学历是您最高的荣誉。愿您好好学习天天向上！！！"
        youxi()
    elif guanxi == "3":
        printword = itname+"您好，我是您的仇人"+yourname+"，尽管我们关系不好，可我还想说：因为有了您，我的世界才会变得如此美丽，混沌之中，才有了指路的明灯，迷茫的夜空，才有了永恒的北斗。愿您天天开心事事如意！！！"
        youxi()
    elif guanxi == "2":
        printword = itname+"您好，我是您的朋友"+yourname+"，因为有了您，我的世界才会变得如此美丽，混沌之中，才有了指路的明灯，迷茫的夜空，才有了永恒的北斗。您的认真让我感动，您的好奇使我沉思。在期盼中送您远走，从你的进步，让我看到希望的曙光，辛勤的汗水是您求知的脚步，高高在上的学历是您最高的荣誉。愿您好好学习天天向上！！！"
        youxi()
    elif guanxi == "5":
        printword = itname+"您好，我是您的同学"+yourname+"，因为有了您，我的世界才会变得如此美丽，混沌之中，才有了指路的明灯，迷茫的夜空，才有了永恒的北斗。您的认真让我感动，您的好奇使我沉思。在期盼中送您远走，从你的进步，让我看到希望的曙光，辛勤的汗水是您求知的脚步，高高在上的学历是您最高的荣誉。愿您好好学习天天向上！！！"
        youxi()
    elif guanxi == "6":
        printword = itname+"您好，我是"+yourname+"，我想对您说：因为有了您，我的世界才会变得如此美丽，混沌之中，才有了指路的明灯，迷茫的夜空，才有了永恒的北斗。愿您天天开心事事如意！！！"
        youxi()
    else:
        print("\033[0m没有此关系,请重新输入")
