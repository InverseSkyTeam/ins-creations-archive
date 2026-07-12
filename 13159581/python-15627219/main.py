from tkinter import *
from easygui import *
root = Tk()
def a():
    msgbox("正中靶心")
Button(root,text="点我",command=a).place(relx=0.5,rely=0.5,anchor=CENTER)
mainloop()