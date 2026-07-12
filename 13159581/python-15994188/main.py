from tkinter import *
p = Tk()
w = Canvas(p,width=400,height=200)
w.pack()
def paint(event):
    x1,y1 = (event.x - 1),(event.y - 1)
    x2,y2 = (event.x + 1),(event.y + 1)
    w.create_oval(x1,y1,x2,y2,fill="yellow")
def clean():
    w.delete('all')
w.bind("<B1-Motion>",paint)
Button(p,text="删除所有图案",command=clean).pack()
Label(p,text="按下鼠标左键，开始画图吧！").pack(side=BOTTOM)
mainloop()