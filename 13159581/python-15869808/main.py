from tkinter import *
root = Tk()
a = Listbox(root)
a.pack(fill=BOTH,expand=True)
for i in range(10):
    a.insert(END,str(i))
mainloop()