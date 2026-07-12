import tkinter as tk,os
root = tk.Tk()
root.geometry("400x200")
root.title("gameeasy发布会")
root.wm_attributes('-topmost',1)
def movie1():
    os.system("1.mp4")
btn1 = tk.Button(root,text = "发布会上",command = movie1)
btn1.pack()
def movie2():
    os.system("2.mp4")
btn2 = tk.Button(root,text = "发布会中",command = movie2)
btn2.pack()
def movie3():
    os.system("3.mp4")
btn3 = tk.Button(root,text = "发布会下",command = movie3)
btn3.pack()
def movie4():
    os.system("4.mp4")
btn4 = tk.Button(root,text = "粉丝福利",command = movie4)
btn4.pack()
root.mainloop()