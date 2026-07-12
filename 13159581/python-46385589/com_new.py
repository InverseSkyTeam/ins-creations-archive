from tkinter import *
from tkinter import ttk
import os
import c
import d
import e

root = Tk()
dd = os.getcwd() + "\\images\\dd.png"
cc = os.getcwd() + "\\images\\cc.png"
ee = os.getcwd() + "\\images\\ee.png"
icon = os.getcwd() + "\\images\\winicon.png"
root.geometry("700x500+200+200")
root.resizable(False,False)
root.iconphoto(False,PhotoImage(file=icon))
root.title("计算机")
C = Canvas(root, bg="gray", height=500, width=700)
C.place(x=0,y=0)

photoc = PhotoImage(file=cc)
photod = PhotoImage(file=dd)
photoe = PhotoImage(file=ee)

ttk.Button(root,image=photoc,command=c.main).grid(row=0,sticky=W)
ttk.Button(root,image=photod,command=d.main).grid(row=0,column=1)
ttk.Button(root,image=photoe,command=e.main).grid(row=0,column=2)

root.mainloop()
