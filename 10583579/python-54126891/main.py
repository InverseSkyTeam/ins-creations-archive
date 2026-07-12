#coding:utf-8
from clib import *
import tkinter as tk
from tkinter import ttk,font
from PIL import Image,ImageTk

root = tk.Tk()
root.title('3000粉后の感慨(个人向)')
WIDTH,HEIGHT = root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry(f"1010x600+{WIDTH//2-505}+{HEIGHT//2-300-25}")

info = eval(read_from_cloud("info",114514,'file',24713360))
uid = get_id()
# print(info)
"""
构想：
{
    "0":[uid1,uid2],
    "1":[uid1,uid2],
    ...
    "616":{
        uid1:xxx
    }
}

"""

window_background = tk.Toplevel(root)
window_background.geometry(f"1010x600+{WIDTH//2-500+8}+{HEIGHT//2-325}")
# window_background.attributes("-topmost",'true')
background = ImageTk.PhotoImage(Image.open("background.jpg"))
background_label = tk.Label(window_background,image=background,borderwidth=0)
background_label.pack()
window_background.overrideredirect(True)
window_background.attributes("-topmost",'true')
def move_background(event):
    if type(event.widget) == tk.Tk:
        window_background.geometry(f"1010x600+{event.x+8}+{event.y+27}")

textbox = tk.Text(root,bg="#222222",fg="white",font=("宋体",15),padx=15,pady=15)
textbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar = tk.Scrollbar(root,orient=tk.VERTICAL, command=textbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
textbox.config(yscrollcommand=scrollbar.set)

textbox.tag_configure("small",font=(None,6))
textbox.tag_configure("color",foreground="#AAAAAA")
textbox.tag_configure("smallcolor",foreground="#AAAAAA",font=(None,10))
textbox.window_create("0.0",window=tk.Label(text="3000粉 感慨+投票",bg="#222222",fg="white",font=("宋体",18,"bold")),padx=(1000-font.Font(root,("宋体",18,"bold")).measure("3000粉 感慨+投票"))//2-10,pady=15)
textbox.insert(tk.END,"""我在2019年首次进入编程社区，并于2024年7月5日达成3000粉(虽然今天掉了)。下面是我的一些感想：\n
我和大多数人一样，从学而思的编程课那里知道了社区，也同大多数人一样怀着好奇与期待来到了这里。刚开""")
textbox.insert(tk.END,"\n\n","small")
textbox.insert(tk.END,"""始，我是一个默默无闻的用户，对于社区也了解甚微。后来我开始发表作品，参与评论，在这个过程中，我结""")
textbox.insert(tk.END,"\n\n","small")
textbox.insert(tk.END,"""识了许多志同道合的朋友，他们的支持和鼓励让我不断进步。我编程技术快速提高的主要时间段是在网课期间""")
textbox.insert(tk.END,"\n\n","small")
textbox.insert(tk.END,"""由于大部分时间都在家中，我在编程这个爱好上投入了大量时间，也写出了云变量、XesScript等作品。同时""")
textbox.insert(tk.END,"\n\n","small")
textbox.insert(tk.END,"""我也开始了互关，使得我的粉丝数也快速增长。这一时期社区中的成员都十分活跃，呈现出一片欣欣向荣的气""")
textbox.insert(tk.END,"\n\n","small")
textbox.insert(tk.END,"""氛，我也结识了许多编程方面的朋友如17025146,12907647,15789959,1473894,3846998等人(只写uid，还有""")
textbox.insert(tk.END,"\n\n","small")
textbox.insert(tk.END,"""很多就不写了)。然而，好景不长，网课时代结束后社区也逐渐走向没落。转眼间，那批原来最活跃的用户已升""")
textbox.insert(tk.END,"\n\n","small")
textbox.insert(tk.END,"""入高年级，准备冲刺中考了，繁重的学业加自身原因使得许多用户退站。圈子的环境也越来越差，我也逐渐销""")
textbox.insert(tk.END,"\n\n","small")
textbox.insert(tk.END,"""声匿迹。如今的社区早已没有了昔日的光辉，我也不像以前那样活跃了，但这并不代表我放弃了编程这门爱好""")
textbox.insert(tk.END,"\n\n","small")
textbox.insert(tk.END,"""我对编程的爱好诞生于社区，但不止于社区。希望未来我的编程能力和学习成绩能更上一层楼，社区也能够复苏。\n
最后，再次感谢那些在我成长过程中帮助过我的伙伴，也祝在看的你学业有成、幸福满满！""")
textbox.insert(tk.END,"""\n
下面是对我后续作品的投票，可以算是3000粉粉福吧，有兴趣的可以看看(可以点其他留言或提出其他建议，建议有可能会公开，但是不要提工作量太大的，暑假太忙了不会花多少时间在编程上)""","color")
textbox.insert(tk.END,"\n\ntips:请不要恶意篡改云变量数据或刷票，如果这种良心作品也要破坏，那我也真无话可说""","smallcolor")
textbox.insert(tk.END,"\n\n","small")
style = ttk.Style()
style.configure("qwq.TButton",background="#222222")

def vote():
    root.destroy()
    window = tk.Tk()
    votelist = [
        "A.完善之前写的tk聊天室并将网盘与其融合",
        "B.联机游戏，主题待定(可能是中国象棋、2d斗蛐蛐之类的)",
        "C.游戏类：录一把花雨庭或ec起床或phigros(录不了手元,没手机)",
        "D.爬虫作品(主题待定)",
        "E.其他(点此在下方留言框留言，有好的建议会加更多选项)"
    ]
    def on_click(idx):
        for i,j in enumerate(boollist):
            if i != idx:
                j.set(False)
        if idx==4: # 修改的话这边也要加，别忘了
            text.configure(state=tk.NORMAL)
            text.delete("1.0",tk.END)
        else:
            text.configure(state=tk.DISABLED)

    def submit():
        global info
        for k,v in enumerate(boollist):
            if v.get():
                break
        k = str(k)
        if k == "4":# 修改的话这边也要
            content = text.get("1.0","end-1c")
            if uid in info["616"]:
                info["616"][uid].append(content)
            else:
                info["616"][uid] = [content]
        else:
            info[k].append(uid)
        if save_to_cloud("info",str(info),114514,24713360):
            from tkinter.messagebox import showinfo
            showinfo("","提交成功，感谢观看≧▽≦")
        else:
            from tkinter.messagebox import showinfo
            showinfo("","提交失败，可以在评论区说一下，有可能是有bug")
        window.destroy()

    checkbuttonlist = []
    boollist = [tk.BooleanVar(),tk.BooleanVar(),tk.BooleanVar(),tk.BooleanVar(),tk.BooleanVar()] # 修改的话这边也要加，别忘了
    window.title("投票")
    window["bg"] = "#222222"
    window.geometry(f"400x450+{WIDTH//2-200}+{HEIGHT//2-250}")
    lab1 = tk.Label(window,text="投票",fg="white",bg="#222222",font=("宋体",18,"bold"))
    lab1.place(x=172,y=10)
    posy = 50
    style = ttk.Style()
    style.configure("awa.TCheckbutton",background="#222222",foreground="white")
    style.configure("pwq.TButton",background="#222222")
    for i,j in enumerate(votelist):
        checkbuttonlist.append(ttk.Checkbutton(window, text=j, variable=boollist[i],style="awa.TCheckbutton"))
        checkbuttonlist[-1].bind("<Button-1>",lambda event,idx=i:on_click(idx))
        checkbuttonlist[-1].place(x=10,y=posy)
        posy += 30
    text = tk.Text(window,font=("宋体",13),bg="#333333",fg="white",width=40,height=10)
    text.insert(tk.END,'点击"其他"才可以在此留言~')
    text.place(x=18,y=posy)
    text.configure(state=tk.DISABLED)
    button = ttk.Button(window,text="提交",style="pwq.TButton",command=submit)
    button.place(x=50,y=400)
    ttk.Button(window,text="关闭",style="pwq.TButton",command=window.destroy).place(x=260,y=400)
    window.mainloop()

textbox.window_create(tk.END,window=ttk.Button(root,text="点我进入投票页面",style="qwq.TButton",command=vote))

root.attributes("-alpha",0.7)
root.bind("<Configure>",move_background)
root.after(40,lambda:root.attributes("-topmost",'true'))
root.after(60,lambda:window_background.attributes("-topmost",'false'))
root.after(60,lambda:root.attributes("-topmost",'false'))
def fn(event):
    root.attributes("-topmost",'true')
    if event.x < 123 and event.x > 17 and event.y > 567 and event.y <593:
        vote()
window_background.bind("<Button-1>",lambda event:fn(event))
root.mainloop()