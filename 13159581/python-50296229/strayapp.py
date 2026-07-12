import tkinter as tk
from tkinter import filedialog,simpledialog,messagebox
from PIL import Image,ImageTk
import threading
import pystray as stray
import time
import sys

class StrayApp(object):
    def __init__(self):
        self.root = tk.Tk()
        self.size()
        self.root.protocol("WM_DELETE_WINDOW",self.close)

    def size(self,x=200,y=200):
        self.root.geometry(str(x)+"x"+str(y))

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
        print('''
    别乱动self.start_icon()中的东西哈
    窗口大小用self.size(x=str,y=str)调整
    窗口标题自己更改
    托盘图标提供函数self.my_icon(icon_image)更改
    ''')
    
    def my_title(self,title='myapp'):
        self.root.title(title)

if __name__ == '__main__':
    app = StrayApp()
    app.run()
