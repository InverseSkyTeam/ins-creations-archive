from wordcloud import *
from imageio import imread
from xesCloud import *
import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog
from PIL import Image,ImageTk
root = tk.Tk()
root.configure(background="yellow")
root.geometry("1200x650")
photo3 = 0
flag = 0
btn3 = tk.Button(root,bg = "yellow")
e = tk.Text(root,width = 90,height = 25)
var1 = tk.IntVar()
var2 = tk.IntVar()
import colorsys
from PIL import Image,ImageTk
import platform
def get_dominant_color(image):
    
#颜色模式转换，以便输出rgb颜色值
    image = image.convert('RGBA')
    
#生成缩略图，减少计算量，减小cpu压力
    image.thumbnail((200, 200))
    
    max_score = 0#原来的代码此处为None
    dominant_color = 0#原来的代码此处为None，但运行出错，改为0以后 运行成功，原因在于在下面的 score > max_score的比较中，max_score的初始格式不定
    
    for count, (r, g, b, a) in image.getcolors(image.size[0] * image.size[1]):
        # 跳过纯黑色
        if a == 0:
            continue
        
        saturation = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)[1]
       
        y = min(abs(r * 2104 + g * 4130 + b * 802 + 4096 + 131072) >> 13, 235)
       
        y = (y - 16.0) / (235 - 16)
        
        # 忽略高亮色
        if y > 0.9:
            continue
        
        # Calculate the score, preferring highly saturated colors.
        # Add 0.1 to the saturation so we don't completely ignore grayscale
        # colors by multiplying the count by zero, but still give them a low
        # weight.
        score = (saturation + 0.1) * count
        
        if score > max_score:
            max_score = score
            dominant_color = (r, g, b)
    
    return dominant_color
def change():
    global selectFileName,imgColor
    img = imread(selectFileName)
    imgColor = ImageColorGenerator(img)
    return imgColor
def get_pic():
    global photo3,flag,btn3,selectFileName
    selectFileName = tkinter.filedialog.askopenfilename(title='选择图片')
    image3 = Image.open(selectFileName)
    photo3 = ImageTk.PhotoImage(image3)
    btn3.configure(image = photo3)
    return selectFileName
def show_cloud(path1):
    image3 = Image.open(path1)
    photo3 = ImageTk.PhotoImage(image3)
    btn5 = tk.Button(root)
    btn5.configure(image = photo3)
    btn5.place(x = 0,y = 0)
def fourth():
    words = xesWord(e.get('0.0','end'))
    img = imread(selectFileName)
    if var2.get() == 1:
        Cloud = WordCloud(
            font_path="SongTi.otf",
            background_color=color,
            height=400,
            width=200,
            max_words=1000,
            max_font_size=80,
            min_font_size=2,
            font_step=2,
            mask=img).generate(words)
    else:
        Cloud = WordCloud(
            font_path="SongTi.otf",
            background_color="white",
            height=400,
            width=200,
            max_words=1000,
            max_font_size=80,
            min_font_size=2,
            font_step=2,
            mask=img).generate(words)
    if var1.get() == 1:
        change()
    try:
        Cloud.recolor(color_func = imgColor)
    except:
        pass
    if platform.system() == "Windows":
        path = tkinter.filedialog.askdirectory(title = "保存文件")+"\词云.png"
        Cloud.to_file(path)
    if platform.system() == "Darwin":
        path = tkinter.filedialog.askdirectory(title = "保存文件")+"/词云.png"
        Cloud.to_file(path)
def third():
    global var1,color,var2
    btn2.destroy()
    btn3.destroy()
    text2 = tk.Label(root,text = "请在此处输入想要添加到词云的文字:",font = ("kaiti",20),bg = "yellow")
    text2.place(x=0,y=0)
    e.place(x=0,y=30)
    c1 = tk.Checkbutton(root, bg = "yellow",text='按照图片填充颜色',variable=var1,onvalue = 1,offvalue = 0)
    c2 = tk.Checkbutton(root, bg = "yellow",text='按照图片出现次数最多的颜色填充背景',variable=var2,onvalue = 1,offvalue = 0)
    color = get_dominant_color(Image.open(selectFileName))
    btn4.configure(text = "导出词云",command = fourth)
    btn4.place(x=1065,y=600)
    c1.place(x = 0,y = 410)
    c2.place(x = 0,y = 435)
    return var1
def second():
    global btn3,btn2,btn4,e
    root.configure(background="yellow")
    btn.destroy()
    text.destroy()
    btn2 = tk.Button(root,text = "上传图片",font = ("kaiti",30),command = get_pic)
    btn4 = tk.Button(root,text = "下一步",font = ("kaiti",20),command = third)
    btn3.place(x=0,y=0)
    btn2.place(x=1000, y=300)
    btn4.place(x=1065,y=600)
text = tk.Label(root,text = "制作词云",font = ("kaiti",70),bg = "yellow")
btn = tk.Button(root,text = "开始创作",font = ("kaiti",30),command = second)
text.place(x=420, y=0)
btn.place(x=515, y=500)
root.mainloop()