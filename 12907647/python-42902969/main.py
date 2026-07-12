import tkinter as tk
import sys

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
    def __init__(self,w,h,winx=0,winy=0,radius=25,bg='#313131',titlebg='#111111'):
        # 基础设施--------------------------------------------
        super().__init__()
        self.setattrs()
        self.run = self.mainloop
        self.radius = radius
        self.bgc = bg
        self.titlebgc = titlebg
        self.configure(bg=self.bgc)
        self.winx = winx
        self.winy = winy
        self.evt_pos = (winx,winy)
        self.w = w
        self.h = h
        self.outsideborder = 20
        self.geometry(f'{self.w+radius+self.outsideborder*2}x{self.h+radius+self.outsideborder}+{self.winx}+{self.winy}')
        
        self.rootcanvas = tk.Canvas(self,width=self.w+radius+self.outsideborder*2,height=self.h+radius+20*2,bg='green')
        self.rootcanvas.place(x=0,y=0)
        round_rectangle(self.rootcanvas,self.outsideborder,self.outsideborder,self.w+radius+self.outsideborder,self.h+self.outsideborder,radius=radius,fill=self.bgc)
        
        # 内部窗口--------------------------------------------
        self.winframe = tk.Frame(self,width=self.w,height=self.h,bg='cyan')
        self.winframe.place(x=self.outsideborder+self.radius/2,y=self.outsideborder,w=self.w,h=self.h)
        
        self.titlebarframe = tk.Frame(self.winframe,height=10,bg=self.titlebgc)
        self.titlebarframe.pack(side='top',fill='x')
        
        self.iconbtn = tk.Button(self.titlebarframe,text='图标',bg='white',activebackground='white')
        self.iconbtn.pack(side='left')
        self.titlelbl = tk.Label(self.titlebarframe,text='INSwindow(Version 0.5 DEV)',bg=self.bgc,fg='white')
        self.titlelbl.pack(side='left')
        self.closebtn = tk.Button(self.titlebarframe,text=' X ',bg='white',activebackground='white',command=lambda:self.destroy())
        self.closebtn.pack(side='right')
        self.fullscbtn = tk.Button(self.titlebarframe,text=' □ ',bg='white',activebackground='white')
        self.fullscbtn.pack(side='right')
        self.icbtn = tk.Button(self.titlebarframe,text=' — ',bg='white',activebackground='white')
        self.icbtn.pack(side='right')
        
        self.titlebarframe.bind("<Button-1>",self.get_evt_pos)
        self.titlebarframe.bind("<B1-Motion>",self.movewin)
    
    def get_evt_pos(self,event):
        self.evt_pos = (event.x,event.y)
    def movewin(self,event):
        self.geometry(f'+{round(event.x_root-self.evt_pos[0]-self.outsideborder-self.radius/2)}+{round(event.y_root-self.evt_pos[1]-self.outsideborder)}')
        
    def setattrs(self):
        self.attributes('-transparentcolor','#f0f0f0')
        self.attributes('-topmost',True)
        self.overrideredirect(True)

def exit():
    print('感谢体验。')
    sys.exit()

root = INSwindow(300,200)
INSwindow(350,600,300,100)
INSwindow(1000,800,666,11)
INSwindow(1400,100,15,800)
button = tk.Button(root.winframe,bg='yellow',activebackground='red',text='全部毁灭',command=exit)
button.pack()
root.run()

exit()