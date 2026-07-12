'''
恭喜你，获得了一个十分有用的英语 学习工具。
不过，这个工具要作为礼物送 给小朋友有点太简陋了
能借助学过 的知识，自己选择窗口背景、排布按钮、 
的字体颜色，做出一个更炫酷的 英语学习助手呢！
'''
import requests,tkinter
from bs4 import BeautifulSoup
from xes.tool import *
history = {}
love = {}
history_list = []
love_list = []
def search():
    global listb, e1, history,history_list
    word = e1.get()
    #在13行补充代码，拼接get获取到的待翻译词语到url中
    url = "http://www.iciba.com/word?w=" + word
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"lxml")
    data = soup.find(name="ul", class_="Mean_part__1RA2V").find_all(name="span")
    #在18行补充清除列表框内容的语句，要求从首行到末行全部清除
    listb.delete(0,tkinter.END)
    history_list = []
    for n in data:
        listb.insert(0, n.text)
        history_list.append(n.text)
        history[word] = history_list
def love1():
    global listb, e1, love,love_list
    word = e1.get()
    #在13行补充代码，拼接get获取到的待翻译词语到url中
    url = "http://www.iciba.com/word?w=" + word
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"lxml")
    data = soup.find(name="ul", class_="Mean_part__1RA2V").find_all(name="span")
    #在18行补充清除列表框内容的语句，要求从首行到末行全部清除
    listb.delete(0,tkinter.END)
    listb.insert(0,"已将"+word+"加入收藏夹")
    love_list = []
    for n in data:
        love_list.append(n.text)
        love[word] = love_list
def look_at_history():
    global history
    listb.delete(0,tkinter.END)
    for i,j in history.items():
        listb.insert(0,"-----------------------------------------------------------------------------------------------------------------")
        listb.insert(0,"以上为"+str(i)+"的全部释义")
        for k in j:
            listb.insert( 0 ,"\n"+str(k))
def look_at_love():
    global love
    listb.delete(0,tkinter.END)
    for i,j in love.items():
        listb.insert(0,"-----------------------------------------------------------------------------------------------------------------")
        listb.insert(0,"以上为"+str(i)+"的全部释义")
        for k in j:
            listb.insert( 0 ,"\n"+str(k))
def download_history():
    with open("历史记录.txt","w",encoding = "utf-8")as file:
        for i,j in history.items():
            file.write("\n-----------------------------------------------------------------------------------------------------------------\n")
            file.write("以下为"+str(i)+"的全部释义")
            for k in j:
                file.write("\n"+str(k))
    xopen()
def download_love():
    with open("收藏夹.txt","w",encoding = "utf-8")as file:
        for i,j in love.items():
            file.write("\n-----------------------------------------------------------------------------------------------------------------\n")
            file.write("以下为"+str(i)+"的全部释义")
            for k in j:
                file.write("\n"+str(k))
    xopen()
root = tkinter.Tk()
root.title("翻译器")
#可以在23行修改主窗口的颜色
root.configure(background="black")
#利用Entry定义输入控件e1，要求输入框的粗细为5
e1 = tkinter.Entry(root,bd = 5)
e1.grid(row = 0,column = 0)
button1 = tkinter.Button(root, text="翻译", command=search)
button2 = tkinter.Button(root, text="历史记录",command = look_at_history)
button3 = tkinter.Button(root, text="收藏", command = love1)
button4 = tkinter.Button(root, text="收藏夹",command = look_at_love)
button5 = tkinter.Button(root, text="导出历史记录",command = download_history)
button6 = tkinter.Button(root, text="导出收藏夹",command = download_love)
button1.grid(row = 0,column = 1)
button2.grid(row = 0,column = 2)
button3.grid(row = 0,column = 3)
button4.grid(row = 0,column = 4)
button5.grid(row = 0,column = 5)
button6.grid(row = 0,column = 6)
#自定义列表框的宽width、高height、背景颜色bg、字体颜色fg（不要丢掉重要的第一个参数主窗口名哦！）
listb = tkinter.Listbox(root,width = 65,height = 24,bg = "black",fg = "white")
listb.grid(row = 1,column = 0,columnspan=7)
root.mainloop()