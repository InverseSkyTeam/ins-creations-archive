from tkinter import *
root = Tk()
a = Text(root,width=30,height=5,autoseparators=False,undo=True,maxundo=10)
a.pack()
def b(event):
    a.edit_separetor()
a.bind('<Key>',b)
a.insert(INSERT,"")
def show():
    a.edit_undo()
Button(root,text="撤销",command=show).pack()
Button(root,text="退出",command=root.quit).pack()
mainloop()