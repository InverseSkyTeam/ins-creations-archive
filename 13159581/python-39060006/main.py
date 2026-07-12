#导库
try:
    from pgzrun import *
    from easygui import *
    from tkinter.messagebox import *
    from tkinter import *
    import os
    import com
    import webbrowser as web
    from time import *
    import sys
except ModuleNotFoundError:
    print("请安装easygui和pgzrun")

stf = os.getcwd() + "\\登陆.html"
stf2 = os.getcwd() + "\\aa.vbs"
WIDTH = 1000
HEIGHT = 916
#为键盘检测做准备
xmm = True
pic = ""
lj = 1
lb = 1
lp = 1
os.chdir("E:\\")

def jt_main():
    os.system("SnippingTool")

def sj_main():
    msgbox("现在时间："+strftime("%H:%M:%S"))

def wz_main():
    os.startfile(stf)

def cmd_main():
    os.system("cmd")

def ll_main():
    web.open("https://www.baidu.com/")

def js_main():
    os.system("calc")

def hs_main():
    os.startfile(stf2)

def ht_main():
    os.system('mspaint')

def a():
    msgbox("无")

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
    msgbox("已把文件保存至E盘")

def wb():
    global lb
    f = open("C:\\新建文本文档("+str(lb)+").txt","w")
    f.close()
    lb = lb + 1
    msgbox("已把文件保存至C盘")

multpasswordbox(msg='请输入用户名和密码：',title='登陆',fields=("用户名：","密码"))
su = buttonbox("注:右键和B键的功能是一样的",image="images//hh.png",choices=("继续","继续"))
if su == "hh.png":
    msgbox("这只是一个bug.......")
else:
    
    #-------------------------------------------------------#
    #角色
    bg = Actor("bg.png",[950,916])
    bg1 = Actor("bg1.png")
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
            root.mainloop()
    #-------------------------------------------#
    def on_mouse_down(pos,button):
        global pic
        global xmm
        global aaa
        if button == mouse.RIGHT and bg.image != "bg1.png":
            if bg.collidepoint(pos):
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
                root.mainloop()
            
            if computer.collidepoint(pos):
                root1 = Tk()
                Button(root1,text="打开",command=com.main).pack()
                root1.mainloop()
            
            if ht.collidepoint(pos):
                root2 = Tk()
                Button(root2,text="打开",command=ht_main).pack()
                root2.mainloop()
            
            if hs.collidepoint(pos):
                root3 = Tk()
                Button(root3,text="打开",command=hs_main).pack()
                root3.mainloop()
            
            if js.collidepoint(pos):
                root4 = Tk()
                Button(root4,text="打开",command=js_main).pack()
                root4.mainloop()
            
            if ll.collidepoint(pos):
                root5 = Tk()
                Button(root5,text="打开",command=ll_main).pack()
                root5.mainloop()
            if cmd.collidepoint(pos):
                root6 = Tk()
                Button(root6,text="打开",command=cmd_main).pack()
                root6.mainloop()
            if wz.collidepoint(pos):
                root7 = Tk()
                Button(root7,text="打开",command=wz_main).pack()
                root7.mainloop()
            if sj.collidepoint(pos):
                root8 = Tk()
                Button(root8,text="打开",command=sj_main).pack()
                root8.mainloop()
            if jt.collidepoint(pos):
                root9 = Tk()
                Button(root9,text="打开",command=jt_main).pack()
                root9.mainloop()
        if button == mouse.LEFT:
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
            if td.collidepoint(pos):
                xmm = True
    #------------------------------------------#
    def on_mouse_move(pos):
        global pic
        if pic != "":
            pic.pos = pos
    #------------------------------------------#
    def on_mouse_up(pos):
        global pic
        pic = ""

    go()
