from tkinter.filedialog import *
root = Tk()

def a():
    filename = askopenfilename(initialdir=r'C:\\')

Button(root,text="打开文件",command=a).pack()

def a_main():
    mainloop()


