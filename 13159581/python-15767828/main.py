from tkinter import *
root = Tk()
def a(event):
    print("单击位置：","x:",event.x,"y:",event.y)
b = Frame(root,width=200,height=200)
b.bind("<Button-1>",a)
b.pack()
mainloop()