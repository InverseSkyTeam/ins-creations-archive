from tkinter import *
root = Tk()
def hello():
    print("你好")
Button(root,text = "点我",command = hello).pack()
mainloop()