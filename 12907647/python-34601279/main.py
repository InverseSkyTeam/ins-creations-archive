from PIL import Image, ImageTk
import tkinter as tk

def get_pos(event):
    global xwin
    global ywin
    xwin = event.x
    ywin = event.y

def move_window(event):
    root.geometry(f'+{event.x_root - xwin}+{event.y_root - ywin}')

def change_on_hovering(event):
    close_button['bg'] = 'red'
    close_button['fg'] = 'lightgreen'

def return_to_normal_state(event):
    close_button['bg'] = back_ground
    close_button['fg'] = 'white'

def change_on_hovering2(event):
    iconic_button['bg'] = 'grey'
    iconic_button['fg'] = 'lightgreen'

def return_to_normal_state2(event):
    iconic_button['bg'] = back_ground
    iconic_button['fg'] = 'white'

def iconic_window():
    root.overrideredirect(False)
    root.state('iconic')

def to_overrideredirect_window():
    if root.state() == 'normal':
        root.overrideredirect(True)
    else:
        root.overrideredirect(False)

# main
back_ground = "#0a0a0a"

root = tk.Tk()
root.state('normal')
root.overrideredirect(True)

root.geometry('400x100+200+200')

title_bar = tk.Frame(root, bg=back_ground, relief='raised', bd=1, 
                     highlightcolor=back_ground, 
                     highlightthickness=0)

iconic_button = tk.Button(title_bar, text='—', # text='︾',
                          bg=back_ground, padx=5, pady=3,
                          bd=0, font='bold', fg='white',
                          activebackground='lightskyblue',
                          activeforeground='white',
                          highlightthickness=0,
                          command=iconic_window)

close_button = tk.Button(title_bar, text='×',
                         bg=back_ground, padx=5, pady=3, 
                         bd=0, font='bold', fg='white',
                         activebackground='#ff1e5e',
                         activeforeground='white', 
                         highlightthickness=0,
                         command=root.destroy)

title_window = 'IX编辑器V0.1[INS-jhx]'
title_name = tk.Label(title_bar, text=title_window, bg=back_ground, fg='white')
icon = ImageTk.PhotoImage(Image.open("IXcodelogo.png"))
title_icon = tk.Label(title_bar, bg=back_ground, image=icon)

window = tk.Canvas(root, bg="#2d2d2d", highlightthickness=0)
title_bar.pack(expand=True, fill='x')
title_icon.pack(side='left')
title_name.pack(side='left')
close_button.pack(side='right')
iconic_button.pack(side='right')
window.pack(expand=True, fill='both')
title_bar.bind("<B1-Motion>", move_window)
title_bar.bind("<Button-1>", get_pos)
close_button.bind('<Enter>', change_on_hovering)
close_button.bind('<Leave>', return_to_normal_state)
iconic_button.bind('<Enter>', change_on_hovering2)
iconic_button.bind('<Leave>', return_to_normal_state2)

while True:
    try:
        to_overrideredirect_window()
        root.update()
    except:
        break