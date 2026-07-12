import pygame,sys,random,os,math,lei,tkinter as tk;from time import *;from tkinter import messagebox
print('\033[1;34m我经历了无数困难\n我经历了无数时间\n我，经历了无数bug!')
p = print
s = sleep
def ps(strings,p=p,s=s):
    p(strings)
    s(0.05)
p('我没想到，我竟然成功了！\nWindos经典游戏扫雷！哇！\n一起来看看我的经历吧！')
s(0.2)
p('2020 years.')
s(0.1)
p('4/3 热身看‘Python从小白到大牛’，完成阅读wx')
s(0.1)
ps('4/4 热身看‘Python从小白到大牛’，完成阅读open')
ps('4/5 热身看‘Python从小白到大牛’，完成阅读class，学习编程')
ps('4/6 热身看‘Python从小白到大牛’，完成阅读复习')
ps('4/8 热身看‘Python从小白到大牛’，完成阅读对象编程')
ps('4/9 热身看‘Python从小白到大牛’，完成阅读高级')
ps('4/10 热身看‘Python从小白到大牛’，完成阅读open')
ps('4/11 热身纸上写代码整整半页')
ps('4/12 学习编程，认识更多优秀作品，获取源代码，吸收知识')
ps('4/13 开学')
ps('4/14 热身纸上写代码整整半页')
ps('4/15 热身纸上写代码整整3页')
ps('4/18 热身纸上写代码整整1页')
ps('4/19 热身纸上写代码整整1页，学习编程')
ps('4/21 热身代码尝试41行')
ps('4/22 热身纸上写代码整整半页')
ps('4/26 学习编程')
ps('4/27 删源代码，重新编程4小时')
ps('4/28 编程wx完成字体')
ps('5/1~5/5 放假，编程、重建、加lei.py(小轩"智"造)')
ps('5月 编程')
ps('6/7 完成编程1.0.1')
input('新的简介下次再说，已经编程2个半小时了，哦，Goodbye~游戏准备~\033[0m看完回车唔~！')
sleep(1)
pygame.init()
XB = 0
RM = 0
AJ = 0
MJ = 0
LJ = 0
WZ = 0
ZDY = 0
ButtonOption = 0
password = ''
name = ''
TEL = ''
RED = (255,8,3)
GREEN = (0,255,14)
BLUE = (0,11,253)
YELLOW = (203,200,1)
WHITE = (255,255,255)
BLACK = (0,0,0)

try:
    import ntpath             # 检测系统
except:
    osingxing = 'MacOs'
    font = pygame.font.SysFont('kaittf', 24)
else:
    osingxing = 'Windows'
    font = pygame.font.SysFont('kaiti', 25)
    del ntpath
finally:
    pass

lei.load_show(font)
def callback():
    res=messagebox.askokcancel("退出","您确定要退出吗？")
    if res==True:
        root.destroy()
        zdy = 0
    else:
        return
def main_loop(pygame=pygame,password=password,name=name,TEL=TEL):
    global entry1,entry2,entry3,label1
    try:
        f = open('扫雷-小轩-个人信息-20x082j9孑孓3101','r')
    except:
        f = open('扫雷-小轩-个人信息-20x082j9孑孓3101','w')
        f2 = open('扫雷-小轩-个人信息-20x082j9孑孓3102','w')
        f3 = open('扫雷-小轩-个人信息-20x082j9孑孓3103','w')
        label1['text'] = "文件打开失败，看来您是新玩家，欢迎！"
        password = entry1.get()
        name = entry2.get()
        TEL = entry3.get()
        f.write(password)
        f2.write(name)
        f3.write(TEL)
        f.close()
        f2.close()
        f3.close()
    else:
        f.close()
        f = open('扫雷-小轩-个人信息-20x082j9孑孓3101','r')
        f2 = open('扫雷-小轩-个人信息-20x082j9孑孓3102','r')
        f3 = open('扫雷-小轩-个人信息-20x082j9孑孓3103','r')
        password2 = str(f.read())
        name2 = str(f2.read())
        TEL2 = str(f3.read())
        password = entry1.get()
        name = entry2.get()
        TEL = entry3.get()
        if password2 != password or name2 != name or TEL2 != TEL:
            label1['text'] = "个人信息与上一次填写的不同，所以被更改"
            f.close()
            f2.close()
            f3.close()
            f = open('扫雷-小轩-个人信息-20x082j9孑孓3101','w')
            f2 = open('扫雷-小轩-个人信息-20x082j9孑孓3102','w')
            f3 = open('扫雷-小轩-个人信息-20x082j9孑孓3103','w')
            password = entry1.get()
            name = entry2.get()
            TEL = entry3.get()
            f.write(password)
            f2.write(name)
            f3.write(TEL)
        else:
            label1['text'] = "登陆成功！"
        f.close()
        f2.close()
        f3.close()
        
root = tk.Tk()
root.title("扫雷-填写个人信息-小轩")
root.geometry("550x350")
label1 = tk.Label(root,text="第一条框请输入密码\n第二条框请输入名字\n第三条框请输入手机号（电话号码）哦\n输入完毕后单击按钮‘输入完成’哦\n若您填写错误，请重新填写在按按钮\n若正确，请关闭窗口哦\n若出错，请再点一次按钮哦",fg="blue",font=("微软雅黑", 10))
entry1 = tk.Entry(root,bd=7,text="")
entry2 = tk.Entry(root,bd=7,text="")
entry3 = tk.Entry(root,bd=7,text="")
button1 = tk.Button(root,text="\n\n        我已经输入完成        \n\n",command=main_loop)
label1.pack()
entry1.pack()
entry2.pack()
entry3.pack()
button1.pack()
root.protocol("WM_DELETE_WINDOW",callback)
root.mainloop()


while True:       #mainloop
    if ButtonOption == 0:
        screen = pygame.display.set_mode((1000,800))
        pygame.display.set_caption('扫雷-大厅-小轩')
        def textRender(text,poses,screen,font=font,BLACK=BLACK):
            myText = font.render(text,True,BLACK)
            screen.blit(myText,poses)
        rect1 = pygame.Rect(23*25/2+25,75*1,75,25)
        rect2 = pygame.Rect(0,75*2,75,25)
        rect3 = pygame.Rect(23*25/2+25,75*3,75,25)
        rect4 = pygame.Rect(0,75*4,75,25)
        rect5 = pygame.Rect(23*25/2+25,75*5,75,25)
        rect6 = pygame.Rect(0,75*6,75,25)
        rect7 = pygame.Rect(23*25/2+25,75*7,75,25)
        while ButtonOption == 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('谢谢使用！')
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if rect1.collidepoint(event.pos):
                        print('小  白')
                        ButtonOption = 2
                    elif rect2.collidepoint(event.pos):
                        print('入  门')
                        ButtonOption = 3
                    elif rect3.collidepoint(event.pos):
                        print('初  级')
                        ButtonOption = 4
                    elif rect4.collidepoint(event.pos):
                        print('中  级')
                        ButtonOption = 5
                    elif rect5.collidepoint(event.pos):
                        print('高  级')
                        ButtonOption = 6
                    elif rect6.collidepoint(event.pos):
                        print('王  者')
                        ButtonOption = 7
                    elif rect7.collidepoint(event.pos):
                        print('自定义')
                        ButtonOption = 1
            
            screen.fill((230,245,255))
            textRender('扫雷-大厅-小轩',(325,0),screen)
            textRender('                        小  白',(0,75*1),screen)
            textRender('入  门',(0,75*2),screen)
            textRender('                        初  级',(0,75*3),screen)
            textRender('中  级',(0,75*4),screen)
            textRender('                        高  级',(0,75*5),screen)
            textRender('王  者',(0,75*6),screen)
            textRender('                        自定义',(0,75*7),screen)
            textRender('注意：点击字体即可进入游戏',(50,700),screen)
            pygame.display.update()
            
    # 小轩的雷库
    if ButtonOption == 2:
        lei.running(4,4,3,3,XB,ButtonOption)
        ButtonOption = 0
    elif ButtonOption == 3:
        lei.running(5,5,4,2,RM,ButtonOption)
        ButtonOption = 0
    elif ButtonOption == 4:
        lei.running(8,8,8,3,AJ,ButtonOption)
        ButtonOption = 0
    elif ButtonOption == 5:
        lei.running(10,10,20,5,MJ,ButtonOption)
        ButtonOption = 0
    elif ButtonOption == 6:
        lei.running(15,15,50,10,LJ,ButtonOption)
        ButtonOption = 0
    elif ButtonOption == 7:
        lei.running(30,30,99,10,WZ,ButtonOption)
        ButtonOption = 0
    #大型Party
    elif ButtonOption == 1:
        zdy = 1
        for abc in range(1):
            # wx云界面创造失败，tk云界面创造
            # 棘手的事情：
            # 1.调节退出云界面
            # 2.pygame协调
            # 3.复杂的嵌套与定义
            # 4.讨人厌的global
            # 5.便签创造
            # 6.循环游戏，主循环及py
            # 7.其他
            def callback():
                res=messagebox.askokcancel("退出","您确定要退出吗？")
                if res==True:
                    root.destroy()
                    zdy = 0
                else:
                    return
                
            def add(pygame=pygame,ZDY=ZDY):
                global entry1,entry2,entry3
                GameOverSound = pygame.mixer.Sound('Game over.wav')
                BoomWait = 0
                wwt = entry1.get()
                wht = entry2.get()
                CB_Num = entry3.get()
                chance = entry4.get()
                try:
                    wwt = int(wwt)
                except:
                    label2["text"]='宽度必须为整数哦！'
            
                try:
                    wht = int(wht)
                except:
                    label2["text"]='高度必须为整数哦！'
                    
                try:
                    CB_Num = int(CB_Num)
                except:
                    label2["text"]='雷数必须为整数哦！'
                    
                try:
                    chance = int(chance)
                except:
                    label2["text"]='生命数必须为整数哦！'
                    
                try:
                    if wwt > 350:
                        label2["text"]='宽太长！'
                    elif wwt < 5:
                        label2["text"]='宽太短！'
                    elif wht > 350:
                        label2["text"]='高太长！'
                    elif wht < 5:
                        label2["text"]='高太短！'
                    elif CB_Num > wwt*wht-10:
                        label2["text"]='雷数太多！'
                    elif CB_Num < 5:
                        label2["text"]='雷数太少！'
                    elif chance == 0 or chance >= int(CB_Num/4*3):
                        label2["text"]='生命值设置错误！'
                    else:
                        label2["text"]='输入成功！'
                        # 定义一些变量
                        # 棘手的事情：无
                        screen = pygame.display.set_mode((wwt*30,wht*30))
                        CBoomN = CB_Num
                        a = ['0','0','0','B']
                        BoomList = []
                        myRectList = []
                        myRectList2 = []
                        myRectList3 = []
                        last = wwt*wht
                        # 加入雷
                        # 棘手的事情：嵌套与加雷，循环
                        for i in range(wht):
                            BoomList.append([])
                        for i in BoomList:
                            for j in range(wwt):
                                i.append('0')
                        while True:
                            for i in range(wwt):
                                for j in range(wht):
                                    b = random.choice(a)
                                    if BoomList[i][j] == 'B':
                                        continue
                                    else:
                                        BoomList[i][j] = b
                                        if b == 'B':
                                            BoomWait += 1
                                        if BoomWait > CBoomN:
                                            BoomList[i][j] = '0'
                                            break
                                if BoomWait > CBoomN:
                                    break
                            if BoomWait > CBoomN:
                                BoomWait = 0
                                break
                            
                        # BoomWait变量清零是因为下面要用第二次。
                        # 棘手的事情：分辨雷区
                        for i in range(wwt):
                            lb1 = wwt - 1
                            lb2 = wht - 1
                            for j in range(wht):
                                # 左：j-1 >= 0
                                # 上：i-1 >= 0
                                # 右：j < lb1
                                # 下：i < lb2
                                if BoomList[i][j] != 'B':
                                    if i-1 >= 0 and j-1 >= 0:
                                        if BoomList[i-1][j-1] == 'B':
                                            BoomWait += 1
                                    if i-1 >= 0:
                                        if BoomList[i-1][j] == 'B':
                                            BoomWait += 1
                                    if i-1 >= 0 and j < lb1:
                                        if BoomList[i-1][j+1] == 'B':
                                            BoomWait += 1
                                    if j-1 >= 0:
                                        if BoomList[i][j-1] == 'B':
                                            BoomWait += 1
                                    if j < lb1:
                                        if BoomList[i][j+1] == 'B':
                                            BoomWait += 1
                                    if j-1 >= 0 and i < lb2:
                                        if BoomList[i+1][j-1] == 'B':
                                            BoomWait += 1
                                    if i < lb2:
                                        if BoomList[i+1][j] == 'B':
                                            BoomWait += 1
                                    if i < lb1 and j < lb1:
                                        if BoomList[i+1][j+1] == 'B':
                                            BoomWait += 1
                                    # if 上 and 左:
                                    #     if BoomList[i-1][j-1] == 'B':
                                    #         BoomWait += 1
                                    # if 上:
                                    #     if BoomList[i-1][j] == 'B':
                                    #         BoomWait += 1
                                    # if 上 and 右:
                                    #     if BoomList[i-1][j+1] == 'B':
                                    #         BoomWait += 1
                                    # if 左:
                                    #     if BoomList[i][j-1] == 'B':
                                    #         BoomWait += 1
                                    # if 右:
                                    #     if BoomList[i][j+1] == 'B':
                                    #         BoomWait += 1
                                    # if 左 and 下:
                                    #     if BoomList[i+1][j-1] == 'B':
                                    #         BoomWait += 1
                                    # if 下:
                                    #     if BoomList[i+1][j] == 'B':
                                    #         BoomWait += 1
                                    # if 右 and 下:
                                    #     if BoomList[i+1][j+1] == 'B':
                                    #         BoomWait += 1
                                    BoomList[i][j] = str(BoomWait)
                                    BoomWait = 0
                                    
                        # 标志
                        # 棘手的事情：对应雷数与未点击，以及设置矩形Rect。
                        for i in range(wwt):
                            myRectList.append([])
                            myRectList2.append([])
                            myRectList3.append([])
                            for j in range(wht):
                                if BoomList[i][j] == '0':
                                    cimg = pygame.image.load('0雷.png')
                                    cimgs = pygame.transform.scale(cimg,(30,30))
                                    cRect = pygame.Rect(i*30,j*30,30,30)
                                    myRect = pygame.Rect(i*30,j*30,30,30)
                                    myRectList[i].append(myRect)
                                    myRectList2[i].append(cimgs)
                                    myRectList3[i].append(cRect)
                                elif BoomList[i][j] == '1':
                                    cimg = pygame.image.load('1雷.png')
                                    cimgs = pygame.transform.scale(cimg,(30,30))
                                    cRect = pygame.Rect(i*30,j*30,30,30)
                                    myRect = pygame.Rect(i*30,j*30,30,30)
                                    myRectList[i].append(myRect)
                                    myRectList2[i].append(cimgs)
                                    myRectList3[i].append(cRect)
                                elif BoomList[i][j] == '2':
                                    cimg = pygame.image.load('2雷.png')
                                    cimgs = pygame.transform.scale(cimg,(30,30))
                                    cRect = pygame.Rect(i*30,j*30,30,30)
                                    myRect = pygame.Rect(i*30,j*30,30,30)
                                    myRectList[i].append(myRect)
                                    myRectList2[i].append(cimgs)
                                    myRectList3[i].append(cRect)
                                elif BoomList[i][j] == '3':
                                    cimg = pygame.image.load('3雷.png')
                                    cimgs = pygame.transform.scale(cimg,(30,30))
                                    cRect = pygame.Rect(i*30,j*30,30,30)
                                    myRect = pygame.Rect(i*30,j*30,30,30)
                                    myRectList[i].append(myRect)
                                    myRectList2[i].append(cimgs)
                                    myRectList3[i].append(cRect)
                                elif BoomList[i][j] == '4':
                                    cimg = pygame.image.load('4雷.png')
                                    cimgs = pygame.transform.scale(cimg,(30,30))
                                    cRect = pygame.Rect(i*30,j*30,30,30)
                                    myRect = pygame.Rect(i*30,j*30,30,30)
                                    myRectList[i].append(myRect)
                                    myRectList2[i].append(cimgs)
                                    myRectList3[i].append(cRect)
                                elif BoomList[i][j] == '5':
                                    cimg = pygame.image.load('5雷.png')
                                    cimgs = pygame.transform.scale(cimg,(30,30))
                                    cRect = pygame.Rect(i*30,j*30,30,30)
                                    myRect = pygame.Rect(i*30,j*30,30,30)
                                    myRectList[i].append(myRect)
                                    myRectList2[i].append(cimgs)
                                    myRectList3[i].append(cRect)
                                elif BoomList[i][j] == '6':
                                    cimg = pygame.image.load('6雷.png')
                                    cimgs = pygame.transform.scale(cimg,(30,30))
                                    cRect = pygame.Rect(i*30,j*30,30,30)
                                    myRect = pygame.Rect(i*30,j*30,30,30)
                                    myRectList[i].append(myRect)
                                    myRectList2[i].append(cimgs)
                                    myRectList3[i].append(cRect)
                                elif BoomList[i][j] == '7':
                                    cimg = pygame.image.load('7雷.png')
                                    cimgs = pygame.transform.scale(cimg,(30,30))
                                    cRect = pygame.Rect(i*30,j*30,30,30)
                                    myRect = pygame.Rect(i*30,j*30,30,30)
                                    myRectList[i].append(myRect)
                                    myRectList2[i].append(cimgs)
                                    myRectList3[i].append(cRect)
                                elif BoomList[i][j] == '8':
                                    cimg = pygame.image.load('8雷.png')
                                    cimgs = pygame.transform.scale(cimg,(30,30))
                                    cRect = pygame.Rect(i*30,j*30,30,30)
                                    myRect = pygame.Rect(i*30,j*30,30,30)
                                    myRectList[i].append(myRect)
                                    myRectList2[i].append(cimgs)
                                    myRectList3[i].append(cRect)
                                elif BoomList[i][j] == 'B':
                                    cimg = pygame.image.load('地雷.png')
                                    cimgs = pygame.transform.scale(cimg,(30,30))
                                    cRect = pygame.Rect(i*30,j*30,30,30)
                                    myRect = pygame.Rect(i*30,j*30,30,30)
                                    myRectList[i].append(myRect)
                                    myRectList2[i].append(cimgs)
                                    myRectList3[i].append(cRect)
                                    
                        BoomWait = 0
                        # 万事俱备，开启while True
                        # 棘手的事情：
                        # 1.鼠标事件
                        # 2.列表检索
                        # 3.层层嵌套
                        # 4.BoomWait再用
                        while BoomWait == 0:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    print('zdy exiting...')
                                    BoomWait = 1
                                    break
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    for i in range(wwt):
                                        for j in range(wht):
                                            try:
                                                if myRectList[i][j].collidepoint(event.pos):
                                                    myRectList[i][j] = ''
                                                    last -= 1
                                                    if last == CBoomN:
                                                        print('Win!')
                                                        ZDY += 1
                                                        print(ZDY)
                                                        zdy = 0
                                                        BoomWait = 1
                                                        pygame.time.delay(2300)
                                                        pygame.quit()
                                                        import pygame
                                                        pygame.init()
                                                    elif BoomList[i][j] == 'B':
                                                        GameOverSound.play()
                                                        print('Boom!')
                                                        chance -= 1
                                                        if chance <= 0:
                                                            zdy = 0
                                                            BoomWait = 1
                                                            pygame.time.delay(2300)
                                                            pygame.quit()
                                                            import pygame
                                                            pygame.init()
                                                    BoomList[i][j] = ''
                                                        
                                            except:
                                                pass
                                            
                                
                            for i in range(wwt):
                                for j in range(wht):
                                    screen.blit(myRectList2[i][j],myRectList3[i][j])
                                    if myRectList[i][j] == '':
                                        continue
                                    else:
                                        pygame.draw.rect(screen,(180,180,180),myRectList[i][j],0)
                                
                            pygame.display.update()
                        
                
                except:
                    pass
                    
            if zdy == 0:
                break
            root = tk.Tk()
            root.title("扫雷-自定义窗口-小轩")
            root.geometry("600x300")
            label1 = tk.Label(root,text="第一条框输入宽（格数）\n第二条框输入高（格数）\n第三条框请输入雷数\n第四条框输入生命数哦\n输入完毕后单击按钮‘输入完成’哦",fg="green",font=("楷体", 13))
            entry1 = tk.Entry(root,bd=5,text="")
            entry2 = tk.Entry(root,bd=5,text="")
            entry3 = tk.Entry(root,bd=5,text="")
            entry4 = tk.Entry(root,bd=5,text="")
            button1 = tk.Button(root,text="       我已经输入完成       ",command=add)
            button2 = tk.Button(root,text="       退出扫雷自定义       ",command=callback)
            label2 = tk.Label(root,text="",fg="red")
            label1.pack()
            entry1.pack()
            entry2.pack()
            entry3.pack()
            entry4.pack()
            button1.pack()
            button2.pack()
            label2.pack()
            root.protocol("WM_DELETE_WINDOW",callback)
            root.mainloop()
        
        #     # ---------------------------wx----------------------------------------------------
        #     class MyFrame(wx.Frame):
        #         def __init__(self):
        #             super().__init__(parent=None,title='扫雷-自定义窗口',size=(600,200))
        #             self.Centre()
        #             panel = wx.Panel(self)
        #             hbox = wx.BoxSizer(wx.HORIZONTAL)
        #             vbox = wx.BoxSizer(wx.VERTICAL)
                    
        #             fgs = wx.FlexGridSizer(3,2,10,10)
                    
        #             wght = wx.StaticText(panel,label = '扫雷窗口的宽度(格数):')
        #             hght = wx.StaticText(panel,label = '扫雷窗口的高度(格数):')
        #             CmBoomNumber = wx.StaticText(panel,label = '扫雷雷数:')
        #             self.canWx = 0
        #             self.tc1 = wx.TextCtrl(panel)
        #             self.tc2 = wx.TextCtrl(panel)
        #             self.tc3 = wx.TextCtrl(panel)
        #             self.tc1.SetValue('请删除这行的内容，填上整数')
        #             self.tc2.SetValue('请删除这行的内容，填上整数')
        #             self.tc3.SetValue('请删除这行的内容，填上整数哦')
                    
        #             self.statictext = wx.StaticText(panel,label='扫雷自定义界面',style = wx.ALIGN_TOP)
        #             self.statictext.SetForegroundColour(wx.RED)
        #             OK_buttonMoution = wx.Button(panel,label = 'OK')
        #             self.Bind(wx.EVT_BUTTON,self.on_click,OK_buttonMoution)
                    
        #             fgs.AddMany([
        #                 wght,(self.tc1,1,wx.EXPAND),
        #                 hght,(self.tc2,1,wx.EXPAND),
        #                 CmBoomNumber,(self.tc3,1,wx.EXPAND)])
        #             fgs.AddGrowableRow(0,1)
        #             fgs.AddGrowableRow(1,1)
        #             fgs.AddGrowableRow(2,1)
        #             fgs.AddGrowableCol(0,4)
        #             fgs.AddGrowableCol(1,1)
                    
        #             vbox.Add(OK_buttonMoution,proportion=1,flag=wx.CENTER | wx.EXPAND)
        #             hbox.Add(100,10,proportion=1,flag=wx.TOP | wx.FIXED_MINSIZE)
        #             hbox.Add(self.statictext,proportion=1,flag=wx.TOP | wx.FIXED_MINSIZE)
        #             hbox.Add(fgs,proportion=2,flag=wx.ALL | wx.EXPAND,border = 15)
        #             vbox.Add(hbox,proportion=5,flag=wx.EXPAND)
        #             panel.SetSizer(vbox)
        #         #------------------init结束---------------------------------------------------
                    
                    
        #         def on_click(self,event):
        #             # ------------------判断-----------------------------------------------------
        #             wwt = self.tc1.GetValue()
        #             wht = self.tc2.GetValue()
        #             CB_Num = self.tc3.GetValue()
        #             try:
        #                 wwt = int(wwt)
        #             except:
        #                 self.statictext.SetLabelText('宽度必须为整数哦！')
        #                 self.canWx = 0
        
        #             try:
        #                 wht = int(wht)
        #             except:
        #                 self.statictext.SetLabelText('高度必须为整数哦！')
        #                 self.canWx = 0
                        
        #             try:
        #                 CB_Num = int(CB_Num)
        #             except:
        #                 self.statictext.SetLabelText('雷数必须为整数哦！')
        #                 self.canWx = 0
                        
        #             try:
        #                 if wwt > 350:
        #                     self.statictext.SetLabelText('宽太长！')
        #                     self.canWx = 0
        #                 elif wwt < 5:
        #                     self.statictext.SetLabelText('宽太短！')
        #                     self.canWx = 0
        #                 elif wht > 350:
        #                     self.statictext.SetLabelText('高太长！')
        #                     self.canWx = 0
        #                 elif wht < 5:
        #                     self.statictext.SetLabelText('高太短！')
        #                     self.canWx = 0
        #                 elif CB_Num > wwt*wht-10:
        #                     self.statictext.SetLabelText('雷数太多！')
        #                     self.canWx = 0
        #                 elif CB_Num < 5:
        #                     self.statictext.SetLabelText('雷数太少！')
        #                     self.canWx = 0
        #                 else:
        #                     self.statictext.SetLabelText('输入成功，关闭窗口以激活游戏！')
        #                     self.canWx = 1
        #             except:
        #                 pass
        #             # ------------------------------判断后---------------------------------------
        
        #     class App(wx.App):
        #         def OnInit(self):
        #             frame = MyFrame()
        #             frame.Show()
        #             return True
        #         def OnExit(self):
        #             return 0
                    
        #     if __name__ == '__main__':
        #         app = App()
        #         app.MainLoop()
        #     # ----------------------------------wx结束------------------------------------------
        #     if canWx != 1:
        #         break
        #     pygame.init()
        #     screen = pygame.display.set_mode(wwt*10,wht*10)
        #     CBoomN = CB_Num
        #     a = [0,0,'B']
        #     BoomList = []
        #     for i in range(wht):
        #         BoomList.append([])
        #     for i in BoomList:
        #         for j in range(wwt):
        #             i.append('0')
        #     for i in BoomList:
        #         pass
        #     print(BoomList)
        
        
        
        
        
        
