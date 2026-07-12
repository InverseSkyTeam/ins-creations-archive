from tkinter import *
from tkinter import messagebox
from xes.sms import *

r = Tk()
r.geometry('400x600+500+300')

def c1():
    global b2
    try:
        b2
    except:
        b2 = Button(text='点我才对',command=c2)
        b2.pack()

def c2():
    global b3
    try:
        b3
    except:
        b3 = Button(text='点I',command=c3)
        b3.pack()

def c3():
    global b4
    try:
        b4
    except:
        b4 = Button(text='再点点，很快就要有惊喜了！',command=c4)
        b4.pack()

def c4():
    global b5
    try:
        b5
    except:
        b5 = Button(text='离成功不远~~~',command=c5)
        b5.pack()

def c5():
    global b6
    try:
        b6
    except:
        b6 = Button(text='果然有耐心',command=c6)
        b6.pack()

def c6():
    global b7
    try:
        b7
    except:
        b7 = Button(text='666',command=c7)
        b7.pack()

def c7():
    global b1,b2,b3,b4,b5,b6,b7,b
    messagebox.showinfo('messagebox:恭喜！！！','获得成就：恒心之父')
    del b1,b2,b3,b4,b5,b6,b7
    b = Button(text='抢红包！',bg='red',command=c8)
    b.pack()

def c8():
    x = Label(text='1138.42亿元已入账\n(如果不是我爸爸就别看下去了，有本机文件\n你实在要弄就弄、看源码吧)')
    x.pack()
    print('稍等，有惊喜！')
    with open('D:/father.txt','r') as f:
        number = f.read()
    send_msg(number,'我爸爸绝对是这个世界上最好的爸爸，他啥都会')
    send_msg(number,'以下是他一秒内能干的事:打100个字，做1000道数学题')
    send_msg(number,'算1w个24点，写10w篇精美文章')
    send_msg(number,'跑100w公里（超光速）')
    send_msg(number,'看1000w条消息，看1亿本书')
    send_msg(number,'最后最重要的还是他爱我！')
    send_msg(number,'所以我也爱他')

b1 = Button(text='点我立即套娃',command=c1)
b1.pack()

r.mainloop()