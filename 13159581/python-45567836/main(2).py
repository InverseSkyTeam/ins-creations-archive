try:
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
    from pickle import *
    #----------------------------------------------------------------------#
    choices = ["a","b"]
    #版本号
    banbeng = "V3.2"
    #----------------------------------------------------------------------#
    stf16 = os.getcwd() + "\\images\\hh.png"
    stf = os.getcwd() + "\\登陆.html"
    stf2 = os.getcwd() + "\\dmy.html"
    stf3 = os.getcwd() + "\\main（带图标移动）.py"
    stf4 = os.getcwd() + "\\com_new.py"
    stf5 = os.getcwd() + "\\calc.py"
    stf6 = os.getcwd() + "\\com.py"
    stf7 = os.getcwd() + "\\calc_old.py"
    stf8 = os.getcwd() + "\\aa.png"
    stf9 = os.getcwd() + "\\日记本.py"
    stf10 = os.getcwd() + "\\二维码生成器.py"
    stf11 = os.getcwd() + "\\python代码编辑器.py"
    stf12 = os.getcwd() + "\\红包雨.py"
    stf13 = os.getcwd() + "\\hs.py"
    stf14 = os.getcwd() + "\\main(2).py"
    stf15 = os.getcwd() + "\\zhxx.py"
    xxx = os.getcwd() + "\\信息.txt"
    stftime = os.getcwd() + "\\now_time.py"
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
                b = multpasswordbox(msg="请输入用户名与密码",fields=["用户名：","密码：","年龄:"])
                d = open(".\\账号.txt","r")
                if str(b) == d.read():
                    msgbox("登陆成功!!")
                    xxxx = b[0]
                    yyyy = b[1]
                    zzzz = b[2]
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
                c = multpasswordbox(msg="请输入用户名与密码",fields=["用户名：","密码：","年龄:"])
                z = open(".\\账号.txt","a")
                z.write(str(c))
                z.close()
    #----------------------------------------------------------------------#
    #窗口大小
    WIDTH = 1000
    HEIGHT = 600
    #为键盘检测做准备
    xmm = True
    lj = 1
    lb = 1
    lp = 1
    #---------------------------------------------------------------------#
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
        msgbox("你关闭此程序的次数是："+q)

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
    def cq():
        os.startfile(stf14)
        sys.exit()

    #
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
            gly = Actor("管理员.png",[950,500])
            #绘制
            def draw():
                bg.draw()
                screen.draw.text(banbeng,(925,575),fontsize=40)
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
                    gly.draw()
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

                    a.add_command(label="python文件",command=py)
                    a.add_command(label="文本文档",command=wb)
                    chen.add_cascade(label="创建",menu=a)

                    b = Menu(chen,tearoff=True)
                    b.add_command(label="")
                    b.add_command(label="")
                    chen.add_cascade(label="",menu=b)
                    root.config(menu=chen)

                    c = Button(root,text="恢复所有被删除的程序",command=hfdel)
                    c.pack()
                    d = Button(root,text="重启",command=cq)
                    d.pack(side=LEFT)

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
                            def com_main():
                                root1.destroy()
                                os.system(stf4)
                            def com_del():
                                global delcom
                                root1.destroy()
                                delcom = True
                            Button(root1,text="打开",command=com_main).pack(fill=X)
                            Button(root1,text="删除",command=com_del).pack(fill=X)
                            root1.mainloop()
                        elif ht.collidepoint(pos) and delht == False:
                            root2 = Tk()
                            def ht_main():
                                root2.destroy()
                                p = Tk()
                                w = Canvas(p,width=400,height=200)
                                w.pack()
                                def paint(event):
                                    x1,y1 = (event.x - 1),(event.y - 1)
                                    x2,y2 = (event.x + 1),(event.y + 1)
                                    w.create_oval(x1,y1,x2,y2,fill="yellow")
                                def clean():
                                    w.delete('all')
                                w.bind("<B1-Motion>",paint)
                                Button(p,text="删除所有图案",command=clean).pack()
                                Label(p,text="按下鼠标左键，开始画图吧！").pack(side=BOTTOM)
                                p.mainloop()
                            def ht_del():
                                global delht
                                root2.destroy()
                                delht = True
                            Button(root2,text="打开",command=ht_main).pack(fill=X)
                            Button(root2,text="删除",command=ht_del).pack(fill=X)
                            root2.mainloop()
                        elif hs.collidepoint(pos) and delhs == False:
                            root3 = Tk()
                            def hs_main():
                                root3.destroy()
                                os.startfile(stf2)
                            def hs_del():
                                global delhs
                                root3.destroy()
                                delhs = True
                            Button(root3,text="打开",command=hs_main).pack(fill=X)
                            Button(root3,text="删除",command=hs_del).pack(fill=X)
                            root3.mainloop()
                        elif js.collidepoint(pos) and deljs == False:
                            root4 = Tk()
                            def js_main():
                                root4.destroy()
                                os.system(stf5)
                            def js_del():
                                global deljs
                                root4.destroy()
                                deljs = True
                            Button(root4,text="打开",command=js_main).pack(fill=X)
                            Button(root4,text="删除",command=js_del).pack(fill=X)
                            root4.mainloop()
                        elif ll.collidepoint(pos) and delll == False:
                            root5 = Tk()
                            def ll_main():
                                root5.destroy()
                                web.open("https://www.baidu.com/")
                            def ll_del():
                                global delll
                                root5.destroy()
                                delll = True
                            Button(root5,text="打开",command=ll_main).pack(fill=X)
                            Button(root5,text="删除",command=ll_del).pack(fill=X)
                            root5.mainloop()
                        elif cmd.collidepoint(pos) and delcmd == False:
                            root6 = Tk()
                            def cmd_main():
                                root6.destroy()
                                os.startfile("C:\\Windows\\System32\\cmd.exe")
                            def cmd_del():
                                global delcmd
                                root6.destroy()
                                delcmd = True
                            Button(root6,text="打开",command=cmd_main).pack(fill=X)
                            Button(root6,text="删除",command=cmd_del).pack(fill=X)
                            root6.mainloop()
                        elif wz.collidepoint(pos) and delwz == False:
                            root7 = Tk()
                            def wz_main():
                                root7.destroy()
                                os.startfile(stf)
                            def wz_del():
                                global delwz
                                root7.destroy()
                                delwz = True
                            Button(root7,text="打开",command=wz_main).pack(fill=X)
                            Button(root7,text="删除",command=wz_del).pack(fill=X)
                            root7.mainloop()
                        elif sj.collidepoint(pos) and delsj == False:
                            root8 = Tk()
                            def sj_main():
                                root8.destroy()
                                os.system(stftime)
                            def sj_del():
                                global delsj
                                root8.destroy()
                                delsj = True
                            Button(root8,text="打开",command=sj_main).pack(fill=X)
                            Button(root8,text="删除",command=sj_del).pack(fill=X)
                            root8.mainloop()
                        elif jt.collidepoint(pos) and deljt == False:
                            root9 = Tk()
                            def jt_main():
                                root9.destroy()
                                os.system("C:\\Windows\\System32\\SnippingTool.exe")
                            def jt_del():
                                global deljt
                                root9.destroy()
                                deljt = True
                            Button(root9,text="打开",command=jt_main).pack(fill=X)
                            Button(root9,text="删除",command=jt_del).pack(fill=X)
                            root9.mainloop()
                        elif jsb.collidepoint(pos) and deljsb == False:
                            root10 = Tk()
                            def jsb_main():
                                root10.destroy()
                                os.system(stf9)
                            def jsb_del():
                                global deljsb
                                root10.destroy()
                                deljsb = True
                            Button(root10,text="打开",command=jsb_main).pack(fill=X)
                            Button(root10,text="删除",command=jsb_del).pack(fill=X)
                            root10.mainloop()
                        elif ewm.collidepoint(pos) and delewm == False:
                            root11 = Tk()
                            def ewm_main():
                                root11.destroy()
                                os.system(stf10)
                            def ewm_del():
                                global delewm
                                root11.destroy()
                                delewm = True
                            Button(root11,text="打开",command=ewm_main).pack(fill=X)
                            Button(root11,text="删除",command=ewm_del).pack(fill=X)
                            root11.mainloop()
                        elif cd.collidepoint(pos):
                            pass
                        elif gj.collidepoint(pos):
                            pass
                        elif xm.collidepoint(pos):
                            pass
                        elif gly.collidepoint(pos):
                            pass
                        elif dm.collidepoint(pos) and deldm == False:
                            root12 = Tk()
                            def dm_main():
                                root12.destroy()
                                os.system(stf11)
                            def dm_del():
                                global deldm
                                root12.destroy()
                                deldm = True
                            Button(root12,text="打开",command=dm_main).pack(fill=X)
                            Button(root12,text="删除",command=dm_del).pack(fill=X)
                            root12.mainloop()
                        else:
                            root = Tk()
                            chen = Menu(root)

                            a = Menu(chen,tearoff=True)

                            a.add_command(label="python文件",command=py)
                            a.add_command(label="文本文档",command=wb)
                            a.add_separator()
                            chen.add_cascade(label="创建",menu=a)

                            b = Menu(chen,tearoff=True)
                            b.add_command(label="")
                            b.add_command(label="")
                            chen.add_cascade(label="",menu=b)
                            root.config(menu=chen)

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
                                root.destroy()
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
                            c = Button(root,text="恢复所有被删除的程序",command=hfdel)
                            c.pack()

                            root.mainloop()
                    
                #左键检测
                if button == mouse.LEFT and xmm == True:
                    if computer.collidepoint(pos) and delcom == False:
                        #comm = buttonbox(msg="你要旧版还是新版？",title="提示",choices=("新","旧"))
                        #if comm == "新":
                        os.system(stf4)
                        #if comm == "旧":
                            #os.system(stf6)
                    if ht.collidepoint(pos) and delht == False:
                        p = Tk()
                        w = Canvas(p,width=400,height=200)
                        w.pack()
                        def paint(event):
                            x1,y1 = (event.x - 1),(event.y - 1)
                            x2,y2 = (event.x + 1),(event.y + 1)
                            w.create_oval(x1,y1,x2,y2,fill="yellow")
                        def clean():
                            w.delete('all')
                        w.bind("<B1-Motion>",paint)
                        Button(p,text="删除所有图案",command=clean).pack()
                        Label(p,text="按下鼠标左键，开始画图吧！").pack(side=BOTTOM)
                        p.mainloop()
                        #os.system('C:\\Windows\\System32\\mspaint.exe')
                    if hs.collidepoint(pos) and delhs == False:
                        os.startfile(stf2)
                    if js.collidepoint(pos) and deljs == False:
                        #jss = buttonbox(msg="你要旧版还是新版？",title="提示",choices=("新","旧"))
                        #if jss == "新":
                        os.system(stf5)
                        #if jss == "旧":
                            #os.system(stf7)
                    if ll.collidepoint(pos) and delll == False:
                        web.open("https://www.baidu.com/")
                    if cmd.collidepoint(pos) and delcmd == False:
                        os.startfile("C:\\Windows\\System32\\cmd.exe")
                    if wz.collidepoint(pos) and delwz == False:
                        os.startfile(stf)
                    if sj.collidepoint(pos) and delsj == False:
                        os.system(stftime)
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
                        ggj = Tk()

                        def wgj():
                            gjj = askokcancel(title="",message="确定关机吗",parent=ggj)
                            if gjj == True:
                                gjcs = gjcs+1
                                f = open(".\\关机次数.txt","w")
                                f.write(str(gjcs))
                                f.close()
                                msgbox("tips:有一个彩蛋需要把代码下载到本地运行才可以正常输出(你可能已经发现了)")
                                sys.exit()
                            else:
                                pass
        
                        Button(ggj,text="关机",command=wgj).pack(fill=X)
                        Button(ggj,text="重启",command=cq).pack(fill=X)

                        ggj.mainloop()
                    if gly.collidepoint(pos):
                        yh = Tk()
                        yh.title("个人中心")
                        yh.geometry("250x250")

                        Label(yh,text="用户中心").grid(row=0,pady=5,columnspan=3)
                        Label(yh,text="用户名："+xxxx).grid(row=2)
                        Label(yh,text="密码："+yyyy).grid(row=3)
                        Label(yh,text="年龄："+zzzz).grid(row=4)

                        tkphoto = PhotoImage(file=stf16)
                        Label(yh,image=tkphoto).grid(row=2,rowspan=2,padx=5,pady=5,column=1)

                        yh.mainloop()
                    if xm.collidepoint(pos):
                        xmm = False
                    if jsb.collidepoint(pos) and deljsb == False:
                        os.system(stf9)
                    if ewm.collidepoint(pos) and delewm == False:
                        os.system(stf10)
                    if dm.collidepoint(pos) and deldm == False:
                        os.system(stf11)
                else:
                    if td.collidepoint(pos):
                        xmm = True

            go()
except Exception as b:
    bug = Tk()
    Label(bug,text=b).pack()
    bug.mainloop()
