from tkinter import *
root = Tk()
def create():
    top = Toplevel()
    top.title("陈锦奕最帅！")
    msg = Message(top,text="陈锦奕最帅！")
    msg.pack()
Button(root,text="创建顶级窗口",command=create).pack()
mainloop()