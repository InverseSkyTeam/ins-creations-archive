from tkinter import *
from tkinter import filedialog, messagebox
from tkinter import ttk
import idlelib.colorizer as idc
import idlelib.percolator as idp
import traceback
import os

class CIDE:
    def __init__(self,tk):
        tk.geometry("500x385")

        self.frame1 = Frame(tk)
        self.yscrollbar = Scrollbar(self.frame1)
        self.text = Text(self.frame1, height=23, width=500)
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
        self.b2 = ttk.Button(self.frame2, text="保存", command=self.save, width=300)
        self.b2.pack()
        self.b3 = ttk.Button(self.frame2, text="退出", command=tk.quit, width=300)
        self.b3.pack()
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
                fn.write(t + "\nimport time\ntime.sleep(3)")
            os.system("start D:\\maincode.py")
        except Exception as b:
            bug = Tk()
            Label(bug,text=b).pack()
            bug.mainloop()
    def save(self):
        try:
            t = self.text.get(1.0, END)
            f = filedialog.asksaveasfile(defaultextension=".py")
            f.write(t)
        except:
            messagebox.showinfo('提示', '保存失败')
        else:
            messagebox.showinfo('提示', '保存成功')

tk = Tk()
CIDE(tk)
tk.mainloop()
