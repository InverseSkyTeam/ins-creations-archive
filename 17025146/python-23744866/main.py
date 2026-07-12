#!/usr/bin/python#本作品作者吴宇航
# -*- coding: utf-8 -*-#本作品作者吴宇航
#本作品作者吴宇航
#导库#本作品作者吴宇航
from __future__ import division#本作品作者吴宇航
import pygame,sys,random,time,turtle#本作品作者吴宇航
from wx import *#本作品作者吴宇航
import os#本作品作者吴宇航
from PIL import ImageGrab#本作品作者吴宇航
from random import *#本作品作者吴宇航
import requests#本作品作者吴宇航
import json#本作品作者吴宇航
from copy import *#本作品作者吴宇航
from tkinter.ttk import Button,Entry,Radiobutton,Scrollbar#本作品作者吴宇航
from tkinter import END,Label,Tk,StringVar,Listbox,messagebox,SINGLE,PhotoImage#本作品作者吴宇航
# from moviepy.editor import *#本作品作者吴宇航
import pyglet#本作品作者吴宇航
from pyglet.media import *#本作品作者吴宇航
from lxml import etree#本作品作者吴宇航
from  selenium import webdriver#本作品作者吴宇航
import wx#本作品作者吴宇航
import wx.html2#本作品作者吴宇航
import webbrowser#本作品作者吴宇航
from PIL import Image,ImageTk#本作品作者吴宇航
import io#本作品作者吴宇航
import re#本作品作者吴宇航
import tkinter as tk#本作品作者吴宇航
from PyQt5.QtWidgets import (QWidget, QDesktopWidget,#本作品作者吴宇航
    QMessageBox, QHBoxLayout, QVBoxLayout, QSlider, QListWidget,#本作品作者吴宇航
    QPushButton, QLabel, QComboBox, QFileDialog)#本作品作者吴宇航
from PyQt5.QtGui import QIcon#本作品作者吴宇航
from PyQt5.QtCore import Qt, QUrl, QTimer#本作品作者吴宇航
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent#本作品作者吴宇航
import configparser#本作品作者吴宇航
from tkinter.filedialog import askdirectory#本作品作者吴宇航
import tkinter.messagebox#本作品作者吴宇航
import pyperclip #本作品作者吴宇航
import tkinter#本作品作者吴宇航
from tkinter import Button#本作品作者吴宇航
from tkinter import Label#本作品作者吴宇航
from tkinter import Entry#本作品作者吴宇航
from tkinter import Scale#本作品作者吴宇航
from tkinter import Label,PhotoImage#本作品作者吴宇航
from tkinter import messagebox#本作品作者吴宇航
from tkinter import Toplevel#本作品作者吴宇航
import copy#本作品作者吴宇航
from pymediainfo import MediaInfo#本作品作者吴宇航
from tkinter import Message#本作品作者吴宇航
import threading#本作品作者吴宇航
from tkinter.filedialog   import askopenfilename#本作品作者吴宇航
from tkinter.filedialog import askdirectory#本作品作者吴宇航
from tkinter import StringVar#本作品作者吴宇航
import os#本作品作者吴宇航
from cefpython3 import cefpython#本作品作者吴宇航
from pygame.locals import *#本作品作者吴宇航
import wx#本作品作者吴宇航
from tkinter import *#本作品作者吴宇航
import tkinter.filedialog#本作品作者吴宇航
import tkinter.messagebox as tmb#本作品作者吴宇航
import urllib.request#本作品作者吴宇航
from lxml import etree#本作品作者吴宇航
from time import*#本作品作者吴宇航
from tkinter import*#本作品作者吴宇航
import wx.html2#本作品作者吴宇航
import pygame.gfxdraw#本作品作者吴宇航
from collections import namedtuple#本作品作者吴宇航
from collections import deque#本作品作者吴宇航
from pyglet import image#本作品作者吴宇航
from pyglet.gl import *#本作品作者吴宇航
import numpy as np#本作品作者吴宇航
from datetime import*#本作品作者吴宇航
import platform#本作品作者吴宇航
import wx.html2#本作品作者吴宇航
from pygame.color import THECOLORS as COLORS#本作品作者吴宇航
from collections import OrderedDict#本作品作者吴宇航
from pyglet.graphics import TextureGroup#本作品作者吴宇航
from pyglet.window import key, mouse#本作品作者吴宇航
from tkinter.ttk import *#本作品作者吴宇航
from math import *#本作品作者吴宇航
from easygui import *#本作品作者吴宇航
import wmi#本作品作者吴宇航
import psutil#本作品作者吴宇航
from os import path#本作品作者吴宇航
from sys import exit#本作品作者吴宇航
from time import sleep#本作品作者吴宇航
from random import choice#本作品作者吴宇航
from itertools import product#本作品作者吴宇航
from matplotlib import pyplot as plt#本作品作者吴宇航
from tkinter.colorchooser import askcolor#本作品作者吴宇航
import pygame, sys, os#本作品作者吴宇航
from pygame.locals import *#本作品作者吴宇航
from tkinter.messagebox import *#本作品作者吴宇航
from tkinter.filedialog import *#本作品作者吴宇航
import math#本作品作者吴宇航
from tkinter import ttk, messagebox, filedialog#本作品作者吴宇航
import tkinter#本作品作者吴宇航
from PIL import Image, ImageTk#本作品作者吴宇航
from email.policy import default#本作品作者吴宇航
from setuptools.sandbox import save_argv#本作品作者吴宇航
from asyncio.protocols import Protocol#本作品作者吴宇航
from PyQt5.QtWidgets import*#本作品作者吴宇航
from tkinter import *#本作品作者吴宇航
import tkinter.ttk as tk#本作品作者吴宇航
import datetime#本作品作者吴宇航
import tkinter.font as tf#本作品作者吴宇航
import random#本作品作者吴宇航
from datetime import*#本作品作者吴宇航
from win10toast import ToastNotifier#本作品作者吴宇航
from MBPython import miniblink#本作品作者吴宇航
from pygame.locals import QUIT, KEYDOWN#本作品作者吴宇航
if (sys.version_info > (3, 0)):#本作品作者吴宇航
    from tkinter import *#本作品作者吴宇航
    from tkinter import messagebox#本作品作者吴宇航
else:#本作品作者吴宇航
    from Tkinter import *#本作品作者吴宇航
import wx,tkinter#本作品作者吴宇航
import math#本作品作者吴宇航
from math import *#本作品作者吴宇航
#本作品作者吴宇航
#基础准备#本作品作者吴宇航
global dakai,xuanzhong#本作品作者吴宇航
pygame.init()#本作品作者吴宇航
mousex, mousey = pygame.mouse.get_pos()#本作品作者吴宇航
mouseRect = pygame.Rect(mousex,mousey,5,5)#本作品作者吴宇航
#本作品作者吴宇航
#图片、文字、矩形对象#本作品作者吴宇航
#本作品作者吴宇航
#矩形对象#本作品作者吴宇航
offRect = pygame.Rect(300,710,60,60)#本作品作者吴宇航
souRect = pygame.Rect(375,710,60,60)#本作品作者吴宇航
zixunRect = pygame.Rect(440,710,60,60)#本作品作者吴宇航
shezhiRect = pygame.Rect(505,710,60,60)#本作品作者吴宇航
wenjianRect = pygame.Rect(570,710,60,60)#本作品作者吴宇航
liulanRect = pygame.Rect(635,710,60,60)#本作品作者吴宇航
shangdianRect = pygame.Rect(700,710,60,60)#本作品作者吴宇航
fileRect = pygame.Rect(30,20,50,50)#本作品作者吴宇航
musicRect = pygame.Rect(105,20,50,50)#本作品作者吴宇航
vsRect = pygame.Rect(180,20,50,50)#本作品作者吴宇航
comRect = pygame.Rect(255,20,50,50)#本作品作者吴宇航
browRect = pygame.Rect(320,20,50,50)#本作品作者吴宇航
videoRect = pygame.Rect(395,20,50,50)#本作品作者吴宇航
txtRect = pygame.Rect(470,20,50,50)#本作品作者吴宇航
drawsRect = pygame.Rect(545,20,50,50)#本作品作者吴宇航
photoRect = pygame.Rect(620,20,50,50)#本作品作者吴宇航
jisuansRect = pygame.Rect(695,20,50,50)#本作品作者吴宇航
shuxuesRect = pygame.Rect(770,20,50,50)#本作品作者吴宇航
ermRect = pygame.Rect(845,20,50,50)#本作品作者吴宇航
fanyiRect = pygame.Rect(920,20,50,50)#本作品作者吴宇航
tianqiRect = pygame.Rect(995,20,50,50)#本作品作者吴宇航
duanxinRect = pygame.Rect(1070,20,50,50)#本作品作者吴宇航
newsRect = pygame.Rect(30,95,50,50)#本作品作者吴宇航
zhengRect = pygame.Rect(105,95,50,50)#本作品作者吴宇航
aoyunRect = pygame.Rect(180,95,50,50)#本作品作者吴宇航
konglongRect = pygame.Rect(255,95,50,50)#本作品作者吴宇航
mincRect = pygame.Rect(330,95,50,50)#本作品作者吴宇航
cmdRect = pygame.Rect(405,95,50,50)#本作品作者吴宇航
planeRect = pygame.Rect(480,95,50,50)#本作品作者吴宇航
maryRect = pygame.Rect(555,95,50,50)#本作品作者吴宇航
erbRect = pygame.Rect(630,95,50,50)#本作品作者吴宇航
saoRect = pygame.Rect(705,95,50,50)#本作品作者吴宇航
psRect = pygame.Rect(780,95,50,50)#本作品作者吴宇航
#本作品作者吴宇航
#任务栏图标#本作品作者吴宇航
offs = "win11.png"#本作品作者吴宇航
sous = "搜索.png"#本作品作者吴宇航
zixuns = "资讯.png"#本作品作者吴宇航
shezhis = "设置.png"#本作品作者吴宇航
wenjians = "文件.png"#本作品作者吴宇航
liulans = "浏览.png"#本作品作者吴宇航
shangdians = "商店.png"#本作品作者吴宇航
#本作品作者吴宇航
#应用图标#本作品作者吴宇航
dianliang = pygame.transform.scale(pygame.image.load("电量.png"),(60,60))#本作品作者吴宇航
shengyin = pygame.transform.scale(pygame.image.load("声音.png"),(60,60))#本作品作者吴宇航
wangluo = pygame.transform.scale(pygame.image.load("网络.png"),(60,60))#本作品作者吴宇航
caidan = pygame.transform.scale(pygame.image.load("任务栏.png"),(1300,60))#本作品作者吴宇航
bg = pygame.transform.scale(pygame.image.load("bg.jpeg"),(1200,800))#本作品作者吴宇航
file = pygame.transform.scale(pygame.image.load("files.ico"),(50,50))#本作品作者吴宇航
music = pygame.transform.scale(pygame.image.load("音乐播放器.jpeg"),(50,50))#本作品作者吴宇航
vs = pygame.transform.scale(pygame.image.load("vscode.jpeg"),(50,50))#本作品作者吴宇航
com = pygame.transform.scale(pygame.image.load("此电脑.png"),(50,50))#本作品作者吴宇航
brow = pygame.transform.scale(pygame.image.load("浏览器.png"),(50,50))#本作品作者吴宇航
video = pygame.transform.scale(pygame.image.load("视频播放器.jpeg"),(50,50))#本作品作者吴宇航
txt = pygame.transform.scale(pygame.image.load("记事本.jpeg"),(50,50))#本作品作者吴宇航
draws = pygame.transform.scale(pygame.image.load("画图.jpeg"),(50,50))#本作品作者吴宇航
photo = pygame.transform.scale(pygame.image.load("图片查看器.png"),(50,50))#本作品作者吴宇航
jisuans = pygame.transform.scale(pygame.image.load("计算器.jpg"),(50,50))#本作品作者吴宇航
shuxues = pygame.transform.scale(pygame.image.load("数学计算.jpeg"),(50,50))#本作品作者吴宇航
erm = pygame.transform.scale(pygame.image.load("二维码生成器.jpeg"),(50,50))#本作品作者吴宇航
fanyi = pygame.transform.scale(pygame.image.load("翻译器.jpg"),(50,50))#本作品作者吴宇航
tianqi = pygame.transform.scale(pygame.image.load("天气预报.jpeg"),(50,50))#本作品作者吴宇航
duanxin = pygame.transform.scale(pygame.image.load("短信发送器.jpeg"),(50,50))#本作品作者吴宇航
news = pygame.transform.scale(pygame.image.load("新闻查看器.jpeg"),(50,50))#本作品作者吴宇航
zheng = pygame.transform.scale(pygame.image.load("文件整理器.png"),(50,50))#本作品作者吴宇航
aoyun = pygame.transform.scale(pygame.image.load("奥运.jpeg"),(50,50))#本作品作者吴宇航
konglong = pygame.transform.scale(pygame.image.load("谷歌小恐龙.jpeg"),(50,50))#本作品作者吴宇航
minc = pygame.transform.scale(pygame.image.load("我的世界.jpeg"),(50,50))#本作品作者吴宇航
cmd = pygame.transform.scale(pygame.image.load("cmd.jpeg"),(50,50))#本作品作者吴宇航
plane = pygame.transform.scale(pygame.image.load("飞机大战.jpeg"),(50,50))#本作品作者吴宇航
mary = pygame.transform.scale(pygame.image.load("超级玛丽.jpeg"),(50,50))#本作品作者吴宇航
erb = pygame.transform.scale(pygame.image.load("2048.jpeg"),(50,50))#本作品作者吴宇航
sao = pygame.transform.scale(pygame.image.load("扫雷.jpeg"),(50,50))#本作品作者吴宇航
ps = pygame.transform.scale(pygame.image.load("ps.jpeg"),(50,50))#本作品作者吴宇航

#本作品作者吴宇航
#文字#本作品作者吴宇航
myFont = pygame.font.SysFont("STzhongsong",15)#本作品作者吴宇航
fileText = myFont.render("文件管理器",True,(255,255,255))#本作品作者吴宇航
musicText = myFont.render("音乐播放器",True,(255,255,255))#本作品作者吴宇航
vsText = myFont.render("VS Code",True,(255,255,255))#本作品作者吴宇航
comText = myFont.render("此电脑",True,(255,255,255))#本作品作者吴宇航
browText = myFont.render("浏览器",True,(255,255,255))#本作品作者吴宇航
videoText = myFont.render("视频播放器",True,(255,255,255))#本作品作者吴宇航
txtText = myFont.render("记事本",True,(255,255,255))#本作品作者吴宇航
drawsText = myFont.render("绘画板",True,(255,255,255))#本作品作者吴宇航
photoText = myFont.render("图片处理器",True,(255,255,255))#本作品作者吴宇航
jisuansText = myFont.render("计算器",True,(255,255,255))#本作品作者吴宇航
shuxuesText = myFont.render("数学计算工具",True,(255,255,255))#本作品作者吴宇航
ermText = myFont.render("二维码",True,(255,255,255))#本作品作者吴宇航
fanyiText = myFont.render("翻译器",True,(255,255,255))#本作品作者吴宇航
tianqiText = myFont.render("天气预报",True,(255,255,255))#本作品作者吴宇航
duanxinText = myFont.render("短信发送器",True,(255,255,255))#本作品作者吴宇航
newsText = myFont.render("新闻查看器",True,(255,255,255))#本作品作者吴宇航
zhengText = myFont.render("文件整理器",True,(255,255,255))#本作品作者吴宇航
aoyunText = myFont.render("奥运会结果",True,(255,255,255))#本作品作者吴宇航
konglongText = myFont.render("谷歌小恐龙",True,(255,255,255))#本作品作者吴宇航
mincText = myFont.render("我的世界",True,(255,255,255))#本作品作者吴宇航
cmdText = myFont.render("cmd命令行",True,(255,255,255))#本作品作者吴宇航
planeText = myFont.render("飞机大战",True,(255,255,255))#本作品作者吴宇航
maryText = myFont.render("超级玛丽",True,(255,255,255))#本作品作者吴宇航
erbText = myFont.render("2048游戏",True,(255,255,255))#本作品作者吴宇航
saoText = myFont.render("扫雷游戏",True,(255,255,255))#本作品作者吴宇航
psText = myFont.render("PhotoShop",True,(255,255,255))#本作品作者吴宇航
#本作品作者吴宇航
#开头欢迎界面#本作品作者吴宇航
messagebox.showinfo("欢迎","尊敬的用户，您好！")#本作品作者吴宇航
messagebox.showinfo("欢迎","欢迎使用星空模拟系统(Starry Sky System,简称S.S.S模拟系统)，该系统为windows11界面版本")#本作品作者吴宇航
messagebox.showinfo("欢迎","本系统为继星空模拟系统windows10界面版本后的又一款星空模拟系统")#本作品作者吴宇航
messagebox.showinfo("欢迎","本系统侧重于工具和算法方面，兼顾一些游戏，使用起来轻便快捷")#本作品作者吴宇航
messagebox.showinfo("欢迎","星空系统这次更新，将UI方面的内容全部重写，使其更加美观，冷色系的界面护眼，带给人一种清新之感")#本作品作者吴宇航
messagebox.showinfo("欢迎","该版本还加入了一些快捷键，使用及其方便，让您真正的更贴近所爱之物")#本作品作者吴宇航
messagebox.showinfo("欢迎","最后，祝您使用愉快！")#本作品作者吴宇航
messagebox.showinfo("提示","快捷键操作：\nf键打开文件管理器\nn键查看资讯新闻\ne键打开浏览器\nc键打开此电脑设置\nr键打开搜索导航\ng键打开命令行界面\nj键截图")#本作品作者吴宇航
#本作品作者吴宇航
#开机动画#本作品作者吴宇航
pygame.display.set_caption("Starry Sky System(星空系统)")#本作品作者吴宇航
# clip = VideoFileClip('open.mp4')#本作品作者吴宇航
# clip= clip.resize(newsize=(1280,720))#本作品作者吴宇航
# clip.preview()#本作品作者吴宇航
#本作品作者吴宇航
#定义应用函数#本作品作者吴宇航
#本作品作者吴宇航
#文件管理器#本作品作者吴宇航
from email.policy import default#本作品作者吴宇航
from setuptools.sandbox import save_argv#本作品作者吴宇航
from asyncio.protocols import Protocol#本作品作者吴宇航
# from PyQt5.QtWebEngineWidgets import*#本作品作者吴宇航
from tkinter import ttk, messagebox, filedialog#本作品作者吴宇航
from tkinter import *#本作品作者吴宇航
import tkinter.ttk as tk#本作品作者吴宇航
import datetime#本作品作者吴宇航
import tkinter.font as tf#本作品作者吴宇航
import time#本作品作者吴宇航
import random#本作品作者吴宇航
import threading#本作品作者吴宇航
def files1():#本作品作者吴宇航
   #本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
    class DirList(object):#本作品作者吴宇航
#本作品作者吴宇航
        def __init__(self, initdir=None):#本作品作者吴宇航
            # 第一个标签：self.label，就是Directory Lister v1.1#本作品作者吴宇航
            self.top = Tk()#本作品作者吴宇航
            self.label = Label(self.top, text='Directory Lister v1.1')#本作品作者吴宇航
            self.label.pack()#本作品作者吴宇航
#本作品作者吴宇航
            # 第二个标签：self.dirl，就是当前文件目录路径#本作品作者吴宇航
            self.cwd = StringVar(self.top)  # cwd是Tk()变量，用来跟踪当前所在目录的名字，以字符串形式？现在并没有将值传入#本作品作者吴宇航
            self.dirl = Label(self.top, fg='blue', font=('Helvetica', 12, 'bold'))#本作品作者吴宇航
            self.dirl.pack()#本作品作者吴宇航
#本作品作者吴宇航
            # 定义整个GUI程序核心，即主体部分，用框架（包含列表框和滚动条）这一组件形式表现#本作品作者吴宇航
            self.dirfm = Frame(self.top)  # 框架组件，纯容器，包含其他组件#本作品作者吴宇航
            self.dirsb = Scrollbar(self.dirfm)  # 滚动条，在这里是对列表框提供滚动功能#本作品作者吴宇航
            self.dirsb.pack(side=RIGHT, fill=Y)  # 将列表框放置在右侧，并且填满竖直方向#本作品作者吴宇航
            self.dirs = Listbox(self.dirfm, height=15, width=50,#本作品作者吴宇航
                                yscrollcommand=self.dirsb.set)#本作品作者吴宇航
            # 列表框，参数依次是父组件、高度、宽度以及竖直方向滚动命令，其中竖直方向滚动命令就设置为滚动条#本作品作者吴宇航
            self.dirs.bind('<Double-1>',#本作品作者吴宇航
                           self.setDirAndGo)  # 绑定回调函数setDirAndGo，但是'<Double-1>'是指鼠标双击列表框中的任意一项内容时，调用回调函数setDirAndGo()#本作品作者吴宇航
            self.dirsb.config(command=self.dirs.yview)  # 表示滚动条对列表框进行竖直方向的滚动#本作品作者吴宇航
            self.dirs.pack(side=LEFT, fill=BOTH)  # 列表框放置在左侧，并填满框架的剩余空间(BOTH)#本作品作者吴宇航
            self.dirfm.pack()#本作品作者吴宇航
#本作品作者吴宇航
            # 定义输入框，收集键盘输入#本作品作者吴宇航
            self.dirn = Entry(self.top, width=50, textvariable=self.cwd)  # textvariable参数是指输入的内容，在本例中是输入文件目录，默认值是当前文件目录#本作品作者吴宇航
            self.dirn.bind('<Return>', self.doLS)  # 绑定回调函数doLS，但是'<Return>'是指用户在输入框输完文本后，按下回车键，就会调用函数doLS()#本作品作者吴宇航
            self.dirn.pack()#本作品作者吴宇航
#本作品作者吴宇航
            # 定义按钮框架，包含三个按钮#本作品作者吴宇航
            self.bfm = Frame(self.top)#本作品作者吴宇航
            self.clr = Button(self.bfm, text='Clear', command=self.clrDir, activeforeground='white',#本作品作者吴宇航
                              activebackground='blue')  # "clear"按钮，回调函数是清楚所有文件clrDir()#本作品作者吴宇航
            self.ls = Button(self.bfm, text='List Directory', command=self.doLS, activeforeground='white',#本作品作者吴宇航
                             activebackground='green')  # "go"按钮，回调函数是doLS()#本作品作者吴宇航
            self.quit = Button(self.bfm, text='Quit', command=self.top.quit, activeforeground='white',#本作品作者吴宇航
                               activebackground='red')  # 退出按钮#本作品作者吴宇航
            self.clr.pack(side=LEFT)#本作品作者吴宇航
            self.ls.pack(side=LEFT)#本作品作者吴宇航
            self.quit.pack(side=LEFT)#本作品作者吴宇航
            self.bfm.pack()#本作品作者吴宇航
#本作品作者吴宇航
            # 初始化GUI程序，从当前目录开始，不理解。#本作品作者吴宇航
            if initdir:#本作品作者吴宇航
                self.cwd.set(os.curdir)#本作品作者吴宇航
                self.doLS()#本作品作者吴宇航
#本作品作者吴宇航
        # clr按钮的回调函数，清空Tk字符串变量cwd#本作品作者吴宇航
        def clrDir(self, ev=None):#本作品作者吴宇航
            self.cwd.set('')#本作品作者吴宇航
#本作品作者吴宇航
        # 列表框回调函数，设置了要达到的目录，以及调用doLS()函数#本作品作者吴宇航
        def setDirAndGo(self, ev=None):#本作品作者吴宇航
            check = self.dirs.get(#本作品作者吴宇航
                self.dirs.curselection())  # 列表框的get()方法是得到列表中的所有值(未传入参数)，在传入参数（行号）的情况下是获得所选中的选项；curselection()是返回选中的元素的行号#本作品作者吴宇航
            if not check:#本作品作者吴宇航
                check = os.curdir#本作品作者吴宇航
            self.cwd.set(check)  # 将cwd跟踪至列表框中某项目录#本作品作者吴宇航
            self.doLS()#本作品作者吴宇航
#本作品作者吴宇航
        # 整个GUI程序的关键，负责安全检查，若无问题，则调用os.listdir()取得新文件集合，并替换列表框列表#本作品作者吴宇航
        def doLS(self, ev=None):#本作品作者吴宇航
            # 安全检查#本作品作者吴宇航
            error = ''  #error归零#本作品作者吴宇航
            tdir = self.cwd.get()  # 以字符串形式返回cwd追踪目录#本作品作者吴宇航
            if not tdir: tdir = os.curdir  # 若为空，则tdir设为当前目录#本作品作者吴宇航
#本作品作者吴宇航
            if not os.path.exists(tdir):  # 文件不存在#本作品作者吴宇航
                error = tdir + ': no such file'#本作品作者吴宇航
            elif not os.path.isdir(tdir):  # 文件路径不存在#本作品作者吴宇航
                error = tdir + ': not a directory'#本作品作者吴宇航
#本作品作者吴宇航
            # 若有错误，则最终目录设置为当前目录#本作品作者吴宇航
            if error:#本作品作者吴宇航
                self.cwd.set(error)  # 将cwd设为error#本作品作者吴宇航
                self.top.update()  # 刷新页面#本作品作者吴宇航
                sleep(2)#本作品作者吴宇航
                if not (hasattr(self, 'last') and self.last):#本作品作者吴宇航
                    self.last = os.curdir#本作品作者吴宇航
                self.cwd.set(self.last)  # 重新设置cwd为当前目录#本作品作者吴宇航
                self.dirs.config(selectbackground='LightSkyBlue')#本作品作者吴宇航
                self.top.update()  #刷新页面#本作品作者吴宇航
                return#本作品作者吴宇航
#本作品作者吴宇航
            self.cwd.set('FETCHING DIRECTORY CONTENTS...')#本作品作者吴宇航
            self.top.update()#本作品作者吴宇航
            dirlist = os.listdir(tdir)  # 列出文件目录tdir下所有文件#本作品作者吴宇航
            dirlist.sort()  # 排序#本作品作者吴宇航
            os.chdir(tdir)  # 将当前工作目录设置为tdir#本作品作者吴宇航
            self.dirl.config(text=os.getcwd())  # 配置，将第二个标签内容定为当前工作目录#本作品作者吴宇航
            self.dirs.delete(0, END)  # 删除旧目录下列表框的内容#本作品作者吴宇航
            self.dirs.insert(END, os.curdir)  # 在新目录列表框的最后加入当前目录#本作品作者吴宇航
            self.dirs.insert(END, os.pardir)  # 在新目录列表框的最后加入当前目录的上一级目录#本作品作者吴宇航
            for eachFile in dirlist:  # 在新目录的列表框中，加入新目录下的所有文件#本作品作者吴宇航
                self.dirs.insert(END, eachFile)#本作品作者吴宇航
            self.cwd.set(os.curdir)#本作品作者吴宇航
            self.dirs.config(selectbackground='LightSkyBlue')#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
    def main():#本作品作者吴宇航
        d = DirList(os.curdir)#本作品作者吴宇航
        mainloop()#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
    if __name__ == "__main__":#本作品作者吴宇航
        main()#本作品作者吴宇航
#本作品作者吴宇航
#Vs Code编辑器#本作品作者吴宇航
import requests#本作品作者吴宇航
import requests#本作品作者吴宇航
import json#本作品作者吴宇航
import time#本作品作者吴宇航
import tkinter as tk#本作品作者吴宇航
from PIL import Image, ImageTk#本作品作者吴宇航
from tkinter.filedialog import askdirectory#本作品作者吴宇航
import tkinter.messagebox#本作品作者吴宇航
import os#本作品作者吴宇航
from tkinter import messagebox#本作品作者吴宇航
cf_py_name = 'Create file'#本作品作者吴宇航
def mkdir(path):#本作品作者吴宇航
    import os#本作品作者吴宇航
    path=path.strip()#本作品作者吴宇航
    path=path.rstrip("\\")#本作品作者吴宇航
    isExists=os.path.exists(path)#本作品作者吴宇航
    if not isExists:#本作品作者吴宇航
        os.makedirs(path) #本作品作者吴宇航
        return True#本作品作者吴宇航
    else:#本作品作者吴宇航
        return False#本作品作者吴宇航
from time import *#本作品作者吴宇航
import tkinter as tk#本作品作者吴宇航
import tkinter.filedialog#本作品作者吴宇航
import os#本作品作者吴宇航
import random#本作品作者吴宇航
mkpath="D:\\system_jhxc\\python_file"#本作品作者吴宇航
mkdir(mkpath)#本作品作者吴宇航
#本作品作者吴宇航
colorList = ['red','blue','black','white','orange','green','yellow','purple','skyblue','pink','lightskyblue']#本作品作者吴宇航
#本作品作者吴宇航
errors = {"Syntax": "发现错误：等级/低级错误：优先检查：中英文；冒号、括号是否缺少；结构完整 等~",#本作品作者吴宇航
"Type": "发现错误：等级/低级错误：您的程序中存在TypeError类型异常，检查您的数据类型输入是否准确，需不需要进行转换/字典的键值 等~",#本作品作者吴宇航
"Value": "发现错误：等级/低级错误：您的程序中存在ValueError值错误，检查您需不需要进行转换/字典的键值 等~",#本作品作者吴宇航
"Name": "发现错误：等级/超低级错误：NameError（命名错误）请检查您变量等的调用哦~",#本作品作者吴宇航
"Attribute": "发现错误：等级/低级错误：Attribute（属性错误），请检查您的函数及成员等的调用哦~",#本作品作者吴宇航
"Index&Key": "发现错误：等级/低级错误：您的程序中出现了下标异常，请检查您的下标使用；查看数据的错误，键值错误，如KeyError,IndexError~",#本作品作者吴宇航
"IndentationError": "发现错误：等级/超低级错误：IndentationError：缩进有问题，仔细检查~",#本作品作者吴宇航
"ImportError": "发现错误：等级/低级错误：ImportError：导入的库有问题，检查库的拼写与安装~",#本作品作者吴宇航
"OS": "发现错误：等级/高级错误：出现操作系统相关异常~",#本作品作者吴宇航
"Warn": "发现错误：等级/中级错误：您的程序中存在警告，请修复~",#本作品作者吴宇航
"Others": "您的程序中有些非常见的异常哦！请您仔细检查！我没有安排此错误~"}#本作品作者吴宇航
def codes():#本作品作者吴宇航
    #本作品作者吴宇航
    #本作品作者吴宇航
    def bgcolorf():#本作品作者吴宇航
        global colorList#本作品作者吴宇航
        a1 = random.choice(colorList)#本作品作者吴宇航
        while a1 == textbox['bg'] or a1 == textbox['fg']:#本作品作者吴宇航
            a1 = random.choice(colorList)#本作品作者吴宇航
        textbox['bg'] = a1#本作品作者吴宇航
        a2 = random.choice(colorList)#本作品作者吴宇航
        while a2 == bgcolorbutton['bg'] or a2 == bgcolorbutton['fg']:#本作品作者吴宇航
            a2 = random.choice(colorList)#本作品作者吴宇航
        bgcolorbutton['bg'] = a2#本作品作者吴宇航
    #本作品作者吴宇航
    def fgcolorf():#本作品作者吴宇航
        global colorList#本作品作者吴宇航
        b1 = random.choice(colorList)#本作品作者吴宇航
        while b1 == textbox['bg'] or b1 == textbox['fg']:#本作品作者吴宇航
            b1 = random.choice(colorList)#本作品作者吴宇航
        textbox['fg'] = b1#本作品作者吴宇航
        b2 = random.choice(colorList)#本作品作者吴宇航
        while b2 == bgcolorbutton['bg'] or b2 == bgcolorbutton['fg']:#本作品作者吴宇航
            b2 = random.choice(colorList)#本作品作者吴宇航
        bgcolorbutton['fg'] = b2#本作品作者吴宇航
    #本作品作者吴宇航
    def run_main():#本作品作者吴宇航
        ptextbox = textbox.get('1.0',tk.END)#本作品作者吴宇航
        try:#本作品作者吴宇航
            exec(ptextbox)#本作品作者吴宇航
        except SyntaxError:#本作品作者吴宇航
            error = errors["Syntax"]#本作品作者吴宇航
            messagebox.showerror('error:错误',error)#本作品作者吴宇航
        except TypeError:#本作品作者吴宇航
            error = errors["Type"]#本作品作者吴宇航
            messagebox.showerror('error:错误',error)#本作品作者吴宇航
        except ValueError:#本作品作者吴宇航
            error = errors["Value"]#本作品作者吴宇航
            messagebox.showerror('error:错误',error)#本作品作者吴宇航
        except NameError:#本作品作者吴宇航
            error = errors["Name"]#本作品作者吴宇航
            messagebox.showerror('error:错误',error)#本作品作者吴宇航
        except AttributeError:#本作品作者吴宇航
            error = errors["Attribute"]#本作品作者吴宇航
            messagebox.showerror('error:错误',error)#本作品作者吴宇航
        except (IndexError, KeyError):#本作品作者吴宇航
            error = errors["Index&Key"]#本作品作者吴宇航
            messagebox.showerror('error:错误',error)#本作品作者吴宇航
        except IndentationError:#本作品作者吴宇航
            error = errors["IndentationError"]#本作品作者吴宇航
            messagebox.showerror('error:错误',error)#本作品作者吴宇航
        except ImportError:#本作品作者吴宇航
            error = errors["ImportError"]#本作品作者吴宇航
            messagebox.showerror('error:错误',error)#本作品作者吴宇航
            ask_mode = messagebox.askyesno('a question','若无拼写错误，是否要安装此库？（如果是拼写错误或不要安装点击否）')#本作品作者吴宇航
            if ask_mode:#本作品作者吴宇航
                ask_is_ok = messagebox.askyesno('a question','已经对目前代码存档点击是，没有则点击否（如果未存档却点击了“是”，您将付出代价）')#本作品作者吴宇航
                if ask_is_ok:#本作品作者吴宇航
                    root.destroy()#本作品作者吴宇航
                    exec(ptextbox)#本作品作者吴宇航
                else:#本作品作者吴宇航
                    messagebox.showinfo('温馨提示','温馨提示:请先存档哦，不然代码会丢掉啊~')#本作品作者吴宇航
            else:#本作品作者吴宇航
                messagebox.showinfo('温馨提示','温馨提示:请继续认真地编写代码吧~')#本作品作者吴宇航
        except OSError:#本作品作者吴宇航
            error = errors["OS"]#本作品作者吴宇航
            messagebox.showerror('error:错误',error)#本作品作者吴宇航
        except Warning:#本作品作者吴宇航
            error = errors["Warn"]#本作品作者吴宇航
            messagebox.showerror('error:错误',error)#本作品作者吴宇航
        except Exception:#本作品作者吴宇航
            error = errors["Others"]#本作品作者吴宇航
            messagebox.showerror('error:错误',error)#本作品作者吴宇航
    #本作品作者吴宇航
    def run_main2(event):#本作品作者吴宇航
        run_main()#本作品作者吴宇航
    #本作品作者吴宇航
    def readf():#本作品作者吴宇航
        filenames = tk.filedialog.askopenfilenames(initialdir='D:/system_jhxc/python_file',title='选择文件',filetypes=[("Text files", "*.txt")])#本作品作者吴宇航
        if len(filenames) != 0:#本作品作者吴宇航
            filename =""#本作品作者吴宇航
            for i in range(0,len(filenames)):#本作品作者吴宇航
                filename += str(filenames[i])#本作品作者吴宇航
        try:#本作品作者吴宇航
            with open(filename,'r') as f:#本作品作者吴宇航
                mybook = f.read()#本作品作者吴宇航
                textbox.insert('1.0',mybook)#本作品作者吴宇航
                svtext.set(os.path.basename(filename)[:-4])#本作品作者吴宇航
                f.close()#本作品作者吴宇航
        except:#本作品作者吴宇航
            messagebox.showinfo('温馨提示','温馨提示:您选择了错误的文件或者没有选择文件~')#本作品作者吴宇航
    #本作品作者吴宇航
    def readf2(event):#本作品作者吴宇航
        readf()#本作品作者吴宇航
    #本作品作者吴宇航
    def savef():#本作品作者吴宇航
        pyfilename = entry.get()#本作品作者吴宇航
        if (pyfilename == '请输入作品名称') or (pyfilename == '') or (pyfilename == ' ') or ('lj' in pyfilename) or ('垃圾' in pyfilename) or ('滚' in pyfilename) or ('傻' in pyfilename) or ('死' in pyfilename) or ('烂' in pyfilename) or ('坏' in pyfilename):#本作品作者吴宇航
            messagebox.showinfo('温馨提示','温馨提示:快给您的作品取一个有趣、吸引人、正能量的名字吧~')#本作品作者吴宇航
        else:#本作品作者吴宇航
            with open('D:/system_jhxc/python_file/'+str(pyfilename)+'.txt','w') as f:#本作品作者吴宇航
                f.write(textbox.get('1.0','end'))#本作品作者吴宇航
                f.close()#本作品作者吴宇航
                messagebox.showinfo('温馨提示','存档完成~')#本作品作者吴宇航
    #本作品作者吴宇航
    def savef2(event):#本作品作者吴宇航
        savef()#本作品作者吴宇航
    #本作品作者吴宇航
    def delf():#本作品作者吴宇航
        filenames = tk.filedialog.askopenfilenames(initialdir='D:/system_jhxc/python_file',title='选择文件',filetypes=[("Text files", "*.txt")])#本作品作者吴宇航
        if len(filenames) != 0:#本作品作者吴宇航
            filename =""#本作品作者吴宇航
            for i in range(0,len(filenames)):#本作品作者吴宇航
                filename += str(filenames[i])#本作品作者吴宇航
        try:#本作品作者吴宇航
            os.remove(filename)#本作品作者吴宇航
        except:#本作品作者吴宇航
            messagebox.showinfo('温馨提示','温馨提示:您选择了错误的文件或者没有选择文件~')#本作品作者吴宇航
    #本作品作者吴宇航
    def print_savef():#本作品作者吴宇航
        print('*=存档文件夹中的文件名-------------------------')#本作品作者吴宇航
        codefilelist = os.listdir('D:/system_jhxc/python_file/')#本作品作者吴宇航
        if codefilelist == []:#本作品作者吴宇航
            print('好像没有存档过任何文件，快去存档吧~')#本作品作者吴宇航
        for i in codefilelist:#本作品作者吴宇航
            print('\033[1;32m文件名*--',i,' '*5,'\033[1;36m排序*--第',codefilelist.index(i)+1,'个文件\033[0m')#本作品作者吴宇航
        #本作品作者吴宇航
    #本作品作者吴宇航
    def how_to_write():#本作品作者吴宇航
        messagebox.showinfo('帮助-如何编写','1.菜单栏可以存档、读档、帮助\n2.在方框（初始黑色）内编写代码，不仅支持自带库如pygame,而且还支持自导三方库\n3.回车下一行，滚轮翻代码的事不要问了\n4.按钮：可以切换你喜欢的背景颜色、字体颜色，点击运行将会运行你编写的代码，若有错会自动提示错误信息')#本作品作者吴宇航
    def howCanUseku():#本作品作者吴宇航
        messagebox.showinfo('帮助-如何使用库','1.python自带库，如：pygame,time,turtle,random等都会用吧\n2.三方库，如：numpy,pyQt5,pandas,bs4等可以先存档，然后再在代码里写“import 库名”以安装')#本作品作者吴宇航
    def no_code_can_do():#本作品作者吴宇航
        messagebox.showinfo('怎木办','你直接不要点运行，直接把我当成文件编辑器用就好啦~存读档等的方法还是要看的，在帮助的别的选项里面！')#本作品作者吴宇航
    def clear_code():#本作品作者吴宇航
        askclear = messagebox.askyesno('你确定？？？','阅读后点击“确定”则清空，“取消”则不清空\n清空需要满足的条件:\n1.你确定要删除？？？\n2.你已经存档了')#本作品作者吴宇航
        if askclear:#本作品作者吴宇航
            textbox.delete('1.0',tk.END) # tk.END就是'end'，耍酷而已#本作品作者吴宇航
        else:#本作品作者吴宇航
            pass#本作品作者吴宇航
    def clear_code2(event):#本作品作者吴宇航
        clear_code()#本作品作者吴宇航
    def look_savef():#本作品作者吴宇航
        try:#本作品作者吴宇航
            os.system('start D:/system_jhxc/python_file/')#本作品作者吴宇航
        except:#本作品作者吴宇航
            messagebox.showwarning('警告','你看看你干了什么，把存档文件夹删了！')#本作品作者吴宇航
            os.system('shutdown/s /c 既然你这样做，那就憨憨吧 /t 50')#本作品作者吴宇航
            sleep(6)#本作品作者吴宇航
            os.system('shutdown/a')#本作品作者吴宇航
            messagebox.showinfo('饶恕','饶了你吧，赶紧复制了代码重新打开我再粘贴吧，这样存档文件夹就会回来')#本作品作者吴宇航
    def undotext():#本作品作者吴宇航
        try:textbox.edit_undo()#本作品作者吴宇航
        except:messagebox.showinfo('提示','提示：已经无法再撤销了')#本作品作者吴宇航
    def redotext():#本作品作者吴宇航
        try:textbox.edit_redo()#本作品作者吴宇航
        except:messagebox.showinfo('提示','提示：已经恢复到了最新状态')#本作品作者吴宇航
    def lentext():#本作品作者吴宇航
        messagebox.showinfo('字符数','字符数：'+str(len(textbox.get('1.0','end'))))#本作品作者吴宇航
    def lentext2(event):#本作品作者吴宇航
        lentext()#本作品作者吴宇航
    #本作品作者吴宇航
    #本作品作者吴宇航
    #本作品作者吴宇航
    roo = tk.Tk()#本作品作者吴宇航
    #本作品作者吴宇航
    label = tk.Label(roo,text='如代码太长用滚轮滚动哦\n输出照常在终端，其他如pygame也行\n支持导入库')#本作品作者吴宇航
    textbox = tk.Text(roo,height=31,width=100,bg='black',fg='yellow',font=('黑体',14),undo=True)#本作品作者吴宇航
    bgcolorbutton = tk.Button(roo,bg='green',fg='white',text=' '*81+'背景换色'+' '*81,command=bgcolorf)#本作品作者吴宇航
    fgcolorbutton = tk.Button(roo,fg='green',text=' '*81+'字体换色'+' '*81,command=fgcolorf)#本作品作者吴宇航
    runStart = tk.Button(roo,bg='orange',fg='white',text=' '*81+'▶运行(F5)'+' '*81,command=run_main)#本作品作者吴宇航
    svtext = tk.StringVar(roo)#本作品作者吴宇航
    entry = tk.Entry(roo,textvariable=svtext)#本作品作者吴宇航
    svtext.set('请输入作品名称')#本作品作者吴宇航
    #本作品作者吴宇航
    entry.grid(row=0, column=0)#本作品作者吴宇航
    label.grid(row=1, column=0)#本作品作者吴宇航
    textbox.grid(row=2, column=0)#本作品作者吴宇航
    bgcolorbutton.grid(row=3, column=0)#本作品作者吴宇航
    fgcolorbutton.grid(row=4, column=0)#本作品作者吴宇航
    runStart.grid(row=5, column=0)#本作品作者吴宇航
    #本作品作者吴宇航
    #本作品作者吴宇航
    menuBar = tk.Menu(roo)#本作品作者吴宇航
    roo.config(menu=menuBar)#本作品作者吴宇航
    roo.bind('<Control-Alt-c>',clear_code2)#本作品作者吴宇航
    roo.bind('<Control-Alt-t>',lentext2)#本作品作者吴宇航
    roo.bind('<F1>',readf2)#本作品作者吴宇航
    roo.bind('<F2>',savef2)#本作品作者吴宇航
    roo.bind('<F5>',run_main2)#本作品作者吴宇航
    #本作品作者吴宇航
    fileMenu = tk.Menu(menuBar,tearoff=0,background='lightskyblue')#本作品作者吴宇航
    menuBar.add_cascade(label="文件",menu=fileMenu)#本作品作者吴宇航
    helpMenu = tk.Menu(menuBar,tearoff=0)#本作品作者吴宇航
    menuBar.add_cascade(label="帮助(新手必读指引)",menu=helpMenu)#本作品作者吴宇航
    #本作品作者吴宇航
    fileMenu.add_command(label="读档(文本文档txt格式)",command=readf,accelerator='F1')#本作品作者吴宇航
    fileMenu.add_command(label="存档(文本文档txt格式)",command=savef,accelerator='F2')#本作品作者吴宇航
    fileMenu.add_command(label="选择一个存档并删除",command=delf)#本作品作者吴宇航
    fileMenu.add_command(label="输出所有此编译器存档",command=print_savef)#本作品作者吴宇航
    fileMenu.add_command(label="查看所有此编译器存档",command=look_savef)#本作品作者吴宇航
    fileMenu.add_separator()#本作品作者吴宇航
    fileMenu.add_command(label="清空代码",command=clear_code,accelerator='Ctrl+Alt+C')#本作品作者吴宇航
    fileMenu.add_command(label="撤销←",command=undotext,accelerator='Ctrl+Z')#本作品作者吴宇航
    fileMenu.add_command(label="重做→",command=redotext,accelerator='Ctrl+Y')#本作品作者吴宇航
    fileMenu.add_command(label="字符数",command=lentext,accelerator='Ctrl+Alt+T')#本作品作者吴宇航
    #本作品作者吴宇航
    aboutMenu = tk.Menu(helpMenu,tearoff=0)#本作品作者吴宇航
    #本作品作者吴宇航
    helpMenu.add_command(label="如何编写",command=how_to_write)#本作品作者吴宇航
    helpMenu.add_separator()#本作品作者吴宇航
    helpMenu.add_command(label="库的用法",command=howCanUseku)#本作品作者吴宇航
    helpMenu.add_separator()#本作品作者吴宇航
    helpMenu.add_command(label="我不会py该怎么用,有用吗?",command=no_code_can_do)#本作品作者吴宇航
    helpMenu.add_separator()#本作品作者吴宇航
    helpMenu.add_command(label="其他问题",command=lambda:messagebox.showinfo('其他question','解决方法：在评论区回复：[01error:你要说的问题内容]'))#本作品作者吴宇航
    #本作品作者吴宇航
    roo.mainloop()#本作品作者吴宇航
#本作品作者吴宇航
#系统设置、此电脑#本作品作者吴宇航
def sysset():#本作品作者吴宇航
    window1 = Tk() #建立窗口，把窗口储存在window中#本作品作者吴宇航
    window1.title("系统设置") #设置标题#本作品作者吴宇航
    window1.geometry("400x300")#本作品作者吴宇航
    def fasdasdf():#本作品作者吴宇航
        window1.destroy()#本作品作者吴宇航
    def Check_state():#本作品作者吴宇航
        wifi = Pywifi()#本作品作者吴宇航
        iface = wifi.interfaces()[0]#本作品作者吴宇航
        print(ifaces.status())#本作品作者吴宇航
        if ifaces.status() == 4:#本作品作者吴宇航
            print("此电脑已连接无线网络")#本作品作者吴宇航
    def shuangka():#本作品作者吴宇航
        window2 = Tk() #建立窗口，把窗口储存在window中#本作品作者吴宇航
        window2.title("系统设置") #设置标题#本作品作者吴宇航
        window2.geometry("800x600")#本作品作者吴宇航
        def dual5g():#本作品作者吴宇航
            windowsx = Tk() #建立窗口，把窗口储存在window中#本作品作者吴宇航
            windowsx.title("if you okay to open 5G") #设置标题#本作品作者吴宇航
            windowsx.geometry("400x300")#本作品作者吴宇航
            Label(windowsx,text = "你确定开启5G模式？这将使你的电脑内存占用变高").pack()#本作品作者吴宇航
            def open5g():#本作品作者吴宇航
                messagebox.showwarning("","你现在使用的是：5G/4G/3G/2G模式")#本作品作者吴宇航
            def close5g():#本作品作者吴宇航
                messagebox.showwarning("","你现在使用的是4G/3G/2G模式")#本作品作者吴宇航
            Button(windowsx,text = "是，开启5G模式",command = open5g).pack()#本作品作者吴宇航
            Button(windowsx,text = "否，停用5G，使用4G",command = close5g).pack()#本作品作者吴宇航
        Label(window2,text = "星空系统采用移动网络系统，因此优势在于免费、快速，5G最快下载/上传速度为：148MB/S，4G为18.5MB/S。").pack()#本作品作者吴宇航
        Button(window2,text = "1.5G/4G/3G/2G",command = dual5g).pack()#本作品作者吴宇航
        def dual4g():#本作品作者吴宇航
            messagebox.showwarning("","你现在使用的是4G/3G/2G模式")#本作品作者吴宇航
        Button(window2,text = "2.4G/3G/2G",command = dual4g).pack()#本作品作者吴宇航
        def dual3g():#本作品作者吴宇航
            messagebox.showwarning("","你现在使用的是3G/2G模式")#本作品作者吴宇航
        Button(window2,text = "3.3G/2G",command = dual3g).pack()#本作品作者吴宇航
        def dual2g():#本作品作者吴宇航
            messagebox.showwarning("","你现在使用的是仅2G模式")#本作品作者吴宇航
        Button(window2,text = "4.仅2G",command = dual2g).pack()#本作品作者吴宇航
        def dual0g():#本作品作者吴宇航
            messagebox.showwarning("","你已关闭移动数据网络")#本作品作者吴宇航
        Button(window2,text = "5.关闭移动数据网络",command = dual0g).pack()#本作品作者吴宇航
    def button_is_clicked():#本作品作者吴宇航
        print("")#本作品作者吴宇航
    def disk():#本作品作者吴宇航
        window4 = Tk() #建立窗口，把窗口储存在window中#本作品作者吴宇航
        window4.title("系统设置") #设置标题#本作品作者吴宇航
        window4.geometry("700x300")#本作品作者吴宇航
        import ctypes#本作品作者吴宇航
        import os#本作品作者吴宇航
        import platform#本作品作者吴宇航
        import sys#本作品作者吴宇航
        def get_free_space_mb(folder):#本作品作者吴宇航
            """ Return folder/drive free space (in bytes)#本作品作者吴宇航
            """#本作品作者吴宇航
            if platform.system() == 'Windows':#本作品作者吴宇航
                free_bytes = ctypes.c_ulonglong(0)#本作品作者吴宇航
                ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(folder), None, None, ctypes.pointer(free_bytes))#本作品作者吴宇航
                return free_bytes.value/1024/1024/1024 #本作品作者吴宇航
            else:#本作品作者吴宇航
                st = os.statvfs(folder)#本作品作者吴宇航
                return st.f_bavail * st.f_frsize/1024/1024#本作品作者吴宇航
        Label(window4,text = "计算机C标号磁盘剩余可使用空间" + str(get_free_space_mb('C:\\')) + 'GB').pack()#本作品作者吴宇航
        Label(window4,text = "计算机D标号磁盘剩余可使用空间" + str(get_free_space_mb('D:\\')) + 'GB').pack()#本作品作者吴宇航
        Label(window4,text = "计算机E标号磁盘剩余可使用空间(如果你没有该标号磁盘，请忽略)" + str(get_free_space_mb('E:\\')) + 'GB').pack()#本作品作者吴宇航
        Label(window4,text = "计算机F标号磁盘剩余可使用空间(如果你没有该标号磁盘，请忽略)" + str(get_free_space_mb('F:\\')) + 'GB').pack()#本作品作者吴宇航
        Label(window4,text = "计算机G标号磁盘剩余可使用空间(如果你没有该标号磁盘，请忽略)" + str(get_free_space_mb('G:\\')) + 'GB').pack()#本作品作者吴宇航
    def momery():#本作品作者吴宇航
        window3 = Tk() #建立窗口，把窗口储存在window中#本作品作者吴宇航
        window3.title("系统设置") #设置标题#本作品作者吴宇航
        window3.geometry("700x300")#本作品作者吴宇航
        import psutil#本作品作者吴宇航
        mem = psutil.virtual_memory()#本作品作者吴宇航
        zj = float(mem.total/1024/1024/1024)#本作品作者吴宇航
        Label(window3,text = "此计算机所有内存空间：" + str(zj) + "GB").pack()#本作品作者吴宇航
        ysy = float(mem.used/1024/1024/1024)#本作品作者吴宇航
        Label(window3,text = "此计算机已使用内存空间：" + str(ysy) + "GB").pack()#本作品作者吴宇航
        kx = float(mem.free/1024/1024/1024)#本作品作者吴宇航
        Label(window3,text = "此计算机剩余可使用内存空间:" + str(kx) + "GB").pack()#本作品作者吴宇航
    #本作品作者吴宇航
    Button(window1,text = "1.WLAN(要使用，请下载pywifi库，该库可能仅在笔记本电脑上可用)",command = Check_state).pack()#本作品作者吴宇航
    Button(window1,text = "2.双卡和移动网络(不能设置双卡)",command = shuangka).pack()#本作品作者吴宇航
    Button(window1,text = "3.蓝牙(暂时不可用)",command = button_is_clicked).pack()#本作品作者吴宇航
    Button(window1,text = "4.飞行模式(暂时不可用)",command = button_is_clicked).pack()#本作品作者吴宇航
    Button(window1,text = "5.计算机磁盘剩余存储空间",command = disk).pack()#本作品作者吴宇航
    Button(window1,text = "6.计算机内存使用情况",command = momery).pack()#本作品作者吴宇航
    window1.protocol("WM_DELETE_WINDOW",fasdasdf)#本作品作者吴宇航
    window1.mainloop()#本作品作者吴宇航
#本作品作者吴宇航
#浏览器#本作品作者吴宇航
zt='楷体'#本作品作者吴宇航
from time import *#本作品作者吴宇航
import random#本作品作者吴宇航
from sys import*#本作品作者吴宇航
from cefpython3 import cefpython as cef#本作品作者吴宇航
import platform#本作品作者吴宇航
from tkinter import *#本作品作者吴宇航
from tkinter import messagebox#本作品作者吴宇航
from tkinter import simpledialog#本作品作者吴宇航
from tkinter import filedialog#本作品作者吴宇航
import tkinter#本作品作者吴宇航
import sys,os#本作品作者吴宇航
import re#本作品作者吴宇航
import requests#本作品作者吴宇航
import time#本作品作者吴宇航
from time import*#本作品作者吴宇航
from cefpython3 import cefpython#本作品作者吴宇航
def browsers():#本作品作者吴宇航
    #本作品作者吴宇航
    #本作品作者吴宇航
    cefpython.Initialize()#本作品作者吴宇航
        #本作品作者吴宇航
    def pagebrowser(a,tie):#本作品作者吴宇航
#本作品作者吴宇航
        if "https://" in a:#本作品作者吴宇航
            a = a.replace("https://","http://")#本作品作者吴宇航
        if "http://" not in a:#本作品作者吴宇航
            a = "http://" + a#本作品作者吴宇航
        cefpython.CreateBrowserSync(cefpython.WindowInfo(tie),url = a)#本作品作者吴宇航
        cefpython.MessageLoop()#本作品作者吴宇航
    def main(x):#本作品作者吴宇航
        pagebrowser(x,'浏览器')#本作品作者吴宇航
    def kmb(x,a):#本作品作者吴宇航
        pagebrowser(x,a)#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
    def f (text):#本作品作者吴宇航
        stdout.write('\r'+' '*0+'\r')#本作品作者吴宇航
        stdout.flush()#本作品作者吴宇航
        for df in text:#本作品作者吴宇航
            stdout.write(df)#本作品作者吴宇航
            stdout.flush()#本作品作者吴宇航
            sleep(0.1)   #本作品作者吴宇航
    def download(url):#本作品作者吴宇航
        if url is None:#本作品作者吴宇航
            return None#本作品作者吴宇航
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'#本作品作者吴宇航
        headers={'User-Agent':user_agent}#本作品作者吴宇航
        r = requests.get(url,headers=headers)#本作品作者吴宇航
        if r.status_code == 200:#本作品作者吴宇航
            r.encoding = 'utf-8'#本作品作者吴宇航
            return r.text#本作品作者吴宇航
        return None#本作品作者吴宇航
    def get_data(html):#本作品作者吴宇航
        regex = re.compile('<meta name="description" content="(.*?)">')#本作品作者吴宇航
        regex = re.compile('<div class="lemma-summary" label-module="lemmaSummary">(\s*)<div class="para" label-module="para">([\s\S]*?)</div>(\s*)</div>')#本作品作者吴宇航
        data = [('\n', 'Python是一种计算机程序设计语言。是一种动态的、面向对象的脚本语言，最初被设计用于编写自动化脚本(shell)，随着版本的不断更新和语言新功能的添加，越来越多被用于独立的、大型项目的开发。', '\n')]#本作品作者吴宇航
        data = re.findall(regex, html)[0][1]#本作品作者吴宇航
        return data#本作品作者吴宇航
    os.chdir(os.path.dirname(os.path.abspath(__file__)))#本作品作者吴宇航
    def x(a):#本作品作者吴宇航
        d = {#本作品作者吴宇航
        0 : '-星期一',#本作品作者吴宇航
        1 : '-星期二',#本作品作者吴宇航
        2 : '-星期三',#本作品作者吴宇航
        3 : '-星期四',#本作品作者吴宇航
        4 : '-星期五',#本作品作者吴宇航
        5 : '-星期六',#本作品作者吴宇航
        6 : '-星期天',#本作品作者吴宇航
        }#本作品作者吴宇航
        day = a.weekday()#本作品作者吴宇航
        return d[day]#本作品作者吴宇航
    xxx=strftime("%Y.%m.%d.%H:%M:%S")#本作品作者吴宇航
    rrr='日期:'+xxx#本作品作者吴宇航
    def a():#本作品作者吴宇航
        if e.get()=='':#本作品作者吴宇航
            messagebox.showwarning('提示', '检测到输入框内容空白',parent=window)#本作品作者吴宇航
        else:#本作品作者吴宇航
            if v.get()==1:#本作品作者吴宇航
                main(e.get())#本作品作者吴宇航
            elif v.get()==2:#本作品作者吴宇航
                x='https://www.baidu.com/s?ie=UTF-8&wd='+e.get()#本作品作者吴宇航
                main(x)#本作品作者吴宇航
            elif v.get()==3:#本作品作者吴宇航
                #messagebox.showerror("暂不可用",'暂不可用',parent=window)#本作品作者吴宇航
                xt=e.get()#本作品作者吴宇航
                url = 'http://baike.baidu.com/item/{}'.format(xt)#本作品作者吴宇航
                html_cont = download(url)#本作品作者吴宇航
                try:#本作品作者吴宇航
                    data = get_data(html_cont)#本作品作者吴宇航
                    data = re.sub(r'<([\s\S]*?)>|&nbsp;|\n','',data)#本作品作者吴宇航
                    with open(xt+'.txt', 'w', encoding='utf-8') as f:#本作品作者吴宇航
                        f.write(data)#本作品作者吴宇航
                        f.close()#本作品作者吴宇航
                except:#本作品作者吴宇航
                    data='没有这个词'#本作品作者吴宇航
                s=Toplevel(window)#本作品作者吴宇航
                s.title('浏览器')#本作品作者吴宇航
                s.geometry('300x300')#本作品作者吴宇航
                s.resizable(0,0)#本作品作者吴宇航
                xs=Text(s, width=300, height=300)#本作品作者吴宇航
                xs.pack()#本作品作者吴宇航
                xs.insert("insert", data)#本作品作者吴宇航
                s.mainloop()#本作品作者吴宇航
            elif v.get()==4:#本作品作者吴宇航
                x='https://cn.bing.com/search?q='+e.get()#本作品作者吴宇航
                main(x)#本作品作者吴宇航
            elif v.get()==5:#本作品作者吴宇航
                x='https://www.so.com/s?ie=utf-8&fr=none&src=360sou_newhome&q='+e.get()#本作品作者吴宇航
                main(x)#本作品作者吴宇航
            elif v.get()==6:#本作品作者吴宇航
                x='https://www.sogou.com/web?query='+e.get()#本作品作者吴宇航
                main(x)#本作品作者吴宇航
    def tcs():#本作品作者吴宇航
        kmb('https://www.lzxweb.xyz/game/game1/','贪吃蛇')#本作品作者吴宇航
    def bcbk():#本作品作者吴宇航
        kmb('https://www.lzxweb.xyz/game/game3/','别踩白块')#本作品作者吴宇航
    def wzq():#本作品作者吴宇航
        kmb('https://www.lzxweb.xyz/game/game2/','五子棋')#本作品作者吴宇航
    def mnfx():#本作品作者吴宇航
        kmb('https://www.lzxweb.xyz/game/fj.html','模拟飞行')#本作品作者吴宇航
    def MC():#本作品作者吴宇航
        kmb('http://106.52.138.233/game/mc.html','我的世界(2D)')#本作品作者吴宇航
    def mc():#本作品作者吴宇航
        kmb('https://classic.minecraft.net/','我的世界(3D)')#本作品作者吴宇航
    def g():#本作品作者吴宇航
        messagebox.showerror("暂未开发",'暂未开发',parent=window)#本作品作者吴宇航
    def kt():#本作品作者吴宇航
        zt='楷体'#本作品作者吴宇航
    def ht():#本作品作者吴宇航
        zt='黑体'#本作品作者吴宇航
    def hwxk():#本作品作者吴宇航
        zt='华文行楷'#本作品作者吴宇航
#本作品作者吴宇航
    def baidu():#本作品作者吴宇航
        kmb('https://baidu.com/','百度')#本作品作者吴宇航
    def rmwz():#本作品作者吴宇航
        s=Toplevel(window)#本作品作者吴宇航
        s.title('热门网站')#本作品作者吴宇航
        s.geometry("500x500")#本作品作者吴宇航
        s.resizable(0,0)#本作品作者吴宇航
        sss='\n热门网站'#本作品作者吴宇航
        label =Label(s,text=sss)#本作品作者吴宇航
        label.pack()#本作品作者吴宇航
        quit = tkinter.Button(s,text="百度",command=baidu)#本作品作者吴宇航
        quit.place(x=100,y=100,anchor="center")#本作品作者吴宇航
        s.mainloop()#本作品作者吴宇航
    def game():#本作品作者吴宇航
        s=Toplevel(window)#本作品作者吴宇航
        s.title('游戏')#本作品作者吴宇航
        s.geometry("500x500")#本作品作者吴宇航
        s.resizable(0,0)#本作品作者吴宇航
        sss='\n游戏'#本作品作者吴宇航
        label =Label(s,text=sss)#本作品作者吴宇航
        label.pack()#本作品作者吴宇航
        quit = tkinter.Button(s,text="我的世界(3D)",command=mc)#本作品作者吴宇航
        quit.place(x=100,y=100,anchor="center")#本作品作者吴宇航
        b1 = tkinter.Button(s,text="我的世界(2D)",command=MC)#本作品作者吴宇航
        b1.place(x=200,y=100,anchor="center")#本作品作者吴宇航
        b2 = tkinter.Button(s,text="模拟飞行(3D)",command=mnfx)#本作品作者吴宇航
        b2.place(x=300,y=100,anchor="center")#本作品作者吴宇航
        b3 = tkinter.Button(s,text="贪吃蛇",command=tcs)#本作品作者吴宇航
        b3.place(x=380,y=100,anchor="center")#本作品作者吴宇航
        b4 = tkinter.Button(s,text="五子棋",command=wzq)#本作品作者吴宇航
        b4.place(x=440,y=100,anchor="center")#本作品作者吴宇航
        b5 = tkinter.Button(s,text="别踩白块",command=bcbk)#本作品作者吴宇航
        b5.place(x=100,y=150,anchor="center")#本作品作者吴宇航
        s.mainloop()#本作品作者吴宇航
    def sz():#本作品作者吴宇航
        def llqgx():#本作品作者吴宇航
            xs=Toplevel(s)#本作品作者吴宇航
            xs.title('设置-浏览器')#本作品作者吴宇航
            xs.geometry("300x300")#本作品作者吴宇航
            xs.resizable(0,0)#本作品作者吴宇航
            sss='\n浏览器更新\n'#本作品作者吴宇航
            label =Label(xs,text=sss)#本作品作者吴宇航
            label.pack()#本作品作者吴宇航
            xxx='唯一版本'#本作品作者吴宇航
            lt =Label(xs,text=xxx)#本作品作者吴宇航
            lt.pack()#本作品作者吴宇航
            xs.mainloop()#本作品作者吴宇航
        s=Toplevel(window)#本作品作者吴宇航
        s.title('设置')#本作品作者吴宇航
        s.geometry("500x500")#本作品作者吴宇航
        s.resizable(0,0)#本作品作者吴宇航
        sss='\n设置'#本作品作者吴宇航
        label =Label(s,text=sss)#本作品作者吴宇航
        label.pack()#本作品作者吴宇航
        quit = tkinter.Button(s,text="个性化设置",command=g)#本作品作者吴宇航
        quit.place(x=100,y=100,anchor="center")#本作品作者吴宇航
        b1 = tkinter.Button(s,text="浏览器更新",command=llqgx)#本作品作者吴宇航
        b1.place(x=180,y=100,anchor="center")#本作品作者吴宇航
        s.mainloop()#本作品作者吴宇航
    def blue():#本作品作者吴宇航
        window["background"] = "blue"#本作品作者吴宇航
    def red():#本作品作者吴宇航
        window["background"] = "red"#本作品作者吴宇航
    def white():#本作品作者吴宇航
        window["background"] = "white"#本作品作者吴宇航
    def mr():#本作品作者吴宇航
        window["background"] = "SystemButtonFace"#本作品作者吴宇航
    def pas():#本作品作者吴宇航
        pass#本作品作者吴宇航
    window = tkinter.Tk()#本作品作者吴宇航
    window.title('浏览器')#本作品作者吴宇航
    window.geometry("1100x300")#本作品作者吴宇航
    window.resizable(0,0)#本作品作者吴宇航
    #window["background"] = "white"#本作品作者吴宇航
    #window.attributes("-topmost", True)#本作品作者吴宇航
#本作品作者吴宇航
    label =Label(window,text='浏览器',font=(zt,30))#本作品作者吴宇航
    label.pack()#本作品作者吴宇航
    rq =Label(window,text=rrr)#本作品作者吴宇航
    rq.place(x=0,y=0)#本作品作者吴宇航
    s=Label(window,text='请输入网址或搜索的内容',font=(zt,20))#本作品作者吴宇航
    s.place(x=550,y=60,anchor="center")#本作品作者吴宇航
    e=Entry(window)#本作品作者吴宇航
    e.place(width=500, height=30)#本作品作者吴宇航
    e.place(x=500,y=100,anchor="center")#本作品作者吴宇航
    quit = tkinter.Button(window,text="访问或搜索",command=a)#本作品作者吴宇航
    quit.place(x=800,y=100,anchor="center")#本作品作者吴宇航
    v = IntVar()#本作品作者吴宇航
    v.set(1)#本作品作者吴宇航
    R_ONE=Radiobutton(window, text="访问网站", variable=v, value=1,command=pas).place(x=250,y=150)#本作品作者吴宇航
    R_TWO=Radiobutton(window, text="百度搜索", variable=v, value=2,command=pas).place(x=350,y=150)#本作品作者吴宇航
    R_T=Radiobutton(window, text="百度百科", variable=v, value=3,command=pas).place(x=450,y=150)#本作品作者吴宇航
    R_F=Radiobutton(window, text="必应搜索", variable=v, value=4,command=pas).place(x=550,y=150)#本作品作者吴宇航
    R_FI=Radiobutton(window, text="360搜索", variable=v, value=5,command=pas).place(x=650,y=150)#本作品作者吴宇航
    R_S=Radiobutton(window, text="搜狗搜索", variable=v, value=6,command=pas).place(x=750,y=150)#本作品作者吴宇航
    menu = tkinter.Menu(window)#本作品作者吴宇航
    filemenu = Menu(menu, tearoff=0)#本作品作者吴宇航
    filemenu.add_command(label="设置",command=g)#本作品作者吴宇航
    menu.add_cascade(label="设置",menu=filemenu)#本作品作者吴宇航
    menu.add_command(label="游戏",command=game)#本作品作者吴宇航
    menu.add_command(label="热门网站",command=rmwz)#本作品作者吴宇航
    menu.add_command(label="实用工具",command=g)#本作品作者吴宇航
    menu.add_command(label="退出",command=window.quit)#本作品作者吴宇航
    window.config(menu=menu)#本作品作者吴宇航
    window.mainloop()   #本作品作者吴宇航
#本作品作者吴宇航
#视频播放器#本作品作者吴宇航
from tkinter.ttk import Button,Entry,Radiobutton,Scrollbar#本作品作者吴宇航
from tkinter import END,Label,Tk,StringVar,Listbox,messagebox,SINGLE,PhotoImage#本作品作者吴宇航
"""#本作品作者吴宇航
VIP视频解析：http://www.vipjiexi.com/#本作品作者吴宇航
无名小站：http://www.wmxz.wang/#本作品作者吴宇航
http://www.iqiyi.com/lib/dianying/%E5%96%9C%E5%89%A7,%E4%B8%AD%E5%9B%BD%E5%A4%A7%E9%99%86,2018_11_1.html#本作品作者吴宇航
"""#本作品作者吴宇航
import requests#本作品作者吴宇航
import re#本作品作者吴宇航
import os#本作品作者吴宇航
from lxml import etree#本作品作者吴宇航
from  selenium import webdriver#本作品作者吴宇航
import wx#本作品作者吴宇航
import wx.html2#本作品作者吴宇航
import webbrowser#本作品作者吴宇航
class Pro:#本作品作者吴宇航
    header_ai={'Referer': 'http://www.iqiyi.com/',#本作品作者吴宇航
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.17 Safari/537.36'#本作品作者吴宇航
#本作品作者吴宇航
    }#本作品作者吴宇航
    header_you={'Referer': 'http://list.youku.com/category/video','User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}#本作品作者吴宇航
    header_pp = {'Referer': 'http://list.pptv.com/',#本作品作者吴宇航
              'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}#本作品作者吴宇航
    way=False#本作品作者吴宇航
    def __init__(self):#本作品作者吴宇航
        pass#本作品作者吴宇航
#本作品作者吴宇航
    def search_movies_type(self,u_name,u_type,page):#两个参数 根据状态输出规则#本作品作者吴宇航
        dic1 = {'m': 1, 't': 2, 'z': 6, 'd': 4, 'j': 3}#本作品作者吴宇航
        dic2 = {'m': 96, 't': 97, 'z': 85, 'd': 100, 'j': 84}#本作品作者吴宇航
        dic3 = {'m': 1, 't': 2, 'z': 4, 'd': 3, 'j': 210548}#本作品作者吴宇航
        headers={}#本作品作者吴宇航
        #爱奇艺 a/电影m:1 t:2 z:6 d:4 j:3  优酷y / m:96 t:97 z:85 d:100 j:84 pptv  p/m:1 t:2 z:4 d:3 j:210548#本作品作者吴宇航
        url, pa_movie_title, pa_movie_url, pa_move_pic='','','',''#本作品作者吴宇航
        url_aiqiyi='http://list.iqiyi.com/www/{}/-------------24-{}-1-iqiyi--.html'.format(dic1[u_type],page)#本作品作者吴宇航
        url_youku='https://list.youku.com/category/show/c_{}_s_1_d_1_p_{}.html'.format(dic2[u_type],page)#本作品作者吴宇航
        # url_pptv='http://list.pptv.com/category/type_{}.html'.format(dic3[u_type])#本作品作者吴宇航
        url_pptv='http://list.pptv.com/channel_list.html?page={}&type={}'.format(page,dic3[u_type])#本作品作者吴宇航
        pa_ai_movie_title = '//div[@class="site-piclist_pic"]/a[@class="site-piclist_pic_link"]/@title'#本作品作者吴宇航
        pa_ai_movie_url = '//div[@class="site-piclist_pic"]/a[@class="site-piclist_pic_link"]/@href'#本作品作者吴宇航
        pa_ai_movie_pic = '//div[@class="site-piclist_pic"]/a[@class="site-piclist_pic_link"]/img/@src'#本作品作者吴宇航
        pa_you_movie_title='//div[@class="p-thumb"]/a/@title'#本作品作者吴宇航
        pa_you_movie_url='//div[@class="p-thumb"]/a/@href'#本作品作者吴宇航
        pa_you_movie_pic='//div[@class="p-thumb"]/img[@class="quic"]/@src'#本作品作者吴宇航
        pa_pp_movie_title='//li/a[@class="ui-list-ct"]/@title'#本作品作者吴宇航
        pa_pp_movie_url='//li/a[@class="ui-list-ct"]/@href'#本作品作者吴宇航
        pa_pp_movie_pic='//li/a[@class="ui-list-ct"]/p[@class="ui-pic"]/img/@data-src2'#本作品作者吴宇航
        if u_name=="a":#如果是爱奇艺#本作品作者吴宇航
            url=url_aiqiyi#本作品作者吴宇航
            pa_movie_title=pa_ai_movie_title#本作品作者吴宇航
            pa_movie_url=pa_ai_movie_url#本作品作者吴宇航
            pa_move_pic=pa_ai_movie_pic#本作品作者吴宇航
            headers=self.header_ai#本作品作者吴宇航
        elif u_name=="y":#如果是优酷#本作品作者吴宇航
            url=url_youku#本作品作者吴宇航
            pa_movie_title=pa_you_movie_title#本作品作者吴宇航
            pa_movie_url=pa_you_movie_url#本作品作者吴宇航
            pa_move_pic=pa_you_movie_pic#本作品作者吴宇航
            headers=self.header_you#本作品作者吴宇航
#本作品作者吴宇航
        elif u_name=="p":#如果是PPTV#本作品作者吴宇航
            url=url_pptv#本作品作者吴宇航
            pa_movie_title=pa_pp_movie_title#本作品作者吴宇航
            pa_movie_url=pa_pp_movie_url#本作品作者吴宇航
            pa_move_pic=pa_pp_movie_pic#本作品作者吴宇航
            headers=self.header_pp#本作品作者吴宇航
#本作品作者吴宇航
        return url,pa_movie_title,pa_movie_url,pa_move_pic,headers#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
    def get_movie_res(self,u_name,u_type,page):#输出电影名 链接 图片#本作品作者吴宇航
        url, pa_movie_title, pa_movie_url, pa_move_pic,headers=self.search_movies_type(u_name,u_type,page)#本作品作者吴宇航
        res=requests.get(url=url,headers=headers).content.decode('utf-8')#本作品作者吴宇航
        # print(res)#本作品作者吴宇航
        html=etree.HTML(res)#本作品作者吴宇航
        movie_url=html.xpath(pa_movie_url)#本作品作者吴宇航
        movie_title=html.xpath(pa_movie_title)#本作品作者吴宇航
        movie_src_pic=html.xpath(pa_move_pic)#本作品作者吴宇航
        print(len(movie_title),movie_title)#本作品作者吴宇航
        print(len(movie_url),movie_url)#本作品作者吴宇航
        print(len(movie_src_pic),movie_src_pic)#本作品作者吴宇航
        return movie_url,movie_title,movie_src_pic#本作品作者吴宇航
#本作品作者吴宇航
    def change_urlink(self,lis):#本作品作者吴宇航
        for i in range(len(lis)):#本作品作者吴宇航
            if '\\' in lis[i]:#本作品作者吴宇航
                lis[i] = lis[i].replace('\\', '')#本作品作者吴宇航
        # print(lis)#本作品作者吴宇航
        return lis#本作品作者吴宇航
#本作品作者吴宇航
    def change_youku_link(self,urls):#本作品作者吴宇航
        pa_link='//.+[.]html'#本作品作者吴宇航
        if re.match(pa_link,urls):#本作品作者吴宇航
            urls='http:'+urls#本作品作者吴宇航
        return urls#本作品作者吴宇航
#本作品作者吴宇航
    def get_more_tv_urls(self,url,u_name,u_type):#获取电视剧分集链接#本作品作者吴宇航
        tv_dic_new = {}#本作品作者吴宇航
        if u_name == 'y':#本作品作者吴宇航
            url=self.change_youku_link(url)#本作品作者吴宇航
            res = requests.get(url, headers=self.header_you).text.encode(encoding='utf-8').decode('utf-8')#本作品作者吴宇航
            html = etree.HTML(res)#本作品作者吴宇航
            print(res)#本作品作者吴宇航
            if u_type=="m" or u_type=="t":#本作品作者吴宇航
                self.tv_more_title = html.xpath('//div[@class="item item-num"]/@title')#本作品作者吴宇航
                self.tv_more_url = html.xpath('//div[@class="item item-num"]/a[@class="sn"]/@href')#本作品作者吴宇航
            elif u_type=="d":#本作品作者吴宇航
                self.tv_more_title = html.xpath('//div[@class="item item-txt"]/@title')#本作品作者吴宇航
                self.tv_more_url = html.xpath('//div[@class="item item-txt"]/a[@class="sn"]/@href')#本作品作者吴宇航
            elif u_type=="z":#本作品作者吴宇航
                self.tv_more_title = html.xpath('//div[@class="item item-cover"]/@title')#本作品作者吴宇航
                self.tv_more_url = html.xpath('//div[@class="item item-cover"]/a/@href')#本作品作者吴宇航
            elif u_type == "j":#本作品作者吴宇航
                self.tv_more_title = html.xpath('//div[@class="item item-cover current"]/@title')#本作品作者吴宇航
                self.tv_more_url = html.xpath('//div[@class="item item-cover current"]/a/@href')#本作品作者吴宇航
        elif u_name == 'a':#本作品作者吴宇航
            res = requests.get(url, headers=self.header_ai).text.encode(encoding='utf-8').decode('utf-8')#本作品作者吴宇航
            html = etree.HTML(res)#本作品作者吴宇航
            print(res)#本作品作者吴宇航
            if u_type=="m" or u_type=="t" or u_type=='d':#本作品作者吴宇航
                self.tv_more_title = html.xpath(#本作品作者吴宇航
                    '//ul/li[@data-albumlist-elem="playItem"]/div[@class="site-piclist_pic"]/a[1]/@title')#本作品作者吴宇航
                self.tv_more_url = html.xpath(#本作品作者吴宇航
                    '//ul/li[@data-albumlist-elem="playItem"]/div[@class="site-piclist_pic"]/a[1]/@href')#本作品作者吴宇航
            elif u_type=="z" or u_type=="j":#本作品作者吴宇航
                self.tv_more_title = html.xpath('//div[@class="recoAlbumTit"]/a[1]/@title')#本作品作者吴宇航
                self.tv_more_url = html.xpath('//div[@class="recoAlbumTit"]/a[1]/@href')#本作品作者吴宇航
        elif u_name == 'p':#本作品作者吴宇航
            res = requests.get(url, headers=self.header_pp).text.encode(encoding='utf-8').decode('utf-8')#本作品作者吴宇航
            # html = etree.HTML(res)#本作品作者吴宇航
            self.tv_more_url2 = re.compile('{"url":"(.+?)"').findall(res)#本作品作者吴宇航
            self.tv_more_url = self.change_urlink(self.tv_more_url2)#本作品作者吴宇航
            self.tv_more_title = ["第{}集".format(x) for x in range(1, len(self.tv_more_url) + 1)]#本作品作者吴宇航
        for i, j in zip(self.tv_more_title, self.tv_more_url):#本作品作者吴宇航
            tv_dic_new[i] = j#本作品作者吴宇航
        print(len(self.tv_more_title), self.tv_more_title)#本作品作者吴宇航
        print(len(self.tv_more_url), self.tv_more_url)#本作品作者吴宇航
        print(tv_dic_new)#本作品作者吴宇航
        return tv_dic_new#本作品作者吴宇航
#本作品作者吴宇航
    def url_change(self,url,flag):#本作品作者吴宇航
        pa_url='http://www.iqiyi.com/a_[.+].html'#本作品作者吴宇航
        if flag=="0":#通道1#本作品作者吴宇航
            if re.match(pa_url, url):#本作品作者吴宇航
                _url = url.replace('a', 'v')#本作品作者吴宇航
            else:#本作品作者吴宇航
                _url=url#本作品作者吴宇航
            # new_url='http://www.wq114.org/weixin.php?url={}'.format(_url[21:])#本作品作者吴宇航
            new_url='http://www.wq114.org/weixin.php?url={}'.format(_url)#本作品作者吴宇航
            return new_url#本作品作者吴宇航
        elif flag == "1":#本作品作者吴宇航
            if re.match(pa_url, url):#本作品作者吴宇航
                _url = url.replace('a', 'v')#本作品作者吴宇航
            else:#本作品作者吴宇航
                _url = url#本作品作者吴宇航
            new_url='http://www.wmxz.wang/video.php?url={}'.format(_url)#本作品作者吴宇航
            return new_url#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
    def play_movie(self,url,flag):#本作品作者吴宇航
        play_url=self.url_change(url,flag)#本作品作者吴宇航
        webbrowser.open(play_url)#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
if __name__ == '__main__':#本作品作者吴宇航
    p=Pro()#本作品作者吴宇航
from PIL import Image,ImageTk#本作品作者吴宇航
import io#本作品作者吴宇航
import re#本作品作者吴宇航
import requests#本作品作者吴宇航
# from urllib.request import urlopen#本作品作者吴宇航
def videos():#本作品作者吴宇航
    class Movie_app:#本作品作者吴宇航
        def __init__(self):#本作品作者吴宇航
            self.win=Tk()#本作品作者吴宇航
            self.win.geometry('600x420')#本作品作者吴宇航
            self.win.title("爱奇艺-优酷-PPTV视频播放下载器V3.1")#本作品作者吴宇航
            self.creat_res()#本作品作者吴宇航
            self.creat_radiores()#本作品作者吴宇航
            self.config()#本作品作者吴宇航
            self.page=1#本作品作者吴宇航
            self.p=Pro()#本作品作者吴宇航
            self.win.mainloop()#本作品作者吴宇航
    #本作品作者吴宇航
    #本作品作者吴宇航
        def creat_res(self):#本作品作者吴宇航
            self.temp=StringVar()#url地址#本作品作者吴宇航
            self.temp2=StringVar()#本作品作者吴宇航
            self.t1=StringVar()#通道#本作品作者吴宇航
            self.t3=StringVar()#爱奇艺，优酷，PPTV#本作品作者吴宇航
            self.La_title=Label(self.win,text="地址:")#本作品作者吴宇航
            self.La_way=Label(self.win,text="选择视频通道:")#本作品作者吴宇航
            self.R_way1=Radiobutton(self.win,text="通道A",variable=self.t1,value=True)#本作品作者吴宇航
            self.R_way2=Radiobutton(self.win,text="通道B",variable=self.t1,value=False)#本作品作者吴宇航
            self.R_aiqiyi=Radiobutton(self.win,text="爱奇艺",variable=self.t3,value="a")#本作品作者吴宇航
            self.R_youku=Radiobutton(self.win,text="优酷",variable=self.t3,value="y")#本作品作者吴宇航
            self.R_pptv=Radiobutton(self.win,text="PPTV",variable=self.t3,value="p")#本作品作者吴宇航
            self.B_play=Button(self.win,text="播放▶")#本作品作者吴宇航
            self.B_uppage=Button(self.win,text="上页")#本作品作者吴宇航
            self.B_nextpage=Button(self.win,text="下页")#本作品作者吴宇航
            self.B_search=Button(self.win,text="♣搜索全站♠")#本作品作者吴宇航
            self.La_mesasge=Label(self.win,text="☜  ⇠☸⇢  ☞",bg="pink")#本作品作者吴宇航
            self.La_page=Label(self.win,bg="#BFEFFF")#本作品作者吴宇航
            self.S_croll=Scrollbar(self.win)#本作品作者吴宇航
            self.L_box=Listbox(self.win,bg="#BFEFFF",selectmode=SINGLE)#本作品作者吴宇航
            self.E_address=Entry(self.win,textvariable=self.temp)#本作品作者吴宇航
            self.La_title.place(x=10,y=50,width=50,height=30)#本作品作者吴宇航
            self.E_address.place(x=70,y=50,width=200,height=30)#本作品作者吴宇航
            self.B_play.place(x=300,y=50,width=50,height=30)#本作品作者吴宇航
            self.R_way1.place(x=160,y=10,width=70,height=30)#本作品作者吴宇航
            self.R_way2.place(x=240,y=10,width=70,height=30)#本作品作者吴宇航
            self.La_way.place(x=10,y=10,width=100,height=30)#本作品作者吴宇航
            self.R_aiqiyi.place(x=20,y=100,width=70,height=30)#本作品作者吴宇航
            self.R_youku.place(x=90,y=100,width=70,height=30)#本作品作者吴宇航
            self.R_pptv.place(x=160,y=100,width=70,height=30)#本作品作者吴宇航
            self.B_search.place(x=252,y=140,width=100,height=30)#本作品作者吴宇航
            self.La_mesasge.place(x=80,y=125,width=90,height=20)#本作品作者吴宇航
            self.L_box.place(x=10,y=180,width=252,height=230)#本作品作者吴宇航
            self.S_croll.place(x=260,y=180,width=20,height=230)#本作品作者吴宇航
            self.B_uppage.place(x=10,y=140,width=50,height=30)#本作品作者吴宇航
            self.B_nextpage.place(x=180,y=140,width=50,height=30)#本作品作者吴宇航
            self.La_page.place(x=80,y=150,width=90,height=28)#本作品作者吴宇航
    #本作品作者吴宇航
        def creat_radiores(self):#本作品作者吴宇航
            self.movie=StringVar()#电影#本作品作者吴宇航
            self.S_croll2=Scrollbar()#分集#本作品作者吴宇航
            self.La_pic=Label(self.win,bg="#E6E6FA")#本作品作者吴宇航
            self.La_movie_message=Listbox(self.win,bg="#7EC0EE")#本作品作者吴宇航
            self.R_movie=Radiobutton(self.win,text="电影",variable=self.movie,value="m")#本作品作者吴宇航
            self.tv=Radiobutton(self.win,text="电视剧",variable=self.movie,value="t")#本作品作者吴宇航
            self.zhongyi=Radiobutton(self.win,text="综艺",variable=self.movie,value="z")#本作品作者吴宇航
            self.dongman=Radiobutton(self.win,text="动漫",variable=self.movie,value="d")#本作品作者吴宇航
            self.jilupian=Radiobutton(self.win,text="纪录片",variable=self.movie,value="j")#本作品作者吴宇航
            self.B_view=Button(self.win,text="✤查看✤")#本作品作者吴宇航
            self.B_info=Button(self.win,text="使用说明")#本作品作者吴宇航
            self.B_clearbox=Button(self.win,text="清空列表")#本作品作者吴宇航
            self.B_add=Button(self.win,text="添加到播放列表")#本作品作者吴宇航
            self.R_movie.place(x=290,y=180,width=80,height=30)#本作品作者吴宇航
            self.B_view.place(x=290,y=330,width=70,height=30)#本作品作者吴宇航
            self.B_add.place(x=370,y=255,width=100,height=30)#本作品作者吴宇航
            self.B_clearbox.place(x=500,y=255,width=70,height=30)#本作品作者吴宇航
            self.tv.place(x=290,y=210,width=80,height=30)#本作品作者吴宇航
            self.zhongyi.place(x=290,y=240,width=80,height=30)#本作品作者吴宇航
            self.dongman.place(x=290,y=270,width=80,height=30)#本作品作者吴宇航
            self.jilupian.place(x=290,y=300,width=80,height=30)#本作品作者吴宇航
            self.La_movie_message.place(x=370,y=290,width=200,height=120)#本作品作者吴宇航
            self.La_pic.place(x=370,y=10,width=200,height=240)#本作品作者吴宇航
            self.B_info.place(x=290,y=370,width=70,height=30)#本作品作者吴宇航
            self.S_croll2.place(x=568,y=290,width=20,height=120)#本作品作者吴宇航
    #本作品作者吴宇航
        def show_info(self):#本作品作者吴宇航
            msg="""#本作品作者吴宇航
            1.输入视频播放地址，即可播放#本作品作者吴宇航
              选择A或者B可切换视频源#本作品作者吴宇航
            2.选择视频网，选择电视剧或者电影，#本作品作者吴宇航
              搜索全网后选择想要看得影片，点#本作品作者吴宇航
              查看，在右方list里选择分集视频#本作品作者吴宇航
              添加到播放列表里点选播放#本作品作者吴宇航
            """#本作品作者吴宇航
            messagebox.showinfo(title="使用说明",message=msg)#本作品作者吴宇航
    #本作品作者吴宇航
        def config(self):#本作品作者吴宇航
            self.t1.set(True)#本作品作者吴宇航
            self.B_play.config(command=self.play_url_movie)#本作品作者吴宇航
            self.B_search.config(command=self.search_full_movie)#本作品作者吴宇航
            self.B_info.config(command=self.show_info)#本作品作者吴宇航
            self.S_croll.config(command=self.L_box.yview)#本作品作者吴宇航
            self.L_box['yscrollcommand']=self.S_croll.set#本作品作者吴宇航
            self.S_croll2.config(command=self.La_movie_message.yview)#本作品作者吴宇航
            self.La_movie_message['yscrollcommand']=self.S_croll2.set#本作品作者吴宇航
            self.B_view.config(command=self.view_movies)#本作品作者吴宇航
            self.B_add.config(command=self.add_play_list)#本作品作者吴宇航
            self.B_clearbox.config(command=self.clear_lisbox2)#本作品作者吴宇航
            self.B_uppage.config(command=self.uppage_)#本作品作者吴宇航
            self.B_nextpage.config(command=self.nextpage_)#本作品作者吴宇航
    #本作品作者吴宇航
        def uppage_(self):#本作品作者吴宇航
            print('---------上一页---------')#本作品作者吴宇航
            self.page-=1#本作品作者吴宇航
            print(self.page)#本作品作者吴宇航
            if self.page<1:#本作品作者吴宇航
                self.page=1#本作品作者吴宇航
    #本作品作者吴宇航
        def nextpage_(self):#本作品作者吴宇航
            print('----------下一页--------')#本作品作者吴宇航
            self.page+=1#本作品作者吴宇航
            print(self.page)#本作品作者吴宇航
            if self.t3=="a" or self.t3=="y":#本作品作者吴宇航
                if self.page>30:#本作品作者吴宇航
                    self.page=30#本作品作者吴宇航
            elif self.t3=="p":#本作品作者吴宇航
                if self.movie=="m":#本作品作者吴宇航
                    if self.page>165:#本作品作者吴宇航
                        self.page=165#本作品作者吴宇航
                elif self.movie == "t":#本作品作者吴宇航
                    if self.page > 85:#本作品作者吴宇航
                        self.page = 85#本作品作者吴宇航
                elif self.movie == "z":#本作品作者吴宇航
                    if self.page > 38:#本作品作者吴宇航
                        self.page = 38#本作品作者吴宇航
                elif self.movie == "d":#本作品作者吴宇航
                    if self.page > 146:#本作品作者吴宇航
                        self.page = 146#本作品作者吴宇航
                elif self.movie == "j":#本作品作者吴宇航
                    if self.page > 40:#本作品作者吴宇航
                        self.page = 40#本作品作者吴宇航
    #本作品作者吴宇航
        def clear_lisbox(self):#本作品作者吴宇航
            self.L_box.delete(0,END)#本作品作者吴宇航
    #本作品作者吴宇航
        def clear_lisbox2(self):#本作品作者吴宇航
            self.La_movie_message.delete(0,END)#本作品作者吴宇航
    #本作品作者吴宇航
        def search_full_movie(self):#本作品作者吴宇航
            print("-----search----")#本作品作者吴宇航
            self.La_page.config(text="当前页:{}".format(self.page))#本作品作者吴宇航
            self.clear_lisbox()#本作品作者吴宇航
            try:#本作品作者吴宇航
                movie_url, movie_title, movie_src_pic=self.p.get_movie_res(self.t3.get(),self.movie.get(),self.page)#本作品作者吴宇航
                self.movie_dic={}#本作品作者吴宇航
                for i,j,k in zip(movie_title,movie_url,movie_src_pic):#本作品作者吴宇航
                    self.movie_dic[i]=[j,k]#本作品作者吴宇航
                for title in movie_title:#本作品作者吴宇航
                    self.L_box.insert(END,title)#本作品作者吴宇航
                print(self.movie_dic)#本作品作者吴宇航
                return self.movie_dic#本作品作者吴宇航
            except:#本作品作者吴宇航
                messagebox.showerror(title='警告',message='请选择电影或者电视剧')#本作品作者吴宇航
    #本作品作者吴宇航
        def add_play_list(self):#本作品作者吴宇航
            print('---------playlist----------')#本作品作者吴宇航
            print(self.movie_dic)#本作品作者吴宇航
            if self.La_movie_message.get(self.La_movie_message.curselection())=="":#本作品作者吴宇航
                messagebox.showwarning(title="警告",message='请在列表选择影片')#本作品作者吴宇航
            else:#本作品作者吴宇航
                print("电影名字:",self.La_movie_message.get(self.La_movie_message.curselection()))#本作品作者吴宇航
                if self.movie.get()!="m":#本作品作者吴宇航
                    self.temp.set(self.new_more_dic[self.La_movie_message.get(self.La_movie_message.curselection())])#本作品作者吴宇航
                else:#本作品作者吴宇航
                    self.temp.set(self.movie_dic[self.La_movie_message.get(self.La_movie_message.curselection())][0])#本作品作者吴宇航
    #本作品作者吴宇航
    #本作品作者吴宇航
        def view_pic(self,pic_url):#本作品作者吴宇航
            print('--------viewpic---------')#本作品作者吴宇航
            pa_url_check=r'//.+[.]jpg'#本作品作者吴宇航
            if re.match(pa_url_check,pic_url):#本作品作者吴宇航
                print("ok")#本作品作者吴宇航
                pic_url="http:"+pic_url#本作品作者吴宇航
            print(pic_url)#本作品作者吴宇航
            data=requests.get(pic_url).content#本作品作者吴宇航
            # data=urlopen(pic_url).read()#本作品作者吴宇航
            io_data=io.BytesIO(data)#本作品作者吴宇航
            self.img=Image.open(io_data)#本作品作者吴宇航
            self.u=ImageTk.PhotoImage(self.img)#本作品作者吴宇航
            self.La_pic.config(image=self.u)#本作品作者吴宇航
    #本作品作者吴宇航
        def view_movies(self):#本作品作者吴宇航
            print("--------viewmovie----------")#本作品作者吴宇航
            cur_index=self.L_box.curselection()#本作品作者吴宇航
            print(self.L_box.get(cur_index))#本作品作者吴宇航
            if self.movie.get()!="m":#非电影类#本作品作者吴宇航
                self.new_more_dic=self.p.get_more_tv_urls(self.movie_dic[self.L_box.get(cur_index)][0],self.t3.get(),self.movie.get())#本作品作者吴宇航
                print(self.new_more_dic)#本作品作者吴宇航
                for i,fenji_url in self.new_more_dic.items():#本作品作者吴宇航
                    self.La_movie_message.insert(END, i)#本作品作者吴宇航
            else:#电影类#本作品作者吴宇航
                self.La_movie_message.insert(END,self.L_box.get(cur_index))#本作品作者吴宇航
            self.view_pic(self.movie_dic[self.L_box.get(self.L_box.curselection())][1])#加载图片#本作品作者吴宇航
    #本作品作者吴宇航
        def play_url_movie(self):#本作品作者吴宇航
            print("--------ok-----------")#本作品作者吴宇航
            # print(type(self.t1.get()),self.t1.get())#本作品作者吴宇航
            if self.temp.get()=="":#本作品作者吴宇航
                messagebox.showwarning(title="警告",message="请先输入视频地址")#本作品作者吴宇航
            else:#本作品作者吴宇航
                if self.t1.get()!="":#本作品作者吴宇航
                    self.p.play_movie(self.temp.get(),self.t1.get())#本作品作者吴宇航
                else:#本作品作者吴宇航
                    messagebox.showwarning(title='警告',message='请选择通道')#本作品作者吴宇航
    #本作品作者吴宇航
    #本作品作者吴宇航
    m=Movie_app()#本作品作者吴宇航
#本作品作者吴宇航
#记事本#本作品作者吴宇航
def notebook():#本作品作者吴宇航
    #新建根窗口#本作品作者吴宇航
    root=Tk()#本作品作者吴宇航
    #新建Menu实例#本作品作者吴宇航
    menu_bar=Menu(root)#本作品作者吴宇航
    file_menu=Menu(menu_bar,tearoff=0)#本作品作者吴宇航
    edit_menu=Menu(menu_bar,tearoff=0)#本作品作者吴宇航
    view_menu=Menu(menu_bar,tearoff=0)#本作品作者吴宇航
    about_menu=Menu(menu_bar,tearoff=0)#本作品作者吴宇航
    themes_menu=Menu(menu_bar,tearoff=0)#本作品作者吴宇航
     #本作品作者吴宇航
    file_name = None#本作品作者吴宇航
    #获取文本行数#本作品作者吴宇航
    def get_line_numbers():#本作品作者吴宇航
        output = ''#本作品作者吴宇航
        if show_line_number.get():#本作品作者吴宇航
            row, col = content_text.index("end").split('.')#本作品作者吴宇航
            for i in range(1, int(row)):#本作品作者吴宇航
                output +=str(i)+ '\n'#本作品作者吴宇航
        return output#本作品作者吴宇航
    #更新文本行数#本作品作者吴宇航
    def update_line_numbers(event = None):#本作品作者吴宇航
        line_numbers = get_line_numbers()#本作品作者吴宇航
        line_number_bar.config(state='normal')#本作品作者吴宇航
        line_number_bar.delete('1.0', 'end')#本作品作者吴宇航
        line_number_bar.insert('1.0', line_numbers)#本作品作者吴宇航
        line_number_bar.config(state='disabled')#本作品作者吴宇航
    #高亮当前行    #本作品作者吴宇航
    def highlight_line(interval=100):#本作品作者吴宇航
        content_text.tag_remove("active_line", 1.0, "end")#本作品作者吴宇航
        content_text.tag_add("active_line", "insert linestart", "insert lineend+1c")#本作品作者吴宇航
        content_text.after(interval, toggle_highlight)#本作品作者吴宇航
    #非高亮当前行    #本作品作者吴宇航
    def undo_highlight():#本作品作者吴宇航
        content_text.tag_remove("active_line", 1.0, "end")#本作品作者吴宇航
    #高亮状态切换#本作品作者吴宇航
    def toggle_highlight(event=None):#本作品作者吴宇航
        if to_highlight_line.get():#本作品作者吴宇航
            highlight_line()#本作品作者吴宇航
        else:#本作品作者吴宇航
            undo_highlight()#本作品作者吴宇航
    #显示光标信息#本作品作者吴宇航
    def show_cursor_info_bar():#本作品作者吴宇航
        show_cursor_info_checked = show_cursor_info.get()#本作品作者吴宇航
        if show_cursor_info_checked:#本作品作者吴宇航
            cursor_info_bar.pack(expand='no', fill=None, side='right', anchor='se')#本作品作者吴宇航
        else:#本作品作者吴宇航
            cursor_info_bar.pack_forget()#本作品作者吴宇航
    #更新光标信息#本作品作者吴宇航
    def update_cursor_info_bar(event=None):#本作品作者吴宇航
        row, col = content_text.index(INSERT).split('.')#本作品作者吴宇航
        line_num, col_num = str(int(row)), str(int(col)+1) #本作品作者吴宇航
        infotext = "Line: {0} | Column: {1}".format(line_num, col_num)#本作品作者吴宇航
        cursor_info_bar.config(text=infotext)#本作品作者吴宇航
    #当文本内容改变时触发#本作品作者吴宇航
    def on_content_changed(event=None):#本作品作者吴宇航
        update_line_numbers()#本作品作者吴宇航
        update_cursor_info_bar()#本作品作者吴宇航
    #打开文件#本作品作者吴宇航
    def open_file(event=None):#本作品作者吴宇航
        input_file_name=tkinter.filedialog.askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents","*.txt")])#本作品作者吴宇航
        if input_file_name:#本作品作者吴宇航
            global file_name#本作品作者吴宇航
            file_name = input_file_name#本作品作者吴宇航
            root.title('{} - {}'.format(os.path.basename(file_name), PROGRAM_NAME))#本作品作者吴宇航
            content_text.delete(1.0, END)#本作品作者吴宇航
            with open(file_name,encoding = "utf-8") as _file:#本作品作者吴宇航
                content_text.insert(1.0, _file.read())#本作品作者吴宇航
            on_content_changed()#本作品作者吴宇航
    #保存文件#本作品作者吴宇航
    def save(event=None):#本作品作者吴宇航
        global file_name#本作品作者吴宇航
        if not file_name:#本作品作者吴宇航
            save_as()#本作品作者吴宇航
        else:#本作品作者吴宇航
            write_to_file(file_name)#本作品作者吴宇航
        return "break"#本作品作者吴宇航
    #保存文件为#本作品作者吴宇航
    def save_as(event=None):#本作品作者吴宇航
        input_file_name = tkinter.filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])#本作品作者吴宇航
        if input_file_name:#本作品作者吴宇航
            global file_name#本作品作者吴宇航
            file_name = input_file_name#本作品作者吴宇航
            write_to_file(file_name)#本作品作者吴宇航
            root.title('{} - {}'.format(os.path.basename(file_name),PROGRAM_NAME))#本作品作者吴宇航
        return "break"#本作品作者吴宇航
    #写入磁盘#本作品作者吴宇航
    def write_to_file(file_name):#本作品作者吴宇航
        try:#本作品作者吴宇航
            content = content_text.get(1.0, 'end')#本作品作者吴宇航
            with open(file_name, 'w') as the_file:#本作品作者吴宇航
                the_file.write(content)#本作品作者吴宇航
        except IOError:#本作品作者吴宇航
            pass#本作品作者吴宇航
    #新建文件#本作品作者吴宇航
    def new_file(event=None):#本作品作者吴宇航
        root.title("Untitled")#本作品作者吴宇航
        global file_name#本作品作者吴宇航
        file_name = None#本作品作者吴宇航
        content_text.delete(1.0,END)#本作品作者吴宇航
        on_content_changed()#本作品作者吴宇航
    #退出编辑器#本作品作者吴宇航
    def exit_editor(event=None):#本作品作者吴宇航
        if tkinter.messagebox.askokcancel("Quit?", "Really quit?"):#本作品作者吴宇航
            root.destroy()#本作品作者吴宇航
    #剪切#本作品作者吴宇航
    def cut():#本作品作者吴宇航
        content_text.event_generate("<<Cut>>")#本作品作者吴宇航
        on_content_changed()#本作品作者吴宇航
    #复制#本作品作者吴宇航
    def copy():#本作品作者吴宇航
        content_text.event_generate("<<Copy>>")#本作品作者吴宇航
    #粘贴#本作品作者吴宇航
    def paste():#本作品作者吴宇航
        content_text.event_generate("<<Paste>>")#本作品作者吴宇航
        on_content_changed()#本作品作者吴宇航
    #恢复#本作品作者吴宇航
    def redo(event=None):#本作品作者吴宇航
        content_text.event_generate("<<Redo>>")#本作品作者吴宇航
        on_content_changed()#本作品作者吴宇航
        return 'break'#本作品作者吴宇航
    #撤销#本作品作者吴宇航
    def undo(event=None):#本作品作者吴宇航
        content_text.event_generate("<<Undo>>")#本作品作者吴宇航
        on_content_changed()#本作品作者吴宇航
        return 'break'#本作品作者吴宇航
    #全选#本作品作者吴宇航
    def select_all(event=None):#本作品作者吴宇航
        content_text.tag_add('sel', '1.0', 'end')#本作品作者吴宇航
        return "break"#本作品作者吴宇航
    #查找#本作品作者吴宇航
    def find_text(event=None):#本作品作者吴宇航
        search_toplevel=Toplevel(root)#本作品作者吴宇航
        search_toplevel.title('Find Text')#本作品作者吴宇航
        search_toplevel.transient(root)#本作品作者吴宇航
        search_toplevel.resizable(False, False)#本作品作者吴宇航
        Label(search_toplevel, text="Find All:").grid(row=0, column=0, sticky='e')#本作品作者吴宇航
        search_entry_widget = Entry(search_toplevel, width=50)#本作品作者吴宇航
        search_entry_widget.grid(row=0, column=1, padx=2, pady=2, sticky='we')#本作品作者吴宇航
        search_entry_widget.focus_set()#本作品作者吴宇航
        ignore_case_value = IntVar()#本作品作者吴宇航
        Checkbutton(search_toplevel, text='Ignore  Case',variable=ignore_case_value).grid(row=1, column=1, sticky='e', padx=2, pady=2)#本作品作者吴宇航
        Button(search_toplevel, text="Find All", underline=0,command=lambda: search_output( search_entry_widget.get(), ignore_case_value.get(), content_text, search_toplevel,search_entry_widget)).grid(row=0, column=2, sticky='e' +'w', padx=2, pady=2)#本作品作者吴宇航
    #关闭查找窗口#本作品作者吴宇航
    def close_search_window():#本作品作者吴宇航
        content_text.tag_remove('match', '1.0', END)#本作品作者吴宇航
        search_toplevel.destroy()#本作品作者吴宇航
        search_toplevel.protocol('WM_DELETE_WINDOW', close_search_window)#本作品作者吴宇航
        return "break"#本作品作者吴宇航
    #查找结果输出#本作品作者吴宇航
    def search_output(needle, if_ignore_case, content_text,search_toplevel, search_box):#本作品作者吴宇航
        content_text.tag_remove('match', '1.0', END)#本作品作者吴宇航
        matches_found = 0#本作品作者吴宇航
        if needle:#本作品作者吴宇航
             start_pos = '1.0'#本作品作者吴宇航
             while True:#本作品作者吴宇航
                 start_pos = content_text.search(needle, start_pos, nocase=if_ignore_case, stopindex=END)#本作品作者吴宇航
                 if not start_pos:#本作品作者吴宇航
                     break#本作品作者吴宇航
                 end_pos = '{}+{}c'.format(start_pos, len(needle))#本作品作者吴宇航
                 content_text.tag_add('match', start_pos, end_pos)#本作品作者吴宇航
                 matches_found += 1#本作品作者吴宇航
                 start_pos = end_pos#本作品作者吴宇航
             content_text.tag_config( 'match', foreground='red', background='yellow')#本作品作者吴宇航
        search_box.focus_set()#本作品作者吴宇航
        search_toplevel.title('{} matches found'.format(matches_found)) #本作品作者吴宇航
    #显示about#本作品作者吴宇航
    def display_about_messagebox(event=None):#本作品作者吴宇航
        tkinter.messagebox.showinfo("About", "{}{}".format(PROGRAM_NAME, "\nTkinter GUI Application\n Development Blueprints"))#本作品作者吴宇航
    #显示help#本作品作者吴宇航
    def display_help_messagebox(event=None):#本作品作者吴宇航
        tkinter.messagebox.showinfo("Help", "Help Book: \nTkinter GUI Application\n Development Blueprints", icon='question')#本作品作者吴宇航
    #变量初始化#本作品作者吴宇航
    show_cursor_info=BooleanVar()#本作品作者吴宇航
    to_highlight_line = BooleanVar() #本作品作者吴宇航
    theme_choice=StringVar()#本作品作者吴宇航
    show_line_number = IntVar()#本作品作者吴宇航
    show_line_number.set(1)#本作品作者吴宇航
    #主题#本作品作者吴宇航
    color_schemes = { 'Default': '#000000.#FFFFFF',#本作品作者吴宇航
                      'Greygarious':'#83406A.#D1D4D1',#本作品作者吴宇航
                      'Aquamarine': '#5B8340.#D1E7E0',#本作品作者吴宇航
                      'Bold Beige': '#4B4620.#FFF0E1',#本作品作者吴宇航
                      'Cobalt Blue':'#ffffBB.#3333aa',#本作品作者吴宇航
                      'Olive Green': '#D1E7E0.#5B8340',#本作品作者吴宇航
                      'Night Mode': '#FFFFFF.#000000'} #本作品作者吴宇航
    #更换主题#本作品作者吴宇航
    def change_theme(event=None):#本作品作者吴宇航
        selected_theme = theme_choice.get()#本作品作者吴宇航
        fg_bg_colors = color_schemes.get(selected_theme)#本作品作者吴宇航
        foreground_color, background_color = fg_bg_colors.split('.')#本作品作者吴宇航
        content_text.config(background=background_color,fg=foreground_color) #本作品作者吴宇航
    #File#本作品作者吴宇航
    file_menu.add_command(label="New", accelerator='Ctrl+N',    compound='left', underline=0,command=new_file)#本作品作者吴宇航
    file_menu.add_command(label="Open", accelerator='Ctrl+O',    compound='left', underline=0,command=open_file)#本作品作者吴宇航
    file_menu.add_command(label="Save", accelerator='Ctrl+S',    compound='left', underline=0 ,command= save)#本作品作者吴宇航
    file_menu.add_command(label="Save as", accelerator='Shift+Ctrl+S',    compound='left', underline=0, command= save_as)#本作品作者吴宇航
    file_menu.add_separator()#本作品作者吴宇航
    file_menu.add_command(label="Exit", accelerator='Alt+F4',    compound='left', underline=0, command= exit_editor)#本作品作者吴宇航
    #Edit#本作品作者吴宇航
    edit_menu.add_command(label="Undo", accelerator='Ctrl + Z',    compound='left',command=undo)#本作品作者吴宇航
    edit_menu.add_command(label="Redo", accelerator='Ctrl + Y',    compound='left',command=redo)#本作品作者吴宇航
    edit_menu.add_separator()#本作品作者吴宇航
    edit_menu.add_command(label="Cut", accelerator='Ctrl + X',    compound='left',command=cut)#本作品作者吴宇航
    edit_menu.add_command(label="Copy", accelerator='Ctrl + C',    compound='left',command=copy)#本作品作者吴宇航
    edit_menu.add_command(label="Paste", accelerator='Ctrl + V',    compound='left',command=paste)#本作品作者吴宇航
    edit_menu.add_separator()#本作品作者吴宇航
    edit_menu.add_command(label="Find",underline=0, accelerator='Ctrl + F',    compound='left',command=find_text)#本作品作者吴宇航
    edit_menu.add_separator()#本作品作者吴宇航
    edit_menu.add_command(label="Select All",underline=7, accelerator='Ctrl + A',    compound='left',command=select_all)#本作品作者吴宇航
    #View#本作品作者吴宇航
    view_menu.add_checkbutton(label="Show Line Number",    variable=show_line_number)#本作品作者吴宇航
    view_menu.add_checkbutton(label="Show Cursor Location at Bottom",variable=show_cursor_info, command=show_cursor_info_bar)#本作品作者吴宇航
    view_menu.add_checkbutton(label='Highlight Current Line',    onvalue=1, offvalue=0, variable=to_highlight_line,command=toggle_highlight)#本作品作者吴宇航
    #Themes#本作品作者吴宇航
    themes_menu.add_radiobutton(label="Default",  variable=theme_choice,command=change_theme)#本作品作者吴宇航
    themes_menu.add_radiobutton(label="Aquamarine", variable=theme_choice,command=change_theme)#本作品作者吴宇航
    themes_menu.add_radiobutton(label="Bold Beige", variable=theme_choice,command=change_theme)#本作品作者吴宇航
    themes_menu.add_radiobutton(label="Cobalt Blue", variable=theme_choice,command=change_theme)#本作品作者吴宇航
    themes_menu.add_radiobutton(label="Greygarious", variable=theme_choice,command=change_theme)#本作品作者吴宇航
    themes_menu.add_radiobutton(label="Night Mode", variable=theme_choice,command=change_theme)#本作品作者吴宇航
    themes_menu.add_radiobutton(label="Olive Green", variable=theme_choice,command=change_theme)#本作品作者吴宇航
    view_menu.add_cascade(label="Themes", menu=themes_menu)#本作品作者吴宇航
    #About#本作品作者吴宇航
    about_menu.add_command(label="About", compound='left', command=display_about_messagebox)#本作品作者吴宇航
    about_menu.add_command(label="Help", compound='left', command=display_help_messagebox)#本作品作者吴宇航
    #主菜单栏#本作品作者吴宇航
    menu_bar.add_cascade(label='File',menu=file_menu)#本作品作者吴宇航
    menu_bar.add_cascade(label='Edit',menu=edit_menu)#本作品作者吴宇航
    menu_bar.add_cascade(label='View',menu=view_menu)#本作品作者吴宇航
    menu_bar.add_cascade(label='About',menu=about_menu)#本作品作者吴宇航
    #窗口名称#本作品作者吴宇航
    PROGRAM_NAME = " Footprint Editor "#本作品作者吴宇航
    root.title(PROGRAM_NAME)#本作品作者吴宇航
    #工具栏#本作品作者吴宇航
    shortcut_bar = Frame(root,  height=25, background='light sea green')#本作品作者吴宇航
    shortcut_bar.pack(expand='no', fill='x')#本作品作者吴宇航
    #图标名称#本作品作者吴宇航
    names = ["新建","打开","保存","剪切","复制","粘贴","撤销","恢复","查找"]#本作品作者吴宇航
    icons = ['new_file', 'open_file', 'save', 'cut', 'copy', 'paste','undo', 'redo', 'find_text']#本作品作者吴宇航
    for i in range(len(icons)):#本作品作者吴宇航
        # tool_bar_icon = PhotoImage(file='icons/{}.gif'.format(icon))#图标文件路径#本作品作者吴宇航
        cmd = eval(icons[i])#本作品作者吴宇航
        tool_bar = Button(shortcut_bar,text = names[i],command=cmd)#本作品作者吴宇航
        #本作品作者吴宇航
        tool_bar.pack(side='left')#本作品作者吴宇航
    #左侧行数区    #本作品作者吴宇航
    line_number_bar = Text(root, width=4, padx=3, takefocus=0,    border=0, background='khaki', state='disabled', wrap='none')#本作品作者吴宇航
    line_number_bar.pack(side='left', fill='y')#本作品作者吴宇航
    #文本内容区和右侧滚动条#本作品作者吴宇航
    content_text = Text(root, wrap='word',undo=1)#本作品作者吴宇航
    content_text.tag_configure('active_line', background='ivory2')#本作品作者吴宇航
    content_text.bind('<Any-KeyPress>', on_content_changed)#本作品作者吴宇航
    content_text.pack(expand='yes', fill='both')#本作品作者吴宇航
    scroll_bar = Scrollbar(content_text)#本作品作者吴宇航
    content_text.configure(yscrollcommand=scroll_bar.set)#本作品作者吴宇航
    scroll_bar.config(command=content_text.yview)#本作品作者吴宇航
    scroll_bar.pack(side='right', fill='y')#本作品作者吴宇航
    #右键下拉菜单#本作品作者吴宇航
    popup_menu = Menu(content_text)#本作品作者吴宇航
    for i in ('cut', 'copy', 'paste', 'undo', 'redo'):#本作品作者吴宇航
        cmd = eval(i)#本作品作者吴宇航
        popup_menu.add_command(label=i, compound='left', command=cmd)#本作品作者吴宇航
    popup_menu.add_separator()#本作品作者吴宇航
    popup_menu.add_command(label='Select All', underline=7,    command=select_all)#本作品作者吴宇航
    def show_popup_menu(event):#本作品作者吴宇航
        popup_menu.tk_popup(event.x_root, event.y_root)#本作品作者吴宇航
    content_text.bind('<Button-3>', show_popup_menu)#本作品作者吴宇航
    #右下侧光标信息显示#本作品作者吴宇航
    cursor_info_bar = Label(content_text, text='Line: 1 | Column: 1')#本作品作者吴宇航
    cursor_info_bar.pack(expand=NO, fill=None, side='right',    anchor='se')#本作品作者吴宇航
     #本作品作者吴宇航
    root.config(menu=menu_bar)#本作品作者吴宇航
    root.mainloop()#本作品作者吴宇航
#本作品作者吴宇航
#绘画板#本作品作者吴宇航
from tkinter import *#本作品作者吴宇航
from tkinter.colorchooser import askcolor#本作品作者吴宇航
import time#本作品作者吴宇航
win_width = 1200#本作品作者吴宇航
win_height = 750#本作品作者吴宇航
bgcolor = 'white'#本作品作者吴宇航
def huihua():#本作品作者吴宇航
    #本作品作者吴宇航
    print("画笔初始颜色为黑色.")#本作品作者吴宇航
    print("橡皮擦要先点橡皮擦再点画笔用哦!")#本作品作者吴宇航
    time.sleep(1)#本作品作者吴宇航
    class Application(Frame):#本作品作者吴宇航
        """一个经典的GUI写法"""#本作品作者吴宇航
    #本作品作者吴宇航
        def __init__(self, master=None):#本作品作者吴宇航
            """初始化方法"""#本作品作者吴宇航
            super().__init__(master)  # 调用父类的初始化方法#本作品作者吴宇航
            self.x = 0#本作品作者吴宇航
            self.y = 0#本作品作者吴宇航
            self.fgcolor = "black"#本作品作者吴宇航
            self.lastdraw = 0#本作品作者吴宇航
            self.start_flag = False#本作品作者吴宇航
            self.master = master#本作品作者吴宇航
            self.pack()#本作品作者吴宇航
            self.createWidget()#本作品作者吴宇航
    #本作品作者吴宇航
        def createWidget(self):#本作品作者吴宇航
            """创建画图区域"""#本作品作者吴宇航
            self.drawpad = Canvas(self, width=win_width, height=win_height, bg=bgcolor)#本作品作者吴宇航
            self.drawpad.pack()#本作品作者吴宇航
            # 创建按钮#本作品作者吴宇航
            self.btn_start = Button(self, name='start', text='开始')#本作品作者吴宇航
            self.btn_start.pack(side='left', padx=50)#本作品作者吴宇航
            self.btn_pen = Button(self, name='pen', text='画笔')#本作品作者吴宇航
            self.btn_pen.pack(side='left', padx=50)#本作品作者吴宇航
            self.btn_rect = Button(self, name='rect', text='矩形')#本作品作者吴宇航
            self.btn_rect.pack(side='left', padx=50)#本作品作者吴宇航
            self.btn_clear = Button(self, name='clear', text='清屏')#本作品作者吴宇航
            self.btn_clear.pack(side='left', padx=50)#本作品作者吴宇航
            self.btn_erasor = Button(self, name='erasor', text='橡皮擦')#本作品作者吴宇航
            self.btn_erasor.pack(side='left', padx=50)#本作品作者吴宇航
            self.btn_line = Button(self, name='line', text='直线')#本作品作者吴宇航
            self.btn_line.pack(side='left', padx=50)#本作品作者吴宇航
            self.btn_line_arrow = Button(self, name='line_arrow', text='箭头直线')#本作品作者吴宇航
            self.btn_line_arrow.pack(side='left', padx=50)#本作品作者吴宇航
            self.btn_color = Button(self, name='color', text='颜色')#本作品作者吴宇航
            self.btn_color.pack(side='left', padx=50)#本作品作者吴宇航
            # 绑定事件#本作品作者吴宇航
            self.btn_line.bind('<Button-1>', self.eventManager)  # 点击按钮事件#本作品作者吴宇航
            self.btn_line_arrow.bind('<Button-1>', self.eventManager)  # 点击按钮事件#本作品作者吴宇航
            self.btn_rect.bind('<Button-1>', self.eventManager)  # 点击按钮事件#本作品作者吴宇航
            self.btn_pen.bind('<Button-1>', self.eventManager)  # 点击按钮事件#本作品作者吴宇航
            self.btn_erasor.bind('<Button-1>', self.eventManager)  # 点击按钮事件#本作品作者吴宇航
            self.btn_clear.bind('<Button-1>', self.eventManager)  # 点击按钮事件#本作品作者吴宇航
            self.btn_color.bind('<Button-1>', self.eventManager)  # 点击按钮事件#本作品作者吴宇航
            self.master.bind('<KeyPress-r>', self.hotKey)  # 绑定快捷键#本作品作者吴宇航
            self.master.bind('<KeyPress-g>', self.hotKey)  # 绑定快捷键#本作品作者吴宇航
            self.master.bind('<KeyPress-b>', self.hotKey)  # 绑定快捷键#本作品作者吴宇航
            self.master.bind('<KeyPress-y>', self.hotKey)  # 绑定快捷键#本作品作者吴宇航
            self.drawpad.bind('<ButtonRelease-1>', self.stopDraw)  # 左键释放按钮#本作品作者吴宇航
    #本作品作者吴宇航
        def eventManager(self, event):#本作品作者吴宇航
            name = event.widget.winfo_name()#本作品作者吴宇航
            print(name)#本作品作者吴宇航
            self.start_flag = True#本作品作者吴宇航
            if name == 'line':#本作品作者吴宇航
                # 左键拖动#本作品作者吴宇航
                self.drawpad.bind('<B1-Motion>', self.myline)#本作品作者吴宇航
            elif name == 'line_arrow':#本作品作者吴宇航
                self.drawpad.bind('<B1-Motion>', self.myline_arrow)#本作品作者吴宇航
            elif name == 'rect':#本作品作者吴宇航
                self.drawpad.bind('<B1-Motion>', self.myrect)#本作品作者吴宇航
            elif name == 'pen':#本作品作者吴宇航
                self.drawpad.bind('<B1-Motion>', self.mypen)#本作品作者吴宇航
            elif name == 'erasor':#本作品作者吴宇航
                self.drawpad.bind('<B1-Motion>', self.myerasor)#本作品作者吴宇航
            elif name == 'clear':#本作品作者吴宇航
                self.drawpad.delete('all')#本作品作者吴宇航
            elif name == 'color':#本作品作者吴宇航
                c = askcolor(color=self.fgcolor, title='请选择颜色')#本作品作者吴宇航
                print(c)  # c的值 ((128.5, 255.99609375, 0.0), '#80ff00')#本作品作者吴宇航
                self.fgcolor = c[1]#本作品作者吴宇航
    #本作品作者吴宇航
        def startDraw(self, event):#本作品作者吴宇航
            self.drawpad.delete(self.lastdraw)#本作品作者吴宇航
            if self.start_flag:#本作品作者吴宇航
                self.start_flag = False#本作品作者吴宇航
                self.x = event.x#本作品作者吴宇航
                self.y = event.y#本作品作者吴宇航
    #本作品作者吴宇航
        def stopDraw(self, event):#本作品作者吴宇航
            self.start_flag = True#本作品作者吴宇航
            self.lastdraw = 0#本作品作者吴宇航
    #本作品作者吴宇航
        def myline(self, event):#本作品作者吴宇航
            self.startDraw(event)#本作品作者吴宇航
            self.lastdraw = self.drawpad.create_line(self.x, self.y, event.x, event.y, fill=self.fgcolor)#本作品作者吴宇航
    #本作品作者吴宇航
        def myline_arrow(self, event):#本作品作者吴宇航
            self.startDraw(event)#本作品作者吴宇航
            self.lastdraw = self.drawpad.create_line(self.x, self.y, event.x, event.y, arrow=LAST, fill=self.fgcolor)#本作品作者吴宇航
    #本作品作者吴宇航
        def myrect(self, event):#本作品作者吴宇航
            self.startDraw(event)#本作品作者吴宇航
            self.lastdraw = self.drawpad.create_rectangle(self.x, self.y, event.x, event.y, outline=self.fgcolor)#本作品作者吴宇航
    #本作品作者吴宇航
        def mypen(self, event):#本作品作者吴宇航
            self.startDraw(event)#本作品作者吴宇航
            print('self.x=', self.x, ',self.y=', self.y)#本作品作者吴宇航
            self.drawpad.create_line(self.x, self.y, event.x, event.y, fill=self.fgcolor)#本作品作者吴宇航
            self.x = event.x#本作品作者吴宇航
            self.y = event.y#本作品作者吴宇航
    #本作品作者吴宇航
        def myerasor(self, event):#本作品作者吴宇航
            self.fgcolor = "white"#本作品作者吴宇航
            #本作品作者吴宇航
        def hotKey(self, event):#本作品作者吴宇航
            c = event.char#本作品作者吴宇航
            if c == 'r':#本作品作者吴宇航
                self.fgcolor = 'red'#本作品作者吴宇航
            elif c == 'g':#本作品作者吴宇航
                self.fgcolor = 'green'#本作品作者吴宇航
            elif c == 'b':#本作品作者吴宇航
                self.fgcolor = 'blue'#本作品作者吴宇航
            elif c == 'y':#本作品作者吴宇航
                self.fgcolor = 'yellow'#本作品作者吴宇航
    #本作品作者吴宇航
    #本作品作者吴宇航
    if __name__ == '__main__':#本作品作者吴宇航
        root = Tk()#本作品作者吴宇航
        root.title('画图窗口')#本作品作者吴宇航
        root.geometry('1200x1000+400+400')#本作品作者吴宇航
        app = Application(master=root)#本作品作者吴宇航
        root.mainloop()#本作品作者吴宇航
#本作品作者吴宇航
#计算器#本作品作者吴宇航
import wx#本作品作者吴宇航
def jisuan():#本作品作者吴宇航
    class Caluculate(wx.Frame):#本作品作者吴宇航
        def __init__(self,*args,**kwargs):#本作品作者吴宇航
            super(Caluculate,self).__init__(*args,**kwargs)#本作品作者吴宇航
            self.panel = wx.Panel(self)#本作品作者吴宇航
            self.printbtn = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE | wx.HSCROLL)#本作品作者吴宇航
            self.num1 = wx.Button(self.panel, label="1")#本作品作者吴宇航
            self.num2 = wx.Button(self.panel, label="2")#本作品作者吴宇航
            self.num3 = wx.Button(self.panel, label="3")#本作品作者吴宇航
            self.num4 = wx.Button(self.panel, label="+")#本作品作者吴宇航
            self.num5 = wx.Button(self.panel, label="4")#本作品作者吴宇航
            self.num6 = wx.Button(self.panel, label="5")#本作品作者吴宇航
            self.num7 = wx.Button(self.panel, label="6")#本作品作者吴宇航
            self.num8 = wx.Button(self.panel, label="-")#本作品作者吴宇航
            self.num9 = wx.Button(self.panel, label="7")#本作品作者吴宇航
            self.num10 = wx.Button(self.panel, label="8")#本作品作者吴宇航
            self.num11 = wx.Button(self.panel, label="9")#本作品作者吴宇航
            self.num12 = wx.Button(self.panel, label="*")#本作品作者吴宇航
            self.num13 = wx.Button(self.panel, label="0")#本作品作者吴宇航
            self.num14 = wx.Button(self.panel, label=".")#本作品作者吴宇航
            self.num15 = wx.Button(self.panel, label="=")#本作品作者吴宇航
            self.num16 = wx.Button(self.panel, label="/")#本作品作者吴宇航
#本作品作者吴宇航
            self.Boxset()#本作品作者吴宇航
            self.Event_bind()#本作品作者吴宇航
            self.Show()#本作品作者吴宇航
#本作品作者吴宇航
        def Boxset(self):#本作品作者吴宇航
            sbox1 = wx.BoxSizer()#本作品作者吴宇航
            sbox2 = wx.BoxSizer()#本作品作者吴宇航
            sbox3 = wx.BoxSizer()#本作品作者吴宇航
            sbox4 = wx.BoxSizer()#本作品作者吴宇航
            sbox5 = wx.BoxSizer()#本作品作者吴宇航
            vbox = wx.BoxSizer(wx.VERTICAL)#本作品作者吴宇航
            sbox1.Add(self.printbtn,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.DOWN,border=5)#本作品作者吴宇航
            sbox2.Add(self.num1,proportion=1,flag=wx.EXPAND|wx.LEFT,border=5)#本作品作者吴宇航
            sbox2.Add(self.num2,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.RIGHT,border=2)#本作品作者吴宇航
            sbox2.Add(self.num3,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.RIGHT,border=2)#本作品作者吴宇航
            sbox2.Add(self.num4,proportion=1,flag=wx.EXPAND|wx.RIGHT,border=5)#本作品作者吴宇航
            sbox3.Add(self.num5,proportion=1,flag=wx.EXPAND|wx.LEFT,border=5)#本作品作者吴宇航
            sbox3.Add(self.num6,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.RIGHT,border=2)#本作品作者吴宇航
            sbox3.Add(self.num7,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.RIGHT,border=2)#本作品作者吴宇航
            sbox3.Add(self.num8,proportion=1,flag=wx.EXPAND|wx.RIGHT,border=5)#本作品作者吴宇航
            sbox4.Add(self.num9,proportion=1,flag=wx.EXPAND|wx.LEFT,border=5)#本作品作者吴宇航
            sbox4.Add(self.num10,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.RIGHT,border=2)#本作品作者吴宇航
            sbox4.Add(self.num11,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.RIGHT,border=2)#本作品作者吴宇航
            sbox4.Add(self.num12,proportion=1,flag=wx.EXPAND|wx.RIGHT,border=5)#本作品作者吴宇航
            sbox5.Add(self.num13,proportion=1,flag=wx.EXPAND|wx.LEFT,border=5)#本作品作者吴宇航
            sbox5.Add(self.num14,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.RIGHT,border=2)#本作品作者吴宇航
            sbox5.Add(self.num15,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.RIGHT,border=2)#本作品作者吴宇航
            sbox5.Add(self.num16,proportion=1,flag=wx.EXPAND|wx.RIGHT,border=5)#本作品作者吴宇航
            vbox.Add(sbox1,proportion=1,flag=wx.EXPAND|wx.ALL,border=2)#本作品作者吴宇航
            vbox.Add(sbox2,proportion=1,flag=wx.EXPAND|wx.ALL,border=2)#本作品作者吴宇航
            vbox.Add(sbox3,proportion=1,flag=wx.EXPAND|wx.ALL,border=2)#本作品作者吴宇航
            vbox.Add(sbox4,proportion=1,flag=wx.EXPAND|wx.ALL,border=2)#本作品作者吴宇航
            vbox.Add(sbox5,proportion=1,flag=wx.EXPAND|wx.ALL,border=2)#本作品作者吴宇航
            self.panel.SetSizer(vbox)#本作品作者吴宇航
#本作品作者吴宇航
        def test1appd(self,event):#本作品作者吴宇航
            prv_result = self.printbtn.GetValue()#本作品作者吴宇航
            self.printbtn.AppendText("1")#本作品作者吴宇航
        def test2appd(self,event):#本作品作者吴宇航
            self.printbtn.AppendText("2")#本作品作者吴宇航
        def test3appd(self,event):#本作品作者吴宇航
            self.printbtn.AppendText("3")#本作品作者吴宇航
        def test4appd(self,event):#本作品作者吴宇航
            self.printbtn.AppendText("+")#本作品作者吴宇航
        def test5appd(self,event):#本作品作者吴宇航
            self.printbtn.AppendText("4")#本作品作者吴宇航
        def test6appd(self,event):#本作品作者吴宇航
            self.printbtn.AppendText("5")#本作品作者吴宇航
        def test7appd(self,event):#本作品作者吴宇航
            self.printbtn.AppendText("6")#本作品作者吴宇航
        def test8appd(self,event):#本作品作者吴宇航
            self.printbtn.AppendText("-")#本作品作者吴宇航
#本作品作者吴宇航
        def test9appd(self,event):#本作品作者吴宇航
            self.printbtn.AppendText("7")#本作品作者吴宇航
        def test10appd(self,event):#本作品作者吴宇航
            self.printbtn.AppendText("8")#本作品作者吴宇航
        def test11appd(self,event):#本作品作者吴宇航
            self.printbtn.AppendText("9")#本作品作者吴宇航
        def test12appd(self,event):#本作品作者吴宇航
            self.printbtn.AppendText("*")#本作品作者吴宇航
        def test13appd(self,event):#本作品作者吴宇航
            self.printbtn.AppendText("0")#本作品作者吴宇航
        def test14appd(self,event):#本作品作者吴宇航
            self.printbtn.AppendText(".")#本作品作者吴宇航
        def test15appd(self,event):#本作品作者吴宇航
            pre_result = str(self.printbtn.GetValue())#本作品作者吴宇航
            result = eval(pre_result)#本作品作者吴宇航
            self.printbtn.SetValue(str(result))#本作品作者吴宇航
        def test16appd(self,event):#本作品作者吴宇航
            self.printbtn.AppendText("/")#本作品作者吴宇航
        def Event_bind(self):#本作品作者吴宇航
            self.num1.Bind(wx.EVT_BUTTON,self.test1appd)#本作品作者吴宇航
            self.num2.Bind(wx.EVT_BUTTON,self.test2appd)#本作品作者吴宇航
            self.num3.Bind(wx.EVT_BUTTON,self.test3appd)#本作品作者吴宇航
            self.num4.Bind(wx.EVT_BUTTON,self.test4appd)#本作品作者吴宇航
            self.num5.Bind(wx.EVT_BUTTON,self.test5appd)#本作品作者吴宇航
            self.num6.Bind(wx.EVT_BUTTON,self.test6appd)#本作品作者吴宇航
            self.num7.Bind(wx.EVT_BUTTON,self.test7appd)#本作品作者吴宇航
            self.num8.Bind(wx.EVT_BUTTON,self.test8appd)#本作品作者吴宇航
            self.num9.Bind(wx.EVT_BUTTON,self.test9appd)#本作品作者吴宇航
            self.num10.Bind(wx.EVT_BUTTON, self.test10appd)#本作品作者吴宇航
            self.num11.Bind(wx.EVT_BUTTON, self.test11appd)#本作品作者吴宇航
            self.num12.Bind(wx.EVT_BUTTON, self.test12appd)#本作品作者吴宇航
            self.num13.Bind(wx.EVT_BUTTON, self.test13appd)#本作品作者吴宇航
            self.num14.Bind(wx.EVT_BUTTON, self.test14appd)#本作品作者吴宇航
            self.num15.Bind(wx.EVT_BUTTON, self.test15appd)#本作品作者吴宇航
            self.num16.Bind(wx.EVT_BUTTON, self.test16appd)#本作品作者吴宇航
    app = wx.App()#本作品作者吴宇航
    Caluculate(None,title="计算器")#本作品作者吴宇航
    app.MainLoop()#本作品作者吴宇航
#本作品作者吴宇航
#数学计算工具#本作品作者吴宇航
from tkinter import messagebox#本作品作者吴宇航
from tkinter import *#本作品作者吴宇航
from tkinter.ttk import *#本作品作者吴宇航
suyinshu,sb,list3,List1,r_list,bilishu = [],{},[],[],[],[]#本作品作者吴宇航
global zuida,x_x,x_x2,x_x3,chooseuser#本作品作者吴宇航
global jieguo1#本作品作者吴宇航
jieguo1 = 0#本作品作者吴宇航
zuida = 0#本作品作者吴宇航
from os import *#本作品作者吴宇航
from time import *#本作品作者吴宇航
from math import *#本作品作者吴宇航
from easygui import *#本作品作者吴宇航
import webbrowser#本作品作者吴宇航
def shuxue():#本作品作者吴宇航
    def jitutonglong(toushu,tuishu):#本作品作者吴宇航
        tuishu = tuishu - toushu * 2#本作品作者吴宇航
        a = int(tuishu / 2)#本作品作者吴宇航
        if a % 1 == 0 and (toushu - a) % 1 == 0:#本作品作者吴宇航
            return "兔" + str(a) + "只鸡" + str(toushu - a) + "只"#本作品作者吴宇航
        else:#本作品作者吴宇航
            return "无解"#本作品作者吴宇航
    def youxi(mode,a,b):#本作品作者吴宇航
        if mode == "1":#本作品作者吴宇航
            return a ** b#本作品作者吴宇航
        elif mode == "2":#本作品作者吴宇航
            a = a ** (1 / b)#本作品作者吴宇航
            return a#本作品作者吴宇航
        elif mode == "3":#本作品作者吴宇航
            return log(b,a)#本作品作者吴宇航
    def hunxunhuan(a,xunhuanjie):#本作品作者吴宇航
        if a[0] == "0":#本作品作者吴宇航
            nima = ""#本作品作者吴宇航
            for i in range(len(xunhuanjie)):#本作品作者吴宇航
                nima = nima + "9"#本作品作者吴宇航
            for i in range(len(a) - 2 - len(xunhuanjie)):#本作品作者吴宇航
                nima = nima + "0"#本作品作者吴宇航
            a = int(a.replace("0.",""))#本作品作者吴宇航
            nima2 = int(str(a).replace(xunhuanjie,""))#本作品作者吴宇航
            b = a - nima2#本作品作者吴宇航
            a = int(nima)#本作品作者吴宇航
            zuida = 0#本作品作者吴宇航
            suyinshu.clear()#本作品作者吴宇航
            if a % b == 0:#本作品作者吴宇航
                zuida = b#本作品作者吴宇航
            elif b % a == 0:#本作品作者吴宇航
                zuida = a#本作品作者吴宇航
            else:#本作品作者吴宇航
                d = a#本作品作者吴宇航
                e = b#本作品作者吴宇航
                list3.clear()#本作品作者吴宇航
                if d > e:#本作品作者吴宇航
                    if e % 2 == 0:#本作品作者吴宇航
                        o = e / 2#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        o = (e - 1) / 2 #本作品作者吴宇航
                else:#本作品作者吴宇航
                    if d % 2 == 0:#本作品作者吴宇航
                        o = d / 2#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        o = (d - 1) / 2#本作品作者吴宇航
                for i in range(1,int(o + 1)):#本作品作者吴宇航
                    if d % i == 0 and e % i == 0:#本作品作者吴宇航
                        if zhihe(i) == "N":#本作品作者吴宇航
                            suyinshu.append(i)#本作品作者吴宇航
                            if i != 1:#本作品作者吴宇航
                                list3.append(i)#本作品作者吴宇航
                            d = d / i#本作品作者吴宇航
                            e = e / i#本作品作者吴宇航
                while True:#本作品作者吴宇航
                    if len(list3) == 0:#本作品作者吴宇航
                        break#本作品作者吴宇航
                    list3.clear()#本作品作者吴宇航
                    if d > e:#本作品作者吴宇航
                        if e % 2 == 0:#本作品作者吴宇航
                            o = e / 2#本作品作者吴宇航
                        else:#本作品作者吴宇航
                            o = (e - 1) / 2 #本作品作者吴宇航
                    else:#本作品作者吴宇航
                        if d % 2 == 0:#本作品作者吴宇航
                            o = d / 2#本作品作者吴宇航
                        else:#本作品作者吴宇航
                            o = (d - 1) / 2#本作品作者吴宇航
                    for i in range(2,int(o + 1)):#本作品作者吴宇航
                        if d % i == 0 and e % i == 0:#本作品作者吴宇航
                            if zhihe(i) == "N":#本作品作者吴宇航
                                suyinshu.append(i)#本作品作者吴宇航
                                list3.append(i)#本作品作者吴宇航
                                d = d / i#本作品作者吴宇航
                                e = e / i#本作品作者吴宇航
                d = 1#本作品作者吴宇航
                for i in range(len(suyinshu)):#本作品作者吴宇航
                    if i != len(suyinshu) - 1:#本作品作者吴宇航
                        d = d * suyinshu[i]#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        zuida = suyinshu[i] * d#本作品作者吴宇航
                if zuida == 0:#本作品作者吴宇航
                    zuida = 1#本作品作者吴宇航
            return str(a // zuida) + "分之" + str(b // zuida)#本作品作者吴宇航
        else:#本作品作者吴宇航
            nima2 = ""#本作品作者吴宇航
            i = 1#本作品作者吴宇航
            while a.index(".") - i != -1:#本作品作者吴宇航
                nima2 = a[a.index(".") - i] + nima2#本作品作者吴宇航
                i += 1#本作品作者吴宇航
            nima = ""#本作品作者吴宇航
            for i in range(len(xunhuanjie)):#本作品作者吴宇航
                nima = nima + "9"#本作品作者吴宇航
            for i in range(len(a) - len(nima2) - 1 - len(xunhuanjie)):#本作品作者吴宇航
                nima = nima + "0"#本作品作者吴宇航
            a = int(a.replace(nima2 + ".",""))#本作品作者吴宇航
            nima2 = int(str(a).replace(xunhuanjie,""))#本作品作者吴宇航
            b = a - nima2#本作品作者吴宇航
            a = int(nima)#本作品作者吴宇航
            zuida = 0#本作品作者吴宇航
            suyinshu.clear()#本作品作者吴宇航
            if a % b == 0:#本作品作者吴宇航
                zuida = b#本作品作者吴宇航
            elif b % a == 0:#本作品作者吴宇航
                zuida = a#本作品作者吴宇航
            else:#本作品作者吴宇航
                d = a#本作品作者吴宇航
                e = b#本作品作者吴宇航
                list3.clear()#本作品作者吴宇航
                if d > e:#本作品作者吴宇航
                    if e % 2 == 0:#本作品作者吴宇航
                        o = e / 2#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        o = (e - 1) / 2 #本作品作者吴宇航
                else:#本作品作者吴宇航
                    if d % 2 == 0:#本作品作者吴宇航
                        o = d / 2#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        o = (d - 1) / 2#本作品作者吴宇航
                for i in range(1,int(o + 1)):#本作品作者吴宇航
                    if d % i == 0 and e % i == 0:#本作品作者吴宇航
                        if zhihe(i) == "N":#本作品作者吴宇航
                            suyinshu.append(i)#本作品作者吴宇航
                            if i != 1:#本作品作者吴宇航
                                list3.append(i)#本作品作者吴宇航
                            d = d / i#本作品作者吴宇航
                            e = e / i#本作品作者吴宇航
                while True:#本作品作者吴宇航
                    if len(list3) == 0:#本作品作者吴宇航
                        break#本作品作者吴宇航
                    list3.clear()#本作品作者吴宇航
                    if d > e:#本作品作者吴宇航
                        if e % 2 == 0:#本作品作者吴宇航
                            o = e / 2#本作品作者吴宇航
                        else:#本作品作者吴宇航
                            o = (e - 1) / 2 #本作品作者吴宇航
                    else:#本作品作者吴宇航
                        if d % 2 == 0:#本作品作者吴宇航
                            o = d / 2#本作品作者吴宇航
                        else:#本作品作者吴宇航
                            o = (d - 1) / 2#本作品作者吴宇航
                    for i in range(2,int(o + 1)):#本作品作者吴宇航
                        if d % i == 0 and e % i == 0:#本作品作者吴宇航
                            if zhihe(i) == "N":#本作品作者吴宇航
                                suyinshu.append(i)#本作品作者吴宇航
                                list3.append(i)#本作品作者吴宇航
                                d = d / i#本作品作者吴宇航
                                e = e / i#本作品作者吴宇航
                d = 1#本作品作者吴宇航
                for i in range(len(suyinshu)):#本作品作者吴宇航
                    if i != len(suyinshu) - 1:#本作品作者吴宇航
                        d = d * suyinshu[i]#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        zuida = suyinshu[i] * d#本作品作者吴宇航
                if zuida == 0:#本作品作者吴宇航
                    zuida = 1#本作品作者吴宇航
            return str(nima2) + "又" + str(a // zuida) + "分之" + str(b // zuida)#本作品作者吴宇航
    def jueduizhi(a):#本作品作者吴宇航
        return abs(a)#本作品作者吴宇航
    def abaabaaba(hahaha):#本作品作者吴宇航
        List1.clear()#本作品作者吴宇航
        if hahaha.count("/") == 2:#本作品作者吴宇航
            if "+" in hahaha:#本作品作者吴宇航
                nima = hahaha[hahaha.index("+") - 1]#本作品作者吴宇航
                i = 2#本作品作者吴宇航
                while hahaha[hahaha.index("+") - i] != "/":#本作品作者吴宇航
                    nima = hahaha[hahaha.index("+") - i] + nima#本作品作者吴宇航
                    i += 1#本作品作者吴宇航
                nima = float(nima)#本作品作者吴宇航
                nima2 = hahaha[hahaha.index("=") - 1]#本作品作者吴宇航
                i = 2#本作品作者吴宇航
                while hahaha[hahaha.index("=") - i] != "/":#本作品作者吴宇航
                    nima2 = hahaha[hahaha.index("=") - i] + nima2#本作品作者吴宇航
                    i += 1#本作品作者吴宇航
                nima2 = float(nima2)#本作品作者吴宇航
                zonghe = hahaha[len(hahaha) - 1]#本作品作者吴宇航
                i = 2#本作品作者吴宇航
                while hahaha[len(hahaha) - i] != "=":#本作品作者吴宇航
                    zonghe = hahaha[len(hahaha) - i] + zonghe#本作品作者吴宇航
                    i += 1#本作品作者吴宇航
                zonghe = int(zonghe)#本作品作者吴宇航
                for i in range(int(zonghe * nima * nima2)):#本作品作者吴宇航
                    if i % nima == 0:#本作品作者吴宇航
                        if i not in List1 and (zonghe - i / nima) * nima not in List1:#本作品作者吴宇航
                            if i >= 0 and (zonghe - i / nima) * nima2 >= 0:#本作品作者吴宇航
                                List1.append(i)#本作品作者吴宇航
                                List1.append(int((zonghe - i / nima) * nima2))#本作品作者吴宇航
                return List1#本作品作者吴宇航
            nima = hahaha[hahaha.index("-") - 1]#本作品作者吴宇航
            i = 2#本作品作者吴宇航
            while hahaha[hahaha.index("-") - i] != "/":#本作品作者吴宇航
                nima = hahaha[hahaha.index("-") - i] + nima#本作品作者吴宇航
                i += 1#本作品作者吴宇航
            nima = float(nima)#本作品作者吴宇航
            nima2 = hahaha[hahaha.index("=") - 1]#本作品作者吴宇航
            i = 2#本作品作者吴宇航
            while hahaha[hahaha.index("=") - i] != "/":#本作品作者吴宇航
                nima2 = hahaha[hahaha.index("=") - i] + nima2#本作品作者吴宇航
                i += 1#本作品作者吴宇航
            nima2 = float(nima2)#本作品作者吴宇航
            zonghe = hahaha[len(hahaha) - 1]#本作品作者吴宇航
            i = 2#本作品作者吴宇航
            while hahaha[len(hahaha) - i] != "=":#本作品作者吴宇航
                zonghe = hahaha[len(hahaha) - i] + zonghe#本作品作者吴宇航
                i += 1#本作品作者吴宇航
            zonghe = int(zonghe)#本作品作者吴宇航
            i = 0#本作品作者吴宇航
            while True:#本作品作者吴宇航
                if i % nima == 0:#本作品作者吴宇航
                    if i not in List1 and (zonghe - i / nima) * nima2 not in List1:#本作品作者吴宇航
                        if i >= 0 and (zonghe - i / nima) * nima3 >= 0:#本作品作者吴宇航
                            list1.append(i)#本作品作者吴宇航
                            list1.append(int((zonghe - i / nima) * nima2))#本作品作者吴宇航
                            break#本作品作者吴宇航
            for i in range(1,11):#本作品作者吴宇航
                list1.append(list1[0] + nima * i)#本作品作者吴宇航
                list1.append(list1[1] + nima2 * i)#本作品作者吴宇航
            return list1#本作品作者吴宇航
        elif hahaha.count("/") == 0:#本作品作者吴宇航
            if "+" in hahaha:#本作品作者吴宇航
                nima = hahaha[hahaha.index("*") - 1]#本作品作者吴宇航
                i = 2#本作品作者吴宇航
                while hahaha.index("*") - i != -1:#本作品作者吴宇航
                    nima = hahaha[hahaha.index("*") - i] + nima#本作品作者吴宇航
                    i += 1#本作品作者吴宇航
                nima = float(nima)#本作品作者吴宇航
                hahaha = hahaha.replace(str(nima) + "*x+","")#本作品作者吴宇航
                nima2 = hahaha[hahaha.index("*") - 1]#本作品作者吴宇航
                i = 2#本作品作者吴宇航
                while hahaha.index("*") - i != -1:#本作品作者吴宇航
                    nima2 = hahaha[hahaha.index("*") - i] + nima2#本作品作者吴宇航
                    i += 1#本作品作者吴宇航
                nima2 = float(nima2)#本作品作者吴宇航
                zonghe = hahaha[len(hahaha) - 1]#本作品作者吴宇航
                i = 2#本作品作者吴宇航
                while hahaha[len(hahaha) - i] != "=":#本作品作者吴宇航
                    zonghe = hahaha[len(hahaha) - i] + nima#本作品作者吴宇航
                    i += 1#本作品作者吴宇航
                zonghe = int(zonghe)#本作品作者吴宇航
                for i in range(int(round(zonghe / nima,0))):#本作品作者吴宇航
                    if zonghe - i * nima % nima2 == 0:#本作品作者吴宇航
                        list1.append(i)#本作品作者吴宇航
                        list1.append(int((zonghe - i / nima) / nima2))#本作品作者吴宇航
                return list1#本作品作者吴宇航
            nima = hahaha[hahaha.index("*") - 1]#本作品作者吴宇航
            i = 2#本作品作者吴宇航
            while hahaha.index("*") - i != -1:#本作品作者吴宇航
                nima = hahaha[hahaha.index("*") - i] + nima#本作品作者吴宇航
                i += 1#本作品作者吴宇航
            nima = float(nima)#本作品作者吴宇航
            hahaha = hahaha.replace(str(nima) + "*x+","")#本作品作者吴宇航
            nima2 = hahaha[hahaha.index("*") - 1]#本作品作者吴宇航
            i = 2#本作品作者吴宇航
            while hahaha.index("*") - i != -1:#本作品作者吴宇航
                nima2 = hahaha[hahaha.index("*") - i] + nima2#本作品作者吴宇航
                i += 1#本作品作者吴宇航
            nima2 = float(nima2)#本作品作者吴宇航
            zonghe = hahaha[len(hahaha) - 1]#本作品作者吴宇航
            i = 2#本作品作者吴宇航
            while hahaha[len(hahaha) - i] != "=":#本作品作者吴宇航
                zonghe = hahaha[len(hahaha) - i] + nima#本作品作者吴宇航
                i += 1#本作品作者吴宇航
            zonghe = int(zonghe)#本作品作者吴宇航
            for i in range(int(round(zonghe / nima,0))):#本作品作者吴宇航
                if i * nima - zonghe % nima2 == 0:#本作品作者吴宇航
                    list1.append(i)#本作品作者吴宇航
                    list1.append(int((i / nima - zonghe) / nima2))#本作品作者吴宇航
            return list1#本作品作者吴宇航
        elif hahaha.count("/") == 1:#本作品作者吴宇航
            if hahaha.index("*") > hahaha.index("/") and "+" in hahaha:#本作品作者吴宇航
                nima = hahaha[hahaha.index("+") - 1]#本作品作者吴宇航
                i = 2#本作品作者吴宇航
                while hahaha[hahaha.index("+") - i] != "/":#本作品作者吴宇航
                    nima = hahaha[hahaha.index("+") - i] + nima#本作品作者吴宇航
                    i += 1#本作品作者吴宇航
                nima = float(nima)#本作品作者吴宇航
                nima2 = hahaha[hahaha.index("=") - 1]#本作品作者吴宇航
                i = 2#本作品作者吴宇航
                while hahaha[hahaha.index("=") - i] != "/":#本作品作者吴宇航
                    nima2 = hahaha[hahaha.index("=") - i] + nima2#本作品作者吴宇航
                    i += 1#本作品作者吴宇航
                nima2 = float(nima2)#本作品作者吴宇航
                zonghe = hahaha[len(hahaha) - 1]#本作品作者吴宇航
                i = 2#本作品作者吴宇航
                while hahaha[len(hahaha) - i] != "=":#本作品作者吴宇航
                    zonghe = hahaha[len(hahaha) - i] + nima#本作品作者吴宇航
                    i += 1#本作品作者吴宇航
                zonghe = int(zonghe)#本作品作者吴宇航
                for i in range(zonghe * nima * nima2):#本作品作者吴宇航
                    if i % nima == 0:#本作品作者吴宇航
                        list1.append(i)#本作品作者吴宇航
                        list1.append(int((zonghe - i / nima) * nima2))#本作品作者吴宇航
                return list1#本作品作者吴宇航
    def yiyuanerci(a):#本作品作者吴宇航
        x_x = a[a.index("x") - 1]#本作品作者吴宇航
        i = 2#本作品作者吴宇航
        while a.index("x") - i != -1:#本作品作者吴宇航
            x_x = a[a.index("x") - i] + x_x#本作品作者吴宇航
            i += 1#本作品作者吴宇航
        a = a.replace(x_x + "x^2","")#本作品作者吴宇航
        x_x2 = a[a.index("x") - 1]#本作品作者吴宇航
        i = 2#本作品作者吴宇航
        while a.index("x") - i != -1:#本作品作者吴宇航
            x_x2 = a[a.index("x") - i] + x_x2#本作品作者吴宇航
            i += 1#本作品作者吴宇航
        a = a.replace(x_x2 + "x","")#本作品作者吴宇航
        x_x3 = a[a.index("=") - 1]#本作品作者吴宇航
        i = 2#本作品作者吴宇航
        while a.index("=") - i != -1:#本作品作者吴宇航
            x_x3 = a[a.index("=") - i] + x_x3#本作品作者吴宇航
            i += 1#本作品作者吴宇航
        x_x,x_x2,x_x3 = float(x_x),float(x_x2),float(x_x3)#本作品作者吴宇航
        try:#本作品作者吴宇航
            haha = (-x_x2 + sqrt(x_x2 ** 2 - 4 * x_x * x_x3)) / (2 * x_x)#本作品作者吴宇航
            if haha % 1 == 0:#本作品作者吴宇航
                haha = int(haha)#本作品作者吴宇航
            if "." in str(haha):#本作品作者吴宇航
                a = ""#本作品作者吴宇航
                i = 2#本作品作者吴宇航
                while haha.index(".") - i != -1:#本作品作者吴宇航
                    a = str(haha)[haha.index(".") - i] + a#本作品作者吴宇航
                    i += 1#本作品作者吴宇航
                if len(haha) - len(a) - 1 < 5:#本作品作者吴宇航
                    haha = str(2 * x_x) + "分之" + str(-x_x2) + "+" + str(x_x2 ** 2 - 4 * x_x * x_x3) + "的平方根"#本作品作者吴宇航
            ahah = (-x_x2 - sqrt(x_x2 ** 2 - 4 * x_x * x_x3)) / (2 * x_x)#本作品作者吴宇航
            if ahah % 1 == 0:#本作品作者吴宇航
                ahah = int(ahah)#本作品作者吴宇航
            if "." in str(ahah):#本作品作者吴宇航
                a = ""#本作品作者吴宇航
                i = 2#本作品作者吴宇航
                while ahah.index(".") - i != -1:#本作品作者吴宇航
                    a = str(ahah)[ahah.index(".") - i] + a#本作品作者吴宇航
                    i += 1#本作品作者吴宇航
                if len(ahah) - len(a) - 1 < 5:#本作品作者吴宇航
                    ahah = str(2 * x_x) + "分之" + str(-x_x2) + "-" + str(x_x2 ** 2 - 4 * x_x * x_x3) + "的平方根"#本作品作者吴宇航
            return "x=" + str(haha) + "和" + str(ahah)#本作品作者吴宇航
        except:#本作品作者吴宇航
            print("这个方程没有解！")#本作品作者吴宇航
    def chunxunhuan(a):#本作品作者吴宇航
        if a[0] == "0":#本作品作者吴宇航
            nima = "9"#本作品作者吴宇航
            for i in range(len(a) - 3):#本作品作者吴宇航
                nima = nima + "9"#本作品作者吴宇航
            b = a[2]#本作品作者吴宇航
            for i in range(3,len(a)):#本作品作者吴宇航
                b = b + a[i]#本作品作者吴宇航
            b = int(b)#本作品作者吴宇航
            a = int(nima)#本作品作者吴宇航
            zuida = 0#本作品作者吴宇航
            suyinshu.clear()#本作品作者吴宇航
            if a % b == 0:#本作品作者吴宇航
                zuida = b#本作品作者吴宇航
            elif b % a == 0:#本作品作者吴宇航
                zuida = a#本作品作者吴宇航
            else:#本作品作者吴宇航
                d = a#本作品作者吴宇航
                e = b#本作品作者吴宇航
                list3.clear()#本作品作者吴宇航
                if d > e:#本作品作者吴宇航
                    if e % 2 == 0:#本作品作者吴宇航
                        o = e / 2#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        o = (e - 1) / 2 #本作品作者吴宇航
                else:#本作品作者吴宇航
                    if d % 2 == 0:#本作品作者吴宇航
                        o = d / 2#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        o = (d - 1) / 2#本作品作者吴宇航
                for i in range(1,int(o + 1)):#本作品作者吴宇航
                    if d % i == 0 and e % i == 0:#本作品作者吴宇航
                        if zhihe(i) == "N":#本作品作者吴宇航
                            suyinshu.append(i)#本作品作者吴宇航
                            if i != 1:#本作品作者吴宇航
                                list3.append(i)#本作品作者吴宇航
                            d = d / i#本作品作者吴宇航
                            e = e / i#本作品作者吴宇航
                while True:#本作品作者吴宇航
                    if len(list3) == 0:#本作品作者吴宇航
                        break#本作品作者吴宇航
                    list3.clear()#本作品作者吴宇航
                    if d > e:#本作品作者吴宇航
                        if e % 2 == 0:#本作品作者吴宇航
                            o = e / 2#本作品作者吴宇航
                        else:#本作品作者吴宇航
                            o = (e - 1) / 2 #本作品作者吴宇航
                    else:#本作品作者吴宇航
                        if d % 2 == 0:#本作品作者吴宇航
                            o = d / 2#本作品作者吴宇航
                        else:#本作品作者吴宇航
                            o = (d - 1) / 2#本作品作者吴宇航
                    for i in range(2,int(o + 1)):#本作品作者吴宇航
                        if d % i == 0 and e % i == 0:#本作品作者吴宇航
                            if zhihe(i) == "N":#本作品作者吴宇航
                                suyinshu.append(i)#本作品作者吴宇航
                                list3.append(i)#本作品作者吴宇航
                                d = d / i#本作品作者吴宇航
                                e = e / i#本作品作者吴宇航
                d = 1#本作品作者吴宇航
                for i in range(len(suyinshu)):#本作品作者吴宇航
                    if i != len(suyinshu) - 1:#本作品作者吴宇航
                        d = d * suyinshu[i]#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        zuida = suyinshu[i] * d#本作品作者吴宇航
                if zuida == 0:#本作品作者吴宇航
                    zuida = 1#本作品作者吴宇航
            return str(a // zuida) + "分之" + str(b // zuida)#本作品作者吴宇航
        else:#本作品作者吴宇航
            nima2 = a#本作品作者吴宇航
            nima = "9"#本作品作者吴宇航
            for i in range(len(a) - 2 - a.index(".")):#本作品作者吴宇航
                nima = nima + "9"#本作品作者吴宇航
            b = a[a.index(".") + 1]#本作品作者吴宇航
            for i in range(a.index(".") + 2,len(a)):#本作品作者吴宇航
                b = b + a[i]#本作品作者吴宇航
            b = int(b)#本作品作者吴宇航
            a = int(nima)#本作品作者吴宇航
            zuida = 0#本作品作者吴宇航
            suyinshu.clear()#本作品作者吴宇航
            if a % b == 0:#本作品作者吴宇航
                zuida = b#本作品作者吴宇航
            elif b % a == 0:#本作品作者吴宇航
                zuida = a#本作品作者吴宇航
            else:#本作品作者吴宇航
                d = a#本作品作者吴宇航
                e = b#本作品作者吴宇航
                list3.clear()#本作品作者吴宇航
                if d > e:#本作品作者吴宇航
                    if e % 2 == 0:#本作品作者吴宇航
                        o = e / 2#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        o = (e - 1) / 2 #本作品作者吴宇航
                else:#本作品作者吴宇航
                    if d % 2 == 0:#本作品作者吴宇航
                        o = d / 2#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        o = (d - 1) / 2#本作品作者吴宇航
                for i in range(1,int(o + 1)):#本作品作者吴宇航
                    if d % i == 0 and e % i == 0:#本作品作者吴宇航
                        if zhihe(i) == "N":#本作品作者吴宇航
                            suyinshu.append(i)#本作品作者吴宇航
                            if i != 1:#本作品作者吴宇航
                                list3.append(i)#本作品作者吴宇航
                            d = d / i#本作品作者吴宇航
                            e = e / i#本作品作者吴宇航
                while True:#本作品作者吴宇航
                    if len(list3) == 0:#本作品作者吴宇航
                        break#本作品作者吴宇航
                    list3.clear()#本作品作者吴宇航
                    if d > e:#本作品作者吴宇航
                        if e % 2 == 0:#本作品作者吴宇航
                            o = e / 2#本作品作者吴宇航
                        else:#本作品作者吴宇航
                            o = (e - 1) / 2 #本作品作者吴宇航
                    else:#本作品作者吴宇航
                        if d % 2 == 0:#本作品作者吴宇航
                            o = d / 2#本作品作者吴宇航
                        else:#本作品作者吴宇航
                            o = (d - 1) / 2#本作品作者吴宇航
                    for i in range(2,int(o + 1)):#本作品作者吴宇航
                        if d % i == 0 and e % i == 0:#本作品作者吴宇航
                            if zhihe(i) == "N":#本作品作者吴宇航
                                suyinshu.append(i)#本作品作者吴宇航
                                list3.append(i)#本作品作者吴宇航
                                d = d / i#本作品作者吴宇航
                                e = e / i#本作品作者吴宇航
                d = 1#本作品作者吴宇航
                for i in range(len(suyinshu)):#本作品作者吴宇航
                    if i != len(suyinshu) - 1:#本作品作者吴宇航
                        d = d * suyinshu[i]#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        zuida = suyinshu[i] * d#本作品作者吴宇航
                if zuida == 0:#本作品作者吴宇航
                    zuida = 1#本作品作者吴宇航
            print(str(nima2) + "又" + str(a // zuida) + "分之" + str(b // zuida))#本作品作者吴宇航
            #本作品作者吴宇航
    def find_all(data,s):#本作品作者吴宇航
        r_list = []#本作品作者吴宇航
        for i in range(len(data)):#本作品作者吴宇航
            if data[i] == s:#本作品作者吴宇航
                break#本作品作者吴宇航
            r_list.append(data[i])#本作品作者吴宇航
        return r_list#本作品作者吴宇航
    def bili(mode,a,bilishu):#本作品作者吴宇航
        zuida = 0#本作品作者吴宇航
        for i in bilishu:#本作品作者吴宇航
            zuida += i#本作品作者吴宇航
        zuida = a / zuida#本作品作者吴宇航
        for i in range(len(bilishu)):#本作品作者吴宇航
            bilishu[i] = bilishu[i] * zuida#本作品作者吴宇航
        return bilishu#本作品作者吴宇航
    def erjiedengcha(mode,shouxiang,dierxiang,gongcha,a):#本作品作者吴宇航
        if mode == 1:#本作品作者吴宇航
            if a == 1:#本作品作者吴宇航
                return shouxiang#本作品作者吴宇航
            nima = dierxiang - shouxiang#本作品作者吴宇航
            nima2 = shouxiang#本作品作者吴宇航
            for i in range(a - 2):#本作品作者吴宇航
                nima2 += nima#本作品作者吴宇航
                nima += gongcha#本作品作者吴宇航
            nima = nima2 + nima#本作品作者吴宇航
            i = 0#本作品作者吴宇航
            while True:#本作品作者吴宇航
                if not i < nima:#本作品作者吴宇航
                    break#本作品作者吴宇航
                i += 1#本作品作者吴宇航
            if nima - i == 0:#本作品作者吴宇航
                return int(nima)#本作品作者吴宇航
            else:#本作品作者吴宇航
                return nima#本作品作者吴宇航
        else:#本作品作者吴宇航
            if a == shouxiang:#本作品作者吴宇航
                return 1#本作品作者吴宇航
            nima = dierxiang - shouxiang#本作品作者吴宇航
            nima2 = shouxiang#本作品作者吴宇航
            i = 3#本作品作者吴宇航
            while True:#本作品作者吴宇航
                nima2 += nima#本作品作者吴宇航
                nima += gongcha#本作品作者吴宇航
                if nima2 == a:#本作品作者吴宇航
                    return i#本作品作者吴宇航
                if nima2 > a:#本作品作者吴宇航
                    return "N"#本作品作者吴宇航
                i += 1#本作品作者吴宇航
    def denbishulie(mode,shouxiang,gongbi,a):#本作品作者吴宇航
        if mode == 1:#本作品作者吴宇航
            return shouxiang * gongbi ** (a - 1)#本作品作者吴宇航
        if mode == 2:#本作品作者吴宇航
            if a == shouxiang:#本作品作者吴宇航
                return a#本作品作者吴宇航
            else:#本作品作者吴宇航
                ia = shouxiang#本作品作者吴宇航
                ai = shouxiang * gongbi#本作品作者吴宇航
                i = 3#本作品作者吴宇航
                while True:#本作品作者吴宇航
                    if i % 2 == 1:#本作品作者吴宇航
                        ia = ai * gongbi#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        ai = ia * gongbi#本作品作者吴宇航
                    if ia == a or ai == a:#本作品作者吴宇航
                        return i#本作品作者吴宇航
                    if ia > a or ai > a:#本作品作者吴宇航
                        return "N"#本作品作者吴宇航
                    i += 1#本作品作者吴宇航
    def dengchashulie(mode,shouxiang,gongcha,a):#本作品作者吴宇航
        if mode == 1:#本作品作者吴宇航
            nima = shouxiang + gongcha * (a - 1)#本作品作者吴宇航
            if nima % 1 == 0:#本作品作者吴宇航
                return int(nima)#本作品作者吴宇航
            else:#本作品作者吴宇航
                return nima#本作品作者吴宇航
        if mode == 2:#本作品作者吴宇航
            nima = (a - shouxiang) / gongcha + 1#本作品作者吴宇航
            if nima % 1 == 0:#本作品作者吴宇航
                return int(nima)#本作品作者吴宇航
            else:#本作品作者吴宇航
                return "N"#本作品作者吴宇航
        elif mode == 3:#本作品作者吴宇航
            nima = (shouxiang * 2 + gongcha * (a - 1)) * a / 2#本作品作者吴宇航
            if nima % 1 == 0:#本作品作者吴宇航
                return int(nima)#本作品作者吴宇航
            else:#本作品作者吴宇航
                return nima#本作品作者吴宇航
    def feibonaqi(mode,a):#本作品作者吴宇航
        if mode == "1":#本作品作者吴宇航
            if a == 1:#本作品作者吴宇航
                return 1#本作品作者吴宇航
            ia = 1#本作品作者吴宇航
            ai = 1#本作品作者吴宇航
            for i in range(a - 2):#本作品作者吴宇航
                if i % 2 == 0:#本作品作者吴宇航
                    ia += ai#本作品作者吴宇航
                else:#本作品作者吴宇航
                    ai += ia#本作品作者吴宇航
            if i % 2 == 0:#本作品作者吴宇航
                return ia#本作品作者吴宇航
            return ai#本作品作者吴宇航
        else:#本作品作者吴宇航
            if a == 1:#本作品作者吴宇航
                return 1#本作品作者吴宇航
            else:#本作品作者吴宇航
                i = 3#本作品作者吴宇航
                ia = 1#本作品作者吴宇航
                ai = 1#本作品作者吴宇航
                while True:#本作品作者吴宇航
                    if i % 2 == 1:#本作品作者吴宇航
                        ia += ai#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        ai += ia#本作品作者吴宇航
                    if ia == a or ai == a:#本作品作者吴宇航
                        return i#本作品作者吴宇航
                    if ia > a or ai > a:#本作品作者吴宇航
                        return "N"#本作品作者吴宇航
                    i += 1#本作品作者吴宇航
    def fenshudaxiao(a,b,c,d):#本作品作者吴宇航
        zuida = 0#本作品作者吴宇航
        suyinshu.clear()#本作品作者吴宇航
        if a % b == 0:#本作品作者吴宇航
            zuida = b#本作品作者吴宇航
        elif b % a == 0:#本作品作者吴宇航
            zuida = a#本作品作者吴宇航
        else:#本作品作者吴宇航
            z = a#本作品作者吴宇航
            e = b#本作品作者吴宇航
            list3.clear()#本作品作者吴宇航
            if z > e:#本作品作者吴宇航
                if e % 2 == 0:#本作品作者吴宇航
                    o = e / 2#本作品作者吴宇航
                else:#本作品作者吴宇航
                    o = (e - 1) / 2 #本作品作者吴宇航
            else:#本作品作者吴宇航
                if z % 2 == 0:#本作品作者吴宇航
                    o = z / 2#本作品作者吴宇航
                else:#本作品作者吴宇航
                    o = (z - 1) / 2#本作品作者吴宇航
            for i in range(2,int(o + 1)):#本作品作者吴宇航
                if z % i == 0 and e % i == 0:#本作品作者吴宇航
                    if zhihe(i) == "N":#本作品作者吴宇航
                        suyinshu.append(i)#本作品作者吴宇航
                        if i != 1:    #本作品作者吴宇航
                            list3.append(i)#本作品作者吴宇航
                        z = z / i#本作品作者吴宇航
                        e = e / i#本作品作者吴宇航
            while True:#本作品作者吴宇航
                if len(list3) == 0:#本作品作者吴宇航
                    break#本作品作者吴宇航
                list3.clear()#本作品作者吴宇航
                if z > e:#本作品作者吴宇航
                    if e % 2 == 0:#本作品作者吴宇航
                        o = e / 2#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        o = (e - 1) / 2 #本作品作者吴宇航
                else:#本作品作者吴宇航
                    if z % 2 == 0:#本作品作者吴宇航
                        o = z / 2#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        o = (z - 1) / 2#本作品作者吴宇航
                for i in range(2,int(o + 1)):#本作品作者吴宇航
                    if z % i == 0 and e % i == 0:#本作品作者吴宇航
                        if zhihe(i) == "N":#本作品作者吴宇航
                            suyinshu.append(i)#本作品作者吴宇航
                            list3.append(i)#本作品作者吴宇航
                            z = z / i#本作品作者吴宇航
                            e = e / i#本作品作者吴宇航
            z = 1#本作品作者吴宇航
            for i in range(len(suyinshu)):#本作品作者吴宇航
                if i != len(suyinshu) - 1:#本作品作者吴宇航
                    d = d * suyinshu[i]#本作品作者吴宇航
                else:#本作品作者吴宇航
                    zuida = suyinshu[i] * z#本作品作者吴宇航
            if zuida == 0:#本作品作者吴宇航
                zuida = 1#本作品作者吴宇航
        c = c * (b / zuida)#本作品作者吴宇航
        d = d * (a / zuida)#本作品作者吴宇航
        if c > d:#本作品作者吴宇航
            return 1#本作品作者吴宇航
        elif d > c:#本作品作者吴宇航
            return 2#本作品作者吴宇航
        else:#本作品作者吴宇航
            return "="#本作品作者吴宇航
    def zhihe(a):#本作品作者吴宇航
        if a == 1 or a == 0:#本作品作者吴宇航
            return "既不是素数也不是合数"#本作品作者吴宇航
        if a != 2 and a % 2 == 0:#本作品作者吴宇航
            return 2#本作品作者吴宇航
        for i in range(2,int(a / 2)):#本作品作者吴宇航
            if a == 2:#本作品作者吴宇航
                return "N"#本作品作者吴宇航
            if a % i == 0:#本作品作者吴宇航
                return i#本作品作者吴宇航
        return "N"#本作品作者吴宇航
    def fenjie(a):#本作品作者吴宇航
        suyinshu,d,sb,list3 = [],a,{},[]#本作品作者吴宇航
        for i in range(2,d):#本作品作者吴宇航
            if a % i == 0 and zhihe(i) == "N":#本作品作者吴宇航
                suyinshu.append(i)#本作品作者吴宇航
                list3.append(i)#本作品作者吴宇航
                d = d // i#本作品作者吴宇航
        while len(list3) != 0:#本作品作者吴宇航
            list3.clear()#本作品作者吴宇航
            for j in range(2,int(d) + 1):#本作品作者吴宇航
                if d % j == 0 and zhihe(j) == "N":#本作品作者吴宇航
                    suyinshu.append(j)#本作品作者吴宇航
                    list3.append(j)#本作品作者吴宇航
                    d = d / j#本作品作者吴宇航
        if len(suyinshu) == 0:#本作品作者吴宇航
            print("这玩意是个质数！")#本作品作者吴宇航
        else:#本作品作者吴宇航
            for i in suyinshu:#本作品作者吴宇航
                if i not in sb:#本作品作者吴宇航
                    sb[i] = suyinshu.count(i)#本作品作者吴宇航
            nima3 = ""#本作品作者吴宇航
            for nima in sb:#本作品作者吴宇航
                for i in range(sb[nima]):#本作品作者吴宇航
                    nima3 = nima3 + str(nima) + "×"#本作品作者吴宇航
            nima3 = nima3[:-1]#本作品作者吴宇航
            return str(a) + "=" + nima3#本作品作者吴宇航
    def common_factor(a,b):#本作品作者吴宇航
        zuida = 0#本作品作者吴宇航
        suyinshu.clear()#本作品作者吴宇航
        if a % b == 0:#本作品作者吴宇航
            return b#本作品作者吴宇航
        if b % a == 0:#本作品作者吴宇航
            return a#本作品作者吴宇航
        d = a#本作品作者吴宇航
        e = b#本作品作者吴宇航
        list3.clear()#本作品作者吴宇航
        if d > e:#本作品作者吴宇航
            if e % 2 == 0:#本作品作者吴宇航
                o = e / 2#本作品作者吴宇航
            else:#本作品作者吴宇航
                o = (e - 1) / 2 #本作品作者吴宇航
        else:#本作品作者吴宇航
            if d % 2 == 0:#本作品作者吴宇航
                o = d / 2#本作品作者吴宇航
            else:#本作品作者吴宇航
                o = (d - 1) / 2#本作品作者吴宇航
        for i in range(1,int(o + 1)):#本作品作者吴宇航
            if d % i == 0 and e % i == 0:#本作品作者吴宇航
                if zhihe(i) == "N":#本作品作者吴宇航
                    suyinshu.append(i)#本作品作者吴宇航
                    if i != 1:#本作品作者吴宇航
                        list3.append(i)#本作品作者吴宇航
                    d = d / i#本作品作者吴宇航
                    e = e / i#本作品作者吴宇航
        while True:#本作品作者吴宇航
            if len(list3) == 0:#本作品作者吴宇航
                break#本作品作者吴宇航
            list3.clear()#本作品作者吴宇航
            if d > e:#本作品作者吴宇航
                if e % 2 == 0:#本作品作者吴宇航
                    o = e / 2#本作品作者吴宇航
                else:#本作品作者吴宇航
                    o = (e - 1) / 2 #本作品作者吴宇航
            else:#本作品作者吴宇航
                if d % 2 == 0:#本作品作者吴宇航
                    o = d / 2#本作品作者吴宇航
                else:#本作品作者吴宇航
                    o = (d - 1) / 2#本作品作者吴宇航
            for i in range(2,int(o + 1)):#本作品作者吴宇航
                if d % i == 0 and e % i == 0:#本作品作者吴宇航
                    if zhihe(i) == "N":#本作品作者吴宇航
                        suyinshu.append(i)#本作品作者吴宇航
                        list3.append(i)#本作品作者吴宇航
                        d = d / i#本作品作者吴宇航
                        e = e / i#本作品作者吴宇航
        d = 1#本作品作者吴宇航
        for i in range(len(suyinshu)):#本作品作者吴宇航
            if i != len(suyinshu) - 1:#本作品作者吴宇航
                d = d * suyinshu[i]#本作品作者吴宇航
            else:#本作品作者吴宇航
                zuida = suyinshu[i] * d#本作品作者吴宇航
        if zuida == 0:#本作品作者吴宇航
            zuida = 1#本作品作者吴宇航
        return zuida    #本作品作者吴宇航
    def zuixiao(a,b):#本作品作者吴宇航
        zuida = 0#本作品作者吴宇航
        suyinshu.clear()#本作品作者吴宇航
        if a % b == 0:#本作品作者吴宇航
            zuida = b#本作品作者吴宇航
        elif b % a == 0:#本作品作者吴宇航
            zuida = a#本作品作者吴宇航
        else:#本作品作者吴宇航
            d = a#本作品作者吴宇航
            e = b#本作品作者吴宇航
            list3.clear()#本作品作者吴宇航
            if d > e:#本作品作者吴宇航
                if e % 2 == 0:#本作品作者吴宇航
                    o = e / 2#本作品作者吴宇航
                else:#本作品作者吴宇航
                    o = (e - 1) / 2 #本作品作者吴宇航
            else:#本作品作者吴宇航
                if d % 2 == 0:#本作品作者吴宇航
                    o = d / 2#本作品作者吴宇航
                else:#本作品作者吴宇航
                    o = (d - 1) / 2#本作品作者吴宇航
            for i in range(1,int(o + 1)):#本作品作者吴宇航
                if d % i == 0 and e % i == 0:#本作品作者吴宇航
                    if zhihe(i) == "N":#本作品作者吴宇航
                        suyinshu.append(i)#本作品作者吴宇航
                        if i != 1:#本作品作者吴宇航
                            list3.append(i)#本作品作者吴宇航
                        d = d / i#本作品作者吴宇航
                        e = e / i#本作品作者吴宇航
            while True:#本作品作者吴宇航
                if len(list3) == 0:#本作品作者吴宇航
                    break#本作品作者吴宇航
                list3.clear()#本作品作者吴宇航
                if d > e:#本作品作者吴宇航
                    if e % 2 == 0:#本作品作者吴宇航
                        o = e / 2#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        o = (e - 1) / 2 #本作品作者吴宇航
                else:#本作品作者吴宇航
                    if d % 2 == 0:#本作品作者吴宇航
                        o = d / 2#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        o = (d - 1) / 2#本作品作者吴宇航
                for i in range(2,int(o + 1)):#本作品作者吴宇航
                    if d % i == 0 and e % i == 0:#本作品作者吴宇航
                        if zhihe(i) == "N":#本作品作者吴宇航
                            suyinshu.append(i)#本作品作者吴宇航
                            list3.append(i)#本作品作者吴宇航
                            d = d / i#本作品作者吴宇航
                            e = e / i#本作品作者吴宇航
            d = 1#本作品作者吴宇航
            for i in range(len(suyinshu)):#本作品作者吴宇航
                if i != len(suyinshu) - 1:#本作品作者吴宇航
                    d = d * suyinshu[i]#本作品作者吴宇航
                else:#本作品作者吴宇航
                    zuida = suyinshu[i] * d#本作品作者吴宇航
            if zuida == 0:#本作品作者吴宇航
                zuida = 1#本作品作者吴宇航
        return zuida * (a / zuida) * (b / zuida)#本作品作者吴宇航
    def fenshuyunsuan(mode,a,b,c,d):#本作品作者吴宇航
        if mode == "1":#本作品作者吴宇航
            zuida = 0#本作品作者吴宇航
            suyinshu.clear()#本作品作者吴宇航
            if a % b == 0:#本作品作者吴宇航
                zuida = b#本作品作者吴宇航
            elif b % a == 0:#本作品作者吴宇航
                zuida = a#本作品作者吴宇航
            else:#本作品作者吴宇航
                z = a#本作品作者吴宇航
                e = b#本作品作者吴宇航
                list3.clear()#本作品作者吴宇航
                if z > e:#本作品作者吴宇航
                    if e % 2 == 0:#本作品作者吴宇航
                        o = e / 2#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        o = (e - 1) / 2 #本作品作者吴宇航
                else:#本作品作者吴宇航
                    if z % 2 == 0:#本作品作者吴宇航
                        o = z / 2#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        o = (z - 1) / 2#本作品作者吴宇航
                for i in range(2,int(o + 1)):#本作品作者吴宇航
                    if z % i == 0 and e % i == 0:#本作品作者吴宇航
                        if zhihe(i) == "N":#本作品作者吴宇航
                            suyinshu.append(i)#本作品作者吴宇航
                            if i != 1:    #本作品作者吴宇航
                                list3.append(i)#本作品作者吴宇航
                            z = z / i#本作品作者吴宇航
                            e = e / i#本作品作者吴宇航
                while True:#本作品作者吴宇航
                    if len(list3) == 0:#本作品作者吴宇航
                        break#本作品作者吴宇航
                    list3.clear()#本作品作者吴宇航
                    if z > e:#本作品作者吴宇航
                        if e % 2 == 0:#本作品作者吴宇航
                            o = e / 2#本作品作者吴宇航
                        else:#本作品作者吴宇航
                            o = (e - 1) / 2 #本作品作者吴宇航
                    else:#本作品作者吴宇航
                        if z % 2 == 0:#本作品作者吴宇航
                            o = z / 2#本作品作者吴宇航
                        else:#本作品作者吴宇航
                            o = (z - 1) / 2#本作品作者吴宇航
                    for i in range(2,int(o + 1)):#本作品作者吴宇航
                        if z % i == 0 and e % i == 0:#本作品作者吴宇航
                            if zhihe(i) == "N":#本作品作者吴宇航
                                suyinshu.append(i)#本作品作者吴宇航
                                list3.append(i)#本作品作者吴宇航
                                z = z / i#本作品作者吴宇航
                                e = e / i#本作品作者吴宇航
            z = 1#本作品作者吴宇航
            for i in range(len(suyinshu)):#本作品作者吴宇航
                if i != len(suyinshu) - 1:#本作品作者吴宇航
                    d = d * suyinshu[i]#本作品作者吴宇航
                else:#本作品作者吴宇航
                    zuida = suyinshu[i] * z#本作品作者吴宇航
            if zuida == 0:#本作品作者吴宇航
                zuida = 1#本作品作者吴宇航
            e = zuida * (a / zuida) * (b / zuida)#本作品作者吴宇航
            f = c * (b / zuida) + d * (a / zuida)#本作品作者吴宇航
            zuida = 0#本作品作者吴宇航
            suyinshu.clear()#本作品作者吴宇航
            if e % f == 0:#本作品作者吴宇航
                zuida = f#本作品作者吴宇航
            elif f % e == 0:#本作品作者吴宇航
                zuida = e#本作品作者吴宇航
            else:#本作品作者吴宇航
                h = e#本作品作者吴宇航
                i = f#本作品作者吴宇航
                list3.clear()#本作品作者吴宇航
                if i > h:#本作品作者吴宇航
                    if h % 2 == 0:#本作品作者吴宇航
                        o = h / 2#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        o = (h - 1) / 2 #本作品作者吴宇航
                else:#本作品作者吴宇航
                    if i % 2 == 0:#本作品作者吴宇航
                        o = i / 2#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        o = (i - 1) / 2#本作品作者吴宇航
                for j in range(1,int(o + 1)):#本作品作者吴宇航
                    if h % j == 0 and i % j == 0:#本作品作者吴宇航
                        if zhihe(j) == "N":#本作品作者吴宇航
                            suyinshu.append(j)#本作品作者吴宇航
                            if j != 1:#本作品作者吴宇航
                                list3.append(j)#本作品作者吴宇航
                            h = h / j#本作品作者吴宇航
                            i = i / j#本作品作者吴宇航
                while True:#本作品作者吴宇航
                    if len(list3) == 0:#本作品作者吴宇航
                        break#本作品作者吴宇航
                    list3.clear()#本作品作者吴宇航
                    if h > i:#本作品作者吴宇航
                        if e % 2 == 0:#本作品作者吴宇航
                            o = i / 2#本作品作者吴宇航
                        else:#本作品作者吴宇航
                            o = (i - 1) / 2 #本作品作者吴宇航
                    else:#本作品作者吴宇航
                        if d % 2 == 0:#本作品作者吴宇航
                            o = h / 2#本作品作者吴宇航
                        else:#本作品作者吴宇航
                            o = (h - 1) / 2#本作品作者吴宇航
                    for j in range(2,int(o + 1)):#本作品作者吴宇航
                        if h % j == 0 and i % j == 0:#本作品作者吴宇航
                            if zhihe(j) == "N":#本作品作者吴宇航
                                suyinshu.append(j)#本作品作者吴宇航
                                list3.append(j)#本作品作者吴宇航
                                h = h / j#本作品作者吴宇航
                                i = i / j#本作品作者吴宇航
                i = 1#本作品作者吴宇航
                for j in range(len(suyinshu)):#本作品作者吴宇航
                    if j != len(suyinshu) - 1:#本作品作者吴宇航
                        i = i * suyinshu[j]#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        zuida = suyinshu[j] * i#本作品作者吴宇航
                if zuida == 0:#本作品作者吴宇航
                    zuida = 1#本作品作者吴宇航
            return str(int(e / zuida)) + "分之" + str(int(f / zuida))#本作品作者吴宇航
        elif mode == "2":#本作品作者吴宇航
            nima = fenshudaxiao(a,b,c,d)#本作品作者吴宇航
            if nima == "=":#本作品作者吴宇航
                return 0#本作品作者吴宇航
            else:#本作品作者吴宇航
                zuida = 0#本作品作者吴宇航
                suyinshu.clear()#本作品作者吴宇航
                if a % b == 0:#本作品作者吴宇航
                    zuida = b#本作品作者吴宇航
                elif b % a == 0:#本作品作者吴宇航
                    zuida = a#本作品作者吴宇航
                else:#本作品作者吴宇航
                    z = a#本作品作者吴宇航
                    e = b#本作品作者吴宇航
                    list3.clear()#本作品作者吴宇航
                    if z > e:#本作品作者吴宇航
                        if e % 2 == 0:#本作品作者吴宇航
                            o = e / 2#本作品作者吴宇航
                        else:#本作品作者吴宇航
                            o = (e - 1) / 2 #本作品作者吴宇航
                    else:#本作品作者吴宇航
                        if z % 2 == 0:#本作品作者吴宇航
                            o = z / 2#本作品作者吴宇航
                        else:#本作品作者吴宇航
                            o = (z - 1) / 2#本作品作者吴宇航
                    for i in range(1,int(o + 1)):#本作品作者吴宇航
                        if z % i == 0 and e % i == 0:#本作品作者吴宇航
                            if zhihe(i) == "N":#本作品作者吴宇航
                                suyinshu.append(i)#本作品作者吴宇航
                                if i != 1:#本作品作者吴宇航
                                    list3.append(i)#本作品作者吴宇航
                                z = z / i#本作品作者吴宇航
                                e = e / i#本作品作者吴宇航
                    while True:#本作品作者吴宇航
                        if len(list3) == 0:#本作品作者吴宇航
                            break#本作品作者吴宇航
                        list3.clear()#本作品作者吴宇航
                        if z > e:#本作品作者吴宇航
                            if e % 2 == 0:#本作品作者吴宇航
                                o = e / 2#本作品作者吴宇航
                            else:#本作品作者吴宇航
                                o = (e - 1) / 2 #本作品作者吴宇航
                        else:#本作品作者吴宇航
                            if z % 2 == 0:#本作品作者吴宇航
                                o = z / 2#本作品作者吴宇航
                            else:#本作品作者吴宇航
                                o = (z - 1) / 2#本作品作者吴宇航
                        for i in range(2,int(o + 1)):#本作品作者吴宇航
                            if z % i == 0 and e % i == 0:#本作品作者吴宇航
                                if zhihe(i) == "N":#本作品作者吴宇航
                                    suyinshu.append(i)#本作品作者吴宇航
                                    list3.append(i)#本作品作者吴宇航
                                    z = z / i#本作品作者吴宇航
                                    e = e / i#本作品作者吴宇航
                z = 1#本作品作者吴宇航
                for i in range(len(suyinshu)):#本作品作者吴宇航
                    if i != len(suyinshu) - 1:#本作品作者吴宇航
                        d = d * suyinshu[i]#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        zuida = suyinshu[i] * z#本作品作者吴宇航
                if zuida == 0:#本作品作者吴宇航
                    zuida = 1#本作品作者吴宇航
                #本作品作者吴宇航
                e = zuida * (a / zuida) * (b / zuida)#本作品作者吴宇航
                f = c * (b / zuida) - d * (a / zuida)#本作品作者吴宇航
                zuida = 0#本作品作者吴宇航
                suyinshu.clear()#本作品作者吴宇航
                if e % f == 0:#本作品作者吴宇航
                    zuida = f#本作品作者吴宇航
                elif f % e == 0:#本作品作者吴宇航
                    zuida = e#本作品作者吴宇航
                else:#本作品作者吴宇航
                    h = e#本作品作者吴宇航
                    i = f#本作品作者吴宇航
                    list3.clear()#本作品作者吴宇航
                    if i > h:#本作品作者吴宇航
                        if h % 2 == 0:#本作品作者吴宇航
                            o = h / 2#本作品作者吴宇航
                        else:#本作品作者吴宇航
                            o = (h - 1) / 2 #本作品作者吴宇航
                    else:#本作品作者吴宇航
                        if i % 2 == 0:#本作品作者吴宇航
                            o = i / 2#本作品作者吴宇航
                        else:#本作品作者吴宇航
                            o = (i - 1) / 2#本作品作者吴宇航
                    for j in range(1,int(o + 1)):#本作品作者吴宇航
                        if h % j == 0 and i % j == 0:#本作品作者吴宇航
                            if zhihe(j) == "N":#本作品作者吴宇航
                                suyinshu.append(j)#本作品作者吴宇航
                                if j != 1:#本作品作者吴宇航
                                    list3.append(j)#本作品作者吴宇航
                                h = h / j#本作品作者吴宇航
                                i = i / j#本作品作者吴宇航
                    while True:#本作品作者吴宇航
                        if len(list3) == 0:#本作品作者吴宇航
                            break#本作品作者吴宇航
                        list3.clear()#本作品作者吴宇航
                        if h > i:#本作品作者吴宇航
                            if e % 2 == 0:#本作品作者吴宇航
                                o = i / 2#本作品作者吴宇航
                            else:#本作品作者吴宇航
                                o = (i - 1) / 2 #本作品作者吴宇航
                        else:#本作品作者吴宇航
                            if d % 2 == 0:#本作品作者吴宇航
                                o = h / 2#本作品作者吴宇航
                            else:#本作品作者吴宇航
                                o = (h - 1) / 2#本作品作者吴宇航
                        for j in range(2,int(o + 1)):#本作品作者吴宇航
                            if h % j == 0 and i % j == 0:#本作品作者吴宇航
                                if zhihe(j) == "N":#本作品作者吴宇航
                                    suyinshu.append(j)#本作品作者吴宇航
                                    list3.append(j)#本作品作者吴宇航
                                    h = h / j#本作品作者吴宇航
                                    i = i / j#本作品作者吴宇航
                    i = 1#本作品作者吴宇航
                    for j in range(len(suyinshu)):#本作品作者吴宇航
                        if j != len(suyinshu) - 1:#本作品作者吴宇航
                            i = i * suyinshu[j]#本作品作者吴宇航
                        else:#本作品作者吴宇航
                            zuida = suyinshu[j] * i#本作品作者吴宇航
                    if zuida == 0:#本作品作者吴宇航
                        zuida = 1#本作品作者吴宇航
                return str(int(e / zuida)) + "分之" + str(int(f / zuida))#本作品作者吴宇航
        if mode == "3":#本作品作者吴宇航
            e = a * b#本作品作者吴宇航
            f = c * d#本作品作者吴宇航
            zuida = 0#本作品作者吴宇航
            suyinshu.clear()#本作品作者吴宇航
            if e % f == 0:#本作品作者吴宇航
                zuida = f#本作品作者吴宇航
            elif f % e == 0:#本作品作者吴宇航
                zuida = e#本作品作者吴宇航
            else:#本作品作者吴宇航
                h = e#本作品作者吴宇航
                i = f#本作品作者吴宇航
                list3.clear()#本作品作者吴宇航
                if i > h:#本作品作者吴宇航
                    if h % 2 == 0:#本作品作者吴宇航
                        o = h / 2#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        o = (h - 1) / 2 #本作品作者吴宇航
                else:#本作品作者吴宇航
                    if i % 2 == 0:#本作品作者吴宇航
                        o = i / 2#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        o = (i - 1) / 2#本作品作者吴宇航
                for j in range(1,int(o + 1)):#本作品作者吴宇航
                    if h % j == 0 and i % j == 0:#本作品作者吴宇航
                        if zhihe(j) == "N":#本作品作者吴宇航
                            suyinshu.append(j)#本作品作者吴宇航
                            if j != 1:#本作品作者吴宇航
                                list3.append(j)#本作品作者吴宇航
                            h = h / j#本作品作者吴宇航
                            i = i / j#本作品作者吴宇航
                while True:#本作品作者吴宇航
                    if len(list3) == 0:#本作品作者吴宇航
                        break#本作品作者吴宇航
                    list3.clear()#本作品作者吴宇航
                    if h > i:#本作品作者吴宇航
                        if e % 2 == 0:#本作品作者吴宇航
                            o = i / 2#本作品作者吴宇航
                        else:#本作品作者吴宇航
                            o = (i - 1) / 2 #本作品作者吴宇航
                    else:#本作品作者吴宇航
                        if d % 2 == 0:#本作品作者吴宇航
                            o = h / 2#本作品作者吴宇航
                        else:#本作品作者吴宇航
                            o = (h - 1) / 2#本作品作者吴宇航
                    for j in range(2,int(o + 1)):#本作品作者吴宇航
                        if h % j == 0 and i % j == 0:#本作品作者吴宇航
                            if zhihe(j) == "N":#本作品作者吴宇航
                                suyinshu.append(j)#本作品作者吴宇航
                                list3.append(j)#本作品作者吴宇航
                                h = h / j#本作品作者吴宇航
                                i = i / j#本作品作者吴宇航
                i = 1#本作品作者吴宇航
                for j in range(len(suyinshu)):#本作品作者吴宇航
                    if j != len(suyinshu) - 1:#本作品作者吴宇航
                        i = i * suyinshu[j]#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        zuida = suyinshu[j] * i#本作品作者吴宇航
                if zuida == 0:#本作品作者吴宇航
                    zuida = 1#本作品作者吴宇航
            return str(int(e / zuida)) + "分之" + str(int(f / zuida))#本作品作者吴宇航
        if mode == "4":#本作品作者吴宇航
            e = a * d#本作品作者吴宇航
            f = b * c#本作品作者吴宇航
            zuida = 0#本作品作者吴宇航
            suyinshu.clear()#本作品作者吴宇航
            if e % f == 0:#本作品作者吴宇航
                zuida = f#本作品作者吴宇航
            elif f % e == 0:#本作品作者吴宇航
                zuida = e#本作品作者吴宇航
            else:#本作品作者吴宇航
                h = e#本作品作者吴宇航
                i = f#本作品作者吴宇航
                list3.clear()#本作品作者吴宇航
                if i > h:#本作品作者吴宇航
                    if h % 2 == 0:#本作品作者吴宇航
                        o = h / 2#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        o = (h - 1) / 2 #本作品作者吴宇航
                else:#本作品作者吴宇航
                    if i % 2 == 0:#本作品作者吴宇航
                        o = i / 2#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        o = (i - 1) / 2#本作品作者吴宇航
                for j in range(1,int(o + 1)):#本作品作者吴宇航
                    if h % j == 0 and i % j == 0:#本作品作者吴宇航
                        if zhihe(j) == "N":#本作品作者吴宇航
                            suyinshu.append(j)#本作品作者吴宇航
                            if j != 1:#本作品作者吴宇航
                                list3.append(j)#本作品作者吴宇航
                            h = h / j#本作品作者吴宇航
                            i = i / j#本作品作者吴宇航
                while True:#本作品作者吴宇航
                    if len(list3) == 0:#本作品作者吴宇航
                        break#本作品作者吴宇航
                    list3.clear()#本作品作者吴宇航
                    if h > i:#本作品作者吴宇航
                        if e % 2 == 0:#本作品作者吴宇航
                            o = i / 2#本作品作者吴宇航
                        else:#本作品作者吴宇航
                            o = (i - 1) / 2 #本作品作者吴宇航
                    else:#本作品作者吴宇航
                        if d % 2 == 0:#本作品作者吴宇航
                            o = h / 2#本作品作者吴宇航
                        else:#本作品作者吴宇航
                            o = (h - 1) / 2#本作品作者吴宇航
                    for j in range(2,int(o + 1)):#本作品作者吴宇航
                        if h % j == 0 and i % j == 0:#本作品作者吴宇航
                            if zhihe(j) == "N":#本作品作者吴宇航
                                suyinshu.append(j)#本作品作者吴宇航
                                list3.append(j)#本作品作者吴宇航
                                h = h / j#本作品作者吴宇航
                                i = i / j#本作品作者吴宇航
                i = 1#本作品作者吴宇航
                for j in range(len(suyinshu)):#本作品作者吴宇航
                    if j != len(suyinshu) - 1:#本作品作者吴宇航
                        i = i * suyinshu[j]#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        zuida = suyinshu[j] * i#本作品作者吴宇航
                if zuida == 0:#本作品作者吴宇航
                    zuida = 1#本作品作者吴宇航
            return str(int(e / zuida)) + "分子" + str(int(f / zuida))#本作品作者吴宇航
    def fenshudagongyin(a,b,c,d):#本作品作者吴宇航
        zuida = 0#本作品作者吴宇航
        suyinshu.clear()#本作品作者吴宇航
        if a % b == 0:#本作品作者吴宇航
            zuida = b#本作品作者吴宇航
        elif b % a == 0:#本作品作者吴宇航
            zuida = a#本作品作者吴宇航
        else:#本作品作者吴宇航
            z = a#本作品作者吴宇航
            e = b#本作品作者吴宇航
            list3.clear()#本作品作者吴宇航
            if z > e:#本作品作者吴宇航
                if e % 2 == 0:#本作品作者吴宇航
                    o = e / 2#本作品作者吴宇航
                else:#本作品作者吴宇航
                    o = (e - 1) / 2 #本作品作者吴宇航
            else:#本作品作者吴宇航
                if z % 2 == 0:#本作品作者吴宇航
                    o = z / 2#本作品作者吴宇航
                else:#本作品作者吴宇航
                    o = (z - 1) / 2#本作品作者吴宇航
            for i in range(2,int(o + 1)):#本作品作者吴宇航
                if z % i == 0 and e % i == 0:#本作品作者吴宇航
                    if zhihe(i) == "N":#本作品作者吴宇航
                        suyinshu.append(i)#本作品作者吴宇航
                        if i != 1:    #本作品作者吴宇航
                            list3.append(i)#本作品作者吴宇航
                        z = z / i#本作品作者吴宇航
                        e = e / i#本作品作者吴宇航
            while True:#本作品作者吴宇航
                if len(list3) == 0:#本作品作者吴宇航
                    break#本作品作者吴宇航
                list3.clear()#本作品作者吴宇航
                if z > e:#本作品作者吴宇航
                    if e % 2 == 0:#本作品作者吴宇航
                        o = e / 2#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        o = (e - 1) / 2 #本作品作者吴宇航
                else:#本作品作者吴宇航
                    if z % 2 == 0:#本作品作者吴宇航
                        o = z / 2#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        o = (z - 1) / 2#本作品作者吴宇航
                for i in range(2,int(o + 1)):#本作品作者吴宇航
                    if z % i == 0 and e % i == 0:#本作品作者吴宇航
                        if zhihe(i) == "N":#本作品作者吴宇航
                            suyinshu.append(i)#本作品作者吴宇航
                            list3.append(i)#本作品作者吴宇航
                            z = z / i#本作品作者吴宇航
                            e = e / i#本作品作者吴宇航
        z = 1#本作品作者吴宇航
        for i in range(len(suyinshu)):#本作品作者吴宇航
            if i != len(suyinshu) - 1:#本作品作者吴宇航
                d = d * suyinshu[i]#本作品作者吴宇航
            else:#本作品作者吴宇航
                zuida = suyinshu[i] * z#本作品作者吴宇航
        if zuida == 0:#本作品作者吴宇航
            zuida = 1#本作品作者吴宇航
        a1 = a * (b / zuida)#本作品作者吴宇航
        b1 = a1#本作品作者吴宇航
        c = c * (b / zuida)#本作品作者吴宇航
        d = d * (a / zuida)#本作品作者吴宇航
        zuida = 0#本作品作者吴宇航
        suyinshu.clear()#本作品作者吴宇航
        if c % d == 0:#本作品作者吴宇航
            zuida = d#本作品作者吴宇航
        elif d % c == 0:#本作品作者吴宇航
            zuida = c#本作品作者吴宇航
        else:#本作品作者吴宇航
            h = c#本作品作者吴宇航
            i = d#本作品作者吴宇航
            list3.clear()#本作品作者吴宇航
            if h > i:#本作品作者吴宇航
                if i % 2 == 0:#本作品作者吴宇航
                    o = i / 2#本作品作者吴宇航
                else:#本作品作者吴宇航
                    o = (i - 1) / 2 #本作品作者吴宇航
            else:#本作品作者吴宇航
                if h % 2 == 0:#本作品作者吴宇航
                    o = h / 2#本作品作者吴宇航
                else:#本作品作者吴宇航
                    o = (h - 1) / 2#本作品作者吴宇航
            for j in range(1,int(o + 1)):#本作品作者吴宇航
                if h % j == 0 and i % j == 0:#本作品作者吴宇航
                    if zhihe(j) == "N":#本作品作者吴宇航
                        suyinshu.append(j)#本作品作者吴宇航
                        if j != 1:#本作品作者吴宇航
                            list3.append(j)#本作品作者吴宇航
                        h = h / j#本作品作者吴宇航
                        i = i / j#本作品作者吴宇航
            while True:#本作品作者吴宇航
                if len(list3) == 0:#本作品作者吴宇航
                    break#本作品作者吴宇航
                list3.clear()#本作品作者吴宇航
                if h > i:#本作品作者吴宇航
                    if i % 2 == 0:#本作品作者吴宇航
                        o = i / 2#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        o = (i - 1) / 2 #本作品作者吴宇航
                else:#本作品作者吴宇航
                    if h % 2 == 0:#本作品作者吴宇航
                        o = h / 2#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        o = (h - 1) / 2#本作品作者吴宇航
                for j in range(2,int(o + 1)):#本作品作者吴宇航
                    if h % j == 0 and i % j == 0:#本作品作者吴宇航
                        if zhihe(j) == "N":#本作品作者吴宇航
                            suyinshu.append(j)#本作品作者吴宇航
                            list3.append(j)#本作品作者吴宇航
                            h = h / j#本作品作者吴宇航
                            i = i / j#本作品作者吴宇航
            z = 1#本作品作者吴宇航
            for j in range(len(suyinshu)):#本作品作者吴宇航
                if j != len(suyinshu) - 1:#本作品作者吴宇航
                    z = z * suyinshu[j]#本作品作者吴宇航
                else:#本作品作者吴宇航
                    zuida = suyinshu[j] * z#本作品作者吴宇航
            if zuida == 0:#本作品作者吴宇航
                zuida = 1#本作品作者吴宇航
        b = zuida#本作品作者吴宇航
        print(b)#本作品作者吴宇航
        zuida = 0#本作品作者吴宇航
        suyinshu.clear()#本作品作者吴宇航
        if a1 % b == 0:#本作品作者吴宇航
            zuida = b#本作品作者吴宇航
        elif b % a1 == 0:#本作品作者吴宇航
            zuida = a1#本作品作者吴宇航
        else:#本作品作者吴宇航
            d = a1#本作品作者吴宇航
            e = b#本作品作者吴宇航
            list3.clear()#本作品作者吴宇航
            if d > e:#本作品作者吴宇航
                if e % 2 == 0:#本作品作者吴宇航
                    o = e / 2#本作品作者吴宇航
                else:#本作品作者吴宇航
                    o = (e - 1) / 2 #本作品作者吴宇航
            else:#本作品作者吴宇航
                if d % 2 == 0:#本作品作者吴宇航
                    o = d / 2#本作品作者吴宇航
                else:#本作品作者吴宇航
                    o = (d - 1) / 2#本作品作者吴宇航
            for i in range(1,int(o + 1)):#本作品作者吴宇航
                if d % i == 0 and e % i == 0:#本作品作者吴宇航
                    if zhihe(i) == "N":#本作品作者吴宇航
                        suyinshu.append(i)#本作品作者吴宇航
                        if i != 1:#本作品作者吴宇航
                            list3.append(i)#本作品作者吴宇航
                        d = d / i#本作品作者吴宇航
                        e = e / i#本作品作者吴宇航
            while True:#本作品作者吴宇航
                if len(list3) == 0:#本作品作者吴宇航
                    break#本作品作者吴宇航
                list3.clear()#本作品作者吴宇航
                if d > e:#本作品作者吴宇航
                    if e % 2 == 0:#本作品作者吴宇航
                        o = e / 2#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        o = (e - 1) / 2 #本作品作者吴宇航
                else:#本作品作者吴宇航
                    if d % 2 == 0:#本作品作者吴宇航
                        o = d / 2#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        o = (d - 1) / 2#本作品作者吴宇航
                for i in range(2,int(o + 1)):#本作品作者吴宇航
                    if d % i == 0 and e % i == 0:#本作品作者吴宇航
                        if zhihe(i) == "N":#本作品作者吴宇航
                            suyinshu.append(i)#本作品作者吴宇航
                            list3.append(i)#本作品作者吴宇航
                            d = d / i#本作品作者吴宇航
                            e = e / i#本作品作者吴宇航
            d = 1#本作品作者吴宇航
            for i in range(len(suyinshu)):#本作品作者吴宇航
                if i != len(suyinshu) - 1:#本作品作者吴宇航
                    d = d * suyinshu[i]#本作品作者吴宇航
                else:#本作品作者吴宇航
                    zuida = suyinshu[i] * d#本作品作者吴宇航
            if zuida == 0:#本作品作者吴宇航
                zuida = 1#本作品作者吴宇航
        return str(a1 // zuida) + "分之" + str(b // zuida)#本作品作者吴宇航
    def pingmianjihe(mode,a,b,c):#本作品作者吴宇航
        if mode == "等边三角形":#本作品作者吴宇航
            return sqrt(3) / 4 * a ** 2#本作品作者吴宇航
        if mode == "梯形":#本作品作者吴宇航
            return (a + b) * c / 2#本作品作者吴宇航
        if mode == "三角形":#本作品作者吴宇航
            return a * b / 2#本作品作者吴宇航
        if mode == "圆形面积":#本作品作者吴宇航
            return a ** 2 * 3.14#本作品作者吴宇航
        if mode == "圆形周长":#本作品作者吴宇航
            return a * 2 * 3.14#本作品作者吴宇航
        if mode == "扇形面积":#本作品作者吴宇航
            return a ** 2 * 3.14 / 360 * b#本作品作者吴宇航
        if mode == "扇形周长":#本作品作者吴宇航
            return 2 * a + a * 2 * 3.14 / 360 * b#本作品作者吴宇航
        if mode == "长方形":#本作品作者吴宇航
            return a * b#本作品作者吴宇航
    def izhihe1():#本作品作者吴宇航
        izhihewin = Tk()#本作品作者吴宇航
        izhihewin.title("质数合数判断")#本作品作者吴宇航
        izhihewin.geometry("400x300")#本作品作者吴宇航
        wo = Label(izhihewin,text = "请输入要计算的数",width = 15)#本作品作者吴宇航
        wo.pack(side = TOP)#本作品作者吴宇航
        var1 = Entry(izhihewin)#本作品作者吴宇航
        var1.pack(side = TOP,expand = True)#本作品作者吴宇航
        def izhihe2():#本作品作者吴宇航
            if "妈" in var1.get():#本作品作者吴宇航
                messagebox.showwarning("","我不是你妈，我是你爹！")#本作品作者吴宇航
            else:#本作品作者吴宇航
                try:#本作品作者吴宇航
                    if "妈" in var1.get():#本作品作者吴宇航
                        messagebox.showwarning("","我不是你妈，我是你爹！")#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        jieguo1 = zhihe(int(var1.get()))#本作品作者吴宇航
                        if jieguo1 == "既不是素数也不是合数":#本作品作者吴宇航
                            jiegu1 = "既不是素数也不是合数"#本作品作者吴宇航
                        elif jieguo1 == "N":#本作品作者吴宇航
                            jieguo1 = "是质数"#本作品作者吴宇航
                        else:#本作品作者吴宇航
                            jieguo1 = "是合数，因数：" + str(jieguo1)#本作品作者吴宇航
                    messagebox.showwarning("",jieguo1)#本作品作者吴宇航
                except:#本作品作者吴宇航
                    messagebox.showwarning("","请不要乱输")#本作品作者吴宇航
        Button(izhihewin,text = "计算",command = izhihe2).pack(fill = BOTH,side = TOP,expand = True)#本作品作者吴宇航
        izhihewin.mainloop()#本作品作者吴宇航
    def izuixiao1():#本作品作者吴宇航
        izuixiaowin = Tk()#本作品作者吴宇航
        izuixiaowin.title("最小公倍数")#本作品作者吴宇航
        izuixiaowin.geometry("400x300")#本作品作者吴宇航
        Label(izuixiaowin,text = "在此输入第一个数").pack(side = TOP,expand = True)#本作品作者吴宇航
        var1 = Entry(izuixiaowin)#本作品作者吴宇航
        var1.pack(side = TOP,expand = True)#本作品作者吴宇航
        Label(izuixiaowin,text = "在此输入第二个数").pack(side = TOP,expand = True)#本作品作者吴宇航
        var2 = Entry(izuixiaowin)#本作品作者吴宇航
        var2.pack(side = TOP,expand = True)#本作品作者吴宇航
        def izuixiao2():#本作品作者吴宇航
            try:#本作品作者吴宇航
                jieguo1 = "最小公倍数是" + str(int(zuixiao(int(var1.get()),int(var2.get()))))#本作品作者吴宇航
                messagebox.showwarning("",jieguo1)#本作品作者吴宇航
            except:#本作品作者吴宇航
                messagebox.showwarning("","请不要乱输")#本作品作者吴宇航
        Button(izuixiaowin,text = "计算",command = izuixiao2).pack(fill = BOTH,side = BOTTOM,expand = True)#本作品作者吴宇航
        izuixiaowin.mainloop()#本作品作者吴宇航
    def izuida1():#本作品作者吴宇航
        izuidawin = Tk()#本作品作者吴宇航
        izuidawin.title("最大公因数")#本作品作者吴宇航
        izuidawin.geometry("400x300")#本作品作者吴宇航
        Label(izuidawin,text = "在此输入第一个数").pack(side = TOP,expand = True)#本作品作者吴宇航
        var1 = Entry(izuidawin)#本作品作者吴宇航
        var1.pack(side = TOP,expand = True)#本作品作者吴宇航
        Label(izuidawin,text = "在此输入第二个数").pack(side = TOP,expand = True)#本作品作者吴宇航
        var2 = Entry(izuidawin)#本作品作者吴宇航
        var2.pack(side = TOP,expand = True)#本作品作者吴宇航
        def izuida2():#本作品作者吴宇航
            try:#本作品作者吴宇航
                jieguo1 = "最大公因数是" + str(common_factor(int(var1.get()),int(var2.get())))#本作品作者吴宇航
                messagebox.showwarning("",jieguo1)#本作品作者吴宇航
            except:#本作品作者吴宇航
                messagebox.showwarning("","请不要乱输")#本作品作者吴宇航
        Button(izuidawin,text = "计算",command = izuida2).pack(fill = BOTH,side = BOTTOM,expand = True)#本作品作者吴宇航
        izuidawin.mainloop()#本作品作者吴宇航
    def fenshu1():#本作品作者吴宇航
        chooseuser = buttonbox(msg="你要使用哪种运算？",title="",choices=("加法","减法","乘法","除法"))#本作品作者吴宇航
        if chooseuser == "加法":#本作品作者吴宇航
            ijiafawin = Tk()#本作品作者吴宇航
            ijiafawin.title("分数加法")#本作品作者吴宇航
            ijiafawin.geometry("400x300")#本作品作者吴宇航
            Label(ijiafawin,text = "在此输入第一个分数的分子").pack(expand = True)#本作品作者吴宇航
            var1 = Entry(ijiafawin)#本作品作者吴宇航
            var1.pack(expand = True)#本作品作者吴宇航
            Label(ijiafawin,text = "在此输入第一个分数的分母").pack(expand = True)#本作品作者吴宇航
            var2 = Entry(ijiafawin)#本作品作者吴宇航
            var2.pack(expand = True)#本作品作者吴宇航
            Label(ijiafawin,text = "在此输入第二个分数的分子").pack(expand = True)#本作品作者吴宇航
            var3 = Entry(ijiafawin)#本作品作者吴宇航
            var3.pack(expand = True)#本作品作者吴宇航
            Label(ijiafawin,text = "在此输入第二个分数的分母").pack(expand = True)#本作品作者吴宇航
            var4 = Entry(ijiafawin)#本作品作者吴宇航
            var4.pack(expand = True)#本作品作者吴宇航
            def ijiafa():#本作品作者吴宇航
                try:#本作品作者吴宇航
                    jieguo1 = fenshuyunsuan("1",int(var2.get()),int(var4.get()),int(var1.get()),int(var3.get()))#本作品作者吴宇航
                    jieguo1 = "运算结果是" + str(jieguo1)#本作品作者吴宇航
                    messagebox.showwarning("",jieguo1)#本作品作者吴宇航
                except:#本作品作者吴宇航
                    messagebox.showwarning("","请不要乱输")#本作品作者吴宇航
            Button(ijiafawin,text = "计算",command = ijiafa).pack(fill = BOTH,side = BOTTOM,expand = True)#本作品作者吴宇航
            ijiafawin.mainloop()#本作品作者吴宇航
        elif chooseuser == "减法":#本作品作者吴宇航
            ijianfawin = Tk()#本作品作者吴宇航
            ijianfawin.title("分数减法")#本作品作者吴宇航
            ijianfawin.geometry("400x300")#本作品作者吴宇航
            Label(ijianfawin,text = "在此输入被减数的分子").pack(expand = True)#本作品作者吴宇航
            var1 = Entry(ijianfawin)#本作品作者吴宇航
            var1.pack(expand = True)#本作品作者吴宇航
            Label(ijianfawin,text = "在此输入被减数的分母").pack(expand = True)#本作品作者吴宇航
            var2 = Entry(ijianfawin)#本作品作者吴宇航
            var2.pack(expand = True)#本作品作者吴宇航
            Label(ijianfawin,text = "在此输入减数的分子").pack(expand = True)#本作品作者吴宇航
            var3 = Entry(ijianfawin)#本作品作者吴宇航
            var3.pack(expand = True)#本作品作者吴宇航
            Label(ijianfawin,text = "在此输入减数的分母").pack(expand = True)#本作品作者吴宇航
            var4 = Entry(ijianfawin)#本作品作者吴宇航
            var4.pack(expand = True)#本作品作者吴宇航
            def ijianfa():#本作品作者吴宇航
                jieguo1 = fenshuyunsuan("2",int(var2.get()),int(var4.get()),int(var1.get()),int(var3.get()))#本作品作者吴宇航
                jieguo1 = "运算结果是" + str(jieguo1)#本作品作者吴宇航
                messagebox.showwarning("",jieguo1)#本作品作者吴宇航
            Button(ijianfawin,text = "计算",command = ijianfa).pack(fill = BOTH,side = BOTTOM,expand = True)#本作品作者吴宇航
            ijianfawin.mainloop()#本作品作者吴宇航
        elif chooseuser == "乘法":#本作品作者吴宇航
            ichengfawin = Tk()#本作品作者吴宇航
            ichengfawin.title("分数乘法")#本作品作者吴宇航
            ichengfawin.geometry("400x300")#本作品作者吴宇航
            Label(ichengfawin,text = "在此输入第一个分数的分子").pack(expand = True)#本作品作者吴宇航
            var1 = Entry(ichengfawin)#本作品作者吴宇航
            var1.pack(expand = True)#本作品作者吴宇航
            Label(ichengfawin,text = "在此输入第一个分数的分母").pack(expand = True)#本作品作者吴宇航
            var2 = Entry(ichengfawin)#本作品作者吴宇航
            var2.pack(expand = True)#本作品作者吴宇航
            Label(ichengfawin,text = "在此输入第二个分数的分子").pack(expand = True)#本作品作者吴宇航
            var3 = Entry(ichengfawin)#本作品作者吴宇航
            var3.pack(expand = True)#本作品作者吴宇航
            Label(ichengfawin,text = "在此输入第二个分数的分母").pack(expand = True)#本作品作者吴宇航
            var4 = Entry(ichengfawin)#本作品作者吴宇航
            var4.pack(expand = True)#本作品作者吴宇航
            def ichengfa():#本作品作者吴宇航
                try:#本作品作者吴宇航
                    jieguo1 = fenshuyunsuan("3",int(var2.get()),int(var4.get()),int(var1.get()),int(var3.get()))#本作品作者吴宇航
                    jieguo1 = "运算结果是" + str(jieguo1)#本作品作者吴宇航
                    messagebox.showwarning("",jieguo1)#本作品作者吴宇航
                except:#本作品作者吴宇航
                    messagebox.showwarning("","请不要乱输")#本作品作者吴宇航
            Button(ichengfawin,text = "计算",command = ichengfa).pack(fill = BOTH,side = BOTTOM,expand = True)#本作品作者吴宇航
            ichengfawin.mainloop()#本作品作者吴宇航
        else:#本作品作者吴宇航
            ichufawin = Tk()#本作品作者吴宇航
            ichufawin.title("分数除法")#本作品作者吴宇航
            ichufawin.geometry("400x300")#本作品作者吴宇航
            Label(ichufawin,text = "在此输入被除数的分子").pack(expand = True)#本作品作者吴宇航
            var1 = Entry(ichufawin)#本作品作者吴宇航
            var1.pack(expand = True)#本作品作者吴宇航
            Label(ichufawin,text = "在此输入被除数的分母").pack(expand = True)#本作品作者吴宇航
            var2 = Entry(ichufawin)#本作品作者吴宇航
            var2.pack(expand = True)#本作品作者吴宇航
            Label(ichufawin,text = "在此输入除数的分子").pack(expand = True)#本作品作者吴宇航
            var3 = Entry(ichufawin)#本作品作者吴宇航
            var3.pack(expand = True)#本作品作者吴宇航
            Label(ichufawin,text = "在此输入除数的分母").pack(expand = True)#本作品作者吴宇航
            var4 = Entry(ichufawin)#本作品作者吴宇航
            var4.pack(expand = True)#本作品作者吴宇航
            def ichufa():#本作品作者吴宇航
                try:#本作品作者吴宇航
                    jieguo1 = fenshuyunsuan("4",int(var2.get()),int(var4.get()),int(var1.get()),int(var3.get()))#本作品作者吴宇航
                    jieguo1 = "运算结果是" + jieguo1#本作品作者吴宇航
                    messagebox.showwarning("",jieguo1)#本作品作者吴宇航
                except:#本作品作者吴宇航
                    messagebox.showwarning("","请不要乱输")#本作品作者吴宇航
            Button(ichufawin,text = "计算",command = ichufa).pack(fill = BOTH,side = BOTTOM,expand = True)#本作品作者吴宇航
            ichufawin.mainloop()#本作品作者吴宇航
    def ifenshu():#本作品作者吴宇航
        ifenshuwin = Tk()#本作品作者吴宇航
        ifenshuwin.title("分数比较大小")#本作品作者吴宇航
        ifenshuwin.geometry("400x300")#本作品作者吴宇航
        Label(ifenshuwin,text = "请输入第一个分数的分子").pack(expand = True)#本作品作者吴宇航
        var1 = Entry(ifenshuwin)#本作品作者吴宇航
        var1.pack()#本作品作者吴宇航
        Label(ifenshuwin,text = "请输入第一个分数的分母").pack(expand = True)#本作品作者吴宇航
        var2 = Entry(ifenshuwin)#本作品作者吴宇航
        var2.pack()#本作品作者吴宇航
        Label(ifenshuwin,text = "请输入第二个分数的分子").pack(expand = True)#本作品作者吴宇航
        var3 = Entry(ifenshuwin)#本作品作者吴宇航
        var3.pack()#本作品作者吴宇航
        Label(ifenshuwin,text = "请输入第二个分数的分母").pack(expand = True)#本作品作者吴宇航
        var4 = Entry(ifenshuwin)#本作品作者吴宇航
        var4.pack()#本作品作者吴宇航
        def bijiao():#本作品作者吴宇航
            try:#本作品作者吴宇航
                jieguo1 = fenshudaxiao(int(var2.get()),int(var4.get()),int(var1.get()),int(var3.get()))#本作品作者吴宇航
                if jieguo1 == 1:#本作品作者吴宇航
                    messagebox.showwarning("",var2.get() + "分之" + var1.get() + "大")#本作品作者吴宇航
                elif jieguo1 == 2:#本作品作者吴宇航
                    messagebox.showwarning("",var4.get() + "分之" + var3.get() + "大")#本作品作者吴宇航
                else:#本作品作者吴宇航
                    messagebox.showwarning("两个数一样大")#本作品作者吴宇航
            except:#本作品作者吴宇航
                messagebox.showwarning("请不要乱输")#本作品作者吴宇航
        Button(ifenshuwin,text = "计算",command = bijiao).pack(fill = BOTH,side = BOTTOM)#本作品作者吴宇航
        ifenshuwin.mainloop()#本作品作者吴宇航
    def ifeibonaqi():#本作品作者吴宇航
        chooseuser = buttonbox(msg = "你要用哪个功能",title = "",choices = ["求某一项","求某个数是第几项"])#本作品作者吴宇航
        if chooseuser == "求某一项":#本作品作者吴宇航
            feibowin1 = Tk()#本作品作者吴宇航
            feibowin1.geometry("400x300")#本作品作者吴宇航
            feibowin1.title("求斐波那契数列的某一项")#本作品作者吴宇航
            Label(feibowin1,text = "你想求第").pack(fill = BOTH,side = TOP,expand = True)#本作品作者吴宇航
            var1 = Entry(feibowin1)#本作品作者吴宇航
            var1.pack(fill = BOTH,side = TOP,expand = True)#本作品作者吴宇航
            Label(feibowin1,text = "项").pack(fill = BOTH,side = TOP,expand = True)#本作品作者吴宇航
            def ifeibo1():#本作品作者吴宇航
                try:#本作品作者吴宇航
                    messagebox.showwarning("","第" + var1.get() + "项是" + str(feibonaqi("1",int(var1.get()))))#本作品作者吴宇航
                except:#本作品作者吴宇航
                    messagebox.showwarning("","请不要乱输")#本作品作者吴宇航
            Button(feibowin1,text = "计算",command = ifeibo1).pack(fill = BOTH,side = BOTTOM)#本作品作者吴宇航
            feibowin1.mainloop()#本作品作者吴宇航
        else:#本作品作者吴宇航
            feibowin2 = Tk()#本作品作者吴宇航
            feibowin2.geometry("400x300")#本作品作者吴宇航
            feibowin2.title("求某个数在数列中的位置")#本作品作者吴宇航
            Label(feibowin2,text = "你想求").pack(side = TOP)#本作品作者吴宇航
            var1 = Entry(feibowin2)#本作品作者吴宇航
            var1.pack(side = TOP,expand = True)#本作品作者吴宇航
            Label(feibowin2,text = "在斐波那契数列中的位置").pack(side = TOP)#本作品作者吴宇航
            def ifeibo2():#本作品作者吴宇航
                try:#本作品作者吴宇航
                    jieguo1 = feibonaqi("2",int(var1.get()))#本作品作者吴宇航
                    if jieguo1 == "N":#本作品作者吴宇航
                        messagebox.showwarning("","这个数不在斐波那契数列中！")#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        messagebox.showwarning("",var1.get() + "是第" + str(jieguo1) + "项")#本作品作者吴宇航
                except:#本作品作者吴宇航
                    messagebox.showwarning("","请不要乱输")#本作品作者吴宇航
            Button(feibowin2,text = "计算",command = ifeibo2).pack(fill = BOTH,side = BOTTOM)#本作品作者吴宇航
            feibowin2.mainloop()#本作品作者吴宇航
    def dengcha():#本作品作者吴宇航
        chooseuser = buttonbox(msg = "你要哪个功能？",title = "",choices = ["求某一项","求某个数的位置","求和"])#本作品作者吴宇航
        if chooseuser == "求某一项":#本作品作者吴宇航
            dengchawin1 = Tk()#本作品作者吴宇航
            dengchawin1.title("求等差数列的某一项")#本作品作者吴宇航
            dengchawin1.geometry("400x300")#本作品作者吴宇航
            Label(dengchawin1,text = "在此输入首项").pack()#本作品作者吴宇航
            var1 = Entry(dengchawin1)#本作品作者吴宇航
            var1.pack()#本作品作者吴宇航
            Label(dengchawin1,text = "在此输入公差").pack()#本作品作者吴宇航
            var2 = Entry(dengchawin1)#本作品作者吴宇航
            var2.pack()#本作品作者吴宇航
            Label(dengchawin1,text = "你想求第几项？").pack()#本作品作者吴宇航
            var3 = Entry(dengchawin1)#本作品作者吴宇航
            var3.pack()#本作品作者吴宇航
            def idengcha1():#本作品作者吴宇航
                try:#本作品作者吴宇航
                    messagebox.showwarning("","第" + var3.get() + "项是" + str(dengchashulie(1,int(var1.get()),int(var2.get()),int(var3.get()))))#本作品作者吴宇航
                except:#本作品作者吴宇航
                    messagebox.showwarning("","请不要乱输")#本作品作者吴宇航
            Button(dengchawin1,text = "计算",command = idengcha1).pack(fill = BOTH,side = BOTTOM)#本作品作者吴宇航
            dengchawin1.mainloop()#本作品作者吴宇航
        elif chooseuser == "求某个数的位置":#本作品作者吴宇航
            dengchawin2 = Tk()#本作品作者吴宇航
            dengchawin2.title("求某个数在等差数列的位置")#本作品作者吴宇航
            dengchawin2.geometry("400x300")#本作品作者吴宇航
            Label(dengchawin2,text = "请输入首项").pack()#本作品作者吴宇航
            var1 = Entry(dengchawin2)#本作品作者吴宇航
            var1.pack()#本作品作者吴宇航
            Label(dengchawin2,text = "请输入公差").pack()#本作品作者吴宇航
            var2 = Entry(dengchawin2)#本作品作者吴宇航
            var2.pack()#本作品作者吴宇航
            Label(dengchawin2,text = "你想求哪个数的位置？").pack()#本作品作者吴宇航
            var3 = Entry(dengchawin2)#本作品作者吴宇航
            var3.pack()#本作品作者吴宇航
            def idengcha2():#本作品作者吴宇航
                try:#本作品作者吴宇航
                    jieguo1 = dengchashulie(2,int(var1.get()),int(var2.get()),int(var3.get()))#本作品作者吴宇航
                    if jieguo1 == "N":#本作品作者吴宇航
                        messagebox.showwarning("","这个数不在等差数列中！")#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        messagebox.showwarning("",var3.get() + "是第" + str(jieguo1) + "项")#本作品作者吴宇航
                except:#本作品作者吴宇航
                    messagebox.showwarning("","请不要乱输")#本作品作者吴宇航
            Button(dengchawin2,text = "计算",command = idengcha2).pack(fill = BOTH,side = BOTTOM)#本作品作者吴宇航
            dengchawin2.mainloop()#本作品作者吴宇航
        elif chooseuser == "求和":#本作品作者吴宇航
            dengchawin3 = Tk()#本作品作者吴宇航
            dengchawin3.title("等差数列求和")#本作品作者吴宇航
            dengchawin3.geometry("400x300")#本作品作者吴宇航
            Label(dengchawin3,text = "请输入首项").pack()#本作品作者吴宇航
            var1 = Entry(dengchawin3)#本作品作者吴宇航
            var1.pack()#本作品作者吴宇航
            Label(dengchawin3,text = "请输入公差").pack()#本作品作者吴宇航
            var2 = Entry(dengchawin3)#本作品作者吴宇航
            var2.pack()#本作品作者吴宇航
            Label(dengchawin3,text = "请输入项数").pack()#本作品作者吴宇航
            var3 = Entry(dengchawin3)#本作品作者吴宇航
            var3.pack()#本作品作者吴宇航
            def idengcha3():#本作品作者吴宇航
                try:#本作品作者吴宇航
                    jieguo1 = dengchashulie(3,int(var1.get()),int(var2.get()),int(var3.get()))#本作品作者吴宇航
                    messagebox.showwarning("","等差数列值和是" + str(jieguo1))#本作品作者吴宇航
                except:#本作品作者吴宇航
                    messagebox.showwarning("","请不要乱输")#本作品作者吴宇航
            Button(dengchawin3,text = "计算",command = idengcha3).pack(fill = BOTH,side = BOTTOM)        #本作品作者吴宇航
    afsd = {#本作品作者吴宇航
        "质数合数判断":izhihe1,#本作品作者吴宇航
        "最大公因数（整数）":izuida1,#本作品作者吴宇航
        "最小公倍数（整数）":izuixiao1,#本作品作者吴宇航
        "分数运算":fenshu1,#本作品作者吴宇航
        "分数比较大小":ifenshu,#本作品作者吴宇航
        "斐波那契数列计算":ifeibonaqi,#本作品作者吴宇航
        "等差数列":dengcha#本作品作者吴宇航
        }#本作品作者吴宇航
    def main():#本作品作者吴宇航
        window = Tk()#本作品作者吴宇航
        window.title("数学作业神器")#本作品作者吴宇航
        window.geometry("400x300")#本作品作者吴宇航
        for k in afsd:#本作品作者吴宇航
            Button(window,text = k,command = afsd[k]).pack(fill = BOTH,side = TOP,expand = True)#本作品作者吴宇航
        def fanhui():#本作品作者吴宇航
            if messagebox.askokcancel("确定退出？","您确定要退出？"):#本作品作者吴宇航
                window.destroy()#本作品作者吴宇航
        window.protocol("WM_DELETE_WINDOW",fanhui)#本作品作者吴宇航
        window.mainloop()#本作品作者吴宇航
    main()#本作品作者吴宇航
#本作品作者吴宇航
#二维码生成器#本作品作者吴宇航
from tkinter import *#本作品作者吴宇航
from tkinter import messagebox as m#本作品作者吴宇航
from tkinter import filedialog as dialog#本作品作者吴宇航
from tkinter import ttk#本作品作者吴宇航
from segno import *#本作品作者吴宇航
from segno import helpers#本作品作者吴宇航
def erma():#本作品作者吴宇航
    tk=Tk()#本作品作者吴宇航
    tk.geometry('+600+400')#本作品作者吴宇航
    tk.resizable(0,0)#本作品作者吴宇航
    tk.title('选择模式-Hello智能二维码生成器')#本作品作者吴宇航
    tk.attributes('-topmost',1)#本作品作者吴宇航
    v=StringVar()#本作品作者吴宇航
    v.set('普通')#本作品作者吴宇航
    def shotishi():#本作品作者吴宇航
        m.showinfo(parent=tk,title='重要提示',message='*注：wifi二维码需要使用手机自带扫\n码工具扫描才可连接到wifi，\n如果扫描后没有出现连接按钮，而是只有一串字符，\n这说明您的扫码工具不支持wifi二维码。\n名片二维码扫描后如果没有正常显示姓名等\n其他信息，而是只有一串字符，\n这说明扫码工具也不支持名片二维码！')#本作品作者吴宇航
    def about():#本作品作者吴宇航
        m.showinfo(title='关于我们',message='Hello智能二维码生成器（作者：陈明翰）\n                         0.7.6版')#本作品作者吴宇航
    def ok():#本作品作者吴宇航
        if v.get()=='普通':#本作品作者吴宇航
            def okpu():#本作品作者吴宇航
                if micro.get()==0:#本作品作者吴宇航
                    pu=make(thing.get(),micro=False)#本作品作者吴宇航
                else:#本作品作者吴宇航
                    try:#本作品作者吴宇航
                        pu=make(thing.get(),micro=True)#本作品作者吴宇航
                    except:#本作品作者吴宇航
                        m.showerror(parent=putk,title='错误',message='二维码数据过多，无法生成微型码')#本作品作者吴宇航
                        return#本作品作者吴宇航
                try:#本作品作者吴宇航
                    scale.get()#本作品作者吴宇航
                except:#本作品作者吴宇航
                    m.showerror(title='错误',message='“每个码源占多少像素”只能是整数！',parent=putk)#本作品作者吴宇航
                    return#本作品作者吴宇航
                if scale.get()==0:#本作品作者吴宇航
                    m.showerror(title='错误',message='“每个码源占多少像素”不能为0！！',parent=putk)#本作品作者吴宇航
                    return#本作品作者吴宇航
                def l():#本作品作者吴宇航
                    f=dialog.asksaveasfilename(title='请选择二维码图片保存地址',parent=erer,filetypes=[('PNG图片格式','.png')],defaultextension='.png')#本作品作者吴宇航
                    if f=='':#本作品作者吴宇航
                        return#本作品作者吴宇航
                    fileway.set(f)#本作品作者吴宇航
                def ok():#本作品作者吴宇航
                    if fileway.get()=='':#本作品作者吴宇航
                        m.showwarning(title='提示',message='您没有填写或选择保存路径',parent=erer)#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        try:#本作品作者吴宇航
                            pu.save(fileway.get(),scale=scale.get())#本作品作者吴宇航
                            putk.destroy()#本作品作者吴宇航
                        except:#本作品作者吴宇航
                            m.showerror(title='错误',message='数据格式或文件路径有误！',parent=erer)#本作品作者吴宇航
                erer=Toplevel(putk)#本作品作者吴宇航
                erer.title('保存文件-Hello智能二维码生成器')#本作品作者吴宇航
                erer.geometry('+400+400')#本作品作者吴宇航
                erer.resizable(0,0)#本作品作者吴宇航
                erer.attributes('-topmost',1)#本作品作者吴宇航
                fileway=StringVar()#本作品作者吴宇航
                Label(erer,text='请输入保存地址：').grid(column=0,row=0)#本作品作者吴宇航
                Entry(erer,textvariable=fileway,width=50).grid(column=1,row=0)#本作品作者吴宇航
                Button(erer,text='浏览',command=l,background="#54b8ed",activebackground="#54b8ed").grid(column=2,row=0)#本作品作者吴宇航
                Button(erer,text='保存',command=ok,width=10,height=2,background="#54b8ed",activebackground="#54b8ed").grid(column=0,row=1)#本作品作者吴宇航
                Button(erer,text='取消',command=erer.destroy,width=10,height=2,background="#54b8ed",activebackground="#54b8ed").grid(column=2,row=1)#本作品作者吴宇航
            def show_fun():#本作品作者吴宇航
                if micro.get()==0:#本作品作者吴宇航
                    pu=make(thing.get(),micro=False)#本作品作者吴宇航
                    m.showinfo(parent=putk,title='二维码信息',message=pu.designator)#本作品作者吴宇航
                else:#本作品作者吴宇航
                    try:#本作品作者吴宇航
                        pu=make(thing.get(),micro=True)#本作品作者吴宇航
                        m.showinfo(parent=putk,title='二维码信息',message=pu.designator)#本作品作者吴宇航
                    except:#本作品作者吴宇航
                        m.showerror(parent=putk,title='警告',message='二维码数据过多，无法生成微型码')#本作品作者吴宇航
            thing=StringVar()#本作品作者吴宇航
            micro=IntVar()#本作品作者吴宇航
            micro.set(0)#本作品作者吴宇航
            scale=IntVar()#本作品作者吴宇航
            putk=Toplevel(tk)#本作品作者吴宇航
            putk.resizable(0,0)#本作品作者吴宇航
            putk.title('创建普通二维码-Hello智能二维码生成器')#本作品作者吴宇航
            putk.geometry('+500+500')#本作品作者吴宇航
            putk.attributes('-topmost',1)#本作品作者吴宇航
            fthings=LabelFrame(putk,text='输入数据')#本作品作者吴宇航
            fthings.grid(column=0,row=0)#本作品作者吴宇航
            fsetting=LabelFrame(putk,text='二维码设置')#本作品作者吴宇航
            fsetting.grid(column=0,row=1)#本作品作者吴宇航
            fcaozuo=LabelFrame(putk,text='操作')#本作品作者吴宇航
            fcaozuo.grid(column=1,row=0,rowspan=2)#本作品作者吴宇航
            Label(fthings,text='请输入二维码包含的文字或网址：').grid(column=0,row=0)#本作品作者吴宇航
            Entry(fthings,textvariable=thing).grid(column=1,row=0)#本作品作者吴宇航
            Checkbutton(fsetting,text='生成微型码',variable=micro,onvalue=1,offvalue=0).grid(column=0,row=0,columnspan=2)#本作品作者吴宇航
            Label(fsetting,text='每个码源占多少像素：').grid(column=0,row=1)#本作品作者吴宇航
            Entry(fsetting,textvariable=scale).grid(column=1,row=1)#本作品作者吴宇航
            Button(fcaozuo,text='查看二维码数据',command=show_fun,width=20,height=2,background="#54b8ed",activebackground="#54b8ed").grid()#本作品作者吴宇航
            Button(fcaozuo,text='生成',command=okpu,width=10,height=2,background="#54b8ed",activebackground="#54b8ed").grid(pady=20)#本作品作者吴宇航
            Button(fcaozuo,text='取消',command=putk.destroy,width=10,height=2,background="#54b8ed",activebackground="#54b8ed").grid()#本作品作者吴宇航
        if v.get()=='名片':#本作品作者吴宇航
            def show_fun():#本作品作者吴宇航
                ming=helpers.make_mecard(name=name.get(),phone=phone.get(),email=email.get(),city=city.get(),country=country.get())#本作品作者吴宇航
                m.showinfo(title='二维码数据',message=ming.designator,parent=mingtk)#本作品作者吴宇航
            def okming():#本作品作者吴宇航
                try:#本作品作者吴宇航
                    scale.get()#本作品作者吴宇航
                except:#本作品作者吴宇航
                    m.showerror(title='错误',message='“每个码源占多少像素”只能是整数！',parent=mingtk)#本作品作者吴宇航
                    return#本作品作者吴宇航
                if scale.get()==0:#本作品作者吴宇航
                    m.showerror(title='错误',message='“每个码源占多少像素”不能为0！！',parent=mingtk)#本作品作者吴宇航
                else:#本作品作者吴宇航
                    def l():#本作品作者吴宇航
                        f=dialog.asksaveasfilename(title='请选择二维码图片保存地址',parent=erer,filetypes=[('PNG图片格式','.png')],defaultextension='.png')#本作品作者吴宇航
                        if f=='':#本作品作者吴宇航
                            return#本作品作者吴宇航
                        fileway.set(f)#本作品作者吴宇航
                    def ok():#本作品作者吴宇航
                        if fileway.get()=='':#本作品作者吴宇航
                            m.showwarning(title='提示',message='您没有填写或选择保存路径',parent=erer)#本作品作者吴宇航
                        else:#本作品作者吴宇航
                            try:#本作品作者吴宇航
                                ming.save(fileway.get(),scale=scale.get())#本作品作者吴宇航
                                mingtk.destroy()#本作品作者吴宇航
                            except:#本作品作者吴宇航
                                m.showerror(title='错误',message='数据格式或文件路径有误！',parent=erer)#本作品作者吴宇航
                    ming=helpers.make_mecard(name=name.get(),phone=phone.get(),email=email.get(),city=city.get(),country=country.get())#本作品作者吴宇航
                    erer=Toplevel(mingtk)#本作品作者吴宇航
                    erer.title('保存文件-Hello智能二维码生成器')#本作品作者吴宇航
                    erer.geometry('+400+400')#本作品作者吴宇航
                    erer.resizable(0,0)#本作品作者吴宇航
                    erer.attributes('-topmost',1)#本作品作者吴宇航
                    fileway=StringVar()#本作品作者吴宇航
                    Label(erer,text='请输入保存地址：').grid(column=0,row=0)#本作品作者吴宇航
                    Entry(erer,textvariable=fileway,width=50).grid(column=1,row=0)#本作品作者吴宇航
                    Button(erer,text='浏览',command=l,background="#54b8ed",activebackground="#54b8ed").grid(column=2,row=0)#本作品作者吴宇航
                    Button(erer,text='保存',command=ok,width=10,height=2,background="#54b8ed",activebackground="#54b8ed").grid(column=0,row=1)#本作品作者吴宇航
                    Button(erer,text='取消',command=erer.destroy,width=10,height=2,background="#54b8ed",activebackground="#54b8ed").grid(column=2,row=1)#本作品作者吴宇航
            mingtk=Toplevel(tk)#本作品作者吴宇航
            mingtk.resizable(0,0)#本作品作者吴宇航
            mingtk.attributes('-topmost',1)#本作品作者吴宇航
            mingtk.title('创建名片二维码-Hello智能二维码生成器')#本作品作者吴宇航
            mingtk.geometry('+500+500')#本作品作者吴宇航
            shujul=LabelFrame(mingtk,text='输入数据')#本作品作者吴宇航
            shujul.grid(column=0,row=0)#本作品作者吴宇航
            shezhil=LabelFrame(mingtk,text='二维码设置')#本作品作者吴宇航
            shezhil.grid(column=0,row=1)#本作品作者吴宇航
            caozuol=LabelFrame(mingtk,text='操作')#本作品作者吴宇航
            caozuol.grid(column=1,row=0,rowspan=2)#本作品作者吴宇航
            name=StringVar()#本作品作者吴宇航
            phone=StringVar()#本作品作者吴宇航
            email=StringVar()#本作品作者吴宇航
            city=StringVar()#本作品作者吴宇航
            country=StringVar()#本作品作者吴宇航
            scale=IntVar()#本作品作者吴宇航
            Label(shujul,text='姓名:').grid(column=0,row=0)#本作品作者吴宇航
            Entry(shujul,textvariable=name).grid(column=1,row=0)#本作品作者吴宇航
            Label(shujul,text='电话:').grid(column=0,row=1)#本作品作者吴宇航
            Entry(shujul,textvariable=phone).grid(column=1,row=1)#本作品作者吴宇航
            Label(shujul,text='电子邮箱:').grid(column=0,row=2)#本作品作者吴宇航
            Entry(shujul,textvariable=email).grid(column=1,row=2)#本作品作者吴宇航
            Label(shujul,text='所住城市:').grid(column=0,row=3)#本作品作者吴宇航
            Entry(shujul,textvariable=city).grid(column=1,row=3)#本作品作者吴宇航
            Label(shujul,text='国家:').grid(column=0,row=4)#本作品作者吴宇航
            Entry(shujul,textvariable=country).grid(column=1,row=4)#本作品作者吴宇航
            Label(shezhil,text='每个码源占多少像素：').grid(column=0,row=0)#本作品作者吴宇航
            Entry(shezhil,textvariable=scale).grid(column=1,row=0)#本作品作者吴宇航
            Button(caozuol,text='查看二维码数据',command=show_fun,width=20,height=2,background="#54b8ed",activebackground="#54b8ed").grid()#本作品作者吴宇航
            Button(caozuol,text='生成',command=okming,width=10,height=2,background="#54b8ed",activebackground="#54b8ed").grid(pady=20)#本作品作者吴宇航
            Button(caozuol,text='取消',command=mingtk.destroy,width=10,height=2,background="#54b8ed",activebackground="#54b8ed").grid()#本作品作者吴宇航
        elif v.get()=='wifi':#本作品作者吴宇航
            def okming():#本作品作者吴宇航
                if ssid.get()=='' or password.get()=='':#本作品作者吴宇航
                    m.showerror(title='错误',message='有必填数据没有填！',parent=ertk)#本作品作者吴宇航
                else:#本作品作者吴宇航
                    try:#本作品作者吴宇航
                        scale.get()#本作品作者吴宇航
                    except:#本作品作者吴宇航
                        m.showerror(title='错误',message='“每个码源占多少像素”只能是整数！',parent=ertk)#本作品作者吴宇航
                        return#本作品作者吴宇航
                    if scale.get()==0:#本作品作者吴宇航
                        m.showerror(title='错误',message='“每个码源占多少像素”不能为0！！',parent=ertk)#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        def l():#本作品作者吴宇航
                            f=dialog.asksaveasfilename(title='请选择二维码图片保存地址',parent=erer,filetypes=[('PNG图片格式','.png')],defaultextension='.png')#本作品作者吴宇航
                            if f=='':#本作品作者吴宇航
                                return#本作品作者吴宇航
                            fileway.set(f)#本作品作者吴宇航
                        def ok():#本作品作者吴宇航
                            if fileway.get()=='':#本作品作者吴宇航
                                m.showwarning(title='提示',message='您没有填写或选择保存路径',parent=erer)#本作品作者吴宇航
                            else:#本作品作者吴宇航
                                try:#本作品作者吴宇航
                                    er.save(fileway.get(),scale=scale.get())#本作品作者吴宇航
                                    ertk.destroy()#本作品作者吴宇航
                                except:#本作品作者吴宇航
                                    m.showerror(title='错误',message='数据格式或文件路径有误！',parent=erer)#本作品作者吴宇航
                        er=helpers.make_wifi(ssid=ssid.get(),password=password.get(),security=c.get())#本作品作者吴宇航
                        erer=Toplevel(ertk)#本作品作者吴宇航
                        erer.title('保存文件-Hello智能二维码生成器')#本作品作者吴宇航
                        erer.geometry('+400+400')#本作品作者吴宇航
                        erer.resizable(0,0)#本作品作者吴宇航
                        erer.attributes('-topmost',1)#本作品作者吴宇航
                        fileway=StringVar()#本作品作者吴宇航
                        Label(erer,text='请输入保存地址：').grid(column=0,row=0)#本作品作者吴宇航
                        Entry(erer,textvariable=fileway,width=50).grid(column=1,row=0)#本作品作者吴宇航
                        Button(erer,text='浏览',command=l,background="#54b8ed",activebackground="#54b8ed").grid(column=2,row=0)#本作品作者吴宇航
                        Button(erer,text='保存',command=ok,width=10,height=2,background="#54b8ed",activebackground="#54b8ed").grid(column=0,row=1)#本作品作者吴宇航
                        Button(erer,text='取消',command=erer.destroy,width=10,height=2,background="#54b8ed",activebackground="#54b8ed").grid(column=2,row=1)#本作品作者吴宇航
            def show_fun():#本作品作者吴宇航
                if ssid.get()=='' or password.get()=='':#本作品作者吴宇航
                    m.showerror(title='错误',message='有必填数据没有填！',parent=ertk)#本作品作者吴宇航
                else:#本作品作者吴宇航
                    er=helpers.make_wifi(ssid=ssid.get(),password=password.get(),security=c.get())#本作品作者吴宇航
                    m.showinfo(parent=ertk,title='二维码信息',message=er.designator)#本作品作者吴宇航
            ertk=Toplevel(tk)#本作品作者吴宇航
            ertk.resizable(0,0)#本作品作者吴宇航
            ertk.title('创建wifi二维码-Hello智能二维码生成器')#本作品作者吴宇航
            ertk.geometry('+500+500')#本作品作者吴宇航
            ertk.attributes('-topmost',1)#本作品作者吴宇航
            shujul=LabelFrame(ertk,text='输入数据')#本作品作者吴宇航
            shujul.grid(column=0,row=0)#本作品作者吴宇航
            shezhil=LabelFrame(ertk,text='二维码设置')#本作品作者吴宇航
            shezhil.grid(column=0,row=1)#本作品作者吴宇航
            caozuol=LabelFrame(ertk,text='操作')#本作品作者吴宇航
            caozuol.grid(column=1,row=0,rowspan=2)#本作品作者吴宇航
            ssid=StringVar()#本作品作者吴宇航
            password=StringVar()#本作品作者吴宇航
            scale=IntVar()#本作品作者吴宇航
            Label(shujul,text='wifi名称（必填）：').grid(column=0,row=0)#本作品作者吴宇航
            Entry(shujul,textvariable=ssid).grid(column=1,row=0)#本作品作者吴宇航
            Label(shujul,text='wifi密码（必填）：').grid(column=0,row=1)#本作品作者吴宇航
            Entry(shujul,textvariable=password,show='*').grid(column=1,row=1)#本作品作者吴宇航
            Label(shujul,text='wifi安全性（必填）：').grid(column=0,row=2)#本作品作者吴宇航
            c=ttk.Combobox(shujul)#本作品作者吴宇航
            c.grid(column=1,row=2)#本作品作者吴宇航
            c['value']=('WEP','WPA')#本作品作者吴宇航
            c['state']='readonly'#本作品作者吴宇航
            c.set('WPA')#本作品作者吴宇航
            Label(shezhil,text='每个码源占多少像素：').grid(column=0,row=0)#本作品作者吴宇航
            Entry(shezhil,textvariable=scale).grid(column=1,row=0)#本作品作者吴宇航
            Button(caozuol,text='查看二维码数据',command=show_fun,width=20,height=2,background="#54b8ed",activebackground="#54b8ed").grid()#本作品作者吴宇航
            Button(caozuol,text='生成',command=okming,width=10,height=2,background="#54b8ed",activebackground="#54b8ed").grid(pady=20)#本作品作者吴宇航
            Button(caozuol,text='取消',command=ertk.destroy,width=10,height=2,background="#54b8ed",activebackground="#54b8ed").grid()#本作品作者吴宇航
    F=LabelFrame(tk,text='请选择一个模式')#本作品作者吴宇航
    F.grid(column=0,row=0,columnspan=3)#本作品作者吴宇航
    Radiobutton(F,text='生成普通二维码',variable=v,value='普通').grid()#本作品作者吴宇航
    Radiobutton(F,text='生成名片二维码',variable=v,value='名片').grid()#本作品作者吴宇航
    Radiobutton(F,text='生成wifi二维码',variable=v,value='wifi').grid()#本作品作者吴宇航
    Button(tk,text='创建',command=ok,width=10,height=2,background="#54b8ed",activebackground="#54b8ed").grid(column=1,row=1,pady=20)#本作品作者吴宇航
    Button(tk,text='使用前\n必读！',command=shotishi,width=10,height=2,background="#54b8ed",activebackground="#54b8ed").grid(column=0,row=2)#本作品作者吴宇航
    Button(tk,text='关闭',command=tk.destroy,width=10,height=2,background="#54b8ed",activebackground="#54b8ed").grid(column=1,row=2,padx=30)#本作品作者吴宇航
    Button(tk,text='关于',command=about,width=10,height=2,background="#54b8ed",activebackground="#54b8ed").grid(column=2,row=2,pady=30)#本作品作者吴宇航
    tk.mainloop()#本作品作者吴宇航
#本作品作者吴宇航
#天气预报#本作品作者吴宇航
from tkinter import *#本作品作者吴宇航
import urllib.request#本作品作者吴宇航
import gzip#本作品作者吴宇航
import json#本作品作者吴宇航
from tkinter import messagebox#本作品作者吴宇航
def temp():#本作品作者吴宇航
    root = Tk()#本作品作者吴宇航
 #本作品作者吴宇航
 #本作品作者吴宇航
    def main():#本作品作者吴宇航
        root.title('实时天气查询器')  #本作品作者吴宇航
        Label(root, text='请输入城市').grid(row=0, column=0) #本作品作者吴宇航
        enter = Entry(root)  #本作品作者吴宇航
        enter.grid(row=0, column=1, padx=20, pady=20)  #本作品作者吴宇航
        enter.delete(0, END)  #本作品作者吴宇航
        enter.insert(0, '输入吧')  #本作品作者吴宇航
        enter_text = enter.get()#本作品作者吴宇航
     #本作品作者吴宇航
        running = 1#本作品作者吴宇航
     #本作品作者吴宇航
        def get_weather_data():  #本作品作者吴宇航
            city_name = enter.get()  #本作品作者吴宇航
            url1 = 'http://wthrcdn.etouch.cn/weather_mini?city=' + urllib.parse.quote(city_name)#本作品作者吴宇航
            url2 = 'http://wthrcdn.etouch.cn/weather_mini?citykey=101010100'#本作品作者吴宇航
            weather_data = urllib.request.urlopen(url1).read()#本作品作者吴宇航
            weather_data = gzip.decompress(weather_data).decode('utf-8')#本作品作者吴宇航
            weather_dict = json.loads(weather_data)#本作品作者吴宇航
            if weather_dict.get('desc') == 'invilad-citykey':#本作品作者吴宇航
                print(messagebox.askokcancel("错误", "您输入的城市名有误，或者天气中心未收录你所在城市"))#本作品作者吴宇航
            else:#本作品作者吴宇航
                show_data(weather_dict, city_name)#本作品作者吴宇航
     #本作品作者吴宇航
        def show_data(weather_dict, city_name): #本作品作者吴宇航
            forecast = weather_dict.get('data').get('forecast')  #本作品作者吴宇航
            root1 = Tk()#本作品作者吴宇航
            root1.geometry('1000x300')  #本作品作者吴宇航
            root1.title(city_name + '天气状况')  #本作品作者吴宇航
     #本作品作者吴宇航
            for i in range(5):  #本作品作者吴宇航
                LANGS = [(forecast[i].get('date'), '日期'),#本作品作者吴宇航
                         (forecast[i].get('fengxiang'), '风向'),#本作品作者吴宇航
                         (str(forecast[i].get('fengji')), '风级'),#本作品作者吴宇航
                         (forecast[i].get('high'), '最高温'),#本作品作者吴宇航
                         (forecast[i].get('low'), '最低温'),#本作品作者吴宇航
                         (forecast[i].get('type'), '天气')]#本作品作者吴宇航
                group = LabelFrame(root1, text='天气状况', padx=0, pady=0) #本作品作者吴宇航
                group.pack(padx=11, pady=0, side=LEFT)  #本作品作者吴宇航
                for lang, value in LANGS:  #本作品作者吴宇航
                    c = Label(group, text=value + ': ' + lang)#本作品作者吴宇航
                    c.pack(anchor=W)#本作品作者吴宇航
            Label(root1, text='今日温馨提示:' + weather_dict.get('data').get('ganmao'),#本作品作者吴宇航
                  fg='red').place(x=40, y=20, height=40)  #本作品作者吴宇航
            Button(root1, text='确认并退出', width=10, command=root1.destroy).place(x=500, y=230, width=80, height=40)  #本作品作者吴宇航
            root1.mainloop()#本作品作者吴宇航
        Button(root, text="确认", width=10, command=get_weather_data) \
            .grid(row=3, column=0, sticky=W, padx=10, pady=5)#本作品作者吴宇航
        Button(root, text='退出', width=10, command=root.destroy) \
            .grid(row=3, column=1, sticky=E, padx=10, pady=5)#本作品作者吴宇航
        if running == 1:#本作品作者吴宇航
            root.mainloop()#本作品作者吴宇航
     #本作品作者吴宇航
    if __name__ == '__main__':#本作品作者吴宇航
        main()#本作品作者吴宇航
#本作品作者吴宇航
#翻译器#本作品作者吴宇航
import requests#本作品作者吴宇航
from requests.exceptions import RequestException#本作品作者吴宇航
import tkinter as tk#本作品作者吴宇航
def translate():#本作品作者吴宇航
    class Translate():#本作品作者吴宇航
        def __init__(self):#本作品作者吴宇航
            self.window = tk.Tk()  #创建window窗口#本作品作者吴宇航
            self.window.title("简易翻译器")  # 定义窗口名称#本作品作者吴宇航
            self.window.resizable(0,0)  # 禁止调整窗口大小#本作品作者吴宇航
            self.input = tk.Entry(self.window, width=80)  # 创建一个输入框,并设置尺寸#本作品作者吴宇航
            self.info = tk.Text(self.window, height=18)   # 创建一个文本展示框，并设置尺寸#本作品作者吴宇航
            # 添加一个按钮，用于触发翻译功能#本作品作者吴宇航
            self.t_button = tk.Button(self.window, text='翻译', relief=tk.RAISED, width=8, height=1, command=self.fanyi)#本作品作者吴宇航
            # 添加一个按钮，用于触发清空输入框功能#本作品作者吴宇航
            self.c_button1 = tk.Button(self.window, text='清空输入', relief=tk.RAISED, width=8, height=1, command=self.cle_e)#本作品作者吴宇航
            # 添加一个按钮，用于触发清空输出框功能#本作品作者吴宇航
            self.c_button2 = tk.Button(self.window, text='清空输出', relief=tk.RAISED,width=8, height=1, command=self.cle)#本作品作者吴宇航
            #本作品作者吴宇航
    #本作品作者吴宇航
        def gui_arrang(self):#本作品作者吴宇航
            """完成页面元素布局，设置各部件的位置"""#本作品作者吴宇航
            self.input.grid(row=0,sticky="W",padx=1)#本作品作者吴宇航
            self.info.grid(row=1)#本作品作者吴宇航
            self.t_button.grid(row=0,column=1,padx=2)#本作品作者吴宇航
            self.c_button1.grid(row=0, column=2, padx=2)#本作品作者吴宇航
            self.c_button2.grid(row=0,column=3,padx=2)#本作品作者吴宇航
    #本作品作者吴宇航
        def fanyi(self):#本作品作者吴宇航
            """定义一个函数，完成翻译功能"""#本作品作者吴宇航
            original_str = self.input.get()  # 定义一个变量，用来接收输入框输入的值#本作品作者吴宇航
            data = {#本作品作者吴宇航
                'doctype': 'json',#本作品作者吴宇航
                'type': 'AUTO',#本作品作者吴宇航
                'i': original_str  # 将输入框输入的值，赋给接口参数#本作品作者吴宇航
            }#本作品作者吴宇航
            url = "http://fanyi.youdao.com/translate"#本作品作者吴宇航
            try:#本作品作者吴宇航
                r = requests.get(url, params=data)#本作品作者吴宇航
                if r.status_code == 200:#本作品作者吴宇航
                    result = r.json()#本作品作者吴宇航
                    translate_result = result['translateResult'][0][0]["tgt"]#本作品作者吴宇航
                    self.info.delete(1.0, "end")  # 输出翻译内容前，先清空输出框的内容#本作品作者吴宇航
                    self.info.insert('end',translate_result)  # 将翻译结果添加到输出框中#本作品作者吴宇航
            except RequestException:#本作品作者吴宇航
                self.info.insert('end', "发生错误")#本作品作者吴宇航
        def cle(self):#本作品作者吴宇航
            """定义一个函数，用于清空输出框的内容"""#本作品作者吴宇航
            self.info.delete(1.0,"end")  # 从第一行清除到最后一行#本作品作者吴宇航
    #本作品作者吴宇航
        def cle_e(self):#本作品作者吴宇航
            """定义一个函数，用于清空输入框的内容"""#本作品作者吴宇航
            self.input.delete(0,"end")#本作品作者吴宇航
    #本作品作者吴宇航
    def main():#本作品作者吴宇航
        t = Translate()#本作品作者吴宇航
        t.gui_arrang()#本作品作者吴宇航
        tk.mainloop()#本作品作者吴宇航
    #本作品作者吴宇航
    if __name__ == '__main__':#本作品作者吴宇航
        main()#本作品作者吴宇航
#本作品作者吴宇航
#短信发送器#本作品作者吴宇航
from tkinter import*;from tkinter import messagebox;from tkinter.ttk import*#本作品作者吴宇航
from xes.sms import*#本作品作者吴宇航
def smstool():#本作品作者吴宇航
    def sk():#本作品作者吴宇航
        z=Enter.get(),Enter1.get()#本作品作者吴宇航
        window.destroy()#本作品作者吴宇航
        send_msg(z[0],z[1])#本作品作者吴宇航
        #本作品作者吴宇航
    def callback():#本作品作者吴宇航
        res=messagebox.askokcancel("","您确定要退出吗？")#本作品作者吴宇航
#本作品作者吴宇航
        if res==True:#本作品作者吴宇航
            window.destroy()#本作品作者吴宇航
        else:#本作品作者吴宇航
            return#本作品作者吴宇航
#本作品作者吴宇航
    window = Tk()#本作品作者吴宇航
    window.title('短信发送器')#本作品作者吴宇航
    window.geometry("655x80")#本作品作者吴宇航
    Enter=Entry(window)#本作品作者吴宇航
    Enter1=Entry(window)#本作品作者吴宇航
    lw=Label(window,text="输入手机号：")#本作品作者吴宇航
    lw1=Label(window,text="输入信息：")#本作品作者吴宇航
    dtn=Button(window,text="点击发送",command=sk)#本作品作者吴宇航
    dtn.pack(side=TOP,fill=BOTH,expand=True)#本作品作者吴宇航
    Enter.pack(side=RIGHT,fill=X,expand=True)#本作品作者吴宇航
    lw.pack(side=RIGHT,fill=BOTH,expand=True)#本作品作者吴宇航
    Enter1.pack(side=RIGHT,fill=X,expand=True)#本作品作者吴宇航
    lw1.pack(side=RIGHT,fill=BOTH,expand=True)#本作品作者吴宇航
    dtn.pack(side=TOP,fill=BOTH,expand=True)#本作品作者吴宇航
    window.protocol("WM_DELETE_WINDOW",callback)#本作品作者吴宇航
#本作品作者吴宇航
    window.mainloop()#本作品作者吴宇航
#本作品作者吴宇航
#新闻查看器#本作品作者吴宇航
import requests, bs4, time, tkinter#本作品作者吴宇航
newsIndex = 0#本作品作者吴宇航
response = requests.get("https://www.36kr.com/information/technology")#本作品作者吴宇航
response.encoding = "UTF-8"#本作品作者吴宇航
soup = bs4.BeautifulSoup(response.text,"lxml")#本作品作者吴宇航
data = soup.find_all(name = "div", class_ = "article-item-info clearfloat")#本作品作者吴宇航
def xinwen():#本作品作者吴宇航
    print(len(data))#本作品作者吴宇航
    def refreshNews():#本作品作者吴宇航
        global data,newsIndex#本作品作者吴宇航
        if newsIndex < len(data):#本作品作者吴宇航
            text = data[newsIndex].find_all(name = "a")#本作品作者吴宇航
            listb.insert(0,"-"*30)#本作品作者吴宇航
            listb.insert(0,"作  者:" + text[2].text)#本作品作者吴宇航
            listb.insert(0,"摘  要:" + text[1].text)#本作品作者吴宇航
            listb.insert(0,"标  题:" + text[0].text)#本作品作者吴宇航
            newsIndex += 1#本作品作者吴宇航
#本作品作者吴宇航
    root = tkinter.Tk(className = "python")#本作品作者吴宇航
    root.geometry("800x600")#本作品作者吴宇航
    root.configure(background = "gray")#本作品作者吴宇航
#本作品作者吴宇航
    listb = tkinter.Listbox(root, width = 90, height = 30, bg = "black", fg = "red")#本作品作者吴宇航
    listb.pack()#本作品作者吴宇航
#本作品作者吴宇航
    button1 = tkinter.Button(root, text = "显示新闻", command = refreshNews )#本作品作者吴宇航
    button1.pack()#本作品作者吴宇航
#本作品作者吴宇航
    root.mainloop()#本作品作者吴宇航
#本作品作者吴宇航
#音乐播放器#本作品作者吴宇航
import tkinter#本作品作者吴宇航
from tkinter import Button#本作品作者吴宇航
from tkinter import Label#本作品作者吴宇航
from tkinter import Entry#本作品作者吴宇航
from tkinter import Scale#本作品作者吴宇航
from tkinter import Label,PhotoImage#本作品作者吴宇航
from PIL import Image,ImageTk#本作品作者吴宇航
from tkinter import messagebox#本作品作者吴宇航
from tkinter import Toplevel#本作品作者吴宇航
from pymediainfo import MediaInfo#本作品作者吴宇航
import re#本作品作者吴宇航
from tkinter import Message#本作品作者吴宇航
import threading#本作品作者吴宇航
import pygame#本作品作者吴宇航
import time#本作品作者吴宇航
import os#本作品作者吴宇航
import random#本作品作者吴宇航
from tkinter.filedialog   import askopenfilename#本作品作者吴宇航
from tkinter.filedialog import askdirectory#本作品作者吴宇航
from tkinter import StringVar#本作品作者吴宇航
num = 0#本作品作者吴宇航
fy = 2#本作品作者吴宇航
w3 = " "#本作品作者吴宇航
headers = {#本作品作者吴宇航
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'#本作品作者吴宇航
}#本作品作者吴宇航
headers1 = {#本作品作者吴宇航
    'Accept': 'application/json, text/plain, */*',#本作品作者吴宇航
    'Accept-Encoding': 'gzip, deflate',#本作品作者吴宇航
    'Accept-Language': 'zh-CN,zh;q=0.9',#本作品作者吴宇航
    'Connection': 'keep-alive',#本作品作者吴宇航
    'Cookie': '_ga=GA1.2.1500987479.1595755923; _gid=GA1.2.568444838.1596065504; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1595755923,1596065505; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1596076178; kw_token=P5XA2TZXG9',#本作品作者吴宇航
    'csrf': 'P5XA2TZXG9',#本作品作者吴宇航
    'Host': 'www.kuwo.cn',#本作品作者吴宇航
    'Referer': 'http://www.kuwo.cn/search/list?key=%E5%A4%95%E9%98%B3%E7%BA%A2',#本作品作者吴宇航
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'#本作品作者吴宇航
}#本作品作者吴宇航
headers2 = {#本作品作者吴宇航
    'Accept': 'application/json, text/plain, */*',#本作品作者吴宇航
    'Accept-Encoding': 'gzip, deflate',#本作品作者吴宇航
    'Accept-Language': 'zh-CN,zh;q=0.9',#本作品作者吴宇航
    'Connection': 'keep-alive',#本作品作者吴宇航
    'Cookie': '_ga=GA1.2.1500987479.1595755923; _gid=GA1.2.568444838.1596065504; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1595755923,1596065505; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1596078189; _gat=1; kw_token=IJATWHHGI8',#本作品作者吴宇航
    'csrf': 'IJATWHHGI8',#本作品作者吴宇航
    'Host': 'www.kuwo.cn',#本作品作者吴宇航
    'Referer': 'http://www.kuwo.cn/search/list?key=%E6%A2%A6%E7%9A%84%E5%9C%B0%E6%96%B9',#本作品作者吴宇航
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',#本作品作者吴宇航
#本作品作者吴宇航
}#本作品作者吴宇航
def musics():#本作品作者吴宇航
    top=tkinter.Tk()#本作品作者吴宇航
    top.geometry("800x400")#本作品作者吴宇航
    top.title("我的音乐播放器")#本作品作者吴宇航
    def printsrceen(texts):#本作品作者吴宇航
        t=int(texts)#本作品作者吴宇航
        top.attributes("-alpha",t/100)#本作品作者吴宇航
     #本作品作者吴宇航
    screenwidth = top.winfo_screenwidth()#本作品作者吴宇航
    screenheight = top.winfo_screenheight() - 100#本作品作者吴宇航
#本作品作者吴宇航
    pygame.init()#本作品作者吴宇航
    path=StringVar()#本作品作者吴宇航
    paths=StringVar()#本作品作者吴宇航
    patht=StringVar()#本作品作者吴宇航
    v=StringVar()#本作品作者吴宇航
    v1=StringVar()#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
    def callback():#搜索本地文件#本作品作者吴宇航
        path_= askopenfilename() #本作品作者吴宇航
        return path_#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
    def selectPath():#随机播放#本作品作者吴宇航
        folder_path="D:/音乐"#本作品作者吴宇航
        folder_list = os.listdir(folder_path)#遍历文件夹里面每个文件#本作品作者吴宇航
        list=[]#本作品作者吴宇航
        count=0#本作品作者吴宇航
        for i in folder_list:#将文件夹里的文件按顺序传提给变量i  此处区别os.walk()#本作品作者吴宇航
            if os.path.splitext(i)[1]=='.flac':#提取特定后缀文件'.***'#本作品作者吴宇航
                list.append (i)#本作品作者吴宇航
            #print(type(list))#本作品作者吴宇航
                count=count+1#本作品作者吴宇航
        #print(count)#本作品作者吴宇航
               #本作品作者吴宇航
        s=random.randint(0,(count-1))#获取随机数#本作品作者吴宇航
        file=list[s]#本作品作者吴宇航
        fil=folder_path+"\\"+file#本作品作者吴宇航
     #本作品作者吴宇航
       #本作品作者吴宇航
        pygame.mixer.music.load(fil)#本作品作者吴宇航
        pygame.mixer.music.play(1,0)#本作品作者吴宇航
        media_info = MediaInfo.parse(fil)#本作品作者吴宇航
        data = media_info.to_json()#medio到json()这两行是获取文件的所有属性#本作品作者吴宇航
        rst=re.search('other_duration.*?(.*?)min(.*?)s.*?',data)#本作品作者吴宇航
        t=int(rst.group(0)[19:20])#本作品作者吴宇航
        r=int(rst.group(0)[-4:-2])#本作品作者吴宇航
        m=(t*60+r)*1000#本作品作者吴宇航
        #本作品作者吴宇航
        musictime=str(t)+':'+str(r)#本作品作者吴宇航
        l2.config(text=file)#本作品作者吴宇航
        l3.config(text=musictime)#本作品作者吴宇航
        lbTime=tkinter.Label(top,anchor='w')#本作品作者吴宇航
        lbTime.place(x=25,y=150)#本作品作者吴宇航
        def autoclose():#本作品作者吴宇航
            for i in range(m//1000):#本作品作者吴宇航
                lbTime['text']='-{} /'.format((m//1000)-i)#本作品作者吴宇航
                time.sleep(1)#本作品作者吴宇航
        t=threading.Thread(target=autoclose)#本作品作者吴宇航
        t.start()#本作品作者吴宇航
        loopl=top.after(m,selectPath)#本作品作者吴宇航
       #本作品作者吴宇航
       #本作品作者吴宇航
#本作品作者吴宇航
    def printScale(text):#本作品作者吴宇航
        t=int(text)#本作品作者吴宇航
        pygame.mixer.music.set_volume(t/100)#本作品作者吴宇航
        #本作品作者吴宇航
    def update_timeText():#本作品作者吴宇航
        # Get the current time, note you can change the format as you wish#本作品作者吴宇航
        current = time.strftime("%H:%M:%S")#获取当前时间#本作品作者吴宇航
#本作品作者吴宇航
    # Update the timeText Label box with the current time#本作品作者吴宇航
        timeText.configure(text=current)#本作品作者吴宇航
#本作品作者吴宇航
    # Call the update_timeText() function after 1 second#本作品作者吴宇航
        top.after(1000, update_timeText)#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        #本作品作者吴宇航
    def remind():#本作品作者吴宇航
        top = Toplevel()#新建一个tkinter窗口#本作品作者吴宇航
        top.title('使用提示')#本作品作者吴宇航
        top.geometry("200x200")#本作品作者吴宇航
        t="半分钟后开始播放音乐"#本作品作者吴宇航
        msg = Message(top,text = t)#本作品作者吴宇航
        msg.config( font=('times', 18, 'italic'))#本作品作者吴宇航
        msg.place(x=0,y=0)#本作品作者吴宇航
        lbTime=tkinter.Label(top,fg="red",anchor='w')#本作品作者吴宇航
        lbTime.place(x=100,y=45)#本作品作者吴宇航
        def autoclose():#本作品作者吴宇航
            for i in range(30):#本作品作者吴宇航
                lbTime['text']='距离窗口关闭还有{}秒'.format(30-i)#本作品作者吴宇航
                time.sleep(1)#本作品作者吴宇航
            top.destroy()#本作品作者吴宇航
        t=threading.Thread(target=autoclose)#本作品作者吴宇航
        t.start()#本作品作者吴宇航
        loopl=top.after(60*59500,remind)#本作品作者吴宇航
#本作品作者吴宇航
        #本作品作者吴宇航
        #本作品作者吴宇航
    def reminds():#本作品作者吴宇航
        top = Toplevel()#本作品作者吴宇航
        top.title('使用提示')#本作品作者吴宇航
        top.geometry("200x200")#本作品作者吴宇航
        t="宝贝可以休息一会啦"#本作品作者吴宇航
        msg = Message(top,text = t)#本作品作者吴宇航
        msg.config( font=('times', 24, 'italic'))#本作品作者吴宇航
        msg.place(x=0,y=0)#本作品作者吴宇航
        folder_path="D:/音乐"#本作品作者吴宇航
        folder_list = os.listdir(folder_path)#遍历文件夹里面每个文件#本作品作者吴宇航
        list=[]#本作品作者吴宇航
        count=0#本作品作者吴宇航
        for i in folder_list:#将文件夹里的文件按顺序传提给变量i  此处区别os.walk()#本作品作者吴宇航
            if os.path.splitext(i)[1]=='.flac':#提取特定后缀文件'.***'#本作品作者吴宇航
                list.append (i)#本作品作者吴宇航
            #print(type(list))#本作品作者吴宇航
                count=count+1#本作品作者吴宇航
            #print(count)#本作品作者吴宇航
        s=random.randint(0,(count-1))#本作品作者吴宇航
        file=list[s]#本作品作者吴宇航
        fil=folder_path+"\\"+file#本作品作者吴宇航
        pygame.mixer.music.load(fil)#本作品作者吴宇航
        pygame.mixer.music.play(1,0)#本作品作者吴宇航
        lbTime=tkinter.Label(top,fg="red",anchor='w')#本作品作者吴宇航
        lbTime.place(x=100,y=45)#本作品作者吴宇航
        def autoclose():#本作品作者吴宇航
            for i in range(300):#本作品作者吴宇航
                lbTime['text']='距离窗口关闭还有{}秒'.format(300-i)#本作品作者吴宇航
                time.sleep(1)#本作品作者吴宇航
            top.destroy()#本作品作者吴宇航
        t=threading.Thread(target=autoclose)#本作品作者吴宇航
        t.start()#本作品作者吴宇航
        loopl=top.after(60*60000,reminds)#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        #本作品作者吴宇航
#本作品作者吴宇航
    def play():#播放音乐#本作品作者吴宇航
        f=callback()#选择制定文件#本作品作者吴宇航
        pygame.mixer.music.load(f)#本作品作者吴宇航
        pygame.mixer.music.play()#本作品作者吴宇航
        path.set(f)#本作品作者吴宇航
        media_info = MediaInfo.parse(f)#本作品作者吴宇航
        data = media_info.to_json()#medio到json()这两行是获取文件的所有属性#本作品作者吴宇航
        rst=re.search('other_duration.*?(.*?)min(.*?)s.*?',data)#本作品作者吴宇航
        t=int(rst.group(0)[19:20])#本作品作者吴宇航
        r=int(rst.group(0)[-4:-2])#本作品作者吴宇航
        m=(t*60+r)*1000#本作品作者吴宇航
        musictime=str(t)+':'+str(r)#本作品作者吴宇航
        l2.config(text=f)#本作品作者吴宇航
        l3.config(text=musictime)#本作品作者吴宇航
        lbTime=tkinter.Label(top,anchor='w')#本作品作者吴宇航
        lbTime.place(x=25,y=150)#本作品作者吴宇航
        def autoclose():#本作品作者吴宇航
            for i in range(m//1000):#本作品作者吴宇航
                lbTime['text']='-{} /'.format((m//1000)-i)#本作品作者吴宇航
                time.sleep(1)#本作品作者吴宇航
        t=threading.Thread(target=autoclose)#本作品作者吴宇航
        t.start()#本作品作者吴宇航
        loopl=top.after(m,selectPath)#本作品作者吴宇航
        #本作品作者吴宇航
       #本作品作者吴宇航
    def stop():#本作品作者吴宇航
        pygame.mixer.music.stop()#停止播放#本作品作者吴宇航
        top.after_cancel(loopl)#本作品作者吴宇航
        #本作品作者吴宇航
#本作品作者吴宇航
    def pause():#本作品作者吴宇航
        pygame.mixer.music.pause()#暂停   #本作品作者吴宇航
    def unpause():#本作品作者吴宇航
        pygame.mixer.music.unpause()#继续播放   #本作品作者吴宇航
    def choosepic():#保存的路径不能有中文，若需要中文则吧/换成\#本作品作者吴宇航
        path_s=askopenfilename()#本作品作者吴宇航
        paths.set(path_s)#本作品作者吴宇航
        img_open=Image.open(e1.get())#本作品作者吴宇航
        img=ImageTk.PhotoImage(img_open)#本作品作者吴宇航
        l1.config(image=img)#本作品作者吴宇航
        l1.image=img#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        #本作品作者吴宇航
    def create():#本作品作者吴宇航
        top = Toplevel()#本作品作者吴宇航
        top.title('使用提示')#本作品作者吴宇航
        top.geometry("400x400")#本作品作者吴宇航
        t="关于照片，新建一个存放图片的文件，用英文命名，然后存里面的图片也用英文命名。关于音乐: 新建一个名字叫音乐的文件，把歌曲添加到该文件夹。"#本作品作者吴宇航
        msg = Message(top,text = t)#本作品作者吴宇航
        msg.config( font=('times', 24, 'italic'))#本作品作者吴宇航
        msg.place(x=0,y=0)#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
    def loop():#本作品作者吴宇航
        top.after(60*60000,reminds)#本作品作者吴宇航
        top.after(60*59500,remind)#本作品作者吴宇航
#本作品作者吴宇航
        #本作品作者吴宇航
    def loops():#本作品作者吴宇航
        selectPath()#本作品作者吴宇航
    def gettime():#本作品作者吴宇航
        t=time.strftime('%H%M%S')#本作品作者吴宇航
        s=int(t[0:2])#本作品作者吴宇航
        d=int(t[2:4])#本作品作者吴宇航
        f=int(t[4:6])#本作品作者吴宇航
        g=s*60*60+d*60+f#本作品作者吴宇航
        return g    #本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        #本作品作者吴宇航
    errmsg = 'Error!'#本作品作者吴宇航
    #时间#本作品作者吴宇航
    timeText = Label(top, text="", font=("Helvetica", 15))#本作品作者吴宇航
    timeText.place(x=180,y=370)#本作品作者吴宇航
    update_timeText()#本作品作者吴宇航
    #选择文件#本作品作者吴宇航
    xl = Button(top,text="选择文件",command=play,width=10,bg="sky blue")#本作品作者吴宇航
    xl.place(x=20,y=20)#本作品作者吴宇航
    Entry(top,text=path,width=25,state='readonly').place(x=120,y=20)#本作品作者吴宇航
#本作品作者吴宇航
    #选择图片#本作品作者吴宇航
    yl = Button(top,text='选择图片', command=choosepic,width=10,bg="sky blue")#本作品作者吴宇航
    yl.place(x=20,y=55)#本作品作者吴宇航
    e1=Entry(top,text=paths,state='readonly',width=25)#本作品作者吴宇航
    e1.place(x=120,y=55)#本作品作者吴宇航
    l1=Label(top)#图片放置位置#本作品作者吴宇航
    l1.place(x=320,y=0)#本作品作者吴宇航
#本作品作者吴宇航
   #本作品作者吴宇航
#本作品作者吴宇航
    #随机播放#本作品作者吴宇航
    Button(top,text="随机播放",command=selectPath,width=7,bg="sky blue").place(x=20,y=225)#本作品作者吴宇航
    l2=Label(top,text='',width=25,font=("Helvetica", 16))#音乐名#本作品作者吴宇航
    l2.place(x=0,y=100)#本作品作者吴宇航
    Button(top,text="下一首",command=loops,width=5,bg="sky blue").place(x=100,y=225)#本作品作者吴宇航
    l3=Label(top,text='',width=15)#音乐时长#本作品作者吴宇航
    l3.place(x=24,y=150)#本作品作者吴宇航
    #暂停，继续播放，结束播放#本作品作者吴宇航
    Button(top,text="暂停",command=pause,width=7,bg="sky blue").place(x=170,y=245)#本作品作者吴宇航
    Button(top,text="继续播放",command=unpause,width=7,bg="sky blue").place(x=170,y=205)#本作品作者吴宇航
    Button(top,text="结束播放",command=stop,width=7,bg="sky blue").place(x=240,y=225)#本作品作者吴宇航
#本作品作者吴宇航
    #提醒功能#本作品作者吴宇航
    Button(top,text='提醒功能', command=loop,width=10,bg="sky blue").place(x=20,y=325)#本作品作者吴宇航
    #使用说明#本作品作者吴宇航
    Button(top,text="使用说明",command = create,width=10,bg="sky blue").place(x=20,y=370)#本作品作者吴宇航
    #音量#本作品作者吴宇航
    w1 = Scale(top, from_=0,to=100, orient="horizontal",length=75,variable=v,command=printScale,label="音量")#本作品作者吴宇航
    w1.place(x=240,y=145)#本作品作者吴宇航
#本作品作者吴宇航
    w2 = Scale(top, from_=30,to=100, orient="horizontal",length=100,variable=v1,command=printsrceen,label="透明度")#本作品作者吴宇航
    w2.place(x=150,y=290)#本作品作者吴宇航
#本作品作者吴宇航
    top.mainloop()#本作品作者吴宇航
#本作品作者吴宇航
#图片查看器#本作品作者吴宇航
from os import *#本作品作者吴宇航
def photos():#本作品作者吴宇航
    system("图片查看软件.exe")#本作品作者吴宇航
#本作品作者吴宇航
#文件整理器#本作品作者吴宇航
import sys#本作品作者吴宇航
import platform#本作品作者吴宇航
#检测系统#本作品作者吴宇航
sysstr = platform.system()#本作品作者吴宇航
if sysstr!="Windows":#本作品作者吴宇航
    from tkinter import *#本作品作者吴宇航
    from tkinter import messagebox#本作品作者吴宇航
    tk=Tk()#本作品作者吴宇航
    tk.withdraw()#本作品作者吴宇航
    messagebox.showerror("错误","此程序仅支持windows!",parent=tk)#本作品作者吴宇航
    sys.exit()#本作品作者吴宇航
import os#本作品作者吴宇航
from PyQt5.QtWidgets import *#本作品作者吴宇航
from PyQt5.QtGui import *#本作品作者吴宇航
from PyQt5.QtCore import Qt#本作品作者吴宇航
import shutil#本作品作者吴宇航
def zhengli():#本作品作者吴宇航
#本作品作者吴宇航
    global path#本作品作者吴宇航
    path=None#本作品作者吴宇航
    global showpath#本作品作者吴宇航
    showpath=None#本作品作者吴宇航
    global defultdir#本作品作者吴宇航
    defultdir=os.getcwd()#本作品作者吴宇航
#本作品作者吴宇航
    class MainWindow(QMainWindow):#本作品作者吴宇航
        def closeEvent(self,event):#本作品作者吴宇航
            f=QMessageBox.question(window,"提示","确认退出吗？")#本作品作者吴宇航
            #本作品作者吴宇航
            if f==QMessageBox.No:#本作品作者吴宇航
                event.ignore()#本作品作者吴宇航
            else:#本作品作者吴宇航
                event.accept()#本作品作者吴宇航
    #文件类型的字典表（如果类型有遗漏欢迎提出）#本作品作者吴宇航
    formats={#本作品作者吴宇航
        "音频":[".mp3",".wav",".m4a"],#本作品作者吴宇航
        "视频":[".mp4",".mov",".wmv"],#本作品作者吴宇航
        "图片":[".jpg",".png",".gif",".bmp",".ico"],#本作品作者吴宇航
        "文档":[".txt",".doc",".docx",".xls",".xlsx",".ppt",".pptx",".pdf"],#本作品作者吴宇航
        "应用程序":[".vbs",".bat",".msi",".exe",".cmd"],#本作品作者吴宇航
        "压缩包":[".zip",".rar",".7z"]#本作品作者吴宇航
    }#本作品作者吴宇航
    #选择文件夹#本作品作者吴宇航
    def choose():#本作品作者吴宇航
        global path#本作品作者吴宇航
        global showpath#本作品作者吴宇航
        a=QFileDialog.getExistingDirectory(window,"选取要整理的文件夹")#本作品作者吴宇航
        if a!='':#本作品作者吴宇航
            path=a#本作品作者吴宇航
            os.chdir(path)#本作品作者吴宇航
            btngo.setEnabled(True)#本作品作者吴宇航
            label2.setText("已选择文件夹")#本作品作者吴宇航
            label2.setToolTip("<font color='#0762f8'>已选择文件夹")#本作品作者吴宇航
            if len(path) >= 17:#本作品作者吴宇航
                showpath=path[0:12]+'...'#本作品作者吴宇航
            label3.setText('''<a href='#' style="text-decoration:none;color:black;">'''+showpath)#本作品作者吴宇航
            palette=QPalette()#本作品作者吴宇航
            palette.setColor(QPalette.WindowText,QColor("#0762f8"))#本作品作者吴宇航
            label2.setPalette(palette)#本作品作者吴宇航
    #选择文件夹#本作品作者吴宇航
    #弹窗显示文件夹路径#本作品作者吴宇航
    def showdir():#本作品作者吴宇航
        dialogdir=QDialog(window)#本作品作者吴宇航
        dialogdir.setWindowTitle("智能文件夹整理器（作者：陈明翰）- 显示文件夹路径")#本作品作者吴宇航
        dialogdir.setModal(Qt.ApplicationModal)#本作品作者吴宇航
        #本作品作者吴宇航
        layout=QVBoxLayout()#本作品作者吴宇航
        labeldir=QLabel()#本作品作者吴宇航
        labeldir.setText(path)#本作品作者吴宇航
        labeldir.setToolTip("完整文件夹路径")#本作品作者吴宇航
        labeldir.setFont(QFont("Microsoft Yahei",20))#本作品作者吴宇航
        labeldir.setAlignment(Qt.AlignCenter)#本作品作者吴宇航
        labelopen=QLabel("<a href='#'>在资源管理器打开")#本作品作者吴宇航
        labelopen.setToolTip("在资源管理器打开")#本作品作者吴宇航
        labelopen.setFont(QFont("Microsoft Yahei",20))#本作品作者吴宇航
        labelopen.setAlignment(Qt.AlignRight)#本作品作者吴宇航
        labelopen.linkActivated.connect(lambda:os.system("explorer ."))#本作品作者吴宇航
        #本作品作者吴宇航
        layout.addWidget(labeldir,alignment=Qt.AlignCenter)#本作品作者吴宇航
        layout.addWidget(labelopen,alignment=Qt.AlignRight)#本作品作者吴宇航
        #本作品作者吴宇航
        dialogdir.setLayout(layout)#本作品作者吴宇航
        dialogdir.setFixedSize(dialogdir.minimumWidth(),dialogdir.minimumHeight())#本作品作者吴宇航
        dialogdir.exec()#本作品作者吴宇航
    #弹窗显示文件夹路径#本作品作者吴宇航
    #整理功能#本作品作者吴宇航
    def go():#本作品作者吴宇航
        label2.setText("整理中")#本作品作者吴宇航
        label2.setToolTip("<font color='#c89100'>整理中")#本作品作者吴宇航
        palette=QPalette()#本作品作者吴宇航
        palette.setColor(QPalette.WindowText,QColor("#c89100"))#本作品作者吴宇航
        label2.setPalette(palette)#本作品作者吴宇航
        try:#本作品作者吴宇航
            for i in os.listdir():#本作品作者吴宇航
                if i=="文件夹" or i=="压缩包" or i=="应用程序" or i=="文档" or i=="图片" or i=="视频" or i=="音频" or i=="其他":#本作品作者吴宇航
                    continue#本作品作者吴宇航
                ext=os.path.splitext(i)[-1].lower()#本作品作者吴宇航
                if os.path.isdir(i):#本作品作者吴宇航
                    if not os.path.isdir("文件夹"):#本作品作者吴宇航
                        os.mkdir("文件夹")#本作品作者吴宇航
                    shutil.move(i,f"文件夹/{i}")#本作品作者吴宇航
                    continue#本作品作者吴宇航
                fff=False#本作品作者吴宇航
                for d,exts in formats.items():#本作品作者吴宇航
                    if not os.path.isdir(d):#本作品作者吴宇航
                        os.mkdir(d)#本作品作者吴宇航
                    if ext in exts:#本作品作者吴宇航
                        shutil.move(i,f"{d}/{i}")#本作品作者吴宇航
                        fff=True#本作品作者吴宇航
                if fff==False:#本作品作者吴宇航
                    if not os.path.isdir("其他"):#本作品作者吴宇航
                        os.mkdir("其他")#本作品作者吴宇航
                    shutil.move(i,f"其他/{i}")#本作品作者吴宇航
            label2.setText("整理成功")#本作品作者吴宇航
            label2.setToolTip("<font color='#009170'>整理成功")#本作品作者吴宇航
            palette=QPalette()#本作品作者吴宇航
            palette.setColor(QPalette.WindowText,QColor("#009170"))#本作品作者吴宇航
            label2.setPalette(palette)#本作品作者吴宇航
            QMessageBox.information(window,"提示","整理成功")#本作品作者吴宇航
#本作品作者吴宇航
        except:#本作品作者吴宇航
            label2.setText("整理失败")#本作品作者吴宇航
            label2.setToolTip("<font color='#fe435a'>整理失败")#本作品作者吴宇航
            palette=QPalette()#本作品作者吴宇航
            palette.setColor(QPalette.WindowText,QColor("#fe435a"))#本作品作者吴宇航
            label2.setPalette(palette)#本作品作者吴宇航
            QMessageBox.critical(window,"错误","整理失败！")#本作品作者吴宇航
    #整理功能#本作品作者吴宇航
    #使用帮助#本作品作者吴宇航
    def use_help():#本作品作者吴宇航
        dialog=QDialog(window)#本作品作者吴宇航
        dialog.setWindowTitle("智能文件夹整理器（作者：陈明翰）- 使用帮助")#本作品作者吴宇航
        dialog.setFixedSize(dialog.minimumWidth(),dialog.minimumHeight())#本作品作者吴宇航
        dialog.setModal(Qt.ApplicationModal)#本作品作者吴宇航
#本作品作者吴宇航
        layouthelp=QVBoxLayout()#本作品作者吴宇航
#本作品作者吴宇航
        labelhelp=QLabel("作者：陈明翰，转载请保留原作者。\n本作品能够直接帮您为乱七八糟的文件夹进行分类，\n只需要先选择要整理的文件夹，然后开始整理即可。\n（详细使用步骤可观看帮助视频↓）")#本作品作者吴宇航
        #本作品作者吴宇航
        labelhelp.setToolTip("帮助信息")#本作品作者吴宇航
        #本作品作者吴宇航
        labelhelp.setFont(QFont("Microsoft Yahei",20))#本作品作者吴宇航
        labelhelp.setAlignment(Qt.AlignCenter)#本作品作者吴宇航
        #本作品作者吴宇航
        #本作品作者吴宇航
#本作品作者吴宇航
        layouthelp.addWidget(labelhelp)#本作品作者吴宇航
        #本作品作者吴宇航
#本作品作者吴宇航
        dialog.setLayout(layouthelp)#本作品作者吴宇航
        dialog.exec()#本作品作者吴宇航
    #使用帮助#本作品作者吴宇航
    #下面是界面代码#本作品作者吴宇航
    app=QApplication(sys.argv)#本作品作者吴宇航
    window=MainWindow()#本作品作者吴宇航
#本作品作者吴宇航
    window.setWindowIcon(QIcon("icon.png"))#本作品作者吴宇航
    window.setWindowTitle("智能文件夹整理器（作者：陈明翰）")#本作品作者吴宇航
#本作品作者吴宇航
    QToolTip.setFont(QFont("Microsoft Yahei",12))#本作品作者吴宇航
    layout=QGridLayout()#本作品作者吴宇航
    layout.setAlignment(Qt.AlignCenter)#本作品作者吴宇航
    widget=QWidget()#本作品作者吴宇航
#本作品作者吴宇航
    btnchoose=QPushButton("选择文件夹")#140 41#本作品作者吴宇航
    btnchoose.setFixedSize(140,41)#本作品作者吴宇航
    btnchoose.setToolTip("选择文件夹")#本作品作者吴宇航
    btnchoose.setFont(QFont("Microsoft Yahei",20))#本作品作者吴宇航
    btnchoose.clicked.connect(choose)#本作品作者吴宇航
#本作品作者吴宇航
    btnabout=QPushButton("关于我们")#本作品作者吴宇航
    btnabout.setFixedSize(140,41)#本作品作者吴宇航
    btnabout.setToolTip("关于我们")#本作品作者吴宇航
    btnabout.setFont(QFont("Microsoft Yahei",20))#本作品作者吴宇航
    btnabout.clicked.connect(lambda:QMessageBox.about(window,"关于我们","Hello智能文件夹整理器\n     （作者：陈明翰）\n    转载请保留原作者！"))#本作品作者吴宇航
#本作品作者吴宇航
    label1=QLabel("当前状态:")#本作品作者吴宇航
    label1.setSizePolicy(QSizePolicy.Minimum,QSizePolicy.Minimum)#本作品作者吴宇航
    label1.setToolTip("当前状态")#本作品作者吴宇航
    label1.setFont(QFont("Microsoft Yahei",20))#本作品作者吴宇航
#本作品作者吴宇航
    label2=QLabel("未选择文件夹")#本作品作者吴宇航
    label2.setSizePolicy(QSizePolicy.Minimum,QSizePolicy.Minimum)#本作品作者吴宇航
    label2.setToolTip("未选择文件夹")#本作品作者吴宇航
    label2.setFont(QFont("Microsoft Yahei",20))#本作品作者吴宇航
#本作品作者吴宇航
    label3=QLabel("文件夹路径")#本作品作者吴宇航
    label3.setSizePolicy(QSizePolicy.Minimum,QSizePolicy.Minimum)#本作品作者吴宇航
    label3.setToolTip("文件夹路径")#本作品作者吴宇航
    label3.linkActivated.connect(showdir)#本作品作者吴宇航
    label3.setFont(QFont("Microsoft Yahei",20))#本作品作者吴宇航
#本作品作者吴宇航
    btngo=QPushButton("开始整理")#本作品作者吴宇航
    btngo.setFixedSize(140,41)#本作品作者吴宇航
    btngo.setToolTip("开始整理")#本作品作者吴宇航
    btngo.setEnabled(False)#本作品作者吴宇航
    btngo.setFont(QFont("Microsoft Yahei",20))#本作品作者吴宇航
    btngo.clicked.connect(go)#本作品作者吴宇航
#本作品作者吴宇航
    btnquit=QPushButton("使用帮助")#本作品作者吴宇航
    btnquit.setFixedSize(140,41)#本作品作者吴宇航
    btnquit.setToolTip("使用帮助")#本作品作者吴宇航
    btnquit.setFont(QFont("Microsoft Yahei",20))#本作品作者吴宇航
    btnquit.clicked.connect(use_help)#本作品作者吴宇航
#本作品作者吴宇航
    layout.addWidget(label1,0,0,alignment=Qt.AlignCenter)#本作品作者吴宇航
    layout.addWidget(label2,0,1,alignment=Qt.AlignCenter)#本作品作者吴宇航
    layout.addWidget(label3,1,0,1,2,alignment=Qt.AlignCenter)#本作品作者吴宇航
    layout.addWidget(btnchoose,2,0,alignment=Qt.AlignCenter)#本作品作者吴宇航
    layout.addWidget(btngo,2,1,alignment=Qt.AlignCenter)#本作品作者吴宇航
    layout.addWidget(btnabout,3,0,alignment=Qt.AlignCenter)#本作品作者吴宇航
    layout.addWidget(btnquit,3,1,alignment=Qt.AlignCenter)#本作品作者吴宇航
    widget.setLayout(layout)#本作品作者吴宇航
    window.setToolTip("智能文件夹整理器（作者：陈明翰）")#本作品作者吴宇航
    window.setCentralWidget(widget)#本作品作者吴宇航
    window.setFixedSize(356,188)#本作品作者吴宇航
#本作品作者吴宇航
    window.show()#本作品作者吴宇航
    sys.exit(app.exec_())#本作品作者吴宇航
#本作品作者吴宇航
#奥运会结果#本作品作者吴宇航
import pygame,sys,requests,tkinter#本作品作者吴宇航
from bs4 import BeautifulSoup#本作品作者吴宇航
from tkinter import messagebox#本作品作者吴宇航
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36'}#本作品作者吴宇航
model = requests.get("https://tiyu.baidu.com/tokyoly/home/tab/奖牌榜/from/pc",headers=headers).text#本作品作者吴宇航
find = BeautifulSoup(model)#本作品作者吴宇航
findtest = find.find_all("div", class_="item-gold china")#本作品作者吴宇航
findtestb = find.find_all("div", class_="item-silver china")#本作品作者吴宇航
findtestc = find.find_all("div", class_="item-copper china")#本作品作者吴宇航
sort = find.find_all("span", class_="name")#本作品作者吴宇航
gold = find.find_all("div", class_="item-gold")#本作品作者吴宇航
sil = find.find_all("div", class_="item-silver")#本作品作者吴宇航
cop = find.find_all("div", class_="item-copper")#本作品作者吴宇航
tadic={}#本作品作者吴宇航
cou=0#本作品作者吴宇航
def aoyunhui():#本作品作者吴宇航
    for i in range(len(sort)):#本作品作者吴宇航
        if str(i) == "0":#本作品作者吴宇航
            aft=[int(findtest[0].text),int(findtestb[0].text),int(findtestc[0].text),int(findtest[0].text)+int(findtestb[0].text)+int(findtestc[0].text)]#本作品作者吴宇航
        else:#本作品作者吴宇航
            aft=[int(gold[i].text),int(sil[i].text),int(cop[i].text),int(gold[i].text)+int(sil[i].text)+int(cop[i].text)]#本作品作者吴宇航
        tadic[sort[i].text]=aft#本作品作者吴宇航
    def nextd():#本作品作者吴宇航
        global tadic#本作品作者吴宇航
        global cou#本作品作者吴宇航
        global sort#本作品作者吴宇航
        if cou >= len(sort):#本作品作者吴宇航
            messagebox.showwarning("提示","已是最后一个了")#本作品作者吴宇航
        elif cou+10 >=len(sort):#本作品作者吴宇航
            for i in range(len(sort)-cou):#本作品作者吴宇航
                if len(sort[cou].text) <6:#本作品作者吴宇航
                    wm = 6-len(sort[cou].text)#本作品作者吴宇航
                if len(sort[cou].text) == 4:#本作品作者吴宇航
                    wm +=1       #本作品作者吴宇航
                elif len(sort[cou].text) == 3:#本作品作者吴宇航
                    wm +=2 #本作品作者吴宇航
                elif len(sort[cou].text) == 2:#本作品作者吴宇航
                    wm +=3 #本作品作者吴宇航
                else:#本作品作者吴宇航
                    wm=0#本作品作者吴宇航
                m.insert("end","\n"+sort[cou].text+":") #本作品作者吴宇航
                for i in range(wm):#本作品作者吴宇航
                    m.insert("end"," ")#本作品作者吴宇航
                m.insert("end",str(tadic[sort[cou].text][0])+"  "+str(tadic[sort[cou].text][1])+"  "+str(tadic[sort[cou].text][2])+"  "+str(tadic[sort[cou].text][3])+"  ")#本作品作者吴宇航
                cou+=1#本作品作者吴宇航
        else:#本作品作者吴宇航
            for i in range(10):#本作品作者吴宇航
                if len(sort[cou].text) <6:#本作品作者吴宇航
                    wm = 6-len(sort[cou].text)#本作品作者吴宇航
                if len(sort[cou].text) == 4:#本作品作者吴宇航
                    wm +=3       #本作品作者吴宇航
                elif len(sort[cou].text) == 3:#本作品作者吴宇航
                    wm +=5  #本作品作者吴宇航
                elif len(sort[cou].text) == 2:#本作品作者吴宇航
                    wm +=7#本作品作者吴宇航
                else:#本作品作者吴宇航
                    wm=0#本作品作者吴宇航
                m.insert("end","\n"+sort[cou].text+":") #本作品作者吴宇航
                for i in range(wm):#本作品作者吴宇航
                    m.insert("end"," ")#本作品作者吴宇航
                m.insert("end",str(tadic[sort[cou].text][0])+"  "+str(tadic[sort[cou].text][1])+"  "+str(tadic[sort[cou].text][2])+"  "+str(tadic[sort[cou].text][3])+"  ")#本作品作者吴宇航
                cou+=1#本作品作者吴宇航
    root = tkinter.Tk()#本作品作者吴宇航
    root.geometry('+600+400')#本作品作者吴宇航
    root.resizable(0,0)#本作品作者吴宇航
    root.configure(background="skyblue")#本作品作者吴宇航
    root.geometry("300x600")#本作品作者吴宇航
    root.resizable(0,0)#本作品作者吴宇航
    root.title("奥运金牌排行榜")#本作品作者吴宇航
    m = tkinter.Text(root)#本作品作者吴宇航
    m.insert("insert","国家           金  银  铜  总\n")#本作品作者吴宇航
    b = tkinter.Button(root,text="下一页",command=nextd)#本作品作者吴宇航
    m.place(x=20,y=20,width=260,height=460)#本作品作者吴宇航
    b.place(x=100,y=515,width=100,height=30)#本作品作者吴宇航
    root.mainloop()#本作品作者吴宇航
#本作品作者吴宇航
#搜索导航#本作品作者吴宇航
def sousou():#本作品作者吴宇航
    cefpython.Initialize()#本作品作者吴宇航
    #本作品作者吴宇航
    def fangwen(a):#本作品作者吴宇航
    #本作品作者吴宇航
        if "https://" in a:#本作品作者吴宇航
            a = a.replace("https://","http://")#本作品作者吴宇航
        if "http://" not in a:#本作品作者吴宇航
            a = "http://" + a#本作品作者吴宇航
        cefpython.CreateBrowserSync(cefpython.WindowInfo(),url = a)#本作品作者吴宇航
        cefpython.MessageLoop()#本作品作者吴宇航
#本作品作者吴宇航
    fangwen("https://livefile.xesimg.com/programme/python_assets/612a2e8f7ee61e4745beccc5cd20bf33.html")#本作品作者吴宇航
    fasdasdf1()#本作品作者吴宇航
#本作品作者吴宇航
#谷歌小恐龙#本作品作者吴宇航
def dino():#本作品作者吴宇航
    # 地图#本作品作者吴宇航
    class GameBackground:#本作品作者吴宇航
        image1 = None#本作品作者吴宇航
        image2 = None#本作品作者吴宇航
        main_scene = None#本作品作者吴宇航
        speed = 10 # 滚动速度#本作品作者吴宇航
        x1 = None#本作品作者吴宇航
        x2 = None#本作品作者吴宇航
    #本作品作者吴宇航
        # 初始化地图#本作品作者吴宇航
        def __init__(self, scene):#本作品作者吴宇航
            # 加载相同张图片资源,做交替实现地图滚动#本作品作者吴宇航
            self.image1 = pygame.image.load("images/dragon/map.png")#本作品作者吴宇航
            self.image2 = self.image1#本作品作者吴宇航
            # 保存场景对象#本作品作者吴宇航
            self.main_scene = scene#本作品作者吴宇航
            # 辅助移动地图#本作品作者吴宇航
            self.x1 = 0#本作品作者吴宇航
            self.x2 = self.main_scene.size[0]#本作品作者吴宇航
    #本作品作者吴宇航
        # 计算地图图片绘制坐标#本作品作者吴宇航
        def action(self):#本作品作者吴宇航
            self.x1 = self.x1 - self.speed#本作品作者吴宇航
            self.x2 = self.x2 - self.speed#本作品作者吴宇航
            if self.x1 <= -self.main_scene.size[0]:#本作品作者吴宇航
                self.x1 = 0#本作品作者吴宇航
            if self.x2 <= 0:#本作品作者吴宇航
                self.x2 = self.main_scene.size[0]#本作品作者吴宇航
    #本作品作者吴宇航
        # 绘制地图的两张图片#本作品作者吴宇航
        def draw(self):#本作品作者吴宇航
            map_y = self.main_scene.size[1] - self.image1.get_height()#本作品作者吴宇航
            self.main_scene.scene.blit(self.image1, (self.x1, map_y))#本作品作者吴宇航
            self.main_scene.scene.blit(self.image2, (self.x2, map_y))#本作品作者吴宇航
    #本作品作者吴宇航
    # 云#本作品作者吴宇航
    class Cloud:#本作品作者吴宇航
        speed = 1#本作品作者吴宇航
        image = None#本作品作者吴宇航
        x = None#本作品作者吴宇航
        y = None#本作品作者吴宇航
    #本作品作者吴宇航
        def __init__(self, x, y, image):#本作品作者吴宇航
            self.x = x#本作品作者吴宇航
            self.y = y#本作品作者吴宇航
            self.image = image#本作品作者吴宇航
    #本作品作者吴宇航
        def move(self):#本作品作者吴宇航
            self.x -= self.speed#本作品作者吴宇航
    #本作品作者吴宇航
    # 仙人掌#本作品作者吴宇航
    class Cactus:#本作品作者吴宇航
        speed = 10#本作品作者吴宇航
        image = None#本作品作者吴宇航
        x = None#本作品作者吴宇航
        y = None#本作品作者吴宇航
        width = None#本作品作者吴宇航
        height = None#本作品作者吴宇航
    #本作品作者吴宇航
        def __init__(self, x, y, image):#本作品作者吴宇航
            self.x = x#本作品作者吴宇航
            self.y = y#本作品作者吴宇航
            self.image = image#本作品作者吴宇航
            self.width = image.get_width()#本作品作者吴宇航
            self.height = image.get_height()#本作品作者吴宇航
    #本作品作者吴宇航
        def move(self):#本作品作者吴宇航
            self.x -= self.speed#本作品作者吴宇航
    #本作品作者吴宇航
    # 鸟#本作品作者吴宇航
    class Bird:#本作品作者吴宇航
        speed = 15.5#本作品作者吴宇航
        image = None#本作品作者吴宇航
        x = None#本作品作者吴宇航
        y = None#本作品作者吴宇航
        width = None#本作品作者吴宇航
        height = None#本作品作者吴宇航
        index = 0#本作品作者吴宇航
        main_scene = None#本作品作者吴宇航
        ret = 1#本作品作者吴宇航
    #本作品作者吴宇航
        def __init__(self, x, y, image, main_scene):#本作品作者吴宇航
            self.x = x#本作品作者吴宇航
            self.y = y#本作品作者吴宇航
            self.image = image#本作品作者吴宇航
            self.main_scene = main_scene#本作品作者吴宇航
            image = self.image[self.index]#本作品作者吴宇航
            self.width = image.get_width()#本作品作者吴宇航
            self.height = image.get_height()#本作品作者吴宇航
    #本作品作者吴宇航
        def move(self):#本作品作者吴宇航
            self.x -= self.speed#本作品作者吴宇航
    #本作品作者吴宇航
        def draw(self):#本作品作者吴宇航
            if self.ret <= 8:#本作品作者吴宇航
                self.index = 0#本作品作者吴宇航
            else:#本作品作者吴宇航
                self.index = 1#本作品作者吴宇航
    #本作品作者吴宇航
            if self.ret == 16:#本作品作者吴宇航
                self.ret = 0#本作品作者吴宇航
    #本作品作者吴宇航
            image = self.image[self.index]#本作品作者吴宇航
            self.main_scene.scene.blit(image, (self.x, self.y))#本作品作者吴宇航
            self.ret += 1#本作品作者吴宇航
    #本作品作者吴宇航
    # 恐龙#本作品作者吴宇航
    class Dragon:#本作品作者吴宇航
        speed = 10#本作品作者吴宇航
        image = None#本作品作者吴宇航
        x = None#本作品作者吴宇航
        y = None#本作品作者吴宇航
        width = None#本作品作者吴宇航
        height = None#本作品作者吴宇航
        index = 0#本作品作者吴宇航
        main_scene = None#本作品作者吴宇航
        ret = 1#本作品作者吴宇航
        style = 0 # 0：站立，1：蹲下#本作品作者吴宇航
        jump = 0 # 0: 未起跳，1：开始上升，2：开始下降#本作品作者吴宇航
        jump_y_add = 0#本作品作者吴宇航
        is_hit = 0#本作品作者吴宇航
    #本作品作者吴宇航
        def __init__(self, x, y, image, main_scene):#本作品作者吴宇航
            self.x = x#本作品作者吴宇航
            self.y = y#本作品作者吴宇航
            self.image = image#本作品作者吴宇航
            self.main_scene = main_scene#本作品作者吴宇航
    #本作品作者吴宇航
        def set_jump(self):#本作品作者吴宇航
            if self.style == 0 and self.jump == 0:#本作品作者吴宇航
                self.jump = 1#本作品作者吴宇航
                self.main_scene.jump_sound.play()#本作品作者吴宇航
    #本作品作者吴宇航
        def move(self):#本作品作者吴宇航
            if self.jump == 1:#本作品作者吴宇航
                self.y -= 10#本作品作者吴宇航
                self.jump_y_add += 10#本作品作者吴宇航
                if self.jump_y_add == 200:#本作品作者吴宇航
                    self.jump = 2#本作品作者吴宇航
    #本作品作者吴宇航
            if self.jump == 2:#本作品作者吴宇航
                self.y += 10#本作品作者吴宇航
                self.jump_y_add -= 10#本作品作者吴宇航
                if self.jump_y_add == 0:#本作品作者吴宇航
                    self.jump = 0#本作品作者吴宇航
    #本作品作者吴宇航
        def draw(self):#本作品作者吴宇航
            if self.ret <= 5:#本作品作者吴宇航
                if self.style == 0:#本作品作者吴宇航
                    self.index = 0#本作品作者吴宇航
                else:#本作品作者吴宇航
                    self.index = 2#本作品作者吴宇航
            else:#本作品作者吴宇航
                if self.style == 0:#本作品作者吴宇航
                    self.index = 1#本作品作者吴宇航
                else:#本作品作者吴宇航
                    self.index = 3#本作品作者吴宇航
    #本作品作者吴宇航
            if self.ret == 10:#本作品作者吴宇航
                self.ret = 0#本作品作者吴宇航
    #本作品作者吴宇航
            image = self.image[self.index]#本作品作者吴宇航
            self.width = image.get_width()#本作品作者吴宇航
            self.height = image.get_height()#本作品作者吴宇航
            self.main_scene.scene.blit(image, (self.x, self.y))#本作品作者吴宇航
            self.ret += 1#本作品作者吴宇航
    #本作品作者吴宇航
    # 主场景#本作品作者吴宇航
    class MainScene:#本作品作者吴宇航
        running = True#本作品作者吴宇航
        size = None#本作品作者吴宇航
        scene = None#本作品作者吴宇航
        bg = None#本作品作者吴宇航
    #本作品作者吴宇航
        clouds = []#本作品作者吴宇航
        cloud_image = None#本作品作者吴宇航
    #本作品作者吴宇航
        items = []#本作品作者吴宇航
        item_images = []#本作品作者吴宇航
        item_ret= 1#本作品作者吴宇航
        item_ret_num = 100#本作品作者吴宇航
    #本作品作者吴宇航
        bird_images = []#本作品作者吴宇航
        birds = []#本作品作者吴宇航
        bird_ret= 1#本作品作者吴宇航
        bird_ret_num = 150#本作品作者吴宇航
    #本作品作者吴宇航
        dragon = None#本作品作者吴宇航
        dragon_images = []#本作品作者吴宇航
    #本作品作者吴宇航
        gameover_image = None#本作品作者吴宇航
        restart_image = None#本作品作者吴宇航
        restart_x = None#本作品作者吴宇航
        restart_y = None#本作品作者吴宇航
        score = 0.0#本作品作者吴宇航
    #本作品作者吴宇航
        jump_sound = None#本作品作者吴宇航
        gameover_sound = None#本作品作者吴宇航
    #本作品作者吴宇航
        # 初始化主场景#本作品作者吴宇航
        def __init__(self):#本作品作者吴宇航
            # 初始化 pygame，使用自定义字体必须用到#本作品作者吴宇航
            pygame.init()#本作品作者吴宇航
            # 场景尺寸#本作品作者吴宇航
            self.size = (800, 350)#本作品作者吴宇航
            # 场景对象#本作品作者吴宇航
            self.scene = pygame.display.set_mode([self.size[0], self.size[1]])#本作品作者吴宇航
            # 设置标题#本作品作者吴宇航
            pygame.display.set_caption("恐龙跑酷")#本作品作者吴宇航
            # 创建clock对象控制帧数#本作品作者吴宇航
            self.timer = pygame.time.Clock()#本作品作者吴宇航
    #本作品作者吴宇航
            # 创建地图对象#本作品作者吴宇航
            self.bg = GameBackground(self)#本作品作者吴宇航
    #本作品作者吴宇航
            # 创建云#本作品作者吴宇航
            self.cloud_image = pygame.image.load("images/dragon/cloud.png")#本作品作者吴宇航
            self.create_cloud()#本作品作者吴宇航
    #本作品作者吴宇航
            # 创建仙人掌#本作品作者吴宇航
            for n in range(7):#本作品作者吴宇航
                self.item_images.append(pygame.image.load("images/dragon/item_" + str(n+1) + ".png"))#本作品作者吴宇航
    #本作品作者吴宇航
            # 创建鸟#本作品作者吴宇航
            self.bird_images.append(pygame.image.load("images/dragon/bird_1.png"))#本作品作者吴宇航
            self.bird_images.append(pygame.image.load("images/dragon/bird_2.png"))#本作品作者吴宇航
    #本作品作者吴宇航
            # 创建恐龙#本作品作者吴宇航
            for n in range(4):#本作品作者吴宇航
                self.dragon_images.append(pygame.image.load("images/dragon/dragon_" + str(n+1) + ".png"))#本作品作者吴宇航
    #本作品作者吴宇航
            d_x = 50#本作品作者吴宇航
            d_y = self.size[1] - self.dragon_images[0].get_height()#本作品作者吴宇航
            self.dragon = Dragon(d_x, d_y, self.dragon_images, self)#本作品作者吴宇航
    #本作品作者吴宇航
            # gameover#本作品作者吴宇航
            self.gameover_image = pygame.image.load("images/dragon/gameover.png")#本作品作者吴宇航
            self.restart_image = pygame.image.load("images/dragon/restart.png")#本作品作者吴宇航
    #本作品作者吴宇航
            # 音效加载#本作品作者吴宇航
            self.jump_sound = pygame.mixer.Sound("sounds/dragon/jump.wav")#本作品作者吴宇航
            self.gameover_sound = pygame.mixer.Sound("sounds/dragon/gameover.wav")#本作品作者吴宇航
    #本作品作者吴宇航
        #  生成两朵云#本作品作者吴宇航
        def create_cloud(self):#本作品作者吴宇航
            self.clouds.append(Cloud(350, 30, self.cloud_image))#本作品作者吴宇航
            self.clouds.append(Cloud(650, 100, self.cloud_image))#本作品作者吴宇航
    #本作品作者吴宇航
        # 绘制#本作品作者吴宇航
        def draw_elements(self):#本作品作者吴宇航
            if self.dragon.is_hit == 1:#本作品作者吴宇航
                g_x = self.size[0] // 2 - self.gameover_image.get_width() // 2#本作品作者吴宇航
                self.scene.blit(self.gameover_image, (g_x, 120))#本作品作者吴宇航
    #本作品作者吴宇航
                self.restart_x = self.size[0] // 2 - self.restart_image.get_width() // 2#本作品作者吴宇航
                self.restart_y = 170#本作品作者吴宇航
                self.scene.blit(self.restart_image, (self.restart_x, self.restart_y))#本作品作者吴宇航
                return#本作品作者吴宇航
    #本作品作者吴宇航
            self.scene.fill((255, 255, 255)) # 填充背景色为白色#本作品作者吴宇航
            self.bg.draw()                   # 绘制背景#本作品作者吴宇航
    #本作品作者吴宇航
            # 绘制云#本作品作者吴宇航
            for c in self.clouds[:]:#本作品作者吴宇航
                self.scene.blit(c.image, (c.x, c.y))#本作品作者吴宇航
    #本作品作者吴宇航
            # 绘制仙人掌#本作品作者吴宇航
            for i in self.items[:]:#本作品作者吴宇航
                self.scene.blit(i.image, (i.x, i.y))#本作品作者吴宇航
    #本作品作者吴宇航
            # 绘制鸟#本作品作者吴宇航
            for b in self.birds[:]:#本作品作者吴宇航
                b.draw()#本作品作者吴宇航
    #本作品作者吴宇航
            # 绘制恐龙#本作品作者吴宇航
            self.dragon.draw()#本作品作者吴宇航
    #本作品作者吴宇航
            # 绘制跑动距离#本作品作者吴宇航
            self.score += 0.1#本作品作者吴宇航
            font = pygame.font.Font("freesansbold.ttf", 20)#本作品作者吴宇航
            text = font.render(str(int(self.score)) + "m", True, (83, 83, 83))#本作品作者吴宇航
            text_rect = text.get_rect()#本作品作者吴宇航
            text_rect.right = self.size[0] - 10#本作品作者吴宇航
            text_rect.top = 10#本作品作者吴宇航
            self.scene.blit(text, text_rect)#本作品作者吴宇航
    #本作品作者吴宇航
        # 计算元素坐标及生成元素#本作品作者吴宇航
        def action_elements(self):#本作品作者吴宇航
            if self.dragon.is_hit == 1:#本作品作者吴宇航
                return#本作品作者吴宇航
    #本作品作者吴宇航
            # 地图#本作品作者吴宇航
            self.bg.action()#本作品作者吴宇航
    #本作品作者吴宇航
            # 云#本作品作者吴宇航
            for c in self.clouds[:]:#本作品作者吴宇航
                c.move()#本作品作者吴宇航
    #本作品作者吴宇航
                if c.x < - self.cloud_image.get_width():#本作品作者吴宇航
                    self.clouds.remove(c)#本作品作者吴宇航
    #本作品作者吴宇航
            if len(self.clouds) == 0:#本作品作者吴宇航
                self.create_cloud()#本作品作者吴宇航
    #本作品作者吴宇航
            # 仙人掌#本作品作者吴宇航
            if self.item_ret % self.item_ret_num == 0:#本作品作者吴宇航
                image = self.item_images[random.randint(0, len(self.item_images) - 1)]#本作品作者吴宇航
                x = self.size[0]#本作品作者吴宇航
                y = self.size[1] - image.get_height()#本作品作者吴宇航
                self.items.append(Cactus(x, y, image))#本作品作者吴宇航
            self.item_ret += 1#本作品作者吴宇航
            if self.item_ret == self.item_ret_num:#本作品作者吴宇航
                self.item_ret = 0#本作品作者吴宇航
                self.item_ret_num = random.randint(60, 110)#本作品作者吴宇航
    #本作品作者吴宇航
            for i in self.items[:]:#本作品作者吴宇航
                i.move()#本作品作者吴宇航
    #本作品作者吴宇航
                if i.x < -i.width:#本作品作者吴宇航
                    self.items.remove(i)#本作品作者吴宇航
    #本作品作者吴宇航
            # 鸟#本作品作者吴宇航
            if int(self.score) > 100:#本作品作者吴宇航
                if self.bird_ret % self.bird_ret_num == 0:#本作品作者吴宇航
                    x = self.size[0]#本作品作者吴宇航
                    y = 210#本作品作者吴宇航
                    self.birds.append(Bird(x, y, self.bird_images, self))#本作品作者吴宇航
                self.bird_ret += 1#本作品作者吴宇航
                if self.bird_ret == self.bird_ret_num:#本作品作者吴宇航
                    self.bird_ret = 0#本作品作者吴宇航
                    self.bird_ret_num = random.randint(150, 300)#本作品作者吴宇航
    #本作品作者吴宇航
                for b in self.birds[:]:#本作品作者吴宇航
                    b.move()#本作品作者吴宇航
    #本作品作者吴宇航
                    if b.x < -b.width:#本作品作者吴宇航
                        self.birds.remove(b)#本作品作者吴宇航
    #本作品作者吴宇航
            # 恐龙#本作品作者吴宇航
            self.dragon.move()#本作品作者吴宇航
    #本作品作者吴宇航
        # 处理事件#本作品作者吴宇航
        def handle_event(self):#本作品作者吴宇航
            for event in pygame.event.get():#本作品作者吴宇航
                # 检测松开键盘事件#本作品作者吴宇航
                if event.type == pygame.KEYUP:#本作品作者吴宇航
                    if event.key == K_DOWN:#本作品作者吴宇航
                        if self.dragon.style == 1:#本作品作者吴宇航
                            self.dragon.style = 0#本作品作者吴宇航
                            self.dragon.y -= 34#本作品作者吴宇航
    #本作品作者吴宇航
                # 检测按下鼠标事件#本作品作者吴宇航
                if event.type == pygame.MOUSEBUTTONDOWN:#本作品作者吴宇航
                    if pygame.mouse.get_pressed()[0]:#本作品作者吴宇航
                        if self.dragon.is_hit == 1:#本作品作者吴宇航
                            pos = event.pos # 点击位置坐标#本作品作者吴宇航
    #本作品作者吴宇航
                            # 判断点击范围是否是重启图片上#本作品作者吴宇航
                            x1 = self.restart_x#本作品作者吴宇航
                            x2 = self.restart_x + self.restart_image.get_width()#本作品作者吴宇航
    #本作品作者吴宇航
                            y1 = self.restart_y#本作品作者吴宇航
                            y2 = self.restart_y + self.restart_image.get_height()#本作品作者吴宇航
    #本作品作者吴宇航
                            if pos[0] >= x1 and pos[0] <= x2 and pos[1] >= y1 and pos[1] <= y2:#本作品作者吴宇航
                                self.dragon.is_hit = 0#本作品作者吴宇航
                                self.score = 0#本作品作者吴宇航
                                self.items.clear()#本作品作者吴宇航
                                self.birds.clear()#本作品作者吴宇航
    #本作品作者吴宇航
    #本作品作者吴宇航
                # 检测到事件为退出时#本作品作者吴宇航
                if event.type == pygame.QUIT:#本作品作者吴宇航
                    self.running = False#本作品作者吴宇航
    #本作品作者吴宇航
        # 碰撞检测#本作品作者吴宇航
        def detect_collision(self):#本作品作者吴宇航
            if self.dragon.is_hit == 0:#本作品作者吴宇航
                for i in self.items[:]:#本作品作者吴宇航
                    if self.collision(self.dragon, i) or self.collision(i, self.dragon):#本作品作者吴宇航
                        self.dragon.is_hit = 1#本作品作者吴宇航
                        break#本作品作者吴宇航
    #本作品作者吴宇航
                for b in self.birds[:]:#本作品作者吴宇航
                    if self.collision(self.dragon, b) or self.collision(b, self.dragon):#本作品作者吴宇航
                        self.dragon.is_hit = 1#本作品作者吴宇航
                        break#本作品作者吴宇航
    #本作品作者吴宇航
                if self.dragon.is_hit == 1:#本作品作者吴宇航
                    self.gameover_sound.play()#本作品作者吴宇航
    #本作品作者吴宇航
        # 验证是否碰撞#本作品作者吴宇航
        def collision(self, a, b):#本作品作者吴宇航
            offset = 30 # 增加20误差，降低难度#本作品作者吴宇航
            temp1 = (b.x + offset <= a.x + a.width <= b.x + offset + b.width)#本作品作者吴宇航
            temp2 = (b.y + offset <= a.y + a.height <= b.y + offset + b.height)#本作品作者吴宇航
            return temp1 and temp2#本作品作者吴宇航
    #本作品作者吴宇航
        # 处理按键#本作品作者吴宇航
        def key_pressed(self):#本作品作者吴宇航
            # 获取按下按键信息#本作品作者吴宇航
            key_pressed = pygame.key.get_pressed()#本作品作者吴宇航
    #本作品作者吴宇航
            if key_pressed[K_DOWN]:#本作品作者吴宇航
                if self.dragon.jump == 0:#本作品作者吴宇航
                    if self.dragon.style == 0:#本作品作者吴宇航
                        self.dragon.style = 1#本作品作者吴宇航
                        self.dragon.y += 34#本作品作者吴宇航
    #本作品作者吴宇航
            if key_pressed[K_SPACE]:#本作品作者吴宇航
                self.dragon.set_jump()#本作品作者吴宇航
    #本作品作者吴宇航
        # 处理帧数#本作品作者吴宇航
        def set_fps(self):#本作品作者吴宇航
            # 刷新显示#本作品作者吴宇航
            pygame.display.update()#本作品作者吴宇航
            # 设置帧率为60fps#本作品作者吴宇航
            self.timer.tick(60)#本作品作者吴宇航
    #本作品作者吴宇航
        # 主循环,主要处理各种事件#本作品作者吴宇航
        def run_scene(self):#本作品作者吴宇航
    #本作品作者吴宇航
            while self.running:#本作品作者吴宇航
                # 计算元素坐标及生成元素#本作品作者吴宇航
                self.action_elements()#本作品作者吴宇航
                # 绘制元素图片#本作品作者吴宇航
                self.draw_elements()#本作品作者吴宇航
                # 处理事件#本作品作者吴宇航
                self.handle_event()#本作品作者吴宇航
                # 碰撞检测#本作品作者吴宇航
                self.detect_collision()#本作品作者吴宇航
                # 按键处理#本作品作者吴宇航
                self.key_pressed()#本作品作者吴宇航
                # 更新画布设置fps#本作品作者吴宇航
                self.set_fps()#本作品作者吴宇航
    #本作品作者吴宇航
    # 创建主场景#本作品作者吴宇航
    mainScene = MainScene()#本作品作者吴宇航
    # 开始游戏#本作品作者吴宇航
    mainScene.run_scene()#本作品作者吴宇航
#本作品作者吴宇航
#命令行cmd#本作品作者吴宇航
def cmds():#本作品作者吴宇航
    class tk:#本作品作者吴宇航
        from tkinter import Tk,Entry,Toplevel,Listbox#本作品作者吴宇航
        from tkinter.scrolledtext import ScrolledText#本作品作者吴宇航
    #设置信息，可选#本作品作者吴宇航
    class terminal_infos:#本作品作者吴宇航
        version='1.0'#版本#本作品作者吴宇航
        by='Jeff'#作者#本作品作者吴宇航
        running_space={'__name__':'__console__'}#运行空间(用于存储变量的)#本作品作者吴宇航
        def print(*value):#本作品作者吴宇航
            return None#本作品作者吴宇航
        def input(*value):#本作品作者吴宇航
            return None#本作品作者吴宇航
        def set(*value):#本作品作者吴宇航
            return None#本作品作者吴宇航
        def Back(*value):#本作品作者吴宇航
            pass#本作品作者吴宇航
        del input,print,set,Back#本作品作者吴宇航
        # exec('''    def print(*value):#本作品作者吴宇航
        #     return None#本作品作者吴宇航
        # def input(*value):#本作品作者吴宇航
        #     return None#本作品作者吴宇航
        # def set(*value):#本作品作者吴宇航
        #     return None#本作品作者吴宇航
        # def Back(*value):#本作品作者吴宇航
        #     pass#本作品作者吴宇航
        # del input,print,set,Back''',running_space)#先把那些Python基础函数替换了#本作品作者吴宇航
        input_list=[]#这个是输入命令记载输入命令的列表#本作品作者吴宇航
    class os:#本作品作者吴宇航
        from os import getcwd,chdir,startfile,popen#本作品作者吴宇航
        from os.path import isfile,isdir#本作品作者吴宇航
    def run_command(command,terminal,commandinput):#本作品作者吴宇航
        def contiune_command():#本作品作者吴宇航
            terminal.insert('end','\n')#本作品作者吴宇航
            terminal.insert('end',f'\n{os.getcwd()}\n','green')#本作品作者吴宇航
            terminal.insert('end',f'$ ')#本作品作者吴宇航
            terminal.window_create('end',window=commandinput)#本作品作者吴宇航
            commandinput.focus_set()#"""#本作品作者吴宇航
        errortext=f'这是一个错误的指令："{command.strip()}"。'#本作品作者吴宇航
    #本作品作者吴宇航
        command=str(command)#这玩意是应付编辑器不知道command是什么类型的#本作品作者吴宇航
        terminal_infos.input_list.append(command)#增加输入了什么命令#本作品作者吴宇航
        terminal.config(state='n')#解锁terminal(Text)#本作品作者吴宇航
    #本作品作者吴宇航
        terminal.delete('end')#删除输入控件#本作品作者吴宇航
        commandinput.delete(0,'end')#删除控件里输入的文本#本作品作者吴宇航
        if command.strip() == "1":#本作品作者吴宇航
            print(1)#本作品作者吴宇航
        if command.strip()=='':#如果啥也没输入#本作品作者吴宇航
            terminal.insert('end',command)#就复述输入内容#本作品作者吴宇航
        elif os.isfile(command.strip().replace('"','')) or os.isfile(os.getcwd()+command.strip().replace('"','')) or os.isfile(command.strip().replace('"','')+'.exe') or os.isfile(os.getcwd()+command.strip().replace('"','')+'.exe'):#如果是个文件#本作品作者吴宇航
            try:#本作品作者吴宇航
                os.startfile(command.strip().replace('"',''))#本作品作者吴宇航
            except:#本作品作者吴宇航
                try:#本作品作者吴宇航
                    os.startfile(os.getcwd()+command.strip().replace('"',''))#本作品作者吴宇航
                except:#本作品作者吴宇航
                    try:#本作品作者吴宇航
                        os.startfile(command.strip().replace('"','')+'.exe')#本作品作者吴宇航
                    except:#本作品作者吴宇航
                        os.startfile(os.getcwd()+command.strip().replace('"','')+'.exe')#本作品作者吴宇航
            terminal.insert('end',command)#本作品作者吴宇航
            contiune_command()#本作品作者吴宇航
        elif len(command.strip())>=2:#当命令长度超过2时#本作品作者吴宇航
            if command[0:2]=='::':#本作品作者吴宇航
                terminal.insert('end',command)#本作品作者吴宇航
                contiune_command()#本作品作者吴宇航
            elif command[0:2]=='cd':#本作品作者吴宇航
                #移动目录#本作品作者吴宇航
                terminal.insert('end',command)#本作品作者吴宇航
                try:#本作品作者吴宇航
                    os.chdir(command.strip()[3:])#本作品作者吴宇航
                except OSError as error:#本作品作者吴宇航
                    terminal.insert('end','\n'+error.args[1]+'\n','red')#本作品作者吴宇航
                except:#本作品作者吴宇航
                    terminal.insert('end','\n移动至工作目录'+command.strip()[3:]+'失败。\n','red')#本作品作者吴宇航
                contiune_command()#本作品作者吴宇航
            elif len(command.strip())>=3:#当命令长度超过3时#本作品作者吴宇航
                if command.lower().strip()[0:3]=='dir':#本作品作者吴宇航
                    terminal.insert('end',command)#本作品作者吴宇航
                    if command.lower().strip()=='dir':#本作品作者吴宇航
                        try:#本作品作者吴宇航
                            terminal.insert('end','\n\n'+os.popen('dir '+os.getcwd()).read())#返回执行dir命令的文本(Windows下)#本作品作者吴宇航
                        except:#本作品作者吴宇航
                            pass#本作品作者吴宇航
                    elif len(command.lower().strip())>4:#本作品作者吴宇航
                        if os.isdir(command.strip()[4:].replace('"','')) or os.isdir(os.getcwd()+command.strip()[4:].replace('"',''))==True:#本作品作者吴宇航
                            terminal.insert('end','\n\n'+os.popen('dir '+command.strip()[4:]).read())#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        terminal.insert('end','\n'+errortext)#本作品作者吴宇航
                    contiune_command()#本作品作者吴宇航
                elif command.lower().strip()[0:3]=='set':#本作品作者吴宇航
                    #让用户设置变量的环节#本作品作者吴宇航
                    terminal.delete('end')#本作品作者吴宇航
                    if len(command.lower().strip())>3:#本作品作者吴宇航
                        if '=' in command[4:]:#本作品作者吴宇航
                            try:#本作品作者吴宇航
                                def tovar(varname,varvalue):#本作品作者吴宇航
                                    try:#本作品作者吴宇航
                                        exec(varname+'='+varvalue,terminal_infos.running_space)#本作品作者吴宇航
                                    except:#本作品作者吴宇航
                                        terminal.insert('end','\n接收输入失败。','red')#本作品作者吴宇航
                                    commandinput.bind('<Return>',lambda v=0:run_command(command_input.get(),TerminalText,command_input))#本作品作者吴宇航
                                    command_input.bind('<Return>',lambda v=0:run_command(command_input.get(),TerminalText,command_input))#本作品作者吴宇航
                                    contiune_command()#本作品作者吴宇航
                                terminal.insert('end',command)#本作品作者吴宇航
                                tovar(command[command.index(' ',0)+1:command.index('=',0)],command[command.index('=',0)+1:])#本作品作者吴宇航
                            except:#本作品作者吴宇航
                                terminal.insert('end','\n接收输入失败。','red')#本作品作者吴宇航
                                contiune_command()#本作品作者吴宇航
                        else:#本作品作者吴宇航
                            terminal.insert('end',command)#每次都复述一遍#本作品作者吴宇航
                            terminal.insert('end','\n没有等于号或等于号位置错误。','red')#本作品作者吴宇航
                            contiune_command()#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        terminal.insert('end',command)#本作品作者吴宇航
                        terminal.insert('end','\n'+errortext,'red')#本作品作者吴宇航
                        contiune_command()#本作品作者吴宇航
                elif len(command.strip())>=4:#本作品作者吴宇航
                    if command.lower().strip()[0:6]=='sysout':#本作品作者吴宇航
                        terminal.insert('end',command)#本作品作者吴宇航
                        if len(command.strip())>4:#本作品作者吴宇航
                            try:#本作品作者吴宇航
                                resultprint=eval('''['''+command[5:]+']',terminal_infos.running_space)#本作品作者吴宇航
                            except NameError:#本作品作者吴宇航
                                terminal.insert('end','\n变量不存在。','red')#本作品作者吴宇航
                                resultprint=['']#本作品作者吴宇航
                            except SyntaxError:#本作品作者吴宇航
                                terminal.insert('end','\n语法错误，请使用","或"+"连接。','red')#本作品作者吴宇航
                                resultprint=['']#本作品作者吴宇航
                            except:#本作品作者吴宇航
                                terminal.insert('end','\nERROR。','red')#本作品作者吴宇航
                                resultprint=['']#本作品作者吴宇航
                            try:#本作品作者吴宇航
                                terminal.insert('end','\n')#本作品作者吴宇航
                                for temp in resultprint:#本作品作者吴宇航
                                    terminal.insert('end',temp)#本作品作者吴宇航
                            except:#本作品作者吴宇航
                                terminal.insert('end','输出了个寂寞。')#本作品作者吴宇航
                        elif command.lower().strip()=='sysout':#本作品作者吴宇航
                            terminal.insert('end',command)#本作品作者吴宇航
                            pass#本作品作者吴宇航
                        else:#本作品作者吴宇航
                            terminal.insert('end',command)#本作品作者吴宇航
                            terminal.insert('end','\n'+errortext)#本作品作者吴宇航
                        contiune_command()#本作品作者吴宇航
                    elif len(command.strip())>=5:#本作品作者吴宇航
                        if command.lower().strip()[0:5]=='sysin':#本作品作者吴宇航
                            #让用户输入文本#本作品作者吴宇航
                            terminal.delete('end')#本作品作者吴宇航
                            if len(command.lower().strip())>5:#本作品作者吴宇航
                                if '=' in command[4:]:#本作品作者吴宇航
                                    try:#本作品作者吴宇航
                                        def tovar(varname,varvalue):#本作品作者吴宇航
                                            try:#本作品作者吴宇航
                                                exec(varname+'="'+varvalue.replace('"','\\"')+'"',terminal_infos.running_space)#本作品作者吴宇航
                                            except:#本作品作者吴宇航
                                                #from traceback import format_exc#本作品作者吴宇航
                                                #terminal.insert('end','\n接收输入失败。\n%s'%format_exc(),'red')#本作品作者吴宇航
                                                terminal.insert('end','\n接收输入失败。','red')#本作品作者吴宇航
                                            commandinput.bind('<Return>',lambda v=0:run_command(command_input.get(),TerminalText,command_input))#本作品作者吴宇航
                                            terminal['state']='n'#本作品作者吴宇航
                                            terminal.insert('end',commandinput.get())#本作品作者吴宇航
                                            commandinput.delete(0,'end')#本作品作者吴宇航
                                            terminal.insert('end','\n')#本作品作者吴宇航
                                            terminal.insert('end',f'\n')#本作品作者吴宇航
                                            terminal.insert('end',f'{os.getcwd()}::','green')#本作品作者吴宇航
                                            terminal.insert('end',f'\n')#本作品作者吴宇航
                                            terminal.insert('end',f'$ ')#本作品作者吴宇航
                                            terminal.window_create('end',window=commandinput)#本作品作者吴宇航
                                            commandinput.focus_set()#本作品作者吴宇航
                                            terminal.see('end')#本作品作者吴宇航
                                            terminal['state']='d'#本作品作者吴宇航
                                        terminal.insert('end',command)#本作品作者吴宇航
                                        terminal.insert('end','\n%s\n'%(command[command.index('=',0)+1:]),'cyan')#本作品作者吴宇航
                                        terminal.insert('end',f'$ ')#本作品作者吴宇航
                                        terminal.window_create('end',window=commandinput)#本作品作者吴宇航
                                        commandinput.bind("<Return>",lambda v=0:tovar(command[command.index(' ',0)+1:command.index('=',0)],commandinput.get()))#本作品作者吴宇航
                                    except:#本作品作者吴宇航
                                        terminal.insert('end','\n接收输入失败。','red')#本作品作者吴宇航
                                        contiune_command()#本作品作者吴宇航
                                else:#本作品作者吴宇航
                                    terminal.insert('end',command)#本作品作者吴宇航
                                    terminal.insert('end','\n没有等于号或等于号位置错误。','red')#本作品作者吴宇航
                                    contiune_command()#本作品作者吴宇航
                            elif command.lower().strip()=='input':#本作品作者吴宇航
                                terminal.insert('end',command)#本作品作者吴宇航
                                terminal.insert('end','\n')#本作品作者吴宇航
                                contiune_command()#本作品作者吴宇航
                            else:#本作品作者吴宇航
                                terminal.insert('end',command)#本作品作者吴宇航
                                terminal.insert('end','\n'+errortext,'red')#本作品作者吴宇航
                                contiune_command()#本作品作者吴宇航
                        else:#本作品作者吴宇航
                            terminal.insert('end',command)#本作品作者吴宇航
                            terminal.insert('end','\n'+errortext,'red')#本作品作者吴宇航
                            contiune_command()#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        terminal.insert('end',command)#本作品作者吴宇航
                        terminal.insert('end','\n'+errortext,'red')#本作品作者吴宇航
                        contiune_command()#本作品作者吴宇航
                else:#本作品作者吴宇航
                    terminal.insert('end',command)#本作品作者吴宇航
                    terminal.insert('end','\n'+errortext,'red')#本作品作者吴宇航
                    contiune_command()#本作品作者吴宇航
            else:#本作品作者吴宇航
                terminal.insert('end',command)#本作品作者吴宇航
                terminal.insert('end','\n'+errortext,'red')#本作品作者吴宇航
                contiune_command()#本作品作者吴宇航
        else:#本作品作者吴宇航
            terminal.insert('end',command)#本作品作者吴宇航
            terminal.insert('end','\n'+errortext,'red')#本作品作者吴宇航
            contiune_command()#本作品作者吴宇航
    #本作品作者吴宇航
        terminal.config(state='d')#本作品作者吴宇航
        terminal.see('end')#本作品作者吴宇航
    def post_inputlist(inputen):#本作品作者吴宇航
        #弹出效果展示中的命令列表#本作品作者吴宇航
        def setit(setmessage):#本作品作者吴宇航
            inputen.delete(0,'end')#本作品作者吴宇航
            inputen.insert('end',setmessage)#本作品作者吴宇航
            postwin.destroy()#本作品作者吴宇航
        postwin=tk.Toplevel(root,bg='#ffffff')#本作品作者吴宇航
        icon_for_window(postwin,'')#本作品作者吴宇航
        postwin.title('CommandList')#本作品作者吴宇航
        postwin.geometry('300x200')#本作品作者吴宇航
        postwin.transient(root)#本作品作者吴宇航
    #本作品作者吴宇航
        commandlist=tk.Listbox(postwin,fg='#800080',selectforeground='white',selectbackground='#800080',font=('terminal',16))#本作品作者吴宇航
        #绑定确定命令的按键#本作品作者吴宇航
        commandlist.bind('<Return>',lambda v=0:setit(commandlist.get(commandlist.curselection())))#本作品作者吴宇航
        commandlist.bind('<Right>',lambda v=0:setit(commandlist.get(commandlist.curselection())))#本作品作者吴宇航
        commandlist.bind('<Left>',lambda v=0:setit(commandlist.get(commandlist.curselection())))#本作品作者吴宇航
        #让Listbox最大占据postwin的控件#本作品作者吴宇航
        commandlist.pack(fill='both',expand=1)#本作品作者吴宇航
    #本作品作者吴宇航
        #给Listbox插入已经输入的内容#本作品作者吴宇航
        for temp in terminal_infos.input_list:#本作品作者吴宇航
            commandlist.insert('end',f'{temp}')#本作品作者吴宇航
    #本作品作者吴宇航
    #创建窗口#本作品作者吴宇航
    root=tk.Tk()#本作品作者吴宇航
    root.attributes('-alpha',0.8)#本作品作者吴宇航
    #设置标题#本作品作者吴宇航
    root.title(f'EasyTerminal {terminal_infos.version}')#本作品作者吴宇航
    #设置图标(用这个方法是为了防止打包后找不到图标的)#本作品作者吴宇航
    # icon_for_window(root,'')#本作品作者吴宇航
    #设置默认大小#本作品作者吴宇航
    root.geometry('645x400')#本作品作者吴宇航
    #让窗口不可改变大小#本作品作者吴宇航
    root.resizable(False,False)#本作品作者吴宇航
    #本作品作者吴宇航
    #新建Text控件#本作品作者吴宇航
    TerminalText=tk.ScrolledText(root,state='d',fg='white',bg='black',insertbackground='white',font=('consolas',13),selectforeground='black',selectbackground='white',takefocus=False)#本作品作者吴宇航
    TerminalText.pack(fill='both',expand='yes')#本作品作者吴宇航
    #本作品作者吴宇航
    #实现不同颜色的效果，用于insert插入标记#本作品作者吴宇航
    TerminalText.tag_config('red',foreground='red',selectforeground='#00ffff',selectbackground='#ffffff')#本作品作者吴宇航
    TerminalText.tag_config('green',foreground='green',selectforeground='#ff7eff',selectbackground='#ffffff')#本作品作者吴宇航
    TerminalText.tag_config('blue',foreground='blue',selectforeground='#ffff7e',selectbackground='#ffffff')#本作品作者吴宇航
    TerminalText.tag_config('cyan',foreground='cyan',selectforeground='red',selectbackground='#ffffff')#本作品作者吴宇航
    #本作品作者吴宇航
    TerminalText['state']='n'#本作品作者吴宇航
    TerminalText.insert('end',f'EasyTerminal {terminal_infos.version} By {terminal_infos.by}\n')#本作品作者吴宇航
    #本作品作者吴宇航
    #后面的'green'就是tag标记，他会应用green这个tag的属性#本作品作者吴宇航
    TerminalText.insert('end',f'{os.getcwd()}\n','green')#本作品作者吴宇航
    TerminalText.insert('end',f'$ ')#本作品作者吴宇航
    #本作品作者吴宇航
    #命令输入框#本作品作者吴宇航
    command_input=tk.Entry(TerminalText,font=('consolas',13),fg='white',bg='black',insertbackground='white',selectforeground='black',selectbackground='white',relief='flat',width=66)#本作品作者吴宇航
    command_input.bind('<Return>',lambda v=0:run_command(command_input.get(),TerminalText,command_input))#本作品作者吴宇航
    #在命令输入框中按F7弹出命令列表窗口#本作品作者吴宇航
    command_input.bind('<F7>',lambda v=0:post_inputlist(command_input))#本作品作者吴宇航
    #本作品作者吴宇航
    #插入命令输入框#本作品作者吴宇航
    TerminalText.window_create('end',window=command_input)#本作品作者吴宇航
    #本作品作者吴宇航
    #让终端Text不可编辑#本作品作者吴宇航
    TerminalText['state']='d'#本作品作者吴宇航
    #本作品作者吴宇航
    #循环窗口#本作品作者吴宇航
    root.mainloop()#本作品作者吴宇航
#本作品作者吴宇航
#我的世界#本作品作者吴宇航
import sys#本作品作者吴宇航
import math#本作品作者吴宇航
import random#本作品作者吴宇航
import time#本作品作者吴宇航
#本作品作者吴宇航
from collections import deque#本作品作者吴宇航
from pyglet import image#本作品作者吴宇航
from pyglet.gl import *#本作品作者吴宇航
from pyglet.graphics import TextureGroup#本作品作者吴宇航
from pyglet.window import key, mouse#本作品作者吴宇航
#本作品作者吴宇航
import random as rand #本作品作者吴宇航
import math#本作品作者吴宇航
def mink():#本作品作者吴宇航
    class NoiseParameters:#本作品作者吴宇航
        def __init__(self, octaves, amplitude, smoothness, roughness, heightOffset):#本作品作者吴宇航
            self.octaves = octaves#本作品作者吴宇航
            self.amplitude = amplitude#本作品作者吴宇航
            self.smoothness = smoothness#本作品作者吴宇航
            self.roughness = roughness#本作品作者吴宇航
            self.heightOffset = heightOffset#本作品作者吴宇航
    #本作品作者吴宇航
    class NoiseGen:#本作品作者吴宇航
        def __init__(self, seed):#本作品作者吴宇航
            self.seed = seed#本作品作者吴宇航
            self.noiseParams = NoiseParameters(#本作品作者吴宇航
                7, 50, 450, 0.3, 20#本作品作者吴宇航
            )#本作品作者吴宇航
    #本作品作者吴宇航
        def _getNoise2(self, n):#本作品作者吴宇航
            n += self.seed #本作品作者吴宇航
            n = (int(n) << 13) ^ int(n)#本作品作者吴宇航
            newn = (n * (n * n * 60493 + 19990303) + 1376312589) & 0x7fffffff#本作品作者吴宇航
            return 1.0 - (float(newn) / 1073741824.0)#本作品作者吴宇航
    #本作品作者吴宇航
        def _getNoise(self, x, z):#本作品作者吴宇航
            return self._getNoise2(x + z * 57)#本作品作者吴宇航
    #本作品作者吴宇航
        def _lerp(self, a, b, z):#本作品作者吴宇航
            mu2 = (1.0 - math.cos(z * 3.14)) / 2.0#本作品作者吴宇航
            return (a * (1 - mu2) + b * mu2)#本作品作者吴宇航
    #本作品作者吴宇航
        def _noise(self, x, z):#本作品作者吴宇航
            floorX = float(int(x))#本作品作者吴宇航
            floorZ = float(int(z))#本作品作者吴宇航
    #本作品作者吴宇航
            s = 0.0,#本作品作者吴宇航
            t = 0.0,#本作品作者吴宇航
            u = 0.0,#本作品作者吴宇航
            v = 0.0;#Integer declaration#本作品作者吴宇航
    #本作品作者吴宇航
            s = self._getNoise(floorX,      floorZ)#本作品作者吴宇航
            t = self._getNoise(floorX + 1,  floorZ)#本作品作者吴宇航
            u = self._getNoise(floorX,      floorZ + 1)#本作品作者吴宇航
            v = self._getNoise(floorX + 1,  floorZ + 1)#本作品作者吴宇航
    #本作品作者吴宇航
            rec1 = self._lerp(s, t, x - floorX)#本作品作者吴宇航
            rec2 = self._lerp(u, v, x - floorX)#本作品作者吴宇航
            rec3 = self._lerp(rec1, rec2, z - floorZ)#本作品作者吴宇航
            return rec3#本作品作者吴宇航
    #本作品作者吴宇航
        def getHeight(self, x, z):#本作品作者吴宇航
            totalValue = 0.0#本作品作者吴宇航
    #本作品作者吴宇航
            for a in range(self.noiseParams.octaves - 1):#本作品作者吴宇航
                freq = math.pow(2.0, a)#本作品作者吴宇航
                amp  = math.pow(self.noiseParams.roughness, a)#本作品作者吴宇航
                totalValue += self._noise(#本作品作者吴宇航
                    (float(x)) * freq / self.noiseParams.smoothness,#本作品作者吴宇航
                    (float(z)) * freq / self.noiseParams.smoothness#本作品作者吴宇航
                ) * self.noiseParams.amplitude#本作品作者吴宇航
    #本作品作者吴宇航
            result = (((totalValue / 2.1) + 1.2) * self.noiseParams.amplitude) + self.noiseParams.heightOffset#本作品作者吴宇航
    #本作品作者吴宇航
            return (totalValue / 5) + self.noiseParams.heightOffset#本作品作者吴宇航
    #本作品作者吴宇航
    #本作品作者吴宇航
    TICKS_PER_SEC = 60#本作品作者吴宇航
    #本作品作者吴宇航
    # Size of sectors used to ease block loading.#本作品作者吴宇航
    SECTOR_SIZE = 16#本作品作者吴宇航
    #本作品作者吴宇航
    # Movement variables#本作品作者吴宇航
    WALKING_SPEED = 5#本作品作者吴宇航
    FLYING_SPEED = 15#本作品作者吴宇航
    CROUCH_SPEED = 2#本作品作者吴宇航
    SPRINT_SPEED = 7#本作品作者吴宇航
    SPRINT_FOV = SPRINT_SPEED / 2#本作品作者吴宇航
    #本作品作者吴宇航
    GRAVITY = 20.0#本作品作者吴宇航
    MAX_JUMP_HEIGHT = 1.0 # About the height of a block.#本作品作者吴宇航
    # To derive the formula for calculating jump speed, first solve#本作品作者吴宇航
    #    v_t = v_0 + a * t#本作品作者吴宇航
    # for the time at which you achieve maximum height, where a is the acceleration#本作品作者吴宇航
    # due to gravity and v_t = 0. This gives:#本作品作者吴宇航
    #    t = - v_0 / a#本作品作者吴宇航
    # Use t and the desired MAX_JUMP_HEIGHT to solve for v_0 (jump speed) in#本作品作者吴宇航
    #    s = s_0 + v_0 * t + (a * t^2) / 2#本作品作者吴宇航
    JUMP_SPEED = math.sqrt(2 * GRAVITY * MAX_JUMP_HEIGHT)#本作品作者吴宇航
    TERMINAL_VELOCITY = 50#本作品作者吴宇航
    #本作品作者吴宇航
    # Player variables#本作品作者吴宇航
    PLAYER_HEIGHT = 2#本作品作者吴宇航
    PLAYER_FOV = 80.0#本作品作者吴宇航
    #本作品作者吴宇航
    if sys.version_info[0] >= 3:#本作品作者吴宇航
        xrange = range#本作品作者吴宇航
    #本作品作者吴宇航
    def cube_vertices(x, y, z, n):#本作品作者吴宇航
        """ Return the vertices of the cube at position x, y, z with size 2*n.#本作品作者吴宇航
    #本作品作者吴宇航
        """#本作品作者吴宇航
        return [#本作品作者吴宇航
            x-n,y+n,z-n, x-n,y+n,z+n, x+n,y+n,z+n, x+n,y+n,z-n,  # top#本作品作者吴宇航
            x-n,y-n,z-n, x+n,y-n,z-n, x+n,y-n,z+n, x-n,y-n,z+n,  # bottom#本作品作者吴宇航
            x-n,y-n,z-n, x-n,y-n,z+n, x-n,y+n,z+n, x-n,y+n,z-n,  # left#本作品作者吴宇航
            x+n,y-n,z+n, x+n,y-n,z-n, x+n,y+n,z-n, x+n,y+n,z+n,  # right#本作品作者吴宇航
            x-n,y-n,z+n, x+n,y-n,z+n, x+n,y+n,z+n, x-n,y+n,z+n,  # front#本作品作者吴宇航
            x+n,y-n,z-n, x-n,y-n,z-n, x-n,y+n,z-n, x+n,y+n,z-n,  # back#本作品作者吴宇航
        ]#本作品作者吴宇航
    #本作品作者吴宇航
    #本作品作者吴宇航
    def tex_coord(x, y, n=4):#本作品作者吴宇航
        """ Return the bounding vertices of the texture square.#本作品作者吴宇航
    #本作品作者吴宇航
        """#本作品作者吴宇航
        m = 1.0 / n#本作品作者吴宇航
        dx = x * m#本作品作者吴宇航
        dy = y * m#本作品作者吴宇航
        return dx, dy, dx + m, dy, dx + m, dy + m, dx, dy + m#本作品作者吴宇航
    #本作品作者吴宇航
    #本作品作者吴宇航
    def tex_coords(top, bottom, side):#本作品作者吴宇航
        """ Return a list of the texture squares for the top, bottom and side.#本作品作者吴宇航
    #本作品作者吴宇航
        """#本作品作者吴宇航
        top = tex_coord(*top)#本作品作者吴宇航
        bottom = tex_coord(*bottom)#本作品作者吴宇航
        side = tex_coord(*side)#本作品作者吴宇航
        result = []#本作品作者吴宇航
        result.extend(top)#本作品作者吴宇航
        result.extend(bottom)#本作品作者吴宇航
        result.extend(side * 4)#本作品作者吴宇航
        return result#本作品作者吴宇航
    #本作品作者吴宇航
    #本作品作者吴宇航
    TEXTURE_PATH = 'texture.png'#本作品作者吴宇航
    #本作品作者吴宇航
    GRASS = tex_coords((1, 0), (0, 1), (0, 0))#本作品作者吴宇航
    SAND = tex_coords((1, 1), (1, 1), (1, 1))#本作品作者吴宇航
    BRICK = tex_coords((2, 0), (2, 0), (2, 0))#本作品作者吴宇航
    STONE = tex_coords((2, 1), (2, 1), (2, 1))#本作品作者吴宇航
    WOOD = tex_coords((3, 1), (3, 1), (3, 1))#本作品作者吴宇航
    LEAF = tex_coords((3, 0), (3, 0), (3, 0))#本作品作者吴宇航
    WATER = tex_coords((0, 2), (0, 2), (0, 2))#本作品作者吴宇航
    #本作品作者吴宇航
    FACES = [#本作品作者吴宇航
        ( 0, 1, 0),#本作品作者吴宇航
        ( 0,-1, 0),#本作品作者吴宇航
        (-1, 0, 0),#本作品作者吴宇航
        ( 1, 0, 0),#本作品作者吴宇航
        ( 0, 0, 1),#本作品作者吴宇航
        ( 0, 0,-1),#本作品作者吴宇航
    ]#本作品作者吴宇航
    #本作品作者吴宇航
    #本作品作者吴宇航
    def normalize(position):#本作品作者吴宇航
        """ Accepts `position` of arbitrary precision and returns the block#本作品作者吴宇航
        containing that position.#本作品作者吴宇航
    #本作品作者吴宇航
        Parameters#本作品作者吴宇航
        ----------#本作品作者吴宇航
        position : tuple of len 3#本作品作者吴宇航
    #本作品作者吴宇航
        Returns#本作品作者吴宇航
        -------#本作品作者吴宇航
        block_position : tuple of ints of len 3#本作品作者吴宇航
    #本作品作者吴宇航
        """#本作品作者吴宇航
        x, y, z = position#本作品作者吴宇航
        x, y, z = (int(round(x)), int(round(y)), int(round(z)))#本作品作者吴宇航
        return (x, y, z)#本作品作者吴宇航
    #本作品作者吴宇航
    #本作品作者吴宇航
    def sectorize(position):#本作品作者吴宇航
        """ Returns a tuple representing the sector for the given `position`.#本作品作者吴宇航
    #本作品作者吴宇航
        Parameters#本作品作者吴宇航
        ----------#本作品作者吴宇航
        position : tuple of len 3#本作品作者吴宇航
    #本作品作者吴宇航
        Returns#本作品作者吴宇航
        -------#本作品作者吴宇航
        sector : tuple of len 3#本作品作者吴宇航
    #本作品作者吴宇航
        """#本作品作者吴宇航
        x, y, z = normalize(position)#本作品作者吴宇航
        x, y, z = x // SECTOR_SIZE, y // SECTOR_SIZE, z // SECTOR_SIZE#本作品作者吴宇航
        return (x, 0, z)#本作品作者吴宇航
    #本作品作者吴宇航
    #本作品作者吴宇航
    class Model(object):#本作品作者吴宇航
    #本作品作者吴宇航
        def __init__(self):#本作品作者吴宇航
    #本作品作者吴宇航
            # A Batch is a collection of vertex lists for batched rendering.#本作品作者吴宇航
            self.batch = pyglet.graphics.Batch()#本作品作者吴宇航
    #本作品作者吴宇航
            # A TextureGroup manages an OpenGL texture.#本作品作者吴宇航
            self.group = TextureGroup(image.load(TEXTURE_PATH).get_texture())#本作品作者吴宇航
    #本作品作者吴宇航
            # A mapping from position to the texture of the block at that position.#本作品作者吴宇航
            # This defines all the blocks that are currently in the world.#本作品作者吴宇航
            self.world = {}#本作品作者吴宇航
    #本作品作者吴宇航
            # Same mapping as `world` but only contains blocks that are shown.#本作品作者吴宇航
            self.shown = {}#本作品作者吴宇航
    #本作品作者吴宇航
            # Mapping from position to a pyglet `VertextList` for all shown blocks.#本作品作者吴宇航
            self._shown = {}#本作品作者吴宇航
    #本作品作者吴宇航
            # Mapping from sector to a list of positions inside that sector.#本作品作者吴宇航
            self.sectors = {}#本作品作者吴宇航
    #本作品作者吴宇航
            # Simple function queue implementation. The queue is populated with#本作品作者吴宇航
            # _show_block() and _hide_block() calls#本作品作者吴宇航
            self.queue = deque()#本作品作者吴宇航
    #本作品作者吴宇航
            self._initialize()#本作品作者吴宇航
    #本作品作者吴宇航
        def _initialize(self):#本作品作者吴宇航
            """ Initialize the world by placing all the blocks.#本作品作者吴宇航
    #本作品作者吴宇航
            """#本作品作者吴宇航
            gen = NoiseGen(452692)#本作品作者吴宇航
    #本作品作者吴宇航
            n = 128 #size of the world#本作品作者吴宇航
            s = 1  # step size#本作品作者吴宇航
            y = 0  # initial y height#本作品作者吴宇航
            #本作品作者吴宇航
            #too lazy to do this properly lol#本作品作者吴宇航
            heightMap = []#本作品作者吴宇航
            for x in xrange(0, n, s):#本作品作者吴宇航
                for z in xrange(0, n, s):#本作品作者吴宇航
                    heightMap.append(0)#本作品作者吴宇航
            for x in xrange(0, n, s):#本作品作者吴宇航
                for z in xrange(0, n, s):#本作品作者吴宇航
                    heightMap[z + x * n] = int(gen.getHeight(x, z))#本作品作者吴宇航
    #本作品作者吴宇航
            #Generate the world#本作品作者吴宇航
            for x in xrange(0, n, s):#本作品作者吴宇航
                for z in xrange(0, n, s):#本作品作者吴宇航
                    h = heightMap[z + x * n]#本作品作者吴宇航
                    if (h < 15):#本作品作者吴宇航
                        self.add_block((x, h, z), SAND, immediate=False)#本作品作者吴宇航
                        for y in range (h, 15):#本作品作者吴宇航
                            self.add_block((x, y, z), WATER, immediate=False)#本作品作者吴宇航
                        continue#本作品作者吴宇航
                    if (h < 18):#本作品作者吴宇航
                        self.add_block((x, h, z), SAND, immediate=False)#本作品作者吴宇航
                    self.add_block((x, h, z), GRASS, immediate=False)#本作品作者吴宇航
                    for y in xrange(h - 1, 0, -1):#本作品作者吴宇航
                        self.add_block((x, y, z), STONE, immediate=False)#本作品作者吴宇航
                    #Maybe add tree at this (x, z)#本作品作者吴宇航
                    if (h > 20):#本作品作者吴宇航
                        if random.randrange(0, 1000) > 990:#本作品作者吴宇航
                            treeHeight = random.randrange(5, 7)#本作品作者吴宇航
                            #Tree trunk#本作品作者吴宇航
                            for y in xrange(h + 1, h + treeHeight):#本作品作者吴宇航
                                self.add_block((x, y, z), WOOD, immediate=False)#本作品作者吴宇航
                            #Tree leaves#本作品作者吴宇航
                            leafh = h + treeHeight#本作品作者吴宇航
                            for lz in xrange(z + -2, z + 3):#本作品作者吴宇航
                                for lx in xrange(x + -2, x + 3): #本作品作者吴宇航
                                    for ly in xrange(3):#本作品作者吴宇航
                                        self.add_block((lx, leafh + ly, lz), LEAF, immediate=False)#本作品作者吴宇航
    #本作品作者吴宇航
        def hit_test(self, position, vector, max_distance=8):#本作品作者吴宇航
            """ Line of sight search from current position. If a block is#本作品作者吴宇航
            intersected it is returned, along with the block previously in the line#本作品作者吴宇航
            of sight. If no block is found, return None, None.#本作品作者吴宇航
    #本作品作者吴宇航
            Parameters#本作品作者吴宇航
            ----------#本作品作者吴宇航
            position : tuple of len 3#本作品作者吴宇航
                The (x, y, z) position to check visibility from.#本作品作者吴宇航
            vector : tuple of len 3#本作品作者吴宇航
                The line of sight vector.#本作品作者吴宇航
            max_distance : int#本作品作者吴宇航
                How many blocks away to search for a hit.#本作品作者吴宇航
    #本作品作者吴宇航
            """#本作品作者吴宇航
            m = 8#本作品作者吴宇航
            x, y, z = position#本作品作者吴宇航
            dx, dy, dz = vector#本作品作者吴宇航
            previous = None#本作品作者吴宇航
            for _ in xrange(max_distance * m):#本作品作者吴宇航
                key = normalize((x, y, z))#本作品作者吴宇航
                if key != previous and key in self.world:#本作品作者吴宇航
                    return key, previous#本作品作者吴宇航
                previous = key#本作品作者吴宇航
                x, y, z = x + dx / m, y + dy / m, z + dz / m#本作品作者吴宇航
            return None, None#本作品作者吴宇航
    #本作品作者吴宇航
        def exposed(self, position):#本作品作者吴宇航
            """ Returns False is given `position` is surrounded on all 6 sides by#本作品作者吴宇航
            blocks, True otherwise.#本作品作者吴宇航
    #本作品作者吴宇航
            """#本作品作者吴宇航
            x, y, z = position#本作品作者吴宇航
            for dx, dy, dz in FACES:#本作品作者吴宇航
                if (x + dx, y + dy, z + dz) not in self.world:#本作品作者吴宇航
                    return True#本作品作者吴宇航
            return False#本作品作者吴宇航
    #本作品作者吴宇航
        def add_block(self, position, texture, immediate=True):#本作品作者吴宇航
            """ Add a block with the given `texture` and `position` to the world.#本作品作者吴宇航
    #本作品作者吴宇航
            Parameters#本作品作者吴宇航
            ----------#本作品作者吴宇航
            position : tuple of len 3#本作品作者吴宇航
                The (x, y, z) position of the block to add.#本作品作者吴宇航
            texture : list of len 3#本作品作者吴宇航
                The coordinates of the texture squares. Use `tex_coords()` to#本作品作者吴宇航
                generate.#本作品作者吴宇航
            immediate : bool#本作品作者吴宇航
                Whether or not to draw the block immediately.#本作品作者吴宇航
    #本作品作者吴宇航
            """#本作品作者吴宇航
            if position in self.world:#本作品作者吴宇航
                self.remove_block(position, immediate)#本作品作者吴宇航
            self.world[position] = texture#本作品作者吴宇航
            self.sectors.setdefault(sectorize(position), []).append(position)#本作品作者吴宇航
            if immediate:#本作品作者吴宇航
                if self.exposed(position):#本作品作者吴宇航
                    self.show_block(position)#本作品作者吴宇航
                self.check_neighbors(position)#本作品作者吴宇航
    #本作品作者吴宇航
        def remove_block(self, position, immediate=True):#本作品作者吴宇航
            """ Remove the block at the given `position`.#本作品作者吴宇航
    #本作品作者吴宇航
            Parameters#本作品作者吴宇航
            ----------#本作品作者吴宇航
            position : tuple of len 3#本作品作者吴宇航
                The (x, y, z) position of the block to remove.#本作品作者吴宇航
            immediate : bool#本作品作者吴宇航
                Whether or not to immediately remove block from canvas.#本作品作者吴宇航
    #本作品作者吴宇航
            """#本作品作者吴宇航
            del self.world[position]#本作品作者吴宇航
            self.sectors[sectorize(position)].remove(position)#本作品作者吴宇航
            if immediate:#本作品作者吴宇航
                if position in self.shown:#本作品作者吴宇航
                    self.hide_block(position)#本作品作者吴宇航
                self.check_neighbors(position)#本作品作者吴宇航
    #本作品作者吴宇航
        def check_neighbors(self, position):#本作品作者吴宇航
            """ Check all blocks surrounding `position` and ensure their visual#本作品作者吴宇航
            state is current. This means hiding blocks that are not exposed and#本作品作者吴宇航
            ensuring that all exposed blocks are shown. Usually used after a block#本作品作者吴宇航
            is added or removed.#本作品作者吴宇航
    #本作品作者吴宇航
            """#本作品作者吴宇航
            x, y, z = position#本作品作者吴宇航
            for dx, dy, dz in FACES:#本作品作者吴宇航
                key = (x + dx, y + dy, z + dz)#本作品作者吴宇航
                if key not in self.world:#本作品作者吴宇航
                    continue#本作品作者吴宇航
                if self.exposed(key):#本作品作者吴宇航
                    if key not in self.shown:#本作品作者吴宇航
                        self.show_block(key)#本作品作者吴宇航
                else:#本作品作者吴宇航
                    if key in self.shown:#本作品作者吴宇航
                        self.hide_block(key)#本作品作者吴宇航
    #本作品作者吴宇航
        def show_block(self, position, immediate=True):#本作品作者吴宇航
            """ Show the block at the given `position`. This method assumes the#本作品作者吴宇航
            block has already been added with add_block()#本作品作者吴宇航
    #本作品作者吴宇航
            Parameters#本作品作者吴宇航
            ----------#本作品作者吴宇航
            position : tuple of len 3#本作品作者吴宇航
                The (x, y, z) position of the block to show.#本作品作者吴宇航
            immediate : bool#本作品作者吴宇航
                Whether or not to show the block immediately.#本作品作者吴宇航
    #本作品作者吴宇航
            """#本作品作者吴宇航
            texture = self.world[position]#本作品作者吴宇航
            self.shown[position] = texture#本作品作者吴宇航
            if immediate:#本作品作者吴宇航
                self._show_block(position, texture)#本作品作者吴宇航
            else:#本作品作者吴宇航
                self._enqueue(self._show_block, position, texture)#本作品作者吴宇航
    #本作品作者吴宇航
        def _show_block(self, position, texture):#本作品作者吴宇航
            """ Private implementation of the `show_block()` method.#本作品作者吴宇航
    #本作品作者吴宇航
            Parameters#本作品作者吴宇航
            ----------#本作品作者吴宇航
            position : tuple of len 3#本作品作者吴宇航
                The (x, y, z) position of the block to show.#本作品作者吴宇航
            texture : list of len 3#本作品作者吴宇航
                The coordinates of the texture squares. Use `tex_coords()` to#本作品作者吴宇航
                generate.#本作品作者吴宇航
    #本作品作者吴宇航
            """#本作品作者吴宇航
            x, y, z = position#本作品作者吴宇航
            vertex_data = cube_vertices(x, y, z, 0.5)#本作品作者吴宇航
            texture_data = list(texture)#本作品作者吴宇航
            # create vertex list#本作品作者吴宇航
            # FIXME Maybe `add_indexed()` should be used instead#本作品作者吴宇航
            self._shown[position] = self.batch.add(24, GL_QUADS, self.group,#本作品作者吴宇航
                ('v3f/static', vertex_data),#本作品作者吴宇航
                ('t2f/static', texture_data))#本作品作者吴宇航
    #本作品作者吴宇航
        def hide_block(self, position, immediate=True):#本作品作者吴宇航
            """ Hide the block at the given `position`. Hiding does not remove the#本作品作者吴宇航
            block from the world.#本作品作者吴宇航
    #本作品作者吴宇航
            Parameters#本作品作者吴宇航
            ----------#本作品作者吴宇航
            position : tuple of len 3#本作品作者吴宇航
                The (x, y, z) position of the block to hide.#本作品作者吴宇航
            immediate : bool#本作品作者吴宇航
                Whether or not to immediately remove the block from the canvas.#本作品作者吴宇航
    #本作品作者吴宇航
            """#本作品作者吴宇航
            self.shown.pop(position)#本作品作者吴宇航
            if immediate:#本作品作者吴宇航
                self._hide_block(position)#本作品作者吴宇航
            else:#本作品作者吴宇航
                self._enqueue(self._hide_block, position)#本作品作者吴宇航
    #本作品作者吴宇航
        def _hide_block(self, position):#本作品作者吴宇航
            """ Private implementation of the 'hide_block()` method.#本作品作者吴宇航
    #本作品作者吴宇航
            """#本作品作者吴宇航
            self._shown.pop(position).delete()#本作品作者吴宇航
    #本作品作者吴宇航
        def show_sector(self, sector):#本作品作者吴宇航
            """ Ensure all blocks in the given sector that should be shown are#本作品作者吴宇航
            drawn to the canvas.#本作品作者吴宇航
    #本作品作者吴宇航
            """#本作品作者吴宇航
            for position in self.sectors.get(sector, []):#本作品作者吴宇航
                if position not in self.shown and self.exposed(position):#本作品作者吴宇航
                    self.show_block(position, False)#本作品作者吴宇航
    #本作品作者吴宇航
        def hide_sector(self, sector):#本作品作者吴宇航
            """ Ensure all blocks in the given sector that should be hidden are#本作品作者吴宇航
            removed from the canvas.#本作品作者吴宇航
    #本作品作者吴宇航
            """#本作品作者吴宇航
            for position in self.sectors.get(sector, []):#本作品作者吴宇航
                if position in self.shown:#本作品作者吴宇航
                    self.hide_block(position, False)#本作品作者吴宇航
    #本作品作者吴宇航
        def change_sectors(self, before, after):#本作品作者吴宇航
            """ Move from sector `before` to sector `after`. A sector is a#本作品作者吴宇航
            contiguous x, y sub-region of world. Sectors are used to speed up#本作品作者吴宇航
            world rendering.#本作品作者吴宇航
    #本作品作者吴宇航
            """#本作品作者吴宇航
            before_set = set()#本作品作者吴宇航
            after_set = set()#本作品作者吴宇航
            pad = 4#本作品作者吴宇航
            for dx in xrange(-pad, pad + 1):#本作品作者吴宇航
                for dy in [0]:  # xrange(-pad, pad + 1):#本作品作者吴宇航
                    for dz in xrange(-pad, pad + 1):#本作品作者吴宇航
                        if dx ** 2 + dy ** 2 + dz ** 2 > (pad + 1) ** 2:#本作品作者吴宇航
                            continue#本作品作者吴宇航
                        if before:#本作品作者吴宇航
                            x, y, z = before#本作品作者吴宇航
                            before_set.add((x + dx, y + dy, z + dz))#本作品作者吴宇航
                        if after:#本作品作者吴宇航
                            x, y, z = after#本作品作者吴宇航
                            after_set.add((x + dx, y + dy, z + dz))#本作品作者吴宇航
            show = after_set - before_set#本作品作者吴宇航
            hide = before_set - after_set#本作品作者吴宇航
            for sector in show:#本作品作者吴宇航
                self.show_sector(sector)#本作品作者吴宇航
            for sector in hide:#本作品作者吴宇航
                self.hide_sector(sector)#本作品作者吴宇航
    #本作品作者吴宇航
        def _enqueue(self, func, *args):#本作品作者吴宇航
            """ Add `func` to the internal queue.#本作品作者吴宇航
    #本作品作者吴宇航
            """#本作品作者吴宇航
            self.queue.append((func, args))#本作品作者吴宇航
    #本作品作者吴宇航
        def _dequeue(self):#本作品作者吴宇航
            """ Pop the top function from the internal queue and call it.#本作品作者吴宇航
    #本作品作者吴宇航
            """#本作品作者吴宇航
            func, args = self.queue.popleft()#本作品作者吴宇航
            func(*args)#本作品作者吴宇航
    #本作品作者吴宇航
        def process_queue(self):#本作品作者吴宇航
            """ Process the entire queue while taking periodic breaks. This allows#本作品作者吴宇航
            the game loop to run smoothly. The queue contains calls to#本作品作者吴宇航
            _show_block() and _hide_block() so this method should be called if#本作品作者吴宇航
            add_block() or remove_block() was called with immediate=False#本作品作者吴宇航
    #本作品作者吴宇航
            """#本作品作者吴宇航
            start = time.process_time()#本作品作者吴宇航
            while self.queue and time.process_time() - start < 1.0 / TICKS_PER_SEC:#本作品作者吴宇航
                self._dequeue()#本作品作者吴宇航
    #本作品作者吴宇航
        def process_entire_queue(self):#本作品作者吴宇航
            """ Process the entire queue with no breaks.#本作品作者吴宇航
    #本作品作者吴宇航
            """#本作品作者吴宇航
            while self.queue:#本作品作者吴宇航
                self._dequeue()#本作品作者吴宇航
    #本作品作者吴宇航
    #本作品作者吴宇航
    class Window(pyglet.window.Window):#本作品作者吴宇航
    #本作品作者吴宇航
        def __init__(self, *args, **kwargs):#本作品作者吴宇航
            super(Window, self).__init__(*args, **kwargs)#本作品作者吴宇航
    #本作品作者吴宇航
            # Whether or not the window exclusively captures the mouse.#本作品作者吴宇航
            self.exclusive = False#本作品作者吴宇航
    #本作品作者吴宇航
            # When flying gravity has no effect and speed is increased.#本作品作者吴宇航
            self.flying = False#本作品作者吴宇航
    #本作品作者吴宇航
            # Used for constant jumping. If the space bar is held down,#本作品作者吴宇航
            # this is true, otherwise, it's false#本作品作者吴宇航
            self.jumping = False#本作品作者吴宇航
    #本作品作者吴宇航
            # If the player actually jumped, this is true#本作品作者吴宇航
            self.jumped = False#本作品作者吴宇航
    #本作品作者吴宇航
            # If this is true, a crouch offset is added to the final glTranslate#本作品作者吴宇航
            self.crouch = False#本作品作者吴宇航
    #本作品作者吴宇航
            # Player sprint#本作品作者吴宇航
            self.sprinting = False#本作品作者吴宇航
    #本作品作者吴宇航
            # This is an offset value so stuff like speed potions can also be easily added#本作品作者吴宇航
            self.fov_offset = 0#本作品作者吴宇航
    #本作品作者吴宇航
            self.collision_types = {"top": False, "bottom": False, "right": False, "left": False}#本作品作者吴宇航
    #本作品作者吴宇航
            # Strafing is moving lateral to the direction you are facing,#本作品作者吴宇航
            # e.g. moving to the left or right while continuing to face forward.#本作品作者吴宇航
            ##本作品作者吴宇航
            # First element is -1 when moving forward, 1 when moving back, and 0#本作品作者吴宇航
            # otherwise. The second element is -1 when moving left, 1 when moving#本作品作者吴宇航
            # right, and 0 otherwise.#本作品作者吴宇航
            self.strafe = [0, 0]#本作品作者吴宇航
    #本作品作者吴宇航
            # Current (x, y, z) position in the world, specified with floats. Note#本作品作者吴宇航
            # that, perhaps unlike in math class, the y-axis is the vertical axis.#本作品作者吴宇航
            self.position = (30, 50, 80)#本作品作者吴宇航
    #本作品作者吴宇航
            # First element is rotation of the player in the x-z plane (ground#本作品作者吴宇航
            # plane) measured from the z-axis down. The second is the rotation#本作品作者吴宇航
            # angle from the ground plane up. Rotation is in degrees.#本作品作者吴宇航
            ##本作品作者吴宇航
            # The vertical plane rotation ranges from -90 (looking straight down) to#本作品作者吴宇航
            # 90 (looking straight up). The horizontal rotation range is unbounded.#本作品作者吴宇航
            self.rotation = (0, 0)#本作品作者吴宇航
    #本作品作者吴宇航
            # Which sector the player is currently in.#本作品作者吴宇航
            self.sector = None#本作品作者吴宇航
    #本作品作者吴宇航
            # The crosshairs at the center of the screen.#本作品作者吴宇航
            self.reticle = None#本作品作者吴宇航
    #本作品作者吴宇航
            # Velocity in the y (upward) direction.#本作品作者吴宇航
            self.dy = 0#本作品作者吴宇航
    #本作品作者吴宇航
            # A list of blocks the player can place. Hit num keys to cycle.#本作品作者吴宇航
            self.inventory = [BRICK, GRASS, SAND, WOOD, LEAF]#本作品作者吴宇航
    #本作品作者吴宇航
            # The current block the user can place. Hit num keys to cycle.#本作品作者吴宇航
            self.block = self.inventory[0]#本作品作者吴宇航
    #本作品作者吴宇航
            # Convenience list of num keys.#本作品作者吴宇航
            self.num_keys = [#本作品作者吴宇航
                key._1, key._2, key._3, key._4, key._5,#本作品作者吴宇航
                key._6, key._7, key._8, key._9, key._0]#本作品作者吴宇航
    #本作品作者吴宇航
            # Instance of the model that handles the world.#本作品作者吴宇航
            self.model = Model()#本作品作者吴宇航
    #本作品作者吴宇航
            # The label that is displayed in the top left of the canvas.#本作品作者吴宇航
            self.label = pyglet.text.Label('', font_name='Arial', font_size=18,#本作品作者吴宇航
                x=10, y=self.height - 10, anchor_x='left', anchor_y='top',#本作品作者吴宇航
                color=(0, 0, 0, 255))#本作品作者吴宇航
    #本作品作者吴宇航
            # This call schedules the `update()` method to be called#本作品作者吴宇航
            # TICKS_PER_SEC. This is the main game event loop.#本作品作者吴宇航
            pyglet.clock.schedule_interval(self.update, 1.0 / TICKS_PER_SEC)#本作品作者吴宇航
    #本作品作者吴宇航
        def set_exclusive_mouse(self, exclusive):#本作品作者吴宇航
            """ If `exclusive` is True, the game will capture the mouse, if False#本作品作者吴宇航
            the game will ignore the mouse.#本作品作者吴宇航
    #本作品作者吴宇航
            """#本作品作者吴宇航
            super(Window, self).set_exclusive_mouse(exclusive)#本作品作者吴宇航
            self.exclusive = exclusive#本作品作者吴宇航
    #本作品作者吴宇航
        def get_sight_vector(self):#本作品作者吴宇航
            """ Returns the current line of sight vector indicating the direction#本作品作者吴宇航
            the player is looking.#本作品作者吴宇航
    #本作品作者吴宇航
            """#本作品作者吴宇航
            x, y = self.rotation#本作品作者吴宇航
            # y ranges from -90 to 90, or -pi/2 to pi/2, so m ranges from 0 to 1 and#本作品作者吴宇航
            # is 1 when looking ahead parallel to the ground and 0 when looking#本作品作者吴宇航
            # straight up or down.#本作品作者吴宇航
            m = math.cos(math.radians(y))#本作品作者吴宇航
            # dy ranges from -1 to 1 and is -1 when looking straight down and 1 when#本作品作者吴宇航
            # looking straight up.#本作品作者吴宇航
            dy = math.sin(math.radians(y))#本作品作者吴宇航
            dx = math.cos(math.radians(x - 90)) * m#本作品作者吴宇航
            dz = math.sin(math.radians(x - 90)) * m#本作品作者吴宇航
            return (dx, dy, dz)#本作品作者吴宇航
    #本作品作者吴宇航
        def get_motion_vector(self):#本作品作者吴宇航
            """ Returns the current motion vector indicating the velocity of the#本作品作者吴宇航
            player.#本作品作者吴宇航
    #本作品作者吴宇航
            Returns#本作品作者吴宇航
            -------#本作品作者吴宇航
            vector : tuple of len 3#本作品作者吴宇航
                Tuple containing the velocity in x, y, and z respectively.#本作品作者吴宇航
    #本作品作者吴宇航
            """#本作品作者吴宇航
            if any(self.strafe):#本作品作者吴宇航
                x, y = self.rotation#本作品作者吴宇航
                strafe = math.degrees(math.atan2(*self.strafe))#本作品作者吴宇航
                y_angle = math.radians(y)#本作品作者吴宇航
                x_angle = math.radians(x + strafe)#本作品作者吴宇航
                if self.flying:#本作品作者吴宇航
                    m = math.cos(y_angle)#本作品作者吴宇航
                    dy = math.sin(y_angle)#本作品作者吴宇航
                    if self.strafe[1]:#本作品作者吴宇航
                        # Moving left or right.#本作品作者吴宇航
                        dy = 0.0#本作品作者吴宇航
                        m = 1#本作品作者吴宇航
                    if self.strafe[0] > 0:#本作品作者吴宇航
                        # Moving backwards.#本作品作者吴宇航
                        dy *= -1#本作品作者吴宇航
                    # When you are flying up or down, you have less left and right#本作品作者吴宇航
                    # motion.#本作品作者吴宇航
                    dx = math.cos(x_angle) * m#本作品作者吴宇航
                    dz = math.sin(x_angle) * m#本作品作者吴宇航
                else:#本作品作者吴宇航
                    dy = 0.0#本作品作者吴宇航
                    dx = math.cos(x_angle)#本作品作者吴宇航
                    dz = math.sin(x_angle)#本作品作者吴宇航
            else:#本作品作者吴宇航
                dy = 0.0#本作品作者吴宇航
                dx = 0.0#本作品作者吴宇航
                dz = 0.0#本作品作者吴宇航
            return (dx, dy, dz)#本作品作者吴宇航
    #本作品作者吴宇航
        def update(self, dt):#本作品作者吴宇航
            """ This method is scheduled to be called repeatedly by the pyglet#本作品作者吴宇航
            clock.#本作品作者吴宇航
    #本作品作者吴宇航
            Parameters#本作品作者吴宇航
            ----------#本作品作者吴宇航
            dt : float#本作品作者吴宇航
                The change in time since the last call.#本作品作者吴宇航
    #本作品作者吴宇航
            """#本作品作者吴宇航
            self.model.process_queue()#本作品作者吴宇航
            sector = sectorize(self.position)#本作品作者吴宇航
            if sector != self.sector:#本作品作者吴宇航
                self.model.change_sectors(self.sector, sector)#本作品作者吴宇航
                if self.sector is None:#本作品作者吴宇航
                    self.model.process_entire_queue()#本作品作者吴宇航
                self.sector = sector#本作品作者吴宇航
            m = 8#本作品作者吴宇航
            dt = min(dt, 0.2)#本作品作者吴宇航
            for _ in xrange(m):#本作品作者吴宇航
                self._update(dt / m)#本作品作者吴宇航
    #本作品作者吴宇航
        def _update(self, dt):#本作品作者吴宇航
            """ Private implementation of the `update()` method. This is where most#本作品作者吴宇航
            of the motion logic lives, along with gravity and collision detection.#本作品作者吴宇航
    #本作品作者吴宇航
            Parameters#本作品作者吴宇航
            ----------#本作品作者吴宇航
            dt : float#本作品作者吴宇航
                The change in time since the last call.#本作品作者吴宇航
    #本作品作者吴宇航
            """#本作品作者吴宇航
            # walking#本作品作者吴宇航
            if self.flying:#本作品作者吴宇航
                speed = FLYING_SPEED#本作品作者吴宇航
            elif self.sprinting:#本作品作者吴宇航
                speed = SPRINT_SPEED#本作品作者吴宇航
            elif self.crouch:#本作品作者吴宇航
                speed = CROUCH_SPEED#本作品作者吴宇航
            else:#本作品作者吴宇航
                speed = WALKING_SPEED#本作品作者吴宇航
    #本作品作者吴宇航
            if self.jumping:#本作品作者吴宇航
                if self.collision_types["top"]:#本作品作者吴宇航
                    self.dy = JUMP_SPEED#本作品作者吴宇航
                    self.jumped = True#本作品作者吴宇航
            else:#本作品作者吴宇航
                if self.collision_types["top"]:#本作品作者吴宇航
                    self.jumped = False#本作品作者吴宇航
            if self.jumped:#本作品作者吴宇航
                speed += 0.7#本作品作者吴宇航
    #本作品作者吴宇航
            d = dt * speed # distance covered this tick.#本作品作者吴宇航
            dx, dy, dz = self.get_motion_vector()#本作品作者吴宇航
            # New position in space, before accounting for gravity.#本作品作者吴宇航
            dx, dy, dz = dx * d, dy * d, dz * d#本作品作者吴宇航
            # gravity#本作品作者吴宇航
            if not self.flying:#本作品作者吴宇航
                # Update your vertical speed: if you are falling, speed up until you#本作品作者吴宇航
                # hit terminal velocity; if you are jumping, slow down until you#本作品作者吴宇航
                # start falling.#本作品作者吴宇航
                self.dy -= dt * GRAVITY#本作品作者吴宇航
                self.dy = max(self.dy, -TERMINAL_VELOCITY)#本作品作者吴宇航
                dy += self.dy * dt#本作品作者吴宇航
            # collisions#本作品作者吴宇航
            old_pos = self.position#本作品作者吴宇航
            x, y, z = old_pos#本作品作者吴宇航
            x, y, z = self.collide((x + dx, y + dy, z + dz), PLAYER_HEIGHT)#本作品作者吴宇航
            self.position = (x, y, z)#本作品作者吴宇航
    #本作品作者吴宇航
            # Sptinting stuff. If the player stops moving in the x and z direction, the player stops sprinting#本作品作者吴宇航
            # and the sprint fov is subtracted from the fov offset#本作品作者吴宇航
            if old_pos[0]-self.position[0] == 0 and old_pos[2]-self.position[2] == 0:#本作品作者吴宇航
                disablefov = False#本作品作者吴宇航
                if self.sprinting:#本作品作者吴宇航
                    disablefov = True#本作品作者吴宇航
                self.sprinting = False#本作品作者吴宇航
                if disablefov:#本作品作者吴宇航
                    self.fov_offset -= SPRINT_FOV#本作品作者吴宇航
    #本作品作者吴宇航
        def collide(self, position, height):#本作品作者吴宇航
            """ Checks to see if the player at the given `position` and `height`#本作品作者吴宇航
            is colliding with any blocks in the world.#本作品作者吴宇航
    #本作品作者吴宇航
            Parameters#本作品作者吴宇航
            ----------#本作品作者吴宇航
            position : tuple of len 3#本作品作者吴宇航
                The (x, y, z) position to check for collisions at.#本作品作者吴宇航
            height : int or float#本作品作者吴宇航
                The height of the player.#本作品作者吴宇航
    #本作品作者吴宇航
            Returns#本作品作者吴宇航
            -------#本作品作者吴宇航
            position : tuple of len 3#本作品作者吴宇航
                The new position of the player taking into account collisions.#本作品作者吴宇航
    #本作品作者吴宇航
            """#本作品作者吴宇航
            # How much overlap with a dimension of a surrounding block you need to#本作品作者吴宇航
            # have to count as a collision. If 0, touching terrain at all counts as#本作品作者吴宇航
            # a collision. If .49, you sink into the ground, as if walking through#本作品作者吴宇航
            # tall grass. If >= .5, you'll fall through the ground.#本作品作者吴宇航
            pad = 0.25#本作品作者吴宇航
            p = list(position)#本作品作者吴宇航
            np = normalize(position)#本作品作者吴宇航
            self.collision_types = {"top":False,"bottom":False,"right":False,"left":False}#本作品作者吴宇航
            for face in FACES:  # check all surrounding blocks#本作品作者吴宇航
                for i in xrange(3):  # check each dimension independently#本作品作者吴宇航
                    if not face[i]:#本作品作者吴宇航
                        continue#本作品作者吴宇航
                    # How much overlap you have with this dimension.#本作品作者吴宇航
                    d = (p[i] - np[i]) * face[i]#本作品作者吴宇航
                    if d < pad:#本作品作者吴宇航
                        continue#本作品作者吴宇航
                    for dy in xrange(height):  # check each height#本作品作者吴宇航
                        op = list(np)#本作品作者吴宇航
                        op[1] -= dy#本作品作者吴宇航
                        op[i] += face[i]#本作品作者吴宇航
                        if tuple(op) not in self.model.world:#本作品作者吴宇航
                            continue#本作品作者吴宇航
                        p[i] -= (d - pad) * face[i]#本作品作者吴宇航
                        # If you are colliding with the ground or ceiling, stop#本作品作者吴宇航
                        # falling / rising.#本作品作者吴宇航
                        if face == (0, -1, 0):#本作品作者吴宇航
                            self.collision_types["top"] = True#本作品作者吴宇航
                            self.dy = 0#本作品作者吴宇航
                        if face == (0, 1, 0):#本作品作者吴宇航
                            self.collision_types["bottom"] = True#本作品作者吴宇航
                            self.dy = 0#本作品作者吴宇航
                        break#本作品作者吴宇航
            return tuple(p)#本作品作者吴宇航
    #本作品作者吴宇航
        def on_mouse_press(self, x, y, button, modifiers):#本作品作者吴宇航
            """ Called when a mouse button is pressed. See pyglet docs for button#本作品作者吴宇航
            amd modifier mappings.#本作品作者吴宇航
    #本作品作者吴宇航
            Parameters#本作品作者吴宇航
            ----------#本作品作者吴宇航
            x, y : int#本作品作者吴宇航
                The coordinates of the mouse click. Always center of the screen if#本作品作者吴宇航
                the mouse is captured.#本作品作者吴宇航
            button : int#本作品作者吴宇航
                Number representing mouse button that was clicked. 1 = left button,#本作品作者吴宇航
                4 = right button.#本作品作者吴宇航
            modifiers : int#本作品作者吴宇航
                Number representing any modifying keys that were pressed when the#本作品作者吴宇航
                mouse button was clicked.#本作品作者吴宇航
    #本作品作者吴宇航
            """#本作品作者吴宇航
            if self.exclusive:#本作品作者吴宇航
                vector = self.get_sight_vector()#本作品作者吴宇航
                block, previous = self.model.hit_test(self.position, vector)#本作品作者吴宇航
                if (button == mouse.RIGHT) or \
                        ((button == mouse.LEFT) and (modifiers & key.MOD_CTRL)):#本作品作者吴宇航
                    # ON OSX, control + left click = right click.#本作品作者吴宇航
                    if previous:#本作品作者吴宇航
                        self.model.add_block(previous, self.block)#本作品作者吴宇航
                elif button == pyglet.window.mouse.LEFT and block:#本作品作者吴宇航
                    texture = self.model.world[block]#本作品作者吴宇航
                    if texture != STONE:#本作品作者吴宇航
                        self.model.remove_block(block)#本作品作者吴宇航
            else:#本作品作者吴宇航
                self.set_exclusive_mouse(True)#本作品作者吴宇航
    #本作品作者吴宇航
        def on_mouse_motion(self, x, y, dx, dy):#本作品作者吴宇航
            """ Called when the player moves the mouse.#本作品作者吴宇航
    #本作品作者吴宇航
            Parameters#本作品作者吴宇航
            ----------#本作品作者吴宇航
            x, y : int#本作品作者吴宇航
                The coordinates of the mouse click. Always center of the screen if#本作品作者吴宇航
                the mouse is captured.#本作品作者吴宇航
            dx, dy : float#本作品作者吴宇航
                The movement of the mouse.#本作品作者吴宇航
    #本作品作者吴宇航
            """#本作品作者吴宇航
            if self.exclusive:#本作品作者吴宇航
                m = 0.15#本作品作者吴宇航
                x, y = self.rotation#本作品作者吴宇航
                x, y = x + dx * m, y + dy * m#本作品作者吴宇航
                y = max(-90, min(90, y))#本作品作者吴宇航
                self.rotation = (x, y)#本作品作者吴宇航
    #本作品作者吴宇航
        def on_key_press(self, symbol, modifiers):#本作品作者吴宇航
            """ Called when the player presses a key. See pyglet docs for key#本作品作者吴宇航
            mappings.#本作品作者吴宇航
    #本作品作者吴宇航
            Parameters#本作品作者吴宇航
            ----------#本作品作者吴宇航
            symbol : int#本作品作者吴宇航
                Number representing the key that was pressed.#本作品作者吴宇航
            modifiers : int#本作品作者吴宇航
                Number representing any modifying keys that were pressed.#本作品作者吴宇航
    #本作品作者吴宇航
            """#本作品作者吴宇航
            if symbol == key.W:#本作品作者吴宇航
                self.strafe[0] -= 1#本作品作者吴宇航
            elif symbol == key.S:#本作品作者吴宇航
                self.strafe[0] += 1#本作品作者吴宇航
            elif symbol == key.A:#本作品作者吴宇航
                self.strafe[1] -= 1#本作品作者吴宇航
            elif symbol == key.D:#本作品作者吴宇航
                self.strafe[1] += 1#本作品作者吴宇航
            elif symbol == key.C:#本作品作者吴宇航
                self.fov_offset -= 60.0#本作品作者吴宇航
            elif symbol == key.SPACE:#本作品作者吴宇航
                self.jumping = True#本作品作者吴宇航
            elif symbol == key.ESCAPE:#本作品作者吴宇航
                self.set_exclusive_mouse(False)#本作品作者吴宇航
            elif symbol == key.LSHIFT:#本作品作者吴宇航
                self.crouch = True#本作品作者吴宇航
                if self.sprinting:#本作品作者吴宇航
                    self.fov_offset -= SPRINT_FOV#本作品作者吴宇航
                    self.sprinting = False#本作品作者吴宇航
            elif symbol == key.R:#本作品作者吴宇航
                if not self.crouch:#本作品作者吴宇航
                    if not self.sprinting:#本作品作者吴宇航
                        self.fov_offset += SPRINT_FOV#本作品作者吴宇航
                    self.sprinting = True#本作品作者吴宇航
            elif symbol == key.TAB:#本作品作者吴宇航
                self.flying = not self.flying#本作品作者吴宇航
            elif symbol in self.num_keys:#本作品作者吴宇航
                index = (symbol - self.num_keys[0]) % len(self.inventory)#本作品作者吴宇航
                self.block = self.inventory[index]#本作品作者吴宇航
    #本作品作者吴宇航
        def on_key_release(self, symbol, modifiers):#本作品作者吴宇航
            """ Called when the player releases a key. See pyglet docs for key#本作品作者吴宇航
            mappings.#本作品作者吴宇航
    #本作品作者吴宇航
            Parameters#本作品作者吴宇航
            ----------#本作品作者吴宇航
            symbol : int#本作品作者吴宇航
                Number representing the key that was pressed.#本作品作者吴宇航
            modifiers : int#本作品作者吴宇航
                Number representing any modifying keys that were pressed.#本作品作者吴宇航
    #本作品作者吴宇航
            """#本作品作者吴宇航
            if symbol == key.W:#本作品作者吴宇航
                self.strafe[0] += 1#本作品作者吴宇航
            elif symbol == key.S:#本作品作者吴宇航
                self.strafe[0] -= 1#本作品作者吴宇航
            elif symbol == key.A:#本作品作者吴宇航
                self.strafe[1] += 1#本作品作者吴宇航
            elif symbol == key.D:#本作品作者吴宇航
                self.strafe[1] -= 1#本作品作者吴宇航
            elif symbol == key.SPACE:#本作品作者吴宇航
                self.jumping = False#本作品作者吴宇航
            elif symbol == key.LSHIFT:#本作品作者吴宇航
                self.crouch = False#本作品作者吴宇航
            elif symbol == key.C:#本作品作者吴宇航
                self.fov_offset += 60.0#本作品作者吴宇航
    #本作品作者吴宇航
        def on_resize(self, width, height):#本作品作者吴宇航
            """ Called when the window is resized to a new `width` and `height`.#本作品作者吴宇航
    #本作品作者吴宇航
            """#本作品作者吴宇航
            # label#本作品作者吴宇航
            self.label.y = height - 10#本作品作者吴宇航
            # reticle#本作品作者吴宇航
            if self.reticle:#本作品作者吴宇航
                self.reticle.delete()#本作品作者吴宇航
            x, y = self.width // 2, self.height // 2#本作品作者吴宇航
            n = 10#本作品作者吴宇航
            self.reticle = pyglet.graphics.vertex_list(4,#本作品作者吴宇航
                ('v2i', (x - n, y, x + n, y, x, y - n, x, y + n))#本作品作者吴宇航
            )#本作品作者吴宇航
    #本作品作者吴宇航
        def set_2d(self):#本作品作者吴宇航
            """ Configure OpenGL to draw in 2d.#本作品作者吴宇航
    #本作品作者吴宇航
            """#本作品作者吴宇航
            width, height = self.get_size()#本作品作者吴宇航
            glDisable(GL_DEPTH_TEST)#本作品作者吴宇航
            viewport = self.get_viewport_size()#本作品作者吴宇航
            glViewport(0, 0, max(1, viewport[0]), max(1, viewport[1]))#本作品作者吴宇航
            glMatrixMode(GL_PROJECTION)#本作品作者吴宇航
            glLoadIdentity()#本作品作者吴宇航
            glOrtho(0, max(1, width), 0, max(1, height), -1, 1)#本作品作者吴宇航
            glMatrixMode(GL_MODELVIEW)#本作品作者吴宇航
            glLoadIdentity()#本作品作者吴宇航
    #本作品作者吴宇航
        def set_3d(self):#本作品作者吴宇航
            """ Configure OpenGL to draw in 3d.#本作品作者吴宇航
    #本作品作者吴宇航
            """#本作品作者吴宇航
            width, height = self.get_size()#本作品作者吴宇航
            glEnable(GL_DEPTH_TEST)#本作品作者吴宇航
            viewport = self.get_viewport_size()#本作品作者吴宇航
            glViewport(0, 0, max(1, viewport[0]), max(1, viewport[1]))#本作品作者吴宇航
            glMatrixMode(GL_PROJECTION)#本作品作者吴宇航
            glLoadIdentity()#本作品作者吴宇航
            gluPerspective(PLAYER_FOV + self.fov_offset, width / float(height), 0.1, 60.0)#本作品作者吴宇航
            glMatrixMode(GL_MODELVIEW)#本作品作者吴宇航
            glLoadIdentity()#本作品作者吴宇航
            x, y = self.rotation#本作品作者吴宇航
            glRotatef(x, 0, 1, 0)#本作品作者吴宇航
            glRotatef(-y, math.cos(math.radians(x)), 0, math.sin(math.radians(x)))#本作品作者吴宇航
            x, y, z = self.position#本作品作者吴宇航
            if self.crouch:#本作品作者吴宇航
                glTranslatef(-x, -y+0.2, -z)#本作品作者吴宇航
            else:#本作品作者吴宇航
                glTranslatef(-x, -y, -z)#本作品作者吴宇航
    #本作品作者吴宇航
        def on_draw(self):#本作品作者吴宇航
            """ Called by pyglet to draw the canvas.#本作品作者吴宇航
    #本作品作者吴宇航
            """#本作品作者吴宇航
            self.clear()#本作品作者吴宇航
            self.set_3d()#本作品作者吴宇航
            glColor3d(1, 1, 1)#本作品作者吴宇航
            self.model.batch.draw()#本作品作者吴宇航
            self.draw_focused_block()#本作品作者吴宇航
            self.set_2d()#本作品作者吴宇航
            self.draw_label()#本作品作者吴宇航
            self.draw_reticle()#本作品作者吴宇航
    #本作品作者吴宇航
        def draw_focused_block(self):#本作品作者吴宇航
            """ Draw black edges around the block that is currently under the#本作品作者吴宇航
            crosshairs.#本作品作者吴宇航
    #本作品作者吴宇航
            """#本作品作者吴宇航
            vector = self.get_sight_vector()#本作品作者吴宇航
            block = self.model.hit_test(self.position, vector)[0]#本作品作者吴宇航
            if block:#本作品作者吴宇航
                x, y, z = block#本作品作者吴宇航
                vertex_data = cube_vertices(x, y, z, 0.51)#本作品作者吴宇航
                glColor3d(0, 0, 0)#本作品作者吴宇航
                glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)#本作品作者吴宇航
                pyglet.graphics.draw(24, GL_QUADS, ('v3f/static', vertex_data))#本作品作者吴宇航
                glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)#本作品作者吴宇航
    #本作品作者吴宇航
        def draw_label(self):#本作品作者吴宇航
            """ Draw the label in the top left of the screen.#本作品作者吴宇航
    #本作品作者吴宇航
            """#本作品作者吴宇航
            x, y, z = self.position#本作品作者吴宇航
            self.label.text = '%02d (%.2f, %.2f, %.2f) %d / %d' % (#本作品作者吴宇航
                pyglet.clock.get_fps(), x, y, z,#本作品作者吴宇航
                len(self.model._shown), len(self.model.world))#本作品作者吴宇航
            self.label.draw()#本作品作者吴宇航
    #本作品作者吴宇航
        def draw_reticle(self):#本作品作者吴宇航
            """ Draw the crosshairs in the center of the screen.#本作品作者吴宇航
    #本作品作者吴宇航
            """#本作品作者吴宇航
            glColor3d(0, 0, 0)#本作品作者吴宇航
            self.reticle.draw(GL_LINES)#本作品作者吴宇航
    #本作品作者吴宇航
    #本作品作者吴宇航
    def setup_fog():#本作品作者吴宇航
        """ Configure the OpenGL fog properties.#本作品作者吴宇航
    #本作品作者吴宇航
        """#本作品作者吴宇航
        # Enable fog. Fog "blends a fog color with each rasterized pixel fragment's#本作品作者吴宇航
        # post-texturing color."#本作品作者吴宇航
        glEnable(GL_FOG)#本作品作者吴宇航
        # Set the fog color.#本作品作者吴宇航
        glFogfv(GL_FOG_COLOR, (GLfloat * 4)(0.5, 0.69, 1.0, 1))#本作品作者吴宇航
        # Say we have no preference between rendering speed and quality.#本作品作者吴宇航
        glHint(GL_FOG_HINT, GL_DONT_CARE)#本作品作者吴宇航
        # Specify the equation used to compute the blending factor.#本作品作者吴宇航
        glFogi(GL_FOG_MODE, GL_LINEAR)#本作品作者吴宇航
        # How close and far away fog starts and ends. The closer the start and end,#本作品作者吴宇航
        # the denser the fog in the fog range.#本作品作者吴宇航
        glFogf(GL_FOG_START, 40.0)#本作品作者吴宇航
        glFogf(GL_FOG_END, 60.0)#本作品作者吴宇航
    #本作品作者吴宇航
    #本作品作者吴宇航
    def setup():#本作品作者吴宇航
        """ Basic OpenGL configuration.#本作品作者吴宇航
    #本作品作者吴宇航
        """#本作品作者吴宇航
        # Set the color of "clear", i.e. the sky, in rgba.#本作品作者吴宇航
        glClearColor(0.5, 0.69, 1.0, 1)#本作品作者吴宇航
        # Enable culling (not rendering) of back-facing facets -- facets that aren't#本作品作者吴宇航
        # visible to you.#本作品作者吴宇航
        glEnable(GL_CULL_FACE)#本作品作者吴宇航
        # Set the texture minification/magnification function to GL_NEAREST (nearest#本作品作者吴宇航
        # in Manhattan distance) to the specified texture coordinates. GL_NEAREST#本作品作者吴宇航
        # "is generally faster than GL_LINEAR, but it can produce textured images#本作品作者吴宇航
        # with sharper edges because the transition between texture elements is not#本作品作者吴宇航
        # as smooth."#本作品作者吴宇航
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)#本作品作者吴宇航
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)#本作品作者吴宇航
        setup_fog()#本作品作者吴宇航
    #本作品作者吴宇航
    #本作品作者吴宇航
    def main():#本作品作者吴宇航
        window = Window(width=1280, height=720, caption='Minecraft', resizable=True)#本作品作者吴宇航
        # Hide the mouse cursor and prevent the mouse from leaving the window.#本作品作者吴宇航
        window.set_exclusive_mouse(True)#本作品作者吴宇航
        setup()#本作品作者吴宇航
        pyglet.app.run()#本作品作者吴宇航
    #本作品作者吴宇航
    main()#本作品作者吴宇航
#本作品作者吴宇航
#飞机大战#本作品作者吴宇航
from Cython import *#本作品作者吴宇航
import wx#本作品作者吴宇航
def feiji():#本作品作者吴宇航
#本作品作者吴宇航
    SCREEN_WIDTH = 480#本作品作者吴宇航
    SCREEN_HEIGHT = 800#本作品作者吴宇航
    #本作品作者吴宇航
    class Bullet(pygame.sprite.Sprite):#本作品作者吴宇航
        def __init__(self, bullet_img, init_pos):#本作品作者吴宇航
            pygame.sprite.Sprite.__init__(self)#本作品作者吴宇航
            self.image = bullet_img#本作品作者吴宇航
            self.rect = self.image.get_rect()#本作品作者吴宇航
            self.rect.midbottom = init_pos#本作品作者吴宇航
            self.speed = 10#本作品作者吴宇航
    #本作品作者吴宇航
        def move(self):#本作品作者吴宇航
            self.rect.top -= self.speed#本作品作者吴宇航
    #本作品作者吴宇航
    class Player(pygame.sprite.Sprite):#本作品作者吴宇航
        def __init__(self, plane_img, player_rect, init_pos):#本作品作者吴宇航
            pygame.sprite.Sprite.__init__(self)#本作品作者吴宇航
            self.image = []                               #本作品作者吴宇航
            for i in range(len(player_rect)):#本作品作者吴宇航
                self.image.append(plane_img.subsurface(player_rect[i]).convert_alpha())#本作品作者吴宇航
            self.rect = player_rect[0]                #本作品作者吴宇航
            self.rect.topleft = init_pos             #本作品作者吴宇航
            self.speed = 8                               #本作品作者吴宇航
            self.bullets = pygame.sprite.Group()       #本作品作者吴宇航
            self.is_hit = False                            #本作品作者吴宇航
    #本作品作者吴宇航
        def moveDown(self):#本作品作者吴宇航
            if self.rect.top >= SCREEN_HEIGHT - self.rect.height:#本作品作者吴宇航
                self.rect.top = SCREEN_HEIGHT - self.rect.height#本作品作者吴宇航
            else:#本作品作者吴宇航
                self.rect.top += self.speed#本作品作者吴宇航
    #本作品作者吴宇航
        def moveLeft(self):#本作品作者吴宇航
            if self.rect.left <= 0:#本作品作者吴宇航
                self.rect.left = 0#本作品作者吴宇航
            else:#本作品作者吴宇航
                self.rect.left -= self.speed#本作品作者吴宇航
        def shoot(self, bullet_img):#本作品作者吴宇航
            bullet = Bullet(bullet_img, self.rect.midtop)#本作品作者吴宇航
            self.bullets.add(bullet)#本作品作者吴宇航
    #本作品作者吴宇航
        def moveUp(self):#本作品作者吴宇航
            if self.rect.top <= 0:#本作品作者吴宇航
                self.rect.top = 0#本作品作者吴宇航
            else:#本作品作者吴宇航
                self.rect.top -= self.speed#本作品作者吴宇航
    #本作品作者吴宇航
         #本作品作者吴宇航
        def moveRight(self):#本作品作者吴宇航
            if self.rect.left >= SCREEN_WIDTH - self.rect.width:#本作品作者吴宇航
                self.rect.left = SCREEN_WIDTH - self.rect.width#本作品作者吴宇航
            else:#本作品作者吴宇航
                self.rect.left += self.speed#本作品作者吴宇航
    #本作品作者吴宇航
    class Enemy(pygame.sprite.Sprite):#本作品作者吴宇航
        def __init__(self, enemy_img, enemy_down_imgs, init_pos):#本作品作者吴宇航
           pygame.sprite.Sprite.__init__(self)#本作品作者吴宇航
           self.image = enemy_img#本作品作者吴宇航
           self.rect = self.image.get_rect()#本作品作者吴宇航
           self.rect.topleft = init_pos#本作品作者吴宇航
           self.down_imgs = enemy_down_imgs#本作品作者吴宇航
           self.speed = 2#本作品作者吴宇航
    #本作品作者吴宇航
        def move(self):#本作品作者吴宇航
            self.rect.top += self.speed#本作品作者吴宇航
    #本作品作者吴宇航
    #本作品作者吴宇航
    pygame.init()#本作品作者吴宇航
    #本作品作者吴宇航
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))#本作品作者吴宇航
    #本作品作者吴宇航
    #本作品作者吴宇航
    pygame.display.set_caption('飞机大战')#本作品作者吴宇航
    background = pygame.image.load('background.png').convert()#本作品作者吴宇航
    game_over = pygame.image.load('gameover.png')#本作品作者吴宇航
    plane_img = pygame.image.load('shoot.png')#本作品作者吴宇航
    player_rect = []#本作品作者吴宇航
    player_rect.append(pygame.Rect(0, 99, 102, 126))      #本作品作者吴宇航
    player_rect.append(pygame.Rect(165, 234, 102, 126))     #本作品作者吴宇航
    #本作品作者吴宇航
    player_pos = [200, 600]#本作品作者吴宇航
    player = Player(plane_img, player_rect, player_pos)#本作品作者吴宇航
    #本作品作者吴宇航
    #本作品作者吴宇航
    bullet_rect = pygame.Rect(1004, 987, 9, 21)#本作品作者吴宇航
    bullet_img = plane_img.subsurface(bullet_rect)#本作品作者吴宇航
    #本作品作者吴宇航
    #本作品作者吴宇航
    enemy1_rect = pygame.Rect(534, 612, 57, 43)#本作品作者吴宇航
    enemy1_img = plane_img.subsurface(enemy1_rect)#本作品作者吴宇航
    enemy1_down_imgs = plane_img.subsurface(pygame.Rect(267, 347, 57, 43))#本作品作者吴宇航
    #本作品作者吴宇航
    #本作品作者吴宇航
    #本作品作者吴宇航
    enemies1 = pygame.sprite.Group()#本作品作者吴宇航
    #本作品作者吴宇航
    #本作品作者吴宇航
    enemies_down = pygame.sprite.Group()#本作品作者吴宇航
    #本作品作者吴宇航
    #本作品作者吴宇航
    shoot_frequency = 0#本作品作者吴宇航
    enemy_frequency = 0#本作品作者吴宇航
    #本作品作者吴宇航
    #本作品作者吴宇航
    score = 0#本作品作者吴宇航
    #本作品作者吴宇航
    #本作品作者吴宇航
    clock = pygame.time.Clock()#本作品作者吴宇航
    #本作品作者吴宇航
    #本作品作者吴宇航
    running = True#本作品作者吴宇航
    #本作品作者吴宇航
    #本作品作者吴宇航
    while running:#本作品作者吴宇航
    #本作品作者吴宇航
        clock.tick(60)#本作品作者吴宇航
    #本作品作者吴宇航
        if not player.is_hit:#本作品作者吴宇航
            if shoot_frequency % 15 == 0:#本作品作者吴宇航
                player.shoot(bullet_img)#本作品作者吴宇航
            shoot_frequency += 1#本作品作者吴宇航
            if shoot_frequency >= 15:#本作品作者吴宇航
                shoot_frequency = 0#本作品作者吴宇航
    #本作品作者吴宇航
    #本作品作者吴宇航
        if enemy_frequency % 50 == 0:#本作品作者吴宇航
            enemy1_pos = [randint(0, SCREEN_WIDTH - enemy1_rect.width), 0]#本作品作者吴宇航
            enemy1 = Enemy(enemy1_img, enemy1_down_imgs, enemy1_pos)#本作品作者吴宇航
            enemies1.add(enemy1)#本作品作者吴宇航
        enemy_frequency += 1#本作品作者吴宇航
        if enemy_frequency >= 100:#本作品作者吴宇航
            enemy_frequency = 0#本作品作者吴宇航
    #本作品作者吴宇航
        for bullet in player.bullets:#本作品作者吴宇航
            bullet.move()#本作品作者吴宇航
            if bullet.rect.bottom < 0:#本作品作者吴宇航
                player.bullets.remove(bullet)   #本作品作者吴宇航
    #本作品作者吴宇航
        for enemy in enemies1:#本作品作者吴宇航
            enemy.move()#本作品作者吴宇航
            if pygame.sprite.collide_circle(enemy, player):#本作品作者吴宇航
                enemies_down.add(enemy)#本作品作者吴宇航
                enemies1.remove(enemy)#本作品作者吴宇航
                player.is_hit = True#本作品作者吴宇航
                break#本作品作者吴宇航
            if enemy.rect.top < 0:#本作品作者吴宇航
                enemies1.remove(enemy)#本作品作者吴宇航
    #本作品作者吴宇航
        enemies1_down = pygame.sprite.groupcollide(enemies1, player.bullets, 1, 1)#本作品作者吴宇航
        for enemy_down in enemies1_down:#本作品作者吴宇航
            enemies_down.add(enemy_down)#本作品作者吴宇航
    #本作品作者吴宇航
        screen.fill(0)#本作品作者吴宇航
        screen.blit(background, (0, 0))#本作品作者吴宇航
    #本作品作者吴宇航
        if not player.is_hit:#本作品作者吴宇航
            screen.blit(player.image[0], player.rect)#本作品作者吴宇航
        else:#本作品作者吴宇航
            screen.blit(player.image[1], player.rect) #本作品作者吴宇航
            running = False#本作品作者吴宇航
    #本作品作者吴宇航
        for enemy_down in enemies_down:#本作品作者吴宇航
            enemies_down.remove(enemy_down)#本作品作者吴宇航
            score += 1#本作品作者吴宇航
            screen.blit(enemy_down.down_imgs, enemy_down.rect)#本作品作者吴宇航
    #本作品作者吴宇航
        player.bullets.draw(screen)#本作品作者吴宇航
        enemies1.draw(screen)#本作品作者吴宇航
    #本作品作者吴宇航
        score_font = pygame.font.Font(None, 36)#本作品作者吴宇航
        score_text = score_font.render('score: '+str(score), True, (128, 128, 128))#本作品作者吴宇航
        text_rect = score_text.get_rect()#本作品作者吴宇航
        text_rect.topleft = [10, 10]#本作品作者吴宇航
        screen.blit(score_text, text_rect)#本作品作者吴宇航
    #本作品作者吴宇航
        pygame.display.update()#本作品作者吴宇航
    #本作品作者吴宇航
        for event in pygame.event.get():#本作品作者吴宇航
            if event.type == pygame.QUIT:#本作品作者吴宇航
                pygame.quit()#本作品作者吴宇航
                exit()#本作品作者吴宇航
    #本作品作者吴宇航
        key_pressed = pygame.key.get_pressed()#本作品作者吴宇航
    #本作品作者吴宇航
        if key_pressed[K_w] or key_pressed[K_UP]:#本作品作者吴宇航
            player.moveUp()#本作品作者吴宇航
        if key_pressed[K_s] or key_pressed[K_DOWN]:#本作品作者吴宇航
            player.moveDown()#本作品作者吴宇航
        if key_pressed[K_a] or key_pressed[K_LEFT]:#本作品作者吴宇航
            player.moveLeft()#本作品作者吴宇航
        if key_pressed[K_d] or key_pressed[K_RIGHT]:#本作品作者吴宇航
            player.moveRight()#本作品作者吴宇航
    #本作品作者吴宇航
    font = pygame.font.Font(None, 64)#本作品作者吴宇航
    text = font.render('score: '+ str(score), True, (255, 0, 0))#本作品作者吴宇航
    text_rect = text.get_rect()#本作品作者吴宇航
    text_rect.centerx = screen.get_rect().centerx#本作品作者吴宇航
    text_rect.centery = screen.get_rect().centery + 24#本作品作者吴宇航
    screen.blit(game_over, (0, 0))#本作品作者吴宇航
    screen.blit(text, text_rect)#本作品作者吴宇航
    #本作品作者吴宇航
    while True:#本作品作者吴宇航
        for event in pygame.event.get():#本作品作者吴宇航
            if event.type == pygame.QUIT:#本作品作者吴宇航
                pygame.quit()#本作品作者吴宇航
                exit()#本作品作者吴宇航
        pygame.display.update()#本作品作者吴宇航
#本作品作者吴宇航
#超级玛丽#本作品作者吴宇航
import pygame as pg#本作品作者吴宇航
from source.main import main#本作品作者吴宇航
def mali():#本作品作者吴宇航
    main()#本作品作者吴宇航
    pg.quit()#本作品作者吴宇航
#本作品作者吴宇航
#2048游戏#本作品作者吴宇航
import tkinter#本作品作者吴宇航
from tkinter import *#本作品作者吴宇航
def erba():#本作品作者吴宇航
    _map_data = [#本作品作者吴宇航
        [0, 0, 0, 0],#本作品作者吴宇航
        [0, 0, 0, 0],#本作品作者吴宇航
        [0, 0, 0, 0],#本作品作者吴宇航
        [0, 0, 0, 0]#本作品作者吴宇航
    ]#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
    # -------------------------以下为2048游戏的基本算法---------------------------#本作品作者吴宇航
#本作品作者吴宇航
    # 重置#本作品作者吴宇航
    def reset():#本作品作者吴宇航
        '''重新设置游戏数据,将地图恢复为初始状态，并加入两个数据 2 作用初始状态'''#本作品作者吴宇航
        _map_data[:] = []  # _map_data.clear()#本作品作者吴宇航
        _map_data.append([0, 0, 0, 0])#本作品作者吴宇航
        _map_data.append([0, 0, 0, 0])#本作品作者吴宇航
        _map_data.append([0, 0, 0, 0])#本作品作者吴宇航
        _map_data.append([0, 0, 0, 0])#本作品作者吴宇航
        # 在空白地图上填充两个2#本作品作者吴宇航
        fill2()#本作品作者吴宇航
        fill2()#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
    # 获取 0 个数#本作品作者吴宇航
    def get_space_count():#本作品作者吴宇航
        """获取没有数字的方格的数量,如果数量为0则说有无法填充新数据，游戏即将结束#本作品作者吴宇航
        """#本作品作者吴宇航
        count = 0#本作品作者吴宇航
        for r in _map_data:#本作品作者吴宇航
            count += r.count(0)#本作品作者吴宇航
        return count#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
    # 计算分数#本作品作者吴宇航
    def get_score():#本作品作者吴宇航
        '''获取游戏的分数,得分规则是每次有两个数加在一起则生成相应的分数。#本作品作者吴宇航
        如 2 和 2 合并后得4分, 8 和 8 分并后得 16分.#本作品作者吴宇航
        根据一个大于2的数字就可以知道他共合并了多少次，可以直接算出分数:#本作品作者吴宇航
        如:#本作品作者吴宇航
           4 一定由两个2合并，得4分#本作品作者吴宇航
           8 一定由两个4合并,则计:8 + 4 + 4 得32分#本作品作者吴宇航
           ... 以此类推#本作品作者吴宇航
        '''#本作品作者吴宇航
        score = 0#本作品作者吴宇航
        for r in _map_data:#本作品作者吴宇航
            for c in r:#本作品作者吴宇航
                score += 0 if c < 4 else c * int((math.log(c, 2) - 1.0))#本作品作者吴宇航
        return score  # 导入数学模块#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
    # 随机数生成#本作品作者吴宇航
    def fill2():#本作品作者吴宇航
        '''填充2到空位置，如果填度成功返回True,如果已满，则返回False'''#本作品作者吴宇航
        blank_count = get_space_count()  # 得到地图上空白位置的个数#本作品作者吴宇航
        if 0 == blank_count:#本作品作者吴宇航
            return False#本作品作者吴宇航
        # 生成随机位置, 如，当只有四个空时，则生成0~3的数，代表自左至右，自上而下的空位置#本作品作者吴宇航
        pos = random.randrange(0, blank_count)#本作品作者吴宇航
        offset = 0#本作品作者吴宇航
        for row in _map_data:  # row为行row#本作品作者吴宇航
            for col in range(4):  # col 为列，column#本作品作者吴宇航
                if 0 == row[col]:#本作品作者吴宇航
                    if offset == pos:#本作品作者吴宇航
                        # 把2填充到第row行，第col列的位置，返回True#本作品作者吴宇航
                        row[col] = 2#本作品作者吴宇航
                        return True#本作品作者吴宇航
                    offset += 1#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
    # 结束判定#本作品作者吴宇航
    def is_gameover():#本作品作者吴宇航
        """判断游戏是否结束,如果结束返回True,否是返回False#本作品作者吴宇航
        """#本作品作者吴宇航
        for r in _map_data:#本作品作者吴宇航
            # 如果水平方向还有0,则游戏没有结束#本作品作者吴宇航
            if r.count(0):#本作品作者吴宇航
                return False#本作品作者吴宇航
            # 水平方向如果有两个相邻的元素相同，应当是可以合并的，则游戏没有结束#本作品作者吴宇航
            for i in range(3):#本作品作者吴宇航
                if r[i] == r[i + 1]:#本作品作者吴宇航
                    return False#本作品作者吴宇航
        for c in range(4):#本作品作者吴宇航
            # 竖直方向如果有两个相邻的元素相同，应当可以合并的，则游戏没有结束#本作品作者吴宇航
            for r in range(3):#本作品作者吴宇航
                if _map_data[r][c] == _map_data[r + 1][c]:#本作品作者吴宇航
                    return False#本作品作者吴宇航
        # 以上都没有，则游戏结束#本作品作者吴宇航
        return True#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
    # 移动合并分数#本作品作者吴宇航
    def _left_move_number(line):#本作品作者吴宇航
        '''左移一行数字,如果有数据移动则返回True，否则返回False:#本作品作者吴宇航
        如: line = [0, 2, 0, 8] 即表达如下一行:#本作品作者吴宇航
            +---+---+---+---+#本作品作者吴宇航
            | 0 | 2 | 0 | 8 |      <----向左移动#本作品作者吴宇航
            +---+---+---+---+#本作品作者吴宇航
        此行数据需要左移三次:#本作品作者吴宇航
          第一次左移结果:#本作品作者吴宇航
            +---+---+---+---+#本作品作者吴宇航
            | 2 | 0 | 8 | 0 |#本作品作者吴宇航
            +---+---+---+---+#本作品作者吴宇航
          第二次左移结果:#本作品作者吴宇航
            +---+---+---+---+#本作品作者吴宇航
            | 2 | 8 | 0 | 0 |#本作品作者吴宇航
            +---+---+---+---+#本作品作者吴宇航
          第三次左移结果:#本作品作者吴宇航
            +---+---+---+---+#本作品作者吴宇航
            | 2 | 8 | 0 | 0 |  # 因为最左则为2,所以8不动#本作品作者吴宇航
            +---+---+---+---+#本作品作者吴宇航
         最终结果: line = [4, 8, 0, 0]#本作品作者吴宇航
        '''#本作品作者吴宇航
        moveflag = False  # 是否移动的标识,先假设没有移动#本作品作者吴宇航
        for _ in range(3):  # 重复执行下面算法三次#本作品作者吴宇航
            for i in range(3):  # i为索引#本作品作者吴宇航
                if 0 == line[i]:  # 此处有空位，右侧相邻数字向左侧移动，右侧填空白#本作品作者吴宇航
                    moveflag = True#本作品作者吴宇航
                    line[i] = line[i + 1]#本作品作者吴宇航
                    line[i + 1] = 0#本作品作者吴宇航
        return moveflag#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
    # 移动位置#本作品作者吴宇航
    def _left_marge_number(line):#本作品作者吴宇航
        '''向左侧进行相同单元格合并,合并结果放在左侧,右侧补零#本作品作者吴宇航
        如: line = [2, 2, 4, 4] 即表达如下一行:#本作品作者吴宇航
            +---+---+---+---+#本作品作者吴宇航
            | 2 | 2 | 4 | 4 |#本作品作者吴宇航
            +---+---+---+---+#本作品作者吴宇航
        全并后的结果为:#本作品作者吴宇航
            +---+---+---+---+#本作品作者吴宇航
            | 4 | 0 | 8 | 0 |#本作品作者吴宇航
            +---+---+---+---+#本作品作者吴宇航
        最终结果: line = [4, 8, 8, 0]#本作品作者吴宇航
        '''#本作品作者吴宇航
        for i in range(3):#本作品作者吴宇航
            if line[i] == line[i + 1]:#本作品作者吴宇航
                moveflag = True#本作品作者吴宇航
                line[i] *= 2  # 左侧翻倍#本作品作者吴宇航
                line[i + 1] = 0  # 右侧归零#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
    # 移动逻辑#本作品作者吴宇航
    def _left_move_aline(line):#本作品作者吴宇航
        '''左移一行数据,如果有数据移动则返回True，否则返回False:#本作品作者吴宇航
        如: line = [2, 0, 2, 8] 即表达如下一行:#本作品作者吴宇航
            +---+---+---+---+#本作品作者吴宇航
            | 2 |   | 2 | 8 |      <----向左移动#本作品作者吴宇航
            +---+---+---+---+#本作品作者吴宇航
        左移算法分为三步:#本作品作者吴宇航
            1. 将所有数字向左移动来填补左侧空格,即:#本作品作者吴宇航
                +---+---+---+---+#本作品作者吴宇航
                | 2 | 2 | 8 |   |#本作品作者吴宇航
                +---+---+---+---+#本作品作者吴宇航
            2. 判断是否发生碰幢，如果两个相临且相等的数值则说明有碰撞需要合并,#本作品作者吴宇航
               合并结果靠左，右则填充空格 #本作品作者吴宇航
                +---+---+---+---+#本作品作者吴宇航
                | 4 |   | 8 |   |#本作品作者吴宇航
                +---+---+---+---+#本作品作者吴宇航
            3. 再重复第一步，将所有数字向左移动来填补左侧空格,即:#本作品作者吴宇航
                +---+---+---+---+#本作品作者吴宇航
                | 4 | 8 |   |   |#本作品作者吴宇航
                +---+---+---+---+#本作品作者吴宇航
            最终结果: line = [4, 8, 0, 0]#本作品作者吴宇航
        '''#本作品作者吴宇航
        moveflag = False#本作品作者吴宇航
        if _left_move_number(line):#本作品作者吴宇航
            moveflag = True#本作品作者吴宇航
        if _left_marge_number(line):#本作品作者吴宇航
            moveflag = True#本作品作者吴宇航
        if _left_move_number(line):#本作品作者吴宇航
            moveflag = True#本作品作者吴宇航
        return moveflag#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
    def left():#本作品作者吴宇航
        """游戏左键按下时或向左滑动屏幕时的算法"""#本作品作者吴宇航
        moveflag = False  # moveflag 是否成功移动数字标志位,如果有移动则为真值,原地图不变则为假值#本作品作者吴宇航
#本作品作者吴宇航
        # 将第一行都向左移动.如果有移动就返回True#本作品作者吴宇航
        for line in _map_data:#本作品作者吴宇航
            if _left_move_aline(line):#本作品作者吴宇航
                moveflag = True#本作品作者吴宇航
        return moveflag#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
    def right():#本作品作者吴宇航
        """游戏右键按下时或向右滑动屏幕时的算法#本作品作者吴宇航
        选将屏幕进行左右对调，对调后，原来的向右滑动即为现在的向左滑动#本作品作者吴宇航
        滑动完毕后，再次左右对调回来#本作品作者吴宇航
        """#本作品作者吴宇航
        # 左右对调#本作品作者吴宇航
        for r in _map_data:#本作品作者吴宇航
            r.reverse()#本作品作者吴宇航
        moveflag = left()  # 向左滑动#本作品作者吴宇航
        # 再次左右对调#本作品作者吴宇航
        for r in _map_data:#本作品作者吴宇航
            r.reverse()#本作品作者吴宇航
        return moveflag#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
    def up():#本作品作者吴宇航
        """游戏上键按下时或向上滑动屏幕时的算法#本作品作者吴宇航
        先把每一列都自上而下放入一个列表中line中，然后执行向滑动，#本作品作者吴宇航
        滑动完成后再将新位置摆回到原来的一列中#本作品作者吴宇航
        """#本作品作者吴宇航
        moveflag = False#本作品作者吴宇航
        line = [0, 0, 0, 0]  # 先初始化一行，准备放入数据#本作品作者吴宇航
        for col in range(4):  # 先取出每一列#本作品作者吴宇航
            # 把一列中的每一行数入放入到line中#本作品作者吴宇航
            for row in range(4):#本作品作者吴宇航
                line[row] = _map_data[row][col]#本作品作者吴宇航
            # 将当前列进行上移，即line 左移#本作品作者吴宇航
            if (_left_move_aline(line)):#本作品作者吴宇航
                moveflag = True#本作品作者吴宇航
            # 把左移后的 line中的数据填充回原来的一列#本作品作者吴宇航
            for row in range(4):#本作品作者吴宇航
                _map_data[row][col] = line[row]#本作品作者吴宇航
        return moveflag#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
    def down():#本作品作者吴宇航
        """游戏下键按下时或向下滑动屏幕时的算法#本作品作者吴宇航
        选将屏幕进行上下对调，对调后，原来的向下滑动即为现在的向上滑动#本作品作者吴宇航
        滑动完毕后，再次上下对调回来#本作品作者吴宇航
        """#本作品作者吴宇航
        _map_data.reverse()#本作品作者吴宇航
        moveflag = up()  # 上滑#本作品作者吴宇航
        _map_data.reverse()#本作品作者吴宇航
        return moveflag#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
    # -------------------------以下为2048游戏的操作界面---------------------------#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
    def main():#本作品作者吴宇航
        reset()  # 先重新设置游戏数据#本作品作者吴宇航
#本作品作者吴宇航
        root = Tk()  # 创建tkinter窗口#本作品作者吴宇航
        root.title('2048游戏')  # 设置标题文字#本作品作者吴宇航
        root.resizable(width=False, height=False)  # 固定宽和高#本作品作者吴宇航
#本作品作者吴宇航
        # 以下是键盘映射#本作品作者吴宇航
        keymap = {#本作品作者吴宇航
            'a': left,#本作品作者吴宇航
            'd': right,#本作品作者吴宇航
            'w': up,#本作品作者吴宇航
            's': down,#本作品作者吴宇航
            'Left': left,#本作品作者吴宇航
            'Right': right,#本作品作者吴宇航
            'Up': up,#本作品作者吴宇航
            'Down': down,#本作品作者吴宇航
            'q': root.quit,#本作品作者吴宇航
        }#本作品作者吴宇航
#本作品作者吴宇航
        game_bg_color = "#bbada0"  # 设置背景颜色#本作品作者吴宇航
#本作品作者吴宇航
        # 设置游戏中每个数据对应色块的颜色#本作品作者吴宇航
        mapcolor = {#本作品作者吴宇航
            0: ("#cdc1b4", "#776e65"),#本作品作者吴宇航
            2: ("#eee4da", "#776e65"),#本作品作者吴宇航
            4: ("#ede0c8", "#f9f6f2"),#本作品作者吴宇航
            8: ("#f2b179", "#f9f6f2"),#本作品作者吴宇航
            16: ("#f59563", "#f9f6f2"),#本作品作者吴宇航
            32: ("#f67c5f", "#f9f6f2"),#本作品作者吴宇航
            64: ("#f65e3b", "#f9f6f2"),#本作品作者吴宇航
            128: ("#edcf72", "#f9f6f2"),#本作品作者吴宇航
            256: ("#edcc61", "#f9f6f2"),#本作品作者吴宇航
            512: ("#e4c02a", "#f9f6f2"),#本作品作者吴宇航
            1024: ("#e2ba13", "#f9f6f2"),#本作品作者吴宇航
            2048: ("#ecc400", "#f9f6f2"),#本作品作者吴宇航
            4096: ("#ae84a8", "#f9f6f2"),#本作品作者吴宇航
            8192: ("#b06ca8", "#f9f6f2"),#本作品作者吴宇航
            # ----其它颜色都与8192相同---------#本作品作者吴宇航
            2 ** 14: ("#b06ca8", "#f9f6f2"),#本作品作者吴宇航
            2 ** 15: ("#b06ca8", "#f9f6f2"),#本作品作者吴宇航
            2 ** 16: ("#b06ca8", "#f9f6f2"),#本作品作者吴宇航
            2 ** 17: ("#b06ca8", "#f9f6f2"),#本作品作者吴宇航
            2 ** 18: ("#b06ca8", "#f9f6f2"),#本作品作者吴宇航
            2 ** 19: ("#b06ca8", "#f9f6f2"),#本作品作者吴宇航
            2 ** 20: ("#b06ca8", "#f9f6f2"),#本作品作者吴宇航
        }#本作品作者吴宇航
#本作品作者吴宇航
        def on_key_down(event):#本作品作者吴宇航
            '键盘按下处理函数'#本作品作者吴宇航
            keysym = event.keysym#本作品作者吴宇航
            if keysym in keymap:#本作品作者吴宇航
                if keymap[keysym]():  # 如果有数字移动#本作品作者吴宇航
                    fill2()  # 填充一个新的2#本作品作者吴宇航
            update_ui()#本作品作者吴宇航
            if is_gameover():#本作品作者吴宇航
                mb = messagebox.askyesno(#本作品作者吴宇航
                    title="gameover", message="游戏结束!\n是否退出游戏!")#本作品作者吴宇航
                if mb:#本作品作者吴宇航
                    root.quit()#本作品作者吴宇航
                else:#本作品作者吴宇航
                    reset()#本作品作者吴宇航
                    update_ui()#本作品作者吴宇航
#本作品作者吴宇航
        def update_ui():#本作品作者吴宇航
            '''刷新界面函数#本作品作者吴宇航
            根据计算出的f地图数据,更新各个Label的设置#本作品作者吴宇航
            '''#本作品作者吴宇航
            for r in range(4):#本作品作者吴宇航
                for c in range(len(_map_data[0])):#本作品作者吴宇航
                    number = _map_data[r][c]  # 设置数字#本作品作者吴宇航
                    label = map_labels[r][c]  # 选中Lable控件#本作品作者吴宇航
                    label['text'] = str(number) if number else ''#本作品作者吴宇航
                    label['bg'] = mapcolor[number][0]#本作品作者吴宇航
                    label['foreground'] = mapcolor[number][1]#本作品作者吴宇航
            label_score['text'] = str(get_score())  # 重设置分数#本作品作者吴宇航
#本作品作者吴宇航
        # 创建一个frame窗口，此创建将容纳全部的widget 部件#本作品作者吴宇航
        frame = Frame(root, bg=game_bg_color)#本作品作者吴宇航
        frame.grid(sticky=N + E + W + S)#本作品作者吴宇航
        # 设置焦点能接收按键事件#本作品作者吴宇航
        frame.focus_set()#本作品作者吴宇航
        frame.bind("<Key>", on_key_down)#本作品作者吴宇航
#本作品作者吴宇航
        # 初始化图形界面#本作品作者吴宇航
        map_labels = []#本作品作者吴宇航
        for r in range(4):#本作品作者吴宇航
            row = []#本作品作者吴宇航
            for c in range(len(_map_data[0])):#本作品作者吴宇航
                value = _map_data[r][c]#本作品作者吴宇航
                text = str(value) if value else ''#本作品作者吴宇航
                label = Label(frame, text=text, width=4, height=2,#本作品作者吴宇航
                              font=("黑体", 30, "bold"))#本作品作者吴宇航
                label.grid(row=r, column=c, padx=5, pady=5, sticky=N + E + W + S)#本作品作者吴宇航
                row.append(label)#本作品作者吴宇航
            map_labels.append(row)#本作品作者吴宇航
#本作品作者吴宇航
        # 设置显示分数的Lable#本作品作者吴宇航
        label = Label(frame, text='分数', font=("黑体", 30, "bold"),#本作品作者吴宇航
                      bg="#bbada0", fg="#eee4da")#本作品作者吴宇航
        label.grid(row=4, column=0, padx=5, pady=5)#本作品作者吴宇航
        label_score = Label(frame, text='0', font=("黑体", 30, "bold"),#本作品作者吴宇航
                            bg="#bbada0", fg="#ffffff")#本作品作者吴宇航
        label_score.grid(row=4, columnspan=2, column=1, padx=5, pady=5)#本作品作者吴宇航
#本作品作者吴宇航
        # 以下设置重新开始按钮#本作品作者吴宇航
        def reset_game():#本作品作者吴宇航
            reset()#本作品作者吴宇航
            update_ui()#本作品作者吴宇航
#本作品作者吴宇航
        restart_button = Button(frame, text='重新开始', font=("黑体", 16, "bold"),#本作品作者吴宇航
                                bg="#8f7a66", fg="#f9f6f2", command=reset_game)#本作品作者吴宇航
        restart_button.grid(row=4, column=3, padx=5, pady=5)#本作品作者吴宇航
#本作品作者吴宇航
        update_ui()  # 更新界面#本作品作者吴宇航
#本作品作者吴宇航
        root.mainloop()  # 进入tkinter主事件循环#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
    main()  # 启动游戏#本作品作者吴宇航
#本作品作者吴宇航
#扫雷游戏#本作品作者吴宇航
def saolei():#本作品作者吴宇航
    # 地雷数量#本作品作者吴宇航
    MINE_COUNT = 99#本作品作者吴宇航
    # 每个方格的大小（宽、高都为20）#本作品作者吴宇航
    SIZE = 20#本作品作者吴宇航
    # 方格的行数#本作品作者吴宇航
    BLOCK_ROW_NUM = 16#本作品作者吴宇航
    # 方格的列数#本作品作者吴宇航
    BLOCK_COL_NUM = 30#本作品作者吴宇航
    # 游戏窗口的宽、高#本作品作者吴宇航
    SCREEN_WIDTH, SCREEN_HEIGHT = BLOCK_COL_NUM * SIZE, (BLOCK_ROW_NUM + 2) * SIZE#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
    def get_mine_flag_num(board_list):#本作品作者吴宇航
        """#本作品作者吴宇航
        计算还剩多少颗雷#本作品作者吴宇航
        """#本作品作者吴宇航
        num = 0#本作品作者吴宇航
        for line in board_list:#本作品作者吴宇航
            for num_dict in line:#本作品作者吴宇航
                if num_dict.get("closed_num") == "雷标记":#本作品作者吴宇航
                    num += 1#本作品作者吴宇航
#本作品作者吴宇航
        return num#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
    def open_all_mine(board_list):#本作品作者吴宇航
        """#本作品作者吴宇航
        显示所有的雷#本作品作者吴宇航
        """#本作品作者吴宇航
        for row, line in enumerate(board_list):#本作品作者吴宇航
            for col, num_dict in enumerate(line):#本作品作者吴宇航
                if num_dict.get("opened_num") == "雷":#本作品作者吴宇航
                    num_dict["opened"] = True#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
    def get_mine_num(row, col, board_list):#本作品作者吴宇航
        """#本作品作者吴宇航
        计算点击的空格周围的雷的数量#本作品作者吴宇航
        """#本作品作者吴宇航
        # 生成起始位置、终止位置#本作品作者吴宇航
        row_start = row - 1 if row - 1 >= 0 else row#本作品作者吴宇航
        row_stop = row + 2 if row + 1 <= BLOCK_ROW_NUM - 1 else row + 1#本作品作者吴宇航
        col_start = col - 1 if col - 1 >= 0 else col#本作品作者吴宇航
        col_stop = col + 2 if col + 1 <= BLOCK_COL_NUM - 1 else col + 1#本作品作者吴宇航
#本作品作者吴宇航
        # 循环遍历当前方格周围的雷的数量#本作品作者吴宇航
        mine_num = 0#本作品作者吴宇航
        for i in range(row_start, row_stop):#本作品作者吴宇航
            for j in range(col_start, col_stop):#本作品作者吴宇航
                if board_list[i][j].get("opened_num") == "雷":#本作品作者吴宇航
                    mine_num += 1#本作品作者吴宇航
        return mine_num#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
    def set_nums_blank(row, col, board_list):#本作品作者吴宇航
        """#本作品作者吴宇航
        判断当前位置的周边位置是否为空，如果是则继续判断，#本作品作者吴宇航
        最终能够实现点击一个空位置后连续的空位置都能够显示出来#本作品作者吴宇航
        """#本作品作者吴宇航
        mine_num = get_mine_num(row, col, board_list)#本作品作者吴宇航
        print("row=%d, col=%d, mine_num=%d" % (row, col, mine_num))#本作品作者吴宇航
        if mine_num == 0:#本作品作者吴宇航
            board_list[row][col]['opened'] = True#本作品作者吴宇航
            board_list[row][col]["opened_num"] = 0#本作品作者吴宇航
            board_list[row][col]["closed_num"] = "空"#本作品作者吴宇航
            # 判断对角是否是数字#本作品作者吴宇航
            for i, j in [(-1, -1), (1, 1), (1, -1), (-1, 1)]:#本作品作者吴宇航
                if 0 <= row + i <= 15 and 0 <= col + j <= 29:#本作品作者吴宇航
                    mine_num = get_mine_num(row + i, col + j, board_list)#本作品作者吴宇航
                    if mine_num:#本作品作者吴宇航
                        board_list[row + i][col + j]['opened'] = True#本作品作者吴宇航
                        board_list[row + i][col + j]["opened_num"] = mine_num#本作品作者吴宇航
                        board_list[row + i][col + j]["closed_num"] = "空"#本作品作者吴宇航
#本作品作者吴宇航
            # 判断剩下4个位置是否是也是0，即空#本作品作者吴宇航
            for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:#本作品作者吴宇航
                if 0 <= row + i <= 15 and 0 <= col + j <= 29:#本作品作者吴宇航
                    if not board_list[row + i][col + j].get("opened"):#本作品作者吴宇航
                        set_nums_blank(row + i, col + j, board_list)#本作品作者吴宇航
        else:#本作品作者吴宇航
            board_list[row][col]['opened'] = True#本作品作者吴宇航
            board_list[row][col]["opened_num"] = mine_num#本作品作者吴宇航
            board_list[row][col]["closed_num"] = "空"#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
    def left_click_block(row, col, board_list):#本作品作者吴宇航
        """#本作品作者吴宇航
        左击空格后的处理#本作品作者吴宇航
        """#本作品作者吴宇航
        if board_list[row][col].get("opened") is False and board_list[row][col].get("opened_num") != "雷":#本作品作者吴宇航
            # 如果不是雷，那么就计算当前位置数字#本作品作者吴宇航
            mine_num = get_mine_num(row, col, board_list)#本作品作者吴宇航
            print("地雷数:", mine_num)#本作品作者吴宇航
            board_list[row][col]["opened_num"] = mine_num#本作品作者吴宇航
            board_list[row][col]["opened"] = True  # 标记为"打开"状态#本作品作者吴宇航
            board_list[row][col]["closed_num"] = "空"  # 标记为"未打开时的状态为空格"，防止显示剩余雷数错误#本作品作者吴宇航
            if mine_num == 0:#本作品作者吴宇航
                # 如果方格周边没有雷此时，判断是否有连续空位置#本作品作者吴宇航
                set_nums_blank(row, col, board_list)#本作品作者吴宇航
        elif board_list[row][col].get("opened") is False and board_list[row][col].get("opened_num") == "雷":#本作品作者吴宇航
            board_list[row][col]["opened_num"] = "踩雷"  # 标记为"踩雷"图片#本作品作者吴宇航
            board_list[row][col]["opened"] = True  # 标记为"打开"状态#本作品作者吴宇航
            board_list[row][col]["closed_num"] = "空"  # 标记为"未打开时的状态为空格"，防止显示剩余雷数错误#本作品作者吴宇航
            return True#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
    def create_random_board(row, col, mine_num):#本作品作者吴宇航
        """#本作品作者吴宇航
        得到一个随机的棋盘#本作品作者吴宇航
        """#本作品作者吴宇航
        # 随机布雷#本作品作者吴宇航
        nums = [{"opened": False, "opened_num": 0, 'closed_num': "空"} for _ in range(row * col - mine_num)]  # 16x30-99 表示的是生成381个0#本作品作者吴宇航
        nums += [{"opened": False, "opened_num": "雷", 'closed_num': "空"} for _ in range(mine_num)]  # 99颗地雷#本作品作者吴宇航
        random.shuffle(nums)  # 乱序，此时nums是乱的#本作品作者吴宇航
        return [list(x) for x in zip(*[iter(nums)] * col)]#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
    def right_click_block(row, col, board_list):#本作品作者吴宇航
        """#本作品作者吴宇航
        右击方格后更新其状态（标记为雷、问号?、取消标记）#本作品作者吴宇航
        """#本作品作者吴宇航
        if board_list[row][col].get("opened") is False:#本作品作者吴宇航
            if board_list[row][col]["closed_num"] == "空":#本作品作者吴宇航
                board_list[row][col]["closed_num"] = "雷标记"#本作品作者吴宇航
            elif board_list[row][col]["closed_num"] == "雷标记":#本作品作者吴宇航
                board_list[row][col]["closed_num"] = "疑问标记"#本作品作者吴宇航
            elif board_list[row][col]["closed_num"] == "疑问标记":#本作品作者吴宇航
                board_list[row][col]["closed_num"] = "空"#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
    def click_block(x, y, board_list):#本作品作者吴宇航
        """#本作品作者吴宇航
        检测点击的是哪个方格（即第x行，第y列）#本作品作者吴宇航
        """#本作品作者吴宇航
        # 计算出点击的空格的行、列#本作品作者吴宇航
        for row, line in enumerate(board_list):#本作品作者吴宇航
            for col, _ in enumerate(line):#本作品作者吴宇航
                if col * SIZE <= x <= (col + 1) * SIZE and (row + 2) * SIZE <= y <= (row + 2 + 1) * SIZE:#本作品作者吴宇航
                    print("点击的空格的位置是:", row, col)#本作品作者吴宇航
                    return row, col#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
    def run(screen):#本作品作者吴宇航
        bgcolor = (225, 225, 225)  # 背景色#本作品作者吴宇航
#本作品作者吴宇航
        # 要显示的棋盘#本作品作者吴宇航
        # board_list = [[0] * BLOCK_COL_NUM for _ in range(BLOCK_ROW_NUM)]#本作品作者吴宇航
        board_list = create_random_board(BLOCK_ROW_NUM, BLOCK_COL_NUM, MINE_COUNT)  # 16行、30列，有99颗地雷#本作品作者吴宇航
#本作品作者吴宇航
        # 默认的方格图片#本作品作者吴宇航
        img_blank = pygame.image.load('resource/blank.bmp').convert()#本作品作者吴宇航
        img_blank = pygame.transform.smoothscale(img_blank, (SIZE, SIZE))#本作品作者吴宇航
        # "雷标记"图片#本作品作者吴宇航
        img_mine_flag = pygame.image.load('resource/flag.bmp').convert()#本作品作者吴宇航
        img_mine_flag = pygame.transform.smoothscale(img_mine_flag, (SIZE, SIZE))#本作品作者吴宇航
        # "雷"图片#本作品作者吴宇航
        img_mine = pygame.image.load('resource/mine.bmp').convert()#本作品作者吴宇航
        img_mine = pygame.transform.smoothscale(img_mine, (SIZE, SIZE))#本作品作者吴宇航
        # "疑问标记"图片#本作品作者吴宇航
        img_ask = pygame.image.load('resource/ask.bmp').convert()#本作品作者吴宇航
        img_ask = pygame.transform.smoothscale(img_ask, (SIZE, SIZE))#本作品作者吴宇航
        # "踩雷"图片#本作品作者吴宇航
        img_blood = pygame.image.load('resource/blood.bmp').convert()#本作品作者吴宇航
        img_blood = pygame.transform.smoothscale(img_blood, (SIZE, SIZE))#本作品作者吴宇航
        # "表情"图片#本作品作者吴宇航
        face_size = int(SIZE * 1.25)#本作品作者吴宇航
        img_face_fail = pygame.image.load('resource/face_fail.bmp').convert()#本作品作者吴宇航
        img_face_fail = pygame.transform.smoothscale(img_face_fail, (face_size, face_size))#本作品作者吴宇航
        img_face_normal = pygame.image.load('resource/face_normal.bmp').convert()#本作品作者吴宇航
        img_face_normal = pygame.transform.smoothscale(img_face_normal, (face_size, face_size))#本作品作者吴宇航
        img_face_success = pygame.image.load('resource/face_success.bmp').convert()#本作品作者吴宇航
        img_face_success = pygame.transform.smoothscale(img_face_success, (face_size, face_size))#本作品作者吴宇航
        # "表情"位置#本作品作者吴宇航
        face_pos_x = (SCREEN_WIDTH - face_size) // 2#本作品作者吴宇航
        face_pos_y = (SIZE * 2 - face_size) // 2#本作品作者吴宇航
        # 类的数量图片#本作品作者吴宇航
        img0 = pygame.image.load('resource/0.bmp').convert()#本作品作者吴宇航
        img0 = pygame.transform.smoothscale(img0, (SIZE, SIZE))#本作品作者吴宇航
        img1 = pygame.image.load('resource/1.bmp').convert()#本作品作者吴宇航
        img1 = pygame.transform.smoothscale(img1, (SIZE, SIZE))#本作品作者吴宇航
        img2 = pygame.image.load('resource/2.bmp').convert()#本作品作者吴宇航
        img2 = pygame.transform.smoothscale(img2, (SIZE, SIZE))#本作品作者吴宇航
        img3 = pygame.image.load('resource/3.bmp').convert()#本作品作者吴宇航
        img3 = pygame.transform.smoothscale(img3, (SIZE, SIZE))#本作品作者吴宇航
        img4 = pygame.image.load('resource/4.bmp').convert()#本作品作者吴宇航
        img4 = pygame.transform.smoothscale(img4, (SIZE, SIZE))#本作品作者吴宇航
        img5 = pygame.image.load('resource/5.bmp').convert()#本作品作者吴宇航
        img5 = pygame.transform.smoothscale(img5, (SIZE, SIZE))#本作品作者吴宇航
        img6 = pygame.image.load('resource/6.bmp').convert()#本作品作者吴宇航
        img6 = pygame.transform.smoothscale(img6, (SIZE, SIZE))#本作品作者吴宇航
        img7 = pygame.image.load('resource/7.bmp').convert()#本作品作者吴宇航
        img7 = pygame.transform.smoothscale(img7, (SIZE, SIZE))#本作品作者吴宇航
        img8 = pygame.image.load('resource/8.bmp').convert()#本作品作者吴宇航
        img8 = pygame.transform.smoothscale(img8, (SIZE, SIZE))#本作品作者吴宇航
        img_dict = {#本作品作者吴宇航
            0: img0,#本作品作者吴宇航
            1: img1,#本作品作者吴宇航
            2: img2,#本作品作者吴宇航
            3: img3,#本作品作者吴宇航
            4: img4,#本作品作者吴宇航
            5: img5,#本作品作者吴宇航
            6: img6,#本作品作者吴宇航
            7: img7,#本作品作者吴宇航
            8: img8,#本作品作者吴宇航
            '雷标记': img_mine_flag,#本作品作者吴宇航
            '雷': img_mine,#本作品作者吴宇航
            '空': img_blank,#本作品作者吴宇航
            '疑问标记': img_ask,#本作品作者吴宇航
            '踩雷': img_blood,#本作品作者吴宇航
        }#本作品作者吴宇航
        # 标记是否踩到雷#本作品作者吴宇航
        game_over = False#本作品作者吴宇航
        # 游戏状态#本作品作者吴宇航
        game_status = "normal"#本作品作者吴宇航
        # 显示雷的数量、耗时用到的资源#本作品作者吴宇航
        font = pygame.font.Font('resource/a.TTF', SIZE * 2)  # 字体#本作品作者吴宇航
        f_width, f_height = font.size('999')#本作品作者吴宇航
        red = (200, 40, 40)#本作品作者吴宇航
        # 标记出雷的个数#本作品作者吴宇航
        flag_count = 0#本作品作者吴宇航
        # 记录耗时#本作品作者吴宇航
        elapsed_time = 0#本作品作者吴宇航
        last_time = time.time()#本作品作者吴宇航
        start_record_time = False#本作品作者吴宇航
#本作品作者吴宇航
        # 创建计时器（防止while循环过快，占用太多CPU的问题）#本作品作者吴宇航
        clock = pygame.time.Clock()#本作品作者吴宇航
        while True:#本作品作者吴宇航
            # 事件检测（鼠标点击、键盘按下等）#本作品作者吴宇航
            for event in pygame.event.get():#本作品作者吴宇航
                if event.type == pygame.QUIT:#本作品作者吴宇航
                    pygame.quit()#本作品作者吴宇航
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button:#本作品作者吴宇航
                    b1, b2, b3 = pygame.mouse.get_pressed()#本作品作者吴宇航
                    mouse_click_type = None#本作品作者吴宇航
                    if b1 and not b2 and not b3:  # 左击#本作品作者吴宇航
                        mouse_click_type = "left"#本作品作者吴宇航
                    elif not b1 and not b2 and b3:  # 右击#本作品作者吴宇航
                        mouse_click_type = "right"#本作品作者吴宇航
                    print("点击了鼠标的[%s]键" % mouse_click_type)#本作品作者吴宇航
                    x, y = pygame.mouse.get_pos()#本作品作者吴宇航
                    if game_status == "normal" and 2 * SIZE <= y <= SCREEN_HEIGHT:#本作品作者吴宇航
                        # 计算点击的是哪个空#本作品作者吴宇航
                        position = click_block(x, y, board_list)#本作品作者吴宇航
                        if position:#本作品作者吴宇航
                            if mouse_click_type == "right":#本作品作者吴宇航
                                # 如果右击方格，那么就更新其状态#本作品作者吴宇航
                                right_click_block(*position, board_list)#本作品作者吴宇航
                                # 更新标记的雷的数量#本作品作者吴宇航
                                flag_count = get_mine_flag_num(board_list)#本作品作者吴宇航
                                start_record_time = True  # 开始记录耗时#本作品作者吴宇航
                            elif mouse_click_type == "left":#本作品作者吴宇航
                                # 点击空格的处理#本作品作者吴宇航
                                game_over = left_click_block(*position, board_list)#本作品作者吴宇航
                                print("是否踩到雷", game_over)#本作品作者吴宇航
                                start_record_time = True  # 开始记录耗时#本作品作者吴宇航
                                # 更新标记的雷的数量#本作品作者吴宇航
                                flag_count = get_mine_flag_num(board_list)#本作品作者吴宇航
                                if game_over:#本作品作者吴宇航
                                    # 将所有雷的位置，标记出来#本作品作者吴宇航
                                    open_all_mine(board_list)#本作品作者吴宇航
                                    # 更改游戏状态#本作品作者吴宇航
                                    game_status = "fail"#本作品作者吴宇航
                                    # 停止记录耗时#本作品作者吴宇航
                                    start_record_time = False#本作品作者吴宇航
                    elif face_pos_x <= x <= face_pos_x + face_size and face_pos_y <= y <= face_pos_y + face_size:#本作品作者吴宇航
                        # 重来一局#本作品作者吴宇航
                        print("点击了再来一局...")#本作品作者吴宇航
                        return#本作品作者吴宇航
#本作品作者吴宇航
            # 填充背景色#本作品作者吴宇航
            screen.fill(bgcolor)#本作品作者吴宇航
#本作品作者吴宇航
            # 显示方格#本作品作者吴宇航
            for i, line in enumerate(board_list):#本作品作者吴宇航
                for j, num_dict in enumerate(line):#本作品作者吴宇航
                    if num_dict.get("opened"):#本作品作者吴宇航
                        screen.blit(img_dict[num_dict.get("opened_num")], (j * SIZE, (i + 2) * SIZE))#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        screen.blit(img_dict[num_dict.get("closed_num")], (j * SIZE, (i + 2) * SIZE))#本作品作者吴宇航
#本作品作者吴宇航
            # 显示表情#本作品作者吴宇航
            if game_status == "win":#本作品作者吴宇航
                screen.blit(img_face_success, (face_pos_x, face_pos_y))#本作品作者吴宇航
            elif game_status == "fail":#本作品作者吴宇航
                screen.blit(img_face_fail, (face_pos_x, face_pos_y))#本作品作者吴宇航
            else:#本作品作者吴宇航
                screen.blit(img_face_normal, (face_pos_x, face_pos_y))#本作品作者吴宇航
#本作品作者吴宇航
            # 显示剩余雷的数量#本作品作者吴宇航
            mine_text = font.render('%02d' % (MINE_COUNT - flag_count), True, red)#本作品作者吴宇航
            screen.blit(mine_text, (30, (SIZE * 2 - f_height) // 2 - 2))#本作品作者吴宇航
#本作品作者吴宇航
            # 显示耗时#本作品作者吴宇航
            if start_record_time and time.time() - last_time >= 1:#本作品作者吴宇航
                elapsed_time += 1#本作品作者吴宇航
                last_time = time.time()#本作品作者吴宇航
            mine_text = font.render('%03d' % elapsed_time, True, red)#本作品作者吴宇航
            screen.blit(mine_text, (SCREEN_WIDTH - f_width - 30, (SIZE * 2 - f_height) // 2 - 2))#本作品作者吴宇航
#本作品作者吴宇航
            # 刷新显示（此时窗口才会真正的显示）#本作品作者吴宇航
            pygame.display.update()#本作品作者吴宇航
            # FPS（每秒钟显示画面的次数）#本作品作者吴宇航
            clock.tick(60)  # 通过一定的延时，实现1秒钟能够循环60次#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
    def main():#本作品作者吴宇航
        """#本作品作者吴宇航
        循环调用run函数，每调用一次就重新来一局游戏#本作品作者吴宇航
        """#本作品作者吴宇航
        pygame.init()#本作品作者吴宇航
        pygame.display.set_caption('扫雷')#本作品作者吴宇航
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))#本作品作者吴宇航
        while True:#本作品作者吴宇航
            run(screen)#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
    if __name__ == '__main__':#本作品作者吴宇航
        main()#本作品作者吴宇航
#图片处理器
from tkinter import messagebox  # 导入来自tkinter库的messagebox模块,用来提示
from PIL import Image as Ima  # 导入来自PIL库的Image模块用来加载图片,防止与tkinter库的image模块混乱,起个小名
from tkinter import *  # 导入tkinter库的全部模块
from tkinter.filedialog import *  # 导入tkinter文件对话框的全部模块
from PIL import ImageEnhance  # 图片各度数增强处理模块
from PIL import ImageFilter  # 图片添加效果模块
def photoshop():
    # 自定义类
    class Window:
        # 定义类初始化函数，创建窗口并设置窗口信息
        def __init__(self):
            self.picformat = ['png', 'jpg']  # 创建图片格式列表，用来判断选择文件是否是图片格式
            self.title = '图片处理器'  # 程序标题
            self.app = Tk()  # 窗口实例化
            self.app.title(self.title)  # 设置窗口标题
            self.app.geometry('342x301')  # 设置窗口大小
            self.app.resizable(False, False)  # 设置窗口宽和高是否可变，默认为True
    
        # 创建窗体组件
        def createWidgets(self):
            self.picVar = StringVar(value='请选择要处理的图片')  # 创建图片文件路径变量，用来显示在Tk控件上
            self.Text1 = Entry(self.app,  textvariable=self.picVar,
                               font=('宋体', 14), state="readonly")  # textvariable 文本显示的变量值，和上面创建的变量绑定
            # state 控件状态 默认为'normal'正常  'readonly'只读  'disabled'禁用
            self.Text1.place(relx=0., rely=0.027, relwidth=0.798,
                             relheight=0.11)  # 设置控件大小及显示的坐标位置
    
            self.cho_pic = Button(self.app, text='加载图片',
                                  command=self.cho_pic_button_click) # 按钮组件 command绑定按钮事件
            self.cho_pic.place(relx=0.819, rely=0.027,
                               relwidth=0.167, relheight=0.11)
    
            self.pathVar = StringVar(value='请选择输出图片路径')
            self.Text2 = Entry(self.app, textvariable=self.pathVar,
                               font=('宋体', 14), state="readonly")
            self.Text2.place(relx=0., rely=0.159, relwidth=0.798, relheight=0.11)
    
            self.cho_path = Button(self.app, text='输出路径',
                                   command=self.cho_path_button_click)
            self.cho_path.place(relx=0.819, rely=0.159,
                                relwidth=0.167, relheight=0.11)
    
            # LabelFrame 分组标签，将小组件包围起来形成边框
            self.Frame1 = LabelFrame(self.app, text='尺寸处理', )
            self.Frame1.place(relx=0.023, rely=0.292,
                              relwidth=0.401, relheight=0.694)
    
            self.angelVar = StringVar(value='旋转角度')
            self.Text3 = Entry(self.app, text='旋转角度',
                               textvariable=self.angelVar, font=('宋体', 9), state='readonly')
            self.Text3.place(relx=0.207, rely=0.372,
                             relwidth=0.183, relheight=0.083)
    
            self.angel_01 = StringVar(value='0')
            self.Check1 = Checkbutton(
                self.app, text='旋转', variable=self.angel_01, command=self.angel_check_click)  # Checkbutton 多选框(多选按钮)
            self.Check1.place(relx=0.047, rely=0.372,
                              relwidth=0.143, relheight=0.083)
    
            self.aroundVar = StringVar(value='0')
            self.Check8 = Checkbutton(
                self.app, text='左右翻转', variable=self.aroundVar)
            self.Check8.place(relx=0.047, rely=0.691,
                              relwidth=0.237, relheight=0.11)
    
            self.fluctuateVar = StringVar(value='0')
            self.Check8 = Checkbutton(
                self.app, text='上下翻转', variable=self.fluctuateVar)
            self.Check8.place(relx=0.047, rely=0.824,
                              relwidth=0.237, relheight=0.11)
    
            self.widthVar = StringVar(value='宽度')
            self.Text4 = Entry(
                self.app, textvariable=self.widthVar, font=('宋体', 9), state='readonly')
            self.Text4.place(relx=0.207, rely=0.478,
                             relwidth=0.183, relheight=0.083)
    
            self.size_01 = StringVar(value='0')
            self.Check2 = Checkbutton(
                self.app, text='尺寸\n调节', variable=self.size_01, command=self.size_check_click)
            self.Check2.place(relx=0.047, rely=0.478,
                              relwidth=0.143, relheight=0.189)
    
            self.heightVar = StringVar(value='高度')
            self.Text5 = Entry(self.app, text='高度',
                               textvariable=self.heightVar, font=('宋体', 9), state='readonly')
            self.Text5.place(relx=0.207, rely=0.585,
                             relwidth=0.183, relheight=0.083)
    
            self.Frame2 = LabelFrame(self.app, text='效果处理')
            self.Frame2.place(relx=0.444, rely=0.292,
                              relwidth=0.307, relheight=0.694)
    
            self.brightnessVar = StringVar(value='0')
            self.Check3 = Checkbutton(
                self.app, text='亮度增强', variable=self.brightnessVar)
            self.Check3.place(relx=0.468, rely=0.346,
                              relwidth=0.237, relheight=0.11)
    
            self.colorVar = StringVar(value='0')
            self.Check4 = Checkbutton(
                self.app, text='色度增强', variable=self.colorVar)
            self.Check4.place(relx=0.468, rely=0.452,
                              relwidth=0.237, relheight=0.11)
    
            self.sharpnessVar = StringVar(value='0')
            self.Check5 = Checkbutton(
                self.app, text='锐度增强', variable=self.sharpnessVar)
            self.Check5.place(relx=0.468, rely=0.558,
                              relwidth=0.237, relheight=0.11)
    
            self.contrastVar = StringVar(value='0')
            self.Check6 = Checkbutton(
                self.app, text='对比度增强', variable=self.contrastVar)
            self.Check6.place(relx=0.468, rely=0.664,
                              relwidth=0.237, relheight=0.11)
    
            self.blurVar = StringVar(value='0')
            self.Check7 = Checkbutton(
                self.app, text='模糊处理', variable=self.blurVar)
            self.Check7.place(relx=0.468, rely=0.771,
                              relwidth=0.237, relheight=0.11)
    
            self.Btn_Start = Button(self.app, text='开始处理',
                                    command=self.start_button_click)
            self.Btn_Start.place(relx=0.772, rely=0.372,
                                 relwidth=0.213, relheight=0.535)
    
        # 选择图片按钮点击事件
        def cho_pic_button_click(self):
            # Var变量.set()函数 设置变量的值 *此处是将图片路径设置并显示到图片路径输入框
            self.picVar.set(askopenfilename())
            self.judge_pic()  # 打开文件对话框后判断图片是否合法，调用下面函数
    
        # 判断选择的图片是否合法
        def judge_pic(self):
            if self.picVar.get() != '':  # 首先判断用户是否点关闭或者取消文件对话框，如果关闭或取消都会返回空的字符串值
                if self.picVar.get() != '请选择要处理的图片':  # 此句判定为了后续开始按钮点击事件使用
                    if self.picVar.get()[-3:] in self.picformat:  # 判断选择的文件后缀名是否为图片后缀
                        self.image = Ima.open(self.picVar.get())  # 合法后打开图片
                        return True  # 返回成功值以便后续判断使用
                    else:  # 选择文件不是图片格式则提示用户
                        # showinfo()函数 用来显示信息
                        messagebox.showinfo(
                            title=self.title, message='错误的图片文件,请重新选择')
                        self.picVar.set('请选择要处理的图片')
            else:
                self.picVar.set('请选择要处理的图片')  # 如果关闭或取消文件对话框，再将提示显示上去
    
        # 输出路径按钮点击事件
        def cho_path_button_click(self):
            self.pathVar.set(askdirectory())
            self.judge_path()
    
        # 判断选择的路径是否合法
        def judge_path(self):
            if self.pathVar.get() != '' and self.pathVar.get() != '请选择输出图片路径':
                self.path = self.pathVar.get()+'/'  # 原路径加上'/' 为了正确输出，必须加！
                return True
            else:
                self.pathVar.set('请选择输出图片路径')
    
        # 旋转多选框点击事件
        def angel_check_click(self):
            if self.angel_01.get() == '0':
                self.Text3.config(state='readonly')
                self.angelVar.set('旋转角度')
            else:
                self.Text3.config(state='normal')
                self.angelVar.set('')
            # 逻辑总结：每次点击都会判断当前选择状态，如果选中那么角度输入框则正常输入并设置输入框为空值方便输入，否则禁用并设置提示文本显示上去
    
        # 尺寸多选框点击事件
        def size_check_click(self):
            if self.size_01.get() == '0':
                self.Text4.config(state='readonly')
                self.Text5.config(state='readonly')
                self.widthVar.set('宽度')
                self.heightVar.set('高度')
            else:
                self.Text4.config(state='normal')
                self.Text5.config(state='normal')
                self.widthVar.set('')
                self.heightVar.set('')
    
        # 判断是否选中旋转，如果选中开始处理
        def start_rotate(self):
            if self.angelVar.get().isdigit() == True:  # 如果选择角度输入框的值为纯整数则可以处理旋转
                self.image = self.image.rotate(
                    int(self.angelVar.get()))  # 将图片旋转过后重新赋值给图片变量，以便后续接着处理
            elif self.angelVar.get() != '旋转角度':  # 如果输入框的值不是纯整数并且不为默认提示内容，就是多选框被选中但是输入角度不合法
                messagebox.showinfo(
                    title=self.title, message='旋转角度有误！旋转失败！')  # 给出提示
            # 需要注意：显示文本的值为字符串类型，旋转角度需要转到int或float
    
        # 判断是否选中尺寸修改，如果选中开始修改
        def start_size(self):
            if self.widthVar.get().isdigit() == True and self.heightVar.get().isdigit() == True:
                self.size = (int(self.widthVar.get()), int(self.heightVar.get()))
                self.image = self.image.resize(self.size)
            elif self.widthVar.get() != '宽度':
                messagebox.showinfo(title=self.title, message='宽度或高度有误！,尺寸调节失败！')
            # 逻辑总结：同旋转，不过注意的是调节尺寸参数为元组类型，需要将宽和高放到一个元组里
    
        # 判断是否选中左右翻转，如果选中开始翻转
        def start_around(self):
            if self.aroundVar.get() == '1':
                self.image = self.image.transpose(Ima.FLIP_LEFT_RIGHT)
    
        # 判断是否选中上下翻转，如果选中开始翻转
        def start_fluctuate(self):
            if self.fluctuateVar.get() == '1':
                self.image = self.image.transpose(Ima.FLIP_TOP_BOTTOM)
    
        # 效果处理函数，逐个判断并处理
        def start_enhance(self):
            if self.brightnessVar.get() == '1':  # 如果亮度多选框选中为真
                self.ima_bri = ImageEnhance.Brightness(self.image)
                self.image = self.ima_bri.enhance(1.5)
    
            if self.colorVar.get() == '1':  # 如果色度多选框选中为真
                self.ima_col = ImageEnhance.Color(self.image)
                self.image = self.ima_col.enhance(1.5)
    
            if self.sharpnessVar.get() == '1':  # 如果锐度多选框选中为真
                self.ima_sha = ImageEnhance.Sharpness(self.image)
                self.image = self.ima_sha.enhance(3.0)
    
            if self.contrastVar.get() == '1':  # 如果对比度多选框选中为真
                self.ima_con = ImageEnhance.Contrast(self.image)
                self.image = self.ima_con.enhance(1.5)
    
            if self.blurVar.get() == '1':  # 如果模糊多选框选中为真
                self.image = self.image.filter(ImageFilter.BLUR)
    
        # 开始处理按钮点击事件
        def start_button_click(self):
            if self.judge_pic() == True and self.judge_path() == True:  # 同时调用两个函数并获取返回值进行判定，同时成立则可以开始处理
                self.start_rotate()  # 调用旋转函数
                self.start_size()  # 调用处理尺寸函数
                self.start_around()  # 调用左右翻转函数
                self.start_fluctuate()  # 调用上下翻转函数
                self.start_enhance()  # 调用效果处理函数
    
                # 处理完毕后保存图片到输出路径，在原文件名前加'处理-'提高识别度
                self.image.save(self.path+'处理-'+self.picVar.get().split('/')[-1])
                # 保存完毕给出提示
                messagebox.showinfo(
                    title=self.title, message='处理完毕！已输出到%s目录下' % (self.pathVar.get()))
            else:  # 如果文件或路径不合法则给出提示信息
                messagebox.showinfo(title=self.title, message='图片或输出路径有误！')
    
    
    window = Window()  # 类实例化
    window.createWidgets()  # 调用创建组件函数
    window.app.mainloop()  # 程序主循环执行

#本作品作者吴宇航
#主程序#本作品作者吴宇航
def fasdasdf1():#本作品作者吴宇航
    #变量定义#本作品作者吴宇航
    global dakai,xuanzhong#本作品作者吴宇航
    xuanzhong = None#本作品作者吴宇航
    dakai = None#本作品作者吴宇航
#本作品作者吴宇航
    #窗口设置#本作品作者吴宇航
    pygame.init()#本作品作者吴宇航
    screen = pygame.display.set_mode((1150,768))#本作品作者吴宇航
    pygame.display.set_caption("Starry Sky System(星空系统)")#本作品作者吴宇航
#本作品作者吴宇航
    #主循环体#本作品作者吴宇航
    while True:#本作品作者吴宇航
        #循环遍历检测#本作品作者吴宇航
        for event in pygame.event.get():#本作品作者吴宇航
            #退出事件#本作品作者吴宇航
            if event.type == pygame.QUIT:#本作品作者吴宇航
                if messagebox.askokcancel("是否退出", "您确定退出吗（主窗口退出将直接结束程序）"):#本作品作者吴宇航
                    sys.exit(0)#本作品作者吴宇航
#本作品作者吴宇航
            #快捷键#本作品作者吴宇航
            elif event.type == pygame.KEYDOWN:#本作品作者吴宇航
                if event.key == pygame.K_j:#本作品作者吴宇航
                    ImageGrab.grab().show()#本作品作者吴宇航
                elif event.key == pygame.K_f:#本作品作者吴宇航
                    dakai = "file"#本作品作者吴宇航
                elif event.key == pygame.K_n:#本作品作者吴宇航
                    dakai = "news"#本作品作者吴宇航
                elif event.key == pygame.K_e:#本作品作者吴宇航
                    dakai = "brow"#本作品作者吴宇航
                elif event.key == pygame.K_c:#本作品作者吴宇航
                    dakai = "com"#本作品作者吴宇航
                elif event.key == pygame.K_r:#本作品作者吴宇航
                    dakai = "sousuo"#本作品作者吴宇航
                elif event.key == pygame.K_g:#本作品作者吴宇航
                    dakai = "cmd"#本作品作者吴宇航
#本作品作者吴宇航
            #检测应用、任务栏被选中、打开#本作品作者吴宇航
            elif event.type == pygame.MOUSEBUTTONDOWN:#本作品作者吴宇航
                #应用打开#本作品作者吴宇航
#本作品作者吴宇航
                #文件管理器#本作品作者吴宇航
                if mouseRect.colliderect(fileRect):#本作品作者吴宇航
                    if xuanzhong == "file":#本作品作者吴宇航
                        dakai = "file"#本作品作者吴宇航
                        #本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "file"#本作品作者吴宇航
#本作品作者吴宇航
                #音乐播放器#本作品作者吴宇航
                if mouseRect.colliderect(musicRect):#本作品作者吴宇航
                    if xuanzhong == "music":#本作品作者吴宇航
                        dakai = "music"#本作品作者吴宇航
                        #本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "music"#本作品作者吴宇航
                #Vs Code编辑器#本作品作者吴宇航
                if mouseRect.colliderect(vsRect):#本作品作者吴宇航
                    if xuanzhong == "vs":#本作品作者吴宇航
                        dakai = "vs"#本作品作者吴宇航
                        #本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "vs"#本作品作者吴宇航
#本作品作者吴宇航
                #系统设置、此电脑#本作品作者吴宇航
                if mouseRect.colliderect(comRect):#本作品作者吴宇航
                    if xuanzhong == "com":#本作品作者吴宇航
                        dakai = "com"#本作品作者吴宇航
                        #本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "com"#本作品作者吴宇航
#本作品作者吴宇航
                #浏览器#本作品作者吴宇航
                if mouseRect.colliderect(browRect):#本作品作者吴宇航
                    if xuanzhong == "brow":#本作品作者吴宇航
                        dakai = "brow"#本作品作者吴宇航
                        #本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "brow"#本作品作者吴宇航
#本作品作者吴宇航
                #视频播放器#本作品作者吴宇航
                if mouseRect.colliderect(videoRect):#本作品作者吴宇航
                    if xuanzhong == "video":#本作品作者吴宇航
                        dakai = "video"#本作品作者吴宇航
                        #本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "video"#本作品作者吴宇航
#本作品作者吴宇航
                #记事本#本作品作者吴宇航
                if mouseRect.colliderect(txtRect):#本作品作者吴宇航
                    if xuanzhong == "txt":#本作品作者吴宇航
                        dakai = "txt"#本作品作者吴宇航
                        #本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "txt"#本作品作者吴宇航
#本作品作者吴宇航
                #绘画板#本作品作者吴宇航
                if mouseRect.colliderect(drawsRect):#本作品作者吴宇航
                    if xuanzhong == "draws":#本作品作者吴宇航
                        dakai = "draws"#本作品作者吴宇航
                        #本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "draws"#本作品作者吴宇航
#本作品作者吴宇航
                #图片查看器#本作品作者吴宇航
                if mouseRect.colliderect(photoRect):#本作品作者吴宇航
                    if xuanzhong == "photo":#本作品作者吴宇航
                        dakai = "photo"#本作品作者吴宇航
                        #本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "photo"#本作品作者吴宇航
#本作品作者吴宇航
                #计算器#本作品作者吴宇航
                if mouseRect.colliderect(jisuansRect):#本作品作者吴宇航
                    if xuanzhong == "jisuans":#本作品作者吴宇航
                        dakai = "jisuans"#本作品作者吴宇航
                        #本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "jisuans"#本作品作者吴宇航
#本作品作者吴宇航
                #数学计算工具#本作品作者吴宇航
                if mouseRect.colliderect(shuxuesRect):#本作品作者吴宇航
                    if xuanzhong == "shuxues":#本作品作者吴宇航
                        dakai = "shuxues"#本作品作者吴宇航
                        #本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "shuxues"#本作品作者吴宇航
#本作品作者吴宇航
                #二维码生成器#本作品作者吴宇航
                if mouseRect.colliderect(ermRect):#本作品作者吴宇航
                    if xuanzhong == "erm":#本作品作者吴宇航
                        dakai = "erm"#本作品作者吴宇航
                        #本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "erm"#本作品作者吴宇航
#本作品作者吴宇航
                #翻译器#本作品作者吴宇航
                if mouseRect.colliderect(fanyiRect):#本作品作者吴宇航
                    if xuanzhong == "fanyi":#本作品作者吴宇航
                        dakai = "fanyi"#本作品作者吴宇航
                        #本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "fanyi"#本作品作者吴宇航
#本作品作者吴宇航
                #天气预报#本作品作者吴宇航
                if mouseRect.colliderect(tianqiRect):#本作品作者吴宇航
                    if xuanzhong == "tianqi":#本作品作者吴宇航
                        dakai = "tianqi"#本作品作者吴宇航
                        #本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "tianqi"#本作品作者吴宇航
#本作品作者吴宇航
                #短信发送器#本作品作者吴宇航
                if mouseRect.colliderect(duanxinRect):#本作品作者吴宇航
                    if xuanzhong == "duanxin":#本作品作者吴宇航
                        dakai = "duanxin"#本作品作者吴宇航
                        #本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "duanxin"#本作品作者吴宇航
#本作品作者吴宇航
                #新闻查看器#本作品作者吴宇航
                if mouseRect.colliderect(newsRect):#本作品作者吴宇航
                    if xuanzhong == "news":#本作品作者吴宇航
                        dakai = "news"#本作品作者吴宇航
                        #本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "news"#本作品作者吴宇航
#本作品作者吴宇航
                #文件整理器#本作品作者吴宇航
                if mouseRect.colliderect(zhengRect):#本作品作者吴宇航
                    if xuanzhong == "zheng":#本作品作者吴宇航
                        dakai = "zheng"#本作品作者吴宇航
                        #本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "zheng"#本作品作者吴宇航
#本作品作者吴宇航
                #奥运会结果#本作品作者吴宇航
                if mouseRect.colliderect(aoyunRect):#本作品作者吴宇航
                    if xuanzhong == "aoyun":#本作品作者吴宇航
                        dakai = "aoyun"#本作品作者吴宇航
                        #本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "aoyun"#本作品作者吴宇航
#本作品作者吴宇航
                #谷歌小恐龙#本作品作者吴宇航
                if mouseRect.colliderect(konglongRect):#本作品作者吴宇航
                    if xuanzhong == "konglong":#本作品作者吴宇航
                        dakai = "konglong"#本作品作者吴宇航
                        #本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "konglong"#本作品作者吴宇航
#本作品作者吴宇航
                #我的世界#本作品作者吴宇航
                if mouseRect.colliderect(mincRect):#本作品作者吴宇航
                    if xuanzhong == "minc":#本作品作者吴宇航
                        dakai = "minc"#本作品作者吴宇航
                        #本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "minc"#本作品作者吴宇航
#本作品作者吴宇航
                #cmd命令行#本作品作者吴宇航
                if mouseRect.colliderect(cmdRect):#本作品作者吴宇航
                    if xuanzhong == "cmd":#本作品作者吴宇航
                        dakai = "cmd"#本作品作者吴宇航
                        #本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "cmd"#本作品作者吴宇航
#本作品作者吴宇航
                #飞机大战#本作品作者吴宇航
                if mouseRect.colliderect(planeRect):#本作品作者吴宇航
                    if xuanzhong == "plane":#本作品作者吴宇航
                        dakai = "plane"#本作品作者吴宇航
                        #本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "plane"#本作品作者吴宇航
#本作品作者吴宇航
                #超级玛丽#本作品作者吴宇航
                if mouseRect.colliderect(maryRect):#本作品作者吴宇航
                    if xuanzhong == "mary":#本作品作者吴宇航
                        dakai = "mary"#本作品作者吴宇航
                        #本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "mary"#本作品作者吴宇航
#本作品作者吴宇航
                #2048游戏#本作品作者吴宇航
                if mouseRect.colliderect(erbRect):#本作品作者吴宇航
                    if xuanzhong == "erb":#本作品作者吴宇航
                        dakai = "erb"#本作品作者吴宇航
                        #本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "erb"#本作品作者吴宇航
#本作品作者吴宇航
                #扫雷游戏#本作品作者吴宇航
                if mouseRect.colliderect(saoRect):#本作品作者吴宇航
                    if xuanzhong == "sao":#本作品作者吴宇航
                        dakai = "sao"#本作品作者吴宇航
                        #本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "sao"#本作品作者吴宇航
                #图片处理器#本作品作者吴宇航
                if mouseRect.colliderect(psRect):#本作品作者吴宇航
                    if xuanzhong == "ps":#本作品作者吴宇航
                        dakai = "ps"#本作品作者吴宇航
                        #本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "ps"#本作品作者吴宇航
                #本作品作者吴宇航
                #任务栏打开#本作品作者吴宇航
#本作品作者吴宇航
                #文件#本作品作者吴宇航
                if mouseRect.colliderect(wenjianRect):#本作品作者吴宇航
                    dakai = "file"#本作品作者吴宇航
#本作品作者吴宇航
                #浏览器#本作品作者吴宇航
                if mouseRect.colliderect(liulanRect):#本作品作者吴宇航
                    dakai = "brow"#本作品作者吴宇航
#本作品作者吴宇航
                #设置#本作品作者吴宇航
                if mouseRect.colliderect(shezhiRect):#本作品作者吴宇航
                    dakai = "com"#本作品作者吴宇航
#本作品作者吴宇航
                #资讯#本作品作者吴宇航
                if mouseRect.colliderect(zixunRect):#本作品作者吴宇航
                    dakai = "news"#本作品作者吴宇航
#本作品作者吴宇航
                #搜索#本作品作者吴宇航
                if mouseRect.colliderect(souRect):#本作品作者吴宇航
                    dakai = "sousuo"#本作品作者吴宇航
                    
                
#本作品作者吴宇航
            #本作品作者吴宇航
            #任务栏图标检测#本作品作者吴宇航
#本作品作者吴宇航
            #开始键    #本作品作者吴宇航
            if mouseRect.colliderect(offRect):#本作品作者吴宇航
                offs = "windows11.png"#本作品作者吴宇航
            else:#本作品作者吴宇航
                offs = "win11.png"#本作品作者吴宇航
#本作品作者吴宇航
            #搜索键#本作品作者吴宇航
            if mouseRect.colliderect(souRect):#本作品作者吴宇航
                sous = "搜索2.png"#本作品作者吴宇航
            else:#本作品作者吴宇航
                sous = "搜索.png"#本作品作者吴宇航
#本作品作者吴宇航
            #资讯键#本作品作者吴宇航
            if mouseRect.colliderect(zixunRect):#本作品作者吴宇航
                zixuns = "资讯2.png"#本作品作者吴宇航
            else:#本作品作者吴宇航
                zixuns = "资讯.png"#本作品作者吴宇航
#本作品作者吴宇航
            #设置键#本作品作者吴宇航
            if mouseRect.colliderect(shezhiRect):#本作品作者吴宇航
                shezhis = "设置2.png"#本作品作者吴宇航
            else:#本作品作者吴宇航
                shezhis = "设置.png"#本作品作者吴宇航
#本作品作者吴宇航
            #此电脑键#本作品作者吴宇航
            if mouseRect.colliderect(wenjianRect):#本作品作者吴宇航
                wenjians = "文件2.png"#本作品作者吴宇航
            else:#本作品作者吴宇航
                wenjians = "文件.png"#本作品作者吴宇航
#本作品作者吴宇航
            #浏览器键#本作品作者吴宇航
            if mouseRect.colliderect(liulanRect):#本作品作者吴宇航
                liulans = "浏览2.png"#本作品作者吴宇航
            else:#本作品作者吴宇航
                liulans = "浏览.png"#本作品作者吴宇航
#本作品作者吴宇航
            #商店键#本作品作者吴宇航
            if mouseRect.colliderect(shangdianRect) :#本作品作者吴宇航
                shangdians = "商店2.png"#本作品作者吴宇航
            else:#本作品作者吴宇航
                shangdians = "商店.png"#本作品作者吴宇航
#本作品作者吴宇航
        #任务执行#本作品作者吴宇航
#本作品作者吴宇航
        #退出检测循环#本作品作者吴宇航
        if dakai != None:#本作品作者吴宇航
            pygame.quit()#本作品作者吴宇航
            break#本作品作者吴宇航
#本作品作者吴宇航
        #绘制背景#本作品作者吴宇航
        screen.fill((255,255,255))#本作品作者吴宇航
        screen.blit(bg,(0,0))#本作品作者吴宇航
        #本作品作者吴宇航
        #任务栏图标设置#本作品作者吴宇航
        off = pygame.transform.scale(pygame.image.load(offs),(80,60))#本作品作者吴宇航
        sou = pygame.transform.scale(pygame.image.load(sous),(60,60))#本作品作者吴宇航
        zixun = pygame.transform.scale(pygame.image.load(zixuns),(60,60))#本作品作者吴宇航
        shezhi = pygame.transform.scale(pygame.image.load(shezhis),(60,60))#本作品作者吴宇航
        wenjian = pygame.transform.scale(pygame.image.load(wenjians),(60,60))#本作品作者吴宇航
        liulan = pygame.transform.scale(pygame.image.load(liulans),(60,60))#本作品作者吴宇航
        shangdian = pygame.transform.scale(pygame.image.load(shangdians),(60,60))#本作品作者吴宇航
#本作品作者吴宇航
        #工具栏图标绘制#本作品作者吴宇航
        screen.blit(dianliang,(970,710))#本作品作者吴宇航
        screen.blit(shengyin,(1030,710))#本作品作者吴宇航
        screen.blit(wangluo,(1080,710))#本作品作者吴宇航
#本作品作者吴宇航
        #任务栏图标绘制#本作品作者吴宇航
        screen.blit(caidan,(0,710))#本作品作者吴宇航
        screen.blit(off,(300,710))#本作品作者吴宇航
        screen.blit(sou,(375,710))#本作品作者吴宇航
        screen.blit(zixun,(435,710))#本作品作者吴宇航
        screen.blit(shezhi,(495,710))#本作品作者吴宇航
        screen.blit(wenjian,(555,710))#本作品作者吴宇航
        screen.blit(liulan,(615,710))#本作品作者吴宇航
        screen.blit(shangdian,(675,710))#本作品作者吴宇航
#本作品作者吴宇航
        #应用图标绘制#本作品作者吴宇航
#本作品作者吴宇航
        #文件管理器#本作品作者吴宇航
#本作品作者吴宇航
        #图片#本作品作者吴宇航
        screen.blit(file,(30,20))#本作品作者吴宇航
        #文字#本作品作者吴宇航
        screen.blit(fileText,(25,70))#本作品作者吴宇航
#本作品作者吴宇航
        #音乐播放器#本作品作者吴宇航
        screen.blit(music,(105,20))#本作品作者吴宇航
        screen.blit(musicText,(105,70))#本作品作者吴宇航
#本作品作者吴宇航
        #VS Code编辑器#本作品作者吴宇航
        screen.blit(vs,(180,20))#本作品作者吴宇航
        screen.blit(vsText,(185,70))#本作品作者吴宇航
#本作品作者吴宇航
        #此电脑设置#本作品作者吴宇航
        screen.blit(com,(255,20))#本作品作者吴宇航
        screen.blit(comText,(255,70))#本作品作者吴宇航
#本作品作者吴宇航
        #浏览器#本作品作者吴宇航
        screen.blit(brow,(320,20))#本作品作者吴宇航
        screen.blit(browText,(320,70))#本作品作者吴宇航
#本作品作者吴宇航
        #视频播放器#本作品作者吴宇航
        screen.blit(video,(395,20))#本作品作者吴宇航
        screen.blit(videoText,(385,70))#本作品作者吴宇航
#本作品作者吴宇航
        #记事本#本作品作者吴宇航
        screen.blit(txt,(470,20))#本作品作者吴宇航
        screen.blit(txtText,(470,70))#本作品作者吴宇航
#本作品作者吴宇航
        #绘画板#本作品作者吴宇航
        screen.blit(draws,(545,20))#本作品作者吴宇航
        screen.blit(drawsText,(545,70))#本作品作者吴宇航
#本作品作者吴宇航
        #图片查看器#本作品作者吴宇航
        screen.blit(photo,(620,20))#本作品作者吴宇航
        screen.blit(photoText,(610,70))#本作品作者吴宇航
#本作品作者吴宇航
        #计算器#本作品作者吴宇航
        screen.blit(jisuans,(695,20))#本作品作者吴宇航
        screen.blit(jisuansText,(695,70))#本作品作者吴宇航
#本作品作者吴宇航
        #数学计算工具#本作品作者吴宇航
        screen.blit(shuxues,(770,20))#本作品作者吴宇航
        screen.blit(shuxuesText,(755,70))#本作品作者吴宇航
#本作品作者吴宇航
        #二维码生成器#本作品作者吴宇航
        screen.blit(erm,(845,20))#本作品作者吴宇航
        screen.blit(ermText,(850,70))#本作品作者吴宇航
#本作品作者吴宇航
        #翻译器#本作品作者吴宇航
        screen.blit(fanyi,(920,20))#本作品作者吴宇航
        screen.blit(fanyiText,(925,70))#本作品作者吴宇航
#本作品作者吴宇航
        #天气预报#本作品作者吴宇航
        screen.blit(tianqi,(995,20))#本作品作者吴宇航
        screen.blit(tianqiText,(995,70))#本作品作者吴宇航
#本作品作者吴宇航
        #短信发送器#本作品作者吴宇航
        screen.blit(duanxin,(1070,20))#本作品作者吴宇航
        screen.blit(duanxinText,(1070,70))#本作品作者吴宇航
#本作品作者吴宇航
        #新闻查看器#本作品作者吴宇航
        screen.blit(news,(30,95))#本作品作者吴宇航
        screen.blit(newsText,(20,145))#本作品作者吴宇航
#本作品作者吴宇航
        #文件整理器#本作品作者吴宇航
        screen.blit(zheng,(105,95))#本作品作者吴宇航
        screen.blit(zhengText,(95,145))#本作品作者吴宇航
#本作品作者吴宇航
        #奥运会结果#本作品作者吴宇航
        screen.blit(aoyun,(180,95))#本作品作者吴宇航
        screen.blit(aoyunText,(175,145))#本作品作者吴宇航
#本作品作者吴宇航
        #谷歌小恐龙#本作品作者吴宇航
        screen.blit(konglong,(255,95))#本作品作者吴宇航
        screen.blit(konglongText,(250,145))#本作品作者吴宇航
#本作品作者吴宇航
        #我的世界#本作品作者吴宇航
        screen.blit(minc,(330,95))#本作品作者吴宇航
        screen.blit(mincText,(330,145))#本作品作者吴宇航
#本作品作者吴宇航
        #cmd命令行#本作品作者吴宇航
        screen.blit(cmd,(405,95))#本作品作者吴宇航
        screen.blit(cmdText,(400,145))#本作品作者吴宇航
#本作品作者吴宇航
        #飞机大战#本作品作者吴宇航
        screen.blit(plane,(480,95))#本作品作者吴宇航
        screen.blit(planeText,(480,145))#本作品作者吴宇航
#本作品作者吴宇航
        #超级玛丽#本作品作者吴宇航
        screen.blit(mary,(555,95))#本作品作者吴宇航
        screen.blit(maryText,(555,145))#本作品作者吴宇航
#本作品作者吴宇航
        #2048游戏#本作品作者吴宇航
        screen.blit(erb,(630,95))#本作品作者吴宇航
        screen.blit(erbText,(630,145))#本作品作者吴宇航
#本作品作者吴宇航
        #扫雷游戏#本作品作者吴宇航
        screen.blit(sao,(705,95))#本作品作者吴宇航
        screen.blit(saoText,(705,145))#本作品作者吴宇航
#本作品作者吴宇航
        #图片处理器#本作品作者吴宇航
        screen.blit(ps,(780,95))#本作品作者吴宇航
        screen.blit(psText,(780,145))#本作品作者吴宇航
        #本作品作者吴宇航
        #更新屏幕#本作品作者吴宇航
        mouseRect.center = (pygame.mouse.get_pos())#本作品作者吴宇航
        pygame.display.update()#本作品作者吴宇航
#本作品作者吴宇航
    #应用判断打开#本作品作者吴宇航
#本作品作者吴宇航
    #文件管理器#本作品作者吴宇航
    if dakai == "file":#本作品作者吴宇航
        #打开函数#本作品作者吴宇航
        files1()#本作品作者吴宇航
        #返回主页#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
#本作品作者吴宇航
    #音乐播放器#本作品作者吴宇航
    elif dakai == "music":#本作品作者吴宇航
        musics()#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
#本作品作者吴宇航
    #Vs Code编辑器#本作品作者吴宇航
    elif dakai == "vs":#本作品作者吴宇航
        codes()#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
#本作品作者吴宇航
    #此电脑设置#本作品作者吴宇航
    elif dakai == "com":#本作品作者吴宇航
        sysset()#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
#本作品作者吴宇航
    #浏览器#本作品作者吴宇航
    elif dakai == "brow":#本作品作者吴宇航
        browsers()#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
#本作品作者吴宇航
    #视频播放器#本作品作者吴宇航
    elif dakai == "video":#本作品作者吴宇航
        videos()#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
#本作品作者吴宇航
    #记事本#本作品作者吴宇航
    elif dakai == "txt":#本作品作者吴宇航
        notebook()#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
#本作品作者吴宇航
    #绘画板#本作品作者吴宇航
    elif dakai == "draws":#本作品作者吴宇航
        huihua()#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
#本作品作者吴宇航
    #图片查看器#本作品作者吴宇航
    elif dakai == "photo":#本作品作者吴宇航
        photos()#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
#本作品作者吴宇航
    #计算器#本作品作者吴宇航
    elif dakai == "jisuans":#本作品作者吴宇航
        jisuan()#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
#本作品作者吴宇航
    #数学计算工具#本作品作者吴宇航
    elif dakai == "shuxues":#本作品作者吴宇航
        shuxue()#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
#本作品作者吴宇航
    #二维码生成器#本作品作者吴宇航
    elif dakai == "erm":#本作品作者吴宇航
        # erma()#本作品作者吴宇航
        messagebox.showinfo("提示","该功能暂未开放")#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
#本作品作者吴宇航
    #翻译器#本作品作者吴宇航
    elif dakai == "fanyi":#本作品作者吴宇航
        translate()#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
#本作品作者吴宇航
    #天气预报#本作品作者吴宇航
    elif dakai == "tianqi":#本作品作者吴宇航
        temp()#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
#本作品作者吴宇航
    #短信发送器#本作品作者吴宇航
    elif dakai == "duanxin":#本作品作者吴宇航
        smstool()#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
#本作品作者吴宇航
    #新闻查看器#本作品作者吴宇航
    elif dakai == "news":#本作品作者吴宇航
        xinwen()#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
#本作品作者吴宇航
    #文件整理器#本作品作者吴宇航
    elif dakai == "zheng":#本作品作者吴宇航
        # zhengli()#本作品作者吴宇航
        messagebox.showinfo("提示","该功能尚未开放")#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
#本作品作者吴宇航
    #奥运结果#本作品作者吴宇航
    elif dakai == "aoyun":#本作品作者吴宇航
        aoyunhui()#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
#本作品作者吴宇航
    #谷歌小恐龙#本作品作者吴宇航
    elif dakai == "konglong":#本作品作者吴宇航
        dino()#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
#本作品作者吴宇航
    #我的世界#本作品作者吴宇航
    elif dakai == "minc":#本作品作者吴宇航
        mink()#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
#本作品作者吴宇航
    #搜索导航#本作品作者吴宇航
    elif dakai == "sousuo":#本作品作者吴宇航
        sousou()#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
#本作品作者吴宇航
    #命令行界面#本作品作者吴宇航
    elif dakai == "cmd":#本作品作者吴宇航
        cmds()#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
#本作品作者吴宇航
    #飞机大战#本作品作者吴宇航
    elif dakai == "plane":#本作品作者吴宇航
        feiji()#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
#本作品作者吴宇航
    #超级玛丽#本作品作者吴宇航
    elif dakai == "mary":#本作品作者吴宇航
        # mali()#本作品作者吴宇航
        messagebox.showinfo("提示","该功能尚未开放")#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
#本作品作者吴宇航
    #2048游戏#本作品作者吴宇航
    elif dakai == "erb":#本作品作者吴宇航
        erba()#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
#本作品作者吴宇航
    #扫雷#本作品作者吴宇航
    elif dakai == "sao":#本作品作者吴宇航
        saolei()#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
#本作品作者吴宇航
    #扫雷#本作品作者吴宇航
    elif dakai == "ps":#本作品作者吴宇航
        photoshop()#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
#本作品作者吴宇航
fasdasdf1()#本作品作者吴宇航
