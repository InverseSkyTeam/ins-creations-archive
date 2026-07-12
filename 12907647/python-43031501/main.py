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

def get_back_color(color):
    dic = {
        'red': 'green',
        'yellow': 'blue',
        'orange': 'cyan',
        'pink': 'lightyellow',
        'purple': 'lightgreen',
        'lightyellow': 'lightskyblue',
        'green': 'red',
        'blue': 'yellow',
        'cyan': 'orange',
        'lightgreen': 'purple',
        'lightskyblue': 'pink',
    }
    if color in dic:
        return dic[color]
    r = 255 - int(color[1]+color[2],16)
    g = 255 - int(color[3]+color[4],16)
    b = 255 - int(color[5]+color[6],16)
    newcolor = str(hex(r))[2:]+str(hex(g))[2:]+str(hex(b))[2:]
    return '#'+newcolor

class INSwindow(tk.Tk):
    def __init__(self,w,h,winx=0,winy=0,radius=25,title='INS window',bg='#313131',titlebg='#111111',icon=None):
        # 基础设施--------------------------------------------
        super().__init__()
        self.setattrs()
        self.run = self.mainloop
        self.radius = radius
        self.bgc = bg
        self.backbgc = get_back_color(self.bgc)
        self.titlebgc = titlebg
        self.savexy = (winx,winy)
        self.evt_pos = (winx,winy)
        self.w = w
        self.h = h
        self.outsideborder = 20
        self.geometry(f'{self.w+radius+self.outsideborder*2}x{self.h+radius+self.outsideborder}+{self.savexy[0]}+{self.savexy[1]}')
        
        self.rootcanvas = tk.Canvas(self,width=self.w+radius+self.outsideborder*2,height=self.h+radius+20*2)
        self.rootcanvas.place(x=0,y=0)
        round_rectangle(self.rootcanvas,self.outsideborder-2,self.outsideborder-2,self.w+radius+self.outsideborder+2,self.h+self.outsideborder+2,radius=radius+2,fill=self.backbgc)
        round_rectangle(self.rootcanvas,self.outsideborder,self.outsideborder,self.w+radius+self.outsideborder,self.h+self.outsideborder,radius=radius,fill=self.bgc)
        
        # 内部窗口--------------------------------------------
        self.winframe = tk.Frame(self,width=self.w,height=self.h,bg=self.bgc)
        self.winframe.place(x=self.outsideborder+self.radius/2,y=self.outsideborder,w=self.w,h=self.h)
        
        self.titlebarframe = tk.Frame(self.winframe,bg=self.titlebgc)
        self.titlebarframe.pack(side='top',fill='x')
        
        self.iconimage = tk.PhotoImage(file='./build/images/icon.png') if icon is None else icon
        self.icimage = tk.PhotoImage(file='./build/images/iconic.png')
        self.closeimage = tk.PhotoImage(file='./build/images/close.png')
        self.fullscimage = tk.PhotoImage(file='./build/images/zoomed.png')
        self.ufullscimage = tk.PhotoImage(file='./build/images/unzoomed.png')
        self.iconbtn = tk.Button(self.titlebarframe,image=self.iconimage,bg='grey',activebackground='grey',relief='flat')
        self.iconbtn.pack(side='left')
        self.titlelbl = tk.Label(self.titlebarframe,text=title,bg=self.bgc,fg='white',font=('Segoe Print',9))
        self.titlelbl.pack(side='left')
        self.closebtn = tk.Button(self.titlebarframe,image=self.closeimage,bg='grey',activebackground='red',relief='flat',command=self.destroy)
        self.closebtn.pack(side='right')
        self.fullscbtn = tk.Button(self.titlebarframe,image=self.fullscimage,bg='grey',activebackground='lightgreen',relief='flat',command=self.zoomed)
        self.fullscbtn.pack(side='right')
        self.icbtn = tk.Button(self.titlebarframe,image=self.icimage,bg='grey',activebackground='lightskyblue',relief='flat',command=self.iconic)
        self.icbtn.pack(side='right')
        
        self.set_iconic()
        self.titlebarframe.bind("<Button-1>",self.get_evt_pos)
        self.titlebarframe.bind("<B1-Motion>",self.movewin)
    
    def get_evt_pos(self,event):
        self.evt_pos = (event.x,event.y)
    def movewin(self,event):
        self.geometry(f'+{round(event.x_root-self.evt_pos[0]-self.outsideborder-self.radius/2)}+{round(event.y_root-self.evt_pos[1]-self.outsideborder)}')
        self.savexy = (self.winfo_x(),self.winfo_y())
    
    def iconic(self):
        self.overrideredirect(False)
        self.state('iconic')
    def mapfunc(self,event):
        if self.state() != 'iconic' and (not self.overrideredirect()):
            self.setattrs()
    def set_iconic(self,to=True):
        if to:
            self.icbtn['command'] = self.iconic
            self.bind("<Map>",self.mapfunc)
        else:
            self.icbtn['command'] = lambda:...
            self.unbind('<Map>')
    
    def zoomed(self):
        self.setattrs()
        if self.state() == 'zoomed':
            self.fullscbtn['image'] = self.fullscimage
            self.rootcanvas.place_forget()
            self.rootcanvas.place(x=0,y=0)
            self.winframe.place_forget()
            self.winframe.place(x=self.outsideborder+self.radius/2,y=self.outsideborder,w=self.w,h=self.h)
            self.state('normal')
            self.geometry(f'+{self.savexy[0]}+{self.savexy[1]}')
        else:
            self.fullscbtn['image'] = self.ufullscimage
            self.rootcanvas.place_forget()
            self.winframe.place_forget()
            self.winframe.place(x=0,y=0,w=self.winfo_screenwidth(),h=self.winfo_screenheight())
            self.state('zoomed')
    
    def setattrs(self):
        self.attributes('-transparentcolor','#f0f0f0')
        self.attributes('-topmost',True)
        self.overrideredirect(True)

def exit():
    print('感谢体验。')
    sys.exit()

root = INSwindow(400,300,400,100,title='INSwindow(Version 0.6 DEV)')
t = tk.Tk()
t.geometry('400x300')
t.title('普通版')
# INSwindow(350,600,300,100,bg='cyan',titlebg='lightgreen')
button = tk.Button(root.winframe,bg='yellow',activebackground='red',text='全部毁灭',command=exit)
button.pack()
root.run()

exit()