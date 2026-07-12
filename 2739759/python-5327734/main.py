from tkinter import*
import time
window = Tk()
window.geometry("200x300+-10+0")
window.resizable(False,False)
window.title("我的第一个tkinter小程序")
window.iconbitmap("img1.png")
def hello4():
    while True:
        print("求赞")
        time.sleep(0)
def hello3():
    btn = Button(window,text = "点me",command = hello4)
    btn.pack()
def hello2():
    btn = Button(window,text = "点I",command = hello3)
    btn.pack()
def hello1():
    btn = Button(window,text = "点wo",command = hello2)
    btn.pack()
btn = Button(window,text = "点我",command = hello1)
btn.pack()
window.mainloop()