from tkinter import *
root = Tk()
Label(root,text="找不同").pack()
a = Listbox(root,setgrid=True)
a.pack()
for i in ["python","c++","scratch","tkinter"]:
    a.insert(END,i)
b = Button(root,text="删除",command=lambda x=a: x.delete(ACTIVE))
b.pack()
mainloop()