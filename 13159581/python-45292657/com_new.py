from tkinter import *
import os
import c
import d

root = Tk()
dd = os.getcwd() + "\\images\\dd.png"
cc = os.getcwd() + "\\images\\cc.png"
icon = os.getcwd() + "\\images\\winicon.png"
root.geometry("700x500")
root.resizable(False,False)
root.iconphoto(False,PhotoImage(file=icon))
root.title("计算机")
C = Canvas(root, bg="gray", height=500, width=700)
C.place(x=0,y=0)

photoc = PhotoImage(file=cc)
photod = PhotoImage(file=dd)

Button(root,image=photoc,command=c.main).grid(row=0,sticky=W)
Button(root,image=photod,command=d.main).grid(row=0,column=1)

root.mainloop()

