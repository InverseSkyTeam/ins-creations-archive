from tkinter import *
root = Tk()
def a(event):
    print("当前位置：",event.x,event.y)
b = Frame(root,width=200,height=200)
b.bind("<Motion>",a)
b.pack()
mainloop()