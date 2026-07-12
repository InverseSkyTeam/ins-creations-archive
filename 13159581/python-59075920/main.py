import tkinter as tk
import windnd,send2trash,random,os
from tkinter import messagebox
from PIL import Image,ImageTk
y=1000
x = 50
flag=False
running = True
top_y = 1000
top_run = True
def show():
    top = tk.Toplevel()
    top.geometry("320x960+350+1000")
    top.overrideredirect(True)
    top.attributes("-transparentcolor","#f0f0f0")
    top.attributes("-topmost",True)
    image = Image.open("./images/作者5.png")
    image = image.resize((320,960))
    photo = ImageTk.PhotoImage(image)
    def destory():
        global top_run
        top_run=False
        top.destroy()
        root.geometry("40x120+50+300")
        image = Image.open("./images/作者7.png")
        image = image.resize((40,120))
        img = ImageTk.PhotoImage(image)
        label.configure(image=img)
        label.image = img

    button = tk.Button(top, image=photo, bd=0, command=destory)
    button.pack()
    def move_up():
        global top_y
        if (top_y>235):
            top.wm_geometry(f'+100+{top_y-10}')
            top_y-=10
            top.after(15, move_up)
    top.after(15,move_up)
    while top_run:
        top.update()
def get_pos(event):
    global xwin
    global ywin
    xwin = event.x
    ywin = event.y
def move_window(event):
    if flag:
        root.geometry(f'+{event.x_root - xwin}+{event.y_root - ywin}')
def dragged_files(files):
    msg = '\n'.join((item.decode('gbk') for item in files))
    if messagebox.askokcancel("","确认删除吗？"):
        for i in msg.split("\n"):
            send2trash.send2trash(i)
        image = Image.open("./images/作者13.png")
        image = image.resize((40,120))
        img = ImageTk.PhotoImage(image)
        label.configure(image=img)
        label.image = img

        def change_back():
            label.configure(image=photo)
            label.image=photo
        label.after(2000,change_back)
def move_away():
    global x,top_run,top_y
    x = root.winfo_x()
    if (x<int(root.winfo_screenwidth())):
        root.wm_geometry(f'+{x+10}+{root.winfo_y()}')
        x+=10
        root.after(15, move_away)
    else:
        top_run = True
        top_y = 1000
        show()
def move():
    global y
    if (y>300):
        root.wm_geometry(f'+50+{y-10}')
        y-=10
        root.after(15, move)
    else:
        label.bind("<B1-Motion>", move_window)
        label.bind("<Button-1>", get_pos)
        windnd.hook_dropfiles(root , func=dragged_files)

        def change_a(event):
            global x
            # image = Image.open("./images/作者"+random.choice(['1','4','6','7','8','9'])+".png")
            rand = random.choice(['1','4','5','6','7','8','9','11','17'])
            image = Image.open("./images/作者"+rand+".png")
            image = image.resize((40,120))
            img = ImageTk.PhotoImage(image)
            label.configure(image=img)
            label.image = img

            if (rand=='5'):
                x = 50
                move_away()
        label.bind("<Double-Button-1>",change_a)
root = tk.Tk()
root.geometry("40x120+50+1000")
root.overrideredirect(True)
root.attributes("-transparentcolor","#f0f0f0")
root.attributes("-topmost",True)

def show_popupmenu(event):
    popupmenu.post(event.x_root,event.y_root)
def change():
    global flag
    if (flag): flag=False
    else: flag=True
popupmenu = tk.Menu(root,tearoff=False)
popupmenu.add_command(label="(取消)固定",command=change)
def exit():
    global running
    running=False
    os._exit(200)
popupmenu.add_command(label="关闭",command=exit)
root.bind("<Button-3>",show_popupmenu)

image = Image.open("./images/作者7.png")
image = image.resize((40,120))
photo = ImageTk.PhotoImage(image)
label = tk.Label(root, image=photo, bd=0)
label.pack()
root.after(15, move)

while running:
    root.update()