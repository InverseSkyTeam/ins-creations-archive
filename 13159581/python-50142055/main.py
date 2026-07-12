import tkinter as tk
from tkinter import filedialog,simpledialog,messagebox
from PIL import Image,ImageTk
import threading
import pystray as stray
import time
import sys

class StrayApp(object):
    '''
    别乱动self.start_icon()中的东西哈
    窗口大小、窗口标题自己更改
    托盘图标提供函数self.my_icon(icon_image)更改
    '''
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("200x200")
        self.root.protocol("WM_DELETE_WINDOW",self.close)

    def run(self):
        def hhhhh():
            while True:
                try:
                    if self.root.state()=='iconic':
                        self.start = False
                        self.root.withdraw()
                    self.root.update()
                except:
                    pass
        threading.Thread(target=self.start_icon).start()
        threading.Thread(target=hhhhh,daemon=True).start()
        self.root.mainloop()

    def close(self):
        self.icon.stop()
        self.root.destroy()

    def start_icon(self):
        self.start = True
        def oqc():
            self.root.destroy()
            self.icon.stop()
        def startapp():
            if self.start == False:
                self.start = True
                self.root.deiconify()
            else:
                return 0

        try:
            self.iconimage
        except AttributeError:
            image = Image.open("./图标.png")
        else:
            try:
                image = Image.open(self.iconimage)
            except:
                image = Image.open("./图标.png")
        menu = (
            stray.MenuItem(text="退出",action=oqc),
            stray.MenuItem(text="打开",action=startapp,default=True),
                )
        self.icon = stray.Icon("name",image,"托盘",menu)
        self.icon.run()

    def my_icon(self,iconimage):
        self.iconimage = iconimage

    def help(self):
        print(self.__doc__)

class DIYApp(object):
    '''
    所有主窗口控件都尽量写在self.window这个框架中
    '''
    def __init__(self):
        self.back_ground = "grey"
        self.root = tk.Tk()
        self.root.geometry("200x200+100+11")
        self.root.attributes('-topmost',True)
        self.root.overrideredirect(True)
        self.title_bar = tk.Frame(self.root, bg=self.back_ground, relief='ridge', bd=1, padx=0,
                             highlightcolor=self.back_ground,
                             highlightthickness=0)
        
        self.iconic_button = tk.Button(self.title_bar, text='—', # text='︾',
                                  bg=self.back_ground, padx=5, pady=3,
                                  bd=0, font='bold', fg='white',
                                  activebackground='lightskyblue',
                                  activeforeground='white',
                                  highlightthickness=0,
                                  cursor='hand2',
                                  command=self.iconic_window)
        
        self.close_button = tk.Button(self.title_bar, text='×',
                                 bg=self.back_ground, padx=5, pady=3, 
                                 bd=0, font='bold', fg='white',
                                 activebackground='#ff1e5e',
                                 activeforeground='white', 
                                 highlightthickness=0,
                                 cursor='hand2',
                                 command=self.root.destroy)
        title = tk.Label(self.title_bar,text="测试",bg=self.back_ground,fg="lightgreen")
        self.title_bar.pack(fill='x')
        title.pack(side='left')
        self.close_button.pack(side='right')
        self.iconic_button.pack(side='right')
        self.title_bar.bind('<B1-Motion>', self.move_window)
        self.title_bar.bind('<Button-1>', self.get_pos)

        self.window = tk.Frame(self.root)
        self.window.pack(expand=True, fill='both')

    def run(self):
        def hhhh():
            while True:
                try:
                    self.to_overrideredirect_window()
                    self.root.update()
                except:
                    pass
        threading.Thread(target=hhhh).start()
        self.root.mainloop()

    def get_pos(self,event):
        self.xwin = event.x
        self.ywin = event.y
        
    def move_window(self,event):
        self.root.geometry(f'+{event.x_root - self.xwin}+{event.y_root - self.ywin}')

    def iconic_window(self):
        self.root.overrideredirect(False)
        self.root.state('iconic')

    def to_overrideredirect_window(self):
        if self.root.state() == 'normal':
            self.root.overrideredirect(True)
        else:
            self.root.overrideredirect(False)

    def help(self):
        print(self.__doc__)

if __name__ == '__main__':
    app = StrayApp()
    app.run()
