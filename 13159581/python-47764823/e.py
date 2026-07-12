import os
from tkinter.messagebox import *

eeee = "E:\\"

def main():
    try:
        os.startfile(eeee)
    except:
        showinfo("提示","对不起，你的电脑中没有E盘")

if __name__ == "__main__":
    main()
