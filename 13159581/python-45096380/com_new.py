from tkinter import *
import os
import c
import d

root = Tk()
dd = os.getcwd() + "\\images\\dd.png"
cc = os.getcwd() + "\\images\\cc.png"
root.geometry("700x500")
root.title("计算机")

photoc = PhotoImage(file=cc)
photod = PhotoImage(file=dd)

Button(root,image=photoc,command=c.main).grid(row=0,sticky=W)
Button(root,image=photod,command=d.main).grid(row=0,column=1)

root.mainloop()

