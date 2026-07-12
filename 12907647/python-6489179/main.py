import pygame,sys,pickle,tkinter as tk,tkinter.messagebox,json,re,requests
from time import *;from urllib import *
pygame.init()
screen = pygame.display.set_mode((1300,800))
pygame.display.set_caption("小轩A字聊天器")

LKimg = pygame.image.load("聊天区.png")
LKrect = LKimg.get_rect()
Ximg = pygame.image.load("小轩.png")
Xrect = Ximg.get_rect()
X2img = pygame.image.load("小A机器人.png")
X2rect = X2img.get_rect()
Fimg = pygame.image.load("我要发言.png")
Frect = Fimg.get_rect()
Limg = pygame.image.load("聊天记录.png")
Lrect = Limg.get_rect()
interval_bar_rect = pygame.Rect(385, 0, 25, 800)
interval_bar_rect2 = pygame.Rect(350, 0, 25, 800)
small_instructions_box = pygame.Rect(350, 0, 25, 25)
small_instructions_box2 = pygame.Rect(0, 0, 15, 15)
LKrect.x = 450
Frect.x = 500
Frect.y = 650
Lrect.x = 750
Lrect.y = 650
X2rect.y = 80 + 5
bigTextList = []
textList = []
bigTextDict = {}
textDict = {}
myClock = pygame.time.Clock()
flag = 0
state = '小轩'

try:import ntpath             # 检测系统
except:osingxing = 'MacOs';font = pygame.font.SysFont('kaittf', 20)
else:osingxing = 'Windows';font = pygame.font.SysFont('kaiti', 20);del ntpath

window=tk.Tk()
window.title('欢迎进入小轩登陆')
window.geometry('450x300')
canvas=tk.Canvas(window,height=300,width=500)
canvas.pack(side='top')
tk.Label(window,text='用户名:').place(x=100,y=150)
tk.Label(window,text='密码:').place(x=100,y=190)
var_usr_name=tk.StringVar()
entry_usr_name=tk.Entry(window,textvariable=var_usr_name)
entry_usr_name.place(x=160,y=150)
var_usr_pwd=tk.StringVar()
entry_usr_pwd=tk.Entry(window,textvariable=var_usr_pwd,show='·')
entry_usr_pwd.place(x=160,y=190)
def usr_log_in():
    usr_name=var_usr_name.get()
    usr_pwd=var_usr_pwd.get()
    try:
        with open('xx.usr_info.pickle','rb') as usr_file:
            usrs_info=pickle.load(usr_file)
    except FileNotFoundError:
        with open('xx.usr_info.pickle','ab') as usr_file:
            usrs_info={'admin':'admin'}
            pickle.dump(usrs_info,usr_file)
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tk.messagebox.showinfo(title='welcome',
                                   message='欢迎登陆呀：'+usr_name)
        else:
            tk.messagebox.showerror(message='密码错误!再试试吧')
    elif usr_name=='' or usr_pwd=='' :
        tk.messagebox.showerror(message='用户名或密码为空咯')
    else:
        is_signup=tk.messagebox.askyesno('欢迎','您还没有注册，是否现在注册')
        if is_signup:
            usr_sign_up()
def usr_sign_up():
    def signtowcg():
        nn=new_name.get()
        np=new_pwd.get()
        npf=new_pwd_confirm.get()
        try:
            with open('xx.usr_info.pickle','rb') as usr_file:
                exist_usr_info=pickle.load(usr_file)
        except FileNotFoundError:
            exist_usr_info={}           
        if nn in exist_usr_info:
            tk.messagebox.showerror('错误','用户名已存在咯')
        elif np =='' or nn=='':
            tk.messagebox.showerror('错误','用户名或密码为空了')
        elif np !=npf:
            tk.messagebox.showerror('错误','密码前后不一致呀')
        else:
            exist_usr_info[nn]=np
            with open('xx.usr_info.pickle','wb') as usr_file:
                pickle.dump(exist_usr_info,usr_file)
            tk.messagebox.showinfo('欢迎你','注册成功')
            window_sign_up.destroy()
    window_sign_up=tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('注册')
    new_name=tk.StringVar()
    tk.Label(window_sign_up,text='用户名：').place(x=10,y=10)
    tk.Entry(window_sign_up,textvariable=new_name).place(x=150,y=10)
    new_pwd=tk.StringVar()
    tk.Label(window_sign_up,text='请输入密码：').place(x=10,y=50)
    tk.Entry(window_sign_up,textvariable=new_pwd,show='·').place(x=150,y=50)    
    new_pwd_confirm=tk.StringVar()
    tk.Label(window_sign_up,text='请再次输入密码：').place(x=10,y=90)
    tk.Entry(window_sign_up,textvariable=new_pwd_confirm,show='·').place(x=150,y=90)    
    bt_confirm_sign_up=tk.Button(window_sign_up,text='确认注册',
                                 command=signtowcg)
    bt_confirm_sign_up.place(x=150,y=130)
def usr_sign_quit():
    window.destroy()
bt_login=tk.Button(window,text='登录',command=usr_log_in)
bt_login.place(x=140,y=230)
bt_logup=tk.Button(window,text='注册',command=usr_sign_up)
bt_logup.place(x=210,y=230)
bt_logquit=tk.Button(window,text='退出',command=usr_sign_quit)
bt_logquit.place(x=280,y=230)
window.mainloop()
del tkinter
from tkinter import *



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    for i in range(256):
        screen.fill((i,0,0))
        sleep(0.005)
        pygame.display.update()
    for i in range(256):
        screen.fill((255,i,0))
        sleep(0.005)
        pygame.display.update()
    for i in range(256):
        screen.fill((255-i,255,0))
        sleep(0.005)
        pygame.display.update()
    for i in range(256):
        screen.fill((0,255,i))
        sleep(0.005)
        pygame.display.update()
    for i in range(256):
        screen.fill((0,255-i,255))
        sleep(0.005)
        pygame.display.update()
    for i in range(256):
        screen.fill((0,0,255-i))
        sleep(0.005)
        pygame.display.update()
    break





while True:
    while flag == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Frect.collidepoint(event.pos):
                    flag = 1
                    break
                elif Lrect.collidepoint(event.pos):
                    if state == '小轩':
                        for i in textList:
                            print(i)
                            sleep(0.04)
                    elif state == '小A机器人':
                        for i in bigTextDict:
                            print(i,bigTextDict[i])
                elif Xrect.collidepoint(event.pos):
                    state = '小轩'
                elif X2rect.collidepoint(event.pos):
                    state = '小A机器人'
            elif event.type == pygame.MOUSEMOTION:
                small_instructions_box2.center = event.pos
        pygame.mouse.set_visible(False)
        screen.fill((229,236,255))
        screen.blit(LKimg,LKrect)
        screen.blit(Ximg,Xrect)
        screen.blit(X2img,X2rect)
        screen.blit(Fimg,Frect)
        screen.blit(Limg,Lrect)
        screen.blit(font.render('[聊天记录将在终端输出]',True,(0,0,0)),(900,775))
        screen.blit(font.render('[请按下按钮‘聊天记录’以在终端输出并详细得知]', True, (0,0,0)),(420,775))
        pygame.draw.rect(screen, (253,5,255), interval_bar_rect, 0)
        pygame.draw.rect(screen, (5,255,255), interval_bar_rect2, 0)
        pygame.draw.rect(screen, (0,75,89), small_instructions_box, 0)
        pygame.draw.rect(screen, (14,185,245), small_instructions_box2, 0)
        screen.blit(font.render('A',True,(0,0,0)),(small_instructions_box2.x+3,small_instructions_box2.y-2))
        
        if state == '小轩':
            small_instructions_box.y = Xrect.y
            try:
                if len(textList) >= 20:
                    textList.remove(textList[0])
                for i in range(len(textList)):
                    screen.blit(font.render('我：'+textList[i], True, (0,0,0)),(1300-len(myWord)*20-140,150+i*21))
            except:
                pass
        elif state == '小A机器人':
            small_instructions_box.y = X2rect.y
            try:
                x = 0
                for i in textDict:
                    x += 1
                    if len(textDict) >= 10:
                        del textDict[i]
                    screen.blit(font.render('我：'+i, True, (0,0,0)),(1300-len(myWord)*20-140,150+x*84))
                    screen.blit(font.render('小A：'+textDict[i], True, (0,0,0)),(1290-len(Aword)*20-140,150+x*(84*1.5)))
            except:
                pass
        pygame.display.update()
        myClock.tick(65)
    while flag == 1:
        root = Tk()
        root.title('发送短信|A|')
        root.geometry('450x225')
        resS = StringVar()
        entry = Entry(root,font=('微软雅黑',15),textvariable = resS,bd = 5)
        button = Button(root,text='发送短信',width='25',command=root.quit)
        resS.set('请输入内容')
        entry.pack()
        button.pack()
        root.mainloop()
        try:
            if state == '小轩':
                myWord = entry.get()
                textList.append(myWord)
                bigTextList.append(myWord)
            elif state == '小A机器人':
                myWord = entry.get()
                if ('再见' in myWord)or('拜拜' in myWord)or('下次见' in myWord)or('886' in myWord):
                    Aword = '好的，'+myWord+'！'
                else:
                    x = parse.quote(myWord)
                    link = request.urlopen("http://nlp.xiaoi.com/robot/webrobot?&callback=__webrobot_processMsg&data=%7B%22sessionId%22%3A%22ff725c236e5245a3ac825b2dd88a7501%22%2C%22robotId%22%3A%22webbot%22%2C%22userId%22%3A%227cd29df3450745fbbdcf1a462e6c58e6%22%2C%22body%22%3A%7B%22content%22%3A%22"+x+"%22%7D%2C%22type%22%3A%22txt%22%7D")
                    html_doc = link.read().decode()
                    reply = re.findall(r'\"content\":\"(.+?)\\r\\n\"', html_doc)
                    Aword = reply[-1]
                textDict[myWord] = Aword
                bigTextDict[myWord] = Aword
        except:
            pass
        flag = 0