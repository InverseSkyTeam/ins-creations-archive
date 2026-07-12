from xes.uploader import *
from clib import *
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
from typing import List,Union,Dict
from tkinter import font
from tkinter import filedialog
import os
from datetime import datetime
# from time import time
from tkinter.messagebox import askyesno
from io import BytesIO

up_down_index = 0
project_id = 24355413
try:
    files:List[Dict[str,str]] = eval(read_from_cloud("data",get_id(),"file",project_id))
except:
    files = []
print(files)
select_flag = 0

root = tk.Tk()
root.title("网盘")
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()
root.geometry(f"1000x600+{WIDTH//2-500}+{HEIGHT//2-325}")
root["bg"] = "#222222"

top_frame = tk.Frame(root,bg="#444444",height=30)
top_frame.pack(fill=tk.X)

canvas_top_frame = tk.Frame(root,height=30,bg="#222222")
canvas_top_frame.pack()

bottom_frame = tk.Frame(root,height=40,bg="white")
bottom_frame.pack(side="bottom",fill="x")

canvas = tk.Canvas(root,highlightthickness=0, bd=0,bg="#222222",width=980)
canvas.pack(fill=tk.BOTH,side="left")

def add_widget_to_canvas(widget):
    window_id.append(canvas.create_window((0, 40 * len(widgets)), window=widget,width=980,anchor="nw"))

def change_up_down():
    global up_down_index,files,window_id,widgets,select_flag
    up_down_index += 1
    if up_down_index%2 == 0:
        sort_button["image"] = up_image
    else:
        sort_button["image"] = down_image
    if select_flag:
        _select = files[select_flag-1]
    files = files[::-1]
    if select_flag:
        select_flag = files.index(_select)+1
    for i in window_id:
        canvas.delete(i)
    window_id = []
    widgets = []
    draw()
    select(None,select_flag-1)

sort_index = 0
Uploader = XesUploader()

def get_size(size,r=2):
    i = 0
    modes = ("B","KB","MB","GB")
    while size >= 1024:
        i += 1
        size /= 1024
    return f"{round(size,r)}{modes[i]}"

def upload_file():
    path = filedialog.askopenfilename(title='上传文件', filetypes=[('All files', '*.*')])
    if not path:
        return
    size = os.path.getsize(path)
    if size > 1024**3*2:
        # 防止滥用服务器资源，虽然不是我的
        print("不支持上传超过2GB的文件")
        return
    link = Uploader.uploadAbsolutePath(path)
    files.append({"name":path.split("/")[-1],"size":get_size(size),"date":str(datetime.now().date()),"link":link})
    save_to_cloud("data",str(files),get_id(),project_id)
    widgets.append([])
    widgets[-1].append(tk.Frame(canvas,height=40,bg="#222222"))
    add_widget_to_canvas(widgets[-1][0])
    widgets[-1][0].bind("<Enter>",lambda event,idx=-1:frame_enter(event,idx))
    widgets[-1][0].bind("<Leave>",lambda event,idx=-1:frame_leave(event,idx))
    widgets[-1][0].bind("<Button-1>",lambda event,idx=len(files)-1:select(event,idx))
    widgets[-1].append(tk.Label(widgets[-1][0],text=files[-1]["name"],bg=bg_color,fg="white",font=(None,12)))
    widgets[-1][1].place(x=get_pos("name",files[-1]["name"]),y=7)
    widgets[-1][1].bind("<Button-1>",lambda event,idx=len(files)-1:select(event,idx))

    widgets[-1].append(tk.Label(widgets[-1][0],text=files[-1]["size"],bg=bg_color,fg="white",font=(None,12)))
    widgets[-1][2].place(x=get_pos("size",files[-1]["size"]),y=7)
    widgets[-1][2].bind("<Button-1>",lambda event,idx=len(files)-1:select(event,idx))

    widgets[-1].append(tk.Label(widgets[-1][0],text=files[-1]["date"],bg=bg_color,fg="white",font=(None,12)))
    widgets[-1][3].place(x=get_pos("date",files[-1]["date"]),y=7)
    widgets[-1][3].bind("<Button-1>",lambda event,idx=len(files)-1:select(event,idx))

def download_file(event):
    info = files[select_flag-1]
    if not select_flag:
        return
    print("正在下载"+info["name"])
    path = filedialog.askdirectory(title="选择文件夹")
    if not path:
        return
    yn = askyesno("请回答","是否采用进度预览模式?(开启后可查看实时进度，但下载速度将大大减慢而且文件很有可能下载不成功)")
    if yn:
        response = requests.get(info["link"],headers={"User-Agent":"1145141919810"},stream=True)
        total = b''
        lab = tk.Label(bottom_frame,bg="white")
        lab.place(x=0,y=14)
        for i,j in enumerate(response.iter_lines()):
            total += j+b"\r\n"
            if i%1024 == 0:
                lab["text"] = f"正在下载 {get_size(len(total),0)}/{info['size']}"
                root.update()
    else:
        response = requests.get(info["link"],headers={"User-Agent":"1145141919810"},stream=False)
        total = response.content
    with open(path+"/"+info["name"],"wb") as f:
        f.write(total)
    f.close()

def delete_file(event):
    info = files[select_flag-1]
    global window_id,widgets,window_id
    if not select_flag:
        return
    yn = askyesno("删除文件",f'确定要永久删除"{info["name"]}"吗?')
    if not yn:
        return
    idx = files.index(info)
    files.remove(info)
    save_to_cloud("data",str(files),get_id(),project_id)
    for i in window_id:
        canvas.delete(i)
    window_id = []
    widgets = []
    draw()

def sort_file(event,form):
    global files,window_id,widgets,select_flag
    if select_flag:
        _select = files[select_flag-1]
    files = sorted(files,key=lambda x:x[form])
    if form == "size":
        def fn(x):
            x = x[form]
            while not x[-1].isdigit():
                x = x[:-1]
            return float(x)
        files = sorted(files,key=fn)
    if select_flag:
        select_flag = files.index(_select)+1
    for i in window_id:
        canvas.delete(i)
    window_id = []
    widgets = []
    draw()
    select(None,select_flag-1)

def preview_file(event):
    if not select_flag:
        return
    global preview_window
    info = files[select_flag-1]  
    preview_window = tk.Toplevel(root)  
    preview_window.title("预览")  
    preview_window["bg"] = "white"
    if info["name"].lower().split(".")[-1] in ("jpg", "jpeg", "png", "bmp", "gif","ico"):  # 简化检查  
        preview_picture(info)  

def preview_picture(info):  
    response = requests.get(info["link"], headers={"User-Agent": "Mozilla/5.0"})  
    response.raise_for_status()  # 检查请求是否成功
    image = Image.open(BytesIO(response.content))  
  
    # 设置窗口大小（可能需要调整以适应屏幕）
    width, height = image.size
    flag = 0
    if width >= 5/3*height:
        flag = 1
    if width > 800 or height > 480:
        if flag:
            height = height * 800 // width
            width = 800
        else:
            width = width * 480 // height
            height = 480
    # 保存对 photo 的引用，防止被垃圾回收  
    photo = ImageTk.PhotoImage(image.resize((width,height)))  # 创建一个 ImageTk.PhotoImage 对象  
    preview_image_label = tk.Label(preview_window, image=photo)  
    preview_image_label.pack()  
    
    def change_size(event):
        nonlocal width,height,photo,preview_image_label
        if event.delta > 0 :
            num = event.delta/120 if event.delta/120 < 2 else 2
            width = int(width*abs(1.1*num))
            height = int(height*abs(1.1*num))
        else:
            num = event.delta/120 if event.delta/120 < 2 else 2
            width = int(width/abs(1.1*num))
            height = int(height/abs(1.1*num))
        photo = ImageTk.PhotoImage(image.resize((width,height)))  # 创建一个 ImageTk.PhotoImage 对象  
        preview_image_label.pack_forget()  
        preview_image_label.config(image=photo)
        preview_image_label.place(relx=0.5,rely=0.5,anchor="center")

    preview_window.geometry(f"{width}x{height}+{(WIDTH-width)//2}+{(root.winfo_screenheight()-height)//2-25}") 
    preview_window.bind("<MouseWheel>",change_size)
    preview_window.mainloop()

def process_wheel(event):  
    # 根据鼠标滚轮的方向滚动 Canvas  
    if event.delta > 0:  # 滚轮向上滚动  
        canvas.yview_scroll(-1, "units")  # 向上滚动  
    else:  # 滚轮向下滚动
        canvas.yview_scroll(1, "units")  # 向下滚动

class Setting(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.config(bg="#222222")
        self.geometry(f"800x480+{WIDTH//2-400}+{HEIGHT//2-240}")
        self.title("设置")
        self.bg_label = tk.Label(self,text="设置背景",font=("宋体",15),bg="#222222",fg="white")
        self.bg_label.place(x=20,y=20)
        self.attributes("-topmost",'true')
        self.mainloop()

scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side="left", fill="y")

def configure_scroll_region(event=None):
    canvas.update_idletasks()  # 更新Canvas的大小
    canvas.config(scrollregion=canvas.bbox("all"))

canvas.bind("<Configure>", configure_scroll_region)
canvas.config(yscrollcommand=scrollbar.set)
canvas.configure(scrollregion=(0, 0, 100, 1000))
root.bind("<MouseWheel>",process_wheel)

up_image = ImageTk.PhotoImage(Image.open("up.png").resize((30,30)))
down_image = ImageTk.PhotoImage(Image.open("down.png").resize((30,30)))
bg_color = root.cget("bg")
sort_button = tk.Button(canvas_top_frame,bg=bg_color,fg="white",image=up_image,border=0,command=change_up_down,activebackground="#444444",activeforeground="white")
sort_button.pack(side="left",padx=5,pady=5,expand=False)

style = ttk.Style()
style.configure("rounded.TButton",borderwidth=3,radius=10,background="#444444",width=10)

upload_button = ttk.Button(top_frame,text="上传",style="rounded.TButton",command=upload_file)
upload_button.pack(side="right",pady=5,padx=5)

download_button = tk.Label(bottom_frame,text="下载",bg="white",fg="#888888",font=(None,11))
download_button.place(x=500,y=12)
download_button.bind("<Button-1>",lambda event:download_file(event))

name_button = tk.Label(canvas_top_frame,text="文件名",bg=bg_color,fg="white",font=(None,12))
name_button.pack(side="left",padx=200)
name_button.bind("<Button-1>",lambda event,form="name":sort_file(event,form))

date_button = tk.Label(canvas_top_frame,text="时间",bg=bg_color,fg="white",font=(None,12))
date_button.pack(side="right",padx=200)
date_button.bind("<Button-1>",lambda event,form="date":sort_file(event,form))

size_button = tk.Label(canvas_top_frame,text="大小",bg=bg_color,fg="white",font=(None,12))
size_button.pack(side="right")
size_button.bind("<Button-1>",lambda event,form="size":sort_file(event,form))

delete_button =  tk.Label(bottom_frame,text="删除",bg="white",fg="#888888",font=(None,11))
delete_button.place(x=750,y=12)
delete_button.bind("<Button-1>",lambda event:delete_file(event))

preview_button = tk.Label(bottom_frame,text="预览",bg="white",fg="#888888",font=(None,11))
preview_button.place(x=250,y=12)
preview_button.bind("<Button-1>",lambda event:preview_file(event))

setting_button = ttk.Button(top_frame,text="设置",style="rounded.TButton",command=Setting)
setting_button.pack(side="right",pady=5,padx=5)

widgets = []
def frame_enter(event,idx):
    if not select_flag:
        for i in widgets[idx]:
            i["bg"] = "#333333"

def frame_leave(event,idx):
    if not select_flag:
        for i in widgets[idx]:
            i["bg"] = bg_color

def get_pos(form,text):
    width = font.Font(family=None,size=12,weight="normal").measure(text)
    if form == "name":
        return 80+(350-width)//2
    elif form == "size":
        return 430+(200-width)//2
    return 630+(280-width)//2

def select(event,idx):
    global select_flag
    if not select_flag:
        for i in widgets[idx]:
            i["bg"] = "#81A2C3"
        select_flag = idx+1
        download_button["fg"] = "black"
        delete_button["fg"] = "black"
        preview_button["fg"] = "black"
    elif select_flag != idx+1:
        for i in widgets[idx]:
            i["bg"] = "#81A2C3"
        for i in widgets[select_flag-1]:
            i["bg"] = bg_color
        select_flag = idx+1
    else:
        select_flag = 0
        download_button["fg"] = "#888888"
        delete_button["fg"] = "#888888"
        preview_button["fg"] = "#888888"
        frame_enter(None,idx)

widgets = []
window_id = []
def draw():
    global widgets
    for i,j in enumerate(files):
        widgets.append([])
        widgets[i].append(tk.Frame(canvas,height=40,bg="#222222"))
        add_widget_to_canvas(widgets[i][0])
        widgets[i][0].bind("<Enter>",lambda event,idx=i:frame_enter(event,idx))
        widgets[i][0].bind("<Leave>",lambda event,idx=i:frame_leave(event,idx))
        widgets[i][0].bind("<Button-1>",lambda event,idx=i:select(event,idx))
        widgets[i].append(tk.Label(widgets[i][0],text=j["name"],bg=bg_color,fg="white",font=(None,12)))
        widgets[i][1].place(x=get_pos("name",j["name"]),y=7)
        widgets[i][1].bind("<Button-1>",lambda event,idx=i:select(event,idx))

        widgets[i].append(tk.Label(widgets[i][0],text=j["size"],bg=bg_color,fg="white",font=(None,12)))
        widgets[i][2].place(x=get_pos("size",j["size"]),y=7)
        widgets[i][2].bind("<Button-1>",lambda event,idx=i:select(event,idx))

        widgets[i].append(tk.Label(widgets[i][0],text=j["date"],bg=bg_color,fg="white",font=(None,12)))
        widgets[i][3].place(x=get_pos("date",j["date"]),y=7)
        widgets[i][3].bind("<Button-1>",lambda event,idx=i:select(event,idx))
draw()
configure_scroll_region()
# def p(event:tk.Event):
#     print(event.x,event.y)
# root.bind("<Button-1>",p)

window_background = tk.Toplevel(root)
window_background.geometry(f"1000x630+{WIDTH//2-500+8}+{HEIGHT//2-325}")
window_background.attributes("-topmost",'true')
window_background.overrideredirect(True)
# window_background.attributes("-topmost",'true')
# background = ImageTk.PhotoImage(Image.open(os.getcwd()+f"\\Distorted_Fate.png").crop((248,0,2048,1080)).resize((1000,600)))
background = ImageTk.PhotoImage(Image.open(os.getcwd()+f"\\Chrono Collapse.png").resize((1000,580)))
background_label = tk.Label(window_background,image=background,borderwidth=0)
background_label.pack()
last_x,last_y=WIDTH//2-500+8,HEIGHT//2-325
def move_background(event):
    global last_x,last_y
    if type(event.widget) == tk.Tk:
        last_x,last_y = event.x,event.y
        window_background.geometry(f"1000x600+{event.x+8}+{event.y+5}")
root.bind("<Configure>",move_background)
root.after(40,lambda:window_background.geometry(f"1000x600+{WIDTH//2-500+8}+{HEIGHT//2-325}"))
root.attributes("-alpha",0.7)
root.after(40,lambda:root.attributes("-topmost",'true'))
root.after(60,lambda:window_background.attributes("-topmost",'false'))
root.after(60,lambda:root.attributes("-topmost",'false'))
root.mainloop()