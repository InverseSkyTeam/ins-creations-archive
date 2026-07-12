#导库
from pgzrun import *
from easygui import *
from tkinter import *
import os
import com
import webbrowser as web

msgbox("注:这个系统的右键被换成了b键")
root = Tk()
WIDTH = 1000
HEIGHT = 916
#为键盘检测做准备
lj = 1
lb = 1
os.chdir("E:\\")
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

menubar = Menu(root)

a = Menu(menubar,tearoff=False)

a.add_command(label="文件夹",command=wj)
a.add_command(label="文本文档",command=wb)
a.add_separator()
a.add_command(label="退出",command=root.quit)
menubar.add_cascade(label="创建",menu=a)

b = Menu(menubar,tearoff=False)
b.add_command(label="",command=wj)
b.add_command(label="",command=wj)
b.add_separator()
b.add_command(label="",command=root.quit)
menubar.add_cascade(label="无",menu=b)

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
        root.config(menu=menubar)
        root.mainloop()
def on_mouse_down(pos):
    if computer.collidepoint(pos):
        com.a_main()
    if ht.collidepoint(pos):
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
        msgbox('正在优化中','正在优化中')
    if js.collidepoint(pos):
        os.system("calc")
    if ll.collidepoint(pos):
        web.open("https://www.baidu.com/")
    if cmd.collidepoint(pos):
        os.system('cmd')

go()
