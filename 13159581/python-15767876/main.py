from tkinter import *
root = Tk()
def a(event):
    print("敲击位置：",repr(event.char))
b = Frame(root,width=200,height=200)
b.bind("<Key>",a)
b.focus_set()
b.pack()
mainloop()