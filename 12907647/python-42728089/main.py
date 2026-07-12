import tkinter as tk

# 圆角方法改编于网上搜集的canvas绘图公式，但精确程度更高，绘制也更慢
# 原方法精确度与现在方法精确度之比约为2:5，从锯齿变圆润
# 支持了Windows98及以上的Windows操作系统，圆角
def round_rectangle(canvas, x1, y1, x2, y2, radius, **kwargs):
    points = [x1+radius, y1, x1+radius, y1, x1+radius, y1, x1+radius, y1, x1+radius, y1, 
              x2-radius, y1, x2-radius, y1, x2-radius, y1, x2-radius, y1, x2-radius, y1, 
              x2, y1,
              x2, y1+radius, x2, y1+radius, x2, y1+radius, x2, y1+radius, x2, y1+radius, 
              x2, y2-radius, x2, y2-radius, x2, y2-radius, x2, y2-radius, x2, y2-radius, 
              x2, y2,
              x2-radius, y2, x2-radius, y2, x2-radius, y2, x2-radius, y2, x2-radius, y2, 
              x1+radius, y2, x1+radius, y2, x1+radius, y2, x1+radius, y2, x1+radius, y2, 
              x1, y2,
              x1, y2-radius, x1, y2-radius, x1, y2-radius, x1, y2-radius, x1, y2-radius, 
              x1, y1+radius, x1, y1+radius, x1, y1+radius, x1, y1+radius, x1, y1+radius, 
              x1, y1]
    return canvas.create_polygon(points, **kwargs, smooth=True)

class INSwindow(tk.Tk):
    def __init__(self,w,h,bg,radius=25):
        super().__init__()
        self.setattrs()
        self.radius = radius
        self.bgc = bg
        self.configure(bg=self.bgc)
        self.w = w + radius
        self.h = h + radius
        self.inw = w
        self.inh = h
        self.geometry(f'{self.w}x{self.h}')
        self.rootcanvas = tk.Canvas(self,width=self.w,height=self.h)
        self.rootcanvas.place(x=0,y=0)
        round_rectangle(self.rootcanvas,radius,radius,self.inw,self.inh,radius=radius,fill=self.bgc)
        self.winframe = tk.Frame(self,width=self.inw-radius*2,height=self.inh-self.radius,bg=self.bgc)
        self.winframe.place(x=radius/2*3,y=radius,w=self.inw-radius*2,h=self.inh-self.radius)
        self.titlebarframe = tk.Frame(self.winframe,height=10,bg=self.bgc)
        self.titlebarframe.pack(side='top',fill='x')
        self.iconbtn = tk.Button(self.titlebarframe,text='图标',bg='white',activebackground='white')
        self.iconbtn.pack(side='left')
        self.titlelbl = tk.Label(self.titlebarframe,text='INSwindow(Version 0.3 DEV)',bg=self.bgc,fg='white')
        self.titlelbl.pack(side='left')
        self.closebtn = tk.Button(self.titlebarframe,text=' X ',bg='white',activebackground='white',command=lambda:self.destroy())
        self.closebtn.pack(side='right')
        self.fullscbtn = tk.Button(self.titlebarframe,text=' □ ',bg='white',activebackground='white')
        self.fullscbtn.pack(side='right')
        self.icbtn = tk.Button(self.titlebarframe,text=' — ',bg='white',activebackground='white')
        self.icbtn.pack(side='right')
    def setattrs(self):
        self.attributes('-transparentcolor','#f0f0f0')
        self.attributes('-topmost',True)
        self.overrideredirect(True)

root = INSwindow(800,600,'#313131')
root.mainloop()