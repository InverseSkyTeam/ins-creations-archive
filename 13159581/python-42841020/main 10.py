#导库
from pgzrun import *
from easygui import *
from tkinter import *
from tkinter.messagebox import *
import os
import com
import webbrowser as web
root = Tk()
WIDTH = 1000
HEIGHT = 916
#为键盘检测做准备
pic = ""
lj = 1
lb = 1
lp = 1
os.chdir("E:\\")
def py():
    global lp
    f = open("C:\\Users\\Administrator\\Desktop\\新建Pyhon文件("+str(lp)+").py","w")
    f.close()
    lp = lp + 1
def wj():
    global lj
    x = str(lj)
    os.mkdir(x)
    lj = lj + 1
    msgbox("已把文件保存至E盘")

def wb():
    global lb
    f = open("C:\\Users\\Administrator\\Desktop\\新建文本文档("+str(lb)+").txt","w")
    f.close()
    lb = lb + 1
su = buttonbox("注:这个系统的右键被换成了b键",image="hh.png",choices=("继续","继续"))
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
    #绘制
    def draw():
        bg.draw()
        computer.draw()
        ht.draw()
        hs.draw()
        js.draw()
        ll.draw()
        cmd.draw()

    #鼠标与键盘的检测
    def on_key_down():
        if keyboard.b == True:
            root.config(menu=chen)
            root.mainloop()
    #-------------------------------------------#
    def on_mouse_down(pos):
        global pic
        if computer.collidepoint(pos):
            pic = computer
            com.a_main()
        if ht.collidepoint(pos):
            pic = ht
            w = Canvas(root,width=400,height=200)
            w.pack()
            def paint(event):
                x1,y1 = (event.x - 1),(event.y - 1)
                x2,y2 = (event.x + 1),(event.y + 1)
                w.create_oval(x1,y1,x2,y2,fill="black")
            w.bind("<B1-Motion>",paint)
            Label(root,text="开始画图吧!").pack(side=BOTTOM)
            Button(root,text="删除全部",command=(lambda x=ALL:w.delete(x))).pack()
            mainloop()
        if hs.collidepoint(pos):
            pic = hs
            showerror("正在优化中","正在优化中")
        if js.collidepoint(pos):
            pic = js
            os.system("calc")
        if ll.collidepoint(pos):
            pic = ll
            web.open("https://www.baidu.com/")
        if cmd.collidepoint(pos):
            pic = cmd
            os.system('cmd')
    #------------------------------------------#
    def on_mouse_move(pos):
        global pic
        if pic != "":
            pic.pos = pos
    def on_mouse_up(pos):
        global pic
        pic = ""

    go()
