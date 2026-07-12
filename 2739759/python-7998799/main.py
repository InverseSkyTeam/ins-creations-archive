import tkinter,pygame
from PIL import Image, ImageTk
import webbrowser
from carton import *
musicNum = 0
pygame.init()
imgNum = 0
#在nameList里添加每张图片对应的名称，一定要
#和左侧你添加的图片名一一对应哦，可以自行添加
nameList = [
    "R2-D2",
    "凯洛·伦",
    "芬恩",
    "詹娜",
    "波·达默龙",
    "佐丽·布利斯",
    "丘巴卡",
    "C-3PO",
    "BB-8",
    "兰多·卡瑞辛",
    "蕾伊",
    "罗丝·蒂科",
    "D-O"
] 
music = ["帝国进行曲","Starwars"]
def nextOne():
    global root, imgNum
    imgNum = imgNum + 1
    if imgNum > len(nameList)-1:
        imgNum = 0
    button0.configure(text = nameList[imgNum])
    image3 = Image.open(nameList[imgNum]+".jpg")
    photo3 = image3.resize((337,500),Image.ANTIALIAS)
    photo3 = ImageTk.PhotoImage(photo3)
    button3.configure(image = photo3)
    button3.image = photo3
    return photo3

def lastOne():
    global root, imgNum
    imgNum = imgNum - 1
    if imgNum < 0:
        imgNum = len(nameList) - 1
    button0.configure(text = nameList[imgNum])
    image3 = Image.open(nameList[imgNum]+".jpg")
    photo3 = image3.resize((337,500),Image.ANTIALIAS)
    photo3 = ImageTk.PhotoImage(photo3)
    button3.configure(image = photo3)
    button3.image = photo3
    return photo3
def change():
    global musicNum
    musicNum = musicNum - 1
    if musicNum < 0:
        musicNum = len(music) -1
    pygame.mixer.music.load(music[musicNum]+".mp3")
    pygame.mixer.music.play(-1)
    return musicNum
pygame.mixer.music.load("帝国进行曲.mp3")
pygame.mixer.music.play(-1)
root = tkinter.Tk()
root.title("星球大战海报展示器")
button0 = tkinter.Button(root, text=nameList[imgNum])
button0.grid(row=0, column=0, columnspan=2)
#定义按钮button1，按钮显示文字"上一部"并绑定lastOne函数
button1 = tkinter.Button(root,text ="上一个", command=lastOne)
button1.grid(row=1, column=0)
button2 = tkinter.Button(root, text="下一个", command=nextOne)
button2.grid(row=1, column=1)
button3 = tkinter.Button(root, text="点我切换背景音乐", command=change)
button3.grid(row=2, column=0,columnspan=2)
image3 = Image.open("R2-D2.jpg")
photo3 = image3.resize((337,500),Image.ANTIALIAS)
photo3 = ImageTk.PhotoImage(photo3)
#给button3图片按钮添加图片photo
button3 = tkinter.Button(root,image = photo3)
#在47行用grid布局显示button3图片按钮，
#行row为2，列column为0，跨度columnspan为2
button3.grid(row=3,column=0,columnspan=2)
root.mainloop()
