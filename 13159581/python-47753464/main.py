from cefpython3 import cefpython as cef
from tkinter import *
import threading

def cw(x='https://code.xueersi.com/space/12907647',t='窗口'):
    cef.Initialize()
    cef.CreateBrowserSync(url=x,window_title=t)
    cef.MessageLoop()

root = Tk()
root.title("浏览器")

frame = Frame()
e1 = Entry(frame,width=100,bg="lightskyblue",fg="green")
e1.grid(row=0,sticky=W)

def search():
    text = e1.get()
    cw(x='https://www.baidu.com/s?wd='+text)
b1 = Button(frame,text="搜 索",width=15,bg="grey",fg="lightgreen",command=search)
b1.grid(row=0,column=1)

frame.grid(row=0)
def search2():
    cw(x='http://127.0.0.1:55824/index.html')
b2 = Button(root,text="完整浏览器",bg="grey",width=115,fg="lightgreen",command=search2)
b2.grid(row=1)

root.mainloop()
