import tkinter,pygame
from PIL import Image, ImageTk
import webbrowser
musicNum = 0
pygame.init()
imgNum = 0
#在nameList里添加每张图片对应的名称，一定要
#和左侧你添加的图片名一一对应哦，可以自行添加
nameList = [
    "星战海报1",
    "星战海报2",
    "星战海报3",
    "星战海报4",
    "星战海报5",
    "星战海报6",
    "星战海报7",
] 
def nextOne():
    global root, imgNum
    imgNum = imgNum + 1
    if imgNum > len(nameList)-1:
        imgNum = 0
    button0.configure(text = nameList[imgNum])
    if imgNum!=2:
        image3 = Image.open(nameList[imgNum]+".png")
    else:
        image3 = Image.open(nameList[imgNum]+".jpg")
    photo3 = ImageTk.PhotoImage(image3)
    button3.configure(image = photo3)
    button3.image = photo3
    return photo3

def lastOne():
    global root, imgNum
    imgNum = imgNum - 1
    if imgNum < 0:
        imgNum = len(nameList) - 1
    button0.configure(text = nameList[imgNum])
    if imgNum!=2:
        image3 = Image.open(nameList[imgNum]+".png")
    else:
        image3 = Image.open(nameList[imgNum]+".jpg")
    photo3 = ImageTk.PhotoImage(image3)
    button3.configure(image = photo3)
    button3.image = photo3
    return photo3
pygame.mixer.music.load("The City of Prague Philharmonic Orchestra _ John Williams _ Paul Bateman - The Imperial March.mp3")
pygame.mixer.music.play(-1)
root = tkinter.Tk()
root.title("一首帝国进行曲送给星战粉们")
button0 = tkinter.Button(root, text=nameList[imgNum])
button0.grid(row=0, column=0, columnspan=2)
#定义按钮button1，按钮显示文字"上一部"并绑定lastOne函数
button1 = tkinter.Button(root,text ="上一个", command=lastOne)
button1.grid(row=1, column=0)
button2 = tkinter.Button(root, text="下一个", command=nextOne)
button2.grid(row=1, column=1)
image3 = Image.open("星战海报1.png")
photo3 = ImageTk.PhotoImage(image3)
#给button3图片按钮添加图片photo
button3 = tkinter.Button(root,image = photo3)
#在47行用grid布局显示button3图片按钮，
#行row为2，列column为0，跨度columnspan为2
button3.grid(row=3,column=0,columnspan=2)
root.mainloop()
