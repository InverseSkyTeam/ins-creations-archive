from pickle import *
from easygui import *
import os
from time import *
import sys
from tkinter import *

root=Tk()
root.geometry("100x100")
root.title("日记本")

def awrite():
    b = textbox("你要写入什么")
    s = enterbox("文件名为？")
    c = os.getcwd() + "\\日记\\"+s+".txt"
    file = open(c,'wb')
    dump(b,file)
    file.close()
def aread():
    msgbox("找到保存日记的位置，并选择日记即可。")
    d = fileopenbox(default="./日记/*.txt")
    file1 = open(d,"rb")
    e = load(file1)
    textbox(msg="你选择的文件的内容如下",text=e)
Button(root,text="写入",command=awrite).pack(fill=X)
Button(root,text="读取",command=aread).pack(fill=X)
Button(root,text="关闭",command=root.quit).pack(fill=X)
mainloop()
