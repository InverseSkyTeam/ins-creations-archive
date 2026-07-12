#导库
try:
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
except ModuleNotFoundError:
    print("请安装easygui和pgzrun")

stf = os.getcwd() + "\\登陆.html"
stf2 = os.getcwd() + "\\aa.vbs"
stf3 = os.getcwd() + "\\main（带图标移动）.py"
stf4 = os.getcwd() + "\\com_new.py"
stf5 = os.getcwd() + "\\calc.py"
stf6 = os.getcwd() + "\\com.py"
stf7 = os.getcwd() + "\\calc_old.py"
stf8 = os.getcwd() + "\\images\\hh.png"
WIDTH = 1000
HEIGHT = 916
#为键盘检测做准备
xmm = True
lj = 1
lb = 1
lp = 1
os.chdir("E:\\")

def com_main():
    comm = buttonbox(msg="你要旧版还是新版？",title="提示",choices=("新","旧"))
    if comm == "新":
        os.system(stf4)
    if comm == "旧":
        os.system(stf6)
def jt_main():
    os.system("C:\\Windows\\System32\\SnippingTool.exe")

def sj_main():
    msgbox("现在时间："+strftime("%H:%M:%S"))

def wz_main():
    os.startfile(stf)

def cmd_main():
    os.startfile("C:\\Windows\\System32\\cmd.exe")
    #msgbox("此功能已被禁用")

def ll_main():
    web.open("https://www.baidu.com/")

def js_main():
    jss = buttonbox(msg="你要旧版还是新版？",title="提示",choices=("新","旧"))
    if jss == "新":
        os.system(stf5)
    if jss == "旧":
        os.system(stf7)
    #os.system(stf5)

def hs_main():
    os.startfile(stf2)

def ht_main():
    os.system('C:\\Windows\\System32\\mspaint.exe')

def a():
    msgbox("无")

def py():
    global lp
    f = open("E:\\新建Pyhon文件("+str(lp)+").py","w")
    f.close()
    lp = lp + 1
    msgbox("已把文件保存至E盘")

def wj():
    global lj
    x = str(lj)
    os.mkdir(x)
    lj = lj + 1
    msgbox("已把文件保存至E盘")

def wb():
    global lb
    f = open("E:\\新建文本文档("+str(lb)+").txt","w")
    f.close()
    lb = lb + 1
    msgbox("已把文件保存至E盘")

a = buttonbox(msg="此代码不带图标拖动，要图标拖动吗？(图标拖动版已经很久没更新了)",title="提示",choices=("要","不要"))
if a == "要":
    os.startfile(stf3)
    sys.exit()
else:
    multpasswordbox(msg='请输入用户名和密码：',title='登陆',fields=("用户名：","密码"))
    su = buttonbox("注:右键和B键的功能是一样的",image=stf8,choices=("继续","继续"))
    if su == stf8:
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
            global xmm
            global aaa
            if button == mouse.RIGHT:
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
                    Button(root1,text="打开",command=com_main).pack()
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
                    comm = buttonbox(msg="你要旧版还是新版？",title="提示",choices=("新","旧"))
                    if comm == "新":
                        os.system(stf4)
                    if comm == "旧":
                        os.system(stf6)
                if ht.collidepoint(pos):
                    os.system('C:\\Windows\\System32\\mspaint.exe')
                if hs.collidepoint(pos):
                    os.startfile(stf2)
                if js.collidepoint(pos):
                    jss = buttonbox(msg="你要旧版还是新版？",title="提示",choices=("新","旧"))
                    if jss == "新":
                        os.system(stf5)
                    if jss == "旧":
                        os.system(stf7)
                    #os.system('C:\\Windows\\System32\\calc.exe')
                if ll.collidepoint(pos):
                    web.open("https://www.baidu.com/")
                if cmd.collidepoint(pos):
                    os.startfile("C:\\Windows\\System32\\cmd.exe")
                if wz.collidepoint(pos):
                    os.startfile(stf)
                if sj.collidepoint(pos):
                    msgbox("现在时间："+strftime("%H:%M:%S"))
                if jt.collidepoint(pos):
                    os.system("C:\\Windows\\System32\\SnippingTool.exe")
                if gj.collidepoint(pos):
                    w = Tk()
                    gjj = askokcancel(title="",message="确定关机吗",parent=w)
                    if gjj == True:
                        sys.exit()
                    else:
                        pass
                if xm.collidepoint(pos):
                    time.sleep(5)
                    xmm = False
                if td.collidepoint(pos):
                    xmm = True

        go()
