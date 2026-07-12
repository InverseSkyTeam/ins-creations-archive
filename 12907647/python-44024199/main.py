# https://code.xueersi.com/ide/code/7277074
import tkinter as tk
import platform
import insjhx
import sys
import os

opsystem_info = {
    'system_name': platform.system(),
    'system_fullname': platform.platform(),
    'python_ver': platform.python_version(),
    'system_info': platform.uname(),
    'username': os.getlogin(),
    'path': os.getcwd(),
}
tkwindow_transparentcolor_command = '-transparentcolor' if opsystem_info['system_name'] == 'Windows' else '-transparent'

# 圆角方法改编于网上搜集的canvas绘图公式，但精确程度更高，绘制也更慢
# 原方法精确度与现在方法精确度之比约为2:5，从锯齿变圆润
# 支持了Windows98及以上的Windows操作系统，圆角
def ret_points(x1, y1, x2, y2, radius):
    return [x1+radius, y1, x1+radius, y1, x1+radius, y1,
            x2-radius, y1, x2-radius, y1, x2-radius, y1,
            x2, y1,
            x2, y1+radius, x2, y1+radius, x2, y1+radius,
            x2, y2-radius, x2, y2-radius, x2, y2-radius,
            x2, y2,
            x2-radius, y2, x2-radius, y2, x2-radius, y2,
            x1+radius, y2, x1+radius, y2, x1+radius, y2,
            x1, y2,
            x1, y2-radius, x1, y2-radius, x1, y2-radius,
            x1, y1+radius, x1, y1+radius, x1, y1+radius,
            x1, y1]
def round_rectangle(canvas, x1, y1, x2, y2, radius, **kwargs):
    points = ret_points(x1,y1,x2,y2,radius)
    return canvas.create_polygon(points, **kwargs, smooth=True)
def change_rectangle(canvas, this, x1, y1, x2, y2, radius):
    points = ret_points(x1,y1,x2,y2,radius)
    canvas.coords(this,points)

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

class INSwindow(tk.Toplevel):
    def __init__(self,w,h,winx=0,winy=0,radius=25,title='INS window',bg='#313131',titlebg='#111111',icon=None):
        # 基础设施--------------------------------------------
        super().__init__()
        self.setattrs()
        self.run = self.mainloop
        self.titletext = title
        self.radius = radius
        self.bgc = bg
        self.backbgc = get_back_color(self.bgc)
        self.titlebgc = titlebg
        self.savexy = (winx,winy)
        self.evt_pos = (winx,winy)
        self.w = w
        self.h = h
        self.win_maxsize = (10000,10000)
        self.win_minsize = (100,50)
        self.edown = False
        self.edown2 = False
        self.outsideborder = 20
        self.geometry(f'{self.w+self.radius+self.outsideborder*2}x{self.h+self.radius+self.outsideborder}+{self.savexy[0]}+{self.savexy[1]}')
        
        self.rootcanvas = tk.Canvas(self,width=self.w+self.radius+self.outsideborder*2,height=self.h+self.radius+self.outsideborder*2)
        self.circlewin()
        self.rr1 = round_rectangle(self.rootcanvas,self.outsideborder-2,self.outsideborder-2,self.w+self.radius+self.outsideborder+2,self.h+self.outsideborder+2,radius=radius+2,fill=self.backbgc)
        self.rr2 = round_rectangle(self.rootcanvas,self.outsideborder,self.outsideborder,self.w+self.radius+self.outsideborder,self.h+self.outsideborder,radius=radius,fill=self.bgc)
        
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
        self.headisland_normal = tk.PhotoImage(file='./build/images/灵动岛普通态.png')
        self.headisland_focus = tk.PhotoImage(file='./build/images/灵动岛激活态.png')
        self.headisland_click = tk.PhotoImage(file='./build/images/灵动岛被捏态.png')
        
        self.iconbtn = tk.Button(self.titlebarframe,image=self.iconimage,bg='grey',activebackground='grey',relief='flat')
        self.iconbtn.pack(side='left')
        self.titlelbl = tk.Label(self.titlebarframe,text=self.titletext,bg=self.bgc,fg='white',font=('Segoe Print',9))
        self.titlelbl.pack(side='left')
        self.headisland = tk.Label(self.titlebarframe,image=self.headisland_normal,bg=self.titlebgc)
        self.headisland.pack(side='left',expand=True)
        self.closebtn = tk.Button(self.titlebarframe,image=self.closeimage,bg='grey',activebackground='red',relief='flat',command=self.destroy)
        self.closebtn.pack(side='right')
        self.fullscbtn = tk.Button(self.titlebarframe,image=self.fullscimage,bg='grey',activebackground='lightgreen',relief='flat',command=self.zoomed)
        self.fullscbtn.pack(side='right')
        self.icbtn = tk.Button(self.titlebarframe,image=self.icimage,bg='grey',activebackground='lightskyblue',relief='flat',command=self.iconic)
        self.icbtn.pack(side='right')
        
        self.headislandMenu = tk.Menu(self,tearoff=0,background='lightyellow')
        self.headislandMenu.add_command(label='最大化/缩小',command=self.zoomed)
        self.headislandMenu.add_command(label='最小化/显示',command=self.iconic)
        self.headislandMenu.add_command(label='圆角化/方形化',command=self.circlewin)
        
        self.set_iconic()
        self.bind("<Button-1>",self.get_evt_pos)
        self.bind("<ButtonRelease-1>",self.eup)
        self.bind("<Motion>",self.to_resize)
        self.titlebarframe.bind("<B1-Motion>",self.movewin)
        self.headisland.bind("<B1-Motion>",self.movewin)
        self.headisland.bind("<Enter>",self.headisland_enter)
        self.headisland.bind("<Leave>",self.headisland_leave)
        self.headisland.bind("<Button-1>",self.headisland_clicked)
        self.headisland.bind("<ButtonRelease-1>",self.headisland_unclicked)
    
    def circlewin(self,to='auto'):
        if to == 'auto':
            to = not self.rootcanvas.place_info()
        if to:
            self.rootcanvas.place(x=0,y=0)
        else:
            self.rootcanvas.place_forget()
    
    def headisland_enter(self,event):
        self.headisland['image'] = self.headisland_focus
    def headisland_leave(self,event):
        self.headisland['image'] = self.headisland_normal
    def headisland_clicked(self,event):
        self.headisland['image'] = self.headisland_click
    def headisland_unclicked(self,event):
        self.headisland['image'] = self.headisland_focus
        self.headislandMenu.post(event.x_root+10,event.y_root+10)
    
    def get_evt_pos(self,event):
        self.edown = True
        self.evt_pos = (event.x_root,event.y_root,self.winfo_x(),self.winfo_y(),self.winfo_width(),self.winfo_height())
    def eup(self,event):
        self.edown = False
    def movewin(self,event):
        if self.state() == 'normal':
            x = event.x_root-self.evt_pos[0]+self.evt_pos[2]
            y = event.y_root-self.evt_pos[1]+self.evt_pos[3]
            self.geometry(f'+{x}+{y}')
            self.savexy = (x,y)
    def to_resize(self,event):
        # round_rectangle(self.outsideborder-2,self.outsideborder-2,self.w+radius+self.outsideborder+2,self.h+self.outsideborder+2)
        if (event.x-self.outsideborder > self.w+self.radius-10) and \
           (event.y-self.outsideborder > self.h-10):
            self.titlelbl['text'] = '拖动以移动'
            if self.edown:
                self.edown2 = True
        elif not self.edown:
            self.edown2 = False
        elif self.titlelbl['text'] == '拖动以移动':
            self.titlelbl['text'] = self.titletext
        if self.edown2:
            neww = abs(self.evt_pos[4]+event.x_root-self.evt_pos[0])
            newh = abs(self.evt_pos[5]+event.y_root-self.evt_pos[1])
            if self.win_minsize[0] > neww-self.radius-self.outsideborder*2:
                neww = self.win_minsize[0]+self.radius+self.outsideborder*2
                self.titlelbl['text'] = '·_·瘦成竹竿了'
            elif self.win_maxsize[0] < neww-self.radius-self.outsideborder*2:
                neww = self.win_maxsize[0]+self.radius+self.outsideborder*2
                self.titlelbl['text'] = '·_·胖成小猪了'
            elif self.win_minsize[1] > newh-self.radius-self.outsideborder:
                newh = self.win_minsize[1]+self.radius+self.outsideborder
                self.titlelbl['text'] = '·_·矮得撑不住了'
            elif self.win_maxsize[1] < newh-self.radius-self.outsideborder:
                newh = self.win_maxsize[1]+self.radius+self.outsideborder
                self.titlelbl['text'] = '·_·高得快散架了'
            self.geometry(f'{neww}x{newh}')
            self.w = neww-self.radius-self.outsideborder*2
            self.h = newh-self.radius-self.outsideborder
            self.rootcanvas['width'] = self.w+self.radius+self.outsideborder*2
            self.rootcanvas['height'] = self.h+self.radius+self.outsideborder*2
            change_rectangle(self.rootcanvas,self.rr1,self.outsideborder-2,self.outsideborder-2,self.w+self.radius+self.outsideborder+2,self.h+self.outsideborder+2,self.radius+2)
            change_rectangle(self.rootcanvas,self.rr2,self.outsideborder,self.outsideborder,self.w+self.radius+self.outsideborder,self.h+self.outsideborder,self.radius)
            self.winframe['width'] = self.w
            self.winframe['height'] = self.h
            self.winframe.place_configure(w=self.w,h=self.h)
            ... # 窗口大小随之移动 同时联系get_evt_pos
    
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
        self.attributes(tkwindow_transparentcolor_command,'#f0f0f0')
        self.attributes('-topmost',True)
        self.overrideredirect(True)
    def change_attr(self,name,to):
        if name == 'maxsize':
            if to == 'unlimit':
                self.win_maxsize = (10000,10000)
            else:
                self.win_maxsize = to
        elif name == 'minsize':
            if to == 'unlimit':
                self.win_minsize = (1,1)
            else:
                self.win_minsize = to
        else:
            raise tk._tkinter.TclError('unknown-attr.It must be maxsize or minsize.')

def exit():
    print('感谢体验。')
    sys.exit()

root = INSwindow(400,300,400,100,title='INSwindow(0.11 dev)')
root.change_attr('maxsize',(800,500))
button = tk.Button(root.winframe,bg='yellow',activebackground='red',text='全部毁灭',command=exit)
button.pack()
root.run()

exit()