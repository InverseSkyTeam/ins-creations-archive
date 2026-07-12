from tkinter import *
from math import *
root = Tk()
w = Canvas(root,width=200,height=100,background="red")
w.pack()
x1 = 100
y1 = 50
r = 50
a = [
    x1 - int(r * sin(2 * pi / 5)),
    y1 - int(r * cos(2 * pi / 5)),
    x1 + int(r * sin(2 * pi / 5)),
    y1 - int(r * cos(2 * pi / 5)),
    x1 - int(r * sin(pi / 5)),
    y1 + int(r * cos(pi / 5)),
    x1,
    y1 - r,
    x1 + int(r * sin(pi / 5)),
    y1 + int(r * cos(pi / 5)),
    ]
w.create_polygon(a,outline="green",fill="yellow")
mainloop()