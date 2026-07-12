from cefpython3 import cefpython as cef
from tkinter import *
import threading
import os

def cw(x='https://code.xueersi.com/space/12907647',t='窗口'):
    cef.Initialize()
    cef.CreateBrowserSync(url=x,window_title=t)
    cef.MessageLoop()

root = Tk()
root.title("浏览器")

frame = Frame()
e1 = Entry(frame,width=102,bg="lightskyblue",fg="green")
e1.grid(row=0,sticky=W)
frame.grid(row=0)

frame2 = Frame()
def search():
    text = e1.get()
    cw(x='https://www.baidu.com/s?wd='+text)
b1 = Button(frame2,text="搜 索",width=50,bg="grey",fg="lightgreen",command=search)
b1.grid(row=0,sticky=W)

def search2():
    text=e1.get()
    if "http:\\"in text or "http://" in text:
        cw(x=text)
    else:
        cw(x="http://"+text)
b2 = Button(frame2,text="打开输入的网址",bg="grey",width=50,fg="lightgreen",command=search2)
b2.grid(row=0,column=1)

frame2.grid(row=1)

root.mainloop()
