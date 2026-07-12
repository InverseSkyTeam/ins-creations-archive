from win32gui import *
from win32con import *
import tkinter as tk
root = tk.Tk()
 
def popup():
    hwnd = GetParent(root.winfo_id())
    res = SetWindowLong(hwnd, GWL_STYLE, GetWindowLong(hwnd, GWL_STYLE) & ~WS_CAPTION & ~WS_POPUPWINDOW)
    root.after(1, popup)

root.after(1,popup)
root.geometry('400x300')

CodeEditBox = tk.Text(root,width=60,height=20,font=('楷体',15))
CodeEditBox.pack()

root.mainloop()