import tkinter as tk,random,os,webbrowser as w
from time import *
root = tk.Tk()
root.geometry('300x400')
root.title('|宇宙|作品集·小轩')
def web(t):
    w.open('https://code.xueersi.com/home/project/detail?lang=code&pid='+str(t)+'&version=offline&form=python&langType=python')
def web_sc(t):
    w.open('https://code.xueersi.com/home/project/detail?lang=scratch&pid='+str(t)+'&version=3.0&langType=scratch')
def yu():
    window=tk.Toplevel(root)
    window.geometry('300x800')
    window.title('|宇宙|作品')
    window.iconbitmap("无.png")
    def https1():
        web(13358211)
    def https2():
        web(13221351)
    def https3():
        web(13033899)
    def https4():
        web(12817956)
    def https5():
        web(12031693)
    def https6():
        web(13144672)
    def https7():
        web(8946083)
    def https8():
        web(8888622)
    def https9():
        web(6489179)
    def https10():
        web(5095577)
    def https11():
        web(8854237)
    def https12():
        web(8178910)
    def https13():
        web(4714155)
    def https14():
        web(4446255)
    def https15():
        web(4295084)
    def https16():
        web(3258973)
    def https17():
        web(2515310)
    def https18():
        web(1576378)
    def https19():
        web(1413178)
    def https20():
        web(1081299)
    def https21():
        web(10151895)
    def https22():
        web(12798626)
    def https23():
        web(13003790)
    def quit_window():
        window.destroy()
    # window button
    # 水印 小轩-原创 预防侵权文字：fdjghjkhsnidughsdi01f65f06df5h498sdfhqpfher90489dfhqwecpoilnmb-'=;ofghn501'by_Xx45sdf4009大6
    wb1 = tk.Button(window,text='套娃-作品集',command=https1)
    wb1.pack()
    wb2 = tk.Button(window,text='|小轩|爆字体！',command=https2)
    wb2.pack()
    wb3 = tk.Button(window,text='死机之歌',command=https3)
    wb3.pack()
    wb4 = tk.Button(window,text='网站1.1.5',command=https4)
    wb4.pack()
    wb5 = tk.Button(window,text='|宇宙|保卫家园+植物大战\n僵尸+文明城市V0.0.4',command=https5)
    wb5.pack()
    wb6 = tk.Button(window,text='C站重要人物',command=https6)
    wb6.pack()
    wb7 = tk.Button(window,text='大战外星电脑5.2-宇宙工作室',command=https7)
    wb7.pack()
    wb8 = tk.Button(window,text='2048进阶版-宇宙工作室',command=https8)
    wb8.pack()
    wb9 = tk.Button(window,text='小轩聊天1.1',command=https9)
    wb9.pack()
    wb10 = tk.Button(window,text='小轩-扫雷1.0.2',command=https10)
    wb10.pack()
    wb11 = tk.Button(window,text='奇怪的红点制表符和exec代码',command=https11)
    wb11.pack()
    wb12 = tk.Button(window,text='宇宙长度小游戏1.0',command=https12)
    wb12.pack()
    wb13 = tk.Button(window,text='大鱼吃小鱼小轩A字版1.3',command=https13)
    wb13.pack()
    wb14 = tk.Button(window,text='99乘法表银河挥霍',command=https14)
    wb14.pack()
    wb15 = tk.Button(window,text='小轩：2行代码搞定疫情地图！！',command=https15)
    wb15.pack()
    wb16 = tk.Button(window,text='球球大嘴怪（多版本）8.5.9',command=https16)
    wb16.pack()
    wb17 = tk.Button(window,text='平方根',command=https17)
    wb17.pack()
    wb18 = tk.Button(window,text='考眼力2',command=https18)
    wb18.pack()
    wb19 = tk.Button(window,text='时光机5.4.8（终极版本！）',command=https19)
    wb19.pack()
    wb20 = tk.Button(window,text='成语接龙',command=https20)
    wb20.pack()
    wb21 = tk.Button(window,text='#我在C站第一个、我与C站的故事#\nC站曾经那些故事1.0',command=https21)
    wb21.pack()
    wb22 = tk.Button(window,text='宇宙工作室普通python-logo',command=https22)
    wb22.pack()
    wb23 = tk.Button(window,text='谁有问题，来这里问',command=https23)
    wb23.pack()
    wbq = tk.Button(window,text='关闭此分窗口',command=quit_window)
    wbq.pack()
def yu2():
    window=tk.Toplevel(root)
    window.geometry('300x300')
    window.title('|宇宙|作品')
    window.iconbitmap("无.png")
    def https1():
        web_sc(12484683)
    def https2():
        web_sc(12416323)
    def https3():
        web_sc(11956416)
    def https4():
        web_sc(5136929)
    def https5():
        web_sc(2425220)
    def quit_window():
        window.destroy()
    # window button
    # 钢印 小轩-原创 预防侵权文字：fdjhxjkhsnidughsmi01f65f06df5h498sdfhqpfher90489dfhqwecpoilnmb-'=;ofghn501'by_Xx45sdf4009大6
    wb1 = tk.Button(window,text='电梯历险记（搞笑，\n后续情节有编，非真）',command=https1)
    wb1.pack()
    wb2 = tk.Button(window,text='死机之歌',command=https2)
    wb2.pack()
    wb3 = tk.Button(window,text='#80粉福#数字国\n版图历史大变化',command=https3)
    wb3.pack()
    wb4 = tk.Button(window,text='小轩-智能五子棋对弈3.8.4',command=https4)
    wb4.pack()
    wb5 = tk.Button(window,text='消灭病毒',command=https5)
    wb5.pack()
    wbq = tk.Button(window,text='关闭此分窗口',command=quit_window)
    wbq.pack()
def yu3():
    window=tk.Toplevel(root)
    window.geometry('300x300')
    window.title('|宇宙|作品')
    window.iconbitmap("无.png")
    def https1():
        web(10244624)
    def https2():
        web(13207625)
    def https3():
        web(13086796)
    def https4():
        web(13203642)
    def https5():
        web(13044683)
    def quit_window():
        window.destroy()
    # window button
    wb1 = tk.Button(window,text='抗洪大作战',command=https1)
    wb1.pack()
    wb2 = tk.Button(window,text='哪吒敖丙打砖块',command=https2)
    wb2.pack()
    wb3 = tk.Button(window,text='制作像素画v5.0\n本系列的收官之作+巅峰之作',command=https3)
    wb3.pack()
    wb4 = tk.Button(window,text='帝国进行曲视频—\n纪念大卫·鲍罗斯',command=https4)
    wb4.pack()
    wb5 = tk.Button(window,text='#2021，C站我想对你说#',command=https5)
    wb5.pack()
    wbq = tk.Button(window,text='关闭此分窗口',command=quit_window)
    wbq.pack()
def yu4():
    window=tk.Toplevel(root)
    window.geometry('300x250')
    window.title('|其他|作品')
    window.iconbitmap("无.png")
    def https1():
        w.open('https://code.xueersi.com/')
    def https2():
        w.open('https://code.xueersi.com/search')
    def https3():
        w.open('https://code.xueersi.com/space/12907647')
    def quit_window():
        window.destroy()
    wb1 = tk.Button(window,text='主页作品',command=https1)
    wb1.pack()
    wb2 = tk.Button(window,text='全部作品',command=https2)
    wb2.pack()
    wb3 = tk.Button(window,text='|小轩|个人主页',command=https3)
    wb3.pack()
    wbq = tk.Button(window,text='关闭此分窗口',command=quit_window)
    wbq.pack()
def yu5():
    window=tk.Toplevel(root)
    window.geometry('300x250')
    window.title('|搜索○、|作品')
    window.iconbitmap("无.png")
    def https0():
        wtg = wt1.get()
        wtg2 = wt2.get()
        if wtg == '1':
            web_sc(wtg2)
        else:
            web(wtg2)
    def quit_window():
        window.destroy()
    wl = tk.Label(window,text='输入框1：输入你要看图形化编程作品\n还是python,图形化输1，否则输别的\n输入框2：输入作品的pid')
    wl.pack()
    wt1 = tk.Entry(window,bd=7)
    wt1.pack()
    wt2 = tk.Entry(window,bd=7)
    wt2.pack()
    wb = tk.Button(window,text='搜索作品',command=https0)
    wb.pack()
    wbq = tk.Button(window,text='关闭此分窗口',command=quit_window)
    wbq.pack()
def yu6():
    window=tk.Toplevel(root)
    window.geometry('300x250')
    window.title('|搜索○、|主页')
    window.iconbitmap("无.png")
    def https0():
        wtg = wt.get()
        w.open('https://code.xueersi.com/space/'+str(wtg))
    def quit_window():
        window.destroy()
    wl = tk.Label(window,text='输入框：输入你要看个人主页的编码')
    wl.pack()
    wt = tk.Entry(window,bd=7)
    wt.pack()
    wb = tk.Button(window,text='搜索这个个人主页',command=https0)
    wb.pack()
    wbq = tk.Button(window,text='关闭此分窗口',command=quit_window)
    wbq.pack()
# root button
rb1 = tk.Button(root,text='宇宙工作室python作品\n[好玩，有趣，创意，我1等推荐]',bg='skyblue',command=yu)
rb1.pack()
rb2 = tk.Button(root,text='宇宙工作室图形化编程作品\n[很好，不错，2等推荐]',bg='yellow',command=yu2)
rb2.pack()
rb3 = tk.Button(root,text='宇宙工作室其他成员作品\n[较好，3等推荐]',bg='lightyellow',command=yu3)
rb3.pack()
rb4 = tk.Button(root,text='别人的作品\n[较好，4等推荐]',command=yu4)
rb4.pack()
rb5 = tk.Button(root,text='搜索作品\n你要知道pid',command=yu5)
rb5.pack()
rb6 = tk.Button(root,text='搜个人\n主页',command=yu6)
rb6.pack()
root.mainloop()