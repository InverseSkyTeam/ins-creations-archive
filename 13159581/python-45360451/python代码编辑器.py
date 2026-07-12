from tkinter import *
from tkinter import filedialog, messagebox
import traceback

def aaaa():
    t = text.get(1.0, END)
    try:
        exec(t)
    except Exception as b:
        bug = Tk()
        Label(bug,text=b).pack()
        bug.mainloop()
def save():
    try:
        t = text.get(1.0, END)
        f = filedialog.asksaveasfile(defaultextension=".py")
        f.write(t)
    except:
        messagebox.showinfo('提示', '保存失败')
    else:
        messagebox.showinfo('提示', '保存成功')

tk = Tk()
tk.geometry("300x400")

text = Text()
text.insert(END,"print(\"Hello World!\")")
text.pack()

b1 = Button(tk,text="运行",command=aaaa)
b1.pack(fill=X)
b2 = Button(tk,text="保存",command=save)
b2.pack(fill=X)
b3 = Button(tk,text="退出",command=tk.quit)
b3.pack(fill=X)

tk.mainloop()
