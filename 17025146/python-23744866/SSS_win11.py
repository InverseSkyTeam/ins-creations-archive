#!/usr/bin/python
# -*- coding: utf-8 -*-

#导库
from __future__ import division
import pygame,sys,random,time,turtle
import math
from wx import *
import os
import time
import sys
from PIL import ImageGrab
from random import *
import requests
import json
from copy import *
from tkinter.ttk import Button,Entry,Radiobutton,Scrollbar
from tkinter import END,Label,Tk,StringVar,Listbox,messagebox,SINGLE,PhotoImage
# from moviepy.editor import *
import pyglet
from pyglet.media import *
import requests
import re
import os
from lxml import etree
from  selenium import webdriver
import wx
import wx.html2
import webbrowser
from PIL import Image,ImageTk
import io
import re
import requests
import tkinter as tk
import sys
from PyQt5.QtWidgets import (QWidget, QDesktopWidget,
    QMessageBox, QHBoxLayout, QVBoxLayout, QSlider, QListWidget,
    QPushButton, QLabel, QComboBox, QFileDialog)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QUrl, QTimer
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
import os, time
import configparser
from PIL import Image, ImageTk
from tkinter.filedialog import askdirectory
import tkinter.messagebox
import pyperclip 
import tkinter
from tkinter import Button
from tkinter import Label
from tkinter import Entry
from tkinter import Scale
from tkinter import Label,PhotoImage
from tkinter import messagebox
from tkinter import Toplevel
import copy
from pymediainfo import MediaInfo
import re
from tkinter import Message
import threading
from tkinter.filedialog   import askopenfilename
from tkinter.filedialog import askdirectory
from tkinter import StringVar
import os
from cefpython3 import cefpython
from pygame.locals import *
import wx
from tkinter import *
import tkinter.filedialog
import tkinter.messagebox as tmb
import urllib.request
from lxml import etree
from time import*
from tkinter import*
import wx.html2
import pygame.gfxdraw
from collections import namedtuple
from collections import deque
from pyglet import image
from pyglet.gl import *
import numpy as np
from datetime import*
import platform
import wx.html2
from pygame.color import THECOLORS as COLORS
from collections import OrderedDict
from pyglet.graphics import TextureGroup
from pyglet.window import key, mouse
from tkinter.ttk import *
from math import *
from easygui import *
import wmi
import psutil
from os import path
from sys import exit
from time import sleep
from random import choice
from itertools import product
from matplotlib import pyplot as plt
from tkinter.colorchooser import askcolor
import pygame, sys, os
from pygame.locals import *
from tkinter.messagebox import *  # 这是弹出窗口
from tkinter.filedialog import *
import math
from tkinter import ttk, messagebox, filedialog
import tkinter
from PIL import Image, ImageTk
from email.policy import default
from setuptools.sandbox import save_argv
from asyncio.protocols import Protocol
from PyQt5.QtWidgets import*
from tkinter import *
import tkinter.ttk as tk
import datetime
import tkinter.font as tf
import time
import random
import threading
import copy
from datetime import*
from win10toast import ToastNotifier
from MBPython import miniblink
from pygame.locals import QUIT, KEYDOWN
if (sys.version_info > (3, 0)):
    from tkinter import *
    from tkinter import messagebox
else:
    from Tkinter import *
import wx,tkinter
import time
import math
from math import *

#基础准备
global dakai,xuanzhong
pygame.init()
mousex, mousey = pygame.mouse.get_pos()
mouseRect = pygame.Rect(mousex,mousey,5,5)

#图片、文字、矩形对象

#矩形对象
offRect = pygame.Rect(300,710,60,60)
souRect = pygame.Rect(375,710,60,60)
zixunRect = pygame.Rect(440,710,60,60)
shezhiRect = pygame.Rect(505,710,60,60)
wenjianRect = pygame.Rect(570,710,60,60)
liulanRect = pygame.Rect(635,710,60,60)
shangdianRect = pygame.Rect(700,710,60,60)
fileRect = pygame.Rect(30,20,50,50)
musicRect = pygame.Rect(105,20,50,50)
vsRect = pygame.Rect(180,20,50,50)
comRect = pygame.Rect(255,20,50,50)
browRect = pygame.Rect(320,20,50,50)
videoRect = pygame.Rect(395,20,50,50)
txtRect = pygame.Rect(470,20,50,50)
drawsRect = pygame.Rect(545,20,50,50)
photoRect = pygame.Rect(620,20,50,50)
jisuansRect = pygame.Rect(695,20,50,50)
shuxuesRect = pygame.Rect(770,20,50,50)
ermRect = pygame.Rect(845,20,50,50)
fanyiRect = pygame.Rect(920,20,50,50)
tianqiRect = pygame.Rect(995,20,50,50)
duanxinRect = pygame.Rect(1070,20,50,50)
newsRect = pygame.Rect(30,95,50,50)
zhengRect = pygame.Rect(105,95,50,50)
aoyunRect = pygame.Rect(180,95,50,50)
konglongRect = pygame.Rect(255,95,50,50)
mincRect = pygame.Rect(330,95,50,50)
cmdRect = pygame.Rect(405,95,50,50)
planeRect = pygame.Rect(480,95,50,50)
maryRect = pygame.Rect(555,95,50,50)
erbRect = pygame.Rect(630,95,50,50)
saoRect = pygame.Rect(705,95,50,50)

#任务栏图标
offs = "win11.png"
sous = "搜索.png"
zixuns = "资讯.png"
shezhis = "设置.png"
wenjians = "文件.png"
liulans = "浏览.png"
shangdians = "商店.png"

#应用图标
dianliang = pygame.transform.scale(pygame.image.load("电量.png"),(60,60))
shengyin = pygame.transform.scale(pygame.image.load("声音.png"),(60,60))
wangluo = pygame.transform.scale(pygame.image.load("网络.png"),(60,60))
caidan = pygame.transform.scale(pygame.image.load("任务栏.png"),(1300,60))
bg = pygame.transform.scale(pygame.image.load("bg.jpeg"),(1200,800))
file = pygame.transform.scale(pygame.image.load("files.ico"),(50,50))
music = pygame.transform.scale(pygame.image.load("音乐播放器.jpeg"),(50,50))
vs = pygame.transform.scale(pygame.image.load("vscode.jpeg"),(50,50))
com = pygame.transform.scale(pygame.image.load("此电脑.png"),(50,50))
brow = pygame.transform.scale(pygame.image.load("浏览器.png"),(50,50))
video = pygame.transform.scale(pygame.image.load("视频播放器.jpeg"),(50,50))
txt = pygame.transform.scale(pygame.image.load("记事本.jpeg"),(50,50))
draws = pygame.transform.scale(pygame.image.load("画图.jpeg"),(50,50))
photo = pygame.transform.scale(pygame.image.load("图片查看器.png"),(50,50))
jisuans = pygame.transform.scale(pygame.image.load("计算器.jpg"),(50,50))
shuxues = pygame.transform.scale(pygame.image.load("数学计算.jpeg"),(50,50))
erm = pygame.transform.scale(pygame.image.load("二维码生成器.jpeg"),(50,50))
fanyi = pygame.transform.scale(pygame.image.load("翻译器.jpg"),(50,50))
tianqi = pygame.transform.scale(pygame.image.load("天气预报.jpeg"),(50,50))
duanxin = pygame.transform.scale(pygame.image.load("短信发送器.jpeg"),(50,50))
news = pygame.transform.scale(pygame.image.load("新闻查看器.jpeg"),(50,50))
zheng = pygame.transform.scale(pygame.image.load("文件整理器.png"),(50,50))
aoyun = pygame.transform.scale(pygame.image.load("奥运.jpeg"),(50,50))
konglong = pygame.transform.scale(pygame.image.load("谷歌小恐龙.jpeg"),(50,50))
minc = pygame.transform.scale(pygame.image.load("我的世界.jpeg"),(50,50))
cmd = pygame.transform.scale(pygame.image.load("cmd.jpeg"),(50,50))
plane = pygame.transform.scale(pygame.image.load("飞机大战.jpeg"),(50,50))
mary = pygame.transform.scale(pygame.image.load("超级玛丽.jpeg"),(50,50))
erb = pygame.transform.scale(pygame.image.load("2048.jpeg"),(50,50))
sao = pygame.transform.scale(pygame.image.load("扫雷.jpeg"),(50,50))

#文字
myFont = pygame.font.SysFont("STzhongsong",15)
fileText = myFont.render("文件管理器",True,(255,255,255))
musicText = myFont.render("音乐播放器",True,(255,255,255))
vsText = myFont.render("VS Code",True,(255,255,255))
comText = myFont.render("此电脑",True,(255,255,255))
browText = myFont.render("浏览器",True,(255,255,255))
videoText = myFont.render("视频播放器",True,(255,255,255))
txtText = myFont.render("记事本",True,(255,255,255))
drawsText = myFont.render("绘画板",True,(255,255,255))
photoText = myFont.render("图片处理器",True,(255,255,255))
jisuansText = myFont.render("计算器",True,(255,255,255))
shuxuesText = myFont.render("数学计算工具",True,(255,255,255))
ermText = myFont.render("二维码",True,(255,255,255))
fanyiText = myFont.render("翻译器",True,(255,255,255))
tianqiText = myFont.render("天气预报",True,(255,255,255))
duanxinText = myFont.render("短信发送器",True,(255,255,255))
newsText = myFont.render("新闻查看器",True,(255,255,255))
zhengText = myFont.render("文件整理器",True,(255,255,255))
aoyunText = myFont.render("奥运会结果",True,(255,255,255))
konglongText = myFont.render("谷歌小恐龙",True,(255,255,255))
mincText = myFont.render("我的世界",True,(255,255,255))
cmdText = myFont.render("cmd命令行",True,(255,255,255))
planeText = myFont.render("飞机大战",True,(255,255,255))
maryText = myFont.render("超级玛丽",True,(255,255,255))
erbText = myFont.render("2048游戏",True,(255,255,255))
saoText = myFont.render("扫雷游戏",True,(255,255,255))

#开头欢迎界面
messagebox.showinfo("欢迎","尊敬的用户，您好！")
messagebox.showinfo("欢迎","欢迎使用星空模拟系统(Starry Sky System,简称S.S.S模拟系统)")
messagebox.showinfo("欢迎","本系统功能齐全，有各种工具与游戏供您使用。")
messagebox.showinfo("欢迎","本系统不同于社区其他系统，本系统是完全以Python为脚本语言，采用了pygame、tkinter、wxpython等多种可视化工具打造的一款图形化模拟系统，而非文字系统。")
messagebox.showinfo("欢迎","本系统完全仿照windows 11系统的UI图形化界面制作，带给您熟悉而方便快捷的体验。")
messagebox.showinfo("欢迎","本系统虽为模拟系统，但却有许多功能与目前电脑系统有直接联系，真实与模拟的电脑系统相交融，带来真正的方便！")
messagebox.showinfo("欢迎","最后，祝您使用愉快！")

#开机动画
pygame.display.set_caption("Starry Sky System(星空系统)")
# clip = VideoFileClip('open.mp4')
# clip= clip.resize(newsize=(1280,720))
# clip.preview()

#定义应用函数

#文件管理器
from email.policy import default
from setuptools.sandbox import save_argv
from asyncio.protocols import Protocol
# from PyQt5.QtWebEngineWidgets import*
from tkinter import ttk, messagebox, filedialog
from tkinter import *
import tkinter.ttk as tk
import datetime
import tkinter.font as tf
import time
import random
import threading
def files1():
   


    class DirList(object):

        def __init__(self, initdir=None):
            # 第一个标签：self.label，就是Directory Lister v1.1
            self.top = Tk()
            self.label = Label(self.top, text='Directory Lister v1.1')
            self.label.pack()

            # 第二个标签：self.dirl，就是当前文件目录路径
            self.cwd = StringVar(self.top)  # cwd是Tk()变量，用来跟踪当前所在目录的名字，以字符串形式？现在并没有将值传入
            self.dirl = Label(self.top, fg='blue', font=('Helvetica', 12, 'bold'))
            self.dirl.pack()

            # 定义整个GUI程序核心，即主体部分，用框架（包含列表框和滚动条）这一组件形式表现
            self.dirfm = Frame(self.top)  # 框架组件，纯容器，包含其他组件
            self.dirsb = Scrollbar(self.dirfm)  # 滚动条，在这里是对列表框提供滚动功能
            self.dirsb.pack(side=RIGHT, fill=Y)  # 将列表框放置在右侧，并且填满竖直方向
            self.dirs = Listbox(self.dirfm, height=15, width=50,
                                yscrollcommand=self.dirsb.set)
            # 列表框，参数依次是父组件、高度、宽度以及竖直方向滚动命令，其中竖直方向滚动命令就设置为滚动条
            self.dirs.bind('<Double-1>',
                           self.setDirAndGo)  # 绑定回调函数setDirAndGo，但是'<Double-1>'是指鼠标双击列表框中的任意一项内容时，调用回调函数setDirAndGo()
            self.dirsb.config(command=self.dirs.yview)  # 表示滚动条对列表框进行竖直方向的滚动
            self.dirs.pack(side=LEFT, fill=BOTH)  # 列表框放置在左侧，并填满框架的剩余空间(BOTH)
            self.dirfm.pack()

            # 定义输入框，收集键盘输入
            self.dirn = Entry(self.top, width=50, textvariable=self.cwd)  # textvariable参数是指输入的内容，在本例中是输入文件目录，默认值是当前文件目录
            self.dirn.bind('<Return>', self.doLS)  # 绑定回调函数doLS，但是'<Return>'是指用户在输入框输完文本后，按下回车键，就会调用函数doLS()
            self.dirn.pack()

            # 定义按钮框架，包含三个按钮
            self.bfm = Frame(self.top)
            self.clr = Button(self.bfm, text='Clear', command=self.clrDir, activeforeground='white',
                              activebackground='blue')  # "clear"按钮，回调函数是清楚所有文件clrDir()
            self.ls = Button(self.bfm, text='List Directory', command=self.doLS, activeforeground='white',
                             activebackground='green')  # "go"按钮，回调函数是doLS()
            self.quit = Button(self.bfm, text='Quit', command=self.top.quit, activeforeground='white',
                               activebackground='red')  # 退出按钮
            self.clr.pack(side=LEFT)
            self.ls.pack(side=LEFT)
            self.quit.pack(side=LEFT)
            self.bfm.pack()

            # 初始化GUI程序，从当前目录开始，不理解。
            if initdir:
                self.cwd.set(os.curdir)
                self.doLS()

        # clr按钮的回调函数，清空Tk字符串变量cwd
        def clrDir(self, ev=None):
            self.cwd.set('')

        # 列表框回调函数，设置了要达到的目录，以及调用doLS()函数
        def setDirAndGo(self, ev=None):
            check = self.dirs.get(
                self.dirs.curselection())  # 列表框的get()方法是得到列表中的所有值(未传入参数)，在传入参数（行号）的情况下是获得所选中的选项；curselection()是返回选中的元素的行号
            if not check:
                check = os.curdir
            self.cwd.set(check)  # 将cwd跟踪至列表框中某项目录
            self.doLS()

        # 整个GUI程序的关键，负责安全检查，若无问题，则调用os.listdir()取得新文件集合，并替换列表框列表
        def doLS(self, ev=None):
            # 安全检查
            error = ''  #error归零
            tdir = self.cwd.get()  # 以字符串形式返回cwd追踪目录
            if not tdir: tdir = os.curdir  # 若为空，则tdir设为当前目录

            if not os.path.exists(tdir):  # 文件不存在
                error = tdir + ': no such file'
            elif not os.path.isdir(tdir):  # 文件路径不存在
                error = tdir + ': not a directory'

            # 若有错误，则最终目录设置为当前目录
            if error:
                self.cwd.set(error)  # 将cwd设为error
                self.top.update()  # 刷新页面
                sleep(2)
                if not (hasattr(self, 'last') and self.last):
                    self.last = os.curdir
                self.cwd.set(self.last)  # 重新设置cwd为当前目录
                self.dirs.config(selectbackground='LightSkyBlue')
                self.top.update()  #刷新页面
                return

            self.cwd.set('FETCHING DIRECTORY CONTENTS...')
            self.top.update()
            dirlist = os.listdir(tdir)  # 列出文件目录tdir下所有文件
            dirlist.sort()  # 排序
            os.chdir(tdir)  # 将当前工作目录设置为tdir
            self.dirl.config(text=os.getcwd())  # 配置，将第二个标签内容定为当前工作目录
            self.dirs.delete(0, END)  # 删除旧目录下列表框的内容
            self.dirs.insert(END, os.curdir)  # 在新目录列表框的最后加入当前目录
            self.dirs.insert(END, os.pardir)  # 在新目录列表框的最后加入当前目录的上一级目录
            for eachFile in dirlist:  # 在新目录的列表框中，加入新目录下的所有文件
                self.dirs.insert(END, eachFile)
            self.cwd.set(os.curdir)
            self.dirs.config(selectbackground='LightSkyBlue')


    def main():
        d = DirList(os.curdir)
        mainloop()


    if __name__ == "__main__":
        main()

#Vs Code编辑器
import requests
import requests
import json
import time
import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askdirectory
import tkinter.messagebox
import os
from tkinter import messagebox
cf_py_name = 'Create file'
def mkdir(path):
    import os
    path=path.strip()
    path=path.rstrip("\\")
    isExists=os.path.exists(path)
    if not isExists:
        os.makedirs(path) 
        return True
    else:
        return False
from time import *
import tkinter as tk
import tkinter.filedialog
import os
import random
mkpath="D:\\system_jhxc\\python_file"
mkdir(mkpath)

colorList = ['red','blue','black','white','orange','green','yellow','purple','skyblue','pink','lightskyblue']

errors = {"Syntax": "发现错误：等级/低级错误：优先检查：中英文；冒号、括号是否缺少；结构完整 等~",
"Type": "发现错误：等级/低级错误：您的程序中存在TypeError类型异常，检查您的数据类型输入是否准确，需不需要进行转换/字典的键值 等~",
"Value": "发现错误：等级/低级错误：您的程序中存在ValueError值错误，检查您需不需要进行转换/字典的键值 等~",
"Name": "发现错误：等级/超低级错误：NameError（命名错误）请检查您变量等的调用哦~",
"Attribute": "发现错误：等级/低级错误：Attribute（属性错误），请检查您的函数及成员等的调用哦~",
"Index&Key": "发现错误：等级/低级错误：您的程序中出现了下标异常，请检查您的下标使用；查看数据的错误，键值错误，如KeyError,IndexError~",
"IndentationError": "发现错误：等级/超低级错误：IndentationError：缩进有问题，仔细检查~",
"ImportError": "发现错误：等级/低级错误：ImportError：导入的库有问题，检查库的拼写与安装~",
"OS": "发现错误：等级/高级错误：出现操作系统相关异常~",
"Warn": "发现错误：等级/中级错误：您的程序中存在警告，请修复~",
"Others": "您的程序中有些非常见的异常哦！请您仔细检查！我没有安排此错误~"}
def codes():
    
    
    def bgcolorf():
        global colorList
        a1 = random.choice(colorList)
        while a1 == textbox['bg'] or a1 == textbox['fg']:
            a1 = random.choice(colorList)
        textbox['bg'] = a1
        a2 = random.choice(colorList)
        while a2 == bgcolorbutton['bg'] or a2 == bgcolorbutton['fg']:
            a2 = random.choice(colorList)
        bgcolorbutton['bg'] = a2
    
    def fgcolorf():
        global colorList
        b1 = random.choice(colorList)
        while b1 == textbox['bg'] or b1 == textbox['fg']:
            b1 = random.choice(colorList)
        textbox['fg'] = b1
        b2 = random.choice(colorList)
        while b2 == bgcolorbutton['bg'] or b2 == bgcolorbutton['fg']:
            b2 = random.choice(colorList)
        bgcolorbutton['fg'] = b2
    
    def run_main():
        ptextbox = textbox.get('1.0',tk.END)
        try:
            exec(ptextbox)
        except SyntaxError:
            error = errors["Syntax"]
            messagebox.showerror('error:错误',error)
        except TypeError:
            error = errors["Type"]
            messagebox.showerror('error:错误',error)
        except ValueError:
            error = errors["Value"]
            messagebox.showerror('error:错误',error)
        except NameError:
            error = errors["Name"]
            messagebox.showerror('error:错误',error)
        except AttributeError:
            error = errors["Attribute"]
            messagebox.showerror('error:错误',error)
        except (IndexError, KeyError):
            error = errors["Index&Key"]
            messagebox.showerror('error:错误',error)
        except IndentationError:
            error = errors["IndentationError"]
            messagebox.showerror('error:错误',error)
        except ImportError:
            error = errors["ImportError"]
            messagebox.showerror('error:错误',error)
            ask_mode = messagebox.askyesno('a question','若无拼写错误，是否要安装此库？（如果是拼写错误或不要安装点击否）')
            if ask_mode:
                ask_is_ok = messagebox.askyesno('a question','已经对目前代码存档点击是，没有则点击否（如果未存档却点击了“是”，您将付出代价）')
                if ask_is_ok:
                    root.destroy()
                    exec(ptextbox)
                else:
                    messagebox.showinfo('温馨提示','温馨提示:请先存档哦，不然代码会丢掉啊~')
            else:
                messagebox.showinfo('温馨提示','温馨提示:请继续认真地编写代码吧~')
        except OSError:
            error = errors["OS"]
            messagebox.showerror('error:错误',error)
        except Warning:
            error = errors["Warn"]
            messagebox.showerror('error:错误',error)
        except Exception:
            error = errors["Others"]
            messagebox.showerror('error:错误',error)
    
    def run_main2(event):
        run_main()
    
    def readf():
        filenames = tk.filedialog.askopenfilenames(initialdir='D:/system_jhxc/python_file',title='选择文件',filetypes=[("Text files", "*.txt")])
        if len(filenames) != 0:
            filename =""
            for i in range(0,len(filenames)):
                filename += str(filenames[i])
        try:
            with open(filename,'r') as f:
                mybook = f.read()
                textbox.insert('1.0',mybook)
                svtext.set(os.path.basename(filename)[:-4])
                f.close()
        except:
            messagebox.showinfo('温馨提示','温馨提示:您选择了错误的文件或者没有选择文件~')
    
    def readf2(event):
        readf()
    
    def savef():
        pyfilename = entry.get()
        if (pyfilename == '请输入作品名称') or (pyfilename == '') or (pyfilename == ' ') or ('lj' in pyfilename) or ('垃圾' in pyfilename) or ('滚' in pyfilename) or ('傻' in pyfilename) or ('死' in pyfilename) or ('烂' in pyfilename) or ('坏' in pyfilename):
            messagebox.showinfo('温馨提示','温馨提示:快给您的作品取一个有趣、吸引人、正能量的名字吧~')
        else:
            with open('D:/system_jhxc/python_file/'+str(pyfilename)+'.txt','w') as f:
                f.write(textbox.get('1.0','end'))
                f.close()
                messagebox.showinfo('温馨提示','存档完成~')
    
    def savef2(event):
        savef()
    
    def delf():
        filenames = tk.filedialog.askopenfilenames(initialdir='D:/system_jhxc/python_file',title='选择文件',filetypes=[("Text files", "*.txt")])
        if len(filenames) != 0:
            filename =""
            for i in range(0,len(filenames)):
                filename += str(filenames[i])
        try:
            os.remove(filename)
        except:
            messagebox.showinfo('温馨提示','温馨提示:您选择了错误的文件或者没有选择文件~')
    
    def print_savef():
        print('*=存档文件夹中的文件名-------------------------')
        codefilelist = os.listdir('D:/system_jhxc/python_file/')
        if codefilelist == []:
            print('好像没有存档过任何文件，快去存档吧~')
        for i in codefilelist:
            print('\033[1;32m文件名*--',i,' '*5,'\033[1;36m排序*--第',codefilelist.index(i)+1,'个文件\033[0m')
        
    
    def how_to_write():
        messagebox.showinfo('帮助-如何编写','1.菜单栏可以存档、读档、帮助\n2.在方框（初始黑色）内编写代码，不仅支持自带库如pygame,而且还支持自导三方库\n3.回车下一行，滚轮翻代码的事不要问了\n4.按钮：可以切换你喜欢的背景颜色、字体颜色，点击运行将会运行你编写的代码，若有错会自动提示错误信息')
    def howCanUseku():
        messagebox.showinfo('帮助-如何使用库','1.python自带库，如：pygame,time,turtle,random等都会用吧\n2.三方库，如：numpy,pyQt5,pandas,bs4等可以先存档，然后再在代码里写“import 库名”以安装')
    def no_code_can_do():
        messagebox.showinfo('怎木办','你直接不要点运行，直接把我当成文件编辑器用就好啦~存读档等的方法还是要看的，在帮助的别的选项里面！')
    def clear_code():
        askclear = messagebox.askyesno('你确定？？？','阅读后点击“确定”则清空，“取消”则不清空\n清空需要满足的条件:\n1.你确定要删除？？？\n2.你已经存档了')
        if askclear:
            textbox.delete('1.0',tk.END) # tk.END就是'end'，耍酷而已
        else:
            pass
    def clear_code2(event):
        clear_code()
    def look_savef():
        try:
            os.system('start D:/system_jhxc/python_file/')
        except:
            messagebox.showwarning('警告','你看看你干了什么，把存档文件夹删了！')
            os.system('shutdown/s /c 既然你这样做，那就憨憨吧 /t 50')
            sleep(6)
            os.system('shutdown/a')
            messagebox.showinfo('饶恕','饶了你吧，赶紧复制了代码重新打开我再粘贴吧，这样存档文件夹就会回来')
    def undotext():
        try:textbox.edit_undo()
        except:messagebox.showinfo('提示','提示：已经无法再撤销了')
    def redotext():
        try:textbox.edit_redo()
        except:messagebox.showinfo('提示','提示：已经恢复到了最新状态')
    def lentext():
        messagebox.showinfo('字符数','字符数：'+str(len(textbox.get('1.0','end'))))
    def lentext2(event):
        lentext()
    
    
    
    roo = tk.Tk()
    
    label = tk.Label(roo,text='如代码太长用滚轮滚动哦\n输出照常在终端，其他如pygame也行\n支持导入库')
    textbox = tk.Text(roo,height=31,width=100,bg='black',fg='yellow',font=('黑体',14),undo=True)
    bgcolorbutton = tk.Button(roo,bg='green',fg='white',text=' '*81+'背景换色'+' '*81,command=bgcolorf)
    fgcolorbutton = tk.Button(roo,fg='green',text=' '*81+'字体换色'+' '*81,command=fgcolorf)
    runStart = tk.Button(roo,bg='orange',fg='white',text=' '*81+'▶运行(F5)'+' '*81,command=run_main)
    svtext = tk.StringVar(roo)
    entry = tk.Entry(roo,textvariable=svtext)
    svtext.set('请输入作品名称')
    
    entry.grid(row=0, column=0)
    label.grid(row=1, column=0)
    textbox.grid(row=2, column=0)
    bgcolorbutton.grid(row=3, column=0)
    fgcolorbutton.grid(row=4, column=0)
    runStart.grid(row=5, column=0)
    
    
    menuBar = tk.Menu(roo)
    roo.config(menu=menuBar)
    roo.bind('<Control-Alt-c>',clear_code2)
    roo.bind('<Control-Alt-t>',lentext2)
    roo.bind('<F1>',readf2)
    roo.bind('<F2>',savef2)
    roo.bind('<F5>',run_main2)
    
    fileMenu = tk.Menu(menuBar,tearoff=0,background='lightskyblue')
    menuBar.add_cascade(label="文件",menu=fileMenu)
    helpMenu = tk.Menu(menuBar,tearoff=0)
    menuBar.add_cascade(label="帮助(新手必读指引)",menu=helpMenu)
    
    fileMenu.add_command(label="读档(文本文档txt格式)",command=readf,accelerator='F1')
    fileMenu.add_command(label="存档(文本文档txt格式)",command=savef,accelerator='F2')
    fileMenu.add_command(label="选择一个存档并删除",command=delf)
    fileMenu.add_command(label="输出所有此编译器存档",command=print_savef)
    fileMenu.add_command(label="查看所有此编译器存档",command=look_savef)
    fileMenu.add_separator()
    fileMenu.add_command(label="清空代码",command=clear_code,accelerator='Ctrl+Alt+C')
    fileMenu.add_command(label="撤销←",command=undotext,accelerator='Ctrl+Z')
    fileMenu.add_command(label="重做→",command=redotext,accelerator='Ctrl+Y')
    fileMenu.add_command(label="字符数",command=lentext,accelerator='Ctrl+Alt+T')
    
    aboutMenu = tk.Menu(helpMenu,tearoff=0)
    
    helpMenu.add_command(label="如何编写",command=how_to_write)
    helpMenu.add_separator()
    helpMenu.add_command(label="库的用法",command=howCanUseku)
    helpMenu.add_separator()
    helpMenu.add_command(label="我不会py该怎么用,有用吗?",command=no_code_can_do)
    helpMenu.add_separator()
    helpMenu.add_command(label="其他问题",command=lambda:messagebox.showinfo('其他question','解决方法：在评论区回复：[01error:你要说的问题内容]'))
    
    roo.mainloop()

#系统设置、此电脑
def sysset():
    window1 = Tk() #建立窗口，把窗口储存在window中
    window1.title("系统设置") #设置标题
    window1.geometry("400x300")
    def fasdasdf():
        window1.destroy()
    def Check_state():
        wifi = Pywifi()
        iface = wifi.interfaces()[0]
        print(ifaces.status())
        if ifaces.status() == 4:
            print("此电脑已连接无线网络")
    def shuangka():
        window2 = Tk() #建立窗口，把窗口储存在window中
        window2.title("系统设置") #设置标题
        window2.geometry("800x600")
        def dual5g():
            windowsx = Tk() #建立窗口，把窗口储存在window中
            windowsx.title("if you okay to open 5G") #设置标题
            windowsx.geometry("400x300")
            Label(windowsx,text = "你确定开启5G模式？这将使你的电脑内存占用变高").pack()
            def open5g():
                messagebox.showwarning("","你现在使用的是：5G/4G/3G/2G模式")
            def close5g():
                messagebox.showwarning("","你现在使用的是4G/3G/2G模式")
            Button(windowsx,text = "是，开启5G模式",command = open5g).pack()
            Button(windowsx,text = "否，停用5G，使用4G",command = close5g).pack()
        Label(window2,text = "星空系统采用移动网络系统，因此优势在于免费、快速，5G最快下载/上传速度为：148MB/S，4G为18.5MB/S。").pack()
        Button(window2,text = "1.5G/4G/3G/2G",command = dual5g).pack()
        def dual4g():
            messagebox.showwarning("","你现在使用的是4G/3G/2G模式")
        Button(window2,text = "2.4G/3G/2G",command = dual4g).pack()
        def dual3g():
            messagebox.showwarning("","你现在使用的是3G/2G模式")
        Button(window2,text = "3.3G/2G",command = dual3g).pack()
        def dual2g():
            messagebox.showwarning("","你现在使用的是仅2G模式")
        Button(window2,text = "4.仅2G",command = dual2g).pack()
        def dual0g():
            messagebox.showwarning("","你已关闭移动数据网络")
        Button(window2,text = "5.关闭移动数据网络",command = dual0g).pack()
    def button_is_clicked():
        print("")
    def disk():
        window4 = Tk() #建立窗口，把窗口储存在window中
        window4.title("系统设置") #设置标题
        window4.geometry("700x300")
        import ctypes
        import os
        import platform
        import sys
        def get_free_space_mb(folder):
            """ Return folder/drive free space (in bytes)
            """
            if platform.system() == 'Windows':
                free_bytes = ctypes.c_ulonglong(0)
                ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(folder), None, None, ctypes.pointer(free_bytes))
                return free_bytes.value/1024/1024/1024 
            else:
                st = os.statvfs(folder)
                return st.f_bavail * st.f_frsize/1024/1024
        Label(window4,text = "计算机C标号磁盘剩余可使用空间" + str(get_free_space_mb('C:\\')) + 'GB').pack()
        Label(window4,text = "计算机D标号磁盘剩余可使用空间" + str(get_free_space_mb('D:\\')) + 'GB').pack()
        Label(window4,text = "计算机E标号磁盘剩余可使用空间(如果你没有该标号磁盘，请忽略)" + str(get_free_space_mb('E:\\')) + 'GB').pack()
        Label(window4,text = "计算机F标号磁盘剩余可使用空间(如果你没有该标号磁盘，请忽略)" + str(get_free_space_mb('F:\\')) + 'GB').pack()
        Label(window4,text = "计算机G标号磁盘剩余可使用空间(如果你没有该标号磁盘，请忽略)" + str(get_free_space_mb('G:\\')) + 'GB').pack()
    def momery():
        window3 = Tk() #建立窗口，把窗口储存在window中
        window3.title("系统设置") #设置标题
        window3.geometry("700x300")
        import psutil
        mem = psutil.virtual_memory()
        zj = float(mem.total/1024/1024/1024)
        Label(window3,text = "此计算机所有内存空间：" + str(zj) + "GB").pack()
        ysy = float(mem.used/1024/1024/1024)
        Label(window3,text = "此计算机已使用内存空间：" + str(ysy) + "GB").pack()
        kx = float(mem.free/1024/1024/1024)
        Label(window3,text = "此计算机剩余可使用内存空间:" + str(kx) + "GB").pack()
    
    Button(window1,text = "1.WLAN(要使用，请下载pywifi库，该库可能仅在笔记本电脑上可用)",command = Check_state).pack()
    Button(window1,text = "2.双卡和移动网络(不能设置双卡)",command = shuangka).pack()
    Button(window1,text = "3.蓝牙(暂时不可用)",command = button_is_clicked).pack()
    Button(window1,text = "4.飞行模式(暂时不可用)",command = button_is_clicked).pack()
    Button(window1,text = "5.计算机磁盘剩余存储空间",command = disk).pack()
    Button(window1,text = "6.计算机内存使用情况",command = momery).pack()
    window1.protocol("WM_DELETE_WINDOW",fasdasdf)
    window1.mainloop()

#浏览器
zt='楷体'
from time import *
import random
from sys import*
from cefpython3 import cefpython as cef
import platform
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog
import tkinter
import sys,os
import re
import requests
import time
from time import*
from cefpython3 import cefpython
def browsers():
    
    
    cefpython.Initialize()
        
    def pagebrowser(a,tie):

        if "https://" in a:
            a = a.replace("https://","http://")
        if "http://" not in a:
            a = "http://" + a
        cefpython.CreateBrowserSync(cefpython.WindowInfo(tie),url = a)
        cefpython.MessageLoop()
    def main(x):
        pagebrowser(x,'浏览器')
    def kmb(x,a):
        pagebrowser(x,a)


    def f (text):
        stdout.write('\r'+' '*0+'\r')
        stdout.flush()
        for df in text:
            stdout.write(df)
            stdout.flush()
            sleep(0.1)   
    def download(url):
        if url is None:
            return None
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'
        headers={'User-Agent':user_agent}
        r = requests.get(url,headers=headers)
        if r.status_code == 200:
            r.encoding = 'utf-8'
            return r.text
        return None
    def get_data(html):
        regex = re.compile('<meta name="description" content="(.*?)">')
        regex = re.compile('<div class="lemma-summary" label-module="lemmaSummary">(\s*)<div class="para" label-module="para">([\s\S]*?)</div>(\s*)</div>')
        data = [('\n', 'Python是一种计算机程序设计语言。是一种动态的、面向对象的脚本语言，最初被设计用于编写自动化脚本(shell)，随着版本的不断更新和语言新功能的添加，越来越多被用于独立的、大型项目的开发。', '\n')]
        data = re.findall(regex, html)[0][1]
        return data
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    def x(a):
        d = {
        0 : '-星期一',
        1 : '-星期二',
        2 : '-星期三',
        3 : '-星期四',
        4 : '-星期五',
        5 : '-星期六',
        6 : '-星期天',
        }
        day = a.weekday()
        return d[day]
    xxx=strftime("%Y.%m.%d.%H:%M:%S")
    rrr='日期:'+xxx
    def a():
        if e.get()=='':
            messagebox.showwarning('提示', '检测到输入框内容空白',parent=window)
        else:
            if v.get()==1:
                main(e.get())
            elif v.get()==2:
                x='https://www.baidu.com/s?ie=UTF-8&wd='+e.get()
                main(x)
            elif v.get()==3:
                #messagebox.showerror("暂不可用",'暂不可用',parent=window)
                xt=e.get()
                url = 'http://baike.baidu.com/item/{}'.format(xt)
                html_cont = download(url)
                try:
                    data = get_data(html_cont)
                    data = re.sub(r'<([\s\S]*?)>|&nbsp;|\n','',data)
                    with open(xt+'.txt', 'w', encoding='utf-8') as f:
                        f.write(data)
                        f.close()
                except:
                    data='没有这个词'
                s=Toplevel(window)
                s.title('浏览器')
                s.geometry('300x300')
                s.resizable(0,0)
                xs=Text(s, width=300, height=300)
                xs.pack()
                xs.insert("insert", data)
                s.mainloop()
            elif v.get()==4:
                x='https://cn.bing.com/search?q='+e.get()
                main(x)
            elif v.get()==5:
                x='https://www.so.com/s?ie=utf-8&fr=none&src=360sou_newhome&q='+e.get()
                main(x)
            elif v.get()==6:
                x='https://www.sogou.com/web?query='+e.get()
                main(x)
    def tcs():
        kmb('https://www.lzxweb.xyz/game/game1/','贪吃蛇')
    def bcbk():
        kmb('https://www.lzxweb.xyz/game/game3/','别踩白块')
    def wzq():
        kmb('https://www.lzxweb.xyz/game/game2/','五子棋')
    def mnfx():
        kmb('https://www.lzxweb.xyz/game/fj.html','模拟飞行')
    def MC():
        kmb('http://106.52.138.233/game/mc.html','我的世界(2D)')
    def mc():
        kmb('https://classic.minecraft.net/','我的世界(3D)')
    def g():
        messagebox.showerror("暂未开发",'暂未开发',parent=window)
    def kt():
        zt='楷体'
    def ht():
        zt='黑体'
    def hwxk():
        zt='华文行楷'

    def baidu():
        kmb('https://baidu.com/','百度')
    def rmwz():
        s=Toplevel(window)
        s.title('热门网站')
        s.geometry("500x500")
        s.resizable(0,0)
        sss='\n热门网站'
        label =Label(s,text=sss)
        label.pack()
        quit = tkinter.Button(s,text="百度",command=baidu)
        quit.place(x=100,y=100,anchor="center")
        s.mainloop()
    def game():
        s=Toplevel(window)
        s.title('游戏')
        s.geometry("500x500")
        s.resizable(0,0)
        sss='\n游戏'
        label =Label(s,text=sss)
        label.pack()
        quit = tkinter.Button(s,text="我的世界(3D)",command=mc)
        quit.place(x=100,y=100,anchor="center")
        b1 = tkinter.Button(s,text="我的世界(2D)",command=MC)
        b1.place(x=200,y=100,anchor="center")
        b2 = tkinter.Button(s,text="模拟飞行(3D)",command=mnfx)
        b2.place(x=300,y=100,anchor="center")
        b3 = tkinter.Button(s,text="贪吃蛇",command=tcs)
        b3.place(x=380,y=100,anchor="center")
        b4 = tkinter.Button(s,text="五子棋",command=wzq)
        b4.place(x=440,y=100,anchor="center")
        b5 = tkinter.Button(s,text="别踩白块",command=bcbk)
        b5.place(x=100,y=150,anchor="center")
        s.mainloop()
    def sz():
        def llqgx():
            xs=Toplevel(s)
            xs.title('设置-浏览器')
            xs.geometry("300x300")
            xs.resizable(0,0)
            sss='\n浏览器更新\n'
            label =Label(xs,text=sss)
            label.pack()
            xxx='唯一版本'
            lt =Label(xs,text=xxx)
            lt.pack()
            xs.mainloop()
        s=Toplevel(window)
        s.title('设置')
        s.geometry("500x500")
        s.resizable(0,0)
        sss='\n设置'
        label =Label(s,text=sss)
        label.pack()
        quit = tkinter.Button(s,text="个性化设置",command=g)
        quit.place(x=100,y=100,anchor="center")
        b1 = tkinter.Button(s,text="浏览器更新",command=llqgx)
        b1.place(x=180,y=100,anchor="center")
        s.mainloop()
    def blue():
        window["background"] = "blue"
    def red():
        window["background"] = "red"
    def white():
        window["background"] = "white"
    def mr():
        window["background"] = "SystemButtonFace"
    def pas():
        pass
    window = tkinter.Tk()
    window.title('浏览器')
    window.geometry("1100x300")
    window.resizable(0,0)
    #window["background"] = "white"
    #window.attributes("-topmost", True)

    label =Label(window,text='浏览器',font=(zt,30))
    label.pack()
    rq =Label(window,text=rrr)
    rq.place(x=0,y=0)
    s=Label(window,text='请输入网址或搜索的内容',font=(zt,20))
    s.place(x=550,y=60,anchor="center")
    e=Entry(window)
    e.place(width=500, height=30)
    e.place(x=500,y=100,anchor="center")
    quit = tkinter.Button(window,text="访问或搜索",command=a)
    quit.place(x=800,y=100,anchor="center")
    v = IntVar()
    v.set(1)
    R_ONE=Radiobutton(window, text="访问网站", variable=v, value=1,command=pas).place(x=250,y=150)
    R_TWO=Radiobutton(window, text="百度搜索", variable=v, value=2,command=pas).place(x=350,y=150)
    R_T=Radiobutton(window, text="百度百科", variable=v, value=3,command=pas).place(x=450,y=150)
    R_F=Radiobutton(window, text="必应搜索", variable=v, value=4,command=pas).place(x=550,y=150)
    R_FI=Radiobutton(window, text="360搜索", variable=v, value=5,command=pas).place(x=650,y=150)
    R_S=Radiobutton(window, text="搜狗搜索", variable=v, value=6,command=pas).place(x=750,y=150)
    menu = tkinter.Menu(window)
    filemenu = Menu(menu, tearoff=0)
    filemenu.add_command(label="设置",command=g)
    menu.add_cascade(label="设置",menu=filemenu)
    menu.add_command(label="游戏",command=game)
    menu.add_command(label="热门网站",command=rmwz)
    menu.add_command(label="实用工具",command=g)
    menu.add_command(label="退出",command=window.quit)
    window.config(menu=menu)
    window.mainloop()   

#视频播放器
from tkinter.ttk import Button,Entry,Radiobutton,Scrollbar
from tkinter import END,Label,Tk,StringVar,Listbox,messagebox,SINGLE,PhotoImage
"""
VIP视频解析：http://www.vipjiexi.com/
无名小站：http://www.wmxz.wang/
http://www.iqiyi.com/lib/dianying/%E5%96%9C%E5%89%A7,%E4%B8%AD%E5%9B%BD%E5%A4%A7%E9%99%86,2018_11_1.html
"""
import requests
import re
import os
from lxml import etree
from  selenium import webdriver
import wx
import wx.html2
import webbrowser
class Pro:
    header_ai={'Referer': 'http://www.iqiyi.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.17 Safari/537.36'

    }
    header_you={'Referer': 'http://list.youku.com/category/video','User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    header_pp = {'Referer': 'http://list.pptv.com/',
              'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    way=False
    def __init__(self):
        pass

    def search_movies_type(self,u_name,u_type,page):#两个参数 根据状态输出规则
        dic1 = {'m': 1, 't': 2, 'z': 6, 'd': 4, 'j': 3}
        dic2 = {'m': 96, 't': 97, 'z': 85, 'd': 100, 'j': 84}
        dic3 = {'m': 1, 't': 2, 'z': 4, 'd': 3, 'j': 210548}
        headers={}
        #爱奇艺 a/电影m:1 t:2 z:6 d:4 j:3  优酷y / m:96 t:97 z:85 d:100 j:84 pptv  p/m:1 t:2 z:4 d:3 j:210548
        url, pa_movie_title, pa_movie_url, pa_move_pic='','','',''
        url_aiqiyi='http://list.iqiyi.com/www/{}/-------------24-{}-1-iqiyi--.html'.format(dic1[u_type],page)
        url_youku='https://list.youku.com/category/show/c_{}_s_1_d_1_p_{}.html'.format(dic2[u_type],page)
        # url_pptv='http://list.pptv.com/category/type_{}.html'.format(dic3[u_type])
        url_pptv='http://list.pptv.com/channel_list.html?page={}&type={}'.format(page,dic3[u_type])
        pa_ai_movie_title = '//div[@class="site-piclist_pic"]/a[@class="site-piclist_pic_link"]/@title'
        pa_ai_movie_url = '//div[@class="site-piclist_pic"]/a[@class="site-piclist_pic_link"]/@href'
        pa_ai_movie_pic = '//div[@class="site-piclist_pic"]/a[@class="site-piclist_pic_link"]/img/@src'
        pa_you_movie_title='//div[@class="p-thumb"]/a/@title'
        pa_you_movie_url='//div[@class="p-thumb"]/a/@href'
        pa_you_movie_pic='//div[@class="p-thumb"]/img[@class="quic"]/@src'
        pa_pp_movie_title='//li/a[@class="ui-list-ct"]/@title'
        pa_pp_movie_url='//li/a[@class="ui-list-ct"]/@href'
        pa_pp_movie_pic='//li/a[@class="ui-list-ct"]/p[@class="ui-pic"]/img/@data-src2'
        if u_name=="a":#如果是爱奇艺
            url=url_aiqiyi
            pa_movie_title=pa_ai_movie_title
            pa_movie_url=pa_ai_movie_url
            pa_move_pic=pa_ai_movie_pic
            headers=self.header_ai
        elif u_name=="y":#如果是优酷
            url=url_youku
            pa_movie_title=pa_you_movie_title
            pa_movie_url=pa_you_movie_url
            pa_move_pic=pa_you_movie_pic
            headers=self.header_you

        elif u_name=="p":#如果是PPTV
            url=url_pptv
            pa_movie_title=pa_pp_movie_title
            pa_movie_url=pa_pp_movie_url
            pa_move_pic=pa_pp_movie_pic
            headers=self.header_pp

        return url,pa_movie_title,pa_movie_url,pa_move_pic,headers


    def get_movie_res(self,u_name,u_type,page):#输出电影名 链接 图片
        url, pa_movie_title, pa_movie_url, pa_move_pic,headers=self.search_movies_type(u_name,u_type,page)
        res=requests.get(url=url,headers=headers).content.decode('utf-8')
        # print(res)
        html=etree.HTML(res)
        movie_url=html.xpath(pa_movie_url)
        movie_title=html.xpath(pa_movie_title)
        movie_src_pic=html.xpath(pa_move_pic)
        print(len(movie_title),movie_title)
        print(len(movie_url),movie_url)
        print(len(movie_src_pic),movie_src_pic)
        return movie_url,movie_title,movie_src_pic

    def change_urlink(self,lis):
        for i in range(len(lis)):
            if '\\' in lis[i]:
                lis[i] = lis[i].replace('\\', '')
        # print(lis)
        return lis

    def change_youku_link(self,urls):
        pa_link='//.+[.]html'
        if re.match(pa_link,urls):
            urls='http:'+urls
        return urls

    def get_more_tv_urls(self,url,u_name,u_type):#获取电视剧分集链接
        tv_dic_new = {}
        if u_name == 'y':
            url=self.change_youku_link(url)
            res = requests.get(url, headers=self.header_you).text.encode(encoding='utf-8').decode('utf-8')
            html = etree.HTML(res)
            print(res)
            if u_type=="m" or u_type=="t":
                self.tv_more_title = html.xpath('//div[@class="item item-num"]/@title')
                self.tv_more_url = html.xpath('//div[@class="item item-num"]/a[@class="sn"]/@href')
            elif u_type=="d":
                self.tv_more_title = html.xpath('//div[@class="item item-txt"]/@title')
                self.tv_more_url = html.xpath('//div[@class="item item-txt"]/a[@class="sn"]/@href')
            elif u_type=="z":
                self.tv_more_title = html.xpath('//div[@class="item item-cover"]/@title')
                self.tv_more_url = html.xpath('//div[@class="item item-cover"]/a/@href')
            elif u_type == "j":
                self.tv_more_title = html.xpath('//div[@class="item item-cover current"]/@title')
                self.tv_more_url = html.xpath('//div[@class="item item-cover current"]/a/@href')
        elif u_name == 'a':
            res = requests.get(url, headers=self.header_ai).text.encode(encoding='utf-8').decode('utf-8')
            html = etree.HTML(res)
            print(res)
            if u_type=="m" or u_type=="t" or u_type=='d':
                self.tv_more_title = html.xpath(
                    '//ul/li[@data-albumlist-elem="playItem"]/div[@class="site-piclist_pic"]/a[1]/@title')
                self.tv_more_url = html.xpath(
                    '//ul/li[@data-albumlist-elem="playItem"]/div[@class="site-piclist_pic"]/a[1]/@href')
            elif u_type=="z" or u_type=="j":
                self.tv_more_title = html.xpath('//div[@class="recoAlbumTit"]/a[1]/@title')
                self.tv_more_url = html.xpath('//div[@class="recoAlbumTit"]/a[1]/@href')
        elif u_name == 'p':
            res = requests.get(url, headers=self.header_pp).text.encode(encoding='utf-8').decode('utf-8')
            # html = etree.HTML(res)
            self.tv_more_url2 = re.compile('{"url":"(.+?)"').findall(res)
            self.tv_more_url = self.change_urlink(self.tv_more_url2)
            self.tv_more_title = ["第{}集".format(x) for x in range(1, len(self.tv_more_url) + 1)]
        for i, j in zip(self.tv_more_title, self.tv_more_url):
            tv_dic_new[i] = j
        print(len(self.tv_more_title), self.tv_more_title)
        print(len(self.tv_more_url), self.tv_more_url)
        print(tv_dic_new)
        return tv_dic_new

    def url_change(self,url,flag):
        pa_url='http://www.iqiyi.com/a_[.+].html'
        if flag=="0":#通道1
            if re.match(pa_url, url):
                _url = url.replace('a', 'v')
            else:
                _url=url
            # new_url='http://www.wq114.org/weixin.php?url={}'.format(_url[21:])
            new_url='http://www.wq114.org/weixin.php?url={}'.format(_url)
            return new_url
        elif flag == "1":
            if re.match(pa_url, url):
                _url = url.replace('a', 'v')
            else:
                _url = url
            new_url='http://www.wmxz.wang/video.php?url={}'.format(_url)
            return new_url


    def play_movie(self,url,flag):
        play_url=self.url_change(url,flag)
        webbrowser.open(play_url)


if __name__ == '__main__':
    p=Pro()
from PIL import Image,ImageTk
import io
import re
import requests
# from urllib.request import urlopen
def videos():
    class Movie_app:
        def __init__(self):
            self.win=Tk()
            self.win.geometry('600x420')
            self.win.title("爱奇艺-优酷-PPTV视频播放下载器V3.1")
            self.creat_res()
            self.creat_radiores()
            self.config()
            self.page=1
            self.p=Pro()
            self.win.mainloop()
    
    
        def creat_res(self):
            self.temp=StringVar()#url地址
            self.temp2=StringVar()
            self.t1=StringVar()#通道
            self.t3=StringVar()#爱奇艺，优酷，PPTV
            self.La_title=Label(self.win,text="地址:")
            self.La_way=Label(self.win,text="选择视频通道:")
            self.R_way1=Radiobutton(self.win,text="通道A",variable=self.t1,value=True)
            self.R_way2=Radiobutton(self.win,text="通道B",variable=self.t1,value=False)
            self.R_aiqiyi=Radiobutton(self.win,text="爱奇艺",variable=self.t3,value="a")
            self.R_youku=Radiobutton(self.win,text="优酷",variable=self.t3,value="y")
            self.R_pptv=Radiobutton(self.win,text="PPTV",variable=self.t3,value="p")
            self.B_play=Button(self.win,text="播放▶")
            self.B_uppage=Button(self.win,text="上页")
            self.B_nextpage=Button(self.win,text="下页")
            self.B_search=Button(self.win,text="♣搜索全站♠")
            self.La_mesasge=Label(self.win,text="☜  ⇠☸⇢  ☞",bg="pink")
            self.La_page=Label(self.win,bg="#BFEFFF")
            self.S_croll=Scrollbar(self.win)
            self.L_box=Listbox(self.win,bg="#BFEFFF",selectmode=SINGLE)
            self.E_address=Entry(self.win,textvariable=self.temp)
            self.La_title.place(x=10,y=50,width=50,height=30)
            self.E_address.place(x=70,y=50,width=200,height=30)
            self.B_play.place(x=300,y=50,width=50,height=30)
            self.R_way1.place(x=160,y=10,width=70,height=30)
            self.R_way2.place(x=240,y=10,width=70,height=30)
            self.La_way.place(x=10,y=10,width=100,height=30)
            self.R_aiqiyi.place(x=20,y=100,width=70,height=30)
            self.R_youku.place(x=90,y=100,width=70,height=30)
            self.R_pptv.place(x=160,y=100,width=70,height=30)
            self.B_search.place(x=252,y=140,width=100,height=30)
            self.La_mesasge.place(x=80,y=125,width=90,height=20)
            self.L_box.place(x=10,y=180,width=252,height=230)
            self.S_croll.place(x=260,y=180,width=20,height=230)
            self.B_uppage.place(x=10,y=140,width=50,height=30)
            self.B_nextpage.place(x=180,y=140,width=50,height=30)
            self.La_page.place(x=80,y=150,width=90,height=28)
    
        def creat_radiores(self):
            self.movie=StringVar()#电影
            self.S_croll2=Scrollbar()#分集
            self.La_pic=Label(self.win,bg="#E6E6FA")
            self.La_movie_message=Listbox(self.win,bg="#7EC0EE")
            self.R_movie=Radiobutton(self.win,text="电影",variable=self.movie,value="m")
            self.tv=Radiobutton(self.win,text="电视剧",variable=self.movie,value="t")
            self.zhongyi=Radiobutton(self.win,text="综艺",variable=self.movie,value="z")
            self.dongman=Radiobutton(self.win,text="动漫",variable=self.movie,value="d")
            self.jilupian=Radiobutton(self.win,text="纪录片",variable=self.movie,value="j")
            self.B_view=Button(self.win,text="✤查看✤")
            self.B_info=Button(self.win,text="使用说明")
            self.B_clearbox=Button(self.win,text="清空列表")
            self.B_add=Button(self.win,text="添加到播放列表")
            self.R_movie.place(x=290,y=180,width=80,height=30)
            self.B_view.place(x=290,y=330,width=70,height=30)
            self.B_add.place(x=370,y=255,width=100,height=30)
            self.B_clearbox.place(x=500,y=255,width=70,height=30)
            self.tv.place(x=290,y=210,width=80,height=30)
            self.zhongyi.place(x=290,y=240,width=80,height=30)
            self.dongman.place(x=290,y=270,width=80,height=30)
            self.jilupian.place(x=290,y=300,width=80,height=30)
            self.La_movie_message.place(x=370,y=290,width=200,height=120)
            self.La_pic.place(x=370,y=10,width=200,height=240)
            self.B_info.place(x=290,y=370,width=70,height=30)
            self.S_croll2.place(x=568,y=290,width=20,height=120)
    
        def show_info(self):
            msg="""
            1.输入视频播放地址，即可播放
              选择A或者B可切换视频源
            2.选择视频网，选择电视剧或者电影，
              搜索全网后选择想要看得影片，点
              查看，在右方list里选择分集视频
              添加到播放列表里点选播放
            """
            messagebox.showinfo(title="使用说明",message=msg)
    
        def config(self):
            self.t1.set(True)
            self.B_play.config(command=self.play_url_movie)
            self.B_search.config(command=self.search_full_movie)
            self.B_info.config(command=self.show_info)
            self.S_croll.config(command=self.L_box.yview)
            self.L_box['yscrollcommand']=self.S_croll.set
            self.S_croll2.config(command=self.La_movie_message.yview)
            self.La_movie_message['yscrollcommand']=self.S_croll2.set
            self.B_view.config(command=self.view_movies)
            self.B_add.config(command=self.add_play_list)
            self.B_clearbox.config(command=self.clear_lisbox2)
            self.B_uppage.config(command=self.uppage_)
            self.B_nextpage.config(command=self.nextpage_)
    
        def uppage_(self):
            print('---------上一页---------')
            self.page-=1
            print(self.page)
            if self.page<1:
                self.page=1
    
        def nextpage_(self):
            print('----------下一页--------')
            self.page+=1
            print(self.page)
            if self.t3=="a" or self.t3=="y":
                if self.page>30:
                    self.page=30
            elif self.t3=="p":
                if self.movie=="m":
                    if self.page>165:
                        self.page=165
                elif self.movie == "t":
                    if self.page > 85:
                        self.page = 85
                elif self.movie == "z":
                    if self.page > 38:
                        self.page = 38
                elif self.movie == "d":
                    if self.page > 146:
                        self.page = 146
                elif self.movie == "j":
                    if self.page > 40:
                        self.page = 40
    
        def clear_lisbox(self):
            self.L_box.delete(0,END)
    
        def clear_lisbox2(self):
            self.La_movie_message.delete(0,END)
    
        def search_full_movie(self):
            print("-----search----")
            self.La_page.config(text="当前页:{}".format(self.page))
            self.clear_lisbox()
            try:
                movie_url, movie_title, movie_src_pic=self.p.get_movie_res(self.t3.get(),self.movie.get(),self.page)
                self.movie_dic={}
                for i,j,k in zip(movie_title,movie_url,movie_src_pic):
                    self.movie_dic[i]=[j,k]
                for title in movie_title:
                    self.L_box.insert(END,title)
                print(self.movie_dic)
                return self.movie_dic
            except:
                messagebox.showerror(title='警告',message='请选择电影或者电视剧')
    
        def add_play_list(self):
            print('---------playlist----------')
            print(self.movie_dic)
            if self.La_movie_message.get(self.La_movie_message.curselection())=="":
                messagebox.showwarning(title="警告",message='请在列表选择影片')
            else:
                print("电影名字:",self.La_movie_message.get(self.La_movie_message.curselection()))
                if self.movie.get()!="m":
                    self.temp.set(self.new_more_dic[self.La_movie_message.get(self.La_movie_message.curselection())])
                else:
                    self.temp.set(self.movie_dic[self.La_movie_message.get(self.La_movie_message.curselection())][0])
    
    
        def view_pic(self,pic_url):
            print('--------viewpic---------')
            pa_url_check=r'//.+[.]jpg'
            if re.match(pa_url_check,pic_url):
                print("ok")
                pic_url="http:"+pic_url
            print(pic_url)
            data=requests.get(pic_url).content
            # data=urlopen(pic_url).read()
            io_data=io.BytesIO(data)
            self.img=Image.open(io_data)
            self.u=ImageTk.PhotoImage(self.img)
            self.La_pic.config(image=self.u)
    
        def view_movies(self):
            print("--------viewmovie----------")
            cur_index=self.L_box.curselection()
            print(self.L_box.get(cur_index))
            if self.movie.get()!="m":#非电影类
                self.new_more_dic=self.p.get_more_tv_urls(self.movie_dic[self.L_box.get(cur_index)][0],self.t3.get(),self.movie.get())
                print(self.new_more_dic)
                for i,fenji_url in self.new_more_dic.items():
                    self.La_movie_message.insert(END, i)
            else:#电影类
                self.La_movie_message.insert(END,self.L_box.get(cur_index))
            self.view_pic(self.movie_dic[self.L_box.get(self.L_box.curselection())][1])#加载图片
    
        def play_url_movie(self):
            print("--------ok-----------")
            # print(type(self.t1.get()),self.t1.get())
            if self.temp.get()=="":
                messagebox.showwarning(title="警告",message="请先输入视频地址")
            else:
                if self.t1.get()!="":
                    self.p.play_movie(self.temp.get(),self.t1.get())
                else:
                    messagebox.showwarning(title='警告',message='请选择通道')
    
    
    m=Movie_app()

#记事本
def notebook():
    #新建根窗口
    root=Tk()
    #新建Menu实例
    menu_bar=Menu(root)
    file_menu=Menu(menu_bar,tearoff=0)
    edit_menu=Menu(menu_bar,tearoff=0)
    view_menu=Menu(menu_bar,tearoff=0)
    about_menu=Menu(menu_bar,tearoff=0)
    themes_menu=Menu(menu_bar,tearoff=0)
     
    file_name = None
    #获取文本行数
    def get_line_numbers():
        output = ''
        if show_line_number.get():
            row, col = content_text.index("end").split('.')
            for i in range(1, int(row)):
                output +=str(i)+ '\n'
        return output
    #更新文本行数
    def update_line_numbers(event = None):
        line_numbers = get_line_numbers()
        line_number_bar.config(state='normal')
        line_number_bar.delete('1.0', 'end')
        line_number_bar.insert('1.0', line_numbers)
        line_number_bar.config(state='disabled')
    #高亮当前行    
    def highlight_line(interval=100):
        content_text.tag_remove("active_line", 1.0, "end")
        content_text.tag_add("active_line", "insert linestart", "insert lineend+1c")
        content_text.after(interval, toggle_highlight)
    #非高亮当前行    
    def undo_highlight():
        content_text.tag_remove("active_line", 1.0, "end")
    #高亮状态切换
    def toggle_highlight(event=None):
        if to_highlight_line.get():
            highlight_line()
        else:
            undo_highlight()
    #显示光标信息
    def show_cursor_info_bar():
        show_cursor_info_checked = show_cursor_info.get()
        if show_cursor_info_checked:
            cursor_info_bar.pack(expand='no', fill=None, side='right', anchor='se')
        else:
            cursor_info_bar.pack_forget()
    #更新光标信息
    def update_cursor_info_bar(event=None):
        row, col = content_text.index(INSERT).split('.')
        line_num, col_num = str(int(row)), str(int(col)+1) 
        infotext = "Line: {0} | Column: {1}".format(line_num, col_num)
        cursor_info_bar.config(text=infotext)
    #当文本内容改变时触发
    def on_content_changed(event=None):
        update_line_numbers()
        update_cursor_info_bar()
    #打开文件
    def open_file(event=None):
        input_file_name=tkinter.filedialog.askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents","*.txt")])
        if input_file_name:
            global file_name
            file_name = input_file_name
            root.title('{} - {}'.format(os.path.basename(file_name), PROGRAM_NAME))
            content_text.delete(1.0, END)
            with open(file_name,encoding = "utf-8") as _file:
                content_text.insert(1.0, _file.read())
            on_content_changed()
    #保存文件
    def save(event=None):
        global file_name
        if not file_name:
            save_as()
        else:
            write_to_file(file_name)
        return "break"
    #保存文件为
    def save_as(event=None):
        input_file_name = tkinter.filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if input_file_name:
            global file_name
            file_name = input_file_name
            write_to_file(file_name)
            root.title('{} - {}'.format(os.path.basename(file_name),PROGRAM_NAME))
        return "break"
    #写入磁盘
    def write_to_file(file_name):
        try:
            content = content_text.get(1.0, 'end')
            with open(file_name, 'w') as the_file:
                the_file.write(content)
        except IOError:
            pass
    #新建文件
    def new_file(event=None):
        root.title("Untitled")
        global file_name
        file_name = None
        content_text.delete(1.0,END)
        on_content_changed()
    #退出编辑器
    def exit_editor(event=None):
        if tkinter.messagebox.askokcancel("Quit?", "Really quit?"):
            root.destroy()
    #剪切
    def cut():
        content_text.event_generate("<<Cut>>")
        on_content_changed()
    #复制
    def copy():
        content_text.event_generate("<<Copy>>")
    #粘贴
    def paste():
        content_text.event_generate("<<Paste>>")
        on_content_changed()
    #恢复
    def redo(event=None):
        content_text.event_generate("<<Redo>>")
        on_content_changed()
        return 'break'
    #撤销
    def undo(event=None):
        content_text.event_generate("<<Undo>>")
        on_content_changed()
        return 'break'
    #全选
    def select_all(event=None):
        content_text.tag_add('sel', '1.0', 'end')
        return "break"
    #查找
    def find_text(event=None):
        search_toplevel=Toplevel(root)
        search_toplevel.title('Find Text')
        search_toplevel.transient(root)
        search_toplevel.resizable(False, False)
        Label(search_toplevel, text="Find All:").grid(row=0, column=0, sticky='e')
        search_entry_widget = Entry(search_toplevel, width=50)
        search_entry_widget.grid(row=0, column=1, padx=2, pady=2, sticky='we')
        search_entry_widget.focus_set()
        ignore_case_value = IntVar()
        Checkbutton(search_toplevel, text='Ignore  Case',variable=ignore_case_value).grid(row=1, column=1, sticky='e', padx=2, pady=2)
        Button(search_toplevel, text="Find All", underline=0,command=lambda: search_output( search_entry_widget.get(), ignore_case_value.get(), content_text, search_toplevel,search_entry_widget)).grid(row=0, column=2, sticky='e' +'w', padx=2, pady=2)
    #关闭查找窗口
    def close_search_window():
        content_text.tag_remove('match', '1.0', END)
        search_toplevel.destroy()
        search_toplevel.protocol('WM_DELETE_WINDOW', close_search_window)
        return "break"
    #查找结果输出
    def search_output(needle, if_ignore_case, content_text,search_toplevel, search_box):
        content_text.tag_remove('match', '1.0', END)
        matches_found = 0
        if needle:
             start_pos = '1.0'
             while True:
                 start_pos = content_text.search(needle, start_pos, nocase=if_ignore_case, stopindex=END)
                 if not start_pos:
                     break
                 end_pos = '{}+{}c'.format(start_pos, len(needle))
                 content_text.tag_add('match', start_pos, end_pos)
                 matches_found += 1
                 start_pos = end_pos
             content_text.tag_config( 'match', foreground='red', background='yellow')
        search_box.focus_set()
        search_toplevel.title('{} matches found'.format(matches_found)) 
    #显示about
    def display_about_messagebox(event=None):
        tkinter.messagebox.showinfo("About", "{}{}".format(PROGRAM_NAME, "\nTkinter GUI Application\n Development Blueprints"))
    #显示help
    def display_help_messagebox(event=None):
        tkinter.messagebox.showinfo("Help", "Help Book: \nTkinter GUI Application\n Development Blueprints", icon='question')
    #变量初始化
    show_cursor_info=BooleanVar()
    to_highlight_line = BooleanVar() 
    theme_choice=StringVar()
    show_line_number = IntVar()
    show_line_number.set(1)
    #主题
    color_schemes = { 'Default': '#000000.#FFFFFF',
                      'Greygarious':'#83406A.#D1D4D1',
                      'Aquamarine': '#5B8340.#D1E7E0',
                      'Bold Beige': '#4B4620.#FFF0E1',
                      'Cobalt Blue':'#ffffBB.#3333aa',
                      'Olive Green': '#D1E7E0.#5B8340',
                      'Night Mode': '#FFFFFF.#000000'} 
    #更换主题
    def change_theme(event=None):
        selected_theme = theme_choice.get()
        fg_bg_colors = color_schemes.get(selected_theme)
        foreground_color, background_color = fg_bg_colors.split('.')
        content_text.config(background=background_color,fg=foreground_color) 
    #File
    file_menu.add_command(label="New", accelerator='Ctrl+N',    compound='left', underline=0,command=new_file)
    file_menu.add_command(label="Open", accelerator='Ctrl+O',    compound='left', underline=0,command=open_file)
    file_menu.add_command(label="Save", accelerator='Ctrl+S',    compound='left', underline=0 ,command= save)
    file_menu.add_command(label="Save as", accelerator='Shift+Ctrl+S',    compound='left', underline=0, command= save_as)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", accelerator='Alt+F4',    compound='left', underline=0, command= exit_editor)
    #Edit
    edit_menu.add_command(label="Undo", accelerator='Ctrl + Z',    compound='left',command=undo)
    edit_menu.add_command(label="Redo", accelerator='Ctrl + Y',    compound='left',command=redo)
    edit_menu.add_separator()
    edit_menu.add_command(label="Cut", accelerator='Ctrl + X',    compound='left',command=cut)
    edit_menu.add_command(label="Copy", accelerator='Ctrl + C',    compound='left',command=copy)
    edit_menu.add_command(label="Paste", accelerator='Ctrl + V',    compound='left',command=paste)
    edit_menu.add_separator()
    edit_menu.add_command(label="Find",underline=0, accelerator='Ctrl + F',    compound='left',command=find_text)
    edit_menu.add_separator()
    edit_menu.add_command(label="Select All",underline=7, accelerator='Ctrl + A',    compound='left',command=select_all)
    #View
    view_menu.add_checkbutton(label="Show Line Number",    variable=show_line_number)
    view_menu.add_checkbutton(label="Show Cursor Location at Bottom",variable=show_cursor_info, command=show_cursor_info_bar)
    view_menu.add_checkbutton(label='Highlight Current Line',    onvalue=1, offvalue=0, variable=to_highlight_line,command=toggle_highlight)
    #Themes
    themes_menu.add_radiobutton(label="Default",  variable=theme_choice,command=change_theme)
    themes_menu.add_radiobutton(label="Aquamarine", variable=theme_choice,command=change_theme)
    themes_menu.add_radiobutton(label="Bold Beige", variable=theme_choice,command=change_theme)
    themes_menu.add_radiobutton(label="Cobalt Blue", variable=theme_choice,command=change_theme)
    themes_menu.add_radiobutton(label="Greygarious", variable=theme_choice,command=change_theme)
    themes_menu.add_radiobutton(label="Night Mode", variable=theme_choice,command=change_theme)
    themes_menu.add_radiobutton(label="Olive Green", variable=theme_choice,command=change_theme)
    view_menu.add_cascade(label="Themes", menu=themes_menu)
    #About
    about_menu.add_command(label="About", compound='left', command=display_about_messagebox)
    about_menu.add_command(label="Help", compound='left', command=display_help_messagebox)
    #主菜单栏
    menu_bar.add_cascade(label='File',menu=file_menu)
    menu_bar.add_cascade(label='Edit',menu=edit_menu)
    menu_bar.add_cascade(label='View',menu=view_menu)
    menu_bar.add_cascade(label='About',menu=about_menu)
    #窗口名称
    PROGRAM_NAME = " Footprint Editor "
    root.title(PROGRAM_NAME)
    #工具栏
    shortcut_bar = Frame(root,  height=25, background='light sea green')
    shortcut_bar.pack(expand='no', fill='x')
    #图标名称
    names = ["新建","打开","保存","剪切","复制","粘贴","撤销","恢复","查找"]
    icons = ['new_file', 'open_file', 'save', 'cut', 'copy', 'paste','undo', 'redo', 'find_text']
    for i in range(len(icons)):
        # tool_bar_icon = PhotoImage(file='icons/{}.gif'.format(icon))#图标文件路径
        cmd = eval(icons[i])
        tool_bar = Button(shortcut_bar,text = names[i],command=cmd)
        
        tool_bar.pack(side='left')
    #左侧行数区    
    line_number_bar = Text(root, width=4, padx=3, takefocus=0,    border=0, background='khaki', state='disabled', wrap='none')
    line_number_bar.pack(side='left', fill='y')
    #文本内容区和右侧滚动条
    content_text = Text(root, wrap='word',undo=1)
    content_text.tag_configure('active_line', background='ivory2')
    content_text.bind('<Any-KeyPress>', on_content_changed)
    content_text.pack(expand='yes', fill='both')
    scroll_bar = Scrollbar(content_text)
    content_text.configure(yscrollcommand=scroll_bar.set)
    scroll_bar.config(command=content_text.yview)
    scroll_bar.pack(side='right', fill='y')
    #右键下拉菜单
    popup_menu = Menu(content_text)
    for i in ('cut', 'copy', 'paste', 'undo', 'redo'):
        cmd = eval(i)
        popup_menu.add_command(label=i, compound='left', command=cmd)
    popup_menu.add_separator()
    popup_menu.add_command(label='Select All', underline=7,    command=select_all)
    def show_popup_menu(event):
        popup_menu.tk_popup(event.x_root, event.y_root)
    content_text.bind('<Button-3>', show_popup_menu)
    #右下侧光标信息显示
    cursor_info_bar = Label(content_text, text='Line: 1 | Column: 1')
    cursor_info_bar.pack(expand=NO, fill=None, side='right',    anchor='se')
     
    root.config(menu=menu_bar)
    root.mainloop()

#绘画板
from tkinter import *
from tkinter.colorchooser import askcolor
import time
win_width = 1200
win_height = 750
bgcolor = 'white'
def huihua():
    
    print("画笔初始颜色为黑色.")
    print("橡皮擦要先点橡皮擦再点画笔用哦!")
    time.sleep(1)
    class Application(Frame):
        """一个经典的GUI写法"""
    
        def __init__(self, master=None):
            """初始化方法"""
            super().__init__(master)  # 调用父类的初始化方法
            self.x = 0
            self.y = 0
            self.fgcolor = "black"
            self.lastdraw = 0
            self.start_flag = False
            self.master = master
            self.pack()
            self.createWidget()
    
        def createWidget(self):
            """创建画图区域"""
            self.drawpad = Canvas(self, width=win_width, height=win_height, bg=bgcolor)
            self.drawpad.pack()
            # 创建按钮
            self.btn_start = Button(self, name='start', text='开始')
            self.btn_start.pack(side='left', padx=50)
            self.btn_pen = Button(self, name='pen', text='画笔')
            self.btn_pen.pack(side='left', padx=50)
            self.btn_rect = Button(self, name='rect', text='矩形')
            self.btn_rect.pack(side='left', padx=50)
            self.btn_clear = Button(self, name='clear', text='清屏')
            self.btn_clear.pack(side='left', padx=50)
            self.btn_erasor = Button(self, name='erasor', text='橡皮擦')
            self.btn_erasor.pack(side='left', padx=50)
            self.btn_line = Button(self, name='line', text='直线')
            self.btn_line.pack(side='left', padx=50)
            self.btn_line_arrow = Button(self, name='line_arrow', text='箭头直线')
            self.btn_line_arrow.pack(side='left', padx=50)
            self.btn_color = Button(self, name='color', text='颜色')
            self.btn_color.pack(side='left', padx=50)
            # 绑定事件
            self.btn_line.bind('<Button-1>', self.eventManager)  # 点击按钮事件
            self.btn_line_arrow.bind('<Button-1>', self.eventManager)  # 点击按钮事件
            self.btn_rect.bind('<Button-1>', self.eventManager)  # 点击按钮事件
            self.btn_pen.bind('<Button-1>', self.eventManager)  # 点击按钮事件
            self.btn_erasor.bind('<Button-1>', self.eventManager)  # 点击按钮事件
            self.btn_clear.bind('<Button-1>', self.eventManager)  # 点击按钮事件
            self.btn_color.bind('<Button-1>', self.eventManager)  # 点击按钮事件
            self.master.bind('<KeyPress-r>', self.hotKey)  # 绑定快捷键
            self.master.bind('<KeyPress-g>', self.hotKey)  # 绑定快捷键
            self.master.bind('<KeyPress-b>', self.hotKey)  # 绑定快捷键
            self.master.bind('<KeyPress-y>', self.hotKey)  # 绑定快捷键
            self.drawpad.bind('<ButtonRelease-1>', self.stopDraw)  # 左键释放按钮
    
        def eventManager(self, event):
            name = event.widget.winfo_name()
            print(name)
            self.start_flag = True
            if name == 'line':
                # 左键拖动
                self.drawpad.bind('<B1-Motion>', self.myline)
            elif name == 'line_arrow':
                self.drawpad.bind('<B1-Motion>', self.myline_arrow)
            elif name == 'rect':
                self.drawpad.bind('<B1-Motion>', self.myrect)
            elif name == 'pen':
                self.drawpad.bind('<B1-Motion>', self.mypen)
            elif name == 'erasor':
                self.drawpad.bind('<B1-Motion>', self.myerasor)
            elif name == 'clear':
                self.drawpad.delete('all')
            elif name == 'color':
                c = askcolor(color=self.fgcolor, title='请选择颜色')
                print(c)  # c的值 ((128.5, 255.99609375, 0.0), '#80ff00')
                self.fgcolor = c[1]
    
        def startDraw(self, event):
            self.drawpad.delete(self.lastdraw)
            if self.start_flag:
                self.start_flag = False
                self.x = event.x
                self.y = event.y
    
        def stopDraw(self, event):
            self.start_flag = True
            self.lastdraw = 0
    
        def myline(self, event):
            self.startDraw(event)
            self.lastdraw = self.drawpad.create_line(self.x, self.y, event.x, event.y, fill=self.fgcolor)
    
        def myline_arrow(self, event):
            self.startDraw(event)
            self.lastdraw = self.drawpad.create_line(self.x, self.y, event.x, event.y, arrow=LAST, fill=self.fgcolor)
    
        def myrect(self, event):
            self.startDraw(event)
            self.lastdraw = self.drawpad.create_rectangle(self.x, self.y, event.x, event.y, outline=self.fgcolor)
    
        def mypen(self, event):
            self.startDraw(event)
            print('self.x=', self.x, ',self.y=', self.y)
            self.drawpad.create_line(self.x, self.y, event.x, event.y, fill=self.fgcolor)
            self.x = event.x
            self.y = event.y
    
        def myerasor(self, event):
            self.fgcolor = "white"
            
        def hotKey(self, event):
            c = event.char
            if c == 'r':
                self.fgcolor = 'red'
            elif c == 'g':
                self.fgcolor = 'green'
            elif c == 'b':
                self.fgcolor = 'blue'
            elif c == 'y':
                self.fgcolor = 'yellow'
    
    
    if __name__ == '__main__':
        root = Tk()
        root.title('画图窗口')
        root.geometry('1200x1000+400+400')
        app = Application(master=root)
        root.mainloop()

#计算器
import wx
def jisuan():
    class Caluculate(wx.Frame):
        def __init__(self,*args,**kwargs):
            super(Caluculate,self).__init__(*args,**kwargs)
            self.panel = wx.Panel(self)
            self.printbtn = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE | wx.HSCROLL)
            self.num1 = wx.Button(self.panel, label="1")
            self.num2 = wx.Button(self.panel, label="2")
            self.num3 = wx.Button(self.panel, label="3")
            self.num4 = wx.Button(self.panel, label="+")
            self.num5 = wx.Button(self.panel, label="4")
            self.num6 = wx.Button(self.panel, label="5")
            self.num7 = wx.Button(self.panel, label="6")
            self.num8 = wx.Button(self.panel, label="-")
            self.num9 = wx.Button(self.panel, label="7")
            self.num10 = wx.Button(self.panel, label="8")
            self.num11 = wx.Button(self.panel, label="9")
            self.num12 = wx.Button(self.panel, label="*")
            self.num13 = wx.Button(self.panel, label="0")
            self.num14 = wx.Button(self.panel, label=".")
            self.num15 = wx.Button(self.panel, label="=")
            self.num16 = wx.Button(self.panel, label="/")

            self.Boxset()
            self.Event_bind()
            self.Show()

        def Boxset(self):
            sbox1 = wx.BoxSizer()
            sbox2 = wx.BoxSizer()
            sbox3 = wx.BoxSizer()
            sbox4 = wx.BoxSizer()
            sbox5 = wx.BoxSizer()
            vbox = wx.BoxSizer(wx.VERTICAL)
            sbox1.Add(self.printbtn,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.DOWN,border=5)
            sbox2.Add(self.num1,proportion=1,flag=wx.EXPAND|wx.LEFT,border=5)
            sbox2.Add(self.num2,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.RIGHT,border=2)
            sbox2.Add(self.num3,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.RIGHT,border=2)
            sbox2.Add(self.num4,proportion=1,flag=wx.EXPAND|wx.RIGHT,border=5)
            sbox3.Add(self.num5,proportion=1,flag=wx.EXPAND|wx.LEFT,border=5)
            sbox3.Add(self.num6,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.RIGHT,border=2)
            sbox3.Add(self.num7,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.RIGHT,border=2)
            sbox3.Add(self.num8,proportion=1,flag=wx.EXPAND|wx.RIGHT,border=5)
            sbox4.Add(self.num9,proportion=1,flag=wx.EXPAND|wx.LEFT,border=5)
            sbox4.Add(self.num10,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.RIGHT,border=2)
            sbox4.Add(self.num11,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.RIGHT,border=2)
            sbox4.Add(self.num12,proportion=1,flag=wx.EXPAND|wx.RIGHT,border=5)
            sbox5.Add(self.num13,proportion=1,flag=wx.EXPAND|wx.LEFT,border=5)
            sbox5.Add(self.num14,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.RIGHT,border=2)
            sbox5.Add(self.num15,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.RIGHT,border=2)
            sbox5.Add(self.num16,proportion=1,flag=wx.EXPAND|wx.RIGHT,border=5)
            vbox.Add(sbox1,proportion=1,flag=wx.EXPAND|wx.ALL,border=2)
            vbox.Add(sbox2,proportion=1,flag=wx.EXPAND|wx.ALL,border=2)
            vbox.Add(sbox3,proportion=1,flag=wx.EXPAND|wx.ALL,border=2)
            vbox.Add(sbox4,proportion=1,flag=wx.EXPAND|wx.ALL,border=2)
            vbox.Add(sbox5,proportion=1,flag=wx.EXPAND|wx.ALL,border=2)
            self.panel.SetSizer(vbox)

        def test1appd(self,event):
            prv_result = self.printbtn.GetValue()
            self.printbtn.AppendText("1")
        def test2appd(self,event):
            self.printbtn.AppendText("2")
        def test3appd(self,event):
            self.printbtn.AppendText("3")
        def test4appd(self,event):
            self.printbtn.AppendText("+")
        def test5appd(self,event):
            self.printbtn.AppendText("4")
        def test6appd(self,event):
            self.printbtn.AppendText("5")
        def test7appd(self,event):
            self.printbtn.AppendText("6")
        def test8appd(self,event):
            self.printbtn.AppendText("-")

        def test9appd(self,event):
            self.printbtn.AppendText("7")
        def test10appd(self,event):
            self.printbtn.AppendText("8")
        def test11appd(self,event):
            self.printbtn.AppendText("9")
        def test12appd(self,event):
            self.printbtn.AppendText("*")
        def test13appd(self,event):
            self.printbtn.AppendText("0")
        def test14appd(self,event):
            self.printbtn.AppendText(".")
        def test15appd(self,event):
            pre_result = str(self.printbtn.GetValue())
            result = eval(pre_result)
            self.printbtn.SetValue(str(result))
        def test16appd(self,event):
            self.printbtn.AppendText("/")
        def Event_bind(self):
            self.num1.Bind(wx.EVT_BUTTON,self.test1appd)
            self.num2.Bind(wx.EVT_BUTTON,self.test2appd)
            self.num3.Bind(wx.EVT_BUTTON,self.test3appd)
            self.num4.Bind(wx.EVT_BUTTON,self.test4appd)
            self.num5.Bind(wx.EVT_BUTTON,self.test5appd)
            self.num6.Bind(wx.EVT_BUTTON,self.test6appd)
            self.num7.Bind(wx.EVT_BUTTON,self.test7appd)
            self.num8.Bind(wx.EVT_BUTTON,self.test8appd)
            self.num9.Bind(wx.EVT_BUTTON,self.test9appd)
            self.num10.Bind(wx.EVT_BUTTON, self.test10appd)
            self.num11.Bind(wx.EVT_BUTTON, self.test11appd)
            self.num12.Bind(wx.EVT_BUTTON, self.test12appd)
            self.num13.Bind(wx.EVT_BUTTON, self.test13appd)
            self.num14.Bind(wx.EVT_BUTTON, self.test14appd)
            self.num15.Bind(wx.EVT_BUTTON, self.test15appd)
            self.num16.Bind(wx.EVT_BUTTON, self.test16appd)
    app = wx.App()
    Caluculate(None,title="计算器")
    app.MainLoop()

#数学计算工具
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import *
suyinshu,sb,list3,List1,r_list,bilishu = [],{},[],[],[],[]
global zuida,x_x,x_x2,x_x3,chooseuser
global jieguo1
jieguo1 = 0
zuida = 0
from os import *
from time import *
from math import *
from easygui import *
import webbrowser
def shuxue():
    def jitutonglong(toushu,tuishu):
        tuishu = tuishu - toushu * 2
        a = int(tuishu / 2)
        if a % 1 == 0 and (toushu - a) % 1 == 0:
            return "兔" + str(a) + "只鸡" + str(toushu - a) + "只"
        else:
            return "无解"
    def youxi(mode,a,b):
        if mode == "1":
            return a ** b
        elif mode == "2":
            a = a ** (1 / b)
            return a
        elif mode == "3":
            return log(b,a)
    def hunxunhuan(a,xunhuanjie):
        if a[0] == "0":
            nima = ""
            for i in range(len(xunhuanjie)):
                nima = nima + "9"
            for i in range(len(a) - 2 - len(xunhuanjie)):
                nima = nima + "0"
            a = int(a.replace("0.",""))
            nima2 = int(str(a).replace(xunhuanjie,""))
            b = a - nima2
            a = int(nima)
            zuida = 0
            suyinshu.clear()
            if a % b == 0:
                zuida = b
            elif b % a == 0:
                zuida = a
            else:
                d = a
                e = b
                list3.clear()
                if d > e:
                    if e % 2 == 0:
                        o = e / 2
                    else:
                        o = (e - 1) / 2 
                else:
                    if d % 2 == 0:
                        o = d / 2
                    else:
                        o = (d - 1) / 2
                for i in range(1,int(o + 1)):
                    if d % i == 0 and e % i == 0:
                        if zhihe(i) == "N":
                            suyinshu.append(i)
                            if i != 1:
                                list3.append(i)
                            d = d / i
                            e = e / i
                while True:
                    if len(list3) == 0:
                        break
                    list3.clear()
                    if d > e:
                        if e % 2 == 0:
                            o = e / 2
                        else:
                            o = (e - 1) / 2 
                    else:
                        if d % 2 == 0:
                            o = d / 2
                        else:
                            o = (d - 1) / 2
                    for i in range(2,int(o + 1)):
                        if d % i == 0 and e % i == 0:
                            if zhihe(i) == "N":
                                suyinshu.append(i)
                                list3.append(i)
                                d = d / i
                                e = e / i
                d = 1
                for i in range(len(suyinshu)):
                    if i != len(suyinshu) - 1:
                        d = d * suyinshu[i]
                    else:
                        zuida = suyinshu[i] * d
                if zuida == 0:
                    zuida = 1
            return str(a // zuida) + "分之" + str(b // zuida)
        else:
            nima2 = ""
            i = 1
            while a.index(".") - i != -1:
                nima2 = a[a.index(".") - i] + nima2
                i += 1
            nima = ""
            for i in range(len(xunhuanjie)):
                nima = nima + "9"
            for i in range(len(a) - len(nima2) - 1 - len(xunhuanjie)):
                nima = nima + "0"
            a = int(a.replace(nima2 + ".",""))
            nima2 = int(str(a).replace(xunhuanjie,""))
            b = a - nima2
            a = int(nima)
            zuida = 0
            suyinshu.clear()
            if a % b == 0:
                zuida = b
            elif b % a == 0:
                zuida = a
            else:
                d = a
                e = b
                list3.clear()
                if d > e:
                    if e % 2 == 0:
                        o = e / 2
                    else:
                        o = (e - 1) / 2 
                else:
                    if d % 2 == 0:
                        o = d / 2
                    else:
                        o = (d - 1) / 2
                for i in range(1,int(o + 1)):
                    if d % i == 0 and e % i == 0:
                        if zhihe(i) == "N":
                            suyinshu.append(i)
                            if i != 1:
                                list3.append(i)
                            d = d / i
                            e = e / i
                while True:
                    if len(list3) == 0:
                        break
                    list3.clear()
                    if d > e:
                        if e % 2 == 0:
                            o = e / 2
                        else:
                            o = (e - 1) / 2 
                    else:
                        if d % 2 == 0:
                            o = d / 2
                        else:
                            o = (d - 1) / 2
                    for i in range(2,int(o + 1)):
                        if d % i == 0 and e % i == 0:
                            if zhihe(i) == "N":
                                suyinshu.append(i)
                                list3.append(i)
                                d = d / i
                                e = e / i
                d = 1
                for i in range(len(suyinshu)):
                    if i != len(suyinshu) - 1:
                        d = d * suyinshu[i]
                    else:
                        zuida = suyinshu[i] * d
                if zuida == 0:
                    zuida = 1
            return str(nima2) + "又" + str(a // zuida) + "分之" + str(b // zuida)
    def jueduizhi(a):
        return abs(a)
    def abaabaaba(hahaha):
        List1.clear()
        if hahaha.count("/") == 2:
            if "+" in hahaha:
                nima = hahaha[hahaha.index("+") - 1]
                i = 2
                while hahaha[hahaha.index("+") - i] != "/":
                    nima = hahaha[hahaha.index("+") - i] + nima
                    i += 1
                nima = float(nima)
                nima2 = hahaha[hahaha.index("=") - 1]
                i = 2
                while hahaha[hahaha.index("=") - i] != "/":
                    nima2 = hahaha[hahaha.index("=") - i] + nima2
                    i += 1
                nima2 = float(nima2)
                zonghe = hahaha[len(hahaha) - 1]
                i = 2
                while hahaha[len(hahaha) - i] != "=":
                    zonghe = hahaha[len(hahaha) - i] + zonghe
                    i += 1
                zonghe = int(zonghe)
                for i in range(int(zonghe * nima * nima2)):
                    if i % nima == 0:
                        if i not in List1 and (zonghe - i / nima) * nima not in List1:
                            if i >= 0 and (zonghe - i / nima) * nima2 >= 0:
                                List1.append(i)
                                List1.append(int((zonghe - i / nima) * nima2))
                return List1
            nima = hahaha[hahaha.index("-") - 1]
            i = 2
            while hahaha[hahaha.index("-") - i] != "/":
                nima = hahaha[hahaha.index("-") - i] + nima
                i += 1
            nima = float(nima)
            nima2 = hahaha[hahaha.index("=") - 1]
            i = 2
            while hahaha[hahaha.index("=") - i] != "/":
                nima2 = hahaha[hahaha.index("=") - i] + nima2
                i += 1
            nima2 = float(nima2)
            zonghe = hahaha[len(hahaha) - 1]
            i = 2
            while hahaha[len(hahaha) - i] != "=":
                zonghe = hahaha[len(hahaha) - i] + zonghe
                i += 1
            zonghe = int(zonghe)
            i = 0
            while True:
                if i % nima == 0:
                    if i not in List1 and (zonghe - i / nima) * nima2 not in List1:
                        if i >= 0 and (zonghe - i / nima) * nima3 >= 0:
                            list1.append(i)
                            list1.append(int((zonghe - i / nima) * nima2))
                            break
            for i in range(1,11):
                list1.append(list1[0] + nima * i)
                list1.append(list1[1] + nima2 * i)
            return list1
        elif hahaha.count("/") == 0:
            if "+" in hahaha:
                nima = hahaha[hahaha.index("*") - 1]
                i = 2
                while hahaha.index("*") - i != -1:
                    nima = hahaha[hahaha.index("*") - i] + nima
                    i += 1
                nima = float(nima)
                hahaha = hahaha.replace(str(nima) + "*x+","")
                nima2 = hahaha[hahaha.index("*") - 1]
                i = 2
                while hahaha.index("*") - i != -1:
                    nima2 = hahaha[hahaha.index("*") - i] + nima2
                    i += 1
                nima2 = float(nima2)
                zonghe = hahaha[len(hahaha) - 1]
                i = 2
                while hahaha[len(hahaha) - i] != "=":
                    zonghe = hahaha[len(hahaha) - i] + nima
                    i += 1
                zonghe = int(zonghe)
                for i in range(int(round(zonghe / nima,0))):
                    if zonghe - i * nima % nima2 == 0:
                        list1.append(i)
                        list1.append(int((zonghe - i / nima) / nima2))
                return list1
            nima = hahaha[hahaha.index("*") - 1]
            i = 2
            while hahaha.index("*") - i != -1:
                nima = hahaha[hahaha.index("*") - i] + nima
                i += 1
            nima = float(nima)
            hahaha = hahaha.replace(str(nima) + "*x+","")
            nima2 = hahaha[hahaha.index("*") - 1]
            i = 2
            while hahaha.index("*") - i != -1:
                nima2 = hahaha[hahaha.index("*") - i] + nima2
                i += 1
            nima2 = float(nima2)
            zonghe = hahaha[len(hahaha) - 1]
            i = 2
            while hahaha[len(hahaha) - i] != "=":
                zonghe = hahaha[len(hahaha) - i] + nima
                i += 1
            zonghe = int(zonghe)
            for i in range(int(round(zonghe / nima,0))):
                if i * nima - zonghe % nima2 == 0:
                    list1.append(i)
                    list1.append(int((i / nima - zonghe) / nima2))
            return list1
        elif hahaha.count("/") == 1:
            if hahaha.index("*") > hahaha.index("/") and "+" in hahaha:
                nima = hahaha[hahaha.index("+") - 1]
                i = 2
                while hahaha[hahaha.index("+") - i] != "/":
                    nima = hahaha[hahaha.index("+") - i] + nima
                    i += 1
                nima = float(nima)
                nima2 = hahaha[hahaha.index("=") - 1]
                i = 2
                while hahaha[hahaha.index("=") - i] != "/":
                    nima2 = hahaha[hahaha.index("=") - i] + nima2
                    i += 1
                nima2 = float(nima2)
                zonghe = hahaha[len(hahaha) - 1]
                i = 2
                while hahaha[len(hahaha) - i] != "=":
                    zonghe = hahaha[len(hahaha) - i] + nima
                    i += 1
                zonghe = int(zonghe)
                for i in range(zonghe * nima * nima2):
                    if i % nima == 0:
                        list1.append(i)
                        list1.append(int((zonghe - i / nima) * nima2))
                return list1
    def yiyuanerci(a):
        x_x = a[a.index("x") - 1]
        i = 2
        while a.index("x") - i != -1:
            x_x = a[a.index("x") - i] + x_x
            i += 1
        a = a.replace(x_x + "x^2","")
        x_x2 = a[a.index("x") - 1]
        i = 2
        while a.index("x") - i != -1:
            x_x2 = a[a.index("x") - i] + x_x2
            i += 1
        a = a.replace(x_x2 + "x","")
        x_x3 = a[a.index("=") - 1]
        i = 2
        while a.index("=") - i != -1:
            x_x3 = a[a.index("=") - i] + x_x3
            i += 1
        x_x,x_x2,x_x3 = float(x_x),float(x_x2),float(x_x3)
        try:
            haha = (-x_x2 + sqrt(x_x2 ** 2 - 4 * x_x * x_x3)) / (2 * x_x)
            if haha % 1 == 0:
                haha = int(haha)
            if "." in str(haha):
                a = ""
                i = 2
                while haha.index(".") - i != -1:
                    a = str(haha)[haha.index(".") - i] + a
                    i += 1
                if len(haha) - len(a) - 1 < 5:
                    haha = str(2 * x_x) + "分之" + str(-x_x2) + "+" + str(x_x2 ** 2 - 4 * x_x * x_x3) + "的平方根"
            ahah = (-x_x2 - sqrt(x_x2 ** 2 - 4 * x_x * x_x3)) / (2 * x_x)
            if ahah % 1 == 0:
                ahah = int(ahah)
            if "." in str(ahah):
                a = ""
                i = 2
                while ahah.index(".") - i != -1:
                    a = str(ahah)[ahah.index(".") - i] + a
                    i += 1
                if len(ahah) - len(a) - 1 < 5:
                    ahah = str(2 * x_x) + "分之" + str(-x_x2) + "-" + str(x_x2 ** 2 - 4 * x_x * x_x3) + "的平方根"
            return "x=" + str(haha) + "和" + str(ahah)
        except:
            print("这个方程没有解！")
    def chunxunhuan(a):
        if a[0] == "0":
            nima = "9"
            for i in range(len(a) - 3):
                nima = nima + "9"
            b = a[2]
            for i in range(3,len(a)):
                b = b + a[i]
            b = int(b)
            a = int(nima)
            zuida = 0
            suyinshu.clear()
            if a % b == 0:
                zuida = b
            elif b % a == 0:
                zuida = a
            else:
                d = a
                e = b
                list3.clear()
                if d > e:
                    if e % 2 == 0:
                        o = e / 2
                    else:
                        o = (e - 1) / 2 
                else:
                    if d % 2 == 0:
                        o = d / 2
                    else:
                        o = (d - 1) / 2
                for i in range(1,int(o + 1)):
                    if d % i == 0 and e % i == 0:
                        if zhihe(i) == "N":
                            suyinshu.append(i)
                            if i != 1:
                                list3.append(i)
                            d = d / i
                            e = e / i
                while True:
                    if len(list3) == 0:
                        break
                    list3.clear()
                    if d > e:
                        if e % 2 == 0:
                            o = e / 2
                        else:
                            o = (e - 1) / 2 
                    else:
                        if d % 2 == 0:
                            o = d / 2
                        else:
                            o = (d - 1) / 2
                    for i in range(2,int(o + 1)):
                        if d % i == 0 and e % i == 0:
                            if zhihe(i) == "N":
                                suyinshu.append(i)
                                list3.append(i)
                                d = d / i
                                e = e / i
                d = 1
                for i in range(len(suyinshu)):
                    if i != len(suyinshu) - 1:
                        d = d * suyinshu[i]
                    else:
                        zuida = suyinshu[i] * d
                if zuida == 0:
                    zuida = 1
            return str(a // zuida) + "分之" + str(b // zuida)
        else:
            nima2 = a
            nima = "9"
            for i in range(len(a) - 2 - a.index(".")):
                nima = nima + "9"
            b = a[a.index(".") + 1]
            for i in range(a.index(".") + 2,len(a)):
                b = b + a[i]
            b = int(b)
            a = int(nima)
            zuida = 0
            suyinshu.clear()
            if a % b == 0:
                zuida = b
            elif b % a == 0:
                zuida = a
            else:
                d = a
                e = b
                list3.clear()
                if d > e:
                    if e % 2 == 0:
                        o = e / 2
                    else:
                        o = (e - 1) / 2 
                else:
                    if d % 2 == 0:
                        o = d / 2
                    else:
                        o = (d - 1) / 2
                for i in range(1,int(o + 1)):
                    if d % i == 0 and e % i == 0:
                        if zhihe(i) == "N":
                            suyinshu.append(i)
                            if i != 1:
                                list3.append(i)
                            d = d / i
                            e = e / i
                while True:
                    if len(list3) == 0:
                        break
                    list3.clear()
                    if d > e:
                        if e % 2 == 0:
                            o = e / 2
                        else:
                            o = (e - 1) / 2 
                    else:
                        if d % 2 == 0:
                            o = d / 2
                        else:
                            o = (d - 1) / 2
                    for i in range(2,int(o + 1)):
                        if d % i == 0 and e % i == 0:
                            if zhihe(i) == "N":
                                suyinshu.append(i)
                                list3.append(i)
                                d = d / i
                                e = e / i
                d = 1
                for i in range(len(suyinshu)):
                    if i != len(suyinshu) - 1:
                        d = d * suyinshu[i]
                    else:
                        zuida = suyinshu[i] * d
                if zuida == 0:
                    zuida = 1
            print(str(nima2) + "又" + str(a // zuida) + "分之" + str(b // zuida))
            
    def find_all(data,s):
        r_list = []
        for i in range(len(data)):
            if data[i] == s:
                break
            r_list.append(data[i])
        return r_list
    def bili(mode,a,bilishu):
        zuida = 0
        for i in bilishu:
            zuida += i
        zuida = a / zuida
        for i in range(len(bilishu)):
            bilishu[i] = bilishu[i] * zuida
        return bilishu
    def erjiedengcha(mode,shouxiang,dierxiang,gongcha,a):
        if mode == 1:
            if a == 1:
                return shouxiang
            nima = dierxiang - shouxiang
            nima2 = shouxiang
            for i in range(a - 2):
                nima2 += nima
                nima += gongcha
            nima = nima2 + nima
            i = 0
            while True:
                if not i < nima:
                    break
                i += 1
            if nima - i == 0:
                return int(nima)
            else:
                return nima
        else:
            if a == shouxiang:
                return 1
            nima = dierxiang - shouxiang
            nima2 = shouxiang
            i = 3
            while True:
                nima2 += nima
                nima += gongcha
                if nima2 == a:
                    return i
                if nima2 > a:
                    return "N"
                i += 1
    def denbishulie(mode,shouxiang,gongbi,a):
        if mode == 1:
            return shouxiang * gongbi ** (a - 1)
        if mode == 2:
            if a == shouxiang:
                return a
            else:
                ia = shouxiang
                ai = shouxiang * gongbi
                i = 3
                while True:
                    if i % 2 == 1:
                        ia = ai * gongbi
                    else:
                        ai = ia * gongbi
                    if ia == a or ai == a:
                        return i
                    if ia > a or ai > a:
                        return "N"
                    i += 1
    def dengchashulie(mode,shouxiang,gongcha,a):
        if mode == 1:
            nima = shouxiang + gongcha * (a - 1)
            if nima % 1 == 0:
                return int(nima)
            else:
                return nima
        if mode == 2:
            nima = (a - shouxiang) / gongcha + 1
            if nima % 1 == 0:
                return int(nima)
            else:
                return "N"
        elif mode == 3:
            nima = (shouxiang * 2 + gongcha * (a - 1)) * a / 2
            if nima % 1 == 0:
                return int(nima)
            else:
                return nima
    def feibonaqi(mode,a):
        if mode == "1":
            if a == 1:
                return 1
            ia = 1
            ai = 1
            for i in range(a - 2):
                if i % 2 == 0:
                    ia += ai
                else:
                    ai += ia
            if i % 2 == 0:
                return ia
            return ai
        else:
            if a == 1:
                return 1
            else:
                i = 3
                ia = 1
                ai = 1
                while True:
                    if i % 2 == 1:
                        ia += ai
                    else:
                        ai += ia
                    if ia == a or ai == a:
                        return i
                    if ia > a or ai > a:
                        return "N"
                    i += 1
    def fenshudaxiao(a,b,c,d):
        zuida = 0
        suyinshu.clear()
        if a % b == 0:
            zuida = b
        elif b % a == 0:
            zuida = a
        else:
            z = a
            e = b
            list3.clear()
            if z > e:
                if e % 2 == 0:
                    o = e / 2
                else:
                    o = (e - 1) / 2 
            else:
                if z % 2 == 0:
                    o = z / 2
                else:
                    o = (z - 1) / 2
            for i in range(2,int(o + 1)):
                if z % i == 0 and e % i == 0:
                    if zhihe(i) == "N":
                        suyinshu.append(i)
                        if i != 1:    
                            list3.append(i)
                        z = z / i
                        e = e / i
            while True:
                if len(list3) == 0:
                    break
                list3.clear()
                if z > e:
                    if e % 2 == 0:
                        o = e / 2
                    else:
                        o = (e - 1) / 2 
                else:
                    if z % 2 == 0:
                        o = z / 2
                    else:
                        o = (z - 1) / 2
                for i in range(2,int(o + 1)):
                    if z % i == 0 and e % i == 0:
                        if zhihe(i) == "N":
                            suyinshu.append(i)
                            list3.append(i)
                            z = z / i
                            e = e / i
            z = 1
            for i in range(len(suyinshu)):
                if i != len(suyinshu) - 1:
                    d = d * suyinshu[i]
                else:
                    zuida = suyinshu[i] * z
            if zuida == 0:
                zuida = 1
        c = c * (b / zuida)
        d = d * (a / zuida)
        if c > d:
            return 1
        elif d > c:
            return 2
        else:
            return "="
    def zhihe(a):
        if a == 1 or a == 0:
            return "既不是素数也不是合数"
        if a != 2 and a % 2 == 0:
            return 2
        for i in range(2,int(a / 2)):
            if a == 2:
                return "N"
            if a % i == 0:
                return i
        return "N"
    def fenjie(a):
        suyinshu,d,sb,list3 = [],a,{},[]
        for i in range(2,d):
            if a % i == 0 and zhihe(i) == "N":
                suyinshu.append(i)
                list3.append(i)
                d = d // i
        while len(list3) != 0:
            list3.clear()
            for j in range(2,int(d) + 1):
                if d % j == 0 and zhihe(j) == "N":
                    suyinshu.append(j)
                    list3.append(j)
                    d = d / j
        if len(suyinshu) == 0:
            print("这玩意是个质数！")
        else:
            for i in suyinshu:
                if i not in sb:
                    sb[i] = suyinshu.count(i)
            nima3 = ""
            for nima in sb:
                for i in range(sb[nima]):
                    nima3 = nima3 + str(nima) + "×"
            nima3 = nima3[:-1]
            return str(a) + "=" + nima3
    def common_factor(a,b):
        zuida = 0
        suyinshu.clear()
        if a % b == 0:
            return b
        if b % a == 0:
            return a
        d = a
        e = b
        list3.clear()
        if d > e:
            if e % 2 == 0:
                o = e / 2
            else:
                o = (e - 1) / 2 
        else:
            if d % 2 == 0:
                o = d / 2
            else:
                o = (d - 1) / 2
        for i in range(1,int(o + 1)):
            if d % i == 0 and e % i == 0:
                if zhihe(i) == "N":
                    suyinshu.append(i)
                    if i != 1:
                        list3.append(i)
                    d = d / i
                    e = e / i
        while True:
            if len(list3) == 0:
                break
            list3.clear()
            if d > e:
                if e % 2 == 0:
                    o = e / 2
                else:
                    o = (e - 1) / 2 
            else:
                if d % 2 == 0:
                    o = d / 2
                else:
                    o = (d - 1) / 2
            for i in range(2,int(o + 1)):
                if d % i == 0 and e % i == 0:
                    if zhihe(i) == "N":
                        suyinshu.append(i)
                        list3.append(i)
                        d = d / i
                        e = e / i
        d = 1
        for i in range(len(suyinshu)):
            if i != len(suyinshu) - 1:
                d = d * suyinshu[i]
            else:
                zuida = suyinshu[i] * d
        if zuida == 0:
            zuida = 1
        return zuida    
    def zuixiao(a,b):
        zuida = 0
        suyinshu.clear()
        if a % b == 0:
            zuida = b
        elif b % a == 0:
            zuida = a
        else:
            d = a
            e = b
            list3.clear()
            if d > e:
                if e % 2 == 0:
                    o = e / 2
                else:
                    o = (e - 1) / 2 
            else:
                if d % 2 == 0:
                    o = d / 2
                else:
                    o = (d - 1) / 2
            for i in range(1,int(o + 1)):
                if d % i == 0 and e % i == 0:
                    if zhihe(i) == "N":
                        suyinshu.append(i)
                        if i != 1:
                            list3.append(i)
                        d = d / i
                        e = e / i
            while True:
                if len(list3) == 0:
                    break
                list3.clear()
                if d > e:
                    if e % 2 == 0:
                        o = e / 2
                    else:
                        o = (e - 1) / 2 
                else:
                    if d % 2 == 0:
                        o = d / 2
                    else:
                        o = (d - 1) / 2
                for i in range(2,int(o + 1)):
                    if d % i == 0 and e % i == 0:
                        if zhihe(i) == "N":
                            suyinshu.append(i)
                            list3.append(i)
                            d = d / i
                            e = e / i
            d = 1
            for i in range(len(suyinshu)):
                if i != len(suyinshu) - 1:
                    d = d * suyinshu[i]
                else:
                    zuida = suyinshu[i] * d
            if zuida == 0:
                zuida = 1
        return zuida * (a / zuida) * (b / zuida)
    def fenshuyunsuan(mode,a,b,c,d):
        if mode == "1":
            zuida = 0
            suyinshu.clear()
            if a % b == 0:
                zuida = b
            elif b % a == 0:
                zuida = a
            else:
                z = a
                e = b
                list3.clear()
                if z > e:
                    if e % 2 == 0:
                        o = e / 2
                    else:
                        o = (e - 1) / 2 
                else:
                    if z % 2 == 0:
                        o = z / 2
                    else:
                        o = (z - 1) / 2
                for i in range(2,int(o + 1)):
                    if z % i == 0 and e % i == 0:
                        if zhihe(i) == "N":
                            suyinshu.append(i)
                            if i != 1:    
                                list3.append(i)
                            z = z / i
                            e = e / i
                while True:
                    if len(list3) == 0:
                        break
                    list3.clear()
                    if z > e:
                        if e % 2 == 0:
                            o = e / 2
                        else:
                            o = (e - 1) / 2 
                    else:
                        if z % 2 == 0:
                            o = z / 2
                        else:
                            o = (z - 1) / 2
                    for i in range(2,int(o + 1)):
                        if z % i == 0 and e % i == 0:
                            if zhihe(i) == "N":
                                suyinshu.append(i)
                                list3.append(i)
                                z = z / i
                                e = e / i
            z = 1
            for i in range(len(suyinshu)):
                if i != len(suyinshu) - 1:
                    d = d * suyinshu[i]
                else:
                    zuida = suyinshu[i] * z
            if zuida == 0:
                zuida = 1
            e = zuida * (a / zuida) * (b / zuida)
            f = c * (b / zuida) + d * (a / zuida)
            zuida = 0
            suyinshu.clear()
            if e % f == 0:
                zuida = f
            elif f % e == 0:
                zuida = e
            else:
                h = e
                i = f
                list3.clear()
                if i > h:
                    if h % 2 == 0:
                        o = h / 2
                    else:
                        o = (h - 1) / 2 
                else:
                    if i % 2 == 0:
                        o = i / 2
                    else:
                        o = (i - 1) / 2
                for j in range(1,int(o + 1)):
                    if h % j == 0 and i % j == 0:
                        if zhihe(j) == "N":
                            suyinshu.append(j)
                            if j != 1:
                                list3.append(j)
                            h = h / j
                            i = i / j
                while True:
                    if len(list3) == 0:
                        break
                    list3.clear()
                    if h > i:
                        if e % 2 == 0:
                            o = i / 2
                        else:
                            o = (i - 1) / 2 
                    else:
                        if d % 2 == 0:
                            o = h / 2
                        else:
                            o = (h - 1) / 2
                    for j in range(2,int(o + 1)):
                        if h % j == 0 and i % j == 0:
                            if zhihe(j) == "N":
                                suyinshu.append(j)
                                list3.append(j)
                                h = h / j
                                i = i / j
                i = 1
                for j in range(len(suyinshu)):
                    if j != len(suyinshu) - 1:
                        i = i * suyinshu[j]
                    else:
                        zuida = suyinshu[j] * i
                if zuida == 0:
                    zuida = 1
            return str(int(e / zuida)) + "分之" + str(int(f / zuida))
        elif mode == "2":
            nima = fenshudaxiao(a,b,c,d)
            if nima == "=":
                return 0
            else:
                zuida = 0
                suyinshu.clear()
                if a % b == 0:
                    zuida = b
                elif b % a == 0:
                    zuida = a
                else:
                    z = a
                    e = b
                    list3.clear()
                    if z > e:
                        if e % 2 == 0:
                            o = e / 2
                        else:
                            o = (e - 1) / 2 
                    else:
                        if z % 2 == 0:
                            o = z / 2
                        else:
                            o = (z - 1) / 2
                    for i in range(1,int(o + 1)):
                        if z % i == 0 and e % i == 0:
                            if zhihe(i) == "N":
                                suyinshu.append(i)
                                if i != 1:
                                    list3.append(i)
                                z = z / i
                                e = e / i
                    while True:
                        if len(list3) == 0:
                            break
                        list3.clear()
                        if z > e:
                            if e % 2 == 0:
                                o = e / 2
                            else:
                                o = (e - 1) / 2 
                        else:
                            if z % 2 == 0:
                                o = z / 2
                            else:
                                o = (z - 1) / 2
                        for i in range(2,int(o + 1)):
                            if z % i == 0 and e % i == 0:
                                if zhihe(i) == "N":
                                    suyinshu.append(i)
                                    list3.append(i)
                                    z = z / i
                                    e = e / i
                z = 1
                for i in range(len(suyinshu)):
                    if i != len(suyinshu) - 1:
                        d = d * suyinshu[i]
                    else:
                        zuida = suyinshu[i] * z
                if zuida == 0:
                    zuida = 1
                
                e = zuida * (a / zuida) * (b / zuida)
                f = c * (b / zuida) - d * (a / zuida)
                zuida = 0
                suyinshu.clear()
                if e % f == 0:
                    zuida = f
                elif f % e == 0:
                    zuida = e
                else:
                    h = e
                    i = f
                    list3.clear()
                    if i > h:
                        if h % 2 == 0:
                            o = h / 2
                        else:
                            o = (h - 1) / 2 
                    else:
                        if i % 2 == 0:
                            o = i / 2
                        else:
                            o = (i - 1) / 2
                    for j in range(1,int(o + 1)):
                        if h % j == 0 and i % j == 0:
                            if zhihe(j) == "N":
                                suyinshu.append(j)
                                if j != 1:
                                    list3.append(j)
                                h = h / j
                                i = i / j
                    while True:
                        if len(list3) == 0:
                            break
                        list3.clear()
                        if h > i:
                            if e % 2 == 0:
                                o = i / 2
                            else:
                                o = (i - 1) / 2 
                        else:
                            if d % 2 == 0:
                                o = h / 2
                            else:
                                o = (h - 1) / 2
                        for j in range(2,int(o + 1)):
                            if h % j == 0 and i % j == 0:
                                if zhihe(j) == "N":
                                    suyinshu.append(j)
                                    list3.append(j)
                                    h = h / j
                                    i = i / j
                    i = 1
                    for j in range(len(suyinshu)):
                        if j != len(suyinshu) - 1:
                            i = i * suyinshu[j]
                        else:
                            zuida = suyinshu[j] * i
                    if zuida == 0:
                        zuida = 1
                return str(int(e / zuida)) + "分之" + str(int(f / zuida))
        if mode == "3":
            e = a * b
            f = c * d
            zuida = 0
            suyinshu.clear()
            if e % f == 0:
                zuida = f
            elif f % e == 0:
                zuida = e
            else:
                h = e
                i = f
                list3.clear()
                if i > h:
                    if h % 2 == 0:
                        o = h / 2
                    else:
                        o = (h - 1) / 2 
                else:
                    if i % 2 == 0:
                        o = i / 2
                    else:
                        o = (i - 1) / 2
                for j in range(1,int(o + 1)):
                    if h % j == 0 and i % j == 0:
                        if zhihe(j) == "N":
                            suyinshu.append(j)
                            if j != 1:
                                list3.append(j)
                            h = h / j
                            i = i / j
                while True:
                    if len(list3) == 0:
                        break
                    list3.clear()
                    if h > i:
                        if e % 2 == 0:
                            o = i / 2
                        else:
                            o = (i - 1) / 2 
                    else:
                        if d % 2 == 0:
                            o = h / 2
                        else:
                            o = (h - 1) / 2
                    for j in range(2,int(o + 1)):
                        if h % j == 0 and i % j == 0:
                            if zhihe(j) == "N":
                                suyinshu.append(j)
                                list3.append(j)
                                h = h / j
                                i = i / j
                i = 1
                for j in range(len(suyinshu)):
                    if j != len(suyinshu) - 1:
                        i = i * suyinshu[j]
                    else:
                        zuida = suyinshu[j] * i
                if zuida == 0:
                    zuida = 1
            return str(int(e / zuida)) + "分之" + str(int(f / zuida))
        if mode == "4":
            e = a * d
            f = b * c
            zuida = 0
            suyinshu.clear()
            if e % f == 0:
                zuida = f
            elif f % e == 0:
                zuida = e
            else:
                h = e
                i = f
                list3.clear()
                if i > h:
                    if h % 2 == 0:
                        o = h / 2
                    else:
                        o = (h - 1) / 2 
                else:
                    if i % 2 == 0:
                        o = i / 2
                    else:
                        o = (i - 1) / 2
                for j in range(1,int(o + 1)):
                    if h % j == 0 and i % j == 0:
                        if zhihe(j) == "N":
                            suyinshu.append(j)
                            if j != 1:
                                list3.append(j)
                            h = h / j
                            i = i / j
                while True:
                    if len(list3) == 0:
                        break
                    list3.clear()
                    if h > i:
                        if e % 2 == 0:
                            o = i / 2
                        else:
                            o = (i - 1) / 2 
                    else:
                        if d % 2 == 0:
                            o = h / 2
                        else:
                            o = (h - 1) / 2
                    for j in range(2,int(o + 1)):
                        if h % j == 0 and i % j == 0:
                            if zhihe(j) == "N":
                                suyinshu.append(j)
                                list3.append(j)
                                h = h / j
                                i = i / j
                i = 1
                for j in range(len(suyinshu)):
                    if j != len(suyinshu) - 1:
                        i = i * suyinshu[j]
                    else:
                        zuida = suyinshu[j] * i
                if zuida == 0:
                    zuida = 1
            return str(int(e / zuida)) + "分子" + str(int(f / zuida))
    def fenshudagongyin(a,b,c,d):
        zuida = 0
        suyinshu.clear()
        if a % b == 0:
            zuida = b
        elif b % a == 0:
            zuida = a
        else:
            z = a
            e = b
            list3.clear()
            if z > e:
                if e % 2 == 0:
                    o = e / 2
                else:
                    o = (e - 1) / 2 
            else:
                if z % 2 == 0:
                    o = z / 2
                else:
                    o = (z - 1) / 2
            for i in range(2,int(o + 1)):
                if z % i == 0 and e % i == 0:
                    if zhihe(i) == "N":
                        suyinshu.append(i)
                        if i != 1:    
                            list3.append(i)
                        z = z / i
                        e = e / i
            while True:
                if len(list3) == 0:
                    break
                list3.clear()
                if z > e:
                    if e % 2 == 0:
                        o = e / 2
                    else:
                        o = (e - 1) / 2 
                else:
                    if z % 2 == 0:
                        o = z / 2
                    else:
                        o = (z - 1) / 2
                for i in range(2,int(o + 1)):
                    if z % i == 0 and e % i == 0:
                        if zhihe(i) == "N":
                            suyinshu.append(i)
                            list3.append(i)
                            z = z / i
                            e = e / i
        z = 1
        for i in range(len(suyinshu)):
            if i != len(suyinshu) - 1:
                d = d * suyinshu[i]
            else:
                zuida = suyinshu[i] * z
        if zuida == 0:
            zuida = 1
        a1 = a * (b / zuida)
        b1 = a1
        c = c * (b / zuida)
        d = d * (a / zuida)
        zuida = 0
        suyinshu.clear()
        if c % d == 0:
            zuida = d
        elif d % c == 0:
            zuida = c
        else:
            h = c
            i = d
            list3.clear()
            if h > i:
                if i % 2 == 0:
                    o = i / 2
                else:
                    o = (i - 1) / 2 
            else:
                if h % 2 == 0:
                    o = h / 2
                else:
                    o = (h - 1) / 2
            for j in range(1,int(o + 1)):
                if h % j == 0 and i % j == 0:
                    if zhihe(j) == "N":
                        suyinshu.append(j)
                        if j != 1:
                            list3.append(j)
                        h = h / j
                        i = i / j
            while True:
                if len(list3) == 0:
                    break
                list3.clear()
                if h > i:
                    if i % 2 == 0:
                        o = i / 2
                    else:
                        o = (i - 1) / 2 
                else:
                    if h % 2 == 0:
                        o = h / 2
                    else:
                        o = (h - 1) / 2
                for j in range(2,int(o + 1)):
                    if h % j == 0 and i % j == 0:
                        if zhihe(j) == "N":
                            suyinshu.append(j)
                            list3.append(j)
                            h = h / j
                            i = i / j
            z = 1
            for j in range(len(suyinshu)):
                if j != len(suyinshu) - 1:
                    z = z * suyinshu[j]
                else:
                    zuida = suyinshu[j] * z
            if zuida == 0:
                zuida = 1
        b = zuida
        print(b)
        zuida = 0
        suyinshu.clear()
        if a1 % b == 0:
            zuida = b
        elif b % a1 == 0:
            zuida = a1
        else:
            d = a1
            e = b
            list3.clear()
            if d > e:
                if e % 2 == 0:
                    o = e / 2
                else:
                    o = (e - 1) / 2 
            else:
                if d % 2 == 0:
                    o = d / 2
                else:
                    o = (d - 1) / 2
            for i in range(1,int(o + 1)):
                if d % i == 0 and e % i == 0:
                    if zhihe(i) == "N":
                        suyinshu.append(i)
                        if i != 1:
                            list3.append(i)
                        d = d / i
                        e = e / i
            while True:
                if len(list3) == 0:
                    break
                list3.clear()
                if d > e:
                    if e % 2 == 0:
                        o = e / 2
                    else:
                        o = (e - 1) / 2 
                else:
                    if d % 2 == 0:
                        o = d / 2
                    else:
                        o = (d - 1) / 2
                for i in range(2,int(o + 1)):
                    if d % i == 0 and e % i == 0:
                        if zhihe(i) == "N":
                            suyinshu.append(i)
                            list3.append(i)
                            d = d / i
                            e = e / i
            d = 1
            for i in range(len(suyinshu)):
                if i != len(suyinshu) - 1:
                    d = d * suyinshu[i]
                else:
                    zuida = suyinshu[i] * d
            if zuida == 0:
                zuida = 1
        return str(a1 // zuida) + "分之" + str(b // zuida)
    def pingmianjihe(mode,a,b,c):
        if mode == "等边三角形":
            return sqrt(3) / 4 * a ** 2
        if mode == "梯形":
            return (a + b) * c / 2
        if mode == "三角形":
            return a * b / 2
        if mode == "圆形面积":
            return a ** 2 * 3.14
        if mode == "圆形周长":
            return a * 2 * 3.14
        if mode == "扇形面积":
            return a ** 2 * 3.14 / 360 * b
        if mode == "扇形周长":
            return 2 * a + a * 2 * 3.14 / 360 * b
        if mode == "长方形":
            return a * b
    def izhihe1():
        izhihewin = Tk()
        izhihewin.title("质数合数判断")
        izhihewin.geometry("400x300")
        wo = Label(izhihewin,text = "请输入要计算的数",width = 15)
        wo.pack(side = TOP)
        var1 = Entry(izhihewin)
        var1.pack(side = TOP,expand = True)
        def izhihe2():
            if "妈" in var1.get():
                messagebox.showwarning("","我不是你妈，我是你爹！")
            else:
                try:
                    if "妈" in var1.get():
                        messagebox.showwarning("","我不是你妈，我是你爹！")
                    else:
                        jieguo1 = zhihe(int(var1.get()))
                        if jieguo1 == "既不是素数也不是合数":
                            jiegu1 = "既不是素数也不是合数"
                        elif jieguo1 == "N":
                            jieguo1 = "是质数"
                        else:
                            jieguo1 = "是合数，因数：" + str(jieguo1)
                    messagebox.showwarning("",jieguo1)
                except:
                    messagebox.showwarning("","请不要乱输")
        Button(izhihewin,text = "计算",command = izhihe2).pack(fill = BOTH,side = TOP,expand = True)
        izhihewin.mainloop()
    def izuixiao1():
        izuixiaowin = Tk()
        izuixiaowin.title("最小公倍数")
        izuixiaowin.geometry("400x300")
        Label(izuixiaowin,text = "在此输入第一个数").pack(side = TOP,expand = True)
        var1 = Entry(izuixiaowin)
        var1.pack(side = TOP,expand = True)
        Label(izuixiaowin,text = "在此输入第二个数").pack(side = TOP,expand = True)
        var2 = Entry(izuixiaowin)
        var2.pack(side = TOP,expand = True)
        def izuixiao2():
            try:
                jieguo1 = "最小公倍数是" + str(int(zuixiao(int(var1.get()),int(var2.get()))))
                messagebox.showwarning("",jieguo1)
            except:
                messagebox.showwarning("","请不要乱输")
        Button(izuixiaowin,text = "计算",command = izuixiao2).pack(fill = BOTH,side = BOTTOM,expand = True)
        izuixiaowin.mainloop()
    def izuida1():
        izuidawin = Tk()
        izuidawin.title("最大公因数")
        izuidawin.geometry("400x300")
        Label(izuidawin,text = "在此输入第一个数").pack(side = TOP,expand = True)
        var1 = Entry(izuidawin)
        var1.pack(side = TOP,expand = True)
        Label(izuidawin,text = "在此输入第二个数").pack(side = TOP,expand = True)
        var2 = Entry(izuidawin)
        var2.pack(side = TOP,expand = True)
        def izuida2():
            try:
                jieguo1 = "最大公因数是" + str(common_factor(int(var1.get()),int(var2.get())))
                messagebox.showwarning("",jieguo1)
            except:
                messagebox.showwarning("","请不要乱输")
        Button(izuidawin,text = "计算",command = izuida2).pack(fill = BOTH,side = BOTTOM,expand = True)
        izuidawin.mainloop()
    def fenshu1():
        chooseuser = buttonbox(msg="你要使用哪种运算？",title="",choices=("加法","减法","乘法","除法"))
        if chooseuser == "加法":
            ijiafawin = Tk()
            ijiafawin.title("分数加法")
            ijiafawin.geometry("400x300")
            Label(ijiafawin,text = "在此输入第一个分数的分子").pack(expand = True)
            var1 = Entry(ijiafawin)
            var1.pack(expand = True)
            Label(ijiafawin,text = "在此输入第一个分数的分母").pack(expand = True)
            var2 = Entry(ijiafawin)
            var2.pack(expand = True)
            Label(ijiafawin,text = "在此输入第二个分数的分子").pack(expand = True)
            var3 = Entry(ijiafawin)
            var3.pack(expand = True)
            Label(ijiafawin,text = "在此输入第二个分数的分母").pack(expand = True)
            var4 = Entry(ijiafawin)
            var4.pack(expand = True)
            def ijiafa():
                try:
                    jieguo1 = fenshuyunsuan("1",int(var2.get()),int(var4.get()),int(var1.get()),int(var3.get()))
                    jieguo1 = "运算结果是" + str(jieguo1)
                    messagebox.showwarning("",jieguo1)
                except:
                    messagebox.showwarning("","请不要乱输")
            Button(ijiafawin,text = "计算",command = ijiafa).pack(fill = BOTH,side = BOTTOM,expand = True)
            ijiafawin.mainloop()
        elif chooseuser == "减法":
            ijianfawin = Tk()
            ijianfawin.title("分数减法")
            ijianfawin.geometry("400x300")
            Label(ijianfawin,text = "在此输入被减数的分子").pack(expand = True)
            var1 = Entry(ijianfawin)
            var1.pack(expand = True)
            Label(ijianfawin,text = "在此输入被减数的分母").pack(expand = True)
            var2 = Entry(ijianfawin)
            var2.pack(expand = True)
            Label(ijianfawin,text = "在此输入减数的分子").pack(expand = True)
            var3 = Entry(ijianfawin)
            var3.pack(expand = True)
            Label(ijianfawin,text = "在此输入减数的分母").pack(expand = True)
            var4 = Entry(ijianfawin)
            var4.pack(expand = True)
            def ijianfa():
                jieguo1 = fenshuyunsuan("2",int(var2.get()),int(var4.get()),int(var1.get()),int(var3.get()))
                jieguo1 = "运算结果是" + str(jieguo1)
                messagebox.showwarning("",jieguo1)
            Button(ijianfawin,text = "计算",command = ijianfa).pack(fill = BOTH,side = BOTTOM,expand = True)
            ijianfawin.mainloop()
        elif chooseuser == "乘法":
            ichengfawin = Tk()
            ichengfawin.title("分数乘法")
            ichengfawin.geometry("400x300")
            Label(ichengfawin,text = "在此输入第一个分数的分子").pack(expand = True)
            var1 = Entry(ichengfawin)
            var1.pack(expand = True)
            Label(ichengfawin,text = "在此输入第一个分数的分母").pack(expand = True)
            var2 = Entry(ichengfawin)
            var2.pack(expand = True)
            Label(ichengfawin,text = "在此输入第二个分数的分子").pack(expand = True)
            var3 = Entry(ichengfawin)
            var3.pack(expand = True)
            Label(ichengfawin,text = "在此输入第二个分数的分母").pack(expand = True)
            var4 = Entry(ichengfawin)
            var4.pack(expand = True)
            def ichengfa():
                try:
                    jieguo1 = fenshuyunsuan("3",int(var2.get()),int(var4.get()),int(var1.get()),int(var3.get()))
                    jieguo1 = "运算结果是" + str(jieguo1)
                    messagebox.showwarning("",jieguo1)
                except:
                    messagebox.showwarning("","请不要乱输")
            Button(ichengfawin,text = "计算",command = ichengfa).pack(fill = BOTH,side = BOTTOM,expand = True)
            ichengfawin.mainloop()
        else:
            ichufawin = Tk()
            ichufawin.title("分数除法")
            ichufawin.geometry("400x300")
            Label(ichufawin,text = "在此输入被除数的分子").pack(expand = True)
            var1 = Entry(ichufawin)
            var1.pack(expand = True)
            Label(ichufawin,text = "在此输入被除数的分母").pack(expand = True)
            var2 = Entry(ichufawin)
            var2.pack(expand = True)
            Label(ichufawin,text = "在此输入除数的分子").pack(expand = True)
            var3 = Entry(ichufawin)
            var3.pack(expand = True)
            Label(ichufawin,text = "在此输入除数的分母").pack(expand = True)
            var4 = Entry(ichufawin)
            var4.pack(expand = True)
            def ichufa():
                try:
                    jieguo1 = fenshuyunsuan("4",int(var2.get()),int(var4.get()),int(var1.get()),int(var3.get()))
                    jieguo1 = "运算结果是" + jieguo1
                    messagebox.showwarning("",jieguo1)
                except:
                    messagebox.showwarning("","请不要乱输")
            Button(ichufawin,text = "计算",command = ichufa).pack(fill = BOTH,side = BOTTOM,expand = True)
            ichufawin.mainloop()
    def ifenshu():
        ifenshuwin = Tk()
        ifenshuwin.title("分数比较大小")
        ifenshuwin.geometry("400x300")
        Label(ifenshuwin,text = "请输入第一个分数的分子").pack(expand = True)
        var1 = Entry(ifenshuwin)
        var1.pack()
        Label(ifenshuwin,text = "请输入第一个分数的分母").pack(expand = True)
        var2 = Entry(ifenshuwin)
        var2.pack()
        Label(ifenshuwin,text = "请输入第二个分数的分子").pack(expand = True)
        var3 = Entry(ifenshuwin)
        var3.pack()
        Label(ifenshuwin,text = "请输入第二个分数的分母").pack(expand = True)
        var4 = Entry(ifenshuwin)
        var4.pack()
        def bijiao():
            try:
                jieguo1 = fenshudaxiao(int(var2.get()),int(var4.get()),int(var1.get()),int(var3.get()))
                if jieguo1 == 1:
                    messagebox.showwarning("",var2.get() + "分之" + var1.get() + "大")
                elif jieguo1 == 2:
                    messagebox.showwarning("",var4.get() + "分之" + var3.get() + "大")
                else:
                    messagebox.showwarning("两个数一样大")
            except:
                messagebox.showwarning("请不要乱输")
        Button(ifenshuwin,text = "计算",command = bijiao).pack(fill = BOTH,side = BOTTOM)
        ifenshuwin.mainloop()
    def ifeibonaqi():
        chooseuser = buttonbox(msg = "你要用哪个功能",title = "",choices = ["求某一项","求某个数是第几项"])
        if chooseuser == "求某一项":
            feibowin1 = Tk()
            feibowin1.geometry("400x300")
            feibowin1.title("求斐波那契数列的某一项")
            Label(feibowin1,text = "你想求第").pack(fill = BOTH,side = TOP,expand = True)
            var1 = Entry(feibowin1)
            var1.pack(fill = BOTH,side = TOP,expand = True)
            Label(feibowin1,text = "项").pack(fill = BOTH,side = TOP,expand = True)
            def ifeibo1():
                try:
                    messagebox.showwarning("","第" + var1.get() + "项是" + str(feibonaqi("1",int(var1.get()))))
                except:
                    messagebox.showwarning("","请不要乱输")
            Button(feibowin1,text = "计算",command = ifeibo1).pack(fill = BOTH,side = BOTTOM)
            feibowin1.mainloop()
        else:
            feibowin2 = Tk()
            feibowin2.geometry("400x300")
            feibowin2.title("求某个数在数列中的位置")
            Label(feibowin2,text = "你想求").pack(side = TOP)
            var1 = Entry(feibowin2)
            var1.pack(side = TOP,expand = True)
            Label(feibowin2,text = "在斐波那契数列中的位置").pack(side = TOP)
            def ifeibo2():
                try:
                    jieguo1 = feibonaqi("2",int(var1.get()))
                    if jieguo1 == "N":
                        messagebox.showwarning("","这个数不在斐波那契数列中！")
                    else:
                        messagebox.showwarning("",var1.get() + "是第" + str(jieguo1) + "项")
                except:
                    messagebox.showwarning("","请不要乱输")
            Button(feibowin2,text = "计算",command = ifeibo2).pack(fill = BOTH,side = BOTTOM)
            feibowin2.mainloop()
    def dengcha():
        chooseuser = buttonbox(msg = "你要哪个功能？",title = "",choices = ["求某一项","求某个数的位置","求和"])
        if chooseuser == "求某一项":
            dengchawin1 = Tk()
            dengchawin1.title("求等差数列的某一项")
            dengchawin1.geometry("400x300")
            Label(dengchawin1,text = "在此输入首项").pack()
            var1 = Entry(dengchawin1)
            var1.pack()
            Label(dengchawin1,text = "在此输入公差").pack()
            var2 = Entry(dengchawin1)
            var2.pack()
            Label(dengchawin1,text = "你想求第几项？").pack()
            var3 = Entry(dengchawin1)
            var3.pack()
            def idengcha1():
                try:
                    messagebox.showwarning("","第" + var3.get() + "项是" + str(dengchashulie(1,int(var1.get()),int(var2.get()),int(var3.get()))))
                except:
                    messagebox.showwarning("","请不要乱输")
            Button(dengchawin1,text = "计算",command = idengcha1).pack(fill = BOTH,side = BOTTOM)
            dengchawin1.mainloop()
        elif chooseuser == "求某个数的位置":
            dengchawin2 = Tk()
            dengchawin2.title("求某个数在等差数列的位置")
            dengchawin2.geometry("400x300")
            Label(dengchawin2,text = "请输入首项").pack()
            var1 = Entry(dengchawin2)
            var1.pack()
            Label(dengchawin2,text = "请输入公差").pack()
            var2 = Entry(dengchawin2)
            var2.pack()
            Label(dengchawin2,text = "你想求哪个数的位置？").pack()
            var3 = Entry(dengchawin2)
            var3.pack()
            def idengcha2():
                try:
                    jieguo1 = dengchashulie(2,int(var1.get()),int(var2.get()),int(var3.get()))
                    if jieguo1 == "N":
                        messagebox.showwarning("","这个数不在等差数列中！")
                    else:
                        messagebox.showwarning("",var3.get() + "是第" + str(jieguo1) + "项")
                except:
                    messagebox.showwarning("","请不要乱输")
            Button(dengchawin2,text = "计算",command = idengcha2).pack(fill = BOTH,side = BOTTOM)
            dengchawin2.mainloop()
        elif chooseuser == "求和":
            dengchawin3 = Tk()
            dengchawin3.title("等差数列求和")
            dengchawin3.geometry("400x300")
            Label(dengchawin3,text = "请输入首项").pack()
            var1 = Entry(dengchawin3)
            var1.pack()
            Label(dengchawin3,text = "请输入公差").pack()
            var2 = Entry(dengchawin3)
            var2.pack()
            Label(dengchawin3,text = "请输入项数").pack()
            var3 = Entry(dengchawin3)
            var3.pack()
            def idengcha3():
                try:
                    jieguo1 = dengchashulie(3,int(var1.get()),int(var2.get()),int(var3.get()))
                    messagebox.showwarning("","等差数列值和是" + str(jieguo1))
                except:
                    messagebox.showwarning("","请不要乱输")
            Button(dengchawin3,text = "计算",command = idengcha3).pack(fill = BOTH,side = BOTTOM)        
    afsd = {
        "质数合数判断":izhihe1,
        "最大公因数（整数）":izuida1,
        "最小公倍数（整数）":izuixiao1,
        "分数运算":fenshu1,
        "分数比较大小":ifenshu,
        "斐波那契数列计算":ifeibonaqi,
        "等差数列":dengcha
        }
    def main():
        window = Tk()
        window.title("数学作业神器")
        window.geometry("400x300")
        for k in afsd:
            Button(window,text = k,command = afsd[k]).pack(fill = BOTH,side = TOP,expand = True)
        def fanhui():
            if messagebox.askokcancel("确定退出？","您确定要退出？"):
                window.destroy()
        window.protocol("WM_DELETE_WINDOW",fanhui)
        window.mainloop()
    main()

#二维码生成器
from tkinter import *
from tkinter import messagebox as m
from tkinter import filedialog as dialog
from tkinter import ttk
from segno import *
from segno import helpers
def erma():
    tk=Tk()
    tk.geometry('+600+400')
    tk.resizable(0,0)
    tk.title('选择模式-Hello智能二维码生成器')
    tk.attributes('-topmost',1)
    v=StringVar()
    v.set('普通')
    def shotishi():
        m.showinfo(parent=tk,title='重要提示',message='*注：wifi二维码需要使用手机自带扫\n码工具扫描才可连接到wifi，\n如果扫描后没有出现连接按钮，而是只有一串字符，\n这说明您的扫码工具不支持wifi二维码。\n名片二维码扫描后如果没有正常显示姓名等\n其他信息，而是只有一串字符，\n这说明扫码工具也不支持名片二维码！')
    def about():
        m.showinfo(title='关于我们',message='Hello智能二维码生成器（作者：陈明翰）\n                         0.7.6版')
    def ok():
        if v.get()=='普通':
            def okpu():
                if micro.get()==0:
                    pu=make(thing.get(),micro=False)
                else:
                    try:
                        pu=make(thing.get(),micro=True)
                    except:
                        m.showerror(parent=putk,title='错误',message='二维码数据过多，无法生成微型码')
                        return
                try:
                    scale.get()
                except:
                    m.showerror(title='错误',message='“每个码源占多少像素”只能是整数！',parent=putk)
                    return
                if scale.get()==0:
                    m.showerror(title='错误',message='“每个码源占多少像素”不能为0！！',parent=putk)
                    return
                def l():
                    f=dialog.asksaveasfilename(title='请选择二维码图片保存地址',parent=erer,filetypes=[('PNG图片格式','.png')],defaultextension='.png')
                    if f=='':
                        return
                    fileway.set(f)
                def ok():
                    if fileway.get()=='':
                        m.showwarning(title='提示',message='您没有填写或选择保存路径',parent=erer)
                    else:
                        try:
                            pu.save(fileway.get(),scale=scale.get())
                            putk.destroy()
                        except:
                            m.showerror(title='错误',message='数据格式或文件路径有误！',parent=erer)
                erer=Toplevel(putk)
                erer.title('保存文件-Hello智能二维码生成器')
                erer.geometry('+400+400')
                erer.resizable(0,0)
                erer.attributes('-topmost',1)
                fileway=StringVar()
                Label(erer,text='请输入保存地址：').grid(column=0,row=0)
                Entry(erer,textvariable=fileway,width=50).grid(column=1,row=0)
                Button(erer,text='浏览',command=l,background="#54b8ed",activebackground="#54b8ed").grid(column=2,row=0)
                Button(erer,text='保存',command=ok,width=10,height=2,background="#54b8ed",activebackground="#54b8ed").grid(column=0,row=1)
                Button(erer,text='取消',command=erer.destroy,width=10,height=2,background="#54b8ed",activebackground="#54b8ed").grid(column=2,row=1)
            def show_fun():
                if micro.get()==0:
                    pu=make(thing.get(),micro=False)
                    m.showinfo(parent=putk,title='二维码信息',message=pu.designator)
                else:
                    try:
                        pu=make(thing.get(),micro=True)
                        m.showinfo(parent=putk,title='二维码信息',message=pu.designator)
                    except:
                        m.showerror(parent=putk,title='警告',message='二维码数据过多，无法生成微型码')
            thing=StringVar()
            micro=IntVar()
            micro.set(0)
            scale=IntVar()
            putk=Toplevel(tk)
            putk.resizable(0,0)
            putk.title('创建普通二维码-Hello智能二维码生成器')
            putk.geometry('+500+500')
            putk.attributes('-topmost',1)
            fthings=LabelFrame(putk,text='输入数据')
            fthings.grid(column=0,row=0)
            fsetting=LabelFrame(putk,text='二维码设置')
            fsetting.grid(column=0,row=1)
            fcaozuo=LabelFrame(putk,text='操作')
            fcaozuo.grid(column=1,row=0,rowspan=2)
            Label(fthings,text='请输入二维码包含的文字或网址：').grid(column=0,row=0)
            Entry(fthings,textvariable=thing).grid(column=1,row=0)
            Checkbutton(fsetting,text='生成微型码',variable=micro,onvalue=1,offvalue=0).grid(column=0,row=0,columnspan=2)
            Label(fsetting,text='每个码源占多少像素：').grid(column=0,row=1)
            Entry(fsetting,textvariable=scale).grid(column=1,row=1)
            Button(fcaozuo,text='查看二维码数据',command=show_fun,width=20,height=2,background="#54b8ed",activebackground="#54b8ed").grid()
            Button(fcaozuo,text='生成',command=okpu,width=10,height=2,background="#54b8ed",activebackground="#54b8ed").grid(pady=20)
            Button(fcaozuo,text='取消',command=putk.destroy,width=10,height=2,background="#54b8ed",activebackground="#54b8ed").grid()
        if v.get()=='名片':
            def show_fun():
                ming=helpers.make_mecard(name=name.get(),phone=phone.get(),email=email.get(),city=city.get(),country=country.get())
                m.showinfo(title='二维码数据',message=ming.designator,parent=mingtk)
            def okming():
                try:
                    scale.get()
                except:
                    m.showerror(title='错误',message='“每个码源占多少像素”只能是整数！',parent=mingtk)
                    return
                if scale.get()==0:
                    m.showerror(title='错误',message='“每个码源占多少像素”不能为0！！',parent=mingtk)
                else:
                    def l():
                        f=dialog.asksaveasfilename(title='请选择二维码图片保存地址',parent=erer,filetypes=[('PNG图片格式','.png')],defaultextension='.png')
                        if f=='':
                            return
                        fileway.set(f)
                    def ok():
                        if fileway.get()=='':
                            m.showwarning(title='提示',message='您没有填写或选择保存路径',parent=erer)
                        else:
                            try:
                                ming.save(fileway.get(),scale=scale.get())
                                mingtk.destroy()
                            except:
                                m.showerror(title='错误',message='数据格式或文件路径有误！',parent=erer)
                    ming=helpers.make_mecard(name=name.get(),phone=phone.get(),email=email.get(),city=city.get(),country=country.get())
                    erer=Toplevel(mingtk)
                    erer.title('保存文件-Hello智能二维码生成器')
                    erer.geometry('+400+400')
                    erer.resizable(0,0)
                    erer.attributes('-topmost',1)
                    fileway=StringVar()
                    Label(erer,text='请输入保存地址：').grid(column=0,row=0)
                    Entry(erer,textvariable=fileway,width=50).grid(column=1,row=0)
                    Button(erer,text='浏览',command=l,background="#54b8ed",activebackground="#54b8ed").grid(column=2,row=0)
                    Button(erer,text='保存',command=ok,width=10,height=2,background="#54b8ed",activebackground="#54b8ed").grid(column=0,row=1)
                    Button(erer,text='取消',command=erer.destroy,width=10,height=2,background="#54b8ed",activebackground="#54b8ed").grid(column=2,row=1)
            mingtk=Toplevel(tk)
            mingtk.resizable(0,0)
            mingtk.attributes('-topmost',1)
            mingtk.title('创建名片二维码-Hello智能二维码生成器')
            mingtk.geometry('+500+500')
            shujul=LabelFrame(mingtk,text='输入数据')
            shujul.grid(column=0,row=0)
            shezhil=LabelFrame(mingtk,text='二维码设置')
            shezhil.grid(column=0,row=1)
            caozuol=LabelFrame(mingtk,text='操作')
            caozuol.grid(column=1,row=0,rowspan=2)
            name=StringVar()
            phone=StringVar()
            email=StringVar()
            city=StringVar()
            country=StringVar()
            scale=IntVar()
            Label(shujul,text='姓名:').grid(column=0,row=0)
            Entry(shujul,textvariable=name).grid(column=1,row=0)
            Label(shujul,text='电话:').grid(column=0,row=1)
            Entry(shujul,textvariable=phone).grid(column=1,row=1)
            Label(shujul,text='电子邮箱:').grid(column=0,row=2)
            Entry(shujul,textvariable=email).grid(column=1,row=2)
            Label(shujul,text='所住城市:').grid(column=0,row=3)
            Entry(shujul,textvariable=city).grid(column=1,row=3)
            Label(shujul,text='国家:').grid(column=0,row=4)
            Entry(shujul,textvariable=country).grid(column=1,row=4)
            Label(shezhil,text='每个码源占多少像素：').grid(column=0,row=0)
            Entry(shezhil,textvariable=scale).grid(column=1,row=0)
            Button(caozuol,text='查看二维码数据',command=show_fun,width=20,height=2,background="#54b8ed",activebackground="#54b8ed").grid()
            Button(caozuol,text='生成',command=okming,width=10,height=2,background="#54b8ed",activebackground="#54b8ed").grid(pady=20)
            Button(caozuol,text='取消',command=mingtk.destroy,width=10,height=2,background="#54b8ed",activebackground="#54b8ed").grid()
        elif v.get()=='wifi':
            def okming():
                if ssid.get()=='' or password.get()=='':
                    m.showerror(title='错误',message='有必填数据没有填！',parent=ertk)
                else:
                    try:
                        scale.get()
                    except:
                        m.showerror(title='错误',message='“每个码源占多少像素”只能是整数！',parent=ertk)
                        return
                    if scale.get()==0:
                        m.showerror(title='错误',message='“每个码源占多少像素”不能为0！！',parent=ertk)
                    else:
                        def l():
                            f=dialog.asksaveasfilename(title='请选择二维码图片保存地址',parent=erer,filetypes=[('PNG图片格式','.png')],defaultextension='.png')
                            if f=='':
                                return
                            fileway.set(f)
                        def ok():
                            if fileway.get()=='':
                                m.showwarning(title='提示',message='您没有填写或选择保存路径',parent=erer)
                            else:
                                try:
                                    er.save(fileway.get(),scale=scale.get())
                                    ertk.destroy()
                                except:
                                    m.showerror(title='错误',message='数据格式或文件路径有误！',parent=erer)
                        er=helpers.make_wifi(ssid=ssid.get(),password=password.get(),security=c.get())
                        erer=Toplevel(ertk)
                        erer.title('保存文件-Hello智能二维码生成器')
                        erer.geometry('+400+400')
                        erer.resizable(0,0)
                        erer.attributes('-topmost',1)
                        fileway=StringVar()
                        Label(erer,text='请输入保存地址：').grid(column=0,row=0)
                        Entry(erer,textvariable=fileway,width=50).grid(column=1,row=0)
                        Button(erer,text='浏览',command=l,background="#54b8ed",activebackground="#54b8ed").grid(column=2,row=0)
                        Button(erer,text='保存',command=ok,width=10,height=2,background="#54b8ed",activebackground="#54b8ed").grid(column=0,row=1)
                        Button(erer,text='取消',command=erer.destroy,width=10,height=2,background="#54b8ed",activebackground="#54b8ed").grid(column=2,row=1)
            def show_fun():
                if ssid.get()=='' or password.get()=='':
                    m.showerror(title='错误',message='有必填数据没有填！',parent=ertk)
                else:
                    er=helpers.make_wifi(ssid=ssid.get(),password=password.get(),security=c.get())
                    m.showinfo(parent=ertk,title='二维码信息',message=er.designator)
            ertk=Toplevel(tk)
            ertk.resizable(0,0)
            ertk.title('创建wifi二维码-Hello智能二维码生成器')
            ertk.geometry('+500+500')
            ertk.attributes('-topmost',1)
            shujul=LabelFrame(ertk,text='输入数据')
            shujul.grid(column=0,row=0)
            shezhil=LabelFrame(ertk,text='二维码设置')
            shezhil.grid(column=0,row=1)
            caozuol=LabelFrame(ertk,text='操作')
            caozuol.grid(column=1,row=0,rowspan=2)
            ssid=StringVar()
            password=StringVar()
            scale=IntVar()
            Label(shujul,text='wifi名称（必填）：').grid(column=0,row=0)
            Entry(shujul,textvariable=ssid).grid(column=1,row=0)
            Label(shujul,text='wifi密码（必填）：').grid(column=0,row=1)
            Entry(shujul,textvariable=password,show='*').grid(column=1,row=1)
            Label(shujul,text='wifi安全性（必填）：').grid(column=0,row=2)
            c=ttk.Combobox(shujul)
            c.grid(column=1,row=2)
            c['value']=('WEP','WPA')
            c['state']='readonly'
            c.set('WPA')
            Label(shezhil,text='每个码源占多少像素：').grid(column=0,row=0)
            Entry(shezhil,textvariable=scale).grid(column=1,row=0)
            Button(caozuol,text='查看二维码数据',command=show_fun,width=20,height=2,background="#54b8ed",activebackground="#54b8ed").grid()
            Button(caozuol,text='生成',command=okming,width=10,height=2,background="#54b8ed",activebackground="#54b8ed").grid(pady=20)
            Button(caozuol,text='取消',command=ertk.destroy,width=10,height=2,background="#54b8ed",activebackground="#54b8ed").grid()
    F=LabelFrame(tk,text='请选择一个模式')
    F.grid(column=0,row=0,columnspan=3)
    Radiobutton(F,text='生成普通二维码',variable=v,value='普通').grid()
    Radiobutton(F,text='生成名片二维码',variable=v,value='名片').grid()
    Radiobutton(F,text='生成wifi二维码',variable=v,value='wifi').grid()
    Button(tk,text='创建',command=ok,width=10,height=2,background="#54b8ed",activebackground="#54b8ed").grid(column=1,row=1,pady=20)
    Button(tk,text='使用前\n必读！',command=shotishi,width=10,height=2,background="#54b8ed",activebackground="#54b8ed").grid(column=0,row=2)
    Button(tk,text='关闭',command=tk.destroy,width=10,height=2,background="#54b8ed",activebackground="#54b8ed").grid(column=1,row=2,padx=30)
    Button(tk,text='关于',command=about,width=10,height=2,background="#54b8ed",activebackground="#54b8ed").grid(column=2,row=2,pady=30)
    tk.mainloop()

#天气预报
from tkinter import *
import urllib.request
import gzip
import json
from tkinter import messagebox
def temp():
    root = Tk()
 
 
    def main():
        root.title('实时天气查询器')  
        Label(root, text='请输入城市').grid(row=0, column=0) 
        enter = Entry(root)  
        enter.grid(row=0, column=1, padx=20, pady=20)  
        enter.delete(0, END)  
        enter.insert(0, '输入吧')  
        enter_text = enter.get()
     
        running = 1
     
        def get_weather_data():  
            city_name = enter.get()  
            url1 = 'http://wthrcdn.etouch.cn/weather_mini?city=' + urllib.parse.quote(city_name)
            url2 = 'http://wthrcdn.etouch.cn/weather_mini?citykey=101010100'
            weather_data = urllib.request.urlopen(url1).read()
            weather_data = gzip.decompress(weather_data).decode('utf-8')
            weather_dict = json.loads(weather_data)
            if weather_dict.get('desc') == 'invilad-citykey':
                print(messagebox.askokcancel("错误", "您输入的城市名有误，或者天气中心未收录你所在城市"))
            else:
                show_data(weather_dict, city_name)
     
        def show_data(weather_dict, city_name): 
            forecast = weather_dict.get('data').get('forecast')  
            root1 = Tk()
            root1.geometry('1000x300')  
            root1.title(city_name + '天气状况')  
     
            for i in range(5):  
                LANGS = [(forecast[i].get('date'), '日期'),
                         (forecast[i].get('fengxiang'), '风向'),
                         (str(forecast[i].get('fengji')), '风级'),
                         (forecast[i].get('high'), '最高温'),
                         (forecast[i].get('low'), '最低温'),
                         (forecast[i].get('type'), '天气')]
                group = LabelFrame(root1, text='天气状况', padx=0, pady=0) 
                group.pack(padx=11, pady=0, side=LEFT)  
                for lang, value in LANGS:  
                    c = Label(group, text=value + ': ' + lang)
                    c.pack(anchor=W)
            Label(root1, text='今日温馨提示:' + weather_dict.get('data').get('ganmao'),
                  fg='red').place(x=40, y=20, height=40)  
            Button(root1, text='确认并退出', width=10, command=root1.destroy).place(x=500, y=230, width=80, height=40)  
            root1.mainloop()
        Button(root, text="确认", width=10, command=get_weather_data) \
            .grid(row=3, column=0, sticky=W, padx=10, pady=5)
        Button(root, text='退出', width=10, command=root.destroy) \
            .grid(row=3, column=1, sticky=E, padx=10, pady=5)
        if running == 1:
            root.mainloop()
     
    if __name__ == '__main__':
        main()

#翻译器
import requests
from requests.exceptions import RequestException
import tkinter as tk
def translate():
    class Translate():
        def __init__(self):
            self.window = tk.Tk()  #创建window窗口
            self.window.title("简易翻译器")  # 定义窗口名称
            self.window.resizable(0,0)  # 禁止调整窗口大小
            self.input = tk.Entry(self.window, width=80)  # 创建一个输入框,并设置尺寸
            self.info = tk.Text(self.window, height=18)   # 创建一个文本展示框，并设置尺寸
            # 添加一个按钮，用于触发翻译功能
            self.t_button = tk.Button(self.window, text='翻译', relief=tk.RAISED, width=8, height=1, command=self.fanyi)
            # 添加一个按钮，用于触发清空输入框功能
            self.c_button1 = tk.Button(self.window, text='清空输入', relief=tk.RAISED, width=8, height=1, command=self.cle_e)
            # 添加一个按钮，用于触发清空输出框功能
            self.c_button2 = tk.Button(self.window, text='清空输出', relief=tk.RAISED,width=8, height=1, command=self.cle)
            
    
        def gui_arrang(self):
            """完成页面元素布局，设置各部件的位置"""
            self.input.grid(row=0,sticky="W",padx=1)
            self.info.grid(row=1)
            self.t_button.grid(row=0,column=1,padx=2)
            self.c_button1.grid(row=0, column=2, padx=2)
            self.c_button2.grid(row=0,column=3,padx=2)
    
        def fanyi(self):
            """定义一个函数，完成翻译功能"""
            original_str = self.input.get()  # 定义一个变量，用来接收输入框输入的值
            data = {
                'doctype': 'json',
                'type': 'AUTO',
                'i': original_str  # 将输入框输入的值，赋给接口参数
            }
            url = "http://fanyi.youdao.com/translate"
            try:
                r = requests.get(url, params=data)
                if r.status_code == 200:
                    result = r.json()
                    translate_result = result['translateResult'][0][0]["tgt"]
                    self.info.delete(1.0, "end")  # 输出翻译内容前，先清空输出框的内容
                    self.info.insert('end',translate_result)  # 将翻译结果添加到输出框中
            except RequestException:
                self.info.insert('end', "发生错误")
        def cle(self):
            """定义一个函数，用于清空输出框的内容"""
            self.info.delete(1.0,"end")  # 从第一行清除到最后一行
    
        def cle_e(self):
            """定义一个函数，用于清空输入框的内容"""
            self.input.delete(0,"end")
    
    def main():
        t = Translate()
        t.gui_arrang()
        tk.mainloop()
    
    if __name__ == '__main__':
        main()

#短信发送器
from tkinter import*;from tkinter import messagebox;from tkinter.ttk import*
from xes.sms import*
def smstool():
    def sk():
        z=Enter.get(),Enter1.get()
        window.destroy()
        send_msg(z[0],z[1])
        
    def callback():
        res=messagebox.askokcancel("","您确定要退出吗？")

        if res==True:
            window.destroy()
        else:
            return

    window = Tk()
    window.title('短信发送器')
    window.geometry("655x80")
    Enter=Entry(window)
    Enter1=Entry(window)
    lw=Label(window,text="输入手机号：")
    lw1=Label(window,text="输入信息：")
    dtn=Button(window,text="点击发送",command=sk)
    dtn.pack(side=TOP,fill=BOTH,expand=True)
    Enter.pack(side=RIGHT,fill=X,expand=True)
    lw.pack(side=RIGHT,fill=BOTH,expand=True)
    Enter1.pack(side=RIGHT,fill=X,expand=True)
    lw1.pack(side=RIGHT,fill=BOTH,expand=True)
    dtn.pack(side=TOP,fill=BOTH,expand=True)
    window.protocol("WM_DELETE_WINDOW",callback)

    window.mainloop()

#新闻查看器
import requests, bs4, time, tkinter
newsIndex = 0
response = requests.get("https://www.36kr.com/information/technology")
response.encoding = "UTF-8"
soup = bs4.BeautifulSoup(response.text,"lxml")
data = soup.find_all(name = "div", class_ = "article-item-info clearfloat")
def xinwen():
    print(len(data))
    def refreshNews():
        global data,newsIndex
        if newsIndex < len(data):
            text = data[newsIndex].find_all(name = "a")
            listb.insert(0,"-"*30)
            listb.insert(0,"作  者:" + text[2].text)
            listb.insert(0,"摘  要:" + text[1].text)
            listb.insert(0,"标  题:" + text[0].text)
            newsIndex += 1

    root = tkinter.Tk(className = "python")
    root.geometry("800x600")
    root.configure(background = "gray")

    listb = tkinter.Listbox(root, width = 90, height = 30, bg = "black", fg = "red")
    listb.pack()

    button1 = tkinter.Button(root, text = "显示新闻", command = refreshNews )
    button1.pack()

    root.mainloop()

#音乐播放器
import tkinter
from tkinter import Button
from tkinter import Label
from tkinter import Entry
from tkinter import Scale
from tkinter import Label,PhotoImage
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import Toplevel
from pymediainfo import MediaInfo
import re
from tkinter import Message
import threading
import pygame
import time
import os
import random
from tkinter.filedialog   import askopenfilename
from tkinter.filedialog import askdirectory
from tkinter import StringVar
num = 0
fy = 2
w3 = " "
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}
headers1 = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': '_ga=GA1.2.1500987479.1595755923; _gid=GA1.2.568444838.1596065504; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1595755923,1596065505; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1596076178; kw_token=P5XA2TZXG9',
    'csrf': 'P5XA2TZXG9',
    'Host': 'www.kuwo.cn',
    'Referer': 'http://www.kuwo.cn/search/list?key=%E5%A4%95%E9%98%B3%E7%BA%A2',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}
headers2 = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': '_ga=GA1.2.1500987479.1595755923; _gid=GA1.2.568444838.1596065504; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1595755923,1596065505; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1596078189; _gat=1; kw_token=IJATWHHGI8',
    'csrf': 'IJATWHHGI8',
    'Host': 'www.kuwo.cn',
    'Referer': 'http://www.kuwo.cn/search/list?key=%E6%A2%A6%E7%9A%84%E5%9C%B0%E6%96%B9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',

}
def musics():
    top=tkinter.Tk()
    top.geometry("800x400")
    top.title("我的音乐播放器")
    def printsrceen(texts):
        t=int(texts)
        top.attributes("-alpha",t/100)
     
    screenwidth = top.winfo_screenwidth()
    screenheight = top.winfo_screenheight() - 100

    pygame.init()
    path=StringVar()
    paths=StringVar()
    patht=StringVar()
    v=StringVar()
    v1=StringVar()


    def callback():#搜索本地文件
        path_= askopenfilename() 
        return path_





    def selectPath():#随机播放
        folder_path="D:/音乐"
        folder_list = os.listdir(folder_path)#遍历文件夹里面每个文件
        list=[]
        count=0
        for i in folder_list:#将文件夹里的文件按顺序传提给变量i  此处区别os.walk()
            if os.path.splitext(i)[1]=='.flac':#提取特定后缀文件'.***'
                list.append (i)
            #print(type(list))
                count=count+1
        #print(count)
               
        s=random.randint(0,(count-1))#获取随机数
        file=list[s]
        fil=folder_path+"\\"+file
     
       
        pygame.mixer.music.load(fil)
        pygame.mixer.music.play(1,0)
        media_info = MediaInfo.parse(fil)
        data = media_info.to_json()#medio到json()这两行是获取文件的所有属性
        rst=re.search('other_duration.*?(.*?)min(.*?)s.*?',data)
        t=int(rst.group(0)[19:20])
        r=int(rst.group(0)[-4:-2])
        m=(t*60+r)*1000
        
        musictime=str(t)+':'+str(r)
        l2.config(text=file)
        l3.config(text=musictime)
        lbTime=tkinter.Label(top,anchor='w')
        lbTime.place(x=25,y=150)
        def autoclose():
            for i in range(m//1000):
                lbTime['text']='-{} /'.format((m//1000)-i)
                time.sleep(1)
        t=threading.Thread(target=autoclose)
        t.start()
        loopl=top.after(m,selectPath)
       
       

    def printScale(text):
        t=int(text)
        pygame.mixer.music.set_volume(t/100)
        
    def update_timeText():
        # Get the current time, note you can change the format as you wish
        current = time.strftime("%H:%M:%S")#获取当前时间

    # Update the timeText Label box with the current time
        timeText.configure(text=current)

    # Call the update_timeText() function after 1 second
        top.after(1000, update_timeText)


        
    def remind():
        top = Toplevel()#新建一个tkinter窗口
        top.title('使用提示')
        top.geometry("200x200")
        t="半分钟后开始播放音乐"
        msg = Message(top,text = t)
        msg.config( font=('times', 18, 'italic'))
        msg.place(x=0,y=0)
        lbTime=tkinter.Label(top,fg="red",anchor='w')
        lbTime.place(x=100,y=45)
        def autoclose():
            for i in range(30):
                lbTime['text']='距离窗口关闭还有{}秒'.format(30-i)
                time.sleep(1)
            top.destroy()
        t=threading.Thread(target=autoclose)
        t.start()
        loopl=top.after(60*59500,remind)

        
        
    def reminds():
        top = Toplevel()
        top.title('使用提示')
        top.geometry("200x200")
        t="宝贝可以休息一会啦"
        msg = Message(top,text = t)
        msg.config( font=('times', 24, 'italic'))
        msg.place(x=0,y=0)
        folder_path="D:/音乐"
        folder_list = os.listdir(folder_path)#遍历文件夹里面每个文件
        list=[]
        count=0
        for i in folder_list:#将文件夹里的文件按顺序传提给变量i  此处区别os.walk()
            if os.path.splitext(i)[1]=='.flac':#提取特定后缀文件'.***'
                list.append (i)
            #print(type(list))
                count=count+1
            #print(count)
        s=random.randint(0,(count-1))
        file=list[s]
        fil=folder_path+"\\"+file
        pygame.mixer.music.load(fil)
        pygame.mixer.music.play(1,0)
        lbTime=tkinter.Label(top,fg="red",anchor='w')
        lbTime.place(x=100,y=45)
        def autoclose():
            for i in range(300):
                lbTime['text']='距离窗口关闭还有{}秒'.format(300-i)
                time.sleep(1)
            top.destroy()
        t=threading.Thread(target=autoclose)
        t.start()
        loopl=top.after(60*60000,reminds)


        

    def play():#播放音乐
        f=callback()#选择制定文件
        pygame.mixer.music.load(f)
        pygame.mixer.music.play()
        path.set(f)
        media_info = MediaInfo.parse(f)
        data = media_info.to_json()#medio到json()这两行是获取文件的所有属性
        rst=re.search('other_duration.*?(.*?)min(.*?)s.*?',data)
        t=int(rst.group(0)[19:20])
        r=int(rst.group(0)[-4:-2])
        m=(t*60+r)*1000
        musictime=str(t)+':'+str(r)
        l2.config(text=f)
        l3.config(text=musictime)
        lbTime=tkinter.Label(top,anchor='w')
        lbTime.place(x=25,y=150)
        def autoclose():
            for i in range(m//1000):
                lbTime['text']='-{} /'.format((m//1000)-i)
                time.sleep(1)
        t=threading.Thread(target=autoclose)
        t.start()
        loopl=top.after(m,selectPath)
        
       
    def stop():
        pygame.mixer.music.stop()#停止播放
        top.after_cancel(loopl)
        

    def pause():
        pygame.mixer.music.pause()#暂停   
    def unpause():
        pygame.mixer.music.unpause()#继续播放   
    def choosepic():#保存的路径不能有中文，若需要中文则吧/换成\
        path_s=askopenfilename()
        paths.set(path_s)
        img_open=Image.open(e1.get())
        img=ImageTk.PhotoImage(img_open)
        l1.config(image=img)
        l1.image=img



        
    def create():
        top = Toplevel()
        top.title('使用提示')
        top.geometry("400x400")
        t="关于照片，新建一个存放图片的文件，用英文命名，然后存里面的图片也用英文命名。关于音乐: 新建一个名字叫音乐的文件，把歌曲添加到该文件夹。"
        msg = Message(top,text = t)
        msg.config( font=('times', 24, 'italic'))
        msg.place(x=0,y=0)


    def loop():
        top.after(60*60000,reminds)
        top.after(60*59500,remind)

        
    def loops():
        selectPath()
    def gettime():
        t=time.strftime('%H%M%S')
        s=int(t[0:2])
        d=int(t[2:4])
        f=int(t[4:6])
        g=s*60*60+d*60+f
        return g    


        
    errmsg = 'Error!'
    #时间
    timeText = Label(top, text="", font=("Helvetica", 15))
    timeText.place(x=180,y=370)
    update_timeText()
    #选择文件
    xl = Button(top,text="选择文件",command=play,width=10,bg="sky blue")
    xl.place(x=20,y=20)
    Entry(top,text=path,width=25,state='readonly').place(x=120,y=20)

    #选择图片
    yl = Button(top,text='选择图片', command=choosepic,width=10,bg="sky blue")
    yl.place(x=20,y=55)
    e1=Entry(top,text=paths,state='readonly',width=25)
    e1.place(x=120,y=55)
    l1=Label(top)#图片放置位置
    l1.place(x=320,y=0)

   

    #随机播放
    Button(top,text="随机播放",command=selectPath,width=7,bg="sky blue").place(x=20,y=225)
    l2=Label(top,text='',width=25,font=("Helvetica", 16))#音乐名
    l2.place(x=0,y=100)
    Button(top,text="下一首",command=loops,width=5,bg="sky blue").place(x=100,y=225)
    l3=Label(top,text='',width=15)#音乐时长
    l3.place(x=24,y=150)
    #暂停，继续播放，结束播放
    Button(top,text="暂停",command=pause,width=7,bg="sky blue").place(x=170,y=245)
    Button(top,text="继续播放",command=unpause,width=7,bg="sky blue").place(x=170,y=205)
    Button(top,text="结束播放",command=stop,width=7,bg="sky blue").place(x=240,y=225)

    #提醒功能
    Button(top,text='提醒功能', command=loop,width=10,bg="sky blue").place(x=20,y=325)
    #使用说明
    Button(top,text="使用说明",command = create,width=10,bg="sky blue").place(x=20,y=370)
    #音量
    w1 = Scale(top, from_=0,to=100, orient="horizontal",length=75,variable=v,command=printScale,label="音量")
    w1.place(x=240,y=145)

    w2 = Scale(top, from_=30,to=100, orient="horizontal",length=100,variable=v1,command=printsrceen,label="透明度")
    w2.place(x=150,y=290)

    top.mainloop()

#图片查看器
from os import *
def photos():
    system("图片查看软件.exe")

#文件整理器
import sys
import platform
#检测系统
sysstr = platform.system()
if sysstr!="Windows":
    from tkinter import *
    from tkinter import messagebox
    tk=Tk()
    tk.withdraw()
    messagebox.showerror("错误","此程序仅支持windows!",parent=tk)
    sys.exit()
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import shutil
def zhengli():

    global path
    path=None
    global showpath
    showpath=None
    global defultdir
    defultdir=os.getcwd()

    class MainWindow(QMainWindow):
        def closeEvent(self,event):
            f=QMessageBox.question(window,"提示","确认退出吗？")
            
            if f==QMessageBox.No:
                event.ignore()
            else:
                event.accept()
    #文件类型的字典表（如果类型有遗漏欢迎提出）
    formats={
        "音频":[".mp3",".wav",".m4a"],
        "视频":[".mp4",".mov",".wmv"],
        "图片":[".jpg",".png",".gif",".bmp",".ico"],
        "文档":[".txt",".doc",".docx",".xls",".xlsx",".ppt",".pptx",".pdf"],
        "应用程序":[".vbs",".bat",".msi",".exe",".cmd"],
        "压缩包":[".zip",".rar",".7z"]
    }
    #选择文件夹
    def choose():
        global path
        global showpath
        a=QFileDialog.getExistingDirectory(window,"选取要整理的文件夹")
        if a!='':
            path=a
            os.chdir(path)
            btngo.setEnabled(True)
            label2.setText("已选择文件夹")
            label2.setToolTip("<font color='#0762f8'>已选择文件夹")
            if len(path) >= 17:
                showpath=path[0:12]+'...'
            label3.setText('''<a href='#' style="text-decoration:none;color:black;">'''+showpath)
            palette=QPalette()
            palette.setColor(QPalette.WindowText,QColor("#0762f8"))
            label2.setPalette(palette)
    #选择文件夹
    #弹窗显示文件夹路径
    def showdir():
        dialogdir=QDialog(window)
        dialogdir.setWindowTitle("智能文件夹整理器（作者：陈明翰）- 显示文件夹路径")
        dialogdir.setModal(Qt.ApplicationModal)
        
        layout=QVBoxLayout()
        labeldir=QLabel()
        labeldir.setText(path)
        labeldir.setToolTip("完整文件夹路径")
        labeldir.setFont(QFont("Microsoft Yahei",20))
        labeldir.setAlignment(Qt.AlignCenter)
        labelopen=QLabel("<a href='#'>在资源管理器打开")
        labelopen.setToolTip("在资源管理器打开")
        labelopen.setFont(QFont("Microsoft Yahei",20))
        labelopen.setAlignment(Qt.AlignRight)
        labelopen.linkActivated.connect(lambda:os.system("explorer ."))
        
        layout.addWidget(labeldir,alignment=Qt.AlignCenter)
        layout.addWidget(labelopen,alignment=Qt.AlignRight)
        
        dialogdir.setLayout(layout)
        dialogdir.setFixedSize(dialogdir.minimumWidth(),dialogdir.minimumHeight())
        dialogdir.exec()
    #弹窗显示文件夹路径
    #整理功能
    def go():
        label2.setText("整理中")
        label2.setToolTip("<font color='#c89100'>整理中")
        palette=QPalette()
        palette.setColor(QPalette.WindowText,QColor("#c89100"))
        label2.setPalette(palette)
        try:
            for i in os.listdir():
                if i=="文件夹" or i=="压缩包" or i=="应用程序" or i=="文档" or i=="图片" or i=="视频" or i=="音频" or i=="其他":
                    continue
                ext=os.path.splitext(i)[-1].lower()
                if os.path.isdir(i):
                    if not os.path.isdir("文件夹"):
                        os.mkdir("文件夹")
                    shutil.move(i,f"文件夹/{i}")
                    continue
                fff=False
                for d,exts in formats.items():
                    if not os.path.isdir(d):
                        os.mkdir(d)
                    if ext in exts:
                        shutil.move(i,f"{d}/{i}")
                        fff=True
                if fff==False:
                    if not os.path.isdir("其他"):
                        os.mkdir("其他")
                    shutil.move(i,f"其他/{i}")
            label2.setText("整理成功")
            label2.setToolTip("<font color='#009170'>整理成功")
            palette=QPalette()
            palette.setColor(QPalette.WindowText,QColor("#009170"))
            label2.setPalette(palette)
            QMessageBox.information(window,"提示","整理成功")

        except:
            label2.setText("整理失败")
            label2.setToolTip("<font color='#fe435a'>整理失败")
            palette=QPalette()
            palette.setColor(QPalette.WindowText,QColor("#fe435a"))
            label2.setPalette(palette)
            QMessageBox.critical(window,"错误","整理失败！")
    #整理功能
    #使用帮助
    def use_help():
        dialog=QDialog(window)
        dialog.setWindowTitle("智能文件夹整理器（作者：陈明翰）- 使用帮助")
        dialog.setFixedSize(dialog.minimumWidth(),dialog.minimumHeight())
        dialog.setModal(Qt.ApplicationModal)

        layouthelp=QVBoxLayout()

        labelhelp=QLabel("作者：陈明翰，转载请保留原作者。\n本作品能够直接帮您为乱七八糟的文件夹进行分类，\n只需要先选择要整理的文件夹，然后开始整理即可。\n（详细使用步骤可观看帮助视频↓）")
        
        labelhelp.setToolTip("帮助信息")
        
        labelhelp.setFont(QFont("Microsoft Yahei",20))
        labelhelp.setAlignment(Qt.AlignCenter)
        
        

        layouthelp.addWidget(labelhelp)
        

        dialog.setLayout(layouthelp)
        dialog.exec()
    #使用帮助
    #下面是界面代码
    app=QApplication(sys.argv)
    window=MainWindow()

    window.setWindowIcon(QIcon("icon.png"))
    window.setWindowTitle("智能文件夹整理器（作者：陈明翰）")

    QToolTip.setFont(QFont("Microsoft Yahei",12))
    layout=QGridLayout()
    layout.setAlignment(Qt.AlignCenter)
    widget=QWidget()

    btnchoose=QPushButton("选择文件夹")#140 41
    btnchoose.setFixedSize(140,41)
    btnchoose.setToolTip("选择文件夹")
    btnchoose.setFont(QFont("Microsoft Yahei",20))
    btnchoose.clicked.connect(choose)

    btnabout=QPushButton("关于我们")
    btnabout.setFixedSize(140,41)
    btnabout.setToolTip("关于我们")
    btnabout.setFont(QFont("Microsoft Yahei",20))
    btnabout.clicked.connect(lambda:QMessageBox.about(window,"关于我们","Hello智能文件夹整理器\n     （作者：陈明翰）\n    转载请保留原作者！"))

    label1=QLabel("当前状态:")
    label1.setSizePolicy(QSizePolicy.Minimum,QSizePolicy.Minimum)
    label1.setToolTip("当前状态")
    label1.setFont(QFont("Microsoft Yahei",20))

    label2=QLabel("未选择文件夹")
    label2.setSizePolicy(QSizePolicy.Minimum,QSizePolicy.Minimum)
    label2.setToolTip("未选择文件夹")
    label2.setFont(QFont("Microsoft Yahei",20))

    label3=QLabel("文件夹路径")
    label3.setSizePolicy(QSizePolicy.Minimum,QSizePolicy.Minimum)
    label3.setToolTip("文件夹路径")
    label3.linkActivated.connect(showdir)
    label3.setFont(QFont("Microsoft Yahei",20))

    btngo=QPushButton("开始整理")
    btngo.setFixedSize(140,41)
    btngo.setToolTip("开始整理")
    btngo.setEnabled(False)
    btngo.setFont(QFont("Microsoft Yahei",20))
    btngo.clicked.connect(go)

    btnquit=QPushButton("使用帮助")
    btnquit.setFixedSize(140,41)
    btnquit.setToolTip("使用帮助")
    btnquit.setFont(QFont("Microsoft Yahei",20))
    btnquit.clicked.connect(use_help)

    layout.addWidget(label1,0,0,alignment=Qt.AlignCenter)
    layout.addWidget(label2,0,1,alignment=Qt.AlignCenter)
    layout.addWidget(label3,1,0,1,2,alignment=Qt.AlignCenter)
    layout.addWidget(btnchoose,2,0,alignment=Qt.AlignCenter)
    layout.addWidget(btngo,2,1,alignment=Qt.AlignCenter)
    layout.addWidget(btnabout,3,0,alignment=Qt.AlignCenter)
    layout.addWidget(btnquit,3,1,alignment=Qt.AlignCenter)
    widget.setLayout(layout)
    window.setToolTip("智能文件夹整理器（作者：陈明翰）")
    window.setCentralWidget(widget)
    window.setFixedSize(356,188)

    window.show()
    sys.exit(app.exec_())

#奥运会结果
import pygame,sys,requests,tkinter
from bs4 import BeautifulSoup
from tkinter import messagebox
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36'}
model = requests.get("https://tiyu.baidu.com/tokyoly/home/tab/奖牌榜/from/pc",headers=headers).text
find = BeautifulSoup(model)
findtest = find.find_all("div", class_="item-gold china")
findtestb = find.find_all("div", class_="item-silver china")
findtestc = find.find_all("div", class_="item-copper china")
sort = find.find_all("span", class_="name")
gold = find.find_all("div", class_="item-gold")
sil = find.find_all("div", class_="item-silver")
cop = find.find_all("div", class_="item-copper")
tadic={}
cou=0
def aoyunhui():
    for i in range(len(sort)):
        if str(i) == "0":
            aft=[int(findtest[0].text),int(findtestb[0].text),int(findtestc[0].text),int(findtest[0].text)+int(findtestb[0].text)+int(findtestc[0].text)]
        else:
            aft=[int(gold[i].text),int(sil[i].text),int(cop[i].text),int(gold[i].text)+int(sil[i].text)+int(cop[i].text)]
        tadic[sort[i].text]=aft
    def nextd():
        global tadic
        global cou
        global sort
        if cou >= len(sort):
            messagebox.showwarning("提示","已是最后一个了")
        elif cou+10 >=len(sort):
            for i in range(len(sort)-cou):
                if len(sort[cou].text) <6:
                    wm = 6-len(sort[cou].text)
                if len(sort[cou].text) == 4:
                    wm +=1       
                elif len(sort[cou].text) == 3:
                    wm +=2 
                elif len(sort[cou].text) == 2:
                    wm +=3 
                else:
                    wm=0
                m.insert("end","\n"+sort[cou].text+":") 
                for i in range(wm):
                    m.insert("end"," ")
                m.insert("end",str(tadic[sort[cou].text][0])+"  "+str(tadic[sort[cou].text][1])+"  "+str(tadic[sort[cou].text][2])+"  "+str(tadic[sort[cou].text][3])+"  ")
                cou+=1
        else:
            for i in range(10):
                if len(sort[cou].text) <6:
                    wm = 6-len(sort[cou].text)
                if len(sort[cou].text) == 4:
                    wm +=3       
                elif len(sort[cou].text) == 3:
                    wm +=5  
                elif len(sort[cou].text) == 2:
                    wm +=7
                else:
                    wm=0
                m.insert("end","\n"+sort[cou].text+":") 
                for i in range(wm):
                    m.insert("end"," ")
                m.insert("end",str(tadic[sort[cou].text][0])+"  "+str(tadic[sort[cou].text][1])+"  "+str(tadic[sort[cou].text][2])+"  "+str(tadic[sort[cou].text][3])+"  ")
                cou+=1
    root = tkinter.Tk()
    root.geometry('+600+400')
    root.resizable(0,0)
    root.configure(background="skyblue")
    root.geometry("300x600")
    root.resizable(0,0)
    root.title("奥运金牌排行榜")
    m = tkinter.Text(root)
    m.insert("insert","国家           金  银  铜  总\n")
    b = tkinter.Button(root,text="下一页",command=nextd)
    m.place(x=20,y=20,width=260,height=460)
    b.place(x=100,y=515,width=100,height=30)
    root.mainloop()

#搜索导航
def sousou():
    cefpython.Initialize()
    
    def fangwen(a):
    
        if "https://" in a:
            a = a.replace("https://","http://")
        if "http://" not in a:
            a = "http://" + a
        cefpython.CreateBrowserSync(cefpython.WindowInfo(),url = a)
        cefpython.MessageLoop()

    fangwen("https://livefile.xesimg.com/programme/python_assets/612a2e8f7ee61e4745beccc5cd20bf33.html")
    fasdasdf1()

#谷歌小恐龙
def dino():
    # 地图
    class GameBackground:
        image1 = None
        image2 = None
        main_scene = None
        speed = 10 # 滚动速度
        x1 = None
        x2 = None
    
        # 初始化地图
        def __init__(self, scene):
            # 加载相同张图片资源,做交替实现地图滚动
            self.image1 = pygame.image.load("images/dragon/map.png")
            self.image2 = self.image1
            # 保存场景对象
            self.main_scene = scene
            # 辅助移动地图
            self.x1 = 0
            self.x2 = self.main_scene.size[0]
    
        # 计算地图图片绘制坐标
        def action(self):
            self.x1 = self.x1 - self.speed
            self.x2 = self.x2 - self.speed
            if self.x1 <= -self.main_scene.size[0]:
                self.x1 = 0
            if self.x2 <= 0:
                self.x2 = self.main_scene.size[0]
    
        # 绘制地图的两张图片
        def draw(self):
            map_y = self.main_scene.size[1] - self.image1.get_height()
            self.main_scene.scene.blit(self.image1, (self.x1, map_y))
            self.main_scene.scene.blit(self.image2, (self.x2, map_y))
    
    # 云
    class Cloud:
        speed = 1
        image = None
        x = None
        y = None
    
        def __init__(self, x, y, image):
            self.x = x
            self.y = y
            self.image = image
    
        def move(self):
            self.x -= self.speed
    
    # 仙人掌
    class Cactus:
        speed = 10
        image = None
        x = None
        y = None
        width = None
        height = None
    
        def __init__(self, x, y, image):
            self.x = x
            self.y = y
            self.image = image
            self.width = image.get_width()
            self.height = image.get_height()
    
        def move(self):
            self.x -= self.speed
    
    # 鸟
    class Bird:
        speed = 15.5
        image = None
        x = None
        y = None
        width = None
        height = None
        index = 0
        main_scene = None
        ret = 1
    
        def __init__(self, x, y, image, main_scene):
            self.x = x
            self.y = y
            self.image = image
            self.main_scene = main_scene
            image = self.image[self.index]
            self.width = image.get_width()
            self.height = image.get_height()
    
        def move(self):
            self.x -= self.speed
    
        def draw(self):
            if self.ret <= 8:
                self.index = 0
            else:
                self.index = 1
    
            if self.ret == 16:
                self.ret = 0
    
            image = self.image[self.index]
            self.main_scene.scene.blit(image, (self.x, self.y))
            self.ret += 1
    
    # 恐龙
    class Dragon:
        speed = 10
        image = None
        x = None
        y = None
        width = None
        height = None
        index = 0
        main_scene = None
        ret = 1
        style = 0 # 0：站立，1：蹲下
        jump = 0 # 0: 未起跳，1：开始上升，2：开始下降
        jump_y_add = 0
        is_hit = 0
    
        def __init__(self, x, y, image, main_scene):
            self.x = x
            self.y = y
            self.image = image
            self.main_scene = main_scene
    
        def set_jump(self):
            if self.style == 0 and self.jump == 0:
                self.jump = 1
                self.main_scene.jump_sound.play()
    
        def move(self):
            if self.jump == 1:
                self.y -= 10
                self.jump_y_add += 10
                if self.jump_y_add == 200:
                    self.jump = 2
    
            if self.jump == 2:
                self.y += 10
                self.jump_y_add -= 10
                if self.jump_y_add == 0:
                    self.jump = 0
    
        def draw(self):
            if self.ret <= 5:
                if self.style == 0:
                    self.index = 0
                else:
                    self.index = 2
            else:
                if self.style == 0:
                    self.index = 1
                else:
                    self.index = 3
    
            if self.ret == 10:
                self.ret = 0
    
            image = self.image[self.index]
            self.width = image.get_width()
            self.height = image.get_height()
            self.main_scene.scene.blit(image, (self.x, self.y))
            self.ret += 1
    
    # 主场景
    class MainScene:
        running = True
        size = None
        scene = None
        bg = None
    
        clouds = []
        cloud_image = None
    
        items = []
        item_images = []
        item_ret= 1
        item_ret_num = 100
    
        bird_images = []
        birds = []
        bird_ret= 1
        bird_ret_num = 150
    
        dragon = None
        dragon_images = []
    
        gameover_image = None
        restart_image = None
        restart_x = None
        restart_y = None
        score = 0.0
    
        jump_sound = None
        gameover_sound = None
    
        # 初始化主场景
        def __init__(self):
            # 初始化 pygame，使用自定义字体必须用到
            pygame.init()
            # 场景尺寸
            self.size = (800, 350)
            # 场景对象
            self.scene = pygame.display.set_mode([self.size[0], self.size[1]])
            # 设置标题
            pygame.display.set_caption("恐龙跑酷")
            # 创建clock对象控制帧数
            self.timer = pygame.time.Clock()
    
            # 创建地图对象
            self.bg = GameBackground(self)
    
            # 创建云
            self.cloud_image = pygame.image.load("images/dragon/cloud.png")
            self.create_cloud()
    
            # 创建仙人掌
            for n in range(7):
                self.item_images.append(pygame.image.load("images/dragon/item_" + str(n+1) + ".png"))
    
            # 创建鸟
            self.bird_images.append(pygame.image.load("images/dragon/bird_1.png"))
            self.bird_images.append(pygame.image.load("images/dragon/bird_2.png"))
    
            # 创建恐龙
            for n in range(4):
                self.dragon_images.append(pygame.image.load("images/dragon/dragon_" + str(n+1) + ".png"))
    
            d_x = 50
            d_y = self.size[1] - self.dragon_images[0].get_height()
            self.dragon = Dragon(d_x, d_y, self.dragon_images, self)
    
            # gameover
            self.gameover_image = pygame.image.load("images/dragon/gameover.png")
            self.restart_image = pygame.image.load("images/dragon/restart.png")
    
            # 音效加载
            self.jump_sound = pygame.mixer.Sound("sounds/dragon/jump.wav")
            self.gameover_sound = pygame.mixer.Sound("sounds/dragon/gameover.wav")
    
        #  生成两朵云
        def create_cloud(self):
            self.clouds.append(Cloud(350, 30, self.cloud_image))
            self.clouds.append(Cloud(650, 100, self.cloud_image))
    
        # 绘制
        def draw_elements(self):
            if self.dragon.is_hit == 1:
                g_x = self.size[0] // 2 - self.gameover_image.get_width() // 2
                self.scene.blit(self.gameover_image, (g_x, 120))
    
                self.restart_x = self.size[0] // 2 - self.restart_image.get_width() // 2
                self.restart_y = 170
                self.scene.blit(self.restart_image, (self.restart_x, self.restart_y))
                return
    
            self.scene.fill((255, 255, 255)) # 填充背景色为白色
            self.bg.draw()                   # 绘制背景
    
            # 绘制云
            for c in self.clouds[:]:
                self.scene.blit(c.image, (c.x, c.y))
    
            # 绘制仙人掌
            for i in self.items[:]:
                self.scene.blit(i.image, (i.x, i.y))
    
            # 绘制鸟
            for b in self.birds[:]:
                b.draw()
    
            # 绘制恐龙
            self.dragon.draw()
    
            # 绘制跑动距离
            self.score += 0.1
            font = pygame.font.Font("freesansbold.ttf", 20)
            text = font.render(str(int(self.score)) + "m", True, (83, 83, 83))
            text_rect = text.get_rect()
            text_rect.right = self.size[0] - 10
            text_rect.top = 10
            self.scene.blit(text, text_rect)
    
        # 计算元素坐标及生成元素
        def action_elements(self):
            if self.dragon.is_hit == 1:
                return
    
            # 地图
            self.bg.action()
    
            # 云
            for c in self.clouds[:]:
                c.move()
    
                if c.x < - self.cloud_image.get_width():
                    self.clouds.remove(c)
    
            if len(self.clouds) == 0:
                self.create_cloud()
    
            # 仙人掌
            if self.item_ret % self.item_ret_num == 0:
                image = self.item_images[random.randint(0, len(self.item_images) - 1)]
                x = self.size[0]
                y = self.size[1] - image.get_height()
                self.items.append(Cactus(x, y, image))
            self.item_ret += 1
            if self.item_ret == self.item_ret_num:
                self.item_ret = 0
                self.item_ret_num = random.randint(60, 110)
    
            for i in self.items[:]:
                i.move()
    
                if i.x < -i.width:
                    self.items.remove(i)
    
            # 鸟
            if int(self.score) > 100:
                if self.bird_ret % self.bird_ret_num == 0:
                    x = self.size[0]
                    y = 210
                    self.birds.append(Bird(x, y, self.bird_images, self))
                self.bird_ret += 1
                if self.bird_ret == self.bird_ret_num:
                    self.bird_ret = 0
                    self.bird_ret_num = random.randint(150, 300)
    
                for b in self.birds[:]:
                    b.move()
    
                    if b.x < -b.width:
                        self.birds.remove(b)
    
            # 恐龙
            self.dragon.move()
    
        # 处理事件
        def handle_event(self):
            for event in pygame.event.get():
                # 检测松开键盘事件
                if event.type == pygame.KEYUP:
                    if event.key == K_DOWN:
                        if self.dragon.style == 1:
                            self.dragon.style = 0
                            self.dragon.y -= 34
    
                # 检测按下鼠标事件
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        if self.dragon.is_hit == 1:
                            pos = event.pos # 点击位置坐标
    
                            # 判断点击范围是否是重启图片上
                            x1 = self.restart_x
                            x2 = self.restart_x + self.restart_image.get_width()
    
                            y1 = self.restart_y
                            y2 = self.restart_y + self.restart_image.get_height()
    
                            if pos[0] >= x1 and pos[0] <= x2 and pos[1] >= y1 and pos[1] <= y2:
                                self.dragon.is_hit = 0
                                self.score = 0
                                self.items.clear()
                                self.birds.clear()
    
    
                # 检测到事件为退出时
                if event.type == pygame.QUIT:
                    self.running = False
    
        # 碰撞检测
        def detect_collision(self):
            if self.dragon.is_hit == 0:
                for i in self.items[:]:
                    if self.collision(self.dragon, i) or self.collision(i, self.dragon):
                        self.dragon.is_hit = 1
                        break
    
                for b in self.birds[:]:
                    if self.collision(self.dragon, b) or self.collision(b, self.dragon):
                        self.dragon.is_hit = 1
                        break
    
                if self.dragon.is_hit == 1:
                    self.gameover_sound.play()
    
        # 验证是否碰撞
        def collision(self, a, b):
            offset = 30 # 增加20误差，降低难度
            temp1 = (b.x + offset <= a.x + a.width <= b.x + offset + b.width)
            temp2 = (b.y + offset <= a.y + a.height <= b.y + offset + b.height)
            return temp1 and temp2
    
        # 处理按键
        def key_pressed(self):
            # 获取按下按键信息
            key_pressed = pygame.key.get_pressed()
    
            if key_pressed[K_DOWN]:
                if self.dragon.jump == 0:
                    if self.dragon.style == 0:
                        self.dragon.style = 1
                        self.dragon.y += 34
    
            if key_pressed[K_SPACE]:
                self.dragon.set_jump()
    
        # 处理帧数
        def set_fps(self):
            # 刷新显示
            pygame.display.update()
            # 设置帧率为60fps
            self.timer.tick(60)
    
        # 主循环,主要处理各种事件
        def run_scene(self):
    
            while self.running:
                # 计算元素坐标及生成元素
                self.action_elements()
                # 绘制元素图片
                self.draw_elements()
                # 处理事件
                self.handle_event()
                # 碰撞检测
                self.detect_collision()
                # 按键处理
                self.key_pressed()
                # 更新画布设置fps
                self.set_fps()
    
    # 创建主场景
    mainScene = MainScene()
    # 开始游戏
    mainScene.run_scene()

#命令行cmd
def cmds():
    class tk:
        from tkinter import Tk,Entry,Toplevel,Listbox
        from tkinter.scrolledtext import ScrolledText
    #设置信息，可选
    class terminal_infos:
        version='1.0'#版本
        by='Jeff'#作者
        running_space={'__name__':'__console__'}#运行空间(用于存储变量的)
        def print(*value):
            return None
        def input(*value):
            return None
        def set(*value):
            return None
        def Back(*value):
            pass
        del input,print,set,Back
        # exec('''    def print(*value):
        #     return None
        # def input(*value):
        #     return None
        # def set(*value):
        #     return None
        # def Back(*value):
        #     pass
        # del input,print,set,Back''',running_space)#先把那些Python基础函数替换了
        input_list=[]#这个是输入命令记载输入命令的列表
    class os:
        from os import getcwd,chdir,startfile,popen
        from os.path import isfile,isdir
    def run_command(command,terminal,commandinput):
        def contiune_command():
            terminal.insert('end','\n')
            terminal.insert('end',f'\n{os.getcwd()}\n','green')
            terminal.insert('end',f'$ ')
            terminal.window_create('end',window=commandinput)
            commandinput.focus_set()#"""
        errortext=f'这是一个错误的指令："{command.strip()}"。'
    
        command=str(command)#这玩意是应付编辑器不知道command是什么类型的
        terminal_infos.input_list.append(command)#增加输入了什么命令
        terminal.config(state='n')#解锁terminal(Text)
    
        terminal.delete('end')#删除输入控件
        commandinput.delete(0,'end')#删除控件里输入的文本
        if command.strip() == "1":
            print(1)
        if command.strip()=='':#如果啥也没输入
            terminal.insert('end',command)#就复述输入内容
        elif os.isfile(command.strip().replace('"','')) or os.isfile(os.getcwd()+command.strip().replace('"','')) or os.isfile(command.strip().replace('"','')+'.exe') or os.isfile(os.getcwd()+command.strip().replace('"','')+'.exe'):#如果是个文件
            try:
                os.startfile(command.strip().replace('"',''))
            except:
                try:
                    os.startfile(os.getcwd()+command.strip().replace('"',''))
                except:
                    try:
                        os.startfile(command.strip().replace('"','')+'.exe')
                    except:
                        os.startfile(os.getcwd()+command.strip().replace('"','')+'.exe')
            terminal.insert('end',command)
            contiune_command()
        elif len(command.strip())>=2:#当命令长度超过2时
            if command[0:2]=='::':
                terminal.insert('end',command)
                contiune_command()
            elif command[0:2]=='cd':
                #移动目录
                terminal.insert('end',command)
                try:
                    os.chdir(command.strip()[3:])
                except OSError as error:
                    terminal.insert('end','\n'+error.args[1]+'\n','red')
                except:
                    terminal.insert('end','\n移动至工作目录'+command.strip()[3:]+'失败。\n','red')
                contiune_command()
            elif len(command.strip())>=3:#当命令长度超过3时
                if command.lower().strip()[0:3]=='dir':
                    terminal.insert('end',command)
                    if command.lower().strip()=='dir':
                        try:
                            terminal.insert('end','\n\n'+os.popen('dir '+os.getcwd()).read())#返回执行dir命令的文本(Windows下)
                        except:
                            pass
                    elif len(command.lower().strip())>4:
                        if os.isdir(command.strip()[4:].replace('"','')) or os.isdir(os.getcwd()+command.strip()[4:].replace('"',''))==True:
                            terminal.insert('end','\n\n'+os.popen('dir '+command.strip()[4:]).read())
                    else:
                        terminal.insert('end','\n'+errortext)
                    contiune_command()
                elif command.lower().strip()[0:3]=='set':
                    #让用户设置变量的环节
                    terminal.delete('end')
                    if len(command.lower().strip())>3:
                        if '=' in command[4:]:
                            try:
                                def tovar(varname,varvalue):
                                    try:
                                        exec(varname+'='+varvalue,terminal_infos.running_space)
                                    except:
                                        terminal.insert('end','\n接收输入失败。','red')
                                    commandinput.bind('<Return>',lambda v=0:run_command(command_input.get(),TerminalText,command_input))
                                    command_input.bind('<Return>',lambda v=0:run_command(command_input.get(),TerminalText,command_input))
                                    contiune_command()
                                terminal.insert('end',command)
                                tovar(command[command.index(' ',0)+1:command.index('=',0)],command[command.index('=',0)+1:])
                            except:
                                terminal.insert('end','\n接收输入失败。','red')
                                contiune_command()
                        else:
                            terminal.insert('end',command)#每次都复述一遍
                            terminal.insert('end','\n没有等于号或等于号位置错误。','red')
                            contiune_command()
                    else:
                        terminal.insert('end',command)
                        terminal.insert('end','\n'+errortext,'red')
                        contiune_command()
                elif len(command.strip())>=4:
                    if command.lower().strip()[0:6]=='sysout':
                        terminal.insert('end',command)
                        if len(command.strip())>4:
                            try:
                                resultprint=eval('''['''+command[5:]+']',terminal_infos.running_space)
                            except NameError:
                                terminal.insert('end','\n变量不存在。','red')
                                resultprint=['']
                            except SyntaxError:
                                terminal.insert('end','\n语法错误，请使用","或"+"连接。','red')
                                resultprint=['']
                            except:
                                terminal.insert('end','\nERROR。','red')
                                resultprint=['']
                            try:
                                terminal.insert('end','\n')
                                for temp in resultprint:
                                    terminal.insert('end',temp)
                            except:
                                terminal.insert('end','输出了个寂寞。')
                        elif command.lower().strip()=='sysout':
                            terminal.insert('end',command)
                            pass
                        else:
                            terminal.insert('end',command)
                            terminal.insert('end','\n'+errortext)
                        contiune_command()
                    elif len(command.strip())>=5:
                        if command.lower().strip()[0:5]=='sysin':
                            #让用户输入文本
                            terminal.delete('end')
                            if len(command.lower().strip())>5:
                                if '=' in command[4:]:
                                    try:
                                        def tovar(varname,varvalue):
                                            try:
                                                exec(varname+'="'+varvalue.replace('"','\\"')+'"',terminal_infos.running_space)
                                            except:
                                                #from traceback import format_exc
                                                #terminal.insert('end','\n接收输入失败。\n%s'%format_exc(),'red')
                                                terminal.insert('end','\n接收输入失败。','red')
                                            commandinput.bind('<Return>',lambda v=0:run_command(command_input.get(),TerminalText,command_input))
                                            terminal['state']='n'
                                            terminal.insert('end',commandinput.get())
                                            commandinput.delete(0,'end')
                                            terminal.insert('end','\n')
                                            terminal.insert('end',f'\n')
                                            terminal.insert('end',f'{os.getcwd()}::','green')
                                            terminal.insert('end',f'\n')
                                            terminal.insert('end',f'$ ')
                                            terminal.window_create('end',window=commandinput)
                                            commandinput.focus_set()
                                            terminal.see('end')
                                            terminal['state']='d'
                                        terminal.insert('end',command)
                                        terminal.insert('end','\n%s\n'%(command[command.index('=',0)+1:]),'cyan')
                                        terminal.insert('end',f'$ ')
                                        terminal.window_create('end',window=commandinput)
                                        commandinput.bind("<Return>",lambda v=0:tovar(command[command.index(' ',0)+1:command.index('=',0)],commandinput.get()))
                                    except:
                                        terminal.insert('end','\n接收输入失败。','red')
                                        contiune_command()
                                else:
                                    terminal.insert('end',command)
                                    terminal.insert('end','\n没有等于号或等于号位置错误。','red')
                                    contiune_command()
                            elif command.lower().strip()=='input':
                                terminal.insert('end',command)
                                terminal.insert('end','\n')
                                contiune_command()
                            else:
                                terminal.insert('end',command)
                                terminal.insert('end','\n'+errortext,'red')
                                contiune_command()
                        else:
                            terminal.insert('end',command)
                            terminal.insert('end','\n'+errortext,'red')
                            contiune_command()
                    else:
                        terminal.insert('end',command)
                        terminal.insert('end','\n'+errortext,'red')
                        contiune_command()
                else:
                    terminal.insert('end',command)
                    terminal.insert('end','\n'+errortext,'red')
                    contiune_command()
            else:
                terminal.insert('end',command)
                terminal.insert('end','\n'+errortext,'red')
                contiune_command()
        else:
            terminal.insert('end',command)
            terminal.insert('end','\n'+errortext,'red')
            contiune_command()
    
        terminal.config(state='d')
        terminal.see('end')
    def post_inputlist(inputen):
        #弹出效果展示中的命令列表
        def setit(setmessage):
            inputen.delete(0,'end')
            inputen.insert('end',setmessage)
            postwin.destroy()
        postwin=tk.Toplevel(root,bg='#ffffff')
        icon_for_window(postwin,'')
        postwin.title('CommandList')
        postwin.geometry('300x200')
        postwin.transient(root)
    
        commandlist=tk.Listbox(postwin,fg='#800080',selectforeground='white',selectbackground='#800080',font=('terminal',16))
        #绑定确定命令的按键
        commandlist.bind('<Return>',lambda v=0:setit(commandlist.get(commandlist.curselection())))
        commandlist.bind('<Right>',lambda v=0:setit(commandlist.get(commandlist.curselection())))
        commandlist.bind('<Left>',lambda v=0:setit(commandlist.get(commandlist.curselection())))
        #让Listbox最大占据postwin的控件
        commandlist.pack(fill='both',expand=1)
    
        #给Listbox插入已经输入的内容
        for temp in terminal_infos.input_list:
            commandlist.insert('end',f'{temp}')
    
    #创建窗口
    root=tk.Tk()
    root.attributes('-alpha',0.8)
    #设置标题
    root.title(f'EasyTerminal {terminal_infos.version}')
    #设置图标(用这个方法是为了防止打包后找不到图标的)
    # icon_for_window(root,'')
    #设置默认大小
    root.geometry('645x400')
    #让窗口不可改变大小
    root.resizable(False,False)
    
    #新建Text控件
    TerminalText=tk.ScrolledText(root,state='d',fg='white',bg='black',insertbackground='white',font=('consolas',13),selectforeground='black',selectbackground='white',takefocus=False)
    TerminalText.pack(fill='both',expand='yes')
    
    #实现不同颜色的效果，用于insert插入标记
    TerminalText.tag_config('red',foreground='red',selectforeground='#00ffff',selectbackground='#ffffff')
    TerminalText.tag_config('green',foreground='green',selectforeground='#ff7eff',selectbackground='#ffffff')
    TerminalText.tag_config('blue',foreground='blue',selectforeground='#ffff7e',selectbackground='#ffffff')
    TerminalText.tag_config('cyan',foreground='cyan',selectforeground='red',selectbackground='#ffffff')
    
    TerminalText['state']='n'
    TerminalText.insert('end',f'EasyTerminal {terminal_infos.version} By {terminal_infos.by}\n')
    
    #后面的'green'就是tag标记，他会应用green这个tag的属性
    TerminalText.insert('end',f'{os.getcwd()}\n','green')
    TerminalText.insert('end',f'$ ')
    
    #命令输入框
    command_input=tk.Entry(TerminalText,font=('consolas',13),fg='white',bg='black',insertbackground='white',selectforeground='black',selectbackground='white',relief='flat',width=66)
    command_input.bind('<Return>',lambda v=0:run_command(command_input.get(),TerminalText,command_input))
    #在命令输入框中按F7弹出命令列表窗口
    command_input.bind('<F7>',lambda v=0:post_inputlist(command_input))
    
    #插入命令输入框
    TerminalText.window_create('end',window=command_input)
    
    #让终端Text不可编辑
    TerminalText['state']='d'
    
    #循环窗口
    root.mainloop()

#我的世界
import sys
import math
import random
import time

from collections import deque
from pyglet import image
from pyglet.gl import *
from pyglet.graphics import TextureGroup
from pyglet.window import key, mouse

import random as rand 
import math
def mink():
    class NoiseParameters:
        def __init__(self, octaves, amplitude, smoothness, roughness, heightOffset):
            self.octaves = octaves
            self.amplitude = amplitude
            self.smoothness = smoothness
            self.roughness = roughness
            self.heightOffset = heightOffset
    
    class NoiseGen:
        def __init__(self, seed):
            self.seed = seed
            self.noiseParams = NoiseParameters(
                7, 50, 450, 0.3, 20
            )
    
        def _getNoise2(self, n):
            n += self.seed 
            n = (int(n) << 13) ^ int(n)
            newn = (n * (n * n * 60493 + 19990303) + 1376312589) & 0x7fffffff
            return 1.0 - (float(newn) / 1073741824.0)
    
        def _getNoise(self, x, z):
            return self._getNoise2(x + z * 57)
    
        def _lerp(self, a, b, z):
            mu2 = (1.0 - math.cos(z * 3.14)) / 2.0
            return (a * (1 - mu2) + b * mu2)
    
        def _noise(self, x, z):
            floorX = float(int(x))
            floorZ = float(int(z))
    
            s = 0.0,
            t = 0.0,
            u = 0.0,
            v = 0.0;#Integer declaration
    
            s = self._getNoise(floorX,      floorZ)
            t = self._getNoise(floorX + 1,  floorZ)
            u = self._getNoise(floorX,      floorZ + 1)
            v = self._getNoise(floorX + 1,  floorZ + 1)
    
            rec1 = self._lerp(s, t, x - floorX)
            rec2 = self._lerp(u, v, x - floorX)
            rec3 = self._lerp(rec1, rec2, z - floorZ)
            return rec3
    
        def getHeight(self, x, z):
            totalValue = 0.0
    
            for a in range(self.noiseParams.octaves - 1):
                freq = math.pow(2.0, a)
                amp  = math.pow(self.noiseParams.roughness, a)
                totalValue += self._noise(
                    (float(x)) * freq / self.noiseParams.smoothness,
                    (float(z)) * freq / self.noiseParams.smoothness
                ) * self.noiseParams.amplitude
    
            result = (((totalValue / 2.1) + 1.2) * self.noiseParams.amplitude) + self.noiseParams.heightOffset
    
            return (totalValue / 5) + self.noiseParams.heightOffset
    
    
    TICKS_PER_SEC = 60
    
    # Size of sectors used to ease block loading.
    SECTOR_SIZE = 16
    
    # Movement variables
    WALKING_SPEED = 5
    FLYING_SPEED = 15
    CROUCH_SPEED = 2
    SPRINT_SPEED = 7
    SPRINT_FOV = SPRINT_SPEED / 2
    
    GRAVITY = 20.0
    MAX_JUMP_HEIGHT = 1.0 # About the height of a block.
    # To derive the formula for calculating jump speed, first solve
    #    v_t = v_0 + a * t
    # for the time at which you achieve maximum height, where a is the acceleration
    # due to gravity and v_t = 0. This gives:
    #    t = - v_0 / a
    # Use t and the desired MAX_JUMP_HEIGHT to solve for v_0 (jump speed) in
    #    s = s_0 + v_0 * t + (a * t^2) / 2
    JUMP_SPEED = math.sqrt(2 * GRAVITY * MAX_JUMP_HEIGHT)
    TERMINAL_VELOCITY = 50
    
    # Player variables
    PLAYER_HEIGHT = 2
    PLAYER_FOV = 80.0
    
    if sys.version_info[0] >= 3:
        xrange = range
    
    def cube_vertices(x, y, z, n):
        """ Return the vertices of the cube at position x, y, z with size 2*n.
    
        """
        return [
            x-n,y+n,z-n, x-n,y+n,z+n, x+n,y+n,z+n, x+n,y+n,z-n,  # top
            x-n,y-n,z-n, x+n,y-n,z-n, x+n,y-n,z+n, x-n,y-n,z+n,  # bottom
            x-n,y-n,z-n, x-n,y-n,z+n, x-n,y+n,z+n, x-n,y+n,z-n,  # left
            x+n,y-n,z+n, x+n,y-n,z-n, x+n,y+n,z-n, x+n,y+n,z+n,  # right
            x-n,y-n,z+n, x+n,y-n,z+n, x+n,y+n,z+n, x-n,y+n,z+n,  # front
            x+n,y-n,z-n, x-n,y-n,z-n, x-n,y+n,z-n, x+n,y+n,z-n,  # back
        ]
    
    
    def tex_coord(x, y, n=4):
        """ Return the bounding vertices of the texture square.
    
        """
        m = 1.0 / n
        dx = x * m
        dy = y * m
        return dx, dy, dx + m, dy, dx + m, dy + m, dx, dy + m
    
    
    def tex_coords(top, bottom, side):
        """ Return a list of the texture squares for the top, bottom and side.
    
        """
        top = tex_coord(*top)
        bottom = tex_coord(*bottom)
        side = tex_coord(*side)
        result = []
        result.extend(top)
        result.extend(bottom)
        result.extend(side * 4)
        return result
    
    
    TEXTURE_PATH = 'texture.png'
    
    GRASS = tex_coords((1, 0), (0, 1), (0, 0))
    SAND = tex_coords((1, 1), (1, 1), (1, 1))
    BRICK = tex_coords((2, 0), (2, 0), (2, 0))
    STONE = tex_coords((2, 1), (2, 1), (2, 1))
    WOOD = tex_coords((3, 1), (3, 1), (3, 1))
    LEAF = tex_coords((3, 0), (3, 0), (3, 0))
    WATER = tex_coords((0, 2), (0, 2), (0, 2))
    
    FACES = [
        ( 0, 1, 0),
        ( 0,-1, 0),
        (-1, 0, 0),
        ( 1, 0, 0),
        ( 0, 0, 1),
        ( 0, 0,-1),
    ]
    
    
    def normalize(position):
        """ Accepts `position` of arbitrary precision and returns the block
        containing that position.
    
        Parameters
        ----------
        position : tuple of len 3
    
        Returns
        -------
        block_position : tuple of ints of len 3
    
        """
        x, y, z = position
        x, y, z = (int(round(x)), int(round(y)), int(round(z)))
        return (x, y, z)
    
    
    def sectorize(position):
        """ Returns a tuple representing the sector for the given `position`.
    
        Parameters
        ----------
        position : tuple of len 3
    
        Returns
        -------
        sector : tuple of len 3
    
        """
        x, y, z = normalize(position)
        x, y, z = x // SECTOR_SIZE, y // SECTOR_SIZE, z // SECTOR_SIZE
        return (x, 0, z)
    
    
    class Model(object):
    
        def __init__(self):
    
            # A Batch is a collection of vertex lists for batched rendering.
            self.batch = pyglet.graphics.Batch()
    
            # A TextureGroup manages an OpenGL texture.
            self.group = TextureGroup(image.load(TEXTURE_PATH).get_texture())
    
            # A mapping from position to the texture of the block at that position.
            # This defines all the blocks that are currently in the world.
            self.world = {}
    
            # Same mapping as `world` but only contains blocks that are shown.
            self.shown = {}
    
            # Mapping from position to a pyglet `VertextList` for all shown blocks.
            self._shown = {}
    
            # Mapping from sector to a list of positions inside that sector.
            self.sectors = {}
    
            # Simple function queue implementation. The queue is populated with
            # _show_block() and _hide_block() calls
            self.queue = deque()
    
            self._initialize()
    
        def _initialize(self):
            """ Initialize the world by placing all the blocks.
    
            """
            gen = NoiseGen(452692)
    
            n = 128 #size of the world
            s = 1  # step size
            y = 0  # initial y height
            
            #too lazy to do this properly lol
            heightMap = []
            for x in xrange(0, n, s):
                for z in xrange(0, n, s):
                    heightMap.append(0)
            for x in xrange(0, n, s):
                for z in xrange(0, n, s):
                    heightMap[z + x * n] = int(gen.getHeight(x, z))
    
            #Generate the world
            for x in xrange(0, n, s):
                for z in xrange(0, n, s):
                    h = heightMap[z + x * n]
                    if (h < 15):
                        self.add_block((x, h, z), SAND, immediate=False)
                        for y in range (h, 15):
                            self.add_block((x, y, z), WATER, immediate=False)
                        continue
                    if (h < 18):
                        self.add_block((x, h, z), SAND, immediate=False)
                    self.add_block((x, h, z), GRASS, immediate=False)
                    for y in xrange(h - 1, 0, -1):
                        self.add_block((x, y, z), STONE, immediate=False)
                    #Maybe add tree at this (x, z)
                    if (h > 20):
                        if random.randrange(0, 1000) > 990:
                            treeHeight = random.randrange(5, 7)
                            #Tree trunk
                            for y in xrange(h + 1, h + treeHeight):
                                self.add_block((x, y, z), WOOD, immediate=False)
                            #Tree leaves
                            leafh = h + treeHeight
                            for lz in xrange(z + -2, z + 3):
                                for lx in xrange(x + -2, x + 3): 
                                    for ly in xrange(3):
                                        self.add_block((lx, leafh + ly, lz), LEAF, immediate=False)
    
        def hit_test(self, position, vector, max_distance=8):
            """ Line of sight search from current position. If a block is
            intersected it is returned, along with the block previously in the line
            of sight. If no block is found, return None, None.
    
            Parameters
            ----------
            position : tuple of len 3
                The (x, y, z) position to check visibility from.
            vector : tuple of len 3
                The line of sight vector.
            max_distance : int
                How many blocks away to search for a hit.
    
            """
            m = 8
            x, y, z = position
            dx, dy, dz = vector
            previous = None
            for _ in xrange(max_distance * m):
                key = normalize((x, y, z))
                if key != previous and key in self.world:
                    return key, previous
                previous = key
                x, y, z = x + dx / m, y + dy / m, z + dz / m
            return None, None
    
        def exposed(self, position):
            """ Returns False is given `position` is surrounded on all 6 sides by
            blocks, True otherwise.
    
            """
            x, y, z = position
            for dx, dy, dz in FACES:
                if (x + dx, y + dy, z + dz) not in self.world:
                    return True
            return False
    
        def add_block(self, position, texture, immediate=True):
            """ Add a block with the given `texture` and `position` to the world.
    
            Parameters
            ----------
            position : tuple of len 3
                The (x, y, z) position of the block to add.
            texture : list of len 3
                The coordinates of the texture squares. Use `tex_coords()` to
                generate.
            immediate : bool
                Whether or not to draw the block immediately.
    
            """
            if position in self.world:
                self.remove_block(position, immediate)
            self.world[position] = texture
            self.sectors.setdefault(sectorize(position), []).append(position)
            if immediate:
                if self.exposed(position):
                    self.show_block(position)
                self.check_neighbors(position)
    
        def remove_block(self, position, immediate=True):
            """ Remove the block at the given `position`.
    
            Parameters
            ----------
            position : tuple of len 3
                The (x, y, z) position of the block to remove.
            immediate : bool
                Whether or not to immediately remove block from canvas.
    
            """
            del self.world[position]
            self.sectors[sectorize(position)].remove(position)
            if immediate:
                if position in self.shown:
                    self.hide_block(position)
                self.check_neighbors(position)
    
        def check_neighbors(self, position):
            """ Check all blocks surrounding `position` and ensure their visual
            state is current. This means hiding blocks that are not exposed and
            ensuring that all exposed blocks are shown. Usually used after a block
            is added or removed.
    
            """
            x, y, z = position
            for dx, dy, dz in FACES:
                key = (x + dx, y + dy, z + dz)
                if key not in self.world:
                    continue
                if self.exposed(key):
                    if key not in self.shown:
                        self.show_block(key)
                else:
                    if key in self.shown:
                        self.hide_block(key)
    
        def show_block(self, position, immediate=True):
            """ Show the block at the given `position`. This method assumes the
            block has already been added with add_block()
    
            Parameters
            ----------
            position : tuple of len 3
                The (x, y, z) position of the block to show.
            immediate : bool
                Whether or not to show the block immediately.
    
            """
            texture = self.world[position]
            self.shown[position] = texture
            if immediate:
                self._show_block(position, texture)
            else:
                self._enqueue(self._show_block, position, texture)
    
        def _show_block(self, position, texture):
            """ Private implementation of the `show_block()` method.
    
            Parameters
            ----------
            position : tuple of len 3
                The (x, y, z) position of the block to show.
            texture : list of len 3
                The coordinates of the texture squares. Use `tex_coords()` to
                generate.
    
            """
            x, y, z = position
            vertex_data = cube_vertices(x, y, z, 0.5)
            texture_data = list(texture)
            # create vertex list
            # FIXME Maybe `add_indexed()` should be used instead
            self._shown[position] = self.batch.add(24, GL_QUADS, self.group,
                ('v3f/static', vertex_data),
                ('t2f/static', texture_data))
    
        def hide_block(self, position, immediate=True):
            """ Hide the block at the given `position`. Hiding does not remove the
            block from the world.
    
            Parameters
            ----------
            position : tuple of len 3
                The (x, y, z) position of the block to hide.
            immediate : bool
                Whether or not to immediately remove the block from the canvas.
    
            """
            self.shown.pop(position)
            if immediate:
                self._hide_block(position)
            else:
                self._enqueue(self._hide_block, position)
    
        def _hide_block(self, position):
            """ Private implementation of the 'hide_block()` method.
    
            """
            self._shown.pop(position).delete()
    
        def show_sector(self, sector):
            """ Ensure all blocks in the given sector that should be shown are
            drawn to the canvas.
    
            """
            for position in self.sectors.get(sector, []):
                if position not in self.shown and self.exposed(position):
                    self.show_block(position, False)
    
        def hide_sector(self, sector):
            """ Ensure all blocks in the given sector that should be hidden are
            removed from the canvas.
    
            """
            for position in self.sectors.get(sector, []):
                if position in self.shown:
                    self.hide_block(position, False)
    
        def change_sectors(self, before, after):
            """ Move from sector `before` to sector `after`. A sector is a
            contiguous x, y sub-region of world. Sectors are used to speed up
            world rendering.
    
            """
            before_set = set()
            after_set = set()
            pad = 4
            for dx in xrange(-pad, pad + 1):
                for dy in [0]:  # xrange(-pad, pad + 1):
                    for dz in xrange(-pad, pad + 1):
                        if dx ** 2 + dy ** 2 + dz ** 2 > (pad + 1) ** 2:
                            continue
                        if before:
                            x, y, z = before
                            before_set.add((x + dx, y + dy, z + dz))
                        if after:
                            x, y, z = after
                            after_set.add((x + dx, y + dy, z + dz))
            show = after_set - before_set
            hide = before_set - after_set
            for sector in show:
                self.show_sector(sector)
            for sector in hide:
                self.hide_sector(sector)
    
        def _enqueue(self, func, *args):
            """ Add `func` to the internal queue.
    
            """
            self.queue.append((func, args))
    
        def _dequeue(self):
            """ Pop the top function from the internal queue and call it.
    
            """
            func, args = self.queue.popleft()
            func(*args)
    
        def process_queue(self):
            """ Process the entire queue while taking periodic breaks. This allows
            the game loop to run smoothly. The queue contains calls to
            _show_block() and _hide_block() so this method should be called if
            add_block() or remove_block() was called with immediate=False
    
            """
            start = time.process_time()
            while self.queue and time.process_time() - start < 1.0 / TICKS_PER_SEC:
                self._dequeue()
    
        def process_entire_queue(self):
            """ Process the entire queue with no breaks.
    
            """
            while self.queue:
                self._dequeue()
    
    
    class Window(pyglet.window.Window):
    
        def __init__(self, *args, **kwargs):
            super(Window, self).__init__(*args, **kwargs)
    
            # Whether or not the window exclusively captures the mouse.
            self.exclusive = False
    
            # When flying gravity has no effect and speed is increased.
            self.flying = False
    
            # Used for constant jumping. If the space bar is held down,
            # this is true, otherwise, it's false
            self.jumping = False
    
            # If the player actually jumped, this is true
            self.jumped = False
    
            # If this is true, a crouch offset is added to the final glTranslate
            self.crouch = False
    
            # Player sprint
            self.sprinting = False
    
            # This is an offset value so stuff like speed potions can also be easily added
            self.fov_offset = 0
    
            self.collision_types = {"top": False, "bottom": False, "right": False, "left": False}
    
            # Strafing is moving lateral to the direction you are facing,
            # e.g. moving to the left or right while continuing to face forward.
            #
            # First element is -1 when moving forward, 1 when moving back, and 0
            # otherwise. The second element is -1 when moving left, 1 when moving
            # right, and 0 otherwise.
            self.strafe = [0, 0]
    
            # Current (x, y, z) position in the world, specified with floats. Note
            # that, perhaps unlike in math class, the y-axis is the vertical axis.
            self.position = (30, 50, 80)
    
            # First element is rotation of the player in the x-z plane (ground
            # plane) measured from the z-axis down. The second is the rotation
            # angle from the ground plane up. Rotation is in degrees.
            #
            # The vertical plane rotation ranges from -90 (looking straight down) to
            # 90 (looking straight up). The horizontal rotation range is unbounded.
            self.rotation = (0, 0)
    
            # Which sector the player is currently in.
            self.sector = None
    
            # The crosshairs at the center of the screen.
            self.reticle = None
    
            # Velocity in the y (upward) direction.
            self.dy = 0
    
            # A list of blocks the player can place. Hit num keys to cycle.
            self.inventory = [BRICK, GRASS, SAND, WOOD, LEAF]
    
            # The current block the user can place. Hit num keys to cycle.
            self.block = self.inventory[0]
    
            # Convenience list of num keys.
            self.num_keys = [
                key._1, key._2, key._3, key._4, key._5,
                key._6, key._7, key._8, key._9, key._0]
    
            # Instance of the model that handles the world.
            self.model = Model()
    
            # The label that is displayed in the top left of the canvas.
            self.label = pyglet.text.Label('', font_name='Arial', font_size=18,
                x=10, y=self.height - 10, anchor_x='left', anchor_y='top',
                color=(0, 0, 0, 255))
    
            # This call schedules the `update()` method to be called
            # TICKS_PER_SEC. This is the main game event loop.
            pyglet.clock.schedule_interval(self.update, 1.0 / TICKS_PER_SEC)
    
        def set_exclusive_mouse(self, exclusive):
            """ If `exclusive` is True, the game will capture the mouse, if False
            the game will ignore the mouse.
    
            """
            super(Window, self).set_exclusive_mouse(exclusive)
            self.exclusive = exclusive
    
        def get_sight_vector(self):
            """ Returns the current line of sight vector indicating the direction
            the player is looking.
    
            """
            x, y = self.rotation
            # y ranges from -90 to 90, or -pi/2 to pi/2, so m ranges from 0 to 1 and
            # is 1 when looking ahead parallel to the ground and 0 when looking
            # straight up or down.
            m = math.cos(math.radians(y))
            # dy ranges from -1 to 1 and is -1 when looking straight down and 1 when
            # looking straight up.
            dy = math.sin(math.radians(y))
            dx = math.cos(math.radians(x - 90)) * m
            dz = math.sin(math.radians(x - 90)) * m
            return (dx, dy, dz)
    
        def get_motion_vector(self):
            """ Returns the current motion vector indicating the velocity of the
            player.
    
            Returns
            -------
            vector : tuple of len 3
                Tuple containing the velocity in x, y, and z respectively.
    
            """
            if any(self.strafe):
                x, y = self.rotation
                strafe = math.degrees(math.atan2(*self.strafe))
                y_angle = math.radians(y)
                x_angle = math.radians(x + strafe)
                if self.flying:
                    m = math.cos(y_angle)
                    dy = math.sin(y_angle)
                    if self.strafe[1]:
                        # Moving left or right.
                        dy = 0.0
                        m = 1
                    if self.strafe[0] > 0:
                        # Moving backwards.
                        dy *= -1
                    # When you are flying up or down, you have less left and right
                    # motion.
                    dx = math.cos(x_angle) * m
                    dz = math.sin(x_angle) * m
                else:
                    dy = 0.0
                    dx = math.cos(x_angle)
                    dz = math.sin(x_angle)
            else:
                dy = 0.0
                dx = 0.0
                dz = 0.0
            return (dx, dy, dz)
    
        def update(self, dt):
            """ This method is scheduled to be called repeatedly by the pyglet
            clock.
    
            Parameters
            ----------
            dt : float
                The change in time since the last call.
    
            """
            self.model.process_queue()
            sector = sectorize(self.position)
            if sector != self.sector:
                self.model.change_sectors(self.sector, sector)
                if self.sector is None:
                    self.model.process_entire_queue()
                self.sector = sector
            m = 8
            dt = min(dt, 0.2)
            for _ in xrange(m):
                self._update(dt / m)
    
        def _update(self, dt):
            """ Private implementation of the `update()` method. This is where most
            of the motion logic lives, along with gravity and collision detection.
    
            Parameters
            ----------
            dt : float
                The change in time since the last call.
    
            """
            # walking
            if self.flying:
                speed = FLYING_SPEED
            elif self.sprinting:
                speed = SPRINT_SPEED
            elif self.crouch:
                speed = CROUCH_SPEED
            else:
                speed = WALKING_SPEED
    
            if self.jumping:
                if self.collision_types["top"]:
                    self.dy = JUMP_SPEED
                    self.jumped = True
            else:
                if self.collision_types["top"]:
                    self.jumped = False
            if self.jumped:
                speed += 0.7
    
            d = dt * speed # distance covered this tick.
            dx, dy, dz = self.get_motion_vector()
            # New position in space, before accounting for gravity.
            dx, dy, dz = dx * d, dy * d, dz * d
            # gravity
            if not self.flying:
                # Update your vertical speed: if you are falling, speed up until you
                # hit terminal velocity; if you are jumping, slow down until you
                # start falling.
                self.dy -= dt * GRAVITY
                self.dy = max(self.dy, -TERMINAL_VELOCITY)
                dy += self.dy * dt
            # collisions
            old_pos = self.position
            x, y, z = old_pos
            x, y, z = self.collide((x + dx, y + dy, z + dz), PLAYER_HEIGHT)
            self.position = (x, y, z)
    
            # Sptinting stuff. If the player stops moving in the x and z direction, the player stops sprinting
            # and the sprint fov is subtracted from the fov offset
            if old_pos[0]-self.position[0] == 0 and old_pos[2]-self.position[2] == 0:
                disablefov = False
                if self.sprinting:
                    disablefov = True
                self.sprinting = False
                if disablefov:
                    self.fov_offset -= SPRINT_FOV
    
        def collide(self, position, height):
            """ Checks to see if the player at the given `position` and `height`
            is colliding with any blocks in the world.
    
            Parameters
            ----------
            position : tuple of len 3
                The (x, y, z) position to check for collisions at.
            height : int or float
                The height of the player.
    
            Returns
            -------
            position : tuple of len 3
                The new position of the player taking into account collisions.
    
            """
            # How much overlap with a dimension of a surrounding block you need to
            # have to count as a collision. If 0, touching terrain at all counts as
            # a collision. If .49, you sink into the ground, as if walking through
            # tall grass. If >= .5, you'll fall through the ground.
            pad = 0.25
            p = list(position)
            np = normalize(position)
            self.collision_types = {"top":False,"bottom":False,"right":False,"left":False}
            for face in FACES:  # check all surrounding blocks
                for i in xrange(3):  # check each dimension independently
                    if not face[i]:
                        continue
                    # How much overlap you have with this dimension.
                    d = (p[i] - np[i]) * face[i]
                    if d < pad:
                        continue
                    for dy in xrange(height):  # check each height
                        op = list(np)
                        op[1] -= dy
                        op[i] += face[i]
                        if tuple(op) not in self.model.world:
                            continue
                        p[i] -= (d - pad) * face[i]
                        # If you are colliding with the ground or ceiling, stop
                        # falling / rising.
                        if face == (0, -1, 0):
                            self.collision_types["top"] = True
                            self.dy = 0
                        if face == (0, 1, 0):
                            self.collision_types["bottom"] = True
                            self.dy = 0
                        break
            return tuple(p)
    
        def on_mouse_press(self, x, y, button, modifiers):
            """ Called when a mouse button is pressed. See pyglet docs for button
            amd modifier mappings.
    
            Parameters
            ----------
            x, y : int
                The coordinates of the mouse click. Always center of the screen if
                the mouse is captured.
            button : int
                Number representing mouse button that was clicked. 1 = left button,
                4 = right button.
            modifiers : int
                Number representing any modifying keys that were pressed when the
                mouse button was clicked.
    
            """
            if self.exclusive:
                vector = self.get_sight_vector()
                block, previous = self.model.hit_test(self.position, vector)
                if (button == mouse.RIGHT) or \
                        ((button == mouse.LEFT) and (modifiers & key.MOD_CTRL)):
                    # ON OSX, control + left click = right click.
                    if previous:
                        self.model.add_block(previous, self.block)
                elif button == pyglet.window.mouse.LEFT and block:
                    texture = self.model.world[block]
                    if texture != STONE:
                        self.model.remove_block(block)
            else:
                self.set_exclusive_mouse(True)
    
        def on_mouse_motion(self, x, y, dx, dy):
            """ Called when the player moves the mouse.
    
            Parameters
            ----------
            x, y : int
                The coordinates of the mouse click. Always center of the screen if
                the mouse is captured.
            dx, dy : float
                The movement of the mouse.
    
            """
            if self.exclusive:
                m = 0.15
                x, y = self.rotation
                x, y = x + dx * m, y + dy * m
                y = max(-90, min(90, y))
                self.rotation = (x, y)
    
        def on_key_press(self, symbol, modifiers):
            """ Called when the player presses a key. See pyglet docs for key
            mappings.
    
            Parameters
            ----------
            symbol : int
                Number representing the key that was pressed.
            modifiers : int
                Number representing any modifying keys that were pressed.
    
            """
            if symbol == key.W:
                self.strafe[0] -= 1
            elif symbol == key.S:
                self.strafe[0] += 1
            elif symbol == key.A:
                self.strafe[1] -= 1
            elif symbol == key.D:
                self.strafe[1] += 1
            elif symbol == key.C:
                self.fov_offset -= 60.0
            elif symbol == key.SPACE:
                self.jumping = True
            elif symbol == key.ESCAPE:
                self.set_exclusive_mouse(False)
            elif symbol == key.LSHIFT:
                self.crouch = True
                if self.sprinting:
                    self.fov_offset -= SPRINT_FOV
                    self.sprinting = False
            elif symbol == key.R:
                if not self.crouch:
                    if not self.sprinting:
                        self.fov_offset += SPRINT_FOV
                    self.sprinting = True
            elif symbol == key.TAB:
                self.flying = not self.flying
            elif symbol in self.num_keys:
                index = (symbol - self.num_keys[0]) % len(self.inventory)
                self.block = self.inventory[index]
    
        def on_key_release(self, symbol, modifiers):
            """ Called when the player releases a key. See pyglet docs for key
            mappings.
    
            Parameters
            ----------
            symbol : int
                Number representing the key that was pressed.
            modifiers : int
                Number representing any modifying keys that were pressed.
    
            """
            if symbol == key.W:
                self.strafe[0] += 1
            elif symbol == key.S:
                self.strafe[0] -= 1
            elif symbol == key.A:
                self.strafe[1] += 1
            elif symbol == key.D:
                self.strafe[1] -= 1
            elif symbol == key.SPACE:
                self.jumping = False
            elif symbol == key.LSHIFT:
                self.crouch = False
            elif symbol == key.C:
                self.fov_offset += 60.0
    
        def on_resize(self, width, height):
            """ Called when the window is resized to a new `width` and `height`.
    
            """
            # label
            self.label.y = height - 10
            # reticle
            if self.reticle:
                self.reticle.delete()
            x, y = self.width // 2, self.height // 2
            n = 10
            self.reticle = pyglet.graphics.vertex_list(4,
                ('v2i', (x - n, y, x + n, y, x, y - n, x, y + n))
            )
    
        def set_2d(self):
            """ Configure OpenGL to draw in 2d.
    
            """
            width, height = self.get_size()
            glDisable(GL_DEPTH_TEST)
            viewport = self.get_viewport_size()
            glViewport(0, 0, max(1, viewport[0]), max(1, viewport[1]))
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            glOrtho(0, max(1, width), 0, max(1, height), -1, 1)
            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()
    
        def set_3d(self):
            """ Configure OpenGL to draw in 3d.
    
            """
            width, height = self.get_size()
            glEnable(GL_DEPTH_TEST)
            viewport = self.get_viewport_size()
            glViewport(0, 0, max(1, viewport[0]), max(1, viewport[1]))
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            gluPerspective(PLAYER_FOV + self.fov_offset, width / float(height), 0.1, 60.0)
            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()
            x, y = self.rotation
            glRotatef(x, 0, 1, 0)
            glRotatef(-y, math.cos(math.radians(x)), 0, math.sin(math.radians(x)))
            x, y, z = self.position
            if self.crouch:
                glTranslatef(-x, -y+0.2, -z)
            else:
                glTranslatef(-x, -y, -z)
    
        def on_draw(self):
            """ Called by pyglet to draw the canvas.
    
            """
            self.clear()
            self.set_3d()
            glColor3d(1, 1, 1)
            self.model.batch.draw()
            self.draw_focused_block()
            self.set_2d()
            self.draw_label()
            self.draw_reticle()
    
        def draw_focused_block(self):
            """ Draw black edges around the block that is currently under the
            crosshairs.
    
            """
            vector = self.get_sight_vector()
            block = self.model.hit_test(self.position, vector)[0]
            if block:
                x, y, z = block
                vertex_data = cube_vertices(x, y, z, 0.51)
                glColor3d(0, 0, 0)
                glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
                pyglet.graphics.draw(24, GL_QUADS, ('v3f/static', vertex_data))
                glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    
        def draw_label(self):
            """ Draw the label in the top left of the screen.
    
            """
            x, y, z = self.position
            self.label.text = '%02d (%.2f, %.2f, %.2f) %d / %d' % (
                pyglet.clock.get_fps(), x, y, z,
                len(self.model._shown), len(self.model.world))
            self.label.draw()
    
        def draw_reticle(self):
            """ Draw the crosshairs in the center of the screen.
    
            """
            glColor3d(0, 0, 0)
            self.reticle.draw(GL_LINES)
    
    
    def setup_fog():
        """ Configure the OpenGL fog properties.
    
        """
        # Enable fog. Fog "blends a fog color with each rasterized pixel fragment's
        # post-texturing color."
        glEnable(GL_FOG)
        # Set the fog color.
        glFogfv(GL_FOG_COLOR, (GLfloat * 4)(0.5, 0.69, 1.0, 1))
        # Say we have no preference between rendering speed and quality.
        glHint(GL_FOG_HINT, GL_DONT_CARE)
        # Specify the equation used to compute the blending factor.
        glFogi(GL_FOG_MODE, GL_LINEAR)
        # How close and far away fog starts and ends. The closer the start and end,
        # the denser the fog in the fog range.
        glFogf(GL_FOG_START, 40.0)
        glFogf(GL_FOG_END, 60.0)
    
    
    def setup():
        """ Basic OpenGL configuration.
    
        """
        # Set the color of "clear", i.e. the sky, in rgba.
        glClearColor(0.5, 0.69, 1.0, 1)
        # Enable culling (not rendering) of back-facing facets -- facets that aren't
        # visible to you.
        glEnable(GL_CULL_FACE)
        # Set the texture minification/magnification function to GL_NEAREST (nearest
        # in Manhattan distance) to the specified texture coordinates. GL_NEAREST
        # "is generally faster than GL_LINEAR, but it can produce textured images
        # with sharper edges because the transition between texture elements is not
        # as smooth."
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        setup_fog()
    
    
    def main():
        window = Window(width=1280, height=720, caption='Minecraft', resizable=True)
        # Hide the mouse cursor and prevent the mouse from leaving the window.
        window.set_exclusive_mouse(True)
        setup()
        pyglet.app.run()
    
    main()

#飞机大战
from Cython import *
import wx
def feiji():

    SCREEN_WIDTH = 480
    SCREEN_HEIGHT = 800
    
    class Bullet(pygame.sprite.Sprite):
        def __init__(self, bullet_img, init_pos):
            pygame.sprite.Sprite.__init__(self)
            self.image = bullet_img
            self.rect = self.image.get_rect()
            self.rect.midbottom = init_pos
            self.speed = 10
    
        def move(self):
            self.rect.top -= self.speed
    
    class Player(pygame.sprite.Sprite):
        def __init__(self, plane_img, player_rect, init_pos):
            pygame.sprite.Sprite.__init__(self)
            self.image = []                               
            for i in range(len(player_rect)):
                self.image.append(plane_img.subsurface(player_rect[i]).convert_alpha())
            self.rect = player_rect[0]                
            self.rect.topleft = init_pos             
            self.speed = 8                               
            self.bullets = pygame.sprite.Group()       
            self.is_hit = False                            
    
        def moveDown(self):
            if self.rect.top >= SCREEN_HEIGHT - self.rect.height:
                self.rect.top = SCREEN_HEIGHT - self.rect.height
            else:
                self.rect.top += self.speed
    
        def moveLeft(self):
            if self.rect.left <= 0:
                self.rect.left = 0
            else:
                self.rect.left -= self.speed
        def shoot(self, bullet_img):
            bullet = Bullet(bullet_img, self.rect.midtop)
            self.bullets.add(bullet)
    
        def moveUp(self):
            if self.rect.top <= 0:
                self.rect.top = 0
            else:
                self.rect.top -= self.speed
    
         
        def moveRight(self):
            if self.rect.left >= SCREEN_WIDTH - self.rect.width:
                self.rect.left = SCREEN_WIDTH - self.rect.width
            else:
                self.rect.left += self.speed
    
    class Enemy(pygame.sprite.Sprite):
        def __init__(self, enemy_img, enemy_down_imgs, init_pos):
           pygame.sprite.Sprite.__init__(self)
           self.image = enemy_img
           self.rect = self.image.get_rect()
           self.rect.topleft = init_pos
           self.down_imgs = enemy_down_imgs
           self.speed = 2
    
        def move(self):
            self.rect.top += self.speed
    
    
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    
    pygame.display.set_caption('飞机大战')
    background = pygame.image.load('background.png').convert()
    game_over = pygame.image.load('gameover.png')
    plane_img = pygame.image.load('shoot.png')
    player_rect = []
    player_rect.append(pygame.Rect(0, 99, 102, 126))      
    player_rect.append(pygame.Rect(165, 234, 102, 126))     
    
    player_pos = [200, 600]
    player = Player(plane_img, player_rect, player_pos)
    
    
    bullet_rect = pygame.Rect(1004, 987, 9, 21)
    bullet_img = plane_img.subsurface(bullet_rect)
    
    
    enemy1_rect = pygame.Rect(534, 612, 57, 43)
    enemy1_img = plane_img.subsurface(enemy1_rect)
    enemy1_down_imgs = plane_img.subsurface(pygame.Rect(267, 347, 57, 43))
    
    
    
    enemies1 = pygame.sprite.Group()
    
    
    enemies_down = pygame.sprite.Group()
    
    
    shoot_frequency = 0
    enemy_frequency = 0
    
    
    score = 0
    
    
    clock = pygame.time.Clock()
    
    
    running = True
    
    
    while running:
    
        clock.tick(60)
    
        if not player.is_hit:
            if shoot_frequency % 15 == 0:
                player.shoot(bullet_img)
            shoot_frequency += 1
            if shoot_frequency >= 15:
                shoot_frequency = 0
    
    
        if enemy_frequency % 50 == 0:
            enemy1_pos = [randint(0, SCREEN_WIDTH - enemy1_rect.width), 0]
            enemy1 = Enemy(enemy1_img, enemy1_down_imgs, enemy1_pos)
            enemies1.add(enemy1)
        enemy_frequency += 1
        if enemy_frequency >= 100:
            enemy_frequency = 0
    
        for bullet in player.bullets:
            bullet.move()
            if bullet.rect.bottom < 0:
                player.bullets.remove(bullet)   
    
        for enemy in enemies1:
            enemy.move()
            if pygame.sprite.collide_circle(enemy, player):
                enemies_down.add(enemy)
                enemies1.remove(enemy)
                player.is_hit = True
                break
            if enemy.rect.top < 0:
                enemies1.remove(enemy)
    
        enemies1_down = pygame.sprite.groupcollide(enemies1, player.bullets, 1, 1)
        for enemy_down in enemies1_down:
            enemies_down.add(enemy_down)
    
        screen.fill(0)
        screen.blit(background, (0, 0))
    
        if not player.is_hit:
            screen.blit(player.image[0], player.rect)
        else:
            screen.blit(player.image[1], player.rect) 
            running = False
    
        for enemy_down in enemies_down:
            enemies_down.remove(enemy_down)
            score += 1
            screen.blit(enemy_down.down_imgs, enemy_down.rect)
    
        player.bullets.draw(screen)
        enemies1.draw(screen)
    
        score_font = pygame.font.Font(None, 36)
        score_text = score_font.render('score: '+str(score), True, (128, 128, 128))
        text_rect = score_text.get_rect()
        text_rect.topleft = [10, 10]
        screen.blit(score_text, text_rect)
    
        pygame.display.update()
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    
        key_pressed = pygame.key.get_pressed()
    
        if key_pressed[K_w] or key_pressed[K_UP]:
            player.moveUp()
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            player.moveDown()
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            player.moveLeft()
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            player.moveRight()
    
    font = pygame.font.Font(None, 64)
    text = font.render('score: '+ str(score), True, (255, 0, 0))
    text_rect = text.get_rect()
    text_rect.centerx = screen.get_rect().centerx
    text_rect.centery = screen.get_rect().centery + 24
    screen.blit(game_over, (0, 0))
    screen.blit(text, text_rect)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.display.update()

#超级玛丽
import pygame as pg
from source.main import main
def mali():
    main()
    pg.quit()

#2048游戏
import tkinter
from tkinter import *
def erba():
    _map_data = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]


    # -------------------------以下为2048游戏的基本算法---------------------------

    # 重置
    def reset():
        '''重新设置游戏数据,将地图恢复为初始状态，并加入两个数据 2 作用初始状态'''
        _map_data[:] = []  # _map_data.clear()
        _map_data.append([0, 0, 0, 0])
        _map_data.append([0, 0, 0, 0])
        _map_data.append([0, 0, 0, 0])
        _map_data.append([0, 0, 0, 0])
        # 在空白地图上填充两个2
        fill2()
        fill2()


    # 获取 0 个数
    def get_space_count():
        """获取没有数字的方格的数量,如果数量为0则说有无法填充新数据，游戏即将结束
        """
        count = 0
        for r in _map_data:
            count += r.count(0)
        return count


    # 计算分数
    def get_score():
        '''获取游戏的分数,得分规则是每次有两个数加在一起则生成相应的分数。
        如 2 和 2 合并后得4分, 8 和 8 分并后得 16分.
        根据一个大于2的数字就可以知道他共合并了多少次，可以直接算出分数:
        如:
           4 一定由两个2合并，得4分
           8 一定由两个4合并,则计:8 + 4 + 4 得32分
           ... 以此类推
        '''
        score = 0
        for r in _map_data:
            for c in r:
                score += 0 if c < 4 else c * int((math.log(c, 2) - 1.0))
        return score  # 导入数学模块


    # 随机数生成
    def fill2():
        '''填充2到空位置，如果填度成功返回True,如果已满，则返回False'''
        blank_count = get_space_count()  # 得到地图上空白位置的个数
        if 0 == blank_count:
            return False
        # 生成随机位置, 如，当只有四个空时，则生成0~3的数，代表自左至右，自上而下的空位置
        pos = random.randrange(0, blank_count)
        offset = 0
        for row in _map_data:  # row为行row
            for col in range(4):  # col 为列，column
                if 0 == row[col]:
                    if offset == pos:
                        # 把2填充到第row行，第col列的位置，返回True
                        row[col] = 2
                        return True
                    offset += 1


    # 结束判定
    def is_gameover():
        """判断游戏是否结束,如果结束返回True,否是返回False
        """
        for r in _map_data:
            # 如果水平方向还有0,则游戏没有结束
            if r.count(0):
                return False
            # 水平方向如果有两个相邻的元素相同，应当是可以合并的，则游戏没有结束
            for i in range(3):
                if r[i] == r[i + 1]:
                    return False
        for c in range(4):
            # 竖直方向如果有两个相邻的元素相同，应当可以合并的，则游戏没有结束
            for r in range(3):
                if _map_data[r][c] == _map_data[r + 1][c]:
                    return False
        # 以上都没有，则游戏结束
        return True


    # 移动合并分数
    def _left_move_number(line):
        '''左移一行数字,如果有数据移动则返回True，否则返回False:
        如: line = [0, 2, 0, 8] 即表达如下一行:
            +---+---+---+---+
            | 0 | 2 | 0 | 8 |      <----向左移动
            +---+---+---+---+
        此行数据需要左移三次:
          第一次左移结果:
            +---+---+---+---+
            | 2 | 0 | 8 | 0 |
            +---+---+---+---+
          第二次左移结果:
            +---+---+---+---+
            | 2 | 8 | 0 | 0 |
            +---+---+---+---+
          第三次左移结果:
            +---+---+---+---+
            | 2 | 8 | 0 | 0 |  # 因为最左则为2,所以8不动
            +---+---+---+---+
         最终结果: line = [4, 8, 0, 0]
        '''
        moveflag = False  # 是否移动的标识,先假设没有移动
        for _ in range(3):  # 重复执行下面算法三次
            for i in range(3):  # i为索引
                if 0 == line[i]:  # 此处有空位，右侧相邻数字向左侧移动，右侧填空白
                    moveflag = True
                    line[i] = line[i + 1]
                    line[i + 1] = 0
        return moveflag


    # 移动位置
    def _left_marge_number(line):
        '''向左侧进行相同单元格合并,合并结果放在左侧,右侧补零
        如: line = [2, 2, 4, 4] 即表达如下一行:
            +---+---+---+---+
            | 2 | 2 | 4 | 4 |
            +---+---+---+---+
        全并后的结果为:
            +---+---+---+---+
            | 4 | 0 | 8 | 0 |
            +---+---+---+---+
        最终结果: line = [4, 8, 8, 0]
        '''
        for i in range(3):
            if line[i] == line[i + 1]:
                moveflag = True
                line[i] *= 2  # 左侧翻倍
                line[i + 1] = 0  # 右侧归零


    # 移动逻辑
    def _left_move_aline(line):
        '''左移一行数据,如果有数据移动则返回True，否则返回False:
        如: line = [2, 0, 2, 8] 即表达如下一行:
            +---+---+---+---+
            | 2 |   | 2 | 8 |      <----向左移动
            +---+---+---+---+
        左移算法分为三步:
            1. 将所有数字向左移动来填补左侧空格,即:
                +---+---+---+---+
                | 2 | 2 | 8 |   |
                +---+---+---+---+
            2. 判断是否发生碰幢，如果两个相临且相等的数值则说明有碰撞需要合并,
               合并结果靠左，右则填充空格 
                +---+---+---+---+
                | 4 |   | 8 |   |
                +---+---+---+---+
            3. 再重复第一步，将所有数字向左移动来填补左侧空格,即:
                +---+---+---+---+
                | 4 | 8 |   |   |
                +---+---+---+---+
            最终结果: line = [4, 8, 0, 0]
        '''
        moveflag = False
        if _left_move_number(line):
            moveflag = True
        if _left_marge_number(line):
            moveflag = True
        if _left_move_number(line):
            moveflag = True
        return moveflag


    def left():
        """游戏左键按下时或向左滑动屏幕时的算法"""
        moveflag = False  # moveflag 是否成功移动数字标志位,如果有移动则为真值,原地图不变则为假值

        # 将第一行都向左移动.如果有移动就返回True
        for line in _map_data:
            if _left_move_aline(line):
                moveflag = True
        return moveflag


    def right():
        """游戏右键按下时或向右滑动屏幕时的算法
        选将屏幕进行左右对调，对调后，原来的向右滑动即为现在的向左滑动
        滑动完毕后，再次左右对调回来
        """
        # 左右对调
        for r in _map_data:
            r.reverse()
        moveflag = left()  # 向左滑动
        # 再次左右对调
        for r in _map_data:
            r.reverse()
        return moveflag


    def up():
        """游戏上键按下时或向上滑动屏幕时的算法
        先把每一列都自上而下放入一个列表中line中，然后执行向滑动，
        滑动完成后再将新位置摆回到原来的一列中
        """
        moveflag = False
        line = [0, 0, 0, 0]  # 先初始化一行，准备放入数据
        for col in range(4):  # 先取出每一列
            # 把一列中的每一行数入放入到line中
            for row in range(4):
                line[row] = _map_data[row][col]
            # 将当前列进行上移，即line 左移
            if (_left_move_aline(line)):
                moveflag = True
            # 把左移后的 line中的数据填充回原来的一列
            for row in range(4):
                _map_data[row][col] = line[row]
        return moveflag


    def down():
        """游戏下键按下时或向下滑动屏幕时的算法
        选将屏幕进行上下对调，对调后，原来的向下滑动即为现在的向上滑动
        滑动完毕后，再次上下对调回来
        """
        _map_data.reverse()
        moveflag = up()  # 上滑
        _map_data.reverse()
        return moveflag


    # -------------------------以下为2048游戏的操作界面---------------------------



    def main():
        reset()  # 先重新设置游戏数据

        root = Tk()  # 创建tkinter窗口
        root.title('2048游戏')  # 设置标题文字
        root.resizable(width=False, height=False)  # 固定宽和高

        # 以下是键盘映射
        keymap = {
            'a': left,
            'd': right,
            'w': up,
            's': down,
            'Left': left,
            'Right': right,
            'Up': up,
            'Down': down,
            'q': root.quit,
        }

        game_bg_color = "#bbada0"  # 设置背景颜色

        # 设置游戏中每个数据对应色块的颜色
        mapcolor = {
            0: ("#cdc1b4", "#776e65"),
            2: ("#eee4da", "#776e65"),
            4: ("#ede0c8", "#f9f6f2"),
            8: ("#f2b179", "#f9f6f2"),
            16: ("#f59563", "#f9f6f2"),
            32: ("#f67c5f", "#f9f6f2"),
            64: ("#f65e3b", "#f9f6f2"),
            128: ("#edcf72", "#f9f6f2"),
            256: ("#edcc61", "#f9f6f2"),
            512: ("#e4c02a", "#f9f6f2"),
            1024: ("#e2ba13", "#f9f6f2"),
            2048: ("#ecc400", "#f9f6f2"),
            4096: ("#ae84a8", "#f9f6f2"),
            8192: ("#b06ca8", "#f9f6f2"),
            # ----其它颜色都与8192相同---------
            2 ** 14: ("#b06ca8", "#f9f6f2"),
            2 ** 15: ("#b06ca8", "#f9f6f2"),
            2 ** 16: ("#b06ca8", "#f9f6f2"),
            2 ** 17: ("#b06ca8", "#f9f6f2"),
            2 ** 18: ("#b06ca8", "#f9f6f2"),
            2 ** 19: ("#b06ca8", "#f9f6f2"),
            2 ** 20: ("#b06ca8", "#f9f6f2"),
        }

        def on_key_down(event):
            '键盘按下处理函数'
            keysym = event.keysym
            if keysym in keymap:
                if keymap[keysym]():  # 如果有数字移动
                    fill2()  # 填充一个新的2
            update_ui()
            if is_gameover():
                mb = messagebox.askyesno(
                    title="gameover", message="游戏结束!\n是否退出游戏!")
                if mb:
                    root.quit()
                else:
                    reset()
                    update_ui()

        def update_ui():
            '''刷新界面函数
            根据计算出的f地图数据,更新各个Label的设置
            '''
            for r in range(4):
                for c in range(len(_map_data[0])):
                    number = _map_data[r][c]  # 设置数字
                    label = map_labels[r][c]  # 选中Lable控件
                    label['text'] = str(number) if number else ''
                    label['bg'] = mapcolor[number][0]
                    label['foreground'] = mapcolor[number][1]
            label_score['text'] = str(get_score())  # 重设置分数

        # 创建一个frame窗口，此创建将容纳全部的widget 部件
        frame = Frame(root, bg=game_bg_color)
        frame.grid(sticky=N + E + W + S)
        # 设置焦点能接收按键事件
        frame.focus_set()
        frame.bind("<Key>", on_key_down)

        # 初始化图形界面
        map_labels = []
        for r in range(4):
            row = []
            for c in range(len(_map_data[0])):
                value = _map_data[r][c]
                text = str(value) if value else ''
                label = Label(frame, text=text, width=4, height=2,
                              font=("黑体", 30, "bold"))
                label.grid(row=r, column=c, padx=5, pady=5, sticky=N + E + W + S)
                row.append(label)
            map_labels.append(row)

        # 设置显示分数的Lable
        label = Label(frame, text='分数', font=("黑体", 30, "bold"),
                      bg="#bbada0", fg="#eee4da")
        label.grid(row=4, column=0, padx=5, pady=5)
        label_score = Label(frame, text='0', font=("黑体", 30, "bold"),
                            bg="#bbada0", fg="#ffffff")
        label_score.grid(row=4, columnspan=2, column=1, padx=5, pady=5)

        # 以下设置重新开始按钮
        def reset_game():
            reset()
            update_ui()

        restart_button = Button(frame, text='重新开始', font=("黑体", 16, "bold"),
                                bg="#8f7a66", fg="#f9f6f2", command=reset_game)
        restart_button.grid(row=4, column=3, padx=5, pady=5)

        update_ui()  # 更新界面

        root.mainloop()  # 进入tkinter主事件循环


    main()  # 启动游戏

#扫雷游戏
def saolei():
    # 地雷数量
    MINE_COUNT = 99
    # 每个方格的大小（宽、高都为20）
    SIZE = 20
    # 方格的行数
    BLOCK_ROW_NUM = 16
    # 方格的列数
    BLOCK_COL_NUM = 30
    # 游戏窗口的宽、高
    SCREEN_WIDTH, SCREEN_HEIGHT = BLOCK_COL_NUM * SIZE, (BLOCK_ROW_NUM + 2) * SIZE


    def get_mine_flag_num(board_list):
        """
        计算还剩多少颗雷
        """
        num = 0
        for line in board_list:
            for num_dict in line:
                if num_dict.get("closed_num") == "雷标记":
                    num += 1

        return num


    def open_all_mine(board_list):
        """
        显示所有的雷
        """
        for row, line in enumerate(board_list):
            for col, num_dict in enumerate(line):
                if num_dict.get("opened_num") == "雷":
                    num_dict["opened"] = True


    def get_mine_num(row, col, board_list):
        """
        计算点击的空格周围的雷的数量
        """
        # 生成起始位置、终止位置
        row_start = row - 1 if row - 1 >= 0 else row
        row_stop = row + 2 if row + 1 <= BLOCK_ROW_NUM - 1 else row + 1
        col_start = col - 1 if col - 1 >= 0 else col
        col_stop = col + 2 if col + 1 <= BLOCK_COL_NUM - 1 else col + 1

        # 循环遍历当前方格周围的雷的数量
        mine_num = 0
        for i in range(row_start, row_stop):
            for j in range(col_start, col_stop):
                if board_list[i][j].get("opened_num") == "雷":
                    mine_num += 1
        return mine_num


    def set_nums_blank(row, col, board_list):
        """
        判断当前位置的周边位置是否为空，如果是则继续判断，
        最终能够实现点击一个空位置后连续的空位置都能够显示出来
        """
        mine_num = get_mine_num(row, col, board_list)
        print("row=%d, col=%d, mine_num=%d" % (row, col, mine_num))
        if mine_num == 0:
            board_list[row][col]['opened'] = True
            board_list[row][col]["opened_num"] = 0
            board_list[row][col]["closed_num"] = "空"
            # 判断对角是否是数字
            for i, j in [(-1, -1), (1, 1), (1, -1), (-1, 1)]:
                if 0 <= row + i <= 15 and 0 <= col + j <= 29:
                    mine_num = get_mine_num(row + i, col + j, board_list)
                    if mine_num:
                        board_list[row + i][col + j]['opened'] = True
                        board_list[row + i][col + j]["opened_num"] = mine_num
                        board_list[row + i][col + j]["closed_num"] = "空"

            # 判断剩下4个位置是否是也是0，即空
            for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if 0 <= row + i <= 15 and 0 <= col + j <= 29:
                    if not board_list[row + i][col + j].get("opened"):
                        set_nums_blank(row + i, col + j, board_list)
        else:
            board_list[row][col]['opened'] = True
            board_list[row][col]["opened_num"] = mine_num
            board_list[row][col]["closed_num"] = "空"


    def left_click_block(row, col, board_list):
        """
        左击空格后的处理
        """
        if board_list[row][col].get("opened") is False and board_list[row][col].get("opened_num") != "雷":
            # 如果不是雷，那么就计算当前位置数字
            mine_num = get_mine_num(row, col, board_list)
            print("地雷数:", mine_num)
            board_list[row][col]["opened_num"] = mine_num
            board_list[row][col]["opened"] = True  # 标记为"打开"状态
            board_list[row][col]["closed_num"] = "空"  # 标记为"未打开时的状态为空格"，防止显示剩余雷数错误
            if mine_num == 0:
                # 如果方格周边没有雷此时，判断是否有连续空位置
                set_nums_blank(row, col, board_list)
        elif board_list[row][col].get("opened") is False and board_list[row][col].get("opened_num") == "雷":
            board_list[row][col]["opened_num"] = "踩雷"  # 标记为"踩雷"图片
            board_list[row][col]["opened"] = True  # 标记为"打开"状态
            board_list[row][col]["closed_num"] = "空"  # 标记为"未打开时的状态为空格"，防止显示剩余雷数错误
            return True


    def create_random_board(row, col, mine_num):
        """
        得到一个随机的棋盘
        """
        # 随机布雷
        nums = [{"opened": False, "opened_num": 0, 'closed_num': "空"} for _ in range(row * col - mine_num)]  # 16x30-99 表示的是生成381个0
        nums += [{"opened": False, "opened_num": "雷", 'closed_num': "空"} for _ in range(mine_num)]  # 99颗地雷
        random.shuffle(nums)  # 乱序，此时nums是乱的
        return [list(x) for x in zip(*[iter(nums)] * col)]


    def right_click_block(row, col, board_list):
        """
        右击方格后更新其状态（标记为雷、问号?、取消标记）
        """
        if board_list[row][col].get("opened") is False:
            if board_list[row][col]["closed_num"] == "空":
                board_list[row][col]["closed_num"] = "雷标记"
            elif board_list[row][col]["closed_num"] == "雷标记":
                board_list[row][col]["closed_num"] = "疑问标记"
            elif board_list[row][col]["closed_num"] == "疑问标记":
                board_list[row][col]["closed_num"] = "空"


    def click_block(x, y, board_list):
        """
        检测点击的是哪个方格（即第x行，第y列）
        """
        # 计算出点击的空格的行、列
        for row, line in enumerate(board_list):
            for col, _ in enumerate(line):
                if col * SIZE <= x <= (col + 1) * SIZE and (row + 2) * SIZE <= y <= (row + 2 + 1) * SIZE:
                    print("点击的空格的位置是:", row, col)
                    return row, col


    def run(screen):
        bgcolor = (225, 225, 225)  # 背景色

        # 要显示的棋盘
        # board_list = [[0] * BLOCK_COL_NUM for _ in range(BLOCK_ROW_NUM)]
        board_list = create_random_board(BLOCK_ROW_NUM, BLOCK_COL_NUM, MINE_COUNT)  # 16行、30列，有99颗地雷

        # 默认的方格图片
        img_blank = pygame.image.load('resource/blank.bmp').convert()
        img_blank = pygame.transform.smoothscale(img_blank, (SIZE, SIZE))
        # "雷标记"图片
        img_mine_flag = pygame.image.load('resource/flag.bmp').convert()
        img_mine_flag = pygame.transform.smoothscale(img_mine_flag, (SIZE, SIZE))
        # "雷"图片
        img_mine = pygame.image.load('resource/mine.bmp').convert()
        img_mine = pygame.transform.smoothscale(img_mine, (SIZE, SIZE))
        # "疑问标记"图片
        img_ask = pygame.image.load('resource/ask.bmp').convert()
        img_ask = pygame.transform.smoothscale(img_ask, (SIZE, SIZE))
        # "踩雷"图片
        img_blood = pygame.image.load('resource/blood.bmp').convert()
        img_blood = pygame.transform.smoothscale(img_blood, (SIZE, SIZE))
        # "表情"图片
        face_size = int(SIZE * 1.25)
        img_face_fail = pygame.image.load('resource/face_fail.bmp').convert()
        img_face_fail = pygame.transform.smoothscale(img_face_fail, (face_size, face_size))
        img_face_normal = pygame.image.load('resource/face_normal.bmp').convert()
        img_face_normal = pygame.transform.smoothscale(img_face_normal, (face_size, face_size))
        img_face_success = pygame.image.load('resource/face_success.bmp').convert()
        img_face_success = pygame.transform.smoothscale(img_face_success, (face_size, face_size))
        # "表情"位置
        face_pos_x = (SCREEN_WIDTH - face_size) // 2
        face_pos_y = (SIZE * 2 - face_size) // 2
        # 类的数量图片
        img0 = pygame.image.load('resource/0.bmp').convert()
        img0 = pygame.transform.smoothscale(img0, (SIZE, SIZE))
        img1 = pygame.image.load('resource/1.bmp').convert()
        img1 = pygame.transform.smoothscale(img1, (SIZE, SIZE))
        img2 = pygame.image.load('resource/2.bmp').convert()
        img2 = pygame.transform.smoothscale(img2, (SIZE, SIZE))
        img3 = pygame.image.load('resource/3.bmp').convert()
        img3 = pygame.transform.smoothscale(img3, (SIZE, SIZE))
        img4 = pygame.image.load('resource/4.bmp').convert()
        img4 = pygame.transform.smoothscale(img4, (SIZE, SIZE))
        img5 = pygame.image.load('resource/5.bmp').convert()
        img5 = pygame.transform.smoothscale(img5, (SIZE, SIZE))
        img6 = pygame.image.load('resource/6.bmp').convert()
        img6 = pygame.transform.smoothscale(img6, (SIZE, SIZE))
        img7 = pygame.image.load('resource/7.bmp').convert()
        img7 = pygame.transform.smoothscale(img7, (SIZE, SIZE))
        img8 = pygame.image.load('resource/8.bmp').convert()
        img8 = pygame.transform.smoothscale(img8, (SIZE, SIZE))
        img_dict = {
            0: img0,
            1: img1,
            2: img2,
            3: img3,
            4: img4,
            5: img5,
            6: img6,
            7: img7,
            8: img8,
            '雷标记': img_mine_flag,
            '雷': img_mine,
            '空': img_blank,
            '疑问标记': img_ask,
            '踩雷': img_blood,
        }
        # 标记是否踩到雷
        game_over = False
        # 游戏状态
        game_status = "normal"
        # 显示雷的数量、耗时用到的资源
        font = pygame.font.Font('resource/a.TTF', SIZE * 2)  # 字体
        f_width, f_height = font.size('999')
        red = (200, 40, 40)
        # 标记出雷的个数
        flag_count = 0
        # 记录耗时
        elapsed_time = 0
        last_time = time.time()
        start_record_time = False

        # 创建计时器（防止while循环过快，占用太多CPU的问题）
        clock = pygame.time.Clock()
        while True:
            # 事件检测（鼠标点击、键盘按下等）
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button:
                    b1, b2, b3 = pygame.mouse.get_pressed()
                    mouse_click_type = None
                    if b1 and not b2 and not b3:  # 左击
                        mouse_click_type = "left"
                    elif not b1 and not b2 and b3:  # 右击
                        mouse_click_type = "right"
                    print("点击了鼠标的[%s]键" % mouse_click_type)
                    x, y = pygame.mouse.get_pos()
                    if game_status == "normal" and 2 * SIZE <= y <= SCREEN_HEIGHT:
                        # 计算点击的是哪个空
                        position = click_block(x, y, board_list)
                        if position:
                            if mouse_click_type == "right":
                                # 如果右击方格，那么就更新其状态
                                right_click_block(*position, board_list)
                                # 更新标记的雷的数量
                                flag_count = get_mine_flag_num(board_list)
                                start_record_time = True  # 开始记录耗时
                            elif mouse_click_type == "left":
                                # 点击空格的处理
                                game_over = left_click_block(*position, board_list)
                                print("是否踩到雷", game_over)
                                start_record_time = True  # 开始记录耗时
                                # 更新标记的雷的数量
                                flag_count = get_mine_flag_num(board_list)
                                if game_over:
                                    # 将所有雷的位置，标记出来
                                    open_all_mine(board_list)
                                    # 更改游戏状态
                                    game_status = "fail"
                                    # 停止记录耗时
                                    start_record_time = False
                    elif face_pos_x <= x <= face_pos_x + face_size and face_pos_y <= y <= face_pos_y + face_size:
                        # 重来一局
                        print("点击了再来一局...")
                        return

            # 填充背景色
            screen.fill(bgcolor)

            # 显示方格
            for i, line in enumerate(board_list):
                for j, num_dict in enumerate(line):
                    if num_dict.get("opened"):
                        screen.blit(img_dict[num_dict.get("opened_num")], (j * SIZE, (i + 2) * SIZE))
                    else:
                        screen.blit(img_dict[num_dict.get("closed_num")], (j * SIZE, (i + 2) * SIZE))

            # 显示表情
            if game_status == "win":
                screen.blit(img_face_success, (face_pos_x, face_pos_y))
            elif game_status == "fail":
                screen.blit(img_face_fail, (face_pos_x, face_pos_y))
            else:
                screen.blit(img_face_normal, (face_pos_x, face_pos_y))

            # 显示剩余雷的数量
            mine_text = font.render('%02d' % (MINE_COUNT - flag_count), True, red)
            screen.blit(mine_text, (30, (SIZE * 2 - f_height) // 2 - 2))

            # 显示耗时
            if start_record_time and time.time() - last_time >= 1:
                elapsed_time += 1
                last_time = time.time()
            mine_text = font.render('%03d' % elapsed_time, True, red)
            screen.blit(mine_text, (SCREEN_WIDTH - f_width - 30, (SIZE * 2 - f_height) // 2 - 2))

            # 刷新显示（此时窗口才会真正的显示）
            pygame.display.update()
            # FPS（每秒钟显示画面的次数）
            clock.tick(60)  # 通过一定的延时，实现1秒钟能够循环60次


    def main():
        """
        循环调用run函数，每调用一次就重新来一局游戏
        """
        pygame.init()
        pygame.display.set_caption('扫雷')
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        while True:
            run(screen)


    if __name__ == '__main__':
        main()

#主程序
def fasdasdf1():
    #变量定义
    global dakai,xuanzhong
    xuanzhong = None
    dakai = None

    #窗口设置
    pygame.init()
    screen = pygame.display.set_mode((1150,768))
    pygame.display.set_caption("Starry Sky System(星空系统)")

    #主循环体
    while True:
        #循环遍历检测
        for event in pygame.event.get():
            #退出事件
            if event.type == pygame.QUIT:
                if messagebox.askokcancel("是否退出", "您确定退出吗（主窗口退出将直接结束程序）"):
                    sys.exit(0)

            #快捷键
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:
                    ImageGrab.grab().show()
                elif event.key == pygame.K_f:
                    dakai = "file"
                elif event.key == pygame.K_n:
                    dakai = "news"
                elif event.key == pygame.K_e:
                    dakai = "brow"
                elif event.key == pygame.K_c:
                    dakai = "com"
                elif event.key == pygame.K_r:
                    dakai = "sousuo"
                elif event.key == pygame.K_g:
                    dakai = "cmd"

            #检测应用、任务栏被选中、打开
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #应用打开

                #文件管理器
                if mouseRect.colliderect(fileRect):
                    if xuanzhong == "file":
                        dakai = "file"
                        
                    else:
                        xuanzhong = "file"

                #音乐播放器
                if mouseRect.colliderect(musicRect):
                    if xuanzhong == "music":
                        dakai = "music"
                        
                    else:
                        xuanzhong = "music"
                #Vs Code编辑器
                if mouseRect.colliderect(vsRect):
                    if xuanzhong == "vs":
                        dakai = "vs"
                        
                    else:
                        xuanzhong = "vs"

                #系统设置、此电脑
                if mouseRect.colliderect(comRect):
                    if xuanzhong == "com":
                        dakai = "com"
                        
                    else:
                        xuanzhong = "com"

                #浏览器
                if mouseRect.colliderect(browRect):
                    if xuanzhong == "brow":
                        dakai = "brow"
                        
                    else:
                        xuanzhong = "brow"

                #视频播放器
                if mouseRect.colliderect(videoRect):
                    if xuanzhong == "video":
                        dakai = "video"
                        
                    else:
                        xuanzhong = "video"

                #记事本
                if mouseRect.colliderect(txtRect):
                    if xuanzhong == "txt":
                        dakai = "txt"
                        
                    else:
                        xuanzhong = "txt"

                #绘画板
                if mouseRect.colliderect(drawsRect):
                    if xuanzhong == "draws":
                        dakai = "draws"
                        
                    else:
                        xuanzhong = "draws"

                #图片查看器
                if mouseRect.colliderect(photoRect):
                    if xuanzhong == "photo":
                        dakai = "photo"
                        
                    else:
                        xuanzhong = "photo"

                #计算器
                if mouseRect.colliderect(jisuansRect):
                    if xuanzhong == "jisuans":
                        dakai = "jisuans"
                        
                    else:
                        xuanzhong = "jisuans"

                #数学计算工具
                if mouseRect.colliderect(shuxuesRect):
                    if xuanzhong == "shuxues":
                        dakai = "shuxues"
                        
                    else:
                        xuanzhong = "shuxues"

                #二维码生成器
                if mouseRect.colliderect(ermRect):
                    if xuanzhong == "erm":
                        dakai = "erm"
                        
                    else:
                        xuanzhong = "erm"

                #翻译器
                if mouseRect.colliderect(fanyiRect):
                    if xuanzhong == "fanyi":
                        dakai = "fanyi"
                        
                    else:
                        xuanzhong = "fanyi"

                #天气预报
                if mouseRect.colliderect(tianqiRect):
                    if xuanzhong == "tianqi":
                        dakai = "tianqi"
                        
                    else:
                        xuanzhong = "tianqi"

                #短信发送器
                if mouseRect.colliderect(duanxinRect):
                    if xuanzhong == "duanxin":
                        dakai = "duanxin"
                        
                    else:
                        xuanzhong = "duanxin"

                #新闻查看器
                if mouseRect.colliderect(newsRect):
                    if xuanzhong == "news":
                        dakai = "news"
                        
                    else:
                        xuanzhong = "news"

                #文件整理器
                if mouseRect.colliderect(zhengRect):
                    if xuanzhong == "zheng":
                        dakai = "zheng"
                        
                    else:
                        xuanzhong = "zheng"

                #奥运会结果
                if mouseRect.colliderect(aoyunRect):
                    if xuanzhong == "aoyun":
                        dakai = "aoyun"
                        
                    else:
                        xuanzhong = "aoyun"

                #谷歌小恐龙
                if mouseRect.colliderect(konglongRect):
                    if xuanzhong == "konglong":
                        dakai = "konglong"
                        
                    else:
                        xuanzhong = "konglong"

                #我的世界
                if mouseRect.colliderect(mincRect):
                    if xuanzhong == "minc":
                        dakai = "minc"
                        
                    else:
                        xuanzhong = "minc"

                #cmd命令行
                if mouseRect.colliderect(cmdRect):
                    if xuanzhong == "cmd":
                        dakai = "cmd"
                        
                    else:
                        xuanzhong = "cmd"

                #飞机大战
                if mouseRect.colliderect(planeRect):
                    if xuanzhong == "plane":
                        dakai = "plane"
                        
                    else:
                        xuanzhong = "plane"

                #超级玛丽
                if mouseRect.colliderect(maryRect):
                    if xuanzhong == "mary":
                        dakai = "mary"
                        
                    else:
                        xuanzhong = "mary"

                #2048游戏
                if mouseRect.colliderect(erbRect):
                    if xuanzhong == "erb":
                        dakai = "erb"
                        
                    else:
                        xuanzhong = "erb"

                #扫雷游戏
                if mouseRect.colliderect(saoRect):
                    if xuanzhong == "sao":
                        dakai = "sao"
                        
                    else:
                        xuanzhong = "sao"
                
                #任务栏打开

                #文件
                if mouseRect.colliderect(wenjianRect):
                    dakai = "file"

                #浏览器
                if mouseRect.colliderect(liulanRect):
                    dakai = "brow"

                #设置
                if mouseRect.colliderect(shezhiRect):
                    dakai = "com"

                #资讯
                if mouseRect.colliderect(zixunRect):
                    dakai = "news"

                #搜索
                if mouseRect.colliderect(souRect):
                    dakai = "sousuo"

            
            #任务栏图标检测

            #开始键    
            if mouseRect.colliderect(offRect):
                offs = "windows11.png"
            else:
                offs = "win11.png"

            #搜索键
            if mouseRect.colliderect(souRect):
                sous = "搜索2.png"
            else:
                sous = "搜索.png"

            #资讯键
            if mouseRect.colliderect(zixunRect):
                zixuns = "资讯2.png"
            else:
                zixuns = "资讯.png"

            #设置键
            if mouseRect.colliderect(shezhiRect):
                shezhis = "设置2.png"
            else:
                shezhis = "设置.png"

            #此电脑键
            if mouseRect.colliderect(wenjianRect):
                wenjians = "文件2.png"
            else:
                wenjians = "文件.png"

            #浏览器键
            if mouseRect.colliderect(liulanRect):
                liulans = "浏览2.png"
            else:
                liulans = "浏览.png"

            #商店键
            if mouseRect.colliderect(shangdianRect) :
                shangdians = "商店2.png"
            else:
                shangdians = "商店.png"

        #任务执行

        #退出检测循环
        if dakai != None:
            pygame.quit()
            break

        #绘制背景
        screen.fill((255,255,255))
        screen.blit(bg,(0,0))
        
        #任务栏图标设置
        off = pygame.transform.scale(pygame.image.load(offs),(80,60))
        sou = pygame.transform.scale(pygame.image.load(sous),(60,60))
        zixun = pygame.transform.scale(pygame.image.load(zixuns),(60,60))
        shezhi = pygame.transform.scale(pygame.image.load(shezhis),(60,60))
        wenjian = pygame.transform.scale(pygame.image.load(wenjians),(60,60))
        liulan = pygame.transform.scale(pygame.image.load(liulans),(60,60))
        shangdian = pygame.transform.scale(pygame.image.load(shangdians),(60,60))

        #工具栏图标绘制
        screen.blit(dianliang,(970,710))
        screen.blit(shengyin,(1030,710))
        screen.blit(wangluo,(1080,710))

        #任务栏图标绘制
        screen.blit(caidan,(0,710))
        screen.blit(off,(300,710))
        screen.blit(sou,(375,710))
        screen.blit(zixun,(435,710))
        screen.blit(shezhi,(495,710))
        screen.blit(wenjian,(555,710))
        screen.blit(liulan,(615,710))
        screen.blit(shangdian,(675,710))

        #应用图标绘制

        #文件管理器

        #图片
        screen.blit(file,(30,20))
        #文字
        screen.blit(fileText,(25,70))

        #音乐播放器
        screen.blit(music,(105,20))
        screen.blit(musicText,(105,70))

        #VS Code编辑器
        screen.blit(vs,(180,20))
        screen.blit(vsText,(185,70))

        #此电脑设置
        screen.blit(com,(255,20))
        screen.blit(comText,(255,70))

        #浏览器
        screen.blit(brow,(320,20))
        screen.blit(browText,(320,70))

        #视频播放器
        screen.blit(video,(395,20))
        screen.blit(videoText,(385,70))

        #记事本
        screen.blit(txt,(470,20))
        screen.blit(txtText,(470,70))

        #绘画板
        screen.blit(draws,(545,20))
        screen.blit(drawsText,(545,70))

        #图片查看器
        screen.blit(photo,(620,20))
        screen.blit(photoText,(610,70))

        #计算器
        screen.blit(jisuans,(695,20))
        screen.blit(jisuansText,(695,70))

        #数学计算工具
        screen.blit(shuxues,(770,20))
        screen.blit(shuxuesText,(755,70))

        #二维码生成器
        screen.blit(erm,(845,20))
        screen.blit(ermText,(850,70))

        #翻译器
        screen.blit(fanyi,(920,20))
        screen.blit(fanyiText,(925,70))

        #天气预报
        screen.blit(tianqi,(995,20))
        screen.blit(tianqiText,(995,70))

        #短信发送器
        screen.blit(duanxin,(1070,20))
        screen.blit(duanxinText,(1070,70))

        #新闻查看器
        screen.blit(news,(30,95))
        screen.blit(newsText,(20,145))

        #文件整理器
        screen.blit(zheng,(105,95))
        screen.blit(zhengText,(95,145))

        #奥运会结果
        screen.blit(aoyun,(180,95))
        screen.blit(aoyunText,(175,145))

        #谷歌小恐龙
        screen.blit(konglong,(255,95))
        screen.blit(konglongText,(250,145))

        #我的世界
        screen.blit(minc,(330,95))
        screen.blit(mincText,(330,145))

        #cmd命令行
        screen.blit(cmd,(405,95))
        screen.blit(cmdText,(400,145))

        #飞机大战
        screen.blit(plane,(480,95))
        screen.blit(planeText,(480,145))

        #超级玛丽
        screen.blit(mary,(555,95))
        screen.blit(maryText,(555,145))

        #2048游戏
        screen.blit(erb,(630,95))
        screen.blit(erbText,(630,145))

        #扫雷游戏
        screen.blit(sao,(705,95))
        screen.blit(saoText,(705,145))
        
        #更新屏幕
        mouseRect.center = (pygame.mouse.get_pos())
        pygame.display.update()

    #应用判断打开

    #文件管理器
    if dakai == "file":
        #打开函数
        files1()
        #返回主页
        fasdasdf1()

    #音乐播放器
    elif dakai == "music":
        musics()
        fasdasdf1()

    #Vs Code编辑器
    elif dakai == "vs":
        codes()
        fasdasdf1()

    #此电脑设置
    elif dakai == "com":
        sysset()
        fasdasdf1()

    #浏览器
    elif dakai == "brow":
        browsers()
        fasdasdf1()

    #视频播放器
    elif dakai == "video":
        videos()
        fasdasdf1()

    #记事本
    elif dakai == "txt":
        notebook()
        fasdasdf1()

    #绘画板
    elif dakai == "draws":
        huihua()
        fasdasdf1()

    #图片查看器
    elif dakai == "photo":
        photos()
        fasdasdf1()

    #计算器
    elif dakai == "jisuans":
        jisuan()
        fasdasdf1()

    #数学计算工具
    elif dakai == "shuxues":
        shuxue()
        fasdasdf1()

    #二维码生成器
    elif dakai == "erm":
        # erma()
        messagebox.showinfo("提示","该功能暂未开放")
        fasdasdf1()

    #翻译器
    elif dakai == "fanyi":
        translate()
        fasdasdf1()

    #天气预报
    elif dakai == "tianqi":
        temp()
        fasdasdf1()

    #短信发送器
    elif dakai == "duanxin":
        smstool()
        fasdasdf1()

    #新闻查看器
    elif dakai == "news":
        xinwen()
        fasdasdf1()

    #文件整理器
    elif dakai == "zheng":
        # zhengli()
        messagebox.showinfo("提示","该功能尚未开放")
        fasdasdf1()

    #奥运结果
    elif dakai == "aoyun":
        aoyunhui()
        fasdasdf1()

    #谷歌小恐龙
    elif dakai == "konglong":
        dino()
        fasdasdf1()

    #我的世界
    elif dakai == "minc":
        mink()
        fasdasdf1()

    #搜索导航
    elif dakai == "sousuo":
        sousou()
        fasdasdf1()

    #命令行界面
    elif dakai == "cmd":
        cmds()
        fasdasdf1()

    #飞机大战
    elif dakai == "plane":
        feiji()
        fasdasdf1()

    #超级玛丽
    elif dakai == "mary":
        # mali()
        messagebox.showinfo("提示","该功能尚未开放")
        fasdasdf1()

    #2048游戏
    elif dakai == "erb":
        erba()
        fasdasdf1()

    #扫雷
    elif dakai == "sao":
        saolei()
        fasdasdf1()

fasdasdf1()