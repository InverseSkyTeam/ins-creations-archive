import tkinter
import time


def gettime():
    timestr = time.strftime("%H:%M:%S")  # 获取当前的时间并转化为字符串
    lb.configure(text=timestr)  # 重新设置标签文本
    tk.after(1000, gettime)  # 每隔1s调用函数 gettime 自身获取时间


tk = tkinter.Tk()
tk.overrideredirect(True)

def move_window(event):
    tk.geometry("+{0}+{1}".format(event.x_root, event.y_root))
title_frame = tkinter.Frame(tk)
title_label = tkinter.Label(title_frame,bg="grey",height=2,fg="lightgreen",text="Time　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　")
title_label.grid(row=0,sticky=tkinter.W)
title_label.bind("<B1-Motion>", move_window)
title_close = tkinter.Button(title_frame,bg="grey",text="×",activebackground='#ff1e5e',activeforeground='white',padx=5,fg="white",pady=3,command=tk.quit)
title_close.grid(row=0,sticky=tkinter.E)
title_frame.pack()

lb = tkinter.Label(tk, text='', fg='blue', font=("黑体", 80))
lb.pack()
gettime()
tk.mainloop()