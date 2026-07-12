from tkinter import *
from tkinter import filedialog, messagebox
from tkinter import ttk
import idlelib.colorizer as idc
import idlelib.percolator as idp
import traceback
import os
import uploader as ul
import requests as r
from PIL import Image,ImageTk
import os

class CIDE:
    def __init__(self,tk):
        tk.geometry("500x485+0+10")
        tk.overrideredirect(True)
        tk.attributes("-topmost",True)

        self.title_frame = Frame(tk)
        self.title_label = Label(self.title_frame,bg="grey",height=2,fg="lightgreen",text="CIDE　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　")
        self.title_label.grid(row=0,sticky=W)
        self.title_label.bind("<B1-Motion>", self.move_window)
        self.title_close = Button(self.title_frame,bg="grey",text="×",activebackground='#ff1e5e',activeforeground='white',padx=5,fg="white",pady=3,command=self.callback)
        self.title_close.grid(row=0,sticky=E)
        self.title_frame.pack()

        self.frame1 = Frame(tk)
        self.yscrollbar = Scrollbar(self.frame1)
        self.text = Text(self.frame1, height=23, width=500,font=(None,12))
        self.yscrollbar.pack(side=RIGHT, fill=Y)
        self.text.pack()
        self.yscrollbar.config(command=self.text.yview)
        self.text.insert(END, "print(\"Hello World!\")")
        self.configCodeHighlight(self.text)
        self.text.config(yscrollcommand=self.yscrollbar.set)
        self.frame1.pack()

        self.frame2 = Frame(tk)
        self.b1 = ttk.Button(self.frame2, width=300, text="运行", command=self.aaaa)
        self.b1.pack()

        self.menub1 = ttk.Menubutton(self.frame2,text="                                                      保存文件",width=300)
        self.menub1.pack()
        self.menu = Menu(self.menub1,tearoff=False)
        self.menu.add_command(label="本地保存",command=self.save)
        self.menu.add_command(label="云端保存", command=self.cloud_save)
        self.menub1.config(menu=self.menu)

        self.b4 = ttk.Menubutton(self.frame2, text="                                                      打开文件", width=300)
        self.b4.pack()
        self.menu2 = Menu(self.b4, tearoff=False)
        self.menu2.add_command(label="本地代码打开", command=self.open)
        self.menu2.add_command(label="云端代码打开", command=self.cloud_run)
        self.b4.config(menu=self.menu2)

        self.frame2.pack()
    def configCodeHighlight(self,component: Text):
        idc.color_config(self.text)
        p = idp.Percolator(self.text)
        d = idc.ColorDelegator()
        p.insertfilter(d)
    def aaaa(self):
        t = self.text.get(1.0, END)
        try:
            with open("D:\\maincode.py", "w", encoding="utf-8") as fn:
                fn.write(t + "\ninput(\"按回车退出\")")
            os.system("start D:\\maincode.py")
        except Exception as b:
            bug = Tk()
            Label(bug,text=b).pack()
            bug.mainloop()
    def save(self):
        try:
            t = self.text.get(1.0, END)
            f = filedialog.asksaveasfile(defaultextension=".py")
            f.write(t + "\ninput(\"按回车退出\")")
        except:
            messagebox.showinfo('提示', '保存失败')
        else:
            messagebox.showinfo('提示', '保存成功')
    def cloud_save(self):
        def abcde():
            uploader = ul.XesUploader()
            path = "C:\\"+e2.get()+".py"
            f = open(path,"w")
            f.write(self.text.get(1.0,END))
            f.close()
            url = uploader.uploadAbsolutePath(path)
            ct.insert(END, "文件的路径是：" + url)
        top = Toplevel()
        label = Label(top,text="请输入要云端保存的文件名:")
        e2 = ttk.Entry(top)
        cb = ttk.Button(top,text="提交",command=abcde)
        ct = Text(top)
        label.pack()
        e2.pack()
        cb.pack()
        ct.pack()


    def cloud_run(self):
        def bbbbbbbb():
            try:
                url = e1.get()
                #print(url)
                head = {
                    "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11"
                }
                res = r.get(url, headers=head)
                res.encoding = res.apparent_encoding
                self.text.delete("1.0", "end")
                self.text.insert(END, res.text)
            except:
                messagebox.showinfo(message="输入网址有误")
        get_url = Toplevel()
        get_url.geometry("200x100")
        Label(get_url,text="请输入文件路径:")
        e1 = ttk.Entry(get_url,width=150)
        e1.pack()
        Label(get_url,text="注意，云端打开有可能导致代码出错，请谨慎使用")
        ttk.Button(get_url,text="确认",command=bbbbbbbb).pack()
    def open(self):
        path = filedialog.askopenfilename(initialdir="C:\\")
        with open(path,"r",encoding="UTF-8") as file:
            self.text.delete("1.0", "end")
            self.text.insert(END,file.read())

    def move_window(self,event):
        tk.geometry("+{0}+{1}".format(event.x_root, event.y_root))

    def callback(self):
        if messagebox.askyesno('关闭', '您确定要关闭CIDE吗?'):
            tk.destroy()
        else:
            pass

tk = Tk()
CIDE(tk)
tk.mainloop()
