from tkinter import *
from tkinter import ttk
root = Tk()
root.state('normal')
root.geometry("200x250-0-50")
root.wm_attributes("-alpha", 0.4)
root.wm_attributes("-toolwindow", True)
root.wm_attributes("-topmost", True)
root.overrideredirect(True)
xwin = 0
ywin = 0
def get_pos(event):
    global xwin, ywin
    xwin = event.x
    ywin = event.y
def move_window(event):
    root.geometry(f'+{event.x_root - xwin}+{event.y_root - ywin}')
frame = Label(root,text="　　　　　　　小便签　　　　　　　",bg="red")
frame.pack()
ttk.Button(root,text="关闭",command=root.quit).pack(fill="x")
frame.bind("<B1-Motion>", move_window)
frame.bind('<Button-1>', get_pos)
a = Text(root,bg="yellow",font=(None,10))
a.pack()
root.mainloop()
