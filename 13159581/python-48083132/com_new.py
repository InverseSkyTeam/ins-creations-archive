from tkinter import *
from tkinter import ttk
import os
import c,d,e,sys


root = Tk()
root.geometry("700x500+200+200")
root.state('normal')
root.attributes('-topmost',True)
root.overrideredirect(True)


def get_pos(event):
    global xwin, ywin
    xwin = event.x
    ywin = event.y
def move_window(event):
    root.geometry(f'+{event.x_root - xwin}+{event.y_root - ywin}')
def iconic_window():
    root.overrideredirect(False)
    root.state('iconic')
def to_overrideredirect_window():
    if root.state() == 'normal':
        root.overrideredirect(True)
    else:
        root.overrideredirect(False)
def run():
    while True:
        try:
            to_overrideredirect_window()
            root.update()
        except:
            break

dd = os.getcwd() + "\\images\\dd.png"
cc = os.getcwd() + "\\images\\cc.png"
ee = os.getcwd() + "\\images\\ee.png"
icon = os.getcwd() + "\\images\\winicon.png"

title_frame = Frame(root)
title_label = Label(title_frame,bg="grey",height=2,fg="lightgreen",text="计算机    　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　")
title_label.grid(row=0,sticky=W)
title_label.bind("<B1-Motion>", move_window)
title_label.bind('<Button-1>', get_pos)
title_iconic = Button(title_frame,bg="grey",text="—",bd=0, font='bold', fg='white',activebackground='lightskyblue',activeforeground='white',highlightthickness=0,cursor='hand2',command=iconic_window)
title_iconic.grid(row=0)
title_close = Button(title_frame,bg="grey",text="×",bd=0,font='blod',activebackground='#ff1e5e',activeforeground='white',fg="white",pady=3,command=root.destroy,cursor='hand2',highlightthickness=0)
title_close.grid(row=0,sticky=E)
title_frame.pack()

frame2 = Frame(root)

photoc = PhotoImage(file=cc)
photod = PhotoImage(file=dd)
photoe = PhotoImage(file=ee)

ttk.Button(frame2,image=photoc,command=c.main).grid(row=0,sticky=W)
ttk.Button(frame2,image=photod,command=d.main).grid(row=0,column=1)
ttk.Button(frame2,image=photoe,command=e.main).grid(row=0,column=2)

frame2.pack()

run()
#root.mainloop()
