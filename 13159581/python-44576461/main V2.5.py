#导库
from pgzrun import *
from easygui import *
from tkinter.messagebox import *
from tkinter import *
import os
#import com
import webbrowser as web
from time import *
import sys
import time
import PIL
#import hs
from random import *
#----------------------------------------------------------------------#
choices = ["a","b"]
stf = os.getcwd() + "\\登陆.html"
stf2 = os.getcwd() + "\\dmy.html"
stf3 = os.getcwd() + "\\main（带图标移动）.py"
stf4 = os.getcwd() + "\\com_new.py"
stf5 = os.getcwd() + "\\calc.py"
stf6 = os.getcwd() + "\\com.py"
stf7 = os.getcwd() + "\\calc_old.py"
stf8 = os.getcwd() + "\\images\\hh.png"
stf9 = os.getcwd() + "\\日记本.py"
stf10 = os.getcwd() + "\\二维码生成器.py"
stf11 = os.getcwd() + "\\python代码编辑器.py"
stf12 = os.getcwd() + "\\红包雨.py"
stf13 = os.getcwd() + "\\hs.py"
delcom = False
deljt = False
delht = False
delhs = False
deljs = False
delll = False
delcmd = False
delwz = False
delsj = False
deljsb = False
delewm = False
deldm = False
#----------------------------------------------------------------------#
f = open(".\\关机次数.txt","r")
gjcs = int(f.read())
f.close()
#----------------------------------------------------------------------#
f = open(".\\账号.txt", "a")
while True:
    a = buttonbox("你要注册还是登陆",choices=["登陆","注册","退出"])
    if a == "登陆":
        x = open(".\\账号.txt","r")
        if x.read() == "":
            msgbox("请先注册!!!")
        else:
            b = multpasswordbox(msg="请输入用户名与密码",fields=["用户名：","密码："])
            d = open(".\\账号.txt","r")
            if str(b) == d.read():
                msgbox("登陆成功!!")
                break
            else:
                msgbox("密码错误")
    if a == "退出":
        sys.exit()
    if a == "注册":
        y = open(".\\账号.txt","r")
        if y.read() != "":
            msgbox("本程序仅可注册一个账号")
        else:
            c = multpasswordbox(msg="请输入用户名与密码",fields=["用户名：","密码："])
            z = open(".\\账号.txt","a")
            z.write(str(c))
            z.close()
#----------------------------------------------------------------------#
WIDTH = 1000
HEIGHT = 600
#为键盘检测做准备
xmm = True
lj = 1
lb = 1
lp = 1
#---------------------------------------------------------------------#
def hfdel():
    global delcom
    global deljt
    global delht
    global delhs
    global deljs
    global delll
    global delcmd
    global delwz
    global delsj
    global deljsb
    global delewm
    global deldm
    delcom = False
    deljt = False
    delht = False
    delhs = False
    deljs = False
    delll = False
    delcmd = False
    delwz = False
    delsj = False
    deljsb = False
    delewm = False
    deldm = False

def com_main():
    comm = buttonbox(msg="你要旧版还是新版？",title="提示",choices=("新","旧"))
    if comm == "新":
        os.system(stf4)
    if comm == "旧":
        os.system(stf6)
def com_del():
    global delcom
    delcom = True

def jt_main():
    os.system("C:\\Windows\\System32\\SnippingTool.exe")
def jt_del():
    global deljt
    deljt = True

def sj_main():
    msgbox("现在时间："+strftime("%H:%M:%S"))

def wz_main():
    os.startfile(stf)

def cmd_main():
    os.startfile("C:\\Windows\\System32\\cmd.exe")
def cmd_del():
    global delcmd
    delcmd = True

def ll_main():
    web.open("https://www.baidu.com/")
def ll_del():
    global delll
    delll = True

def js_main():
    jss = buttonbox(msg="你要旧版还是新版？",title="提示",choices=("新","旧"))
    if jss == "新":
        os.system(stf5)
    if jss == "旧":
        os.system(stf7)
    #os.system(stf5)
def js_del():
    global deljs
    deljs = True

def hs_main():
    os.startfile(stf2)
def hs_del():
    global delhs
    delhs = True

def ht_main():
    os.system('C:\\Windows\\System32\\mspaint.exe')
def ht_del():
    global delht
    delht = True

def wz_del():
    global delwz
    delwz = True

def sj_del():
    global delsj
    delsj = True

def jsb_main():
    os.startfile(stf9)
def jsb_del():
    global deljsb
    deljsb = True

def ewm_main():
    os.startfile(stf10)
def ewm_del():
    global delewm
    delewm = True

def dm_main():
    os.startfile(stf11)
def dm_del():
    global deldm
    deldm = True

def a():
    msgbox("无")

def py():
    global lp
    f = open("C:\\新建Pyhon文件("+str(lp)+").py","w")
    f.close()
    lp = lp + 1
    msgbox("已把文件保存至C盘")

def cd_main():
    f = open(".\\关机次数.txt","r")
    q = f.read()
    f.close()
    print("你关闭此程序的次数是："+q)

def wj():
    global lj
    x = str(lj)
    os.mkdir("C:\\")
    lj = lj + 1
    msgbox("已把文件保存至C盘")

def wb():
    global lb
    f = open("C:\\新建文本文档("+str(lb)+").txt","w")
    f.close()
    lb = lb + 1
    msgbox("已把文件保存至C盘")
#----------------------------------------------------------------------#
a = buttonbox(msg="此代码不带图标拖动，要图标拖动吗？(图标拖动版已经很久没更新了)",title="提示",choices=("要","不要"))
if a == "要":
    os.startfile(stf3)
    sys.exit()
else:
    su = buttonbox("注:右键和B键的功能是一样的",image=stf8,choices=("继续","继续"))
    if su == stf8:
        os.startfile(stf12)
        sys.exit()
    else:
        #角色
        bg = Actor("bg.png",[0,0])
        bg1 = Actor("bg1.png")
        computer = Actor("计算机.png",[50,50])
        ht = Actor("画图.png",[50,150])
        hs = Actor("回收站.png",[50,250])
        js = Actor("计算器.png",[50,350])
        ll = Actor("浏览器.png",[50,450])
        cmd = Actor("cmd.png",[50,550])
        wz = Actor("网站.png",[150,550])
        sj = Actor("时间.png",[150,350])
        jt = Actor("截图.png",[150,450])
        #sj = Actor("时间.png",[250,50])
        jsb = Actor("记事本.png",[150,50])
        gj = Actor("关机.png",[950,25])
        xm = Actor("休眠.png",[950,75])
        td = Actor("td.png",[500,200])
        ewm = Actor("二维码.png",[150,150])
        dm = Actor("代码.png",[150,250])
        cd = Actor("彩蛋.png",[950,125])
        #绘制
        def draw():
            bg.draw()
            if xmm == True:
                if delcom == False:
                    computer.draw()
                if deljt == False:
                    jt.draw()
                if delht == False:
                    ht.draw()
                if delhs == False:
                    hs.draw()
                if deljs == False:
                    js.draw()
                if delll == False:
                    ll.draw()
                if delcmd == False:
                    cmd.draw()
                if delwz == False:
                    wz.draw()
                if delsj == False:
                    sj.draw()
                if deljsb == False:
                    jsb.draw()
                if delewm == False:
                    ewm.draw()
                gj.draw()
                xm.draw()
                if deldm == False:
                    dm.draw()
                cd.draw()
            else:
                bg1.draw()
                td.draw()

        #-------------------------------------------#
        #鼠标与键盘的检测
        def on_key_down():
            if keyboard.b == True:
                root = Tk()
                chen = Menu(root)

                a = Menu(chen,tearoff=True)

                a.add_command(label="文件夹",command=wj)
                a.add_command(label="文本文档",command=wb)
                a.add_separator()
                a.add_command(label="退出",command=root.quit)
                chen.add_cascade(label="创建",menu=a)

                b = Menu(chen,tearoff=True)
                b.add_command(label="Pyhon文件",command=py)
                b.add_command(label="",command=a)
                chen.add_cascade(label="创建",menu=b)
                root.config(menu=chen)

                c = Button(root,text="恢复所有被删除的程序",command=hfdel)
                c.pack()

                root.mainloop()
        #-------------------------------------------#
        #鼠标检测
        def on_mouse_down(pos,button):
            global xmm
            global aaa
            global gjcs
            global choices
            global delcom
            global deljt
            global delht
            #右键检测
            if button == mouse.RIGHT and xmm == True:
                if bg.collidepoint(pos):
                    if computer.collidepoint(pos) and delcom == False:
                        root1 = Tk()
                        Button(root1,text="打开",command=com_main).pack()
                        Button(root1,text="删除",command=com_del).pack()
                        root1.mainloop()
                    elif ht.collidepoint(pos) and delht == False:
                        root2 = Tk()
                        Button(root2,text="打开",command=ht_main).pack()
                        Button(root2,text="删除",command=ht_del).pack()
                        root2.mainloop()
                    elif hs.collidepoint(pos) and delhs == False:
                        root3 = Tk()
                        Button(root3,text="打开",command=hs_main).pack()
                        Button(root3,text="删除",command=hs_del).pack()
                        root3.mainloop()
                    elif js.collidepoint(pos) and deljs == False:
                        root4 = Tk()
                        Button(root4,text="打开",command=js_main).pack()
                        Button(root4,text="删除",command=js_del).pack()
                        root4.mainloop()
                    elif ll.collidepoint(pos) and delll == False:
                        root5 = Tk()
                        Button(root5,text="打开",command=ll_main).pack()
                        Button(root5,text="删除",command=ll_del).pack()
                        root5.mainloop()
                    elif cmd.collidepoint(pos) and delcmd == False:
                        root6 = Tk()
                        Button(root6,text="打开",command=cmd_main).pack()
                        Button(root6,text="删除",command=cmd_del).pack()
                        root6.mainloop()
                    elif wz.collidepoint(pos) and delwz == False:
                        root7 = Tk()
                        Button(root7,text="打开",command=wz_main).pack()
                        Button(root7,text="删除",command=wz_del).pack()
                        root7.mainloop()
                    elif sj.collidepoint(pos) and delsj == False:
                        root8 = Tk()
                        Button(root8,text="打开",command=sj_main).pack()
                        Button(root8,text="删除",command=sj_del).pack()
                        root8.mainloop()
                    elif jt.collidepoint(pos) and deljt == False:
                        root9 = Tk()
                        Button(root9,text="打开",command=jt_main).pack()
                        Button(root9,text="删除",command=jt_del).pack()
                        root9.mainloop()
                    elif jsb.collidepoint(pos) and deljsb == False:
                        root10 = Tk()
                        Button(root10,text="打开",command=jsb_main).pack()
                        Button(root10,text="删除",command=jsb_del).pack()
                        root10.mainloop()
                    elif ewm.collidepoint(pos) and delewm == False:
                        root11 = Tk()
                        Button(root11,text="打开",command=ewm_main).pack()
                        Button(root11,text="删除",command=ewm_del).pack()
                        root11.mainloop()
                    elif cd.collidepoint(pos):
                        root15 = Tk()
                        Button(root15,text="打开",command=cd_main).pack()
                        root15.mainloop()
                    elif gj.collidepoint(pos):
                        pass
                    elif xm.collidepoint(pos):
                        pass
                    elif dm.collidepoint(pos) and deldm == False:
                        root12 = Tk()
                        Button(root12,text="打开",command=dm_main).pack()
                        Button(root12,text="删除",command=dm_del).pack()
                        root12.mainloop()
                    else:
                        root = Tk()
                        chen = Menu(root)

                        a = Menu(chen,tearoff=True)

                        a.add_command(label="文件夹",command=wj)
                        a.add_command(label="文本文档",command=wb)
                        a.add_separator()
                        a.add_command(label="退出",command=root.quit)
                        chen.add_cascade(label="创建",menu=a)

                        b = Menu(chen,tearoff=True)
                        b.add_command(label="Pyhon文件",command=py)
                        b.add_command(label="",command=a)
                        chen.add_cascade(label="创建",menu=b)
                        root.config(menu=chen)

                        c = Button(root,text="恢复所有被删除的程序",command=hfdel)
                        c.pack()

                        root.mainloop()
                
            #左键检测
            if button == mouse.LEFT and xmm == True:
                if computer.collidepoint(pos) and delcom == False:
                    comm = buttonbox(msg="你要旧版还是新版？",title="提示",choices=("新","旧"))
                    if comm == "新":
                        os.system(stf4)
                    if comm == "旧":
                        os.system(stf6)
                if ht.collidepoint(pos) and delht == False:
                    os.system('C:\\Windows\\System32\\mspaint.exe')
                if hs.collidepoint(pos) and delhs == False:
                    os.startfile(stf2)
                if js.collidepoint(pos) and deljs == False:
                    jss = buttonbox(msg="你要旧版还是新版？",title="提示",choices=("新","旧"))
                    if jss == "新":
                        os.system(stf5)
                    if jss == "旧":
                        os.system(stf7)
                if ll.collidepoint(pos) and delll == False:
                    web.open("https://www.baidu.com/")
                if cmd.collidepoint(pos) and delcmd == False:
                    os.startfile("C:\\Windows\\System32\\cmd.exe")
                if wz.collidepoint(pos) and delwz == False:
                    os.startfile(stf)
                if sj.collidepoint(pos) and delsj == False:
                    msgbox("现在时间："+strftime("%H:%M:%S"))
                if jt.collidepoint(pos) and deljt == False:
                    os.system("C:\\Windows\\System32\\SnippingTool.exe")
                if cd.collidepoint(pos):
                    hshs = choice(choices)
                    if hshs == "a":
                        f = open(".\\关机次数.txt","r")
                        q = f.read()
                        f.close()
                        print("你关闭此程序的次数是："+q)
                    elif hshs == "b":
                        os.system(stf13)
                if gj.collidepoint(pos):
                    w = Tk()
                    gjj = askokcancel(title="",message="确定关机吗",parent=w)
                    if gjj == True:
                        gjcs = gjcs+1
                        f = open(".\\关机次数.txt","w")
                        f.write(str(gjcs))
                        f.close()
                        print("tips:有一个彩蛋需要把代码下载到本地运行才可以正常输出(你可能已经发现了)")
                        sys.exit()
                    else:
                        pass
                if xm.collidepoint(pos):
                    xmm = False
                if jsb.collidepoint(pos) and deljsb == False:
                    os.startfile(stf9)
                if ewm.collidepoint(pos) and delewm == False:
                    os.startfile(stf10)
                if dm.collidepoint(pos) and deldm == False:
                    os.startfile(stf11)
            else:
                if td.collidepoint(pos):
                    xmm = True

        go()
