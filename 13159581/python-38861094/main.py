#导库
from pgzrun import *
from easygui import *
from tkinter.messagebox import *
from tkinter import *
import os
import com
import webbrowser as web
from time import *
import sys

stf = os.getcwd() + "\\登陆.html"
stf2 = os.getcwd() + "\\aa.vbs"
root = Tk()
WIDTH = 1000
HEIGHT = 916
#为键盘检测做准备
xmm = True
pic = ""
lj = 1
lb = 1
lp = 1
os.chdir("C:\\")
def py():
    global lp
    f = open("C:\\新建Pyhon文件("+str(lp)+").py","w")
    f.close()
    lp = lp + 1
    msgbox("已把文件保存至C盘")
def wj():
    global lj
    x = str(lj)
    os.mkdir(x)
    lj = lj + 1
    msgbox("已把文件保存至C盘")

def wb():
    global lb
    f = open("C:\\新建文本文档("+str(lb)+").txt","w")
    f.close()
    lb = lb + 1
    msgbox("已把文件保存至C盘")
multpasswordbox(msg='请输入用户名和密码：',title='登陆',fields=("用户名：","密码"))
su = buttonbox("注:这个系统的右键被换成了b键",image="images//hh.png",choices=("继续","继续"))
if su == "hh.png":
    msgbox("这只是一个bug.......")
else:
    chen = Menu(root)

    a = Menu(chen,tearoff=True)

    a.add_command(label="文件夹",command=wj)
    a.add_command(label="文本文档",command=wb)
    a.add_separator()
    a.add_command(label="退出",command=root.quit)
    chen.add_cascade(label="创建",menu=a)

    b = Menu(chen,tearoff=True)
    b.add_command(label="Pyhon文件",command=py)
    b.add_command(label="",command=print("无"))
    chen.add_cascade(label="创建",menu=b)
    #-------------------------------------------------------#

    #角色
    bg = Actor("bg.png")
    computer = Actor("计算机.png",[50,50])
    ht = Actor("画图.png",[50,150])
    hs = Actor("回收站.png",[50,250])
    js = Actor("计算器.png",[50,350])
    ll = Actor("浏览器.png",[50,450])
    cmd = Actor("cmd.png",[50,550])
    wz = Actor("网站.png",[50,650])
    sj = Actor("时间.png",[50,750])
    jt = Actor("截图.png",[50,850])
    gj = Actor("关机.png",[950,890])
    xm = Actor("休眠.png",[950,850])
    td = Actor("td.png",[500,500])
    #绘制
    def draw():
        bg.draw()
        if xmm == True:
            computer.draw()
            ht.draw()
            hs.draw()
            js.draw()
            ll.draw()
            cmd.draw()
            wz.draw()
            sj.draw()
            jt.draw()
            gj.draw()
            xm.draw()
        else:
            td.draw()

    #鼠标与键盘的检测
    def on_key_down():
        if keyboard.b == True:
            root.config(menu=chen)
            root.mainloop()
    #-------------------------------------------#
    def on_mouse_down(pos):
        global pic
        global xmm
        if computer.collidepoint(pos):
            pic = computer
            com.main()
        if ht.collidepoint(pos):
            pic = ht
            os.system('mspaint')
        if hs.collidepoint(pos):
            pic = hs
            os.startfile(stf2)
        if js.collidepoint(pos):
            pic = js
            os.system('calc')
        if ll.collidepoint(pos):
            pic = ll
            web.open("https://www.baidu.com/")
        if cmd.collidepoint(pos):
            pic = cmd
            os.system('cmd')
        if wz.collidepoint(pos):
            pic = wz
            os.startfile(stf)
        if sj.collidepoint(pos):
            pic = sj
            msgbox("现在时间："+strftime("%H:%M:%S"))
        if jt.collidepoint(pos):
            pic = jt
            os.system("SnippingTool")
        if gj.collidepoint(pos):
            sys.exit()
        if xm.collidepoint(pos):
            xmm = False
            bg.image = "bg1.png"
        if td.collidepoint(pos):
            xmm = True
            bg.image = "bg.png"
    #------------------------------------------#
    def on_mouse_move(pos):
        global pic
        if pic != "":
            pic.pos = pos
    def on_mouse_up(pos):
        global pic
        pic = ""

    go()
