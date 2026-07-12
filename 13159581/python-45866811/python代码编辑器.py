from tkinter import *
from tkinter import filedialog, messagebox
import idlelib.colorizer as idc
import idlelib.percolator as idp
import traceback

def configCodeHighlight(component: Text):
    idc.color_config(text)
    p = idp.Percolator(text)
    d = idc.ColorDelegator()
    p.insertfilter(d)
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
tk.geometry("300x395")

frame1 = Frame(tk)
yscrollbar = Scrollbar(frame1)
text = Text(frame1,height=23,width=300)
yscrollbar.pack(side=RIGHT,fill=Y)
text.pack() 
yscrollbar.config(command=text.yview)
text.insert(END,"print(\"Hello World!\")")
configCodeHighlight(text)
text.config(yscrollcommand=yscrollbar.set)
frame1.pack()

frame2 = Frame(tk)
b1 = Button(frame2,width=300,text="运行",command=aaaa)
b1.pack()
b2 = Button(frame2,text="保存",command=save,width=300)
b2.pack()
b3 = Button(frame2,text="退出",command=tk.quit,width=300)
b3.pack()
frame2.pack()

tk.mainloop()
