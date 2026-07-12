import time
from tkinter import *

def get_time():
    time2 = time.strftime("%Y-%m-%d %H:%M:%S")
    clock = Label(root,text=time2,font=28)
    clock.place(x=0,y=0)
    clock.after(1000,get_time)

root = Tk()
root.geometry("200x50")
get_time()
root.mainloop()
