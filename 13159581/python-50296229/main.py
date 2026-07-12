import strayapp
import tkinter as tk

class Myapp(strayapp.StrayApp):
    def __init__(self):
        super().__init__()
        self.size(200,200)#设置窗口大小
        self.my_title("chen")#设置标题
        tk.Label(text="test").pack()#逻辑代码
        self.help()#帮助

app = Myapp()
app.run()
