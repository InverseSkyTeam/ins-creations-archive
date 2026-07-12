import tkinter as tk
root = tk.Tk()
root.geometry('1000x300+500+500')
root.attributes("-transparentcolor","#f0f0f0")
root.attributes("-topmost",True)
root.overrideredirect(True)
label = tk.Label(root,text='我透明了！',fg='cyan',font=('楷体',100))
label.pack()
root.mainloop()