import tkinter
import time


def gettime():
    timestr = time.strftime("%H:%M:%S")  # 获取当前的时间并转化为字符串
    lb.configure(text=timestr)  # 重新设置标签文本
    tk.after(1000, gettime)  # 每隔1s调用函数 gettime 自身获取时间


tk = tkinter.Tk()
tk.overrideredirect(True)

def get_pos(event):
    global xwin, ywin
    xwin = event.x
    ywin = event.y
def move_window(event):
    tk.geometry(f'+{event.x_root - xwin}+{event.y_root - ywin}')
def iconic_window():
    tk.overrideredirect(False)
    tk.state('iconic')
def to_overrideredirect_window():
    if tk.state() == 'normal':
        tk.overrideredirect(True)
    else:
        tk.overrideredirect(False)
def run():
    while True:
        try:
            to_overrideredirect_window()
            tk.update()
        except:
            break
title_frame = tkinter.Frame(tk)
title_label = tkinter.Label(title_frame,bg="grey",height=2,fg="lightgreen",text="Time　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　")
title_label.grid(row=0,sticky=tkinter.W)
title_label.bind("<B1-Motion>", move_window)
title_label.bind('<Button-1>', get_pos)
title_iconic = tkinter.Button(title_frame,bg="grey",text="—",bd=0, font='bold', fg='white',activebackground='lightskyblue',activeforeground='white',highlightthickness=0,cursor='hand2',command=iconic_window)
title_iconic.grid(row=0)
title_close = tkinter.Button(title_frame,bg="grey",text="×",bd=0,font='blod',activebackground='#ff1e5e',activeforeground='white',fg="white",pady=3,command=tk.destroy,cursor='hand2',highlightthickness=0)
title_close.grid(row=0,sticky=tkinter.E)
title_frame.pack()

lb = tkinter.Label(tk, text='', fg='blue', font=("黑体", 80))
lb.pack()
gettime()
run()