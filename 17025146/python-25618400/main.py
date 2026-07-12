from tkinter import *
from tkinter.ttk import *
import os,sys,keyword
import webbrowser
import pyperclip,tkinter
from tkinter import*
from tkinter.ttk import*
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askdirectory
import requests
from tkinter import messagebox
txt = """好消息！好消息！星空模拟系统有github了！
github地址：https://github.com/wuyuhang0/Starry-Sky-System
这个代码仓库面向所有人永久免费开放，大家可以在上面下载项目，或者对此项目做出贡献。
Q1：为什么要将星空模拟系统传到github上？
A1：为了方便大家远程下载星空模拟系统的代码和素材。
Q2：github版本和xes社区版本是否有不同？
A2：肯定有不同，xes社区版本添加了水印，且运行慢，github版本为纯净无水印版，且运行稳定。
Q3：两种版本各自的优缺点？
A3：xes社区版本更加轻便，始终保持最新版，但代码可读性差，bug不能及时发现，github版本需要有本地环境，还要配置很多库，但代码可读性高，支持与作者合作，且只有稳定版才会发布到github，保证用户体验，长期保持更新，优化bug。
Q4：两种版本哪种好？
A4：作者推荐github版本，适合长期使用、学习，更加轻量化，不过xes社区版本运行更加简便，适合体验、尝鲜。
Q5：星空模拟系统更新规律是怎样的？
A5：有了新功能，先在工作室/合作者之间内测，内测无bug后发布至xes社区公测，xes社区公测一段时间后若用户体验较好就作为稳定版发布至github，github上的版本为最终稳定版。
Q6：星空模拟系统下一步更新内容？
A6：下一步更新偏重动画、教程方面，也许会出win7老式经典界面版本。
好了，大致就这些了，大家快去看看吧！"""
def s1():
    webbrowser.open("https://github.com/wuyuhang0/Starry-Sky-System")
def s2():
    webbrowser.open("https://livefile.xesimg.com/programme/python_assets/8ed0598abf4c82321ed6c718b92ea5a8.zip")
def s3():
    path = askdirectory(title = "请选择保存路径")
    bins = requests.get("https://livefile.xesimg.com/programme/python_assets/8ed0598abf4c82321ed6c718b92ea5a8.zip").content
    with open(path + "/星空系统.zip","wb") as file:
        file.write(bins)
    messagebox.showinfo("提示","下载完毕！")
def s4():
    webbrowser.open("https://code.xueersi.com/home/project/detail?lang=code&pid=21452480&version=offline&form=python&langType=python")
def s5():
    webbrowser.open("https://code.xueersi.com/home/project/detail?lang=code&pid=23744866&version=offline&form=python&langType=python")
def s6():
    xxx = Tk()
    xxx.geometry("500x600")
    xxx.title("开源地址帮助文档")
    xy = Text(xxx,width = 80,height = 50)
    xy.insert("insert",txt)
    xy.pack()
    xxx.mainloop()
def s7():
    txts = """2020年9月，也就是去年开学时，第一次诞生要制作一个模拟系统的想法，那时我完全没有想到这会是一个代码上万行的超大项目。
    2020年12月，初步搭建了系统主体框架，也就是一个可以容纳很多作品的结构。
    2021年2月，我制作好了系统UI界面，并决定了使用win10的图形化界面。
    2021年3~5月，一直在制作里面的应用，直到五月中旬，制作了二十余款应用后，初步定下了第一版。
    2021年7月，星空模拟系统发布，有了很大的热度，同时开始制作win11版本。
    2021年7月~8月中旬，将要开学时，制作了星空模拟系统win11界面版本，并发布、持续更新。
    2021年10月2日，发布星空模拟系统github版。
    这个作品一步步走到现在，全都靠了大家，在此我要感谢大家的支持。回望这段时间，真可谓路漫漫其修远兮，我也在编程之路中上下求索，我以后也会用更好的作品来面对大家！"""
    xxx = Tk()
    xxx.geometry("500x600")
    xxx.title("作品更新历史")
    xy = Text(xxx,width = 80,height = 50)
    xy.insert("insert",txts)
    xy.pack()
    xxx.mainloop()
def s8():
    txts = """星空模拟系统下一步将要更新动画、教程方面的内容，主体规划如下：
    1、搭建win7界面框架
    2、制作动画、教程
    3、收集网络上的图片、文档、视频、代码、软件等资源分享给大家
    4、制作三个星空模拟系统合计，预计称之为“星空虚拟机”
    5、更换内核，从pygame改为tkinter内核，再改为PyQt内核，使界面更美观
    6、添加文件算法，可以任意创建、修改文件
    7、增添大型游戏、全能工具等大项目
    好了，差不多就这些了，以前两个星空模拟系统是我个人制作，现在我有了方圆工作室，一个工作室的力量来制作，一定会更加强大，希望大家支持，谢谢！"""
    xxx = Tk()
    xxx.geometry("500x600")
    xxx.title("作品更新历史")
    xy = Text(xxx,width = 80,height = 50)
    xy.insert("insert",txts)
    xy.pack()
    xxx.mainloop()
root = Tk()
root.geometry("400x500")
root.title("Starry-Sky-System Helper")
Label(text = "星空模拟系统帮助",font = ("kaiti",20)).pack()
b1 = Button(text = "转到github地址",width = 60,command = s1)
b1.pack()
b2 = Button(text = "转到压缩包下载地址",width = 60,command = s2)
b2.pack()
b3 = Button(text = "直接下载安装包",width = 60,command = s3)
b3.pack()
b4 = Button(text = "转到xes社区地址(一)",width = 60,command = s4)
b4.pack()
b5 = Button(text = "转到xes社区地址(二)",width = 60,command = s5)
b5.pack()
b6 = Button(text = "开源地址帮助文档",width = 60,command = s6)
b6.pack()
b7 = Button(text = "作品更新历史",width = 60,command = s7)
b7.pack()
b8 = Button(text = "下一步更新内容",width = 60,command = s8)
b8.pack()
root.mainloop()