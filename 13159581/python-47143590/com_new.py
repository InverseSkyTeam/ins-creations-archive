from tkinter import *
from tkinter import ttk
import os
import c
import d
import e

root = Tk()
dd = os.getcwd() + "\\images\\dd.png"
cc = os.getcwd() + "\\images\\cc.png"
ee = os.getcwd() + "\\images\\ee.png"
icon = os.getcwd() + "\\images\\winicon.png"
root.geometry("700x500+200+200")
root.overrideredirect(True)
def move_window(event):
    root.geometry("+{0}+{1}".format(event.x_root, event.y_root))
title_frame = Frame(root)
title_label = Label(title_frame,bg="grey",height=2,fg="lightgreen",text="计算机　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　")
title_label.grid(row=0,sticky=W)
title_label.bind("<B1-Motion>", move_window)
title_close = Button(title_frame,bg="grey",text="×",activebackground='#ff1e5e',activeforeground='white',padx=5,fg="white",pady=3,command=root.quit)
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

root.mainloop()
