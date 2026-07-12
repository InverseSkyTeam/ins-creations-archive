from tkinter import *
'''
c_tkprint("这里写内容","这里写标题")
'''
def c_tkprint(a,b):
    root = Tk()
    root.title(b)
    Label(root,text=a).pack()
    mainloop()
import time
'''
┌──────────────┐
│--------------│
│ 陈锦奕最帅！ │
│--------------│
└──────────────┘
'''
def c_card(a):
    h1 = "─"
    h2 = "-"
    f = "!@#$%^&*()_+-=,.`\[]{};':<>|"
    list = [49,50,51,52,53,54,55,56,57,48,183,65]
    i = 1
    l = 65
    y = 0
    n = 0
    for i in range(57):
        if i == 26:
            l=96
        l = l+1
        list.append(l)
    for i in range(len(a)):
        i1 = i+1
        a1 = a[i:i1]
        a1 = ord(a1)
        if a1 in list :
            y = y+1
        else:
            n = n+1
    if n == 0 and y > 0:
        k1 = "─"
        k2 = "-"
    if n > 0 and y == 0:
        k1 = "─"*2
        k2 = "-"*2
    else:
        k1 = "─"
        k2 = "-"
    for i in range(len(a)):
        h1 = h1+k1
        h2 = h2+k2
    if n > 0 and y > 0:
        h1 = h1+"─"*n
        h2 = h2+"-"*n
    print("┌─"+h1+"┐")
    time.sleep(0.05)
    print("│-"+h2+"│")
    time.sleep(0.05)
    print("│ "+a+" │")
    time.sleep(0.05)
    print("│-"+h2+"│")
    time.sleep(0.05)
    print("└─"+h1+"┘") 
import time
'''
用c_print("里面写你想逐字输出的字")
'''
def c_print(js):
    ohh=int(0)
    for i in js:
        print(js[ohh],end="",flush=True)
        time.sleep(0.085)
        ohh+=1
import time
'''
c_t1()#等待一秒
c_t2()#等待二秒
c_t(t)#在t里面写要等待的秒数
'''
def c_t1():
    time.sleep(1)
def c_t2():
    time.sleep(2)
def c_t(t):
    time.sleep(t)
import time
'''
c_clear()#这是清屏用的
'''
def c_clear():
    print("\033[2J\033[1000A",end='')
'''
c_tclear(t)#先sleept秒再清屏
'''
def c_tclear(t):
    time.sleep(t)
    print("\033[2J\033[1000A",end='')
from tkinter import *
import easygui as a
'''
c_tk()#一款登录器
'''
def c_tk():
    root = Tk()
    Label(root,text="账号：").grid(row=0)
    Label(root,text="密码：").grid(row=1)
    v1 = StringVar()
    v2 = StringVar()
    e1 = Entry(root,textvariable=v1) 
    e2 = Entry(root,textvariable=v2,show="*")
    e1.grid(row=0,column=1,padx=10,pady=5)
    e2.grid(row=1,column=1,padx=10,pady=5)
    def show():
        a.msgbox("账号：%s" % v1.get())
        a.msgbox("密码：%s" % v2.get())
        e1.delete(0,END)
        e2.delete(0,END)
    Button(root,text="芝麻开门",width=10,command=show).grid(row=3,column=0,sticky=W,padx=10,pady=5)
    Button(root,text="退出",width=10,command=root.quit).grid(row=3,column=1,sticky=E,padx=10,pady=5)
    mainloop()
import time
'''
c_spark，是闪烁c_spark接收两个参数，第一个是你要写出来的句子，第二个是闪烁次数 代码示例：c_spark('hello',10)——这样“hello”这个句子就会闪烁10次了！
'''
def c_spark(x,y):
    for i in range(y):
        print("\033[30m"+x)
        time.sleep(0.1)
        print("\033[2J\033[1000A",end='')
        print("\033[31m"+x)
        time.sleep(0.1)
        print("\033[2J\033[1000A",end='')
        print("\033[32m"+x)
        time.sleep(0.1)
        print("\033[2J\033[1000A",end='')
        print("\033[33m"+x)
        time.sleep(0.1)
        print("\033[2J\033[1000A",end='')
        print("\033[34m"+x)
        time.sleep(0.1)
        print("\033[2J\033[1000A",end='')
        print("\033[35m"+x)
        time.sleep(0.1)
        print("\033[2J\033[1000A",end='')
        print("\033[36m"+x)
        time.sleep(0.1)
        print("\033[2J\033[1000A",end='')
        print("\033[37m"+x)
        time.sleep(0.1)
        print("\033[2J\033[1000A",end='')
'''
0——打印一个空格长度的黑色背景

1——打印一个空格长度的红色背景
        
2——打印一个空格长度的绿色背景
        
3——打印一个空格长度的黄色背景
    
4——打印一个空格长度的蓝色背景
        
5——打印一个空格长度的紫红色背景
        
6——打印一个空格长度的青蓝色背景
        
7——打印一个空格长度的白色背景
        
d——将下一个字符染为黑色
        
r——将下一个字符染为红色
        
g——将下一个字符染为绿色
        
y——将下一个字符染为黄色
        
b——将下一个字符染为蓝色
        
p——将下一个字符染为紫红色
        
q——将下一个字符染为青蓝色
        
w——将下一个字符染为白色
'''
def logo(a):
    for x in range(len(a)):
        if a[x] == "0":
            print("\033[40m ", end="")
        elif a[x] == "1":
            print("\033[41m ", end="")
        elif a[x] == "2":
            print("\033[42m ", end="")
        elif a[x] == "3":
            print("\033[43m ", end="")
        elif a[x] == "4":
            print("\033[44m ", end="")
        elif a[x] == "5":
            print("\033[45m ", end="")
        elif a[x] == "6":
            print("\033[46m ", end="")
        elif a[x] == "7":
            print("\033[47m ", end="")
        elif a[x] == "d":
            print("\033[30m ", end='')
        elif a[x] == "r":
            print("\033[31m ", end="")
        elif a[x] == "g":
            print("\033[32m ", end="")
        elif a[x] == "y":
            print("\033[33m ", end="")
        elif a[x] == "b":
            print("\033[34m ", end="")
        elif a[x] == "p":
            print("\033[35m ", end="")
        elif a[x] == "q":
            print("\033[36m ", end="")
        elif a[x] == "w":
            print("\033[37m ", end="")
        else:
            print(a[x], end="")
    print("\033[0m")