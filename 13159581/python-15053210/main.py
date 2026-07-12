from tkinter import *
root = Tk()
group = LabelFrame(root,text="最好的脚本语言是？",padx=5,pady=10)
group.pack(padx=5,pady=10)
LANGS = [
    ("c++",1),
    ("python",2),
    ("scratch",3),
    ("html",4),
    ("css",5),
    ("javascript",6)]
v = IntVar()
v.set(1)
for lang,num in LANGS:
    b = Radiobutton(group,text=lang,variable=v,value=num,indicatoron=False)
    b.pack(fill=X)
mainloop()