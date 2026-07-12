#!/usr/bin/python#本作品作者吴宇航
# -*- coding: utf-8 -*-#本作品作者吴宇航
from __future__ import division#本作品作者吴宇航
import pygame,sys,random,time,turtle#本作品作者吴宇航
import math#本作品作者吴宇航
from wx import *#本作品作者吴宇航
import os#本作品作者吴宇航
import time#本作品作者吴宇航
import sys#本作品作者吴宇航
#本作品作者吴宇航
import requests#本作品作者吴宇航
import json#本作品作者吴宇航
from copy import *#本作品作者吴宇航
from tkinter.ttk import Button,Entry,Radiobutton,Scrollbar#本作品作者吴宇航
from tkinter import END,Label,Tk,StringVar,Listbox,messagebox,SINGLE,PhotoImage#本作品作者吴宇航
"""#本作品作者吴宇航
VIP视频解析：http://www.vipjiexi.com/#本作品作者吴宇航
无名小站：http://www.wmxz.wang/#本作品作者吴宇航
http://www.iqiyi.com/lib/dianying/%E5%96%9C%E5%89%A7,%E4%B8%AD%E5%9B%BD%E5%A4%A7%E9%99%86,2018_11_1.html#本作品作者吴宇航
"""#本作品作者吴宇航
from moviepy.editor import *#本作品作者吴宇航
import pyglet#本作品作者吴宇航
from pyglet.media import *#本作品作者吴宇航
import requests#本作品作者吴宇航
import re#本作品作者吴宇航
import os#本作品作者吴宇航
from lxml import etree#本作品作者吴宇航
from  selenium import webdriver#本作品作者吴宇航
import wx#本作品作者吴宇航
import wx.html2#本作品作者吴宇航
import webbrowser#本作品作者吴宇航
from PIL import Image,ImageTk#本作品作者吴宇航
import io#本作品作者吴宇航
import re#本作品作者吴宇航
import requests#本作品作者吴宇航
import tkinter as tk#本作品作者吴宇航
import sys#本作品作者吴宇航
from PyQt5.QtWidgets import (QWidget, QDesktopWidget,#本作品作者吴宇航
    QMessageBox, QHBoxLayout, QVBoxLayout, QSlider, QListWidget,#本作品作者吴宇航
    QPushButton, QLabel, QComboBox, QFileDialog)#本作品作者吴宇航
from PyQt5.QtGui import QIcon#本作品作者吴宇航
from PyQt5.QtCore import Qt, QUrl, QTimer#本作品作者吴宇航
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent#本作品作者吴宇航
import os, time#本作品作者吴宇航
import configparser#本作品作者吴宇航
from PIL import Image, ImageTk#本作品作者吴宇航
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
import re#本作品作者吴宇航
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
pygame.init()#本作品作者吴宇航
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
from datetime import*#本作品作者吴宇航
from win10toast import ToastNotifier#本作品作者吴宇航
class ErrorAction(ToastNotifier):#本作品作者吴宇航
    def __init__(self,text = ''):#本作品作者吴宇航
        super().__init__()#本作品作者吴宇航
        self.show_toast(title="Error!", msg=text,#本作品作者吴宇航
                        duration=2)#本作品作者吴宇航
                        #本作品作者吴宇航
class InfoAction(ToastNotifier):#本作品作者吴宇航
    def __init__(self,title = '嘿,有一个事情',text = ''):#本作品作者吴宇航
        super().__init__()#本作品作者吴宇航
        self.show_toast(title=title, msg=text,#本作品作者吴宇航
                        duration=2)#本作品作者吴宇航
                        #本作品作者吴宇航
class AskAction(ToastNotifier):#本作品作者吴宇航
    def __init__(self,title = '嘿,有一个问题',text = ''):#本作品作者吴宇航
        super().__init__()#本作品作者吴宇航
        self.show_toast(title=title, msg=text,#本作品作者吴宇航
                        duration=2)#本作品作者吴宇航
from MBPython import miniblink#本作品作者吴宇航
from pygame.locals import QUIT, KEYDOWN#本作品作者吴宇航
if (sys.version_info > (3, 0)):#本作品作者吴宇航
    from tkinter import *#本作品作者吴宇航
    from tkinter import messagebox#本作品作者吴宇航
else:#本作品作者吴宇航
    from Tkinter import *#本作品作者吴宇航
import wx,tkinter#本作品作者吴宇航
from wx import *#本作品作者吴宇航
import time#本作品作者吴宇航
import math#本作品作者吴宇航
from math import *#本作品作者吴宇航
global dakai,xuanzhong#本作品作者吴宇航
kaishijian = "win10开始键.png"#本作品作者吴宇航
applist = ["浏览器","计算器","画图器(未开放)","聊天机器人","BMI检测(未开放)","五子棋","我的世界","贪吃蛇","俄罗斯方块","2048游戏(未开放)","数字华容道","数独游戏","沙盘游戏","Flappy Bird","绘画板","记事本","代码编辑器","音乐播放器","小球打砖块","设置(未开放)","迷宫游戏(未开放)","打字游戏","此电脑文件(未开放)","视频播放器(未开放)"]#本作品作者吴宇航
dakailist = ["setting","chrome","jisuan","huatu","qq","bmi","off","wuziqi","minecraft","snake","eluosi","twofour","huarong","shudu","shapan","flybird","huihua","wenben","code","music"]#本作品作者吴宇航
mousex, mousey = pygame.mouse.get_pos()#本作品作者吴宇航
mouseRect = pygame.Rect(mousex,mousey,5,5)#本作品作者吴宇航
settingRect = pygame.Rect(50,25,50,50)#本作品作者吴宇航
chromeRect = pygame.Rect(125,25,50,50)#本作品作者吴宇航
jisuanRect = pygame.Rect(200,25,50,50)#本作品作者吴宇航
musicRect = pygame.Rect(275,25,50,50)#本作品作者吴宇航
qqRect = pygame.Rect(350,25,50,50)#本作品作者吴宇航
offRect = pygame.Rect(0,710,60,60)#本作品作者吴宇航
codeRect = pygame.Rect(425,25,50,50)#本作品作者吴宇航
wuziqiRect = pygame.Rect(500,25,50,50)#本作品作者吴宇航
minecraftRect = pygame.Rect(575,25,50,50)#本作品作者吴宇航
snakeRect = pygame.Rect(650,25,50,50)#本作品作者吴宇航
eluosiRect = pygame.Rect(725,25,50,50)#本作品作者吴宇航
daziRect = pygame.Rect(800,25,50,50)#本作品作者吴宇航
huarongRect = pygame.Rect(875,25,50,50)#本作品作者吴宇航
shuduRect = pygame.Rect(950,25,50,50)#本作品作者吴宇航
shapanRect = pygame.Rect(50,100,50,50)#本作品作者吴宇航
flybirdRect = pygame.Rect(125,100,50,50)#本作品作者吴宇航
huihuaRect = pygame.Rect(200,100,50,50)#本作品作者吴宇航
wenbenRect = pygame.Rect(275,100,50,50)#本作品作者吴宇航
huatuRect = pygame.Rect(350,100,50,50)#本作品作者吴宇航
xiaoqiuRect = pygame.Rect(425,100,50,50)#本作品作者吴宇航
migongRect = pygame.Rect(500,100,50,50)#本作品作者吴宇航
shipinRect = pygame.Rect(575,100,50,50)#本作品作者吴宇航
mofangRect = pygame.Rect(650,100,50,50)#本作品作者吴宇航
twofourRect = pygame.Rect(725,100,50,50)#本作品作者吴宇航
tuixiangRect = pygame.Rect(800,100,50,50)#本作品作者吴宇航
chidouRect = pygame.Rect(875,100,50,50)#本作品作者吴宇航
golfRect = pygame.Rect(950,100,50,50)#本作品作者吴宇航
paokuRect = pygame.Rect(50,175,50,50)#本作品作者吴宇航
saoleiRect = pygame.Rect(125,175,50,50)#本作品作者吴宇航
saicheRect = pygame.Rect(200,175,50,50)#本作品作者吴宇航
dongwuRect = pygame.Rect(275,175,50,50)#本作品作者吴宇航
fanpaiRect = pygame.Rect(350,175,50,50)#本作品作者吴宇航
qiangzhanRect = pygame.Rect(425,175,50,50)#本作品作者吴宇航
tafangRect = pygame.Rect(500,175,50,50)#本作品作者吴宇航
tailaRect = pygame.Rect(575,175,50,50)#本作品作者吴宇航
baoweiRect = pygame.Rect(650,175,50,50)#本作品作者吴宇航
renzheRect = pygame.Rect(725,175,50,50)#本作品作者吴宇航
feijiRect = pygame.Rect(800,175,50,50)#本作品作者吴宇航
secaiRect = pygame.Rect(875,175,50,50)#本作品作者吴宇航
hepingRect = pygame.Rect(950,175,50,50)#本作品作者吴宇航
wangzheRect = pygame.Rect(50,250,50,50)#本作品作者吴宇航
shijianRect = pygame.Rect(800,710,60,60)#本作品作者吴宇航
cortanaRect = pygame.Rect(70,710,60,60)#本作品作者吴宇航
souRect = pygame.Rect(140,710,60,60)#本作品作者吴宇航
renwuRect = pygame.Rect(210,710,60,60)#本作品作者吴宇航
kongzhi = pygame.transform.scale(pygame.image.load("files.ico"),(50,50))#本作品作者吴宇航
chrome = pygame.transform.scale(pygame.image.load("chrome.jpeg"),(50,50))#本作品作者吴宇航
jisuan = pygame.transform.scale(pygame.image.load("计算器.jpg"),(50,50))#本作品作者吴宇航
music = pygame.transform.scale(pygame.image.load("音乐播放器.jpeg"),(50,50))#本作品作者吴宇航
bg = pygame.transform.scale(pygame.image.load("png.jpeg"),(1200,800))#本作品作者吴宇航
qq = pygame.transform.scale(pygame.image.load("聊天机器人.jpg"),(50,50))#本作品作者吴宇航
twofour = pygame.transform.scale(pygame.image.load("2048游戏.jpeg"),(50,50))#本作品作者吴宇航
code = pygame.transform.scale(pygame.image.load("icon.jpg"),(50,50))#本作品作者吴宇航
wuziqi = pygame.transform.scale(pygame.image.load("五子棋.jpeg"),(50,50))#本作品作者吴宇航
minecraft = pygame.transform.scale(pygame.image.load("我的世界.jpeg"),(50,50))#本作品作者吴宇航
snake = pygame.transform.scale(pygame.image.load("贪吃蛇.jpeg"),(50,50))#本作品作者吴宇航
eluosi = pygame.transform.scale(pygame.image.load("俄罗斯方块.jpeg"),(50,50))#本作品作者吴宇航
dazi = pygame.transform.scale(pygame.image.load("打字游戏.jpeg"),(50,50))#本作品作者吴宇航
caidan = pygame.transform.scale(pygame.image.load("菜单栏.png"),(1300,60))#本作品作者吴宇航
huarong = pygame.transform.scale(pygame.image.load("数字华容道.jpeg"),(50,50))#本作品作者吴宇航
shudu = pygame.transform.scale(pygame.image.load("数独游戏.jpeg"),(50,50))#本作品作者吴宇航
shapan = pygame.transform.scale(pygame.image.load("沙盘游戏.png"),(50,50))#本作品作者吴宇航
flybird = pygame.transform.scale(pygame.image.load("flybird.jpeg"),(50,50))#本作品作者吴宇航
huihua = pygame.transform.scale(pygame.image.load("画图.jpeg"),(50,50))#本作品作者吴宇航
wenben = pygame.transform.scale(pygame.image.load("记事本.jpeg"),(50,50))#本作品作者吴宇航
huatu = pygame.transform.scale(pygame.image.load("画图器.jpg"),(50,50))#本作品作者吴宇航
xiaoqiu = pygame.transform.scale(pygame.image.load("小球打砖块.jpeg"),(50,50))#本作品作者吴宇航
migong = pygame.transform.scale(pygame.image.load("迷宫游戏.jpg"),(50,50))#本作品作者吴宇航
shipin = pygame.transform.scale(pygame.image.load("视频播放器.jpeg"),(50,50))#本作品作者吴宇航
mofang = pygame.transform.scale(pygame.image.load("魔方游戏.jpeg"),(50,50))#本作品作者吴宇航
tuixiang = pygame.transform.scale(pygame.image.load("推箱子.jpeg"),(50,50))#本作品作者吴宇航
chidou = pygame.transform.scale(pygame.image.load("吃豆人游戏.jpeg"),(50,50))#本作品作者吴宇航
golf = pygame.transform.scale(pygame.image.load("高尔夫球游戏.png"),(50,50))#本作品作者吴宇航
paoku = pygame.transform.scale(pygame.image.load("跑酷游戏.jpeg"),(50,50))#本作品作者吴宇航
saolei = pygame.transform.scale(pygame.image.load("扫雷游戏.jpeg"),(50,50))#本作品作者吴宇航
saiche = pygame.transform.scale(pygame.image.load("赛车游戏.png"),(50,50))#本作品作者吴宇航
dongwu = pygame.transform.scale(pygame.image.load("动物棋.jpg"),(50,50))#本作品作者吴宇航
fanpai = pygame.transform.scale(pygame.image.load("翻牌.jpeg"),(50,50))#本作品作者吴宇航
qiangzhan = pygame.transform.scale(pygame.image.load("枪战游戏.jpeg"),(50,50))#本作品作者吴宇航
tafang = pygame.transform.scale(pygame.image.load("塔防游戏.jpeg"),(50,50))#本作品作者吴宇航
taila = pygame.transform.scale(pygame.image.load("泰拉瑞亚.jpeg"),(50,50))#本作品作者吴宇航
baowei = pygame.transform.scale(pygame.image.load("保卫萝卜.jpeg"),(50,50))#本作品作者吴宇航
renzhe = pygame.transform.scale(pygame.image.load("忍者游戏.jpeg"),(50,50))#本作品作者吴宇航
feiji = pygame.transform.scale(pygame.image.load("模拟飞机.jpeg"),(50,50))#本作品作者吴宇航
secai = pygame.transform.scale(pygame.image.load("色彩游戏.jpeg"),(50,50))#本作品作者吴宇航
heping = pygame.transform.scale(pygame.image.load("和平精英.jpeg"),(50,50))#本作品作者吴宇航
wangzhe = pygame.transform.scale(pygame.image.load("王者荣耀.jpeg"),(50,50))#本作品作者吴宇航
shijian = pygame.transform.scale(pygame.image.load("时钟.jpeg"),(60,60))#本作品作者吴宇航
dianliang = pygame.transform.scale(pygame.image.load("电池.png"),(60,60))#本作品作者吴宇航
shengyin = pygame.transform.scale(pygame.image.load("声音.png"),(60,60))#本作品作者吴宇航
wangluo = pygame.transform.scale(pygame.image.load("网络.png"),(60,60))#本作品作者吴宇航
myFont = pygame.font.SysFont("STzhongsong",15)#本作品作者吴宇航
kongzhiText = myFont.render("此电脑",True,(255,255,255))#本作品作者吴宇航
chromeText = myFont.render("浏览器",True,(255,255,255))#本作品作者吴宇航
jisuanText = myFont.render("计算器",True,(255,255,255))#本作品作者吴宇航
musicText = myFont.render("音乐播放器",True,(255,255,255))#本作品作者吴宇航
qqText = myFont.render("聊天机器人",True,(255,255,255))#本作品作者吴宇航
codeText = myFont.render("代码编辑器",True,(255,255,255))#本作品作者吴宇航
wuziqiText = myFont.render("五子棋",True,(255,255,255))#本作品作者吴宇航
minecraftText = myFont.render("我的世界",True,(255,255,255))#本作品作者吴宇航
snakeText = myFont.render("贪吃蛇",True,(255,255,255))#本作品作者吴宇航
eluosiText = myFont.render("俄罗斯方块",True,(255,255,255))#本作品作者吴宇航
daziText = myFont.render("打字游戏",True,(255,255,255))#本作品作者吴宇航
huarongText = myFont.render("数字华容道",True,(255,255,255))#本作品作者吴宇航
shuduText = myFont.render("数独游戏",True,(255,255,255))#本作品作者吴宇航
shapanText = myFont.render("沙盘游戏",True,(255,255,255))#本作品作者吴宇航
flybirdText = myFont.render("Flappy Bird",True,(255,255,255))#本作品作者吴宇航
huihuaText = myFont.render("绘画板",True,(255,255,255))#本作品作者吴宇航
wenbenText = myFont.render("记事本",True,(255,255,255))#本作品作者吴宇航
huatuText = myFont.render("画图器",True,(255,255,255))#本作品作者吴宇航
xiaoqiuText = myFont.render("小球打砖块",True,(255,255,255))#本作品作者吴宇航
migongText = myFont.render("迷宫游戏",True,(255,255,255))#本作品作者吴宇航
shipinText = myFont.render("视频播放器",True,(255,255,255))#本作品作者吴宇航
mofangText = myFont.render("魔方游戏",True,(255,255,255))#本作品作者吴宇航
twofourText = myFont.render("2048游戏",True,(255,255,255))#本作品作者吴宇航
tuixiangText = myFont.render("推箱子",True,(255,255,255))#本作品作者吴宇航
chidouText = myFont.render("吃豆人",True,(255,255,255))#本作品作者吴宇航
golfText = myFont.render("高尔夫球",True,(255,255,255))#本作品作者吴宇航
paokuText = myFont.render("跑酷游戏",True,(255,255,255))#本作品作者吴宇航
saoleiText = myFont.render("扫雷游戏",True,(255,255,255))#本作品作者吴宇航
saicheText = myFont.render("赛车游戏",True,(255,255,255))#本作品作者吴宇航
dongwuText = myFont.render("动物棋",True,(255,255,255))#本作品作者吴宇航
fanpaiText = myFont.render("记忆翻牌",True,(255,255,255))#本作品作者吴宇航
qiangzhanText = myFont.render("枪战游戏",True,(255,255,255))#本作品作者吴宇航
tafangText = myFont.render("塔防游戏",True,(255,255,255))#本作品作者吴宇航
tailaText = myFont.render("泰拉瑞亚",True,(255,255,255))#本作品作者吴宇航
baoweiText = myFont.render("保卫萝卜",True,(255,255,255))#本作品作者吴宇航
renzheText = myFont.render("忍者游戏",True,(255,255,255))#本作品作者吴宇航
feijiText = myFont.render("模拟飞机",True,(255,255,255))#本作品作者吴宇航
secaiText = myFont.render("色彩游戏",True,(255,255,255))#本作品作者吴宇航
hepingText = myFont.render("和平精英",True,(255,255,255))#本作品作者吴宇航
wangzheText = myFont.render("王者荣耀",True,(255,255,255))#本作品作者吴宇航
messagebox.showinfo("欢迎","尊敬的用户，您好！")#本作品作者吴宇航
messagebox.showinfo("欢迎","欢迎使用星空模拟系统(Starry Sky System,简称S.S.S模拟系统)")#本作品作者吴宇航
messagebox.showinfo("欢迎","本系统功能齐全，有各种工具与游戏供您使用。")#本作品作者吴宇航
messagebox.showinfo("欢迎","本系统不同于社区其他系统，本系统是完全以Python为脚本语言，采用了pygame、tkinter、wxpython等多种可视化工具打造的一款图形化模拟系统，而非文字系统。")#本作品作者吴宇航
messagebox.showinfo("欢迎","本系统完全仿照windows 10系统的UI图形化界面制作，带给您熟悉而方便快捷的体验。")#本作品作者吴宇航
messagebox.showinfo("欢迎","本系统虽为模拟系统，但却有许多功能与目前电脑系统有直接联系，真实与模拟的电脑系统相交融，带来真正的方便！")#本作品作者吴宇航
messagebox.showinfo("欢迎","最后，祝您使用愉快！")#本作品作者吴宇航
pygame.display.set_caption("Starry Sky System(星空系统)")#本作品作者吴宇航
clip = VideoFileClip('open.mp4')#本作品作者吴宇航
clip= clip.resize(newsize=(1280,720))#本作品作者吴宇航
clip.preview()#本作品作者吴宇航
def fasdasdf1():#本作品作者吴宇航
#本作品作者吴宇航
    global dakai,xuanzhong#本作品作者吴宇航
    xuanzhong = None#本作品作者吴宇航
    dakai = None#本作品作者吴宇航
    pygame.init()#本作品作者吴宇航
    screen = pygame.display.set_mode((1024,768))#本作品作者吴宇航
    pygame.display.set_caption("Starry Sky System(星空系统)")#本作品作者吴宇航
    # clip = VideoFileClip('open.mp4')#本作品作者吴宇航
    # clip= clip.resize(newsize=(1280,720))#本作品作者吴宇航
    # clip.preview()#本作品作者吴宇航
    #本作品作者吴宇航
    while True:#本作品作者吴宇航
        for event in pygame.event.get():#本作品作者吴宇航
            if event.type == pygame.QUIT:#本作品作者吴宇航
                if messagebox.askokcancel("是否退出", "您确定退出吗（主窗口退出将直接结束程序）"):#本作品作者吴宇航
                    sys.exit(0)#本作品作者吴宇航
            elif event.type == pygame.MOUSEBUTTONDOWN:#本作品作者吴宇航
                if mouseRect.colliderect(settingRect):#本作品作者吴宇航
                    if xuanzhong == "setting":#本作品作者吴宇航
                        dakai = "setting"#本作品作者吴宇航
                        break#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "setting"#本作品作者吴宇航
                elif mouseRect.colliderect(chromeRect):#本作品作者吴宇航
                    if xuanzhong == "chrome":#本作品作者吴宇航
                        dakai = "chrome"#本作品作者吴宇航
                        #本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "chrome"#本作品作者吴宇航
                elif mouseRect.colliderect(jisuanRect):#本作品作者吴宇航
                    if xuanzhong == "jisuan":#本作品作者吴宇航
                        dakai = "jisuan"#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "jisuan"#本作品作者吴宇航
                elif mouseRect.colliderect(qqRect):#本作品作者吴宇航
                    if xuanzhong == "qq":#本作品作者吴宇航
                        dakai = "qq"#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "qq"#本作品作者吴宇航
                elif mouseRect.colliderect(offRect):#本作品作者吴宇航
                    if xuanzhong == "off":#本作品作者吴宇航
                        dakai = "off"#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        dakai = "off"#本作品作者吴宇航
                elif mouseRect.colliderect(wuziqiRect):#本作品作者吴宇航
                    if xuanzhong == "wuziqi":#本作品作者吴宇航
                        dakai = "wuziqi"#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "wuziqi"#本作品作者吴宇航
                elif mouseRect.colliderect(minecraftRect):#本作品作者吴宇航
                    if xuanzhong == "minecraft":#本作品作者吴宇航
                        dakai = "minecraft"#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "minecraft"#本作品作者吴宇航
                elif mouseRect.colliderect(snakeRect):#本作品作者吴宇航
                    if xuanzhong == "snake":#本作品作者吴宇航
                        dakai = "snake"#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "snake"#本作品作者吴宇航
                elif mouseRect.colliderect(eluosiRect):#本作品作者吴宇航
                    if xuanzhong == "eluosi":#本作品作者吴宇航
                        dakai = "eluosi"#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "eluosi"#本作品作者吴宇航
                elif mouseRect.colliderect(daziRect):#本作品作者吴宇航
                    if xuanzhong == "dazi":#本作品作者吴宇航
                        dakai = "dazi"#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "dazi"#本作品作者吴宇航
                elif mouseRect.colliderect(huarongRect):#本作品作者吴宇航
                    if xuanzhong == "huarong":#本作品作者吴宇航
                        dakai = "huarong"#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "huarong"#本作品作者吴宇航
                elif mouseRect.colliderect(shuduRect):#本作品作者吴宇航
                    if xuanzhong == "shudu":#本作品作者吴宇航
                        dakai = "shudu"#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "shudu"#本作品作者吴宇航
                elif mouseRect.colliderect(shapanRect):#本作品作者吴宇航
                    if xuanzhong == "shapan":#本作品作者吴宇航
                        dakai = "shapan"#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "shapan"#本作品作者吴宇航
                elif mouseRect.colliderect(flybirdRect):#本作品作者吴宇航
                    if xuanzhong == "flybird":#本作品作者吴宇航
                        dakai = "flybird"#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "flybird"#本作品作者吴宇航
                elif mouseRect.colliderect(huihuaRect):#本作品作者吴宇航
                    if xuanzhong == "huihua":#本作品作者吴宇航
                        dakai = "huihua"#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "huihua"#本作品作者吴宇航
                elif mouseRect.colliderect(wenbenRect):#本作品作者吴宇航
                    if xuanzhong == "wenben":#本作品作者吴宇航
                        dakai = "wenben"#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "wenben"#本作品作者吴宇航
                elif mouseRect.colliderect(codeRect):#本作品作者吴宇航
                    if xuanzhong == "code":#本作品作者吴宇航
                        dakai = "code"#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "code"#本作品作者吴宇航
                elif mouseRect.colliderect(musicRect):#本作品作者吴宇航
                    if xuanzhong == "music":#本作品作者吴宇航
                        dakai = "music"#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "music"#本作品作者吴宇航
                elif mouseRect.colliderect(huatuRect):#本作品作者吴宇航
                    if xuanzhong == "huatu":#本作品作者吴宇航
                        dakai = "huatu"#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "huatu"#本作品作者吴宇航
                elif mouseRect.colliderect(xiaoqiuRect):#本作品作者吴宇航
                    if xuanzhong == "xiaoqiu":#本作品作者吴宇航
                        dakai = "xiaoqiu"#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "xiaoqiu"#本作品作者吴宇航
                elif mouseRect.colliderect(migongRect):#本作品作者吴宇航
                    if xuanzhong == "migong":#本作品作者吴宇航
                        dakai = "migong"#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "migong"#本作品作者吴宇航
                elif mouseRect.colliderect(shipinRect):#本作品作者吴宇航
                    if xuanzhong == "shipin":#本作品作者吴宇航
                        dakai = "shipin"#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "shipin"#本作品作者吴宇航
                elif mouseRect.colliderect(mofangRect):#本作品作者吴宇航
                    if xuanzhong == "mofang":#本作品作者吴宇航
                        dakai = "mofang"#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "mofang"#本作品作者吴宇航
                elif mouseRect.colliderect(twofourRect):#本作品作者吴宇航
                    if xuanzhong == "twofour":#本作品作者吴宇航
                        dakai = "twofour"#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "twofour"#本作品作者吴宇航
                elif mouseRect.colliderect(tuixiangRect):#本作品作者吴宇航
                    if xuanzhong == "tuixiang":#本作品作者吴宇航
                        dakai = "tuixiang"#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "tuixiang"#本作品作者吴宇航
                elif mouseRect.colliderect(chidouRect):#本作品作者吴宇航
                    if xuanzhong == "chidou":#本作品作者吴宇航
                        dakai = "chidou"#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "chidou"#本作品作者吴宇航
                elif mouseRect.colliderect(golfRect):#本作品作者吴宇航
                    if xuanzhong == "golf":#本作品作者吴宇航
                        dakai = "golf"#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "golf"#本作品作者吴宇航
                elif mouseRect.colliderect(paokuRect):#本作品作者吴宇航
                    if xuanzhong == "paoku":#本作品作者吴宇航
                        dakai = "paoku"#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "paoku"#本作品作者吴宇航
                elif mouseRect.colliderect(saoleiRect):#本作品作者吴宇航
                    if xuanzhong == "saolei":#本作品作者吴宇航
                        dakai = "saolei"#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "saolei"#本作品作者吴宇航
                elif mouseRect.colliderect(saicheRect):#本作品作者吴宇航
                    if xuanzhong == "saiche":#本作品作者吴宇航
                        dakai = "saiche"#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "saiche"#本作品作者吴宇航
                elif mouseRect.colliderect(dongwuRect):#本作品作者吴宇航
                    if xuanzhong == "dongwu":#本作品作者吴宇航
                        dakai = "dongwu"#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "dongwu"#本作品作者吴宇航
                elif mouseRect.colliderect(fanpaiRect):#本作品作者吴宇航
                    if xuanzhong == "fanpai":#本作品作者吴宇航
                        dakai = "fanpai"#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "fanpai"#本作品作者吴宇航
                elif mouseRect.colliderect(qiangzhanRect):#本作品作者吴宇航
                    if xuanzhong == "qiangzhan":#本作品作者吴宇航
                        dakai = "qiangzhan"#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "qiangzhan"#本作品作者吴宇航
                elif mouseRect.colliderect(tafangRect):#本作品作者吴宇航
                    if xuanzhong == "tafang":#本作品作者吴宇航
                        dakai = "tafang"#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "tafang"#本作品作者吴宇航
                elif mouseRect.colliderect(tailaRect):#本作品作者吴宇航
                    if xuanzhong == "taila":#本作品作者吴宇航
                        dakai = "taila"#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "taila"#本作品作者吴宇航
                elif mouseRect.colliderect(baoweiRect):#本作品作者吴宇航
                    if xuanzhong == "baowei":#本作品作者吴宇航
                        dakai = "baowei"#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "baowei"#本作品作者吴宇航
                elif mouseRect.colliderect(renzheRect):#本作品作者吴宇航
                    if xuanzhong == "renzhe":#本作品作者吴宇航
                        dakai = "renzhe"#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "renzhe"#本作品作者吴宇航
                elif mouseRect.colliderect(feijiRect):#本作品作者吴宇航
                    if xuanzhong == "feiji":#本作品作者吴宇航
                        dakai = "feiji"#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "feiji"#本作品作者吴宇航
                elif mouseRect.colliderect(hepingRect):#本作品作者吴宇航
                    if xuanzhong == "heping":#本作品作者吴宇航
                        dakai = "heping"#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "heping"#本作品作者吴宇航
                elif mouseRect.colliderect(secaiRect):#本作品作者吴宇航
                    if xuanzhong == "secai":#本作品作者吴宇航
                        dakai = "secai"#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "secai"#本作品作者吴宇航
                elif mouseRect.colliderect(wangzheRect):#本作品作者吴宇航
                    if xuanzhong == "wangzhe":#本作品作者吴宇航
                        dakai = "wangzhe"#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        xuanzhong = "wangzhe"#本作品作者吴宇航
                elif mouseRect.colliderect(shijianRect):#本作品作者吴宇航
                    dakai = "shijian"#本作品作者吴宇航
                elif mouseRect.colliderect(cortanaRect):#本作品作者吴宇航
                    dakai = "cortana" #本作品作者吴宇航
            if mouseRect.colliderect(offRect) and not(event.type == pygame.MOUSEBUTTONDOWN):#本作品作者吴宇航
                kaishijian = "windows10.png"#本作品作者吴宇航
            else:#本作品作者吴宇航
                kaishijian = "win10开始键.png"#本作品作者吴宇航
            if mouseRect.colliderect(cortanaRect) and not(event.type == pygame.MOUSEBUTTONDOWN):#本作品作者吴宇航
                cortanajian = "cortana1.png"#本作品作者吴宇航
            else:#本作品作者吴宇航
                cortanajian = "cortana.png"#本作品作者吴宇航
            if mouseRect.colliderect(souRect) and not(event.type == pygame.MOUSEBUTTONDOWN):#本作品作者吴宇航
                soujian = "sou1.png"#本作品作者吴宇航
            else:#本作品作者吴宇航
                soujian = "sou.png"#本作品作者吴宇航
            if mouseRect.colliderect(renwuRect) and not(event.type == pygame.MOUSEBUTTONDOWN):#本作品作者吴宇航
                renwujian = "任务视图1.png"#本作品作者吴宇航
            else:#本作品作者吴宇航
                renwujian = "任务视图.png"#本作品作者吴宇航
        if dakai != None:#本作品作者吴宇航
            pygame.quit()#本作品作者吴宇航
            break#本作品作者吴宇航
        screen.fill((255,255,255))#本作品作者吴宇航
        screen.blit(bg,(0,0))#本作品作者吴宇航
        screen.blit(kongzhi,(50,25))#本作品作者吴宇航
        screen.blit(kongzhiText,(60,75))#本作品作者吴宇航
        screen.blit(chrome,(125,25))#本作品作者吴宇航
        screen.blit(chromeText,(125,75))#本作品作者吴宇航
        screen.blit(jisuan,(200,25))#本作品作者吴宇航
        screen.blit(jisuanText,(200,75))#本作品作者吴宇航
        screen.blit(music,(275,25))#本作品作者吴宇航
        screen.blit(musicText,(260,75))#本作品作者吴宇航
        screen.blit(qq, (350, 25))#本作品作者吴宇航
        screen.blit(qqText, (340, 75))#本作品作者吴宇航
        screen.blit(code,(425,25))#本作品作者吴宇航
        screen.blit(codeText,(418,75))#本作品作者吴宇航
        screen.blit(wuziqi,(500,25))#本作品作者吴宇航
        screen.blit(wuziqiText,(500,75))#本作品作者吴宇航
        screen.blit(minecraft,(575,25))#本作品作者吴宇航
        screen.blit(minecraftText,(575,75))#本作品作者吴宇航
        screen.blit(snake,(650,25))#本作品作者吴宇航
        screen.blit(snakeText,(650,75))#本作品作者吴宇航
        screen.blit(eluosi,(725,25))#本作品作者吴宇航
        screen.blit(eluosiText,(710,75))#本作品作者吴宇航
        screen.blit(dazi,(800,25))#本作品作者吴宇航
        screen.blit(daziText,(790,75))#本作品作者吴宇航
        screen.blit(huarong,(875,25))#本作品作者吴宇航
        screen.blit(huarongText,(860,75))#本作品作者吴宇航
        screen.blit(shudu,(950,25))#本作品作者吴宇航
        screen.blit(shuduText,(945,75))#本作品作者吴宇航
        screen.blit(shapan,(50,100))#本作品作者吴宇航
        screen.blit(shapanText,(40,150))#本作品作者吴宇航
        screen.blit(flybird,(125,100))#本作品作者吴宇航
        screen.blit(flybirdText,(110,150))#本作品作者吴宇航
        screen.blit(huihua,(200,100))#本作品作者吴宇航
        screen.blit(huihuaText,(210,150))#本作品作者吴宇航
        screen.blit(wenben,(275,100))#本作品作者吴宇航
        screen.blit(wenbenText,(275,150))#本作品作者吴宇航
        screen.blit(huatu,(350,100))#本作品作者吴宇航
        screen.blit(huatuText,(350,150))#本作品作者吴宇航
        screen.blit(xiaoqiu,(425,100))#本作品作者吴宇航
        screen.blit(xiaoqiuText,(405,150))#本作品作者吴宇航
        screen.blit(migong,(500,100))#本作品作者吴宇航
        screen.blit(migongText,(490,150))#本作品作者吴宇航
        screen.blit(shipin,(575,100))#本作品作者吴宇航
        screen.blit(shipinText,(560,150))#本作品作者吴宇航
        screen.blit(mofang,(650,100))#本作品作者吴宇航
        screen.blit(mofangText,(640,150))#本作品作者吴宇航
        screen.blit(twofour,(725,100))#本作品作者吴宇航
        screen.blit(twofourText,(715,150))#本作品作者吴宇航
        screen.blit(tuixiang,(800,100))#本作品作者吴宇航
        screen.blit(tuixiangText,(795,150))#本作品作者吴宇航
        screen.blit(chidou,(875,100))#本作品作者吴宇航
        screen.blit(chidouText,(870,150))#本作品作者吴宇航
        screen.blit(golf,(950,100))#本作品作者吴宇航
        screen.blit(golfText,(945,150))#本作品作者吴宇航
        screen.blit(paoku,(50,175))#本作品作者吴宇航
        screen.blit(paokuText,(50,225))#本作品作者吴宇航
        screen.blit(saolei,(125,175))#本作品作者吴宇航
        screen.blit(saoleiText,(125,225))#本作品作者吴宇航
        screen.blit(saiche,(200,175))#本作品作者吴宇航
        screen.blit(saicheText,(200,225))#本作品作者吴宇航
        screen.blit(dongwu,(275,175))#本作品作者吴宇航
        screen.blit(dongwuText,(275,225))#本作品作者吴宇航
        screen.blit(fanpai,(350,175))#本作品作者吴宇航
        screen.blit(fanpaiText,(350,225))#本作品作者吴宇航
        screen.blit(qiangzhan,(425,175))#本作品作者吴宇航
        screen.blit(qiangzhanText,(425,225))#本作品作者吴宇航
        screen.blit(tafang,(500,175))#本作品作者吴宇航
        screen.blit(tafangText,(500,225))#本作品作者吴宇航
        screen.blit(taila,(575,175))#本作品作者吴宇航
        screen.blit(tailaText,(575,225))#本作品作者吴宇航
        screen.blit(baowei,(650,175))#本作品作者吴宇航
        screen.blit(baoweiText,(650,225))#本作品作者吴宇航
        screen.blit(renzhe,(725,175))#本作品作者吴宇航
        screen.blit(renzheText,(725,225))#本作品作者吴宇航
        screen.blit(feiji,(800,175))#本作品作者吴宇航
        screen.blit(feijiText,(800,225))#本作品作者吴宇航
        screen.blit(secai,(875,175))#本作品作者吴宇航
        screen.blit(secaiText,(875,225))#本作品作者吴宇航
        screen.blit(heping,(950,175))#本作品作者吴宇航
        screen.blit(hepingText,(950,225))#本作品作者吴宇航
        screen.blit(wangzhe,(50,250))#本作品作者吴宇航
        screen.blit(wangzheText,(50,300))#本作品作者吴宇航
        screen.blit(caidan,(81,710))#本作品作者吴宇航
        screen.blit(shijian,(800,710))#本作品作者吴宇航
        screen.blit(dianliang,(863,710))#本作品作者吴宇航
        screen.blit(shengyin,(918,710))#本作品作者吴宇航
        screen.blit(wangluo,(975,710))#本作品作者吴宇航
        #本作品作者吴宇航
        off = pygame.transform.scale(pygame.image.load(kaishijian),(80,60))#本作品作者吴宇航
        cortana = pygame.transform.scale(pygame.image.load(cortanajian),(60,60))#本作品作者吴宇航
        sou = pygame.transform.scale(pygame.image.load(soujian),(60,60))#本作品作者吴宇航
        renwu = pygame.transform.scale(pygame.image.load(renwujian),(60,60))#本作品作者吴宇航
        screen.blit(off,(0,710))#本作品作者吴宇航
        screen.blit(cortana,(70,710))#本作品作者吴宇航
        screen.blit(sou,(140,710))#本作品作者吴宇航
        screen.blit(renwu,(210,710))#本作品作者吴宇航
        #本作品作者吴宇航
        mouseRect.center = (pygame.mouse.get_pos())#本作品作者吴宇航
        pygame.display.update()#本作品作者吴宇航
    if dakai == "setting":#本作品作者吴宇航
        try:#本作品作者吴宇航
            # -*- coding: utf-8 -*-#本作品作者吴宇航
            __author__ = 'Yang'#本作品作者吴宇航
#本作品作者吴宇航
            class Application_UI(object):#本作品作者吴宇航
#本作品作者吴宇航
                # path = r"E:\\python开发工具\\project\\tkinter"#本作品作者吴宇航
                path = os.path.abspath(".")#本作品作者吴宇航
                file_types = [".png", ".jpg", ".jpeg", ".ico", ".gif"]#本作品作者吴宇航
                scroll_visiblity = True#本作品作者吴宇航
#本作品作者吴宇航
                font = 11#本作品作者吴宇航
                font_type = "Courier New"#本作品作者吴宇航
#本作品作者吴宇航
                def __init__(self):#本作品作者吴宇航
                    # 设置UI界面#本作品作者吴宇航
                    window = tkinter.Tk()#本作品作者吴宇航
                    self.root = window#本作品作者吴宇航
                    win_width = 800#本作品作者吴宇航
                    win_height = 600#本作品作者吴宇航
#本作品作者吴宇航
                    screen_width, screen_height = window.maxsize()#本作品作者吴宇航
                    x = int((screen_width - win_width) / 2)#本作品作者吴宇航
                    y = int((screen_height - win_height) / 2)#本作品作者吴宇航
                    window.title("文件管理工具")#本作品作者吴宇航
                    window.geometry("%sx%s+%s+%s" % (win_width, win_height, x, y))#本作品作者吴宇航
#本作品作者吴宇航
                    menu = tkinter.Menu(window)#本作品作者吴宇航
                    window.config(menu=menu)#本作品作者吴宇航
#本作品作者吴宇航
                    selct_path = tkinter.Menu(menu, tearoff=0)#本作品作者吴宇航
                    selct_path.add_command(label="打开", accelerator="Ctrl + O", command=self.open_dir)#本作品作者吴宇航
                    selct_path.add_command(label="保存", accelerator="Ctrl + S", command=self.save_file)#本作品作者吴宇航
#本作品作者吴宇航
                    menu.add_cascade(label="文件", menu=selct_path)#本作品作者吴宇航
#本作品作者吴宇航
                    about = tkinter.Menu(menu, tearoff=0)#本作品作者吴宇航
                    about.add_command(label="版本", accelerator="v1.0.0")#本作品作者吴宇航
                    about.add_command(label="作者", accelerator="样子")#本作品作者吴宇航
                    menu.add_cascade(label="关于", menu=about)#本作品作者吴宇航
#本作品作者吴宇航
                    # 顶部frame#本作品作者吴宇航
                    top_frame = Frame(window, bg="#fff")#本作品作者吴宇航
                    top_frame.pack(side=TOP, fill=X)#本作品作者吴宇航
                    label = Label(top_frame, text="当前选中路径：", bg="#fff")#本作品作者吴宇航
                    label.pack(side=LEFT)#本作品作者吴宇航
#本作品作者吴宇航
                    self.path_var = StringVar()#本作品作者吴宇航
                    self.path_var.set("无")#本作品作者吴宇航
                    label_path = Label(top_frame, textvariable=self.path_var, bg="#fff", fg="red", height=2)#本作品作者吴宇航
                    label_path.pack(anchor=W)#本作品作者吴宇航
#本作品作者吴宇航
                    paned_window = PanedWindow(window, showhandle=False, orient=HORIZONTAL)#本作品作者吴宇航
                    paned_window.pack(expand=1, fill=BOTH)#本作品作者吴宇航
#本作品作者吴宇航
                    # 左侧frame#本作品作者吴宇航
                    self.left_frame = Frame(paned_window)#本作品作者吴宇航
                    paned_window.add(self.left_frame)#本作品作者吴宇航
#本作品作者吴宇航
                    self.tree = ttk.Treeview(self.left_frame, show="tree", selectmode="browse")#本作品作者吴宇航
                    tree_y_scroll_bar = Scrollbar(self.left_frame, command=self.tree.yview, relief=SUNKEN, width=2)#本作品作者吴宇航
                    tree_y_scroll_bar.pack(side=RIGHT, fill=Y)#本作品作者吴宇航
                    self.tree.config(yscrollcommand=tree_y_scroll_bar.set)#本作品作者吴宇航
                    self.tree.pack(expand=1, fill=BOTH)#本作品作者吴宇航
#本作品作者吴宇航
                    # 右侧frame#本作品作者吴宇航
                    right_frame = Frame(paned_window)#本作品作者吴宇航
                    paned_window.add(right_frame)#本作品作者吴宇航
#本作品作者吴宇航
                    # 右上角frame#本作品作者吴宇航
                    right_top_frame = Frame(right_frame)#本作品作者吴宇航
                    right_top_frame.pack(expand=1, fill=BOTH)#本作品作者吴宇航
#本作品作者吴宇航
                    self.number_line = Text(right_top_frame, width=0, takefocus=0, border=0, font=(self.font_type, self.font),#本作品作者吴宇航
                                            cursor="")#本作品作者吴宇航
                    self.number_line.pack(side=LEFT, fill=Y)#本作品作者吴宇航
#本作品作者吴宇航
                    # 右上角Text#本作品作者吴宇航
                    text = Text(right_top_frame, font=(self.font_type, self.font), state=DISABLED, cursor="", wrap=NONE)#本作品作者吴宇航
                    self.text_obj = text#本作品作者吴宇航
                    text_x_scroll = Scrollbar(right_frame, command=text.xview, orient=HORIZONTAL)#本作品作者吴宇航
                    text_y_scroll = Scrollbar(right_top_frame, command=text.yview)#本作品作者吴宇航
                    self.text_scroll_obj = text_y_scroll#本作品作者吴宇航
                    text.config(xscrollcommand=text_x_scroll.set, yscrollcommand=text_y_scroll.set)#本作品作者吴宇航
                    text_y_scroll.pack(side=RIGHT, fill=Y)#本作品作者吴宇航
                    text_x_scroll.pack(side=BOTTOM, fill=X)#本作品作者吴宇航
                    text.pack(expand=1, fill=BOTH)#本作品作者吴宇航
#本作品作者吴宇航
                    # 右下角frame#本作品作者吴宇航
                    right_bottom_frame = Frame(right_frame)#本作品作者吴宇航
                    right_bottom_frame.pack(side=BOTTOM, fill=X)#本作品作者吴宇航
#本作品作者吴宇航
                    self.folder_img = PhotoImage(file=r"./image/folder.png")#本作品作者吴宇航
                    self.file_img = PhotoImage(file=r"./image/text_file.png")#本作品作者吴宇航
#本作品作者吴宇航
                    php_img = PhotoImage(file=r"./image/php.png")#本作品作者吴宇航
                    python_img = PhotoImage(file=r"./image/python.png")#本作品作者吴宇航
                    image_img = PhotoImage(file=r"./image/img.png")#本作品作者吴宇航
#本作品作者吴宇航
                    # 设置文件图标#本作品作者吴宇航
                    self.icon = {".php": php_img, ".py": python_img, ".pyc": python_img, ".png": image_img, ".jpg": image_img,#本作品作者吴宇航
                                 ".jpeg": image_img, ".gif": image_img, ".ico": image_img}#本作品作者吴宇航
#本作品作者吴宇航
                    # 加载目录文件#本作品作者吴宇航
                    self.load_tree("", self.path)#本作品作者吴宇航
                    self.tree.bind("<<TreeviewSelect>>", lambda event: self.select_tree())#本作品作者吴宇航
                    text.bind("<MouseWheel>", lambda event: self.update_line())#本作品作者吴宇航
#本作品作者吴宇航
                    self.number_line.bind("<FocusIn>", self.focus_in_event)#本作品作者吴宇航
                    self.number_line.bind('<Button-1>', self.button_ignore)#本作品作者吴宇航
                    self.number_line.bind('<Button-2>', self.button_ignore)#本作品作者吴宇航
                    self.number_line.bind('<Button-3>', self.button_ignore)#本作品作者吴宇航
                    self.number_line.bind('<B1-Motion>', self.button_ignore)#本作品作者吴宇航
                    self.number_line.bind('<B2-Motion>', self.button_ignore)#本作品作者吴宇航
                    self.number_line.bind('<B3-Motion>', self.button_ignore)#本作品作者吴宇航
#本作品作者吴宇航
                    self.text_scroll_obj.bind('<B1-Motion>', lambda event: self.update_line())#本作品作者吴宇航
                    self.text_obj.bind('<KeyRelease>', lambda event: self.update_line())#本作品作者吴宇航
#本作品作者吴宇航
                    text.bind("<Control-Key-s>", lambda event: self.save_file())#本作品作者吴宇航
                    text.bind("<Control-Key-S>", lambda event: self.save_file())#本作品作者吴宇航
                    text.bind("<Control-Key-Z>", lambda event: self.toUndo())#本作品作者吴宇航
                    text.bind("<Control-Key-Y>", lambda event: self.toRedo())#本作品作者吴宇航
#本作品作者吴宇航
                    window.mainloop()#本作品作者吴宇航
#本作品作者吴宇航
            class Application(Application_UI):#本作品作者吴宇航
                def __init__(self):#本作品作者吴宇航
                    Application_UI.__init__(self)#本作品作者吴宇航
#本作品作者吴宇航
                ''' 保存文件'''#本作品作者吴宇航
#本作品作者吴宇航
                def save_file(self):#本作品作者吴宇航
                    # 判断是否是文件#本作品作者吴宇航
                    path = self.path_var.get()#本作品作者吴宇航
                    print(path)#本作品作者吴宇航
                    if self.is_file(path) is True:#本作品作者吴宇航
                        # 判断是否为图片#本作品作者吴宇航
                        if self.is_type_in(path) is False:#本作品作者吴宇航
                            content = self.text_obj.get(1.0, END)[:-1]#本作品作者吴宇航
                            with open(path, "w", encoding="utf-8") as f:#本作品作者吴宇航
                                f.write(content)#本作品作者吴宇航
                            messagebox.showinfo("提示", "保存成功")#本作品作者吴宇航
                        else:#本作品作者吴宇航
                            messagebox.showwarning("提示", "不能保存图片")#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        messagebox.showwarning("提示", "不能保存目录")#本作品作者吴宇航
#本作品作者吴宇航
                ''' 设置默认搜索路径'''#本作品作者吴宇航
#本作品作者吴宇航
                def open_dir(self):#本作品作者吴宇航
                    path = filedialog.askdirectory(title=u"设置目录", initialdir=self.path)#本作品作者吴宇航
                    print("设置路径：" + path)#本作品作者吴宇航
                    self.path = path#本作品作者吴宇航
                    # 删除所有目录#本作品作者吴宇航
                    self.delete_tree()#本作品作者吴宇航
                    self.load_tree("", self.path)#本作品作者吴宇航
#本作品作者吴宇航
                ''' 判断是否为文件'''#本作品作者吴宇航
#本作品作者吴宇航
                def is_file(self, path):#本作品作者吴宇航
                    if os.path.isfile(path):#本作品作者吴宇航
                        return True#本作品作者吴宇航
                    return False#本作品作者吴宇航
#本作品作者吴宇航
                ''' 判断是否是图片类型'''#本作品作者吴宇航
#本作品作者吴宇航
                def is_type_in(self, path):#本作品作者吴宇航
                    ext = self.file_extension(path)#本作品作者吴宇航
                    if ext in self.file_types:#本作品作者吴宇航
                        return True#本作品作者吴宇航
                    return False#本作品作者吴宇航
#本作品作者吴宇航
                ''' 删除树'''#本作品作者吴宇航
#本作品作者吴宇航
                def delete_tree(self):#本作品作者吴宇航
                    self.tree.delete(self.tree.get_children())#本作品作者吴宇航
#本作品作者吴宇航
                def focus_in_event(self, event=None):#本作品作者吴宇航
                    self.text_obj.focus_set()#本作品作者吴宇航
#本作品作者吴宇航
                def button_ignore(self, ev=None):#本作品作者吴宇航
                    return "break"#本作品作者吴宇航
#本作品作者吴宇航
                ''' 加载目录'''#本作品作者吴宇航
#本作品作者吴宇航
                def load_tree(self, root, path):#本作品作者吴宇航
                    is_open = False#本作品作者吴宇航
                    if root == "":#本作品作者吴宇航
                        is_open = True#本作品作者吴宇航
#本作品作者吴宇航
                    root = self.tree.insert(root, END, text=" " + self.dir_name(path), values=(path,), open=is_open,#本作品作者吴宇航
                                            image=self.folder_img)#本作品作者吴宇航
#本作品作者吴宇航
                    try:#本作品作者吴宇航
                        for file in os.listdir(path):#本作品作者吴宇航
                            file_path = path + "\\" + file#本作品作者吴宇航
                            if os.path.isdir(file_path):#本作品作者吴宇航
                                self.load_tree(root, file_path)#本作品作者吴宇航
                            else:#本作品作者吴宇航
                                ext = self.file_extension(file)#本作品作者吴宇航
                                img = self.icon.get(ext)#本作品作者吴宇航
                                if img is None:#本作品作者吴宇航
                                    img = self.file_img#本作品作者吴宇航
                                self.tree.insert(root, END, text=" " + file, values=(file_path,), image=img)#本作品作者吴宇航
                    except Exception as e:#本作品作者吴宇航
                        print(e)#本作品作者吴宇航
#本作品作者吴宇航
                ''' 获取文件后缀'''#本作品作者吴宇航
#本作品作者吴宇航
                def file_extension(self, file):#本作品作者吴宇航
                    file_info = os.path.splitext(file)#本作品作者吴宇航
                    return file_info[-1]#本作品作者吴宇航
#本作品作者吴宇航
                ''' 获取目录名称'''#本作品作者吴宇航
#本作品作者吴宇航
                def dir_name(self, path):#本作品作者吴宇航
                    path_list = os.path.split(path)#本作品作者吴宇航
                    return path_list[-1]#本作品作者吴宇航
#本作品作者吴宇航
                ''' 更新行数'''#本作品作者吴宇航
#本作品作者吴宇航
                def update_line(self):#本作品作者吴宇航
                    if not self.scroll_visiblity:#本作品作者吴宇航
                        return#本作品作者吴宇航
                    self.number_line.delete(1.0, END)#本作品作者吴宇航
                    text_h, text_l = map(int, str.split(self.text_obj.index(END), "."))#本作品作者吴宇航
                    q = range(1, text_h)#本作品作者吴宇航
                    r = map(lambda x: '%i' % x, q)#本作品作者吴宇航
                    s = '\n'.join(r)#本作品作者吴宇航
                    self.number_line.insert(END, s)#本作品作者吴宇航
#本作品作者吴宇航
                    if text_h <= 100:#本作品作者吴宇航
                        width = 2#本作品作者吴宇航
                    elif text_h <= 1000:#本作品作者吴宇航
                        width = 3#本作品作者吴宇航
                    elif text_h <= 10000:#本作品作者吴宇航
                        width = 4#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        width = 5#本作品作者吴宇航
                    self.number_line.configure(width=width)#本作品作者吴宇航
                    self.number_line.yview_moveto(self.text_obj.yview()[0])#本作品作者吴宇航
#本作品作者吴宇航
                ''' 选中item回调'''#本作品作者吴宇航
#本作品作者吴宇航
                def select_tree(self):#本作品作者吴宇航
                    for item in self.tree.selection():#本作品作者吴宇航
                        item_text = self.tree.item(item, "values")#本作品作者吴宇航
                        select_path = "\\".join(item_text)#本作品作者吴宇航
                        self.path_var.set(select_path)#本作品作者吴宇航
#本作品作者吴宇航
                        self.text_obj.config(state=NORMAL, cursor="xterm")#本作品作者吴宇航
                        # 清空text内容#本作品作者吴宇航
                        self.text_obj.delete(1.0, END)#本作品作者吴宇航
                        self.update_line()#本作品作者吴宇航
                        if self.is_file(select_path) is True:#本作品作者吴宇航
                            if self.is_type_in(select_path) is True:#本作品作者吴宇航
                                self.text_obj.config(state=DISABLED, cursor="")#本作品作者吴宇航
                                self.look_image(select_path)#本作品作者吴宇航
                            else:#本作品作者吴宇航
                                try:#本作品作者吴宇航
                                    self.open_file(select_path, "r", "utf-8")#本作品作者吴宇航
                                    self.update_line()#本作品作者吴宇航
                                except Exception as e:#本作品作者吴宇航
                                    print(e)#本作品作者吴宇航
                        else:#本作品作者吴宇航
                            self.text_obj.config(state=DISABLED, cursor="")#本作品作者吴宇航
#本作品作者吴宇航
                ''' 查看图片'''#本作品作者吴宇航
#本作品作者吴宇航
                def look_image(self, select_path):#本作品作者吴宇航
                    try:#本作品作者吴宇航
                        image = Image.open(select_path)#本作品作者吴宇航
                        self.look_photo = ImageTk.PhotoImage(image)#本作品作者吴宇航
                        self.text_obj.image_create(END, image=self.look_photo)#本作品作者吴宇航
                    except Exception as e:#本作品作者吴宇航
                        print(e)#本作品作者吴宇航
#本作品作者吴宇航
                ''' 打开文件写入内容'''#本作品作者吴宇航
#本作品作者吴宇航
                def open_file(self, select_path, mode, encoding=None):#本作品作者吴宇航
                    with open(select_path, mode=mode, encoding=encoding) as f:#本作品作者吴宇航
                        self.text_obj.insert(1.0, f.read())#本作品作者吴宇航
#本作品作者吴宇航
            if __name__ == "__main__":#本作品作者吴宇航
                Application()#本作品作者吴宇航
            # def fasdasdf():#本作品作者吴宇航
            #     window1.destroy()#本作品作者吴宇航
            #     fasdasdf1()#本作品作者吴宇航
            # window1 = Tk() #建立窗口，把窗口储存在window中#本作品作者吴宇航
            # window1.title("Lightning UI Setting") #设置标题#本作品作者吴宇航
            # window1.geometry("400x300")#本作品作者吴宇航
            # window1.iconbitmap("金星.ico")#本作品作者吴宇航
            # def Check_state():#本作品作者吴宇航
            #     wifi = Pywifi()#本作品作者吴宇航
            #     iface = wifi.interfaces()[0]#本作品作者吴宇航
            #     print(ifaces.status())#本作品作者吴宇航
            #     if ifaces.status() == 4:#本作品作者吴宇航
            #         print("此电脑已连接无线网络")#本作品作者吴宇航
            # def shuangka():#本作品作者吴宇航
            #     window2 = Tk() #建立窗口，把窗口储存在window中#本作品作者吴宇航
            #     window2.title("Lightning Dual Card Settings") #设置标题#本作品作者吴宇航
            #     window2.geometry("800x600")#本作品作者吴宇航
            #     def dual5g():#本作品作者吴宇航
            #         windowsx = Tk() #建立窗口，把窗口储存在window中#本作品作者吴宇航
            #         windowsx.title("if you okay to open 5G") #设置标题#本作品作者吴宇航
            #         windowsx.geometry("400x300")#本作品作者吴宇航
            #         Label(windowsx,text = "你确定开启5G模式？这将使你的电脑内存占用变高").pack()#本作品作者吴宇航
            #         def open5g():#本作品作者吴宇航
            #             messagebox.showwarning("","你现在使用的是：5G/4G/3G/2G模式")#本作品作者吴宇航
            #         def close5g():#本作品作者吴宇航
            #             messagebox.showwarning("","你现在使用的是4G/3G/2G模式")#本作品作者吴宇航
            #         Button(windowsx,text = "是，开启5G模式",command = open5g).pack()#本作品作者吴宇航
            #         Button(windowsx,text = "否，停用5G，使用4G",command = close5g).pack()#本作品作者吴宇航
            #     Label(window2,text = "星空系统采用移动网络系统，因此优势在于免费、快速，5G最快下载/上传速度为：148MB/S，4G为18.5MB/S。").pack()#本作品作者吴宇航
            #     Button(window2,text = "1.5G/4G/3G/2G",command = dual5g).pack()#本作品作者吴宇航
            #     def dual4g():#本作品作者吴宇航
            #         messagebox.showwarning("","你现在使用的是4G/3G/2G模式")#本作品作者吴宇航
            #     Button(window2,text = "2.4G/3G/2G",command = dual4g).pack()#本作品作者吴宇航
            #     def dual3g():#本作品作者吴宇航
            #         messagebox.showwarning("","你现在使用的是3G/2G模式")#本作品作者吴宇航
            #     Button(window2,text = "3.3G/2G",command = dual3g).pack()#本作品作者吴宇航
            #     def dual2g():#本作品作者吴宇航
            #         messagebox.showwarning("","你现在使用的是仅2G模式")#本作品作者吴宇航
            #     Button(window2,text = "4.仅2G",command = dual2g).pack()#本作品作者吴宇航
            #     def dual0g():#本作品作者吴宇航
            #         messagebox.showwarning("","你已关闭移动数据网络")#本作品作者吴宇航
            #     Button(window2,text = "5.关闭移动数据网络",command = dual0g).pack()#本作品作者吴宇航
            # def button_is_clicked():#本作品作者吴宇航
            #     print("")#本作品作者吴宇航
            # def disk():#本作品作者吴宇航
            #     window4 = Tk() #建立窗口，把窗口储存在window中#本作品作者吴宇航
            #     window4.title("Lightning Disk Management") #设置标题#本作品作者吴宇航
            #     window4.geometry("700x300")#本作品作者吴宇航
            #     import ctypes#本作品作者吴宇航
            #     import os#本作品作者吴宇航
            #     import platform#本作品作者吴宇航
            #     import sys#本作品作者吴宇航
            #     def get_free_space_mb(folder):#本作品作者吴宇航
            #         """ Return folder/drive free space (in bytes)#本作品作者吴宇航
            #         """#本作品作者吴宇航
            #         if platform.system() == 'Windows':#本作品作者吴宇航
            #             free_bytes = ctypes.c_ulonglong(0)#本作品作者吴宇航
            #             ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(folder), None, None, ctypes.pointer(free_bytes))#本作品作者吴宇航
            #             return free_bytes.value/1024/1024/1024 #本作品作者吴宇航
            #         else:#本作品作者吴宇航
            #             st = os.statvfs(folder)#本作品作者吴宇航
            #             return st.f_bavail * st.f_frsize/1024/1024#本作品作者吴宇航
            #     Label(window4,text = "计算机C标号磁盘剩余可使用空间" + str(get_free_space_mb('C:\\')) + 'GB').pack()#本作品作者吴宇航
            #     Label(window4,text = "计算机D标号磁盘剩余可使用空间" + str(get_free_space_mb('D:\\')) + 'GB').pack()#本作品作者吴宇航
            #     Label(window4,text = "计算机E标号磁盘剩余可使用空间(如果你没有该标号磁盘，请忽略)" + str(get_free_space_mb('E:\\')) + 'GB').pack()#本作品作者吴宇航
            #     Label(window4,text = "计算机F标号磁盘剩余可使用空间(如果你没有该标号磁盘，请忽略)" + str(get_free_space_mb('F:\\')) + 'GB').pack()#本作品作者吴宇航
            #     Label(window4,text = "计算机G标号磁盘剩余可使用空间(如果你没有该标号磁盘，请忽略)" + str(get_free_space_mb('G:\\')) + 'GB').pack()#本作品作者吴宇航
            # def momery():#本作品作者吴宇航
            #     window3 = Tk() #建立窗口，把窗口储存在window中#本作品作者吴宇航
            #     window3.title("Lightning Detect Memory") #设置标题#本作品作者吴宇航
            #     window3.geometry("700x300")#本作品作者吴宇航
            #     import psutil#本作品作者吴宇航
            #     mem = psutil.virtual_memory()#本作品作者吴宇航
            #     zj = float(mem.total/1024/1024/1024)#本作品作者吴宇航
            #     Label(window3,text = "此计算机所有内存空间：" + str(zj) + "GB").pack()#本作品作者吴宇航
            #     ysy = float(mem.used/1024/1024/1024)#本作品作者吴宇航
            #     Label(window3,text = "此计算机已使用内存空间：" + str(ysy) + "GB").pack()#本作品作者吴宇航
            #     kx = float(mem.free/1024/1024/1024)#本作品作者吴宇航
            #     Label(window3,text = "此计算机剩余可使用内存空间:" + str(kx) + "GB").pack()#本作品作者吴宇航
            # def system():#本作品作者吴宇航
            #     window888 = Tk() #建立窗口，把窗口储存在window中#本作品作者吴宇航
            #     window888.title("Night Star System") #设置标题#本作品作者吴宇航
            #     window888.geometry("1070x606")#本作品作者吴宇航
            #     import platform#本作品作者吴宇航
            #     import wmi#本作品作者吴宇航
            #     import psutil#本作品作者吴宇航
            #     Label(window888,text = "Lightning UI").pack()#本作品作者吴宇航
            #     Label(window888,text = "设备规格").pack()#本作品作者吴宇航
            #     cpuinfo = wmi.WMI()#本作品作者吴宇航
            #     for cpu in cpuinfo.Win32_Processor(): #本作品作者吴宇航
            #         Label(window888,text = "处理器：" + cpu.Name).pack()#本作品作者吴宇航
            #     mem = psutil.virtual_memory()#本作品作者吴宇航
            #     zj = float(mem.total)#本作品作者吴宇航
            #     Label(window888,text = "机带RAM：" + str(zj / 1024 / 1024 /1024) + " GB").pack()#本作品作者吴宇航
            #     Label(window888,text = "设备ID：16ASDG59-AF4W-ASGF-1F2D-A4EW69GRW3E5")#本作品作者吴宇航
            #     Label(window888,text = "产品ID：00916-49852-94836-AG156")#本作品作者吴宇航
            #     import os#本作品作者吴宇航
            #     prg = 'C:Program Files(x86)'#本作品作者吴宇航
            #     if True == os.path.exists( prg ):#本作品作者吴宇航
            #         Label(window888,text = "系统类型：32位操作系统，基于x86的处理器").pack()#本作品作者吴宇航
            #     else:#本作品作者吴宇航
            #         Label(window888,text = "系统类型：64位操作系统，基于x64的处理器").pack()#本作品作者吴宇航
            #     Label(window888,text = "笔和触控：没有可用于此显示器的笔或触控").pack()#本作品作者吴宇航
            #     Label(window888,text = "Lightning UI 规格").pack()#本作品作者吴宇航
            #     Label(window888,text = "版本：Lightning UI 1.1 测试版").pack()#本作品作者吴宇航
            #     Label(window888,text = "版本号：1002").pack()#本作品作者吴宇航
            #     Label(window888,text = "安装日期：" + strftime("%Y/%m/%d %H:%M:%S")).pack()#本作品作者吴宇航
            #     Label(window888,text = "操作系统版本：10325.9582").pack()#本作品作者吴宇航
            #     Label(window888,text = "体验：Lightning UI Feature Experience Pack 165.1563.18.6980").pack()#本作品作者吴宇航
            # Button(window1,text = "1.WLAN(要使用，请下载pywifi库，该库可能仅在笔记本电脑上可用)",command = Check_state).pack()#本作品作者吴宇航
            # Button(window1,text = "2.双卡和移动网络(不能设置双卡)",command = shuangka).pack()#本作品作者吴宇航
            # Button(window1,text = "3.蓝牙(暂时不可用)",command = button_is_clicked).pack()#本作品作者吴宇航
            # Button(window1,text = "4.飞行模式(暂时不可用)",command = button_is_clicked).pack()#本作品作者吴宇航
            # Button(window1,text = "5.计算机磁盘剩余存储空间",command = disk).pack()#本作品作者吴宇航
            # Button(window1,text = "6.计算机内存使用情况",command = momery).pack()#本作品作者吴宇航
            # Button(window1,text = "7.关于 Lightning UI",command = system).pack()#本作品作者吴宇航
            # window1.protocol("WM_DELETE_WINDOW",fasdasdf)#本作品作者吴宇航
            # window1.mainloop()#本作品作者吴宇航
        except:#本作品作者吴宇航
            messagebox.showinfo("提示","该功能维护中，暂未开放")#本作品作者吴宇航
            fasdasdf1()#本作品作者吴宇航
    elif dakai == "chrome":#本作品作者吴宇航
        #本作品作者吴宇航
#本作品作者吴宇航
        def download(url):#本作品作者吴宇航
            # 请求地址#本作品作者吴宇航
            url = 'https://baike.baidu.com/item/' + urllib.parse.quote(url)#本作品作者吴宇航
            # 请求头部#本作品作者吴宇航
            headers = { #本作品作者吴宇航
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36' #本作品作者吴宇航
            }#本作品作者吴宇航
            # 利用请求地址和请求头部构造请求对象#本作品作者吴宇航
            req = urllib.request.Request(url=url, headers=headers, method='GET')#本作品作者吴宇航
            # 发送请求，获得响应#本作品作者吴宇航
            response = urllib.request.urlopen(req)#本作品作者吴宇航
            # 读取响应，获得文本#本作品作者吴宇航
            text = response.read().decode('utf-8')#本作品作者吴宇航
            # 构造 _Element 对象#本作品作者吴宇航
            html = etree.HTML(text)#本作品作者吴宇航
            # 使用 xpath 匹配数据，得到匹配字符串列表#本作品作者吴宇航
            sen_list = html.xpath('//div[contains(@class,"lemma-summary") or contains(@class,"lemmaWgt-lemmaSummary")]//text()') #本作品作者吴宇航
            # 过滤数据，去掉空白#本作品作者吴宇航
            sen_list_after_filter = [item.strip('\n') for item in sen_list]#本作品作者吴宇航
            # 将字符串列表连成字符串并返回#本作品作者吴宇航
            return ''.join(sen_list_after_filter)#本作品作者吴宇航
        def get_data(html):#本作品作者吴宇航
            regex = re.compile('<meta name="description" content="(.*?)">')#本作品作者吴宇航
            regex = re.compile('<div class="lemma-summary" label-module="lemmaSummary">(\s*)<div class="para" label-module="para">([\s\S]*?)</div>(\s*)</div>')#本作品作者吴宇航
            data = [('\n', 'Python是一种计算机程序设计语言。是一种动态的、面向对象的脚本语言，最初被设计用于编写自动化脚本(shell)，随着版本的不断更新和语言新功能的添加，越来越多被用于独立的、大型项目的开发。', '\n')]#本作品作者吴宇航
            data = re.findall(regex, html)[0][1]#本作品作者吴宇航
            return data#本作品作者吴宇航
        curr_time = datetime.now()#本作品作者吴宇航
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
        xxx=x(datetime.now())#本作品作者吴宇航
        ttt=curr_time.strftime("%Y-%m-%d")#本作品作者吴宇航
        rrr='日期:'+ttt+xxx#本作品作者吴宇航
        def main(a):#本作品作者吴宇航
            class MyBrowser(wx.Dialog):#本作品作者吴宇航
                def __init__(self, *args, **kwds):#本作品作者吴宇航
                    wx.Dialog.__init__(self, *args, **kwds)#本作品作者吴宇航
                    sizer = wx.BoxSizer(wx.VERTICAL)#本作品作者吴宇航
                    self.browser = wx.html2.WebView.New(self)#本作品作者吴宇航
                    sizer.Add(self.browser, 1, wx.EXPAND, 10)#本作品作者吴宇航
                    self.SetSizer(sizer)#本作品作者吴宇航
                    self.SetSize((1500, 1500))#本作品作者吴宇航
            app = wx.App()#本作品作者吴宇航
            dialog = MyBrowser(None, -1)#本作品作者吴宇航
            dialog.browser.LoadURL(a) #加载页面。如果是加载html字符串应该使用  dialog.browser.SetPage(html_string,"")#本作品作者吴宇航
            dialog.Show()#本作品作者吴宇航
            app.MainLoop()#本作品作者吴宇航
        class MyFrame(wx.Frame):#本作品作者吴宇航
            def __init__(self, parent, id):#本作品作者吴宇航
                wx.Frame.__init__(self, parent, id, '银河浏览器', size=(1100, 600),name='银河浏览器')#本作品作者吴宇航
                panel = wx.Panel(self)#本作品作者吴宇航
                self.SetBackgroundColour("#00BFFF") #本作品作者吴宇航
                self.bt_confirm = wx.Button(panel, label='访问网站')#本作品作者吴宇航
                self.bt_confirm.Bind(wx.EVT_BUTTON,self.OnclickSubmit)#本作品作者吴宇航
                self.bt_km = wx.Button(panel, label='银河搜索')#本作品作者吴宇航
                self.bt_km.Bind(wx.EVT_BUTTON,self.km)#本作品作者吴宇航
                self.bt_baidu = wx.Button(panel, label='百度搜索')#本作品作者吴宇航
                self.bt_baidu.Bind(wx.EVT_BUTTON,self.baidu)#本作品作者吴宇航
                self.bt_bdbk = wx.Button(panel, label='百度百科')#本作品作者吴宇航
                self.bt_bdbk.Bind(wx.EVT_BUTTON,self.bdbk)#本作品作者吴宇航
                self.bt_bing= wx.Button(panel, label='必应搜索')#本作品作者吴宇航
                self.bt_bing.Bind(wx.EVT_BUTTON,self.bing)#本作品作者吴宇航
                self.bt_s= wx.Button(panel, label='360搜索')#本作品作者吴宇航
                self.bt_s.Bind(wx.EVT_BUTTON,self.s)#本作品作者吴宇航
                self.bt_sougou= wx.Button(panel, label='搜狗搜索')#本作品作者吴宇航
                self.bt_sougou.Bind(wx.EVT_BUTTON,self.sougou)#本作品作者吴宇航
                self.bt_cancel = wx.Button(panel, label='清除内容')#本作品作者吴宇航
                self.bt_cancel.Bind(wx.EVT_BUTTON,self.OnclickCancel)#本作品作者吴宇航
                self.bt_gx= wx.Button(panel, label='查看更新')#本作品作者吴宇航
                self.bt_gx.Bind(wx.EVT_BUTTON,self.gx)#本作品作者吴宇航
                self.x= wx.StaticText(panel, label='银河浏览器')#本作品作者吴宇航
                font = wx.Font(20, wx.DEFAULT, wx.FONTSTYLE_NORMAL, wx.NORMAL)#本作品作者吴宇航
                self.x.SetFont(font)#本作品作者吴宇航
                self.bq=wx.StaticText(panel, label='© 2021 吴宇航 版权所有')#本作品作者吴宇航
                self.lzx=wx.StaticText(panel, label=rrr)#本作品作者吴宇航
                self.title = wx.StaticText(panel, label="输入网址或搜索内容")#本作品作者吴宇航
                self.text_user = wx.TextCtrl(panel, style=wx.TE_LEFT)#本作品作者吴宇航
                hsizer_user = wx.BoxSizer(wx.HORIZONTAL)#本作品作者吴宇航
                hsizer_user.Add(self.text_user, proportion=1, flag=wx.ALL, border=5)#本作品作者吴宇航
                hsizer_pwd = wx.BoxSizer(wx.HORIZONTAL)#本作品作者吴宇航
                hsizer_button = wx.BoxSizer(wx.HORIZONTAL)#本作品作者吴宇航
                hsizer_button.Add(self.bt_confirm, proportion=1, flag=wx.ALIGN_CENTER | wx.LEFT, border=10)#本作品作者吴宇航
                hsizer_button.Add(self.bt_km, proportion=1, flag=wx.ALIGN_CENTER | wx.LEFT, border=10)#本作品作者吴宇航
                hsizer_button.Add(self.bt_baidu, proportion=1, flag=wx.ALIGN_CENTER | wx.LEFT, border=10)#本作品作者吴宇航
                hsizer_button.Add(self.bt_bdbk, proportion=1, flag=wx.ALIGN_CENTER | wx.LEFT, border=10)#本作品作者吴宇航
                hsizer_button.Add(self.bt_bing, proportion=1, flag=wx.ALIGN_CENTER | wx.LEFT, border=10)#本作品作者吴宇航
                hsizer_button.Add(self.bt_s, proportion=1, flag=wx.ALIGN_CENTER | wx.LEFT, border=10)#本作品作者吴宇航
                hsizer_button.Add(self.bt_sougou, proportion=1, flag=wx.ALIGN_CENTER | wx.LEFT, border=10)#本作品作者吴宇航
                hsizer_button.Add(self.bt_cancel, proportion=1, flag=wx.ALIGN_CENTER | wx.LEFT, border=10)#本作品作者吴宇航
                hsizer_button.Add(self.bt_gx, proportion=1, flag=wx.ALIGN_CENTER | wx.LEFT, border=10)#本作品作者吴宇航
                vsizer_all = wx.BoxSizer(wx.VERTICAL)#本作品作者吴宇航
                vsizer_all.Add(self.x, proportion=0, flag=wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER,#本作品作者吴宇航
                                border=15)#本作品作者吴宇航
                vsizer_all.Add(self.title, proportion=0, flag=wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER,#本作品作者吴宇航
                                border=15)#本作品作者吴宇航
                vsizer_all.Add(hsizer_user, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=45)#本作品作者吴宇航
                vsizer_all.Add(hsizer_pwd, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=45)#本作品作者吴宇航
                vsizer_all.Add(hsizer_button, proportion=0, flag=wx.ALIGN_CENTER | wx.TOP, border=15)#本作品作者吴宇航
                hsizer_pwd = wx.BoxSizer(wx.HORIZONTAL)#本作品作者吴宇航
                hsizer_button = wx.BoxSizer(wx.HORIZONTAL)#本作品作者吴宇航
                vsizer_all.Add(self.bq, proportion=0, flag= wx.TOP | wx.ALIGN_CENTER,#本作品作者吴宇航
                                border=350)#本作品作者吴宇航
                panel.SetSizer(vsizer_all)#本作品作者吴宇航
            def OnclickSubmit(self,event):#本作品作者吴宇航
                message = ""#本作品作者吴宇航
                username = self.text_user.GetValue()  #本作品作者吴宇航
                if username == "":#本作品作者吴宇航
                    message = '检测到网址空白'#本作品作者吴宇航
                    wx.MessageBox(message)#本作品作者吴宇航
                else:#本作品作者吴宇航
                    main(username)#本作品作者吴宇航
            def OnclickCancel(self,event):#本作品作者吴宇航
                self.text_user.SetValue("") #本作品作者吴宇航
            def baidu(self,event):#本作品作者吴宇航
                message = ""#本作品作者吴宇航
                username = self.text_user.GetValue()#本作品作者吴宇航
                if username == "":#本作品作者吴宇航
                    message = '检测到内容空白'#本作品作者吴宇航
                    wx.MessageBox(message)#本作品作者吴宇航
                else:#本作品作者吴宇航
                    x='https://www.baidu.com/s?ie=UTF-8&wd='+username#本作品作者吴宇航
                    main(x)#本作品作者吴宇航
            def gx(self,event):#本作品作者吴宇航
                message = """版本:终结版#本作品作者吴宇航
                更新:哎，我不说，我就是玩儿#本作品作者吴宇航
                """#本作品作者吴宇航
                wx.MessageBox(message)#本作品作者吴宇航
            def bing(self,event):#本作品作者吴宇航
                message = ""#本作品作者吴宇航
                username = self.text_user.GetValue()#本作品作者吴宇航
                if username == "":#本作品作者吴宇航
                    message = '检测到内容空白'#本作品作者吴宇航
                    wx.MessageBox(message)#本作品作者吴宇航
                else:#本作品作者吴宇航
                    x='https://cn.bing.com/search?q='+username#本作品作者吴宇航
                    main(x)#本作品作者吴宇航
            def s(self,event):#本作品作者吴宇航
                message = ""#本作品作者吴宇航
                username = self.text_user.GetValue()#本作品作者吴宇航
                if username == "":#本作品作者吴宇航
                    message = '检测到内容空白'#本作品作者吴宇航
                    wx.MessageBox(message)#本作品作者吴宇航
                else:#本作品作者吴宇航
                    x='https://www.so.com/s?ie=utf-8&fr=none&src=360sou_newhome&q='+username#本作品作者吴宇航
                    main(x)#本作品作者吴宇航
            def sougou(self,event):#本作品作者吴宇航
                message = ""#本作品作者吴宇航
                username = self.text_user.GetValue()#本作品作者吴宇航
                if username == "":#本作品作者吴宇航
                    message = '检测到内容空白'#本作品作者吴宇航
                    wx.MessageBox(message)#本作品作者吴宇航
                else:#本作品作者吴宇航
                    x='https://www.sogou.com/web?query='+username#本作品作者吴宇航
                    main(x)#本作品作者吴宇航
            def bdbk(self,event):#本作品作者吴宇航
                message = ""#本作品作者吴宇航
                username = self.text_user.GetValue()#本作品作者吴宇航
                if username == "":#本作品作者吴宇航
                    message = '检测到内容空白'#本作品作者吴宇航
                else:#本作品作者吴宇航
                    a=username#本作品作者吴宇航
                    message = download(a)#本作品作者吴宇航
                    # url = 'http://baike.baidu.com/item/{}'.format(a)#本作品作者吴宇航
                    # html_cont = download(url)#本作品作者吴宇航
                    # try:#本作品作者吴宇航
                    #     data = get_data(html_cont)#本作品作者吴宇航
                    #     data = re.sub(r'<([\s\S]*?)>|&nbsp;|\n','',data)#本作品作者吴宇航
                    #     with open(a+'.txt', 'w', encoding='utf-8') as f:#本作品作者吴宇航
                    #         f.write(data)#本作品作者吴宇航
                    #         f.close()#本作品作者吴宇航
                    # except:#本作品作者吴宇航
                    #     data='没有这个词'#本作品作者吴宇航
                    # message=data#本作品作者吴宇航
                wx.MessageBox(message)#本作品作者吴宇航
            def km(self,event):#本作品作者吴宇航
                message = ""#本作品作者吴宇航
                username = self.text_user.GetValue()#本作品作者吴宇航
                if username == "":#本作品作者吴宇航
                    message = '检测到内容空白'#本作品作者吴宇航
                else:#本作品作者吴宇航
                    a=username#本作品作者吴宇航
                    if a =="飞机":#本作品作者吴宇航
                        b='''#本作品作者吴宇航
                        搜索：飞机#本作品作者吴宇航
                        ┌──────────┐#本作品作者吴宇航
                        │----------│#本作品作者吴宇航
                        │   飞机   │#本作品作者吴宇航
                        │----------│#本作品作者吴宇航
                        └──────────┘#本作品作者吴宇航
                        #本作品作者吴宇航
                        飞机（aeroplane,airplane）是指具有一具或多具发动机的动力装置产生前进的推力或拉力，由机身的固定机翼产生升力，在大气层内飞行的重于空气的航空器。  飞机是20世纪初最重大的发明之一，公认由美国人莱特兄弟发明。他们在1903年12月17日进行的飞行作为“第一次重于空气的航空器进行的受控的持续动力飞行”被国际航空联合会（FAI）所认可，同年他们创办了“莱特飞机公司”。自从飞机发明以后，飞机日益成为现代文明不可缺少的工具。它深刻的改变和影响了人们的生活，开启了人们征服蓝天历史。 #本作品作者吴宇航
                        '''#本作品作者吴宇航
                    elif a == "C++" or a == "c++":#本作品作者吴宇航
                        b='''#本作品作者吴宇航
                        搜索：C++#本作品作者吴宇航
                        ┌──────────┐  #本作品作者吴宇航
                        │----------│  #本作品作者吴宇航
                        │   C++    │  编程语言?#本作品作者吴宇航
                        │----------│#本作品作者吴宇航
                        └──────────┘  #本作品作者吴宇航
                        C++是一种面向对象的计算机程序设计语言，由美国AT&T贝尔实验室的本贾尼·斯特劳斯特卢普博士发明并实现（最初这种语言被称作“C with Classes”带类的C）。#本作品作者吴宇航
                        它是一种静态数据类型检查的、支持多重编程范式的通用程序设计语言。它支持过程化程序设计、数据抽象、面向对象程序设计、泛型程序设计等多种程序设计风格。\nC++是C语言的继承，进一步扩充和完善了C语言，成为一种面向对象的程序设计语言。C++这个词在中国大陆的程序员圈子中通常被读做“C++”，而西方的程序员通常读做“C plus plus”，“CPP”。#本作品作者吴宇航
                        '''#本作品作者吴宇航
                    elif a == "857" or  a == "八五七":#本作品作者吴宇航
                        b='''#本作品作者吴宇航
                        搜索：857#本作品作者吴宇航
                        ┌──────────┐#本作品作者吴宇航
                        │----------│#本作品作者吴宇航
                        │    857   │     网络流行语#本作品作者吴宇航
                        │----------│#本作品作者吴宇航
                        └──────────┘    #本作品作者吴宇航
                        857，网络流行语，指蹦迪神曲《bow chi bow》和《feel my bass》副歌里面的空耳，现已发展成蹦迪的代名词。#本作品作者吴宇航
                        '''#本作品作者吴宇航
                    elif a == "baidu" or a == "百度":#本作品作者吴宇航
                        b='''#本作品作者吴宇航
                        搜索：百度/baidu#本作品作者吴宇航
                        ┌──────────┐#本作品作者吴宇航
                        │----------│ #本作品作者吴宇航
                        │   百度   │? 全球最大的中文搜索引擎、最大的中文网站#本作品作者吴宇航
                        │----------│#本作品作者吴宇航
                        └──────────┘#本作品作者吴宇航
                        百度，全球最大的中文搜索引擎、最大的中文网站。百度二字，来自于八百年前南宋词人辛弃疾的一句词：众里寻他千百度。这句话描述了词人对理想的执着追求。1999年底，身在美国硅谷的李彦宏看到了中国互联网及中文搜索引擎服务的巨大发展潜力，抱着技术改变世界的梦想，他毅然辞掉硅谷的高薪工作，携搜索引擎专利技术，于 2000年1月1日在中关村创建了百度公司。#本作品作者吴宇航
                        '''#本作品作者吴宇航
                    elif a == "易语言" or a == "EPL" or a == "erl" or a == "Erl":#本作品作者吴宇航
                        b='''#本作品作者吴宇航
                        搜索：易语言#本作品作者吴宇航
                        ┌──────────┐#本作品作者吴宇航
                        │----------│#本作品作者吴宇航
                        │  易语言  │     专为中国人设置的简单编程语言")#本作品作者吴宇航
                        │----------│#本作品作者吴宇航
                        └──────────┘  #本作品作者吴宇航
                        易语言（EPL）是一门以中文作为程序代码编程语言，其以“易”著称，创始人为吴涛。易语言早期版本的名字为E语言。其最早的版本的发布可追溯至2000年9月11日。创造易语言的初衷是进行用中文来编写程序的实践，方便中国人以中国人的思维编写程序，并不用再去学习西方思维。易语言的诞生极大的降低了编程的门槛和学习的难度。从2000年以来，易语言已经发展到一定的规模，功能上、用户数量上都十分可观。#本作品作者吴宇航
                        '''#本作品作者吴宇航
                    #本作品作者吴宇航
                    #本作品作者吴宇航
                    elif a == "CEO" or a == "ceo":#本作品作者吴宇航
                        b='''#本作品作者吴宇航
                        搜索：CEO#本作品作者吴宇航
                        ┌───────────┐#本作品作者吴宇航
                        │-----------│#本作品作者吴宇航
                        │    CEO    │  Chief Executive Officer#本作品作者吴宇航
                        │-----------│#本作品作者吴宇航
                        └───────────┘   #本作品作者吴宇航
                        首席执行官（Chief Executive Officer)职位名称，是在一个企业中负责日常事务的最高行政官员，主司企业行政事务，故又称作司政、行政总裁、总经理或最高执行长。在政治组织机构中，首席执行官为政府首脑，相当于部长会议主席、总理、首相、阁揆、行政院院长、政府主席等级别的行政事务最高负责高官。#本作品作者吴宇航
                        '''#本作品作者吴宇航
                    elif a == "钉钉":#本作品作者吴宇航
                        b='''#本作品作者吴宇航
                        搜索：钉钉#本作品作者吴宇航
                        ┌──────────┐#本作品作者吴宇航
                        │----------│#本作品作者吴宇航
                        │   钉钉   │  专为中国企业打造的免费沟通和协同的多端平台#本作品作者吴宇航
                        │----------│#本作品作者吴宇航
                        └──────────┘   #本作品作者吴宇航
                        钉钉（DingTalk）是阿里巴巴集团专为中国企业打造的免费沟通和协同的多端平台 [1]  ，提供PC版，Web版，Mac版和手机版，支持手机和电脑间文件互传。#本作品作者吴宇航
                        '''#本作品作者吴宇航
                    elif a == "乔布斯" or a == "史蒂夫·乔布斯" or a == "史蒂夫乔布斯 ":#本作品作者吴宇航
                        b='''#本作品作者吴宇航
                        搜索：史蒂夫·乔布斯#本作品作者吴宇航
                        ┌─────────────┐#本作品作者吴宇航
                        │-------------│#本作品作者吴宇航
                        │史蒂夫·乔布斯│ 美国发明家、企业家、美国苹果公司联合创始人#本作品作者吴宇航
                        │-------------│#本作品作者吴宇航
                        └─────────────┘   #本作品作者吴宇航
                        史蒂夫·乔布斯  （Steve Jobs，1955年2月24日—2011年10月5日   ），出生于美国加利福尼亚州旧金山，美国发明家、企业家、美国苹果公司联合创始人。 #本作品作者吴宇航
                        乔布斯被认为是计算机业界与娱乐业界的标志性人物，他经历了苹果公司几十年的起落与兴衰，先后领导和推出了麦金塔计算机（Macintosh）、iMac、iPod、iPhone、iPad等风靡全球的电子产品，深刻地改变了现代通讯、娱乐、生活方式。乔布斯同时也是前Pixar动画公司的董事长及行政总裁。#本作品作者吴宇航
                        '''#本作品作者吴宇航
                    elif a == "比尔盖茨" or a == "比尔" or a == "盖茨" or a == "Bill Gates" or a == "bill gates" or a == "Bill gates" or a == "billgates" or a == "BillGates" or a == "Billgates":#本作品作者吴宇航
                        b='''#本作品作者吴宇航
                        搜索：比尔盖茨#本作品作者吴宇航
                        ┌─────────────┐#本作品作者吴宇航
                        │-------------│#本作品作者吴宇航
                        │  比尔·盖茨  │ 比尔·盖茨 [1]  （Bill Gates），全名威廉·亨利·盖茨三世，简称比尔或盖茨#本作品作者吴宇航
                        │-------------│#本作品作者吴宇航
                        └─────────────┘#本作品作者吴宇航
                        比尔·盖茨 [1]  （Bill Gates），全名威廉·亨利·盖茨三世，简称比尔或盖茨。1955年10月28日出生于美国华盛顿州西雅图，企业家、软件工程师、慈善家、微软公司创始人。曾任微软董事长、CEO和首席软件设计师。#本作品作者吴宇航
                        '''#本作品作者吴宇航
                    #本作品作者吴宇航
                    #本作品作者吴宇航
                    #本作品作者吴宇航
                    #本作品作者吴宇航
                    #本作品作者吴宇航
                    #本作品作者吴宇航
                    elif a == "Windows" or a == "windows":#本作品作者吴宇航
                        b='''#本作品作者吴宇航
                        搜索：Windows#本作品作者吴宇航
                        ┌───────────┐#本作品作者吴宇航
                        │-----------│#本作品作者吴宇航
                        │  Windows  │   Microsoft Windows操作系统/美国微软公司研发的一套操作系统#本作品作者吴宇航
                        │-----------│#本作品作者吴宇航
                        └───────────┘  #本作品作者吴宇航
                        MicrosoftWindows操作系统是美国微软公司研发的一套操作系统，它问世于1985年，起初仅仅是Microsoft-DOS模拟环境，后续的系统版本由于微软不断的更新升级，不但易用，也当前应用最广泛的操作系统。 [1] Windows采用了图形化模式GUI，比起从前的Dos需要输入指令使用的方式，更为人性化。随着计算机硬件和软件的不断升级，微软的 Windows也在不断升级，从架构的16位、32位再到64位,系统版本从最初的 Windows1.0到大家熟知的 Windows95、 Windows98、 Windows2000、 Windows XP、 Windows Vista、 Windows7、Windows8、Windows8.1、Windows 10和Windows Server服务器企业级操作系统，微软一直在致力于Windows操作系统的开发和完善。 [1]#本作品作者吴宇航
                        '''#本作品作者吴宇航
                    elif a == "编程" or a == "biancheng":#本作品作者吴宇航
                        b='''#本作品作者吴宇航
                        搜索：编程#本作品作者吴宇航
                        ┌──────────┐  #本作品作者吴宇航
                        │----------│  #本作品作者吴宇航
                        │   编程   │  编程#本作品作者吴宇航
                        │----------│  #本作品作者吴宇航
                        └──────────┘  #本作品作者吴宇航
                        编程（biān chéng）是编定程序的中文简称，就是让计算机代为解决某个问题，对某个计算体系规定一定的运算方式，使计算体系按照该计算方式运行，并最终得到相应结果的过程。#本作品作者吴宇航
                        '''#本作品作者吴宇航
                    elif a == "猿辅导":#本作品作者吴宇航
                        b='''#本作品作者吴宇航
                        搜索：猿辅导#本作品作者吴宇航
                        ┌──────────┐#本作品作者吴宇航
                        │----------│#本作品作者吴宇航
                        │  猿辅导  │#本作品作者吴宇航
                        │----------│#本作品作者吴宇航
                        └──────────┘#本作品作者吴宇航
                        截至2020年1月，猿辅导在线教育全国累计用户数突破4亿。(还不是被疫情逼的）) [1] 公司旗下拥有猿辅导、小猿搜题、猿题库、小猿口算、斑马AI课等多款在线教育产品。 [2-3] 猿辅导提供中小学全学科的课程，全国任何地区的中小学生，都可在家上名师直播课 [4]  。2019年6月11日，猿辅导入选“2019福布斯中国最具创新力企业榜”。 [5-6] 2019年12月16日，猿辅导、小猿搜题、猿题库、小猿口算、斑马英语列入第一批教育App备案名单。 [7] 猿辅导创立于2012年 [2]  ，顺利完成由IDG资本、高瓴资本、博裕资本、华平投资、腾讯等知名基金、巨头公司领投的多轮融资，估值超过78亿美元。 [8]  是K-12（覆盖学前到12年义务教育）在线教育首个独角兽公司 [9]  ，“2019胡润品牌榜-最具价值中国品牌”。#本作品作者吴宇航
                        '''#本作品作者吴宇航
                    elif a == "月高工作室":#本作品作者吴宇航
                        b='''#本作品作者吴宇航
                        搜索：月高工作室#本作品作者吴宇航
                        ┌────────────┐#本作品作者吴宇航
                        │------------│#本作品作者吴宇航
                        │工作室许可证│#本作品作者吴宇航
                        │------------│#本作品作者吴宇航
                        └────────────┘#本作品作者吴宇航
                        月高工作室于2019年11月23日由创始人潘夕习成立，目前具有代表作《跳舞的线》。#本作品作者吴宇航
                        '''#本作品作者吴宇航
                    elif a == "oppo" or a == "OPPO" or a == "Oppo":#本作品作者吴宇航
                        b='''#本作品作者吴宇航
                        搜索：OPPO#本作品作者吴宇航
                        ┌──────────┐#本作品作者吴宇航
                        │----------│#本作品作者吴宇航
                        │   OPPO   │        开启探索和引领至美科技之旅#本作品作者吴宇航
                        │----------│#本作品作者吴宇航
                        └──────────┘#本作品作者吴宇航
                        OPPO于2008年推出第一款“笑脸手机”，由此开启探索和引领至美科技之旅。今天，OPPO凭借以Find和R系列手机为核心的智能终端产品，以及OPPO+等互联网服务，让全球消费者尽享至美科技。#本作品作者吴宇航
                        '''#本作品作者吴宇航
                    elif a == "安卓" or a == "Android" or a == "android" or a == "anzhuo":#本作品作者吴宇航
                        b='''#本作品作者吴宇航
                        搜索：安卓#本作品作者吴宇航
                        ┌──────────┐#本作品作者吴宇航
                        │----------│#本作品作者吴宇航
                        │   安卓   │         自由及开放源代码的操作系统#本作品作者吴宇航
                        │----------│#本作品作者吴宇航
                        └──────────┘#本作品作者吴宇航
                        安卓是一种基于Linux内核（不包含GNU组件）的自由及开放源代码的操作系统。主要使用于移动设备，如智能手机和平板电脑，由美国Google公司和开放手机联盟领导及开发。Android操作系统最初由Andy Rubin开发，主要支持手机。#本作品作者吴宇航
                        '''#本作品作者吴宇航
                    elif a == "致所有人":#本作品作者吴宇航
                        b='''#本作品作者吴宇航
                        我不知道是谁引起的这个抄袭之风，连有些工作室都开始抄袭了，希望大家多多举报那些抄袭的作品，抄袭出来的毕竟不是自己的，自己做出来的作品会让你感到有所成就，而其他抄袭的作品会找到所有人的唾弃，希望那些抄袭的人不要再继续抄下去了，抄袭有意思吗》？#本作品作者吴宇航
                        我想有些不要脸的人应该会说“有”，因为他们就知道抄！啊哈哈，抄袭只会害了自己，不会害了其他人，只会害了抄袭的自己呀！哎，还请抄袭的人不要再这样下去了#本作品作者吴宇航
                        ！@闪翼抄袭室，请你们不要再抄袭了！请马上撤回抄袭作品！谢谢配合！#本作品作者吴宇航
                        '''#本作品作者吴宇航
                    elif a == "星光工作室" or a == "星光":#本作品作者吴宇航
                        b='''#本作品作者吴宇航
                        搜索：星光工作室#本作品作者吴宇航
                        ┌────────────┐#本作品作者吴宇航
                        │------------│#本作品作者吴宇航
                        │工作室许可证│#本作品作者吴宇航
                        │------------│#本作品作者吴宇航
                        └────────────┘#本作品作者吴宇航
                        关于 Star light （S.L.）星光工作室2020年2月28日以学而思编程为启动平台创立，主要建立教学部、科技研发部，以作品优秀著称,欢迎大家加入。#本作品作者吴宇航
                        优秀的作品全学而思公认最水的工作室(滑稽)，作品涉及爬虫、pygame、tkinter和python终端输出。不断创新创新永远是我们的口号，探索探索再探索，学习学习再学习！技术党拥有涉及许多方面的技术人才，打造良好的学习环境。Idea创意使我们不甘平庸，创意使我们继续向前！#本作品作者吴宇航
                        '''#本作品作者吴宇航
                    elif a == "人类" or a == "renlei":#本作品作者吴宇航
                        b='''#本作品作者吴宇航
                        搜索：人类#本作品作者吴宇航
                        ┌──────────┐#本作品作者吴宇航
                        │----------│#本作品作者吴宇航
                        │   人类   │   高智商生物#本作品作者吴宇航
                        │----------│#本作品作者吴宇航
                        └──────────┘#本作品作者吴宇航
                        智人（学名：Homo sapiens），是人属下的唯一现存物种。形态特征比直立人更为进步。分为早期智人和晚期智人。#本作品作者吴宇航
                        早期智人过去曾叫古人，生活在距今25万～4万年前，主要特征是脑容量大，在1300毫升以上；眉嵴发达，前额较倾斜，枕部突出，鼻部宽扁，颌部前突。一般认为是由直立人进化来的，但有争议 [1]  认为直立人在后来崛起的智人（现代人）走出非洲后灭绝或在此之前就灭绝了。#本作品作者吴宇航
                        晚期智人（新人）是解剖结构上的现代人。大约从距今四五万年前开始出现。两者形态上的主要差别在于前部牙齿和面部减小，眉嵴减弱，颅高增大，到现代人则更加明显。晚期智人臂不过膝，体毛退化，有语言和劳动，有社会性和阶级性。有三种类型的材料来研究人从哪里来这个问题：基因、化石、语言文化。其中语言文化一般不能超过新石器时代。很多形态特征并不与种系差异相关。#本作品作者吴宇航
                        ''' #本作品作者吴宇航
                    elif a == "霍格沃兹工作室":#本作品作者吴宇航
                        b='''#本作品作者吴宇航
                        搜索：霍格沃兹工作室#本作品作者吴宇航
                        ┌────────────┐#本作品作者吴宇航
                        │------------│#本作品作者吴宇航
                        │工作室许可证│#本作品作者吴宇航
                        │------------│#本作品作者吴宇航
                        └────────────┘#本作品作者吴宇航
                        霍格沃茨工作室在2020年3月9日成立，室长是陈张远致，随后，大批优秀成员进入。我们的精选作品：分院仪式，作者方政：https://code.xueersi.com/home/project/detail?lang=code&pid=4761562&version=python&form=python&langType=python密室大逃脱，作者茜烨：https://code.xueersi.com/home/project/detail?lang=code&pid=4887936&version=cpp&form=cpp&langType=cpp最强大脑特约版，作者李承骏、方政&金恺文（荐）：https://code.xueersi.com/home/project/detail?lang=code&pid=4982950&version=python&form=python&langType=python想要霍格沃茨四大学院的标志吗，作者陈张远致：https://code.xueersi.com/home/project/detail?lang=scratch&pid=5204731&version=3.0&langType=scratch更多优秀作品在我们的优秀作品大全！！（走过路过不要错过）里面#本作品作者吴宇航
                        '''#本作品作者吴宇航
                    elif a== "火焰工作室":#本作品作者吴宇航
                        b='''#本作品作者吴宇航
                        搜索：火焰工作室#本作品作者吴宇航
                        ┌────────────┐#本作品作者吴宇航
                        │------------│#本作品作者吴宇航
                        │工作室许可证│#本作品作者吴宇航
                        │------------│#本作品作者吴宇航
                        └────────────┘#本作品作者吴宇航
                        火焰工作室成立于2019-08-18日,是社区中较早的优秀的工作室,主攻python,以终端输出的美观与科技感而出名,目前最高观看8949点赞509,是值得认可的工作室!#本作品作者吴宇航
                        '''#本作品作者吴宇航
                    elif a == "浏览器" or a == "liulanqi":#本作品作者吴宇航
                        b='''#本作品作者吴宇航
                        搜索：浏览器#本作品作者吴宇航
                        ┌──────────┐#本作品作者吴宇航
                        │----------│#本作品作者吴宇航
                        │  浏览器  │#本作品作者吴宇航
                        │----------│#本作品作者吴宇航
                        └──────────┘#本作品作者吴宇航
                        浏览器是用来显示在万维网或局域网等内的文字、图像及其他信息的软件，它还可以让用户与这些文件进行交互操作。浏览器是电脑上网时经常使用到的应用软件，浏览器正是Internet时代的产物，随着电脑操作系统的普及、Internet的全球连接及人们对信息需求的爆炸式增长，为浏览器的诞生和兴起提供了强大的动力，同时它也标志着互联网时代的来临 [1]#本作品作者吴宇航
                        '''#本作品作者吴宇航
                    elif a == "诺耀工作室":#本作品作者吴宇航
                        b='''#本作品作者吴宇航
                        搜索：诺耀工作室#本作品作者吴宇航
                        ┌────────────┐#本作品作者吴宇航
                        │------------│#本作品作者吴宇航
                        │工作室许可证│#本作品作者吴宇航
                        │------------│#本作品作者吴宇航
                        └────────────┘#本作品作者吴宇航
                        诺耀工作室创建于2020年3月13日，由创始人李佳诺所建。2020年3月17日开始有了自己的官网：http://nuoyaogzsguanfang.cn，在短期内有了许多的成就。也在2020年4月16日创建了“诺耀工作室”的微信公众号。目前在学而思，网易卡塔，小码王等社区内总共作品超过60个！！！#本作品作者吴宇航
                        '''#本作品作者吴宇航
                    elif a == "梦想之星工作室":#本作品作者吴宇航
                        b='''#本作品作者吴宇航
                        搜索：梦想之星工作室#本作品作者吴宇航
                        ┌────────────┐#本作品作者吴宇航
                        │------------│#本作品作者吴宇航
                        │工作室许可证│#本作品作者吴宇航
                        │------------│#本作品作者吴宇航
                        └────────────┘#本作品作者吴宇航
                        相当于半个漫威，因为漫威的三大副室长全在这里，这里的人都是大佬，技术很NB#本作品作者吴宇航
                        '''#本作品作者吴宇航
                    elif a == "星斩工作室":#本作品作者吴宇航
                        b='''#本作品作者吴宇航
                        搜索：星斩工作室#本作品作者吴宇航
                        ┌────────────┐#本作品作者吴宇航
                        │------------│#本作品作者吴宇航
                        │工作室许可证│#本作品作者吴宇航
                        │------------│#本作品作者吴宇航
                        └────────────┘#本作品作者吴宇航
                        星斩工作室成立于2020.1.30。拥有成员20+，许多语言的程序员。官方网站：www.starcutc.com。官方邮箱：starcutcn@163.com、starcut@starcutc.com。在学而思、编程猫、卡搭社区都有人员。#本作品作者吴宇航
                        '''#本作品作者吴宇航
                    elif a == "张奥程"or a == "zac":#本作品作者吴宇航
                        b="张奥程，男，原漫威副室长，原梦想之星副室长，会html，css，js，ddos，cc，bat，vbs，e，py，c++，sc，很牛逼的一个人"#本作品作者吴宇航
                    elif a == "新型冠状病毒"or a == "新冠肺炎"or a == "新冠":#本作品作者吴宇航
                        b="2019新型冠状病毒，2020年1月12日被世界卫生组织命名为2019-nCoV [1]  ，2020年2月11日被国际病毒分类委员会命名为SARS-CoV-2 [2]  。冠状病毒是一个大型病毒家族，已知可引起感冒以及中东呼吸综合征（MERS）和严重急性呼吸综合征（SARS）等较严重疾病。新型冠状病毒是以前从未在人体中发现的冠状病毒新毒株。"#本作品作者吴宇航
                    elif a == "scratch" or a == "Scratch" :#本作品作者吴宇航
                        b="Scratch是一款由麻省理工学院(MIT) 设计开发的少儿编程工具。其特点是:使用者可以不认识英文单词，也可以不会使用键盘。构成程序的命令和参数通过积木形状的模块来实现。用鼠标拖动模块到程序编辑栏就可以了。右边的部分是编辑好的程序代码，中间是可以用来选择的功能模块，左边上部是程序预览和运行窗口，左边下部是角色窗口。"#本作品作者吴宇航
                    elif a == "thinkpad" or a == "Thinkpad" or a == "思考本":#本作品作者吴宇航
                        b="ThinkPad（思考本）是IBM PC事业部旗下创立的便携式计算机品牌，凭借坚固和可靠的特性在业界享有很高声誉。2005年被联想（Lenovo）收购，ThinkPad商标为联想所有。ThinkPad自问世以来一直保持着黑色的经典外观并对技术有着自己独到的见解，如：TrackPoint（指点杆，俗称小红帽）、ThinkLight键盘灯、全尺寸键盘和APS（Active Protection System，主动保护系统）。"#本作品作者吴宇航
                    elif a == "Python" or a == "python":#本作品作者吴宇航
                        b="Python是一种计算机程序设计语言。是一种面向对象的动态类型语言，最初被设计用于编写自动化脚本(shell)，随着版本的不断更新和语言新功能的添加，越来越多被用于独立的、大型项目的开发。"#本作品作者吴宇航
                    elif a == "css" or a == "CSS":#本作品作者吴宇航
                        b="层叠样式表(英文全称：Cascading Style Sheets)是一种用来表现HTML（标准通用标记语言的一个应用）或XML（标准通用标记语言的一个子集）等文件样式的计算机语言。CSS不仅可以静态地修饰网页，还可以配合各种脚本语言动态地对网页各元素进行格式化。 CSS 能够对网页中元素位置的排版进行像素级精确控制，支持几乎所有的字体字号样式，拥有对网页对象和模型样式编辑的能力。"#本作品作者吴宇航
                    elif a == "HTML" or a == "html"or a == "Html":#本作品作者吴宇航
                        b="HTML（超文本标记语言）是用于在Internet上显示Web页面的主要标记语言。网页由HTML组成，用于通过Web浏览器显示文本，图像或其他资源。HTML文件的文件扩展名为.htm或.html。"#本作品作者吴宇航
                    elif a == "PHP" or a == "Php" or a == "php":#本作品作者吴宇航
                        b="PHP是PHP的递归首字母缩写：Hypertext Preprocessor，一种用于创建动态和交互式HTML网页的脚本语言。当网站访问者打开页面时，服务器处理PHP命令，然后将结果发送到访问者的浏览器。"#本作品作者吴宇航
                    elif a == "RCD" or a == "rcd":#本作品作者吴宇航
                        b("RCD（room temperature catalytic decomposition，室温催化分解），在室温条件下利用空气中的热量长期稳定的将空气中甲醛污染物催化氧化成水和二氧化碳。") #本作品作者吴宇航
                        sleep(3)#本作品作者吴宇航
                        system("clear")#本作品作者吴宇航
                    elif a == "JavaScript" or a == "js" or a=="javascript" or a=="JS" or a=="Script" or a=="script":#本作品作者吴宇航
                        b="JavaScript（简称“JS”） 是一种具有函数优先的轻量级，解释型或即时编译型的编程语言。虽然它是作为开发Web页面的脚本语言而出名的，但是它也被用到了很多非浏览器环境中，JavaScript 基于原型编程、多范式的动态脚本语言，并且支持面向对象、命令式和声明式（如函数式编程）风格。 [1] JavaScript在1995年由Netscape公司的Brendan Eich，在网景导航者浏览器上首次设计实现而成。因为Netscape与Sun合作，Netscape管理层希望它外观看起来像Java，因此取名为JavaScript。但实际上它的语法风格与Self及Scheme较为接近。 [2] JavaScript的标准是ECMAScript 。截至 2012 年，所有浏览器都完整的支持ECMAScript 5.1，旧版本的浏览器至少支持ECMAScript 3 标准。2015年6月17日，ECMA国际组织发布了ECMAScript 的第六版，该版本正式名称为 ECMAScript 2015，但通常被称为ECMAScript 6 或者ES6。"#本作品作者吴宇航
                    elif a == "华为" or a == "HUAWEI" or a == "huawei":#本作品作者吴宇航
                        b='''#本作品作者吴宇航
                        华为技术有限公司#本作品作者吴宇航
                        华为消费者业务产品全面覆盖手机、移动宽带终端、终端云等，凭借自身的全球化网络优势、全球化运营能力，致力于将最新的科技带给消费者，让世界各地享受到技术进步的喜悦，以行践言，实现梦想。#本作品作者吴宇航
                        '''#本作品作者吴宇航
                    elif a == "apple" or a == "Apple":#本作品作者吴宇航
                        b='''#本作品作者吴宇航
                        中文意思：苹果#本作品作者吴宇航
                        苹果公司（Apple Inc. ）是美国一家高科技公司。由史蒂夫·乔布斯、斯蒂夫·沃兹尼亚克和罗·韦恩(Ron Wayne)等人于1976年4月1日创立，并命名为美国苹果电脑公司（Apple Computer Inc. ），2007年1月9日更名为苹果公司，总部位于加利福尼亚州的库比蒂诺。#本作品作者吴宇航
                        苹果公司1980年12月12日公开招股上市，2012年创下6235亿美元的市值记录，截至2014年6月，苹果公司已经连续三年成为全球市值最大公司。苹果公司在2016年世界500强排行榜中排名第9名。   2013年9月30日，在宏盟集团的“全球最佳品牌”报告中，苹果公司超过可口可乐成为世界最有价值品牌。2014年，苹果品牌超越谷歌（Google），成为世界最具价值品牌。#本作品作者吴宇航
                        2016年9月8日凌晨1点，2016苹果秋季新品发布会在美国旧金山的比尔·格雷厄姆市政礼堂举行 [2]  。10月，苹果成为2016年全球100大最有价值品牌第一名。#本作品作者吴宇航
                        2017年1月6日早晨8点整，“红色星期五”促销活动在苹果官网正式上线，瞬间大量用户涌入官网进行抢购，仅两分钟所有参与活动的耳机便被抢光；2月，Brand Finance发布2017年度全球500强品牌榜单，苹果排名第二； [3]  6月7日，2017年《财富》美国500强排行榜发布，苹果排名第3位； [4]  7月20日，2017年世界500强排名第9位。  #本作品作者吴宇航
                        2018年12月18日，世界品牌实验室编制的《2018世界品牌500强》揭晓，苹果排名第3位。 2018年8月2日晚间，苹果盘中市值首次超过1万亿美元，股价刷新历史最高位至203.57美元。   入选2019《财富》世界500强、 2019福布斯全球数字经济100强榜第1位 #本作品作者吴宇航
                        '''#本作品作者吴宇航
                    elif a == "秦浩铭" or a == "漫威室长" or a == "原漫威室长":#本作品作者吴宇航
                        b="漫威原室长，本作品的词库提供方之一，创造了很多奇迹。"#本作品作者吴宇航
                    elif  a == "微软" or a == "微软公司" or a == "Microsoft":#本作品作者吴宇航
                        b='''#本作品作者吴宇航
                        微软  （英文名称：Microsoft；中文名称：微软公司或美国微软公司）始建于1975年，是一家美国跨国科技公司，也是世界PC（Personal Computer，个人计算机）软件开发的先导，由比尔·盖茨与保罗·艾伦创办于1975年，公司总部设立在华盛顿州的雷德蒙德（Redmond，邻近西雅图）。以研发、制造、授权和提供广泛的电脑软件服务业务为主。#本作品作者吴宇航
                        最为著名和畅销的产品为Microsoft Windows操作系统和Microsoft Office系列软件，目前是全球最大的电脑软件提供商。#本作品作者吴宇航
                        2018年4月22日，2017年全球最赚钱企业排行榜第15。   2018年5月29日，《2018年BrandZ全球最具价值品牌100强》第4位。 2018年7月19日，《财富》世界500强排行榜位列71位。   2018年12月18日，《2018世界品牌500强》第4位。#本作品作者吴宇航
                        2019年6月，微软悄然删除其MS Celeb人脸识别数据库，微软称该数据库是全球最大的公开人脸识别数据库。   2019年7月，《财富》世界500强排行榜发布，微软位列60位。 2019福布斯全球数字经济100强榜排名第2位。  2019年10月，Interbrand发布的全球品牌百强排名第四位。  2020年1月22日，名列2020年《财富》全球最受赞赏公司榜单第3位。#本作品作者吴宇航
                        '''#本作品作者吴宇航
                    elif a == "迷你世界" or a == "迷你"  or a == "mini":#本作品作者吴宇航
                        b='一款抄袭我的世界的垃圾游戏，玩家都是幼儿园和1、2年级的xxs'#本作品作者吴宇航
                    elif a == "微博" or a == "微型博客" or a == "Wei Bo" or a == "Weibo" or a == "weibo" :#本作品作者吴宇航
                        b="微博（Weibo）是指一种基于用户关系信息分享、传播以及获取的通过关注机制分享简短实时信息的广播式的社交媒体、网络平台，允许用户通过Web、Wap、Mail、App、IM、SMS以及用户可以通过PC、手机等多种移动终端接入，以文字、图片、视频等多媒体形式，实现信息的即时分享、传播互动。2009年8月新浪推出“新浪微博”内测版，成为门户网站中第一家提供微博服务的网站。此外微博还包括腾讯微博，网易微博，搜狐微博等。但如若没有特别说明，微博就是指新浪微博。2014年3月27日晚间，在中国微博领域一枝独秀的新浪微博宣布改名为“微博”，并推出了新的LOGO标识，新浪色彩逐步淡化。2018年8月8日，微博获金运奖年度最佳效果运营奖。"#本作品作者吴宇航
                    elif a == "PEN果" or a == "PEN果公司" or a == "PEN果工作室" or  a== "MOGO" or a == "Mogo" or a == "mogo" or a == "pen果" or a == "Pen果" or a == "PENGUO" or a == "penguo" or a == "Penguo" or a == "PENguo":#本作品作者吴宇航
                        b="PEN果公司，全英文名MOGO，全中文名笔果，旗下有酷喵公司，微软工作室，专攻编程专业，研究技术，成立于2019.6.6。室长【缪子航】"#本作品作者吴宇航
                    elif a == "苹果":#本作品作者吴宇航
                        b="苹果是蔷薇科苹果亚科苹果属植物，其树为落叶乔木。苹果营养价值很高，富含矿物质和维生素，含钙量丰富，有助于代谢掉体内多余盐分，苹果酸可代谢热量，防止下半身肥胖。苹果是一种低热量的食物，每100克产生大约60千卡左右的热量。苹果中营养成分可溶性大，容易被人体吸收，故有“活水”之称。它有利于溶解硫元素，使皮肤润滑柔嫩。"#本作品作者吴宇航
                    elif a == "星河工作室":#本作品作者吴宇航
                        b="暂无介绍。"#本作品作者吴宇航
                    elif a == "Tank Stars" or  a == "tank stars" or a == "Tank stars" or a == "TANK STARS":#本作品作者吴宇航
                        b="《Tank Stars》 是一款动作射击冒险游戏，在这个游戏中，玩家需要寻找对手，然后进行互相射击。游戏采用2D卡通风格画面呈现，游戏支持多人模式，玩家可以与好友一起挑战高分，也有单机挑战，在排行榜寻找对战好友。"#本作品作者吴宇航
                    elif a == "呵呵" or a == "呵呵呵" or a == "呵" :#本作品作者吴宇航
                        b="呵呵是一个汉语词汇，一指笑声的拟声词，二指形容说话声音含混不清。在网络中常表示在否定对方的同时表达嘲讽和不屑，而容易让人误解为嘲讽为【呵呵】本意或主意。"#本作品作者吴宇航
                    elif a == "Mojang" or a == "mojang"  or a == "MOJANG"  or a == "MOJANG AB" or a == "Mojang AB" or a == "MOJANG ab" or a == "mojang ab" or a == "Mojäng Aktiebolag":#本作品作者吴宇航
                        b='''#本作品作者吴宇航
                        Mojang AB（瑞典文：mojäng /mʊˈjɛŋ/）全名Mojäng Aktiebolag（直译为小工具有限公司）是一个位于瑞典的电子游戏开发商，于2009年由马库斯·佩尔松以“Mojang Specifications”之名创立。因开发了沙盒游戏《我的世界》（Minecraft）而成名。此公司已经开发《Scrolls》和《Cobalt》，同时也继续更新《我的世界》。Mojang总部位于瑞典的首都斯德哥尔摩。#本作品作者吴宇航
                        该公司已于2014年9月15日被微软以25亿美元收购。#本作品作者吴宇航
                        '''#本作品作者吴宇航
                    elif a == "酷喵" or a == "酷喵公司" or a == "酷喵工作室" or a == "kumiao":#本作品作者吴宇航
                        b="酷喵公司（kumiao）：PEN果公司旗下工作室，成立于2019.1.1，于2019.6.6加入PEN果公司旗下，室长【缪子航】"#本作品作者吴宇航
                    elif a == "cpb"or a == "Cpb"or a == "CPB"or a == "CPB防栗局"or a == "cpb防栗局"or a == "Cpb防栗局"or a == "SEVA工作室"or a == "SEVA"or a == "seva"or a == "seva工作室":#本作品作者吴宇航
                        b="原名CPB(防栗局)后改名为SEVA，出过许多出名人物和作品。"#本作品作者吴宇航
                    elif a == "漫威工作室" or a == "manwei" or a == "漫威":#本作品作者吴宇航
                        b="漫威工作室创建于2019年10月23日，室长秦浩铭，最多50人左右。"#本作品作者吴宇航
                    elif a == "qq" or a == "QQ":#本作品作者吴宇航
                        b='''#本作品作者吴宇航
                        QQ是腾讯QQ的简称，是一款基于Internet即时通信（IM）软件。目前QQ已经覆盖Microsoft Windows、macOS、Android、iOS、Windows Phone、Linux等多种主流平台。其标志是一只戴着红色围巾的小企鹅。腾讯QQ支持在线聊天、视频通话、点对点断点续传文件、共享文件、网络硬盘、自定义面板、QQ邮箱等多种功能，并可与多种通讯终端相连。#本作品作者吴宇航
                        2017年1月5日，腾讯QQ和美的集团在深圳正式签署战略合作协议，双方将共同构建基于IP授权与物联云技术的深度合作，实现家电产品的连接、对话和远程控制。双方合作的第一步，是共同推出基于QQfamily IP授权和腾讯物联云技术的多款智能家电产品。#本作品作者吴宇航
                        2018年12月12日，QQ发布公告，称由于业务调整，webQQ即将在2019年1月1日停止服务，并提示用户下载QQ客户端   。2019年3月13日起，QQ号码可注销   。#本作品作者吴宇航
                        2019年03月27日，腾讯QQ宣布推出“鹅的20岁”生日庆典特别栏目，第一期分享了那个企鹅图标的“黑历史”。   2019年4月13日，腾讯QQ正式推送了iOS版的v8.0版本更新，将全新的操作界面带给了正式版用户。 #本作品作者吴宇航
                        '''#本作品作者吴宇航
                    elif a == "微信" or a == "weixin" or a == "WeChat" or a == "wechat" or a == "Wechat":#本作品作者吴宇航
                        b='''#本作品作者吴宇航
                        微信 （腾讯公司的通讯服务应用程序） #本作品作者吴宇航
                        微信（WeChat）  是腾讯公司于2011年1月21日推出的一个为智能终端提供即时通讯服务的免费应用程序   ，由张小龙所带领的腾讯广州研发中心产品团队打造 。#本作品作者吴宇航
                        微信支持跨通信运营商、跨操作系统平台通过网络快速发送免费（需消耗少量网络流量）语音短信、视频、图片和文字，同时，也可以使用通过共享流媒体内容的资料和基于位置的社交插件“摇一摇”、“漂流瓶”、“朋友圈”、”公众平台“、”语音记事本“等服务插件。#本作品作者吴宇航
                        截止到2016年第二季度，微信已经覆盖中国 94% 以上的智能手机，月活跃用户达到 8.06亿，   用户覆盖 200 多个国家、超过 20 种语言。   此外，各品牌的微信公众账号总数已经超过 800 万个，移动应用对接数量超过 85000 个，广告收入增至36.79亿人民币 [3]  ，微信支付用户则达到了4亿左右。 [4] #本作品作者吴宇航
                        微信提供公众平台、朋友圈、消息推送等功能，用户可以通过“摇一摇”、“搜索号码”、“附近的人”、扫二维码方式添加好友和关注公众平台，同时微信将内容分享给好友以及将用户看到的精彩内容分享到微信朋友圈。#本作品作者吴宇航
                        2018年4月1日起，微信静态条码支付，每天限额500元。   11月30日起，微信暂时下线漂流瓶服务#本作品作者吴宇航
                        '''#本作品作者吴宇航
                    elif a == "设置" or a == "set up" or a == "Set up": #本作品作者吴宇航
                        b="设置是一个汉语词汇，读音为shè zhì，动词，指设立，布置；放置；装置。出自于黄溍 《圣寿院记》：“器物之须，设置如式。"#本作品作者吴宇航
                    elif a == "学而思网校":#本作品作者吴宇航
                        b=" 学而思网校是好未来旗下的中小学在线教育平台，依托学而思强大的教学资源与师资力量，以实现优秀教育资源的共享为己任，建立起的中小学在线教育平台。\n2016年，学而思网校提出“在线学习更有效”的品牌主张，并进行了全面的课程升级，推出“小班直播+个性化辅导”的先进模式。\n学而思网校注册学生人数已超过600万，遍及全国200多个城市。学而思网校以“在线学习更有效”的理念，开创了“直播+辅导”的模式。学而思网校用科技赋能教育，通过人机对话、语音测评等人工智能科技手段，构建更加完善和个性化的教学产品和服务。" #本作品作者吴宇航
                    elif a =="mc"or a=="Mc"or a=="MC"or a=="minecraft"or a=="Minecraft"or a=="我的世界"or a=="麦块"or a == "我的":#本作品作者吴宇航
                        b='''#本作品作者吴宇航
                        《Minecraft》（官方中文译名《我的世界》，台湾译为《当个创世神》。华人圈亦有人按照谐音称之麦块等），是一款创造生存类游戏，玩家可以在一个三维世界里用各种方块建造建筑物。最初由瑞典人马库斯·阿列克谢·泊松（Markus 'Notch' Persson，很多Minecraft玩家称之为Notch）单独开发，现已成立Mojang公司来开发此游戏。该游戏基于Java平台，开发灵感来自《矮人要塞》（Dwarf Fortress）、《模拟乐园》（Thrillville）、《地城守护者》（Dungeon Keeper）和《Infiniminer》。;现在Minecraft较为流行的四个版本是JAVA版(PC版)，PC中国版，基岩版（PE版），PE中国版（iOS），中国版手游安卓版。有的用Minecraft衍生出很多动画。#本作品作者吴宇航
                        2014年9月15日，Mojang AB以及Minecraft被微软(Microsoft)以25亿美元的价格收购。2017年3月，中国大陆代理商网易正式确定Minecraft中文名为《我的世界》，《我的世界》中国版于2017年4月10开始小规模技术性删档测试，于2017年7月14日开始限号不删档测试，于2017年8月8日开始不限号测试，中国版手游iOS于2017年9月15日公测，手游安卓于2017年10月12日开玩。2018年7月6日，《我的世界》海洋版本正式上线手游。7月10日推出海洋更新版本。2018年11月，《我的世界》1.14测试版更新（至11月20日）。2019年4月，《我的世界》正式更新1.14版本，此版本更新了一个全新的材质包等等。"#本作品作者吴宇航
                        '''#本作品作者吴宇航
                    elif a == "中国" or a == "中华人民共和国":#本作品作者吴宇航
                        b="中国，是以华夏文明为源泉、 中华文化为基础，并以汉族为主体民族的多民族国家，通用汉语、汉字，汉族与少数民族被统称为“ 中华民族”，又自称为炎黄子孙、龙的传人。中国是世界四大文明古国之一，有着悠久的历史，距今约5000年前，以中原地区为中心开始出现聚落组织进而形成 国家，后历经多次民族交融和朝代更迭，直至形成多民族国家的 大一统局面。20世纪初辛亥革命后， 君主政体退出历史舞台，共和政体建立。1949年中华人民共和国成立后，在中国大陆建立了人民代表大会制度的政体。中国文化渊远流长，是东亚文化圈的文化宗主国，在世界文化体系内占有重要地位，由于各地的地理位置、自然条件的差异，人文、经济方面也各有特点。传统文化艺术形式有 诗词、戏曲、书法、国画等，而春节、元宵、清明、端午、中秋、重阳等则是中国重要的传统节日。" #本作品作者吴宇航
                    elif a == "马子锦"or a == "马秃头" or  a =="马没秃":#本作品作者吴宇航
                        b="马子锦，星河室长，又称马秃头。于2019年8月28号建立了星河工作室，他改编了slow函数，这个函数的作用是逐字输出。他十分伟大，伟大到什么程度呢？你看的C++里的逐字输出，就是他做的。" #本作品作者吴宇航
                    elif a == "缪子航": #本作品作者吴宇航
                        b="缪子航，PEN果室长。" #本作品作者吴宇航
                    elif a == "lcj"or a == "李承骏":#本作品作者吴宇航
                        b="李承骏，星光工作室的优秀员工，干劲十足、创意源源不断，最强大脑是他的成名作。"#本作品作者吴宇航
                    elif a=="吴宇航":#本作品作者吴宇航
                        b='''#本作品作者吴宇航
                          吴宇航 #本作品作者吴宇航
                        此作品作者#本作品作者吴宇航
                        '''#本作品作者吴宇航
                    elif a=="三文鱼":#本作品作者吴宇航
                        b="三文鱼（Oncorhynchus），又名大马哈鱼、鲑鱼、撒蒙鱼，属硬骨鱼纲、鲑形目、鲑属，主要分布在大西洋与太平洋、北冰洋交界的水域，属于冷水性的高度洄游鱼类，被国际美食界誉为“冰海之皇”。研究表明，金枪鱼和三文鱼均肉质鲜美，营养丰富，并且富含EPA和DHA等生物活性物质。 三文鱼具有商业价值的品种有30多个，目前最常见的是2种鳟鱼（三文鳟、金鳟）和4种鲑鱼（太平洋鲑、大西洋鲑、北极白点鲑、银鲑）。  "#本作品作者吴宇航
                    elif a=="方便面":#本作品作者吴宇航
                        b="""方便面，又称快餐面、泡面、杯面、快熟面、速食面、即食面，南方一般称为碗面，香港则称之为公仔面，是一种可在短时间之内用热水泡熟食用的面制食品。#本作品作者吴宇航
                        广义上是指一种可在短时间之内用热水泡熟食用的面制食品，有相关的菜肴如归泡面、泡面沙拉等；狭义的方便面上通常指由面饼、调料包及油包组成的销售成品，市面上以袋装和杯或碗装居多。安藤百福在1958年发明方便面，随着生活节奏加快及旅行需要，方便面为现代生活不可或缺的简易食品之一。#本作品作者吴宇航
                        方便面是通过对切丝出来的面条进行蒸煮、油炸，让面条形状固定（一般为方形或圆形），食用前以开水冲泡，溶解调味料，并将面条加热冲泡开，在短时间（一般在3分钟内）内便可食用的即食方便食品。#本作品作者吴宇航
                        如今市场上各种品牌的方便面充斥着各大商场的货架，从大型零售超市到街头的小门头商铺都能够看到它的身影。"""#本作品作者吴宇航
                    elif a=="手机":#本作品作者吴宇航
                        b="手机、全称为移动电话或无线电话，通常称为手机，原本只是一种通讯工具，早期又有大哥大的俗称  ，是可以在较广范围内使用的便携式电话终端，最早是由美国贝尔实验室在1940年制造的战地移动电话机发展而来。1958年，苏联工程师列昂尼德.库普里扬诺维奇发明了ЛК-1型移动电话，1973年，美国摩托罗拉工程师马丁·库帕发明了世界上第一部商业化手机。迄今为止已发展至5G时代了。"#本作品作者吴宇航
                    elif a == "电视剧":#本作品作者吴宇航
                        b="电视剧（ TVplay; teleplay; TV drama; TV serial;）一种专为在电视上播映的演剧形式。它兼容电影、戏剧、 文学、音乐、舞蹈、绘画、造型等现代艺术诸元素，是一种适应电视广播特点、融合舞台和电影艺术的表现方法而形成的现代艺术样式。一般分单本剧和系列剧（电视影集）。电视剧是随着电视广播事业的诞生而发展起来的，在这幕后有一定的推动作用致使一些电视剧网站孕育而生，比较典型的分类电视剧在线观看网站很受大众的喜爱。生活中，电视剧的定义已经狭义化，仅指电视剧集系列，而非其他形式。“电视剧”的概念是中国特有的，在美国称“电视戏剧”，在苏联称“电视故事片”，在日本称“电视小说”。电视剧（又称为剧集、电视戏剧节目、电视戏剧或电视系列剧）是一种适应电视广播特点、融合舞台和电影艺术的表现方法而形成的艺术样式。一般分单元剧和连续剧，利用电视技术制作并通过电视网放映。电视发明后不断普及，最后改变大家对艺术欣赏的方式。电视剧的播放平台一般叫剧场。"#本作品作者吴宇航
                    elif a == "电影":#本作品作者吴宇航
                        b="电影，是由活动照相术和幻灯放映术结合发展起来的一种连续的影像画面，是一门视觉和听觉的现代艺术，也是一门可以容纳戏剧、摄影、绘画、音乐、舞蹈、文字、雕塑、建筑等多种艺术的现代科技与艺术的综合体。但它又具有独自的特征，电影在艺术表现力上不但具有其它各种艺术的特征，又因可以运用蒙太奇（法语：Montage）这种艺术性突跃的电影组接技巧，具有超越其它一切艺术的表现手段，而且影片可以大量复制放映，随着现代社会的发展，电影已深入到人类社会生活的方方面面，是人们日常生活不可或缺的一部分。国务院法制办于2018年2月2日—22日就《电影行政处罚裁量办法（征求意见稿）》向社会公开征求意见。"#本作品作者吴宇航
                    elif a == "巧克力":#本作品作者吴宇航
                        b="巧克力（chocolate也译朱古力），原产中南美洲，其鼻祖是“xocolatl”，意为“苦水”。其主要原料可可豆产于赤道南北纬18度以内的狭长地带。作饮料时，常称为“热巧克力”或可可亚。"#本作品作者吴宇航
                    elif a == "尚书":#本作品作者吴宇航
                        b="《尚书》，最早书名为《书》，约成书于前五世纪，传统《尚书》（又称《今文尚书》）由伏生传下来。传说为上古文化《三坟五典》遗留著作。西汉学者伏生口述的二十八篇《尚书》为今文《尚书》，鲁恭王在拆除孔子故宅一段墙壁时，发现的另一部《尚书》，为古文《尚书》。西晋永嘉年间战乱，今、古文《尚书》全都散失了。东晋初，豫章内史梅赜给朝廷献上了一部《尚书》，包括《今文尚书》33篇，以及伪《古文尚书》25篇 。《尚书》列为重要核心儒家经典之一， “尚”即“上”，《尚书》就是上古的书，它是中国上古历史文献和部分追述古代事迹著作的汇编，是我国最早的一部历史文献汇编。2018年11月，清华大学战国竹简研究成果发布，证实其中古文《尚书》系后人伪作。其「部份篇目」内容的来源可靠性从南宋开始遭受怀疑。清初，这些篇目在主流学术界被定作「伪书」，甚至排除出《尚书》之外。近十多年来，随着出土文献研究的发展，大大拓展了对古代尚书文献的认识。"#本作品作者吴宇航
                    elif a == "十二生肖":#本作品作者吴宇航
                        b="十二生肖，又叫属相，是中国与十二地支相配以人出生年份的十二种动物，包括鼠、牛、虎、兔、龙、蛇、马、羊、猴、鸡、狗、猪。 十二生肖的起源与动物崇拜有关。据湖北云梦睡虎地和甘肃天水放马滩出土的秦简可知，先秦时期即有比较完整的生肖系统存在。最早记载与现代相同的十二生肖的传世文献是东汉王充的《论衡》。 十二生肖是十二地支的形象化代表，即子（鼠）、丑（牛）、寅（虎）、卯（兔）、辰（龙）、巳（蛇）、午（马）、未（羊）、申（猴）、酉（鸡）、戌（狗）、亥（猪），随着历史的发展逐渐融合到相生相克的民间信仰观念，表现在婚姻、人生、年运等，每一种生肖都有丰富的传说，并以此形成一种观念阐释系统，成为民间文化中的形象哲学，如婚配上的属相、庙会祈祷、本命年等。现代，更多人把生肖作为春节的吉祥物，成为娱乐文化活动的象征。生肖作为悠久的民俗文化符号，历代留下了大量描绘生肖形象和象征意义的诗歌、春联、绘画、书画和民间工艺作品。除中国外，世界多国在春节期间发行生肖邮票，以此来表达对中国新年的祝福。 "#本作品作者吴宇航
                    elif a == "节日":#本作品作者吴宇航
                        b="节日，是指生活中值得纪念的重要日子。是世界人民为适应生产和生活的需要而共同创造的一种民俗文化，是世界民俗文化的重要组成部分。各民族和地区都有自己的节日。一些节日源于传统习俗，如中国的春节、中秋节、清明节、重阳节等。有的节日源于宗教，比如##教国家的圣诞节。有的节日源于对某人或某件事件的纪念，比如中国的端午节、国庆节、青年节等等。另有国际组织提倡的运动指定的日子，如劳动节、妇女节、母亲节。随着时间推移，节日的内涵和庆祝方式也在发生着变化。而现时节日经常与假日相混淆，事实上大多数节日都没有法定假期，如中国部分传统节日仍没有假期，如重阳节。"#本作品作者吴宇航
                    elif a == "吸烟":#本作品作者吴宇航
                        b="吸烟有危害，不仅仅危害人体健康，还会对社会产生不良的影响。任何有组织生物体只要还有生命迹象就必须要呼吸，呼出体内的二氧化碳，吸入空气中的氧气，进行新陈代谢，以维持正常的生命活动。不吸烟的人，每天都能吸入大量的新鲜空气；而经常吸烟的人，却享受不到大自然的恩惠，吸入的不是新鲜空气，而是被烟雾污染的有毒气体。烟叶里含有毒质烟碱，也叫尼古丁。1克重的烟碱能毒死300只兔或500只老鼠。如果给人注射50毫克烟碱，就会致死。吸烟对呼吸道危害最大，很容易引起喉头炎、气管炎，肺气肿等咳嗽病。吸烟的时候烟从口入，经过喉咙、气管、支气管、进入血液里。吸烟会让男性丢失Y染色体，增加患癌风险。  2017年10月27日，世界卫生组织国际癌症研究机构公布的致癌物清单初步整理参考，吸烟在一类致癌物清单中。 2018年5月1日起，在动车组列车上吸烟的旅客将被纳入“失信人”名单，在180天内限制乘车。"#本作品作者吴宇航
                    elif a == "水":#本作品作者吴宇航
                        b="水，化学式为H₂O，是由氢、氧两种元素组成的无机物，无毒，可饮用。在常温常压下为无色无味的透明液体，被称为人类生命的源泉。水是地球上最常见的物质之一，是包括无机化合、人类在内所有生命生存的重要资源，也是生物体最重要的组成部分。 纯水可以导电，但十分微弱，属于极弱的电解质。日常生活中的水由于溶解了其他电解质而有较多的正负离子，导电性增强。 "#本作品作者吴宇航
                    elif a == "奥里给" or a == "奥利给" or a == "奥力给":#本作品作者吴宇航
                        b="奥利给出自快手上的主播在直播或者录视频时的说的话术，该词就是我们常说的“给力”的意思，也称给力噢，作为感叹词，可能包含了赞美、加油打气等多种感情色彩。属于网络流行词。"#本作品作者吴宇航
                    elif a == "1":#本作品作者吴宇航
                        b="阿拉伯数字 1"#本作品作者吴宇航
                    elif a == "2":#本作品作者吴宇航
                        b="阿拉伯数字 2"#本作品作者吴宇航
                    elif a == "3":#本作品作者吴宇航
                        b="阿拉伯数字 3"#本作品作者吴宇航
                    elif a == "4":#本作品作者吴宇航
                        b="阿拉伯数字 4"#本作品作者吴宇航
                    elif a == "5":#本作品作者吴宇航
                        b="阿拉伯数字 5"#本作品作者吴宇航
                    elif a == "6":#本作品作者吴宇航
                        b="阿拉伯数字 6"#本作品作者吴宇航
                    elif a == "7":#本作品作者吴宇航
                        b="阿拉伯数字 7"#本作品作者吴宇航
                    elif a == "8":#本作品作者吴宇航
                        b="阿拉伯数字 8"#本作品作者吴宇航
                    elif a == "9":#本作品作者吴宇航
                        b="阿拉伯数字 9"#本作品作者吴宇航
                    elif a == "阿拉伯数字":#本作品作者吴宇航
                        b="阿拉伯数字由0，1，2，3，4，5，6，7，8，9共10个计数符号组成，阿拉伯数字最初由古印度人发明，后由阿拉伯人传向欧洲，之后再经欧洲人将其现代化，人们以为是阿拉伯发明，所以人们称其为“阿拉伯数字”。"#本作品作者吴宇航
                    elif a == "皇帝":#本作品作者吴宇航
                        b="上古三皇五帝，如羲皇伏羲、娲皇女娲、黄帝轩辕、炎帝神农等都不是真正帝王，仅为部落首领或部落联盟首领，其“皇”或“帝”号，为后人所追加。夏朝君主称“后”，商朝君主称“帝”，周天子称“王”。战国诸侯大多僭越称王，尊周天子为“天王”。秦王嬴政统一中国，认为自己“德兼三皇、功盖五帝”，创“皇帝”一词作为华夏最高统治者的正式称号。所以，秦始皇嬴政是中国首位皇帝，自称“始皇帝”。从此“皇帝”取代了“帝”与“王”，成为中国两千年多来封建社会最高统治者的称呼。"#本作品作者吴宇航
                    elif a == "编程社区":#本作品作者吴宇航
                        b="学而思编程社区、慧编程社区、小码王编程社区、编程猫编程社区、卡塔编程社区、GitHub等一些社区，去浏览器里搜就能搜到"#本作品作者吴宇航
                    elif a == "《风》":#本作品作者吴宇航
                        b="《风》是唐代诗人李峤创作的一首诗。此诗通过抓住“叶”“花”“浪”“竹”四样自然界物象在风力作用下的易变，间接地表现了“风”之种种形力、魅力与威力：它能使晚秋的树叶脱落，能催开早春二月的鲜花，经过江河时能掀起千尺巨浪，刮进竹林时可把万棵翠竹吹得歪歪斜斜。全诗四句两两成偶，以“三”“二”“千”“万”数字对举排列来表现风的强大，也表达了诗人对大自然的敬畏之情。"#本作品作者吴宇航
                    elif a == "游戏":#本作品作者吴宇航
                        b="游戏是所有哺乳类动物，特别是灵长类动物学习生存的第一步。它是一种基于物质需求满足之上的，在一些特定时间、空间范围内遵循某种特定规则的，追求精神世界需求满足的社会行为方式，但同时这种行为方式也是哺乳类动物或者灵长类动物所需的一种降压减排的方式，不管是在出生幼年期，或者发育期，成熟期都会需要的一种行为方式。 合理适度的游戏允许人类在模拟环境下挑战和克服障碍，可以帮助人类开发智力、锻炼思维和反应能力、训练技能、培养规则意识等，大型网络游戏还可以培养战略战术意识和团队精神。但凡事过犹不及，过度游戏也会对人的身心健康产生危害，沉迷于虚拟世界里，随心所欲的宣泄情感，因此长期沉迷网络游戏的孩子会对周围的人和事冷漠麻木，有的还会荒废学业，甚至发生犯罪现象，给正常生长带来各种各样的危害。2018年6月18日，世界卫生组织发布新版《国际疾病分类》，“游戏障碍”，被列为疾病。但是游戏障碍与人们口中说的游戏成瘾是两个不同的概念，容易混淆。 游戏有智力游戏和活动###之分，又翻译为Play、Pastime、Playgame、Sport、Spore、Squail、Games、Hopscotch、Jeu、Toy。现在的游戏多指各种平台上的电子游戏。"#本作品作者吴宇航
                    elif a == "大脑":#本作品作者吴宇航
                        b="大脑为神经系统最高级部分，由左、右两个大脑半球组成，两半球间有横行的神经纤维相联系。每个半球包括：大脑皮层（大脑皮质）：是表面的一层灰质（神经细胞的细胞体集中部分）。人的大脑表面有很多往下凹的沟（裂），沟（裂）之间有隆起的回，因而大大增加了大脑皮层的面积。人的大脑皮层最为发达，是思维的器官，主导机体内一切活动过程，并调节机体与周围环境的平衡，所以大脑皮层是高级神经活动的物质基础。"#本作品作者吴宇航
                    elif a == "表情":#本作品作者吴宇航
                        b="表情是一个汉语词语，拼音是biǎo qíng，意思是表达感情、情意。表现在面部或姿态上的思想感情。现代年轻人聊天多用图片类表情来代替语言进行交流，并衍生出海峡两岸表情大战等年轻文化交流事件。表情是情绪的主观体验的外部表现模式。人的表情主要有三种方式：面部表情、语言声调表情和身体姿态表情"#本作品作者吴宇航
                    elif a == "666":#本作品作者吴宇航
                        b="666是一个网络用语，用来形容某人或某物很厉害很牛、令人折服（大多是指游戏玩的好）。而在西方，666指魔鬼，撒旦和灵魂，是不吉利的象征。随着时代的发展，各类游戏的节奏也越来越快，666这样的语言用的越来越多。在江苏破获的网络涉毒案中，犯罪嫌疑人用666暗指吸毒，意思是让你溜。当人们表现出超常的能力时也会用来感叹。"#本作品作者吴宇航
                    elif a == "555定时器":#本作品作者吴宇航
                        b="55定时器是一种集成电路芯片，常被用于定时器、脉冲产生器和振荡电路。555可被作为电路中的延时器件、触发器或起振元件。555定时器于1971年由西格尼蒂克公司推出，由于其易用性、低廉的价格和良好的可靠性，直至今日仍被广泛应用于电子电路的设计中。许多厂家都生产555芯片，包括采用双极型晶体管的传统型号和采用CMOS设计的版本。555被认为是当前年产量最高的芯片之一，仅2003年，就有约10亿枚的产量。"#本作品作者吴宇航
                    elif a == "哥斯拉":#本作品作者吴宇航
                        b="《哥斯拉》（Godzilla）是一部由传奇影业与华纳兄弟影业公司合拍，英国导演加里斯·爱德华斯执导的美国科幻怪兽电影，是“哥斯拉系列”的重启、美国拍摄的第二部有关“哥斯拉”的影片，上一部同名影片于1998年上映。该片由亚伦·泰勒-约翰逊、渡边谦、伊丽莎白·奥尔森、朱丽叶·比诺什、莎莉·霍金斯、大卫·斯特雷泽恩、布莱恩·科兰斯顿等主演。该片重塑日本哥斯拉“可怕的自然之力”形象，于2014年5月16日"#本作品作者吴宇航
                    elif a == "哪吒":#本作品作者吴宇航
                        b="""哪吒（ nézhā），中国古代神话传说人物，道教##神。   哪吒信仰兴盛于道教与民间信仰；在道教的头衔为中坛元帅、通天太师、威灵显赫大将军、三坛海会大神等；尊称太子爷、三太子、善胜童子。 #本作品作者吴宇航
                        主要记载源于元代宗教神话典籍《三教搜神大全》，活跃于明代神魔系列小说名著《西游记》、《南游记》、《封神演义》等多部古典文学作品。 托塔李天王家的三太子，最早传说来自古波斯和古印度教的神话，随着本土化的传教，唐末起就从古盛传至今，由佛教##军神“那咤”演变而成 [6]  ，记载已在东晋有之，主要定型于闹海传说与屠龙之说的内容，以及降魔伏妖再成仙成圣等古籍文献，出生奇异，一身神器，能变化三头六臂又或三头八臂，百邪不侵专克摄魂夺魄的莲花化身。#本作品作者吴宇航
                        在中国各地成为世代传奇且家喻户晓的著名艺术形象；后期影响民间奉祀为保护神，并渐被道教所吸纳，将其遵崇供为中央祭坛的大罗天神，地位高贵鼎盛；神仙谱中被归类为“忠武战神”之位，属于武神一系。在民俗被尊为护世护民的“五营神将”之首；乃统领天兵天将的元帅之神，又称“太子元帅”，还被敬作“天帅领袖”和“火轮天王”，常以娃娃或者少年儿童的模样登场，终成神话史上独特无双、神通广大的天庭童神。在儒释道三体合流相融的文化传承中，得享华人的普遍崇拜与信仰。更因为其鲜明精彩的古老形象与经典传说故事名气响亮，从而吸引现代众多动漫和影视剧都将哪吒设定为主角，加以儿童化的少年英雄方式传扬，深受诸多孩子们的欢迎和喜爱。"""#本作品作者吴宇航
                    elif a == "你好":#本作品作者吴宇航
                        b="拼音[nǐ hǎo] 打招呼的敬语，作为一般对话的开场白、常用语。这也是个最基本的中文词语。主要用于打招呼请教别人问题前的时候，或者单纯表示礼貌的时候等。"#本作品作者吴宇航
                    elif a == "KFC"or a =="肯德基":#本作品作者吴宇航
                        b="肯德基（KentuckyFried Chicken，肯塔基州炸鸡，简称KFC），是美国跨国连锁餐厅之一，也是世界第二大速食及最大炸鸡连锁企业，1952年由创始人哈兰·山德士（Colonel Harland Sanders）创建， 主要出售炸鸡、汉堡、薯条、盖饭、蛋挞、汽水等高热量快餐食品。肯德基隶属于百胜中国控股有限公司（简称“百胜中国”） [2]  ， 股票代码为YUMC  ，是Yum！Brands在中国大陆的特许经营商   ，拥有肯德基品牌在中国大陆的独家经营权。 肯德基与百事可乐结成了战略联盟，固定销售百事公司提供的碳酸饮料。2017年6月，《2017年BrandZ最具价值全球品牌100强》公布，肯德基排名第81位。 自2018年2月17日开始，英国的大部分肯德基网点仍然暂停营业。当地900家门店中，截至2月20日，仍有562家处于关闭状态，在2月18日晚歇业的门店数量达到顶峰的646家。 在2018世界品牌500强排行榜中，肯德基排名第129位。"#本作品作者吴宇航
                    elif a == "82年的拉菲":#本作品作者吴宇航
                        b="82年的拉菲，网络流行语，源自影视剧中开拉菲的桥段，由于82年的拉菲酒品质好、价格昂贵，所以“82年的拉菲”是高规格的代名词。常常在网络聊天时作为表情包使用。"#本作品作者吴宇航
                    elif a == "面":#本作品作者吴宇航
                        b="（1）面，读作：miàn。面字从“一 + 自”，从囗（wéi）。“一 + 自”表示“鼻子及其附近”。“囗”指“外围”。“一 + 自”与“囗”联合起来表示“人脸”。本义是人脸。转义是妇人以谷粉擦脸。（2）麺、麪，读作：miàn。形声。从麦，丏或面声。本义：麦子磨的面粉。"#本作品作者吴宇航
                    elif a == "饭":#本作品作者吴宇航
                        b="fàn形声。字从食，从反，反亦声。“反”意为“镜像对称的事物或动作”。“食”与“反”联合起来表示“二人对食”。本义：夫妻对食。TA说"#本作品作者吴宇航
                    elif a == "酒":#本作品作者吴宇航
                        b="酒，中国汉语词汇，音jiu。英文：wine,Alcohol酒的化学成分是乙醇，一般含有微量的杂醇和酯类物质，食用白酒的浓度一般在60度（即60%）以下（少数有60度以上），白酒经分馏提纯至75%以上为医用酒精，提纯到99.5%以上为无水乙醇。酒是以粮食为原料经发酵酿造而成的。据新华社消息，饮酒量不论多少都无益。"#本作品作者吴宇航
                    elif a == "牛肉":#本作品作者吴宇航
                        b="牛肉（拼音：niú ròu），指从牛身上获得的肉，为常见的肉品之一。来源可以是奶牛、公牛、小母牛。牛的肌肉部分可以切成牛排、牛肉块或牛仔骨，也可以与其他的肉混合做成香肠或血肠。其他部位可食用的还有牛尾、牛肝、牛舌、牛百叶、牛胰腺、牛胸腺、牛心、牛脑、牛肾、牛鞭。牛肠也可以吃，不过常用来做香肠衣。牛骨可用做饲料。阉牛和小母牛肉质相似，但阉牛的脂肪更少。年纪大的母牛和公牛肉质粗硬，常用来做牛肉末。肉牛一般需要经过育肥，饲以谷物、膳食纤维、蛋白质、维生素和矿物质。牛肉是世界第三消耗肉品，约占肉制品市场的25%。落后于猪肉（38%）和家禽（30%）。美国、巴西和中国是世界消费牛肉前三的国家。按2009年人年消费来看，阿根廷以64.6千克排名第一，美国为42.1千克，欧洲为11.9千克。最大的牛肉出口国包括印度、巴西、澳大利亚和美国。牛肉制品对于巴拉圭、阿根廷、爱尔兰、墨西哥、新西兰、尼加拉瓜、乌拉圭的经济有重要影响。"#本作品作者吴宇航
                    elif a == "空手道":#本作品作者吴宇航
                        b="空手道是日本传统格斗术结合琉球武术唐手而形成的，起源于日本武道和琉球的唐手。唐手是中国武术传入琉球，结合当地武术琉球手发展而成的，而日本本土人又将九州、本州的摔、投等格斗技与唐手相结合，最终形成空手道。二战之后通过美军宣传而在全世界广泛传播。空手道当中包含踢、打、摔、拿、投、锁、绞、逆技、点穴等多种技术，一些流派中还练习武器术。一九九四年日本广岛第十二届亚运会空手道首次成为正式比赛项目，空手道比赛场地一般为8×8米；至于比赛项目有套路赛（型）和格斗赛（组手）两种，而在组手比赛中一方有效进攻导致对手瞬时丧失战斗能力或重心明显移动为得分标准。"#本作品作者吴宇航
                    elif a == "《刀》":#本作品作者吴宇航
                        b="《刀》是由徐克执导，赵文卓、熊欣欣、桑妮主演的动作片。影片讲述了刀客黎定安尽管失去右手又只有一本残缺的绝世刀谱在身，仍义无反顾地自创独臂刀法决战仇家，为父报仇的故事。该片于1995年12月21日在香港上映。"#本作品作者吴宇航
                    elif a == "细菌":#本作品作者吴宇航
                        b="细菌（学名：Bacteria）是指生物的主要类群之一，属于细菌域。也是所有生物中数量最多的一类，据估计，其总数约有5×10^30个。细菌的形状相当多样，主要有球状、杆状，以及螺旋状。细菌也对人类活动有很大的影响。一方面，细菌是许多疾病的病原体，包括肺结核、淋病、炭疽病、梅毒、鼠疫、砂眼等疾病都是由细菌所引发。然而，人类也时常利用细菌，例如乳酪及酸奶和酒酿的制作、部分抗生素的制造、废水的处理等，都与细菌有关。在生物科技领域中，细菌也有着广泛的运用。"#本作品作者吴宇航
                    elif a == "自然"or a == "大自然":#本作品作者吴宇航
                        b="自然，哲学名词，广义而言指的即是自然界，规模，   大至宇宙，小至基本粒子， 包括物理学宇宙、物质世界及物质宇宙。亦指道家术语。   东汉至六朝的佛教深受道教自然影响。至南北朝时期左右本土化佛教逐渐完成，由佛教所挑起的关于自然、因缘的争论。《楞严经》：“非因缘生，非自然性”，《道德真经广圣义》：“以无为体，以无为用，自然为体，因缘为用。此皆无也。” 与道家/教重视自然原则不同， 早期佛教认为世界万法都是因缘而成，均无其独立自性，因而是不真实的。这种通过分析主义的思维途径来论证事物虚幻不实的作法为其后大乘佛教所继承。大乘佛教进一步提出缘起论以对世界做性空的价值判断。这种通过层层分析达至的空相对中国传统重视阴阳和合的思想传统， 实在缺乏强制性。道理很简单， 因为中国人根本就不认为阴阳和合的事物不真实， 反而认为事物只有通过阴阳和合才能达至更高的善与美。这应当与中国古代重视综合性、 整体性思维方式密切相关。跟刘宋高僧慧琳一样在 《白黑论》 中对佛教的缘起性空理论予以驳斥：今析毫空树， 无伤垂荫之茂;离材虚空， 不损轮奂之美。明无常增其渴荫之情， 陈苦伪笃其竞辰之虑。 (《宋书》 卷九七 《天竺迦毗黎传》 )贝锦以繁采发挥， 和羹以盐梅致旨， 齐侯追爽鸠之乐， 燕王无延年之术。恐和合之辨， 危脆之教， 正足恋其嗜欲之私， 无以倾其爱竞之惑也。 (《宋书》 卷九七 《天竺迦毗黎传》 )这显然是用中土的和合论来对抗佛教的缘起论。"#本作品作者吴宇航
                    elif a == "起床":#本作品作者吴宇航
                        b="起床，本意离床下地、起身，喻指病愈。语出《儒林外史》第四八回：“饿到六天上，不能起牀（床）。"#本作品作者吴宇航
                    elif a == "起床战争":#本作品作者吴宇航
                        b="起床战争是《Minecraft》服务器中流行的PVP游戏，目的是搭方块到各种岛屿收集各种资源，保护自家的床并且挖掉其他队的床并杀死所有敌人来赢得游戏胜利。起床战争内容主题为‘床’（有些服务器是蛋糕），即重生点。玩家至少需要1人。一般的起床战争玩家分为4队或8队，每队4～16人。"#本作品作者吴宇航
                    elif a == "PVP":#本作品作者吴宇航
                        b="Present value of product： 即产品的现期价值，它是指经过一些时间变化后，所生产出来的产品在现在时间比以前时间所体现出来的价值。"#本作品作者吴宇航
                    elif a == "小欢喜":#本作品作者吴宇航
                        b="《小欢喜》是由汪俊执导，黄磊、海清、陶虹、王砚辉、咏梅领衔主演，周奇、李庚希、郭子凡、刘家祎主演，沙溢、任重特别出演的都市情感剧  。该剧改编自鲁引弓的同名小说   ，以方圆、童文洁夫妇的视角，讲述了方家、季家、乔家等几个高三考生家庭在高三这一年的故事  。该剧于2019年7月31日在东方卫视、浙江卫视首播，并在爱奇艺、腾讯视频同步播出"#本作品作者吴宇航
                    elif a == "标准":#本作品作者吴宇航
                        b="标准是规范性文件之一。其定义是为了在一定的范围内获得最佳秩序，经协商一致制定并由公认机构批准，共同使用的和重复使用的一种规范性文件。"#本作品作者吴宇航
                    elif a == "作业帮":#本作品作者吴宇航
                        b="作业帮致力于为全国中小学生提供全学科的学习辅导服务，作业帮用户量突破8亿 [1]  ，月活用户约1.7亿 [2]  ，是中小学在线教育领军品牌。 [3-6] 作业帮自主研发多余项学习工具，包括拍照搜题、作业帮直播课、古文助手、作文搜索等。在作业帮，学生可以通过拍照、语音等方式得到难题的解析步骤、考点答案；可以通过作业帮直播课与教师互动学习；可以迅速发现自己的知识薄弱点，精准练习补充；可以观看课程直播，手机互动学习；也可以连线老师在线一对一答疑解惑；学习之余还能与全国同龄学生一起交流，讨论学习生活中的趣事。2019年6月11日，作业帮入选“2019福布斯中国最具创新力企业榜”。 [7-8] 2019年12月24日，通过教育部备案，备案号为教APP备1100058号。 [9]"#本作品作者吴宇航
                    elif a == "谷歌":#本作品作者吴宇航
                        b="谷歌公司（Google Inc.）成立于1998年9月4日，由拉里·佩奇和谢尔盖·布林共同创建，被公认为全球最大的搜索引擎公司。 [1] 谷歌是一家位于美国的跨国科技企业，业务包括互联网搜索、云计算、广告技术等，同时开发并提供大量基于互联网的产品与服务，其主要利润来自于AdWords等广告服务。 [2] 1999年下半年，谷歌网站“Google”正式启用。 [3]  2010年3月23日，宣布关闭在中国大陆市场搜索服务。2015年8月10日，宣布对企业架构进行调整，并创办了一家名为Alphabet的“伞形公司”（Umbrella Company），成为Alphabet旗下子公司。2015年，在2015年度“世界品牌500强”排行中重返榜首，苹果和亚马逊分别位居第二和第三名。2016年6月8日，《2016年BrandZ全球最具价值品牌百强榜》公布，以2291.98亿美元的品牌价值重新超越苹果成为百强第一。 [4]  2017年2月，Brand Finance发布2017年度全球500强品牌榜单，排名第一。 [5]  2017年6月，《2017年BrandZ最具价值全球品牌100强》公布，谷歌公司名列第一位。 [6] 2017年12月13日，谷歌正式宣布谷歌AI中国中心（Google AI China Center）在北京成立。 [7] 2018年1月，腾讯和谷歌宣布双方签署一份覆盖多项产品和技术的专利交叉授权许可协议。 [8]  2018年5月29日，《2018年BrandZ全球最具价值品牌100强》发布，谷歌公司名列第一位。12月18日，世界品牌实验室编制的《2018世界品牌500强》揭晓，Google排名第2位。 [9]  2019年度全球最具价值100大品牌榜第二位。 [10]"#本作品作者吴宇航
                    elif a == "小米" or a == "小米公司":#本作品作者吴宇航
                        b="北京小米科技有限责任公司成立于2010年3月3日 [1]  ，是一家专注于智能硬件和电子产品研发的全球化移动互联网企业 [2]  ，同时也是一家专注于高端智能手机、互联网电视及智能家居生态链建设的创新型科技企业。 [3] 小米公司创造了用互联网模式开发手机操作系统、发烧友参与开发改进的模式。小米还是继苹果、三星、华为之后第四家拥有手机芯片自研能力的科技公司。2018年7月9日在香港交易所主板挂牌上市，成为港交所上市制度改革后首家采用不同投票权架构的上市企业。 [4] “为发烧而生”是小米的产品概念。“让每个人都能享受科技的乐趣”是小米公司的愿景。小米公司应用了互联网开发模式开发产品的模式，用极客精神做产品，用互联网模式干掉中间环节，致力让全球每个人，都能享用来自中国的优质科技产品。 [3] 小米已经建成了全球最大消费类IoT物联网平台，连接超过1亿台智能设备 [5]  ，MIUI月活跃用户达到2.42亿 [6]  。小米系投资的公司接近400家，覆盖智能硬件、生活消费用品、教育、游戏、社交网络、文化娱乐、医疗健康、汽车交通、金融等领域。2019年6月，入选2019福布斯中国最具创新力企业榜。 [7-8]  2019年7月，2019世界500强排行榜发布，小米排名468位 [9]  。2019年10月，2019福布斯全球数字经济100强榜发布，小米位列第56位。 [10]  2019年12月18日，人民日报“中国品牌发展指数”100榜单排名30位。 [11] 2019年，小米手机出货量1.25亿台，全球排名第四， [12]  电视在中国售出1021万台，排名第一。 [13]  入围2020全球百强创新名单，AI等专利位于全球前列。 [14] "#本作品作者吴宇航
                    elif a == "苹果电脑" or a == "macbook" or a == "Macbook":#本作品作者吴宇航
                        b="苹果电脑是苹果公司开发上市的一种产品，苹果公司原称苹果电脑公司（Apple Computer, Inc.）总部位于美国加利福尼亚的库比提诺，核心业务是电子科技产品，全球电脑市场占有率为3.8%。苹果的Apple II于1970年代助长了个人电脑革命，其后的Macintosh接力于1980年代持续发展。最知名的产品是其出品的Apple II、Macintosh电脑、iPod数位音乐播放器、iTunes音乐商店和iPhone智能手机，它在高科技企业中以创新而闻名。苹果公司于2007年1月9日旧金山的Macworld Expo上宣布改名。"#本作品作者吴宇航
                    elif a == "2020":#本作品作者吴宇航
                        b="尔凌软件科技有限公司（2020软件）成立于2007年，是一家辅助家居行业的软件供应商。主要经营计算机软件的开发、设计、制作，销售自产产品。总部位于加拿大，在上海和广州分别设立了办公室，2020的主要产品有针对家居行业设计、生产、管理的软件。2020Design 家具设计软件、2020 imos 易模式家具工艺软件、2020Insight 家具管理软件、2020IdealSpaces家居体验设计平台。"#本作品作者吴宇航
                    elif a == "2012":#本作品作者吴宇航
                        b="《2012》是一部关于全球毁灭的灾难电影，由罗兰·艾默里奇执导，约翰·库萨克、桑迪·牛顿、阿曼达·皮特和切瓦特·埃加福特等联袂出演，影片于2009年11月13日在美国上映。影片故事发生在2012年12月，一家人正在度假。没想到根据玛雅预言，2012年的12月21日，正是世界末日，玛雅人的日历也到那天为止，再没有下一页。电影讲述了主人公以及世界各国人民挣扎求生的经历，灾难面前，尽现人间百态"#本作品作者吴宇航
                    elif a == "清"or a == "清朝":#本作品作者吴宇航
                        b="清朝（1636年—1912年），是中国历史上最后一个封建王朝，共传十二帝  ，从努尔哈赤建立后金政权起，总计296年。   从皇太极改国号为清开始，国祚276年。   从清兵入关，建立全国性政权算起为268年。 1616年，建州女真首领努尔哈赤建立后金。1636年，皇太极改国号为大清。1644年，驻守山海关的明将吴三桂降清，多尔衮率领清兵入关，至1659年平定大顺、大西、南明等政权。后又平定三藩之乱、统一台湾，逐步掌控全国。  康雍乾三朝走向鼎盛，在此期间，中国的传统社会取得了前所未有的发展成就。清初人口增殖，土地增垦，物产盈丰，边境无事，小农经济的生产方式和社会生活相对繁荣稳定，综合国力远胜于汉唐。 [8]  鸦片战争后多遭列强入侵，中国人民进行了洋务运动和戊戌变法等近代化的探索和改革。1912年2月12日，北洋大臣袁世凯诱使清帝溥仪逊位，颁布了退位诏书，清朝从此结束。 [9-10] 清朝时期，统一多民族国家得到巩固和发展，清朝统治者统一蒙古诸部，将新疆和西藏纳入版图，积极维护国家领土主权的完整。乾隆年间，中国作为统一的多民族世界大国的格局最终确定。极盛时期的清朝，西抵葱岭和巴尔喀什湖，西北包括唐努乌梁海，北至漠北和西伯利亚，东到太平洋（包括库页岛），南达南沙群岛。包括50多个民族，国家空前统一。 期间中国古代的专制主义也推向了最高峰。清朝前期农业和商业发达，江南出现了密集的商业城市，并在全国出现了大商帮。在此基础上，人口突破四亿大关，占世界总人口十亿的近一半。"#本作品作者吴宇航
                    elif a == "吃":#本作品作者吴宇航
                        b="吃（拼音：chī），是指用手或工具（筷子，叉子，勺子等）把食物送进口腔，经过牙齿咀嚼后下咽经食道管进入胃里，再由消化系统完成整个消化过程。方言读音：四川方言读音为qī（启）。广东方言读音为hek方言用词：湖南省方言用“呷”（读qia，掐音）表示“吃”：呷饭。"#本作品作者吴宇航
                    elif a == "麦片":#本作品作者吴宇航
                        b="麦片(oatmeal)：是一种以小麦为原料加工而成的食品。是用普通的麦子和一些东西加工而成的。它曾经是第一种被工业化生产的早餐谷物食品。麦片的“片”字是指，它是一种来自被煮过，辗碎，和加以烘干的谷物，通常被放在牛奶和果汁里，或做成麦片粥加以食用。 麦片还分为普通麦片和燕麦片，燕麦片是由燕麦做成的，由于麦片食品的制作过程简单，而且省时，有的种类的麦片，只要经过水泡，就可以食用，所以受到了很多人的欢迎。"#本作品作者吴宇航
                    elif a == "王思聪":#本作品作者吴宇航
                        b="王思聪，1988年1月3日出生于辽宁省大连市，毕业于伦敦大学学院哲学系，  万达集团董事长王健林的独子，北京普思投资有限公司董事长、IG电子竞技俱乐部创始人、万达集团董事。2010年底，王思聪持有万达院线约1000万股。  2011年4月，因在微博上炮轰俏江南董事长张兰造谣，引起热议。2014年9月12日，王思聪以侵犯名誉权为由，起诉网易和搜狐，否认斥资千万拉票   。2015年8月末，王思聪出镜的BBC纪录片《中国的秘密》播出  ；9月5日，王思聪参加腾讯《英雄联盟》四周年庆典，并表示担任熊猫TV的CEO；10月24日，中国移动电竞联盟成立，王思聪任主席。 2016年，新版“京城四少”名单火热出炉，王思聪位居榜首。  2018年8月18日，王思聪开始自己的职业LOL生涯。同年9月19日，王思聪正式宣布退役。  2019年1月25日，王思聪豪掷630万招募编剧人才和优秀剧本"#本作品作者吴宇航
                    elif a == "李现":#本作品作者吴宇航
                        b="李现，曾用名李晛，1991年10月19日出生于湖北省咸宁市，成长于湖北省荆州市，中国内地影视男演员，毕业于北京电影学院表演系2010级。2011年，出演个人首部电影《万箭穿心》，从而正式进入演艺圈。2012年，主演青春爱情电影《初恋未满》。2013年，出演绿色环保爱情喜剧电影《玩命试爱》。2014年，出演国内首部原创都市奇幻单元《奇妙世纪》中第二集“最长的25米”。"#本作品作者吴宇航
                    elif a == "陈伟霆":#本作品作者吴宇航
                        b="陈伟霆（William Chan），1985年11月21日出生于中国香港，华语影视男演员、歌手、主持人。2003年，因参加全球华人新秀香港区选拔赛而进入演艺圈。2006年成为Sun Boy’z组合一员。2008年开始独立发展，随后推出个人首张专辑《Will Power》，并获香港十大劲歌金曲颁奖礼最受欢迎男新人金奖及香港十大中文金曲最有前途新人金奖。2013年，陈伟霆将工作重心转移至中国内地，"#本作品作者吴宇航
                    elif a == "黄家驹":#本作品作者吴宇航
                        b="黄家驹（1962年6月10日-1993年6月30日），出生于中国香港，中国香港男歌手、原创音乐人、吉他手、摇滚乐队Beyond的主唱、节奏吉他手及创队成员。1983年以歌曲《大厦》出道，并组建Beyond乐队，担任主唱。1988年凭借专辑《秘密警察》在香港歌坛获得关注，其中由黄家驹创作的歌曲《大地》获得十大劲歌金曲奖。1989年凭借歌曲《真的爱你》获得十大劲歌金曲奖以及十大中文金曲奖。"#本作品作者吴宇航
                    elif a == "周星驰":#本作品作者吴宇航
                        b="周星驰，1962年6月22日生于香港，祖籍浙江宁波，中国香港演员、导演、编剧、制作人、商人，毕业于无线电视艺员训练班。1980年成为丽的电视台的特约演员，从而进入演艺圈。1981年出演个人首部电视剧《IQ成熟时》。1988年将演艺事业的重心转向大银幕，并于同年出演电影处女作《捕风汉子》。1990年凭借喜剧片《一本漫画闯天涯》确立其无厘头的表演风格 [1]  ；同年，因其主演的喜剧动作片《赌圣》打破香港地区票房纪录而获得关注  。1991年主演喜剧片《逃学威龙》，并再次打破香港地区票房纪录   。1995年凭借喜剧爱情片《大话西游》奠定其在华语影坛的地位。1999年自导自演的喜剧片《喜剧之王》获得香港电影年度票房冠军 2002年凭借喜剧片《少林足球》获得第21届香港电影金像奖最佳男主角奖以及最佳导演奖   。2003年成为美国《时代周刊》封面人物   。2005年凭借喜剧动作片《功夫》获得第42届台湾电影金马奖最佳导演奖 [7]  。2008年自导自演的科幻喜剧片《长江7号》获得香港电影年度票房冠军 [8]  。2013年执导古装喜剧片《西游·降魔篇》，该片以2.18亿美元的票房成绩打破华语电影在全球的票房纪录   。2016年担任科幻喜剧片《美人鱼》的导演、编剧、制作人，该片以超过33亿元的票房创下中国内地电影票房纪录 演艺事业外，周星驰还涉足商界。1989年成立星炜有限公司  。1996年成立星辉公司   。2010年出任比高集团有限公司执行董事"#本作品作者吴宇航
                    elif a == "赵丽颖":#本作品作者吴宇航
                        b="赵丽颖，1987年10月16日出生于河北省廊坊市，中国内地影视女演员、歌手。2006年，因获得雅虎搜星比赛冯小刚组冠军而进入演艺圈；同年，在冯小刚执导的广告片《跪族篇》中担任女主角。2011年，因在古装剧《新还珠格格》中饰演晴儿一角而被观众认识。2013年，凭借古装剧《陆贞传奇》获得更多关注。2014年10月，在第10届金鹰电视艺术节举办的投票活动中被选为“金鹰女神”；"#本作品作者吴宇航
                    elif a == "蔡徐坤":#本作品作者吴宇航
                        b="蔡徐坤（KUN），1998年8月2日出生于浙江省，中国内地男歌手、演员、音乐制作人。2012年4月，蔡徐坤因参加综艺节目《向上吧！少年》进入全国200强   ；同年8月，参演个人首部偶像剧《童话二分之一》   。2014年3月，参演个人首部电影《完美假妻168》。2018年1月，参加偶像男团竞演养成类真人秀《偶像练习生》，并于同年4月6日获得最高票数，以NINE PERCENT九人男团C位出道并担任队长 [3]  ；同年8月，发行个人首张EP《1》 [4]  ；随后获得出道后首个个人音乐类奖项亚洲新歌榜2018年度盛典“最受欢迎潜力男歌手”   ；同年12月，获第十二届音乐盛典咪咕汇年度“最佳彩铃销量歌手”、年度十大金曲《Wait Wait Wait》、搜狐时尚盛典“年度人气男明星”以及今日头条年度盛典“年度偶像人物”。2019年2月，首登北京台春晚便包揽词曲，为其创作歌曲《那年春天》  。2月18日，发布单曲《没有意外》   。3月22日，发布海外公演主题曲《Bigger》  。4月19日，发布单曲《Hard To Get》"#本作品作者吴宇航
                    elif a == "迪丽热巴":#本作品作者吴宇航
                        b="迪丽热巴（Dilraba），1992年6月3日出生于新疆乌鲁木齐市，中国内地影视女演员、歌手，毕业于上海戏剧学院。2013年，迪丽热巴因主演个人首部电视剧《阿娜尔罕》而出道。2014年，她主演了奇幻剧《逆光之恋》。2015年，迪丽热巴凭借爱情剧《克拉恋人》赢得高人气，并获得国剧盛典最受欢迎新人女演员奖。2016年，其主演的现代剧《麻辣变形计》播出；"#本作品作者吴宇航
                    elif a == "李荣浩":#本作品作者吴宇航
                        b="李荣浩，1985年7月11日出生于安徽省蚌埠市，中国流行乐男歌手、音乐制作人、吉他手、演员。2013年9月正式出道，至2019年，共发行5张专辑，其作品在大中华区有很高的流行度；入围9次金曲奖，并获得内地首位金曲最佳新人奖；与众多歌手合作，为他人操刀作品逾200首；举办3轮大型巡回演唱会，是首位同时登上台北小巨蛋和香港红磡的内地歌手。2019年8月，获2019福布斯中国100名人榜荣誉。"#本作品作者吴宇航
                    elif a == "Angelababy"or a=='杨颖':#本作品作者吴宇航
                        b="angelababy（杨颖），1989年2月28日出生于上海市，华语影视女演员、时尚模特。2003年，Angelababy以模特身份出道，此后，她因担任时尚模特而在香港崭露头角。2007年，她开始将工作重心转向大银幕。2011年，她在爱情片《夏日乐悠悠》中首次担任女主角。2012年，凭借言情片《第一次》获得第13届华语电影传媒大奖最受瞩目女演员奖。"#本作品作者吴宇航
                    elif a == "海清":#本作品作者吴宇航
                        b="海清，本名黄怡，1977年1月12日生于中国江苏省南京市，演员，毕业于北京电影学院表演系。2003年，通过出演电视剧《玉观音》中的钟宁一角而出道。2009年11月，出演滕华涛执导的都市情感剧《蜗居》，该剧让海清的演艺事业取得了一定的成功。2010年，凭借主演爱情电视剧《媳妇的美好时代》获得第28届中国电视剧“飞天奖”优秀女演员奖，和第25届中国电视金鹰奖观众喜爱的电视剧女演员奖。"#本作品作者吴宇航
                    elif a == "黄磊":#本作品作者吴宇航
                        b="黄磊，1971年12月6日出生于江西省南昌市，中国大陆男演员、导演、编剧、监制、制片人、歌手、教师、作家。1990年黄磊考入北京电影学院表演系，同年出演陈凯歌执导电影《边走边唱》。1996年凭借电影《夜半歌声》获得第3届中国长春电影节最佳男配角奖。1997年北京电影学院硕士毕业后留校任教，同年发行第一张音乐专辑《边走边唱》。1999年出演电视剧《人间四月天》，饰演徐志摩。"#本作品作者吴宇航
                    elif a == "张信哲":#本作品作者吴宇航
                        b="张信哲，1967年3月26日生于中国台湾云林县，中国台湾流行乐男歌手、演员、舞台剧团团长。1987年张信哲签约滚石唱片的子公司巨石音乐，1989年发行第一张专辑《说谎》。1995年成立音乐工作室潮水音乐，并加盟EMI旗下附属厂牌种子音乐，1996年凭着专辑《宽容》获得第7届台湾金曲奖最佳国语男歌手奖。1997年推出专辑《过火》、《思念》、《挚爱》、《直觉》。"#本作品作者吴宇航
                    elif a == "牯牛降风景区":#本作品作者吴宇航
                        b="牯牛降风景区位于石台县与祁门县交界处，是安徽南部三大高山（黄山、清凉峰、牯牛降）之一，距石台县城22公里，主峰海拔1727.6米，总面积为6700公顷。牯牛降共分五大景区:主峰景区、灵山景区、双龙谷景区、龙门景区、观音堂景区。其中前四个皆位于石台县境内，观音堂景区位于祁门县境内。牯牛降以雄、奇、险著称，是黄山山脉向西延伸的主体，古称“西黄山”，山岳风光秀美绮丽。境内有36大峰，72小峰，36大岔，72小岔。因其山形酷似一头牯牛从天而降，故名牯牛降。2014年，牯牛降旅游景点荣获“安徽名牌”产品称号。"#本作品作者吴宇航
                    elif a == "安庆天柱山风景名胜区":#本作品作者吴宇航
                        b="天柱山风景名胜区，位于安徽省安庆市潜山市西部，景区因主峰如“擎天一柱”而得名，被誉为“江淮第一山”，主要有天柱峰、飞来峰、天池峰，千米以上高峰有45座，主峰海拔为1488.4米，景区规划保护区面积为333平方公里，风景区面积为82.46平方公里。天柱山风景名胜区内分布有名崖、奇石、异洞、涧瀑、云海等自然景观，位列安徽省三大名山之一（黄山、九华山、天柱山）。景区宗教文化积淀深厚，是中华佛教禅宗发源地之一。禅宗第三代祖师僧璨在此驻锡弘法、传承衣钵。三祖寺多次受到历代帝王加封，享有“禅林谁第一，此地冠南州”的盛誉。保留有“解缚石”、三祖舍利塔、三祖洞等珍贵文物。1982年，被国务院批准为首批国家重点风景名胜区。1992年，被批准为国家森林公园。2000年，被评为国家AAAAA级旅游景区、 2011年，被批准为世界地质公园。"#本作品作者吴宇航
                    elif a == "沙巴州":#本作品作者吴宇航
                        b="沙巴州（Negeri Sabah）简称沙州，旧称北婆罗洲，有“风下之地”之美誉，是马来西亚十三个州之一，首府亚庇（旧称哥打京那峇鲁）。位于加里曼丹岛东北部，面积74500平方公里，人口共385.38万（2017年）  ，属于热带雨林气候。沙巴州下设5省，即西海岸省、内陆省、古达省、山打根省、及斗湖省。  2016年沙巴州生产总值达到738亿令吉，人均收入21081令吉，低于马来西亚人均收入38887令吉。  沙巴于1881年至1963年间被英国人统治，直到1963年8月31日起自治（国防、外交、财政、内政等事务仍由英国殖民政府掌管）。1963年9月16日，沙巴加入马来西亚。1984年，沙巴州政府将纳闽分割出来设立成联邦直辖区，是马来西亚唯一的岸外金融中心。"#本作品作者吴宇航
                    elif a == "亚庇国际机场":#本作品作者吴宇航
                        b="亚庇国际机场（IATA：BKI，ICAO：WBKK）是马来西亚沙巴最繁忙的国际机场，也是继吉隆坡国际机场全国第二繁忙的机场。位于亚庇市中心附近，是亚洲航空、马来西亚航空的重点城市。机场分为两个航厦，分为第一航厦（Terminal 1）和第二航厦（Terminal 2）。 2006年服务200万名乘客。"#本作品作者吴宇航
                    elif a == "贝勒大学":#本作品作者吴宇航
                        b="（Baylor University）创立于1845年, 是德克萨斯州历史上最悠久的大学，也是美国密西西比河以西的第一批教育机构之一。 该大学位于达拉斯 - 沃斯堡大都会区和奥斯汀之间，沿着布拉佐斯河畔而建，占地1000英亩(约4平方公里)。它是一所世界享有盛誉的私立研究型大学，也是世界上最大的浸信会大学校园。"#本作品作者吴宇航
                    elif a == "君主立宪制":#本作品作者吴宇航
                        b="君主立宪制（英语：Constitutional monarchy），亦即“有限君主制”，是相对于君主专制的一种国家体制。君主立宪是在保留君主制的前提下，通过立宪，树立人民主权、限制君主权力、实现事务上的共和主义理想但不采用共和政体。可分为二元制君主立宪制、议会制君主立宪制。英国的“光荣革命”为君主立宪制国家开启了先例。一般君主是终身制的，君主的地位从定义上就已经高于国家的其他公民（这是君主与一些其他元首如独裁者的一个区别），往往君主属于一个特别的阶层（贵族），此外世袭制也往往是君主的一个特点。君主虽然是国家元首（head of state），但君主的产生方式与权力范围，会依各个国家的制度而不同；纵使是同一个国家，往往在不同时期，君主的产生方式与权力范围也各不相同。君主立宪制与一个国家的国情和文化传统有着密切关系，它具有一定的进步性，同时也有一定的妥协性，局限性。英国在革命后通过《权利法案》首先确定。"#本作品作者吴宇航
                    elif a == "佛罗里达大学":#本作品作者吴宇航
                        b="佛罗里达大学（University of Florida，简称UF，也称作UFL）是位于美国佛罗里达州盖恩斯维尔（Gainesville）的一所著名的公立研究型大学。佛罗里达大学是北美顶尖大学联盟美国大学协会（AAU）成员之一，建校可追溯至1853年。佛罗里达大学被誉为公立常春藤，在《美国新闻与世界报道（US NEWS）》2019全美综合排名中排第35位，位列全美公立大学第8位；2017年niche   全美公立大学排名第12位，在《美国新闻与世界报道（US NEWS）》2016世界大学排名中排世界第47位。在2018-2019 CWUR世界大学排名中排世界第62位   。在美国本土国家大学排名体系中位列全球第50名。世界大学学术表现排行（URAP）位列世界45名。大学作为全美最大的研究型大学之一，每年为佛罗里达州经济贡献近60亿美元，并创造近七万五千个工作职位。佛罗里达大学共获得研究资金五亿八千三百万美元，其金额超过佛州所有其他大学的总和。学校有超过40位美国国家科学院，工程院，医学院院士。著名的校友包括成功破译遗传密码的Marshall Nirenberg，最早成功提出超导体的微观理论的John Robert Schrieffer，安塔娜索夫-数字计算机之父、卡德-佳得乐饮料的发明者、女星费唐纳威、男星埃布森、佛罗里达州州长。同时贡献了多位NBA球星，如贾森威廉姆斯，阿尔霍福德，钱德勒帕森斯等。校友中至少有10位参议员，40位众议员，17位州长，2位诺贝尔奖得主，3位NASA宇航员和几十位专业运动员，及多位普利策奖和菲尔兹奖获得者。"#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        b='词库暂时没有该词可联系作者添加'#本作品作者吴宇航
                    message=b#本作品作者吴宇航
                wx.MessageBox(message)  #本作品作者吴宇航
        if __name__ == '__main__':#本作品作者吴宇航
            app = wx.App()                      #本作品作者吴宇航
            frame = MyFrame(parent=None,id=-1)  #本作品作者吴宇航
            frame.Show()                       #本作品作者吴宇航
            app.MainLoop()#本作品作者吴宇航
            fasdasdf1()#本作品作者吴宇航
    elif dakai == "jisuan":#本作品作者吴宇航
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
        fasdasdf1()#本作品作者吴宇航
    #     suyinshu,sb,list3,List1,r_list,bilishu = [],{},[],[],[],[]#本作品作者吴宇航
    #     global zuida,x_x,x_x2,x_x3,chooseuser#本作品作者吴宇航
    #     global jieguo1#本作品作者吴宇航
    #     jieguo1 = 0#本作品作者吴宇航
    #     zuida = 0#本作品作者吴宇航
    #     import webbrowser#本作品作者吴宇航
    #     def jitutonglong(toushu,tuishu):#本作品作者吴宇航
    #         tuishu = tuishu - toushu * 2#本作品作者吴宇航
    #         a = int(tuishu / 2)#本作品作者吴宇航
    #         if a % 1 == 0 and (toushu - a) % 1 == 0:#本作品作者吴宇航
    #             return "兔" + str(a) + "只鸡" + str(toushu - a) + "只"#本作品作者吴宇航
    #         else:#本作品作者吴宇航
    #             return "无解"#本作品作者吴宇航
    #     def youxi(mode,a,b):#本作品作者吴宇航
    #         if mode == "1":#本作品作者吴宇航
    #             return a ** b#本作品作者吴宇航
    #         elif mode == "2":#本作品作者吴宇航
    #             a = a ** (1 / b)#本作品作者吴宇航
    #             return a#本作品作者吴宇航
    #         elif mode == "3":#本作品作者吴宇航
    #             return log(b,a)#本作品作者吴宇航
    #     def hunxunhuan(a,xunhuanjie):#本作品作者吴宇航
    #         if a[0] == "0":#本作品作者吴宇航
    #             nima = ""#本作品作者吴宇航
    #             for i in range(len(xunhuanjie)):#本作品作者吴宇航
    #                 nima = nima + "9"#本作品作者吴宇航
    #             for i in range(len(a) - 2 - len(xunhuanjie)):#本作品作者吴宇航
    #                 nima = nima + "0"#本作品作者吴宇航
    #             a = int(a.replace("0.",""))#本作品作者吴宇航
    #             nima2 = int(str(a).replace(xunhuanjie,""))#本作品作者吴宇航
    #             b = a - nima2#本作品作者吴宇航
    #             a = int(nima)#本作品作者吴宇航
    #             zuida = 0#本作品作者吴宇航
    #             suyinshu.clear()#本作品作者吴宇航
    #             if a % b == 0:#本作品作者吴宇航
    #                 zuida = b#本作品作者吴宇航
    #             elif b % a == 0:#本作品作者吴宇航
    #                 zuida = a#本作品作者吴宇航
    #             else:#本作品作者吴宇航
    #                 d = a#本作品作者吴宇航
    #                 e = b#本作品作者吴宇航
    #                 list3.clear()#本作品作者吴宇航
    #                 if d > e:#本作品作者吴宇航
    #                     if e % 2 == 0:#本作品作者吴宇航
    #                         o = e / 2#本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         o = (e - 1) / 2 #本作品作者吴宇航
    #                 else:#本作品作者吴宇航
    #                     if d % 2 == 0:#本作品作者吴宇航
    #                         o = d / 2#本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         o = (d - 1) / 2#本作品作者吴宇航
    #                 for i in range(1,int(o + 1)):#本作品作者吴宇航
    #                     if d % i == 0 and e % i == 0:#本作品作者吴宇航
    #                         if zhihe(i) == "N":#本作品作者吴宇航
    #                             suyinshu.append(i)#本作品作者吴宇航
    #                             if i != 1:#本作品作者吴宇航
    #                                 list3.append(i)#本作品作者吴宇航
    #                             d = d / i#本作品作者吴宇航
    #                             e = e / i#本作品作者吴宇航
    #                 while True:#本作品作者吴宇航
    #                     if len(list3) == 0:#本作品作者吴宇航
    #                         break#本作品作者吴宇航
    #                     list3.clear()#本作品作者吴宇航
    #                     if d > e:#本作品作者吴宇航
    #                         if e % 2 == 0:#本作品作者吴宇航
    #                             o = e / 2#本作品作者吴宇航
    #                         else:#本作品作者吴宇航
    #                             o = (e - 1) / 2 #本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         if d % 2 == 0:#本作品作者吴宇航
    #                             o = d / 2#本作品作者吴宇航
    #                         else:#本作品作者吴宇航
    #                             o = (d - 1) / 2#本作品作者吴宇航
    #                     for i in range(2,int(o + 1)):#本作品作者吴宇航
    #                         if d % i == 0 and e % i == 0:#本作品作者吴宇航
    #                             if zhihe(i) == "N":#本作品作者吴宇航
    #                                 suyinshu.append(i)#本作品作者吴宇航
    #                                 list3.append(i)#本作品作者吴宇航
    #                                 d = d / i#本作品作者吴宇航
    #                                 e = e / i#本作品作者吴宇航
    #                 d = 1#本作品作者吴宇航
    #                 for i in range(len(suyinshu)):#本作品作者吴宇航
    #                     if i != len(suyinshu) - 1:#本作品作者吴宇航
    #                         d = d * suyinshu[i]#本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         zuida = suyinshu[i] * d#本作品作者吴宇航
    #                 if zuida == 0:#本作品作者吴宇航
    #                     zuida = 1#本作品作者吴宇航
    #             return str(a // zuida) + "分之" + str(b // zuida)#本作品作者吴宇航
    #         else:#本作品作者吴宇航
    #             nima2 = ""#本作品作者吴宇航
    #             i = 1#本作品作者吴宇航
    #             while a.index(".") - i != -1:#本作品作者吴宇航
    #                 nima2 = a[a.index(".") - i] + nima2#本作品作者吴宇航
    #                 i += 1#本作品作者吴宇航
    #             nima = ""#本作品作者吴宇航
    #             for i in range(len(xunhuanjie)):#本作品作者吴宇航
    #                 nima = nima + "9"#本作品作者吴宇航
    #             for i in range(len(a) - len(nima2) - 1 - len(xunhuanjie)):#本作品作者吴宇航
    #                 nima = nima + "0"#本作品作者吴宇航
    #             a = int(a.replace(nima2 + ".",""))#本作品作者吴宇航
    #             nima2 = int(str(a).replace(xunhuanjie,""))#本作品作者吴宇航
    #             b = a - nima2#本作品作者吴宇航
    #             a = int(nima)#本作品作者吴宇航
    #             zuida = 0#本作品作者吴宇航
    #             suyinshu.clear()#本作品作者吴宇航
    #             if a % b == 0:#本作品作者吴宇航
    #                 zuida = b#本作品作者吴宇航
    #             elif b % a == 0:#本作品作者吴宇航
    #                 zuida = a#本作品作者吴宇航
    #             else:#本作品作者吴宇航
    #                 d = a#本作品作者吴宇航
    #                 e = b#本作品作者吴宇航
    #                 list3.clear()#本作品作者吴宇航
    #                 if d > e:#本作品作者吴宇航
    #                     if e % 2 == 0:#本作品作者吴宇航
    #                         o = e / 2#本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         o = (e - 1) / 2 #本作品作者吴宇航
    #                 else:#本作品作者吴宇航
    #                     if d % 2 == 0:#本作品作者吴宇航
    #                         o = d / 2#本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         o = (d - 1) / 2#本作品作者吴宇航
    #                 for i in range(1,int(o + 1)):#本作品作者吴宇航
    #                     if d % i == 0 and e % i == 0:#本作品作者吴宇航
    #                         if zhihe(i) == "N":#本作品作者吴宇航
    #                             suyinshu.append(i)#本作品作者吴宇航
    #                             if i != 1:#本作品作者吴宇航
    #                                 list3.append(i)#本作品作者吴宇航
    #                             d = d / i#本作品作者吴宇航
    #                             e = e / i#本作品作者吴宇航
    #                 while True:#本作品作者吴宇航
    #                     if len(list3) == 0:#本作品作者吴宇航
    #                         break#本作品作者吴宇航
    #                     list3.clear()#本作品作者吴宇航
    #                     if d > e:#本作品作者吴宇航
    #                         if e % 2 == 0:#本作品作者吴宇航
    #                             o = e / 2#本作品作者吴宇航
    #                         else:#本作品作者吴宇航
    #                             o = (e - 1) / 2 #本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         if d % 2 == 0:#本作品作者吴宇航
    #                             o = d / 2#本作品作者吴宇航
    #                         else:#本作品作者吴宇航
    #                             o = (d - 1) / 2#本作品作者吴宇航
    #                     for i in range(2,int(o + 1)):#本作品作者吴宇航
    #                         if d % i == 0 and e % i == 0:#本作品作者吴宇航
    #                             if zhihe(i) == "N":#本作品作者吴宇航
    #                                 suyinshu.append(i)#本作品作者吴宇航
    #                                 list3.append(i)#本作品作者吴宇航
    #                             d = d / i#本作品作者吴宇航
    #                             e = e / i#本作品作者吴宇航
    #                 d = 1#本作品作者吴宇航
    #                 for i in range(len(suyinshu)):#本作品作者吴宇航
    #                     if i != len(suyinshu) - 1:#本作品作者吴宇航
    #                         d = d * suyinshu[i]#本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         zuida = suyinshu[i] * d#本作品作者吴宇航
    #                 if zuida == 0:#本作品作者吴宇航
    #                     zuida = 1#本作品作者吴宇航
    #                 return str(nima2) + "又" + str(a // zuida) + "分之" + str(b // zuida)#本作品作者吴宇航
    #     def jueduizhi(a):#本作品作者吴宇航
    #         return abs(a)#本作品作者吴宇航
    #     def abaabaaba(hahaha):#本作品作者吴宇航
    #         List1.clear()#本作品作者吴宇航
    #         if hahaha.count("/") == 2:#本作品作者吴宇航
    #             if "+" in hahaha:#本作品作者吴宇航
    #                 nima = hahaha[hahaha.index("+") - 1]#本作品作者吴宇航
    #                 i = 2#本作品作者吴宇航
    #                 while hahaha[hahaha.index("+") - i] != "/":#本作品作者吴宇航
    #                     nima = hahaha[hahaha.index("+") - i] + nima#本作品作者吴宇航
    #                     i += 1#本作品作者吴宇航
    #                 nima = float(nima)#本作品作者吴宇航
    #                 nima2 = hahaha[hahaha.index("=") - 1]#本作品作者吴宇航
    #                 i = 2#本作品作者吴宇航
    #                 while hahaha[hahaha.index("=") - i] != "/":#本作品作者吴宇航
    #                     nima2 = hahaha[hahaha.index("=") - i] + nima2#本作品作者吴宇航
    #                     i += 1#本作品作者吴宇航
    #                 nima2 = float(nima2)#本作品作者吴宇航
    #                 zonghe = hahaha[len(hahaha) - 1]#本作品作者吴宇航
    #                 i = 2#本作品作者吴宇航
    #                 while hahaha[len(hahaha) - i] != "=":#本作品作者吴宇航
    #                     zonghe = hahaha[len(hahaha) - i] + zonghe#本作品作者吴宇航
    #                     i += 1#本作品作者吴宇航
    #                 zonghe = int(zonghe)#本作品作者吴宇航
    #                 for i in range(int(zonghe * nima * nima2)):#本作品作者吴宇航
    #                     if i % nima == 0:#本作品作者吴宇航
    #                         if i not in List1 and (zonghe - i / nima) * nima not in List1:#本作品作者吴宇航
    #                             if i >= 0 and (zonghe - i / nima) * nima2 >= 0:#本作品作者吴宇航
    #                                 List1.append(i)#本作品作者吴宇航
    #                                 List1.append(int((zonghe - i / nima) * nima2))#本作品作者吴宇航
    #                 return List1#本作品作者吴宇航
    #             nima = hahaha[hahaha.index("-") - 1]#本作品作者吴宇航
    #             i = 2#本作品作者吴宇航
    #             while hahaha[hahaha.index("-") - i] != "/":#本作品作者吴宇航
    #                 nima = hahaha[hahaha.index("-") - i] + nima#本作品作者吴宇航
    #                 i += 1#本作品作者吴宇航
    #             nima = float(nima)#本作品作者吴宇航
    #             nima2 = hahaha[hahaha.index("=") - 1]#本作品作者吴宇航
    #             i = 2#本作品作者吴宇航
    #             while hahaha[hahaha.index("=") - i] != "/":#本作品作者吴宇航
    #                 nima2 = hahaha[hahaha.index("=") - i] + nima2#本作品作者吴宇航
    #                 i += 1#本作品作者吴宇航
    #             nima2 = float(nima2)#本作品作者吴宇航
    #             zonghe = hahaha[len(hahaha) - 1]#本作品作者吴宇航
    #             i = 2#本作品作者吴宇航
    #             while hahaha[len(hahaha) - i] != "=":#本作品作者吴宇航
    #                 zonghe = hahaha[len(hahaha) - i] + zonghe#本作品作者吴宇航
    #                 i += 1#本作品作者吴宇航
    #             zonghe = int(zonghe)#本作品作者吴宇航
    #             i = 0#本作品作者吴宇航
    #             while True:#本作品作者吴宇航
    #                 if i % nima == 0:#本作品作者吴宇航
    #                     if i not in List1 and (zonghe - i / nima) * nima2 not in List1:#本作品作者吴宇航
    #                         if i >= 0 and (zonghe - i / nima) * nima3 >= 0:#本作品作者吴宇航
    #                             list1.append(i)#本作品作者吴宇航
    #                             list1.append(int((zonghe - i / nima) * nima2))#本作品作者吴宇航
    #                             break#本作品作者吴宇航
    #             for i in range(1,11):#本作品作者吴宇航
    #                 list1.append(list1[0] + nima * i)#本作品作者吴宇航
    #                 list1.append(list1[1] + nima2 * i)#本作品作者吴宇航
    #             return list1#本作品作者吴宇航
    #         elif hahaha.count("/") == 0:#本作品作者吴宇航
    #             if "+" in hahaha:#本作品作者吴宇航
    #                 nima = hahaha[hahaha.index("*") - 1]#本作品作者吴宇航
    #                 i = 2#本作品作者吴宇航
    #                 while hahaha.index("*") - i != -1:#本作品作者吴宇航
    #                     nima = hahaha[hahaha.index("*") - i] + nima#本作品作者吴宇航
    #                     i += 1#本作品作者吴宇航
    #                 nima = float(nima)#本作品作者吴宇航
    #                 hahaha = hahaha.replace(str(nima) + "*x+","")#本作品作者吴宇航
    #                 nima2 = hahaha[hahaha.index("*") - 1]#本作品作者吴宇航
    #                 i = 2#本作品作者吴宇航
    #                 while hahaha.index("*") - i != -1:#本作品作者吴宇航
    #                     nima2 = hahaha[hahaha.index("*") - i] + nima2#本作品作者吴宇航
    #                     i += 1#本作品作者吴宇航
    #                 nima2 = float(nima2)#本作品作者吴宇航
    #                 zonghe = hahaha[len(hahaha) - 1]#本作品作者吴宇航
    #                 i = 2#本作品作者吴宇航
    #                 while hahaha[len(hahaha) - i] != "=":#本作品作者吴宇航
    #                     zonghe = hahaha[len(hahaha) - i] + nima#本作品作者吴宇航
    #                     i += 1#本作品作者吴宇航
    #                 zonghe = int(zonghe)#本作品作者吴宇航
    #                 for i in range(int(round(zonghe / nima,0))):#本作品作者吴宇航
    #                     if zonghe - i * nima % nima2 == 0:#本作品作者吴宇航
    #                         list1.append(i)#本作品作者吴宇航
    #                         list1.append(int((zonghe - i / nima) / nima2))#本作品作者吴宇航
    #                 return list1#本作品作者吴宇航
    #             nima = hahaha[hahaha.index("*") - 1]#本作品作者吴宇航
    #             i = 2#本作品作者吴宇航
    #             while hahaha.index("*") - i != -1:#本作品作者吴宇航
    #                 nima = hahaha[hahaha.index("*") - i] + nima#本作品作者吴宇航
    #                 i += 1#本作品作者吴宇航
    #             nima = float(nima)#本作品作者吴宇航
    #             hahaha = hahaha.replace(str(nima) + "*x+","")#本作品作者吴宇航
    #             nima2 = hahaha[hahaha.index("*") - 1]#本作品作者吴宇航
    #             i = 2#本作品作者吴宇航
    #             while hahaha.index("*") - i != -1:#本作品作者吴宇航
    #                 nima2 = hahaha[hahaha.index("*") - i] + nima2#本作品作者吴宇航
    #                 i += 1#本作品作者吴宇航
    #             nima2 = float(nima2)#本作品作者吴宇航
    #             zonghe = hahaha[len(hahaha) - 1]#本作品作者吴宇航
    #             i = 2#本作品作者吴宇航
    #             while hahaha[len(hahaha) - i] != "=":#本作品作者吴宇航
    #                 zonghe = hahaha[len(hahaha) - i] + nima#本作品作者吴宇航
    #                 i += 1#本作品作者吴宇航
    #             zonghe = int(zonghe)#本作品作者吴宇航
    #             for i in range(int(round(zonghe / nima,0))):#本作品作者吴宇航
    #                 if i * nima - zonghe % nima2 == 0:#本作品作者吴宇航
    #                     list1.append(i)#本作品作者吴宇航
    #                     list1.append(int((i / nima - zonghe) / nima2))#本作品作者吴宇航
    #             return list1#本作品作者吴宇航
    #         elif hahaha.count("/") == 1:#本作品作者吴宇航
    #             if hahaha.index("*") > hahaha.index("/") and "+" in hahaha:#本作品作者吴宇航
    #                 nima = hahaha[hahaha.index("+") - 1]#本作品作者吴宇航
    #                 i = 2#本作品作者吴宇航
    #                 while hahaha[hahaha.index("+") - i] != "/":#本作品作者吴宇航
    #                     nima = hahaha[hahaha.index("+") - i] + nima#本作品作者吴宇航
    #                     i += 1#本作品作者吴宇航
    #                 nima = float(nima)#本作品作者吴宇航
    #                 nima2 = hahaha[hahaha.index("=") - 1]#本作品作者吴宇航
    #                 i = 2#本作品作者吴宇航
    #                 while hahaha[hahaha.index("=") - i] != "/":#本作品作者吴宇航
    #                     nima2 = hahaha[hahaha.index("=") - i] + nima2#本作品作者吴宇航
    #                     i += 1#本作品作者吴宇航
    #                 nima2 = float(nima2)#本作品作者吴宇航
    #                 zonghe = hahaha[len(hahaha) - 1]#本作品作者吴宇航
    #                 i = 2#本作品作者吴宇航
    #                 while hahaha[len(hahaha) - i] != "=":#本作品作者吴宇航
    #                     zonghe = hahaha[len(hahaha) - i] + nima#本作品作者吴宇航
    #                     i += 1#本作品作者吴宇航
    #                 zonghe = int(zonghe)#本作品作者吴宇航
    #                 for i in range(zonghe * nima * nima2):#本作品作者吴宇航
    #                     if i % nima == 0:#本作品作者吴宇航
    #                         list1.append(i)#本作品作者吴宇航
    #                         list1.append(int((zonghe - i / nima) * nima2))#本作品作者吴宇航
    #                 return list1#本作品作者吴宇航
    #     def yiyuanerci(a):#本作品作者吴宇航
    #         x_x = a[a.index("x") - 1]#本作品作者吴宇航
    #         i = 2#本作品作者吴宇航
    #         while a.index("x") - i != -1:#本作品作者吴宇航
    #             x_x = a[a.index("x") - i] + x_x#本作品作者吴宇航
    #             i += 1#本作品作者吴宇航
    #         a = a.replace(x_x + "x^2","")#本作品作者吴宇航
    #         x_x2 = a[a.index("x") - 1]#本作品作者吴宇航
    #         i = 2#本作品作者吴宇航
    #         while a.index("x") - i != -1:#本作品作者吴宇航
    #             x_x2 = a[a.index("x") - i] + x_x2#本作品作者吴宇航
    #             i += 1#本作品作者吴宇航
    #         a = a.replace(x_x2 + "x","")#本作品作者吴宇航
    #         x_x3 = a[a.index("=") - 1]#本作品作者吴宇航
    #         i = 2#本作品作者吴宇航
    #         while a.index("=") - i != -1:#本作品作者吴宇航
    #             x_x3 = a[a.index("=") - i] + x_x3#本作品作者吴宇航
    #             i += 1#本作品作者吴宇航
    #         x_x,x_x2,x_x3 = float(x_x),float(x_x2),float(x_x3)#本作品作者吴宇航
    #         try:#本作品作者吴宇航
    #             haha = (-x_x2 + sqrt(x_x2 ** 2 - 4 * x_x * x_x3)) / (2 * x_x)#本作品作者吴宇航
    #             if haha % 1 == 0:#本作品作者吴宇航
    #                 haha = int(haha)#本作品作者吴宇航
    #             if "." in str(haha):#本作品作者吴宇航
    #                 a = ""#本作品作者吴宇航
    #                 i = 2#本作品作者吴宇航
    #                 while haha.index(".") - i != -1:#本作品作者吴宇航
    #                     a = str(haha)[haha.index(".") - i] + a#本作品作者吴宇航
    #                     i += 1#本作品作者吴宇航
    #                 if len(haha) - len(a) - 1 < 5:#本作品作者吴宇航
    #                     haha = str(2 * x_x) + "分之" + str(-x_x2) + "+" + str(x_x2 ** 2 - 4 * x_x * x_x3) + "的平方根"#本作品作者吴宇航
    #             ahah = (-x_x2 - sqrt(x_x2 ** 2 - 4 * x_x * x_x3)) / (2 * x_x)#本作品作者吴宇航
    #             if ahah % 1 == 0:#本作品作者吴宇航
    #                 ahah = int(ahah)#本作品作者吴宇航
    #             if "." in str(ahah):#本作品作者吴宇航
    #                 a = ""#本作品作者吴宇航
    #                 i = 2#本作品作者吴宇航
    #                 while ahah.index(".") - i != -1:#本作品作者吴宇航
    #                     a = str(ahah)[ahah.index(".") - i] + a#本作品作者吴宇航
    #                     i += 1#本作品作者吴宇航
    #                 if len(ahah) - len(a) - 1 < 5:#本作品作者吴宇航
    #                     ahah = str(2 * x_x) + "分之" + str(-x_x2) + "-" + str(x_x2 ** 2 - 4 * x_x * x_x3) + "的平方根"#本作品作者吴宇航
    #             return "x=" + str(haha) + "和" + str(ahah)#本作品作者吴宇航
    #         except:#本作品作者吴宇航
    #             print("这个方程没有解！")#本作品作者吴宇航
    #     def chunxunhuan(a):#本作品作者吴宇航
    #         if a[0] == "0":#本作品作者吴宇航
    #             nima = "9"#本作品作者吴宇航
    #             for i in range(len(a) - 3):#本作品作者吴宇航
    #                 nima = nima + "9"#本作品作者吴宇航
    #             b = a[2]#本作品作者吴宇航
    #             for i in range(3,len(a)):#本作品作者吴宇航
    #                 b = b + a[i]#本作品作者吴宇航
    #             b = int(b)#本作品作者吴宇航
    #             a = int(nima)#本作品作者吴宇航
    #             zuida = 0#本作品作者吴宇航
    #             suyinshu.clear()#本作品作者吴宇航
    #             if a % b == 0:#本作品作者吴宇航
    #                 zuida = b#本作品作者吴宇航
    #             elif b % a == 0:#本作品作者吴宇航
    #                 zuida = a#本作品作者吴宇航
    #             else:#本作品作者吴宇航
    #                 d = a#本作品作者吴宇航
    #                 e = b#本作品作者吴宇航
    #                 list3.clear()#本作品作者吴宇航
    #                 if d > e:#本作品作者吴宇航
    #                     if e % 2 == 0:#本作品作者吴宇航
    #                         o = e / 2#本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         o = (e - 1) / 2 #本作品作者吴宇航
    #                 else:#本作品作者吴宇航
    #                     if d % 2 == 0:#本作品作者吴宇航
    #                         o = d / 2#本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         o = (d - 1) / 2#本作品作者吴宇航
    #                 for i in range(1,int(o + 1)):#本作品作者吴宇航
    #                     if d % i == 0 and e % i == 0:#本作品作者吴宇航
    #                         if zhihe(i) == "N":#本作品作者吴宇航
    #                             suyinshu.append(i)#本作品作者吴宇航
    #                             if i != 1:#本作品作者吴宇航
    #                                 list3.append(i)#本作品作者吴宇航
    #                             d = d / i#本作品作者吴宇航
    #                             e = e / i#本作品作者吴宇航
    #                 while True:#本作品作者吴宇航
    #                     if len(list3) == 0:#本作品作者吴宇航
    #                         break#本作品作者吴宇航
    #                     list3.clear()#本作品作者吴宇航
    #                     if d > e:#本作品作者吴宇航
    #                         if e % 2 == 0:#本作品作者吴宇航
    #                             o = e / 2#本作品作者吴宇航
    #                         else:#本作品作者吴宇航
    #                             o = (e - 1) / 2 #本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         if d % 2 == 0:#本作品作者吴宇航
    #                             o = d / 2#本作品作者吴宇航
    #                         else:#本作品作者吴宇航
    #                             o = (d - 1) / 2#本作品作者吴宇航
    #                     for i in range(2,int(o + 1)):#本作品作者吴宇航
    #                         if d % i == 0 and e % i == 0:#本作品作者吴宇航
    #                             if zhihe(i) == "N":#本作品作者吴宇航
    #                                 suyinshu.append(i)#本作品作者吴宇航
    #                                 list3.append(i)#本作品作者吴宇航
    #                                 d = d / i#本作品作者吴宇航
    #                                 e = e / i#本作品作者吴宇航
    #                 d = 1#本作品作者吴宇航
    #                 for i in range(len(suyinshu)):#本作品作者吴宇航
    #                     if i != len(suyinshu) - 1:#本作品作者吴宇航
    #                         d = d * suyinshu[i]#本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         zuida = suyinshu[i] * d#本作品作者吴宇航
    #                 if zuida == 0:#本作品作者吴宇航
    #                     zuida = 1#本作品作者吴宇航
    #             return str(a // zuida) + "分之" + str(b // zuida)#本作品作者吴宇航
    #         else:#本作品作者吴宇航
    #             nima2 = a#本作品作者吴宇航
    #             nima = "9"#本作品作者吴宇航
    #             for i in range(len(a) - 2 - a.index(".")):#本作品作者吴宇航
    #                 nima = nima + "9"#本作品作者吴宇航
    #             b = a[a.index(".") + 1]#本作品作者吴宇航
    #             for i in range(a.index(".") + 2,len(a)):#本作品作者吴宇航
    #                 b = b + a[i]#本作品作者吴宇航
    #             b = int(b)#本作品作者吴宇航
    #             a = int(nima)#本作品作者吴宇航
    #             zuida = 0#本作品作者吴宇航
    #             suyinshu.clear()#本作品作者吴宇航
    #             if a % b == 0:#本作品作者吴宇航
    #                 zuida = b#本作品作者吴宇航
    #             elif b % a == 0:#本作品作者吴宇航
    #                 zuida = a#本作品作者吴宇航
    #             else:#本作品作者吴宇航
    #                 d = a#本作品作者吴宇航
    #                 e = b#本作品作者吴宇航
    #                 list3.clear()#本作品作者吴宇航
    #                 if d > e:#本作品作者吴宇航
    #                     if e % 2 == 0:#本作品作者吴宇航
    #                         o = e / 2#本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         o = (e - 1) / 2 #本作品作者吴宇航
    #                 else:#本作品作者吴宇航
    #                     if d % 2 == 0:#本作品作者吴宇航
    #                         o = d / 2#本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         o = (d - 1) / 2#本作品作者吴宇航
    #                 for i in range(1,int(o + 1)):#本作品作者吴宇航
    #                     if d % i == 0 and e % i == 0:#本作品作者吴宇航
    #                         if zhihe(i) == "N":#本作品作者吴宇航
    #                             suyinshu.append(i)#本作品作者吴宇航
    #                             if i != 1:#本作品作者吴宇航
    #                                 list3.append(i)#本作品作者吴宇航
    #                             d = d / i#本作品作者吴宇航
    #                             e = e / i#本作品作者吴宇航
    #                 while True:#本作品作者吴宇航
    #                     if len(list3) == 0:#本作品作者吴宇航
    #                         break#本作品作者吴宇航
    #                     list3.clear()#本作品作者吴宇航
    #                     if d > e:#本作品作者吴宇航
    #                         if e % 2 == 0:#本作品作者吴宇航
    #                             o = e / 2#本作品作者吴宇航
    #                         else:#本作品作者吴宇航
    #                             o = (e - 1) / 2 #本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         if d % 2 == 0:#本作品作者吴宇航
    #                             o = d / 2#本作品作者吴宇航
    #                         else:#本作品作者吴宇航
    #                             o = (d - 1) / 2#本作品作者吴宇航
    #                     for i in range(2,int(o + 1)):#本作品作者吴宇航
    #                         if d % i == 0 and e % i == 0:#本作品作者吴宇航
    #                             if zhihe(i) == "N":#本作品作者吴宇航
    #                                 suyinshu.append(i)#本作品作者吴宇航
    #                                 list3.append(i)#本作品作者吴宇航
    #                                 d = d / i#本作品作者吴宇航
    #                                 e = e / i#本作品作者吴宇航
    #                 d = 1#本作品作者吴宇航
    #                 for i in range(len(suyinshu)):#本作品作者吴宇航
    #                     if i != len(suyinshu) - 1:#本作品作者吴宇航
    #                         d = d * suyinshu[i]#本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         zuida = suyinshu[i] * d#本作品作者吴宇航
    #                 if zuida == 0:#本作品作者吴宇航
    #                     zuida = 1#本作品作者吴宇航
    #             return str(nima2) + "又" + str(a // zuida) + "分之" + str(b // zuida)#本作品作者吴宇航
    #     def find_all(data,s):#本作品作者吴宇航
    #         r_list = []#本作品作者吴宇航
    #         for i in range(len(data)):#本作品作者吴宇航
    #             if data[i] == s:#本作品作者吴宇航
    #                 break#本作品作者吴宇航
    #             r_list.append(data[i])#本作品作者吴宇航
    #         return r_list#本作品作者吴宇航
    #     def bili(mode,a,bilishu):#本作品作者吴宇航
    #         zuida = 0#本作品作者吴宇航
    #         for i in bilishu:#本作品作者吴宇航
    #             zuida += i#本作品作者吴宇航
    #         zuida = a / zuida#本作品作者吴宇航
    #         for i in range(len(bilishu)):#本作品作者吴宇航
    #             bilishu[i] = bilishu[i] * zuida#本作品作者吴宇航
    #         return bilishu#本作品作者吴宇航
    #     def erjiedengcha(mode,shouxiang,dierxiang,gongcha,a):#本作品作者吴宇航
    #         if mode == 1:#本作品作者吴宇航
    #             if a == 1:#本作品作者吴宇航
    #                 return shouxiang#本作品作者吴宇航
    #             nima = dierxiang - shouxiang#本作品作者吴宇航
    #             nima2 = shouxiang#本作品作者吴宇航
    #             for i in range(a - 2):#本作品作者吴宇航
    #                 nima2 += nima#本作品作者吴宇航
    #                 nima += gongcha#本作品作者吴宇航
    #             nima = nima2 + nima#本作品作者吴宇航
    #             i = 0#本作品作者吴宇航
    #             while True:#本作品作者吴宇航
    #                 if not i < nima:#本作品作者吴宇航
    #                     break#本作品作者吴宇航
    #                 i += 1#本作品作者吴宇航
    #             if nima - i == 0:#本作品作者吴宇航
    #                 return int(nima)#本作品作者吴宇航
    #             else:#本作品作者吴宇航
    #                 return nima#本作品作者吴宇航
    #         else:#本作品作者吴宇航
    #             if a == shouxiang:#本作品作者吴宇航
    #                 return 1#本作品作者吴宇航
    #             nima = dierxiang - shouxiang#本作品作者吴宇航
    #             nima2 = shouxiang#本作品作者吴宇航
    #             i = 3#本作品作者吴宇航
    #             while True:#本作品作者吴宇航
    #                 nima2 += nima#本作品作者吴宇航
    #                 nima += gongcha#本作品作者吴宇航
    #                 if nima2 == a:#本作品作者吴宇航
    #                     return i#本作品作者吴宇航
    #                 if nima2 > a:#本作品作者吴宇航
    #                     return "N"#本作品作者吴宇航
    #                 i += 1#本作品作者吴宇航
    #     def denbishulie(mode,shouxiang,gongbi,a):#本作品作者吴宇航
    #         if mode == 1:#本作品作者吴宇航
    #             return shouxiang * gongbi ** (a - 1)#本作品作者吴宇航
    #         if mode == 2:#本作品作者吴宇航
    #             if a == shouxiang:#本作品作者吴宇航
    #                 return a#本作品作者吴宇航
    #             else:#本作品作者吴宇航
    #                 ia = shouxiang#本作品作者吴宇航
    #                 ai = shouxiang * gongbi#本作品作者吴宇航
    #                 i = 3#本作品作者吴宇航
    #                 while True:#本作品作者吴宇航
    #                     if i % 2 == 1:#本作品作者吴宇航
    #                         ia = ai * gongbi#本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         ai = ia * gongbi#本作品作者吴宇航
    #                     if ia == a or ai == a:#本作品作者吴宇航
    #                         return i#本作品作者吴宇航
    #                     if ia > a or ai > a:#本作品作者吴宇航
    #                         return "N"#本作品作者吴宇航
    #                     i += 1#本作品作者吴宇航
    #     def dengchashulie(mode,shouxiang,gongcha,a):#本作品作者吴宇航
    #         if mode == 1:#本作品作者吴宇航
    #             nima = shouxiang + gongcha * (a - 1)#本作品作者吴宇航
    #             if nima % 1 == 0:#本作品作者吴宇航
    #                 return int(nima)#本作品作者吴宇航
    #             else:#本作品作者吴宇航
    #                 return nima#本作品作者吴宇航
    #         if mode == 2:#本作品作者吴宇航
    #             nima = (a - shouxiang) / gongcha + 1#本作品作者吴宇航
    #             if nima % 1 == 0:#本作品作者吴宇航
    #                 return int(nima)#本作品作者吴宇航
    #             else:#本作品作者吴宇航
    #                 return "N"#本作品作者吴宇航
    #         elif mode == 3:#本作品作者吴宇航
    #             nima = (shouxiang * 2 + gongcha * (a - 1)) * a / 2#本作品作者吴宇航
    #             if nima % 1 == 0:#本作品作者吴宇航
    #                 return int(nima)#本作品作者吴宇航
    #             else:#本作品作者吴宇航
    #                 return nima#本作品作者吴宇航
    #     def feibonaqi(mode,a):#本作品作者吴宇航
    #         if mode == "1":#本作品作者吴宇航
    #             if a == 1:#本作品作者吴宇航
    #                 return 1#本作品作者吴宇航
    #             ia = 1#本作品作者吴宇航
    #             ai = 1#本作品作者吴宇航
    #             for i in range(a - 2):#本作品作者吴宇航
    #                 if i % 2 == 0:#本作品作者吴宇航
    #                     ia += ai#本作品作者吴宇航
    #                 else:#本作品作者吴宇航
    #                     ai += ia#本作品作者吴宇航
    #             if i % 2 == 0:#本作品作者吴宇航
    #                 return ia#本作品作者吴宇航
    #             return ai#本作品作者吴宇航
    #         else:#本作品作者吴宇航
    #             if a == 1:#本作品作者吴宇航
    #                 return 1#本作品作者吴宇航
    #             else:#本作品作者吴宇航
    #                 i = 3#本作品作者吴宇航
    #                 ia = 1#本作品作者吴宇航
    #                 ai = 1#本作品作者吴宇航
    #                 while True:#本作品作者吴宇航
    #                     if i % 2 == 1:#本作品作者吴宇航
    #                         ia += ai#本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         ai += ia#本作品作者吴宇航
    #                     if ia == a or ai == a:#本作品作者吴宇航
    #                         return i#本作品作者吴宇航
    #                     if ia > a or ai > a:#本作品作者吴宇航
    #                         return "N"#本作品作者吴宇航
    #                     i += 1#本作品作者吴宇航
    #     def fenshudaxiao(a,b,c,d):#本作品作者吴宇航
    #         zuida = 0#本作品作者吴宇航
    #         suyinshu.clear()#本作品作者吴宇航
    #         if a % b == 0:#本作品作者吴宇航
    #             zuida = b#本作品作者吴宇航
    #         elif b % a == 0:#本作品作者吴宇航
    #             zuida = a#本作品作者吴宇航
    #         else:#本作品作者吴宇航
    #             z = a#本作品作者吴宇航
    #             e = b#本作品作者吴宇航
    #             list3.clear()#本作品作者吴宇航
    #             if z > e:#本作品作者吴宇航
    #                 if e % 2 == 0:#本作品作者吴宇航
    #                     o = e / 2#本作品作者吴宇航
    #                 else:#本作品作者吴宇航
    #                     o = (e - 1) / 2 #本作品作者吴宇航
    #             else:#本作品作者吴宇航
    #                 if z % 2 == 0:#本作品作者吴宇航
    #                     o = z / 2#本作品作者吴宇航
    #                 else:#本作品作者吴宇航
    #                     o = (z - 1) / 2#本作品作者吴宇航
    #             for i in range(2,int(o + 1)):#本作品作者吴宇航
    #                 if z % i == 0 and e % i == 0:#本作品作者吴宇航
    #                     if zhihe(i) == "N":#本作品作者吴宇航
    #                         suyinshu.append(i)#本作品作者吴宇航
    #                         if i != 1:    #本作品作者吴宇航
    #                             list3.append(i)#本作品作者吴宇航
    #                         z = z / i#本作品作者吴宇航
    #                         e = e / i#本作品作者吴宇航
    #             while True:#本作品作者吴宇航
    #                 if len(list3) == 0:#本作品作者吴宇航
    #                     break#本作品作者吴宇航
    #                 list3.clear()#本作品作者吴宇航
    #                 if z > e:#本作品作者吴宇航
    #                     if e % 2 == 0:#本作品作者吴宇航
    #                         o = e / 2#本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         o = (e - 1) / 2 #本作品作者吴宇航
    #                 else:#本作品作者吴宇航
    #                     if z % 2 == 0:#本作品作者吴宇航
    #                         o = z / 2#本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         o = (z - 1) / 2#本作品作者吴宇航
    #                 for i in range(2,int(o + 1)):#本作品作者吴宇航
    #                     if z % i == 0 and e % i == 0:#本作品作者吴宇航
    #                         if zhihe(i) == "N":#本作品作者吴宇航
    #                             suyinshu.append(i)#本作品作者吴宇航
    #                             list3.append(i)#本作品作者吴宇航
    #                             z = z / i#本作品作者吴宇航
    #                             e = e / i#本作品作者吴宇航
    #             z = 1#本作品作者吴宇航
    #             for i in range(len(suyinshu)):#本作品作者吴宇航
    #                 if i != len(suyinshu) - 1:#本作品作者吴宇航
    #                     d = d * suyinshu[i]#本作品作者吴宇航
    #                 else:#本作品作者吴宇航
    #                     zuida = suyinshu[i] * z#本作品作者吴宇航
    #             if zuida == 0:#本作品作者吴宇航
    #                 zuida = 1#本作品作者吴宇航
    #         c = c * (b / zuida)#本作品作者吴宇航
    #         d = d * (a / zuida)#本作品作者吴宇航
    #         if c > d:#本作品作者吴宇航
    #             return 1#本作品作者吴宇航
    #         elif d > c:#本作品作者吴宇航
    #             return 2#本作品作者吴宇航
    #         else:#本作品作者吴宇航
    #             return "="#本作品作者吴宇航
    #     def zhihe(a):#本作品作者吴宇航
    #         if a == 1 or a == 0:#本作品作者吴宇航
    #             return "既不是素数也不是合数"#本作品作者吴宇航
    #         if a != 2 and a % 2 == 0:#本作品作者吴宇航
    #             return 2#本作品作者吴宇航
    #         for i in range(2,int(a / 2)):#本作品作者吴宇航
    #             if a == 2:#本作品作者吴宇航
    #                 return "N"#本作品作者吴宇航
    #             if a % i == 0:#本作品作者吴宇航
    #                 return i#本作品作者吴宇航
    #         return "N"#本作品作者吴宇航
    #     def fenjie(a):#本作品作者吴宇航
    #         suyinshu,d,sb,list3 = [],a,{},[]#本作品作者吴宇航
    #         for i in range(2,d):#本作品作者吴宇航
    #             if a % i == 0 and zhihe(i) == "N":#本作品作者吴宇航
    #                 suyinshu.append(i)#本作品作者吴宇航
    #                 list3.append(i)#本作品作者吴宇航
    #                 d = d // i#本作品作者吴宇航
    #         while len(list3) != 0:#本作品作者吴宇航
    #             list3.clear()#本作品作者吴宇航
    #             for j in range(2,int(d) + 1):#本作品作者吴宇航
    #                 if d % j == 0 and zhihe(j) == "N":#本作品作者吴宇航
    #                     suyinshu.append(j)#本作品作者吴宇航
    #                     list3.append(j)#本作品作者吴宇航
    #                     d = d / j#本作品作者吴宇航
    #         if len(suyinshu) == 0:#本作品作者吴宇航
    #             print("这是个质数！")#本作品作者吴宇航
    #         else:#本作品作者吴宇航
    #             for i in suyinshu:#本作品作者吴宇航
    #                 if i not in sb:#本作品作者吴宇航
    #                     sb[i] = suyinshu.count(i)#本作品作者吴宇航
    #             nima3 = ""#本作品作者吴宇航
    #             for nima in sb:#本作品作者吴宇航
    #                 for i in range(sb[nima]):#本作品作者吴宇航
    #                     nima3 = nima3 + str(nima) + "×"#本作品作者吴宇航
    #             nima3 = nima3[:-1]#本作品作者吴宇航
    #             return str(a) + "=" + nima3#本作品作者吴宇航
    #     def common_factor(a,b):#本作品作者吴宇航
    #         zuida = 0#本作品作者吴宇航
    #         suyinshu.clear()#本作品作者吴宇航
    #         if a % b == 0:#本作品作者吴宇航
    #             return b#本作品作者吴宇航
    #         if b % a == 0:#本作品作者吴宇航
    #             return a#本作品作者吴宇航
    #         d = a#本作品作者吴宇航
    #         e = b#本作品作者吴宇航
    #         list3.clear()#本作品作者吴宇航
    #         if d > e:#本作品作者吴宇航
    #             if e % 2 == 0:#本作品作者吴宇航
    #                 o = e / 2#本作品作者吴宇航
    #             else:#本作品作者吴宇航
    #                 o = (e - 1) / 2 #本作品作者吴宇航
    #         else:#本作品作者吴宇航
    #             if d % 2 == 0:#本作品作者吴宇航
    #                 o = d / 2#本作品作者吴宇航
    #             else:#本作品作者吴宇航
    #                 o = (d - 1) / 2#本作品作者吴宇航
    #         for i in range(1,int(o + 1)):#本作品作者吴宇航
    #             if d % i == 0 and e % i == 0:#本作品作者吴宇航
    #                 if zhihe(i) == "N":#本作品作者吴宇航
    #                     suyinshu.append(i)#本作品作者吴宇航
    #                     if i != 1:#本作品作者吴宇航
    #                         list3.append(i)#本作品作者吴宇航
    #                     d = d / i#本作品作者吴宇航
    #                     e = e / i#本作品作者吴宇航
    #         while True:#本作品作者吴宇航
    #             if len(list3) == 0:#本作品作者吴宇航
    #                 break#本作品作者吴宇航
    #             list3.clear()#本作品作者吴宇航
    #             if d > e:#本作品作者吴宇航
    #                 if e % 2 == 0:#本作品作者吴宇航
    #                     o = e / 2#本作品作者吴宇航
    #                 else:#本作品作者吴宇航
    #                     o = (e - 1) / 2 #本作品作者吴宇航
    #             else:#本作品作者吴宇航
    #                 if d % 2 == 0:#本作品作者吴宇航
    #                     o = d / 2#本作品作者吴宇航
    #                 else:#本作品作者吴宇航
    #                     o = (d - 1) / 2#本作品作者吴宇航
    #             for i in range(2,int(o + 1)):#本作品作者吴宇航
    #                 if d % i == 0 and e % i == 0:#本作品作者吴宇航
    #                     if zhihe(i) == "N":#本作品作者吴宇航
    #                         suyinshu.append(i)#本作品作者吴宇航
    #                         list3.append(i)#本作品作者吴宇航
    #                         d = d / i#本作品作者吴宇航
    #                         e = e / i#本作品作者吴宇航
    #         d = 1#本作品作者吴宇航
    #         for i in range(len(suyinshu)):#本作品作者吴宇航
    #             if i != len(suyinshu) - 1:#本作品作者吴宇航
    #                 d = d * suyinshu[i]#本作品作者吴宇航
    #             else:#本作品作者吴宇航
    #                 zuida = suyinshu[i] * d#本作品作者吴宇航
    #         if zuida == 0:#本作品作者吴宇航
    #             zuida = 1#本作品作者吴宇航
    #         return zuida  #本作品作者吴宇航
    #     def zuixiao(a,b):#本作品作者吴宇航
    #         zuida = 0#本作品作者吴宇航
    #         suyinshu.clear()#本作品作者吴宇航
    #         if a % b == 0:#本作品作者吴宇航
    #             zuida = b#本作品作者吴宇航
    #         elif b % a == 0:#本作品作者吴宇航
    #             zuida = a#本作品作者吴宇航
    #         else:#本作品作者吴宇航
    #             d = a#本作品作者吴宇航
    #             e = b#本作品作者吴宇航
    #             list3.clear()#本作品作者吴宇航
    #             if d > e:#本作品作者吴宇航
    #                 if e % 2 == 0:#本作品作者吴宇航
    #                     o = e / 2#本作品作者吴宇航
    #                 else:#本作品作者吴宇航
    #                     o = (e - 1) / 2 #本作品作者吴宇航
    #             else:#本作品作者吴宇航
    #                 if d % 2 == 0:#本作品作者吴宇航
    #                     o = d / 2#本作品作者吴宇航
    #                 else:#本作品作者吴宇航
    #                     o = (d - 1) / 2#本作品作者吴宇航
    #             for i in range(1,int(o + 1)):#本作品作者吴宇航
    #                 if d % i == 0 and e % i == 0:#本作品作者吴宇航
    #                     if zhihe(i) == "N":#本作品作者吴宇航
    #                         suyinshu.append(i)#本作品作者吴宇航
    #                         if i != 1:#本作品作者吴宇航
    #                             list3.append(i)#本作品作者吴宇航
    #                         d = d / i#本作品作者吴宇航
    #                         e = e / i#本作品作者吴宇航
    #             while True:#本作品作者吴宇航
    #                 if len(list3) == 0:#本作品作者吴宇航
    #                     break#本作品作者吴宇航
    #                 list3.clear()#本作品作者吴宇航
    #                 if d > e:#本作品作者吴宇航
    #                     if e % 2 == 0:#本作品作者吴宇航
    #                         o = e / 2#本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         o = (e - 1) / 2 #本作品作者吴宇航
    #                 else:#本作品作者吴宇航
    #                     if d % 2 == 0:#本作品作者吴宇航
    #                         o = d / 2#本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         o = (d - 1) / 2#本作品作者吴宇航
    #                 for i in range(2,int(o + 1)):#本作品作者吴宇航
    #                     if d % i == 0 and e % i == 0:#本作品作者吴宇航
    #                         if zhihe(i) == "N":#本作品作者吴宇航
    #                             suyinshu.append(i)#本作品作者吴宇航
    #                             list3.append(i)#本作品作者吴宇航
    #                             d = d / i#本作品作者吴宇航
    #                             e = e / i#本作品作者吴宇航
    #             d = 1#本作品作者吴宇航
    #             for i in range(len(suyinshu)):#本作品作者吴宇航
    #                 if i != len(suyinshu) - 1:#本作品作者吴宇航
    #                     d = d * suyinshu[i]#本作品作者吴宇航
    #                 else:#本作品作者吴宇航
    #                     zuida = suyinshu[i] * d#本作品作者吴宇航
    #             if zuida == 0:#本作品作者吴宇航
    #                 zuida = 1#本作品作者吴宇航
    #         return zuida * (a / zuida) * (b / zuida)#本作品作者吴宇航
    #     def fenshuyunsuan(mode,a,b,c,d):#本作品作者吴宇航
    #         if mode == "1":#本作品作者吴宇航
    #             zuida = 0#本作品作者吴宇航
    #             suyinshu.clear()#本作品作者吴宇航
    #             if a % b == 0:#本作品作者吴宇航
    #                 zuida = b#本作品作者吴宇航
    #             elif b % a == 0:#本作品作者吴宇航
    #                 zuida = a#本作品作者吴宇航
    #             else:#本作品作者吴宇航
    #                 z = a#本作品作者吴宇航
    #                 e = b#本作品作者吴宇航
    #                 list3.clear()#本作品作者吴宇航
    #                 if z > e:#本作品作者吴宇航
    #                     if e % 2 == 0:#本作品作者吴宇航
    #                         o = e / 2#本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         o = (e - 1) / 2 #本作品作者吴宇航
    #                 else:#本作品作者吴宇航
    #                     if z % 2 == 0:#本作品作者吴宇航
    #                         o = z / 2#本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         o = (z - 1) / 2#本作品作者吴宇航
    #                 for i in range(2,int(o + 1)):#本作品作者吴宇航
    #                     if z % i == 0 and e % i == 0:#本作品作者吴宇航
    #                         if zhihe(i) == "N":#本作品作者吴宇航
    #                             suyinshu.append(i)#本作品作者吴宇航
    #                             if i != 1:    #本作品作者吴宇航
    #                                 list3.append(i)#本作品作者吴宇航
    #                             z = z / i#本作品作者吴宇航
    #                             e = e / i#本作品作者吴宇航
    #                 while True:#本作品作者吴宇航
    #                     if len(list3) == 0:#本作品作者吴宇航
    #                         break#本作品作者吴宇航
    #                     list3.clear()#本作品作者吴宇航
    #                     if z > e:#本作品作者吴宇航
    #                         if e % 2 == 0:#本作品作者吴宇航
    #                             o = e / 2#本作品作者吴宇航
    #                         else:#本作品作者吴宇航
    #                             o = (e - 1) / 2 #本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         if z % 2 == 0:#本作品作者吴宇航
    #                             o = z / 2#本作品作者吴宇航
    #                         else:#本作品作者吴宇航
    #                             o = (z - 1) / 2#本作品作者吴宇航
    #                     for i in range(2,int(o + 1)):#本作品作者吴宇航
    #                         if z % i == 0 and e % i == 0:#本作品作者吴宇航
    #                             if zhihe(i) == "N":#本作品作者吴宇航
    #                                 suyinshu.append(i)#本作品作者吴宇航
    #                                 list3.append(i)#本作品作者吴宇航
    #                                 z = z / i#本作品作者吴宇航
    #                                 e = e / i#本作品作者吴宇航
    #                 z = 1#本作品作者吴宇航
    #                 for i in range(len(suyinshu)):#本作品作者吴宇航
    #                     if i != len(suyinshu) - 1:#本作品作者吴宇航
    #                         d = d * suyinshu[i]#本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         zuida = suyinshu[i] * z#本作品作者吴宇航
    #                 if zuida == 0:#本作品作者吴宇航
    #                     zuida = 1#本作品作者吴宇航
    #             e = zuida * (a / zuida) * (b / zuida)#本作品作者吴宇航
    #             f = c * (b / zuida) + d * (a / zuida)#本作品作者吴宇航
    #             zuida = 0#本作品作者吴宇航
    #             suyinshu.clear()#本作品作者吴宇航
    #             if e % f == 0:#本作品作者吴宇航
    #                 zuida = f#本作品作者吴宇航
    #             elif f % e == 0:#本作品作者吴宇航
    #                 zuida = e#本作品作者吴宇航
    #             else:#本作品作者吴宇航
    #                 h = e#本作品作者吴宇航
    #                 i = f#本作品作者吴宇航
    #                 list3.clear()#本作品作者吴宇航
    #                 if i > h:#本作品作者吴宇航
    #                     if h % 2 == 0:#本作品作者吴宇航
    #                         o = h / 2#本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         o = (h - 1) / 2 #本作品作者吴宇航
    #                 else:#本作品作者吴宇航
    #                     if i % 2 == 0:#本作品作者吴宇航
    #                         o = i / 2#本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         o = (i - 1) / 2#本作品作者吴宇航
    #                 for j in range(1,int(o + 1)):#本作品作者吴宇航
    #                     if h % j == 0 and i % j == 0:#本作品作者吴宇航
    #                         if zhihe(j) == "N":#本作品作者吴宇航
    #                             suyinshu.append(j)#本作品作者吴宇航
    #                             if j != 1:#本作品作者吴宇航
    #                                 list3.append(j)#本作品作者吴宇航
    #                             h = h / j#本作品作者吴宇航
    #                             i = i / j#本作品作者吴宇航
    #                 while True:#本作品作者吴宇航
    #                     if len(list3) == 0:#本作品作者吴宇航
    #                         break#本作品作者吴宇航
    #                     list3.clear()#本作品作者吴宇航
    #                     if h > i:#本作品作者吴宇航
    #                         if e % 2 == 0:#本作品作者吴宇航
    #                             o = i / 2#本作品作者吴宇航
    #                         else:#本作品作者吴宇航
    #                             o = (i - 1) / 2 #本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         if d % 2 == 0:#本作品作者吴宇航
    #                             o = h / 2#本作品作者吴宇航
    #                         else:#本作品作者吴宇航
    #                             o = (h - 1) / 2#本作品作者吴宇航
    #                     for j in range(2,int(o + 1)):#本作品作者吴宇航
    #                         if h % j == 0 and i % j == 0:#本作品作者吴宇航
    #                             if zhihe(j) == "N":#本作品作者吴宇航
    #                                 suyinshu.append(j)#本作品作者吴宇航
    #                                 list3.append(j)#本作品作者吴宇航
    #                                 h = h / j#本作品作者吴宇航
    #                                 i = i / j#本作品作者吴宇航
    #                 i = 1#本作品作者吴宇航
    #                 for j in range(len(suyinshu)):#本作品作者吴宇航
    #                     if j != len(suyinshu) - 1:#本作品作者吴宇航
    #                         i = i * suyinshu[j]#本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         zuida = suyinshu[j] * i#本作品作者吴宇航
    #                 if zuida == 0:#本作品作者吴宇航
    #                     zuida = 1#本作品作者吴宇航
    #             return str(int(e / zuida)) + "分之" + str(int(f / zuida))#本作品作者吴宇航
    #         elif mode == "2":#本作品作者吴宇航
    #             nima = fenshudaxiao(a,b,c,d)#本作品作者吴宇航
    #             if nima == "=":#本作品作者吴宇航
    #                 return 0#本作品作者吴宇航
    #             else:#本作品作者吴宇航
    #                 zuida = 0#本作品作者吴宇航
    #                 suyinshu.clear()#本作品作者吴宇航
    #                 if a % b == 0:#本作品作者吴宇航
    #                     zuida = b#本作品作者吴宇航
    #                 elif b % a == 0:#本作品作者吴宇航
    #                     zuida = a#本作品作者吴宇航
    #                 else:#本作品作者吴宇航
    #                     z = a#本作品作者吴宇航
    #                     e = b#本作品作者吴宇航
    #                     list3.clear()#本作品作者吴宇航
    #                     if z > e:#本作品作者吴宇航
    #                         if e % 2 == 0:#本作品作者吴宇航
    #                             o = e / 2#本作品作者吴宇航
    #                         else:#本作品作者吴宇航
    #                             o = (e - 1) / 2 #本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         if z % 2 == 0:#本作品作者吴宇航
    #                             o = z / 2#本作品作者吴宇航
    #                         else:#本作品作者吴宇航
    #                             o = (z - 1) / 2#本作品作者吴宇航
    #                     for i in range(1,int(o + 1)):#本作品作者吴宇航
    #                         if z % i == 0 and e % i == 0:#本作品作者吴宇航
    #                             if zhihe(i) == "N":#本作品作者吴宇航
    #                                 suyinshu.append(i)#本作品作者吴宇航
    #                                 if i != 1:#本作品作者吴宇航
    #                                     list3.append(i)#本作品作者吴宇航
    #                                 z = z / i#本作品作者吴宇航
    #                                 e = e / i#本作品作者吴宇航
    #                     while True:#本作品作者吴宇航
    #                         if len(list3) == 0:#本作品作者吴宇航
    #                             break#本作品作者吴宇航
    #                         list3.clear()#本作品作者吴宇航
    #                         if z > e:#本作品作者吴宇航
    #                             if e % 2 == 0:#本作品作者吴宇航
    #                                 o = e / 2#本作品作者吴宇航
    #                             else:#本作品作者吴宇航
    #                                 o = (e - 1) / 2 #本作品作者吴宇航
    #                         else:#本作品作者吴宇航
    #                             if z % 2 == 0:#本作品作者吴宇航
    #                                 o = z / 2#本作品作者吴宇航
    #                             else:#本作品作者吴宇航
    #                                 o = (z - 1) / 2#本作品作者吴宇航
    #                         for i in range(2,int(o + 1)):#本作品作者吴宇航
    #                             if z % i == 0 and e % i == 0:#本作品作者吴宇航
    #                                 if zhihe(i) == "N":#本作品作者吴宇航
    #                                     suyinshu.append(i)#本作品作者吴宇航
    #                                     list3.append(i)#本作品作者吴宇航
    #                                     z = z / i#本作品作者吴宇航
    #                                     e = e / i#本作品作者吴宇航
    #                 z = 1#本作品作者吴宇航
    #                 for i in range(len(suyinshu)):#本作品作者吴宇航
    #                     if i != len(suyinshu) - 1:#本作品作者吴宇航
    #                         d = d * suyinshu[i]#本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         zuida = suyinshu[i] * z#本作品作者吴宇航
    #                 if zuida == 0:#本作品作者吴宇航
    #                     zuida = 1#本作品作者吴宇航
                    #本作品作者吴宇航
    #                 e = zuida * (a / zuida) * (b / zuida)#本作品作者吴宇航
    #                 f = c * (b / zuida) - d * (a / zuida)#本作品作者吴宇航
    #                 zuida = 0#本作品作者吴宇航
    #                 suyinshu.clear()#本作品作者吴宇航
    #                 if e % f == 0:#本作品作者吴宇航
    #                     zuida = f#本作品作者吴宇航
    #                 elif f % e == 0:#本作品作者吴宇航
    #                     zuida = e#本作品作者吴宇航
    #                 else:#本作品作者吴宇航
    #                     h = e#本作品作者吴宇航
    #                     i = f#本作品作者吴宇航
    #                     list3.clear()#本作品作者吴宇航
    #                     if i > h:#本作品作者吴宇航
    #                         if h % 2 == 0:#本作品作者吴宇航
    #                             o = h / 2#本作品作者吴宇航
    #                         else:#本作品作者吴宇航
    #                             o = (h - 1) / 2 #本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         if i % 2 == 0:#本作品作者吴宇航
    #                             o = i / 2#本作品作者吴宇航
    #                         else:#本作品作者吴宇航
    #                             o = (i - 1) / 2#本作品作者吴宇航
    #                     for j in range(1,int(o + 1)):#本作品作者吴宇航
    #                         if h % j == 0 and i % j == 0:#本作品作者吴宇航
    #                             if zhihe(j) == "N":#本作品作者吴宇航
    #                                 suyinshu.append(j)#本作品作者吴宇航
    #                                 if j != 1:#本作品作者吴宇航
    #                                     list3.append(j)#本作品作者吴宇航
    #                                 h = h / j#本作品作者吴宇航
    #                                 i = i / j#本作品作者吴宇航
    #                     while True:#本作品作者吴宇航
    #                         if len(list3) == 0:#本作品作者吴宇航
    #                             break#本作品作者吴宇航
    #                         list3.clear()#本作品作者吴宇航
    #                         if h > i:#本作品作者吴宇航
    #                             if e % 2 == 0:#本作品作者吴宇航
    #                                 o = i / 2#本作品作者吴宇航
    #                             else:#本作品作者吴宇航
    #                                 o = (i - 1) / 2 #本作品作者吴宇航
    #                         else:#本作品作者吴宇航
    #                             if d % 2 == 0:#本作品作者吴宇航
    #                                 o = h / 2#本作品作者吴宇航
    #                             else:#本作品作者吴宇航
    #                                 o = (h - 1) / 2#本作品作者吴宇航
    #                         for j in range(2,int(o + 1)):#本作品作者吴宇航
    #                             if h % j == 0 and i % j == 0:#本作品作者吴宇航
    #                                 if zhihe(j) == "N":#本作品作者吴宇航
    #                                     suyinshu.append(j)#本作品作者吴宇航
    #                                     list3.append(j)#本作品作者吴宇航
    #                                     h = h / j#本作品作者吴宇航
    #                                     i = i / j#本作品作者吴宇航
    #                     i = 1#本作品作者吴宇航
    #                     for j in range(len(suyinshu)):#本作品作者吴宇航
    #                         if j != len(suyinshu) - 1:#本作品作者吴宇航
    #                             i = i * suyinshu[j]#本作品作者吴宇航
    #                         else:#本作品作者吴宇航
    #                             zuida = suyinshu[j] * i#本作品作者吴宇航
    #                     if zuida == 0:#本作品作者吴宇航
    #                         zuida = 1#本作品作者吴宇航
    #                 return str(int(e / zuida)) + "分之" + str(int(f / zuida))#本作品作者吴宇航
    #         if mode == "3":#本作品作者吴宇航
    #             e = a * b#本作品作者吴宇航
    #             f = c * d#本作品作者吴宇航
    #             zuida = 0#本作品作者吴宇航
    #             suyinshu.clear()#本作品作者吴宇航
    #             if e % f == 0:#本作品作者吴宇航
    #                 zuida = f#本作品作者吴宇航
    #             elif f % e == 0:#本作品作者吴宇航
    #                 zuida = e#本作品作者吴宇航
    #             else:#本作品作者吴宇航
    #                 h = e#本作品作者吴宇航
    #                 i = f#本作品作者吴宇航
    #                 list3.clear()#本作品作者吴宇航
    #                 if i > h:#本作品作者吴宇航
    #                     if h % 2 == 0:#本作品作者吴宇航
    #                         o = h / 2#本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         o = (h - 1) / 2 #本作品作者吴宇航
    #                 else:#本作品作者吴宇航
    #                     if i % 2 == 0:#本作品作者吴宇航
    #                         o = i / 2#本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         o = (i - 1) / 2#本作品作者吴宇航
    #                 for j in range(1,int(o + 1)):#本作品作者吴宇航
    #                     if h % j == 0 and i % j == 0:#本作品作者吴宇航
    #                         if zhihe(j) == "N":#本作品作者吴宇航
    #                             suyinshu.append(j)#本作品作者吴宇航
    #                             if j != 1:#本作品作者吴宇航
    #                                 list3.append(j)#本作品作者吴宇航
    #                             h = h / j#本作品作者吴宇航
    #                             i = i / j#本作品作者吴宇航
    #                 while True:#本作品作者吴宇航
    #                     if len(list3) == 0:#本作品作者吴宇航
    #                         break#本作品作者吴宇航
    #                     list3.clear()#本作品作者吴宇航
    #                     if h > i:#本作品作者吴宇航
    #                         if e % 2 == 0:#本作品作者吴宇航
    #                             o = i / 2#本作品作者吴宇航
    #                         else:#本作品作者吴宇航
    #                             o = (i - 1) / 2 #本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         if d % 2 == 0:#本作品作者吴宇航
    #                             o = h / 2#本作品作者吴宇航
    #                         else:#本作品作者吴宇航
    #                             o = (h - 1) / 2#本作品作者吴宇航
    #                     for j in range(2,int(o + 1)):#本作品作者吴宇航
    #                         if h % j == 0 and i % j == 0:#本作品作者吴宇航
    #                             if zhihe(j) == "N":#本作品作者吴宇航
    #                                 suyinshu.append(j)#本作品作者吴宇航
    #                                 list3.append(j)#本作品作者吴宇航
    #                                 h = h / j#本作品作者吴宇航
    #                                 i = i / j#本作品作者吴宇航
    #                 i = 1#本作品作者吴宇航
    #                 for j in range(len(suyinshu)):#本作品作者吴宇航
    #                     if j != len(suyinshu) - 1:#本作品作者吴宇航
    #                         i = i * suyinshu[j]#本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         zuida = suyinshu[j] * i#本作品作者吴宇航
    #                 if zuida == 0:#本作品作者吴宇航
    #                     zuida = 1#本作品作者吴宇航
    #             return str(int(e / zuida)) + "分之" + str(int(f / zuida))#本作品作者吴宇航
    #         if mode == "4":#本作品作者吴宇航
    #             e = a * d#本作品作者吴宇航
    #             f = b * c#本作品作者吴宇航
    #             zuida = 0#本作品作者吴宇航
    #             suyinshu.clear()#本作品作者吴宇航
    #             if e % f == 0:#本作品作者吴宇航
    #                 zuida = f#本作品作者吴宇航
    #             elif f % e == 0:#本作品作者吴宇航
    #                 zuida = e#本作品作者吴宇航
    #             else:#本作品作者吴宇航
    #                 h = e#本作品作者吴宇航
    #                 i = f#本作品作者吴宇航
    #                 list3.clear()#本作品作者吴宇航
    #                 if i > h:#本作品作者吴宇航
    #                     if h % 2 == 0:#本作品作者吴宇航
    #                         o = h / 2#本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         o = (h - 1) / 2 #本作品作者吴宇航
    #                 else:#本作品作者吴宇航
    #                     if i % 2 == 0:#本作品作者吴宇航
    #                         o = i / 2#本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         o = (i - 1) / 2#本作品作者吴宇航
    #                 for j in range(1,int(o + 1)):#本作品作者吴宇航
    #                     if h % j == 0 and i % j == 0:#本作品作者吴宇航
    #                         if zhihe(j) == "N":#本作品作者吴宇航
    #                             suyinshu.append(j)#本作品作者吴宇航
    #                             if j != 1:#本作品作者吴宇航
    #                                 list3.append(j)#本作品作者吴宇航
    #                             h = h / j#本作品作者吴宇航
    #                             i = i / j#本作品作者吴宇航
    #                 while True:#本作品作者吴宇航
    #                     if len(list3) == 0:#本作品作者吴宇航
    #                         break#本作品作者吴宇航
    #                     list3.clear()#本作品作者吴宇航
    #                     if h > i:#本作品作者吴宇航
    #                         if e % 2 == 0:#本作品作者吴宇航
    #                             o = i / 2#本作品作者吴宇航
    #                         else:#本作品作者吴宇航
    #                             o = (i - 1) / 2 #本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         if d % 2 == 0:#本作品作者吴宇航
    #                             o = h / 2#本作品作者吴宇航
    #                         else:#本作品作者吴宇航
    #                             o = (h - 1) / 2#本作品作者吴宇航
    #                     for j in range(2,int(o + 1)):#本作品作者吴宇航
    #                         if h % j == 0 and i % j == 0:#本作品作者吴宇航
    #                             if zhihe(j) == "N":#本作品作者吴宇航
    #                                 suyinshu.append(j)#本作品作者吴宇航
    #                                 list3.append(j)#本作品作者吴宇航
    #                                 h = h / j#本作品作者吴宇航
    #                                 i = i / j#本作品作者吴宇航
    #                 i = 1#本作品作者吴宇航
    #                 for j in range(len(suyinshu)):#本作品作者吴宇航
    #                     if j != len(suyinshu) - 1:#本作品作者吴宇航
    #                         i = i * suyinshu[j]#本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         zuida = suyinshu[j] * i#本作品作者吴宇航
    #                 if zuida == 0:#本作品作者吴宇航
    #                     zuida = 1#本作品作者吴宇航
    #             return str(int(e / zuida)) + "分子" + str(int(f / zuida))#本作品作者吴宇航
    #     def fenshudagongyin(a,b,c,d):#本作品作者吴宇航
    #         zuida = 0#本作品作者吴宇航
    #         suyinshu.clear()#本作品作者吴宇航
    #         if a % b == 0:#本作品作者吴宇航
    #             zuida = b#本作品作者吴宇航
    #         elif b % a == 0:#本作品作者吴宇航
    #             zuida = a#本作品作者吴宇航
    #         else:#本作品作者吴宇航
    #             z = a#本作品作者吴宇航
    #             e = b#本作品作者吴宇航
    #             list3.clear()#本作品作者吴宇航
    #             if z > e:#本作品作者吴宇航
    #                 if e % 2 == 0:#本作品作者吴宇航
    #                     o = e / 2#本作品作者吴宇航
    #                 else:#本作品作者吴宇航
    #                     o = (e - 1) / 2 #本作品作者吴宇航
    #             else:#本作品作者吴宇航
    #                 if z % 2 == 0:#本作品作者吴宇航
    #                     o = z / 2#本作品作者吴宇航
    #                 else:#本作品作者吴宇航
    #                     o = (z - 1) / 2#本作品作者吴宇航
    #             for i in range(2,int(o + 1)):#本作品作者吴宇航
    #                 if z % i == 0 and e % i == 0:#本作品作者吴宇航
    #                     if zhihe(i) == "N":#本作品作者吴宇航
    #                         suyinshu.append(i)#本作品作者吴宇航
    #                         if i != 1:    #本作品作者吴宇航
    #                             list3.append(i)#本作品作者吴宇航
    #                         z = z / i#本作品作者吴宇航
    #                         e = e / i#本作品作者吴宇航
    #             while True:#本作品作者吴宇航
    #                 if len(list3) == 0:#本作品作者吴宇航
    #                     break#本作品作者吴宇航
    #                 list3.clear()#本作品作者吴宇航
    #                 if z > e:#本作品作者吴宇航
    #                     if e % 2 == 0:#本作品作者吴宇航
    #                         o = e / 2#本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         o = (e - 1) / 2 #本作品作者吴宇航
    #                 else:#本作品作者吴宇航
    #                     if z % 2 == 0:#本作品作者吴宇航
    #                         o = z / 2#本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         o = (z - 1) / 2#本作品作者吴宇航
    #                 for i in range(2,int(o + 1)):#本作品作者吴宇航
    #                     if z % i == 0 and e % i == 0:#本作品作者吴宇航
    #                         if zhihe(i) == "N":#本作品作者吴宇航
    #                             suyinshu.append(i)#本作品作者吴宇航
    #                             list3.append(i)#本作品作者吴宇航
    #                             z = z / i#本作品作者吴宇航
    #                             e = e / i#本作品作者吴宇航
    #         z = 1#本作品作者吴宇航
    #         for i in range(len(suyinshu)):#本作品作者吴宇航
    #             if i != len(suyinshu) - 1:#本作品作者吴宇航
    #                 d = d * suyinshu[i]#本作品作者吴宇航
    #             else:#本作品作者吴宇航
    #                 zuida = suyinshu[i] * z#本作品作者吴宇航
    #         if zuida == 0:#本作品作者吴宇航
    #             zuida = 1#本作品作者吴宇航
    #         a1 = a * (b / zuida)#本作品作者吴宇航
    #         b1 = a1#本作品作者吴宇航
    #         c = c * (b / zuida)#本作品作者吴宇航
    #         d = d * (a / zuida)#本作品作者吴宇航
    #         zuida = 0#本作品作者吴宇航
    #         suyinshu.clear()#本作品作者吴宇航
    #         if c % d == 0:#本作品作者吴宇航
    #             zuida = d#本作品作者吴宇航
    #         elif d % c == 0:#本作品作者吴宇航
    #             zuida = c#本作品作者吴宇航
    #         else:#本作品作者吴宇航
    #             h = c#本作品作者吴宇航
    #             i = d#本作品作者吴宇航
    #             list3.clear()#本作品作者吴宇航
    #             if h > i:#本作品作者吴宇航
    #                 if i % 2 == 0:#本作品作者吴宇航
    #                     o = i / 2#本作品作者吴宇航
    #                 else:#本作品作者吴宇航
    #                     o = (i - 1) / 2 #本作品作者吴宇航
    #             else:#本作品作者吴宇航
    #                 if h % 2 == 0:#本作品作者吴宇航
    #                     o = h / 2#本作品作者吴宇航
    #                 else:#本作品作者吴宇航
    #                     o = (h - 1) / 2#本作品作者吴宇航
    #             for j in range(1,int(o + 1)):#本作品作者吴宇航
    #                 if h % j == 0 and i % j == 0:#本作品作者吴宇航
    #                     if zhihe(j) == "N":#本作品作者吴宇航
    #                         suyinshu.append(j)#本作品作者吴宇航
    #                         if j != 1:#本作品作者吴宇航
    #                             list3.append(j)#本作品作者吴宇航
    #                         h = h / j#本作品作者吴宇航
    #                         i = i / j#本作品作者吴宇航
    #             while True:#本作品作者吴宇航
    #                 if len(list3) == 0:#本作品作者吴宇航
    #                     break#本作品作者吴宇航
    #                 list3.clear()#本作品作者吴宇航
    #                 if h > i:#本作品作者吴宇航
    #                     if i % 2 == 0:#本作品作者吴宇航
    #                         o = i / 2#本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         o = (i - 1) / 2 #本作品作者吴宇航
    #                 else:#本作品作者吴宇航
    #                     if h % 2 == 0:#本作品作者吴宇航
    #                         o = h / 2#本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         o = (h - 1) / 2#本作品作者吴宇航
    #                 for j in range(2,int(o + 1)):#本作品作者吴宇航
    #                     if h % j == 0 and i % j == 0:#本作品作者吴宇航
    #                         if zhihe(j) == "N":#本作品作者吴宇航
    #                             suyinshu.append(j)#本作品作者吴宇航
    #                             list3.append(j)#本作品作者吴宇航
    #                             h = h / j#本作品作者吴宇航
    #                             i = i / j#本作品作者吴宇航
    #             z = 1#本作品作者吴宇航
    #             for j in range(len(suyinshu)):#本作品作者吴宇航
    #                 if j != len(suyinshu) - 1:#本作品作者吴宇航
    #                     z = z * suyinshu[j]#本作品作者吴宇航
    #                 else:#本作品作者吴宇航
    #                     zuida = suyinshu[j] * z#本作品作者吴宇航
    #             if zuida == 0:#本作品作者吴宇航
    #                 zuida = 1#本作品作者吴宇航
    #         b = zuida#本作品作者吴宇航
    #         zuida = 0#本作品作者吴宇航
    #         suyinshu.clear()#本作品作者吴宇航
    #         if a1 % b == 0:#本作品作者吴宇航
    #             zuida = b#本作品作者吴宇航
    #         elif b % a1 == 0:#本作品作者吴宇航
    #             zuida = a1#本作品作者吴宇航
    #         else:#本作品作者吴宇航
    #             d = a1#本作品作者吴宇航
    #             e = b#本作品作者吴宇航
    #             list3.clear()#本作品作者吴宇航
    #             if d > e:#本作品作者吴宇航
    #                 if e % 2 == 0:#本作品作者吴宇航
    #                     o = e / 2#本作品作者吴宇航
    #                 else:#本作品作者吴宇航
    #                     o = (e - 1) / 2 #本作品作者吴宇航
    #             else:#本作品作者吴宇航
    #                 if d % 2 == 0:#本作品作者吴宇航
    #                     o = d / 2#本作品作者吴宇航
    #                 else:#本作品作者吴宇航
    #                     o = (d - 1) / 2#本作品作者吴宇航
    #             for i in range(1,int(o + 1)):#本作品作者吴宇航
    #                 if d % i == 0 and e % i == 0:#本作品作者吴宇航
    #                     if zhihe(i) == "N":#本作品作者吴宇航
    #                         suyinshu.append(i)#本作品作者吴宇航
    #                         if i != 1:#本作品作者吴宇航
    #                             list3.append(i)#本作品作者吴宇航
    #                         d = d / i#本作品作者吴宇航
    #                         e = e / i#本作品作者吴宇航
    #             while True:#本作品作者吴宇航
    #                 if len(list3) == 0:#本作品作者吴宇航
    #                     break#本作品作者吴宇航
    #                 list3.clear()#本作品作者吴宇航
    #                 if d > e:#本作品作者吴宇航
    #                     if e % 2 == 0:#本作品作者吴宇航
    #                         o = e / 2#本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         o = (e - 1) / 2 #本作品作者吴宇航
    #                 else:#本作品作者吴宇航
    #                     if d % 2 == 0:#本作品作者吴宇航
    #                         o = d / 2#本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         o = (d - 1) / 2#本作品作者吴宇航
    #                 for i in range(2,int(o + 1)):#本作品作者吴宇航
    #                     if d % i == 0 and e % i == 0:#本作品作者吴宇航
    #                         if zhihe(i) == "N":#本作品作者吴宇航
    #                             suyinshu.append(i)#本作品作者吴宇航
    #                             list3.append(i)#本作品作者吴宇航
    #                             d = d / i#本作品作者吴宇航
    #                             e = e / i#本作品作者吴宇航
    #             d = 1#本作品作者吴宇航
    #             for i in range(len(suyinshu)):#本作品作者吴宇航
    #                 if i != len(suyinshu) - 1:#本作品作者吴宇航
    #                     d = d * suyinshu[i]#本作品作者吴宇航
    #                 else:#本作品作者吴宇航
    #                     zuida = suyinshu[i] * d#本作品作者吴宇航
    #             if zuida == 0:#本作品作者吴宇航
    #                 zuida = 1#本作品作者吴宇航
    #         return str(a1 // zuida) + "分之" + str(b // zuida)#本作品作者吴宇航
    #     def pingmianjihe(mode,a,b,c):#本作品作者吴宇航
    #         if mode == "等边三角形":#本作品作者吴宇航
    #             return sqrt(3) / 4 * a ** 2#本作品作者吴宇航
    #         if mode == "梯形":#本作品作者吴宇航
    #             return (a + b) * c / 2#本作品作者吴宇航
    #         if mode == "三角形":#本作品作者吴宇航
    #             return a * b / 2#本作品作者吴宇航
    #         if mode == "圆形面积":#本作品作者吴宇航
    #             return a ** 2 * 3.14#本作品作者吴宇航
    #         if mode == "圆形周长":#本作品作者吴宇航
    #             return a * 2 * 3.14#本作品作者吴宇航
    #         if mode == "扇形面积":#本作品作者吴宇航
    #             return a ** 2 * 3.14 / 360 * b#本作品作者吴宇航
    #         if mode == "扇形周长":#本作品作者吴宇航
    #             return 2 * a + a * 2 * 3.14 / 360 * b#本作品作者吴宇航
    #         if mode == "长方形":#本作品作者吴宇航
    #             return a * b#本作品作者吴宇航
    #     def izhihe1():#本作品作者吴宇航
    #         global izhihewin#本作品作者吴宇航
    #         window.destroy()#本作品作者吴宇航
    #         izhihewin = Tk()#本作品作者吴宇航
    #         izhihewin.title("质数合数判断")#本作品作者吴宇航
    #         izhihewin.geometry("400x300")#本作品作者吴宇航
    #         wo = Label(izhihewin,text = "请输入要计算的数",width = 15)#本作品作者吴宇航
    #         wo.pack(side = TOP)#本作品作者吴宇航
    #         var1 = Entry(izhihewin)#本作品作者吴宇航
    #         var1.pack(side = TOP,expand = True)#本作品作者吴宇航
    #         def izhihe2():#本作品作者吴宇航
    #             if "妈" in var1.get():#本作品作者吴宇航
    #                 messagebox.showwarning("","我不是你妈，我是你爹！")#本作品作者吴宇航
    #             else:#本作品作者吴宇航
    #                 try:#本作品作者吴宇航
    #                     if "妈" in var1.get():#本作品作者吴宇航
    #                         messagebox.showwarning("","我不是你妈，我是你爹！")#本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         jieguo1 = zhihe(int(var1.get()))#本作品作者吴宇航
    #                         if jieguo1 == "既不是素数也不是合数":#本作品作者吴宇航
    #                             jiegu1 = "既不是素数也不是合数"#本作品作者吴宇航
    #                         elif jieguo1 == "N":#本作品作者吴宇航
    #                             jieguo1 = "是质数"#本作品作者吴宇航
    #                         else:#本作品作者吴宇航
    #                             jieguo1 = "是合数，因数：" + str(jieguo1)#本作品作者吴宇航
    #                     messagebox.showwarning("",jieguo1)#本作品作者吴宇航
    #                 except:#本作品作者吴宇航
    #                     messagebox.showwarning("","请不要乱输")#本作品作者吴宇航
    #         def sbsb1():#本作品作者吴宇航
    #             izhihewin.destroy()#本作品作者吴宇航
    #             main()#本作品作者吴宇航
    #         izhihewin.protocol("WM_DELETE_WINDOW",sbsb1)#本作品作者吴宇航
    #         Button(izhihewin,text = "计算",command = izhihe2).pack(fill = BOTH,side = TOP,expand = True)#本作品作者吴宇航
    #         izhihewin.mainloop()#本作品作者吴宇航
#本作品作者吴宇航
    #     def izuixiao1():#本作品作者吴宇航
    #         global izuixiaowin#本作品作者吴宇航
    #         window.destroy()#本作品作者吴宇航
    #         izuixiaowin = Tk()#本作品作者吴宇航
    #         izuixiaowin.title("最小公倍数")#本作品作者吴宇航
    #         izuixiaowin.geometry("400x300")#本作品作者吴宇航
    #         Label(izuixiaowin,text = "在此输入第一个数").pack(side = TOP,expand = True)#本作品作者吴宇航
    #         var1 = Entry(izuixiaowin)#本作品作者吴宇航
    #         var1.pack(side = TOP,expand = True)#本作品作者吴宇航
    #         Label(izuixiaowin,text = "在此输入第二个数").pack(side = TOP,expand = True)#本作品作者吴宇航
    #         var2 = Entry(izuixiaowin)#本作品作者吴宇航
    #         var2.pack(side = TOP,expand = True)#本作品作者吴宇航
    #         def izuixiao2():#本作品作者吴宇航
    #             try:#本作品作者吴宇航
    #                 jieguo1 = "最小公倍数是" + str(int(zuixiao(int(var1.get()),int(var2.get()))))#本作品作者吴宇航
    #                 messagebox.showwarning("",jieguo1)#本作品作者吴宇航
    #             except:#本作品作者吴宇航
    #                 messagebox.showwarning("","请不要乱输")#本作品作者吴宇航
    #         Button(izuixiaowin,text = "计算",command = izuixiao2).pack(fill = BOTH,side = BOTTOM,expand = True)#本作品作者吴宇航
    #         def sbsb2():#本作品作者吴宇航
    #             izuixiaowin.destroy()#本作品作者吴宇航
    #             main()#本作品作者吴宇航
    #         izuixiaowin.protocol("WM_DELETE_WINDOW",sbsb2)#本作品作者吴宇航
    #         izuixiaowin.mainloop()#本作品作者吴宇航
    #     def izuida1():#本作品作者吴宇航
    #         global izuidawin#本作品作者吴宇航
    #         window.destroy()#本作品作者吴宇航
    #         izuidawin = Tk()#本作品作者吴宇航
    #         izuidawin.title("最大公因数")#本作品作者吴宇航
    #         izuidawin.geometry("400x300")#本作品作者吴宇航
    #         Label(izuidawin,text = "在此输入第一个数").pack(side = TOP,expand = True)#本作品作者吴宇航
    #         var1 = Entry(izuidawin)#本作品作者吴宇航
    #         var1.pack(side = TOP,expand = True)#本作品作者吴宇航
    #         Label(izuidawin,text = "在此输入第二个数").pack(side = TOP,expand = True)#本作品作者吴宇航
    #         var2 = Entry(izuidawin)#本作品作者吴宇航
    #         var2.pack(side = TOP,expand = True)#本作品作者吴宇航
    #         def izuida2():#本作品作者吴宇航
    #             try:#本作品作者吴宇航
    #                 jieguo1 = "最大公因数是" + str(common_factor(int(var1.get()),int(var2.get())))#本作品作者吴宇航
    #                 messagebox.showwarning("",jieguo1)#本作品作者吴宇航
    #             except:#本作品作者吴宇航
    #                 messagebox.showwarning("","请不要乱输")#本作品作者吴宇航
    #         Button(izuidawin,text = "计算",command = izuida2).pack(fill = BOTH,side = BOTTOM,expand = True)#本作品作者吴宇航
    #         def sbsb3():#本作品作者吴宇航
    #             izuidawin.destroy()#本作品作者吴宇航
    #             main()#本作品作者吴宇航
    #         izuidawin.protocol("WM_DELETE_WINDOW",sbsb3)#本作品作者吴宇航
    #         izuidawin.mainloop()#本作品作者吴宇航
    #     def fenshu1():#本作品作者吴宇航
    #         chooseuser = buttonbox(msg = "你要使用哪种运算？",title = "",choices = ["加法","减法","乘法","除法"])#本作品作者吴宇航
    #         window.destroy()#本作品作者吴宇航
    #         if chooseuser == "加法":#本作品作者吴宇航
    #             global ijiafawin#本作品作者吴宇航
    #             ijiafawin = Tk()#本作品作者吴宇航
    #             ijiafawin.title("分数加法")#本作品作者吴宇航
    #             ijiafawin.geometry("400x300")#本作品作者吴宇航
    #             Label(ijiafawin,text = "在此输入第一个分数的分子").pack(expand = True)#本作品作者吴宇航
    #             var1 = Entry(ijiafawin)#本作品作者吴宇航
    #             var1.pack(expand = True)#本作品作者吴宇航
    #             Label(ijiafawin,text = "在此输入第一个分数的分母").pack(expand = True)#本作品作者吴宇航
    #             var2 = Entry(ijiafawin)#本作品作者吴宇航
    #             var2.pack(expand = True)#本作品作者吴宇航
    #             Label(ijiafawin,text = "在此输入第二个分数的分子").pack(expand = True)#本作品作者吴宇航
    #             var3 = Entry(ijiafawin)#本作品作者吴宇航
    #             var3.pack(expand = True)#本作品作者吴宇航
    #             Label(ijiafawin,text = "在此输入第二个分数的分母").pack(expand = True)#本作品作者吴宇航
    #             var4 = Entry(ijiafawin)#本作品作者吴宇航
    #             var4.pack(expand = True)#本作品作者吴宇航
    #             def ijiafa():#本作品作者吴宇航
    #                 try:#本作品作者吴宇航
    #                     jieguo1 = fenshuyunsuan("1",int(var2.get()),int(var4.get()),int(var1.get()),int(var3.get()))#本作品作者吴宇航
    #                     jieguo1 = "运算结果是" + str(jieguo1)#本作品作者吴宇航
    #                     messagebox.showwarning("",jieguo1)#本作品作者吴宇航
    #                 except:#本作品作者吴宇航
    #                     messagebox.showwarning("","请不要乱输")#本作品作者吴宇航
    #             Button(ijiafawin,text = "计算",command = ijiafa).pack(fill = BOTH,side = BOTTOM,expand = True)#本作品作者吴宇航
    #             def sbsb4():#本作品作者吴宇航
    #                 ijiafawin.destroy()#本作品作者吴宇航
    #                 main()#本作品作者吴宇航
    #             ijiafawin.protocol("WM_DELETE_WINDOW",sbsb4)#本作品作者吴宇航
    #             ijiafawin.mainloop()#本作品作者吴宇航
    #         elif chooseuser == "减法":#本作品作者吴宇航
    #             global ijianfawin#本作品作者吴宇航
    #             ijianfawin = Tk()#本作品作者吴宇航
    #             ijianfawin.title("分数减法")#本作品作者吴宇航
    #             ijianfawin.geometry("400x300")#本作品作者吴宇航
    #             Label(ijianfawin,text = "在此输入被减数的分子").pack(expand = True)#本作品作者吴宇航
    #             var1 = Entry(ijianfawin)#本作品作者吴宇航
    #             var1.pack(expand = True)#本作品作者吴宇航
    #             Label(ijianfawin,text = "在此输入被减数的分母").pack(expand = True)#本作品作者吴宇航
    #             var2 = Entry(ijianfawin)#本作品作者吴宇航
    #             var2.pack(expand = True)#本作品作者吴宇航
    #             Label(ijianfawin,text = "在此输入减数的分子").pack(expand = True)#本作品作者吴宇航
    #             var3 = Entry(ijianfawin)#本作品作者吴宇航
    #             var3.pack(expand = True)#本作品作者吴宇航
    #             Label(ijianfawin,text = "在此输入减数的分母").pack(expand = True)#本作品作者吴宇航
    #             var4 = Entry(ijianfawin)#本作品作者吴宇航
    #             var4.pack(expand = True)#本作品作者吴宇航
    #             def ijianfa():#本作品作者吴宇航
    #                 try:#本作品作者吴宇航
    #                     jieguo1 = fenshuyunsuan("2",int(var2.get()),int(var4.get()),int(var1.get()),int(var3.get()))#本作品作者吴宇航
    #                     jieguo1 = "运算结果是" + str(jieguo1)#本作品作者吴宇航
    #                     messagebox.showwarning("",jieguo1)#本作品作者吴宇航
    #                 except:#本作品作者吴宇航
    #                     messagebox.showwarning("","请不要乱输")#本作品作者吴宇航
    #             Button(ijianfawin,text = "计算",command = ijianfa).pack(fill = BOTH,side = BOTTOM,expand = True)#本作品作者吴宇航
    #             def sbsb5():#本作品作者吴宇航
    #                 ijianfawin.destroy()#本作品作者吴宇航
    #                 main()#本作品作者吴宇航
    #             ijianfawin.protocol("WM_DELETE_WINDOW",sbsb5)#本作品作者吴宇航
    #             ijianfawin.mainloop()#本作品作者吴宇航
    #         elif chooseuser == "乘法":#本作品作者吴宇航
    #             global ichengfawin#本作品作者吴宇航
    #             ichengfawin = Tk()#本作品作者吴宇航
    #             ichengfawin.title("分数乘法")#本作品作者吴宇航
    #             ichengfawin.geometry("400x300")#本作品作者吴宇航
    #             Label(ichengfawin,text = "在此输入第一个分数的分子").pack(expand = True)#本作品作者吴宇航
    #             var1 = Entry(ichengfawin)#本作品作者吴宇航
    #             var1.pack(expand = True)#本作品作者吴宇航
    #             Label(ichengfawin,text = "在此输入第一个分数的分母").pack(expand = True)#本作品作者吴宇航
    #             var2 = Entry(ichengfawin)#本作品作者吴宇航
    #             var2.pack(expand = True)#本作品作者吴宇航
    #             Label(ichengfawin,text = "在此输入第二个分数的分子").pack(expand = True)#本作品作者吴宇航
    #             var3 = Entry(ichengfawin)#本作品作者吴宇航
    #             var3.pack(expand = True)#本作品作者吴宇航
    #             Label(ichengfawin,text = "在此输入第二个分数的分母").pack(expand = True)#本作品作者吴宇航
    #             var4 = Entry(ichengfawin)#本作品作者吴宇航
    #             var4.pack(expand = True)#本作品作者吴宇航
    #             def ichengfa():#本作品作者吴宇航
    #                 try:#本作品作者吴宇航
    #                     jieguo1 = fenshuyunsuan("3",int(var2.get()),int(var4.get()),int(var1.get()),int(var3.get()))#本作品作者吴宇航
    #                     jieguo1 = "运算结果是" + str(jieguo1)#本作品作者吴宇航
    #                     messagebox.showwarning("",jieguo1)#本作品作者吴宇航
    #                 except:#本作品作者吴宇航
    #                     messagebox.showwarning("","请不要乱输")#本作品作者吴宇航
    #             Button(ichengfawin,text = "计算",command = ichengfa).pack(fill = BOTH,side = BOTTOM,expand = True)#本作品作者吴宇航
    #             def sbsb6():#本作品作者吴宇航
    #                 ichengfawin.destroy()#本作品作者吴宇航
    #                 main()#本作品作者吴宇航
    #             ichengfawin.protocol("WM_DELETE_WINDOW",sbsb6)#本作品作者吴宇航
    #             ichengfawin.mainloop()#本作品作者吴宇航
    #         elif chooseuser == "除法":#本作品作者吴宇航
    #             global ichufawin#本作品作者吴宇航
    #             ichufawin = Tk()#本作品作者吴宇航
    #             ichufawin.title("分数除法")#本作品作者吴宇航
    #             ichufawin.geometry("400x300")#本作品作者吴宇航
    #             Label(ichufawin,text = "在此输入被除数的分子").pack(expand = True)#本作品作者吴宇航
    #             var1 = Entry(ichufawin)#本作品作者吴宇航
    #             var1.pack(expand = True)#本作品作者吴宇航
    #             Label(ichufawin,text = "在此输入被除数的分母").pack(expand = True)#本作品作者吴宇航
    #             var2 = Entry(ichufawin)#本作品作者吴宇航
    #             var2.pack(expand = True)#本作品作者吴宇航
    #             Label(ichufawin,text = "在此输入除数的分子").pack(expand = True)#本作品作者吴宇航
    #             var3 = Entry(ichufawin)#本作品作者吴宇航
    #             var3.pack(expand = True)#本作品作者吴宇航
    #             Label(ichufawin,text = "在此输入除数的分母").pack(expand = True)#本作品作者吴宇航
    #             var4 = Entry(ichufawin)#本作品作者吴宇航
    #             var4.pack(expand = True)#本作品作者吴宇航
    #             def ichufa():#本作品作者吴宇航
    #                 try:#本作品作者吴宇航
    #                     jieguo1 = fenshuyunsuan("4",int(var2.get()),int(var4.get()),int(var1.get()),int(var3.get()))#本作品作者吴宇航
    #                     jieguo1 = "运算结果是" + jieguo1#本作品作者吴宇航
    #                     messagebox.showwarning("",jieguo1)#本作品作者吴宇航
    #                 except:#本作品作者吴宇航
    #                     messagebox.showwarning("","请不要乱输")#本作品作者吴宇航
    #             Button(ichufawin,text = "计算",command = ichufa).pack(fill = BOTH,side = BOTTOM,expand = True)#本作品作者吴宇航
    #             def sbsb7():#本作品作者吴宇航
    #                 ichufawin.destroy()#本作品作者吴宇航
    #                 main()#本作品作者吴宇航
    #             ichufawin.protocol("WM_DELETE_WINDOW",sbsb7)#本作品作者吴宇航
    #             ichufawin.mainloop()#本作品作者吴宇航
    #         else:#本作品作者吴宇航
    #             main()#本作品作者吴宇航
    #     def fenshu():#本作品作者吴宇航
    #         global ifenshuwin#本作品作者吴宇航
    #         window.destroy()#本作品作者吴宇航
    #         ifenshuwin = Tk()#本作品作者吴宇航
    #         ifenshuwin.title("分数比较大小")#本作品作者吴宇航
    #         ifenshuwin.geometry("400x300")#本作品作者吴宇航
    #         Label(ifenshuwin,text = "请输入第一个分数的分子").pack(expand = True)#本作品作者吴宇航
    #         var1 = Entry(ifenshuwin)#本作品作者吴宇航
    #         var1.pack()#本作品作者吴宇航
    #         Label(ifenshuwin,text = "请输入第一个分数的分母").pack(expand = True)#本作品作者吴宇航
    #         var2 = Entry(ifenshuwin)#本作品作者吴宇航
    #         var2.pack()#本作品作者吴宇航
    #         Label(ifenshuwin,text = "请输入第二个分数的分子").pack(expand = True)#本作品作者吴宇航
    #         var3 = Entry(ifenshuwin)#本作品作者吴宇航
    #         var3.pack()#本作品作者吴宇航
    #         Label(ifenshuwin,text = "请输入第二个分数的分母").pack(expand = True)#本作品作者吴宇航
    #         var4 = Entry(ifenshuwin)#本作品作者吴宇航
    #         var4.pack()#本作品作者吴宇航
    #         def bijiao():#本作品作者吴宇航
    #             try:#本作品作者吴宇航
    #                 jieguo1 = fenshudaxiao(int(var2.get()),int(var4.get()),int(var1.get()),int(var3.get()))#本作品作者吴宇航
    #                 if jieguo1 == 1:#本作品作者吴宇航
    #                     messagebox.showwarning("",var2.get() + "分之" + var1.get() + "大")#本作品作者吴宇航
    #                 elif jieguo1 == 2:#本作品作者吴宇航
    #                     messagebox.showwarning("",var4.get() + "分之" + var3.get() + "大")#本作品作者吴宇航
    #                 else:#本作品作者吴宇航
    #                     messagebox.showwarning("两个数一样大")#本作品作者吴宇航
    #             except:#本作品作者吴宇航
    #                 messagebox.showwarning("请不要乱输")#本作品作者吴宇航
    #         Button(ifenshuwin,text = "计算",command = bijiao).pack(fill = BOTH,side = BOTTOM)#本作品作者吴宇航
    #         def sbsb8():#本作品作者吴宇航
    #             ifenshuwin.destroy()#本作品作者吴宇航
    #             main()#本作品作者吴宇航
    #         ifenshuwin.protocol("WM_DELETE_WINDOW",sbsb8)#本作品作者吴宇航
    #         ifenshuwin.mainloop()#本作品作者吴宇航
    #     def ifeibonaqi():#本作品作者吴宇航
    #         chooseuser = buttonbox(msg = "你要用哪个功能",title = "",choices = ["求某一项","求某个数是第几项"])#本作品作者吴宇航
    #         window.destroy()#本作品作者吴宇航
    #         if chooseuser == "求某一项":#本作品作者吴宇航
    #             global feibowin1#本作品作者吴宇航
    #             feibowin1 = Tk()#本作品作者吴宇航
    #             feibowin1.geometry("400x300")#本作品作者吴宇航
    #             feibowin1.title("求斐波那契数列的某一项")#本作品作者吴宇航
    #             Label(feibowin1,text = "你想求第").pack(fill = BOTH,side = TOP,expand = True)#本作品作者吴宇航
    #             var1 = Entry(feibowin1)#本作品作者吴宇航
    #             var1.pack(fill = BOTH,side = TOP,expand = True)#本作品作者吴宇航
    #             Label(feibowin1,text = "项").pack(fill = BOTH,side = TOP,expand = True)#本作品作者吴宇航
    #             def ifeibo1():#本作品作者吴宇航
    #                 try:#本作品作者吴宇航
    #                     messagebox.showwarning("","第" + var1.get() + "项是" + str(feibonaqi("1",int(var1.get()))))#本作品作者吴宇航
    #                 except:#本作品作者吴宇航
    #                     messagebox.showwarning("","请不要乱输")#本作品作者吴宇航
    #             Button(feibowin1,text = "计算",command = ifeibo1).pack(fill = BOTH,side = BOTTOM)#本作品作者吴宇航
    #             def sbsb9():#本作品作者吴宇航
    #                 feibowin1.destroy()#本作品作者吴宇航
    #             feibowin1.protocol("WM_DELETE_WINDOW",sbsb9)#本作品作者吴宇航
    #             feibowin1.mainloop()#本作品作者吴宇航
    #         elif chooseuser == "求某个数是第几项":#本作品作者吴宇航
    #             global feibowin2#本作品作者吴宇航
    #             feibowin2 = Tk()#本作品作者吴宇航
    #             feibowin2.geometry("400x300")#本作品作者吴宇航
    #             feibowin2.title("求某个数在数列中的位置")#本作品作者吴宇航
    #             Label(feibowin2,text = "你想求").pack(side = TOP)#本作品作者吴宇航
    #             var1 = Entry(feibowin2)#本作品作者吴宇航
    #             var1.pack(side = TOP,expand = True)#本作品作者吴宇航
    #             Label(feibowin2,text = "在斐波那契数列中的位置").pack(side = TOP)#本作品作者吴宇航
    #             def ifeibo2():#本作品作者吴宇航
    #                 try:#本作品作者吴宇航
    #                     jieguo1 = feibonaqi("2",int(var1.get()))#本作品作者吴宇航
    #                     if jieguo1 == "N":#本作品作者吴宇航
    #                         messagebox.showwarning("","这个数不在斐波那契数列中！")#本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         messagebox.showwarning("",var1.get() + "是第" + str(jieguo1) + "项")#本作品作者吴宇航
    #                 except:#本作品作者吴宇航
    #                     messagebox.showwarning("","请不要乱输")#本作品作者吴宇航
    #             Button(feibowin2,text = "计算",command = ifeibo2).pack(fill = BOTH,side = BOTTOM)#本作品作者吴宇航
    #             def sbsb10():#本作品作者吴宇航
    #                 feibowin2.destroy()#本作品作者吴宇航
    #                 main()#本作品作者吴宇航
    #             feibowin2.protocol("WM_DELETE_WINDOW",sbsb10)#本作品作者吴宇航
    #             feibowin2.mainloop()#本作品作者吴宇航
    #         else:#本作品作者吴宇航
    #             main()#本作品作者吴宇航
    #     def dengcha():#本作品作者吴宇航
    #         chooseuser = buttonbox(msg = "你要哪个功能？",title = "",choices = ["求某一项","求某个数的位置","求和"])#本作品作者吴宇航
    #         window.destroy()#本作品作者吴宇航
    #         if chooseuser == "求某一项":#本作品作者吴宇航
    #             global dengchawin1#本作品作者吴宇航
    #             dengchawin1 = Tk()#本作品作者吴宇航
    #             dengchawin1.title("求等差数列的某一项")#本作品作者吴宇航
    #             dengchawin1.geometry("400x300")#本作品作者吴宇航
    #             Label(dengchawin1,text = "在此输入首项").pack()#本作品作者吴宇航
    #             var1 = Entry(dengchawin1)#本作品作者吴宇航
    #             var1.pack()#本作品作者吴宇航
    #             Label(dengchawin1,text = "在此输入公差").pack()#本作品作者吴宇航
    #             var2 = Entry(dengchawin1)#本作品作者吴宇航
    #             var2.pack()#本作品作者吴宇航
    #             Label(dengchawin1,text = "你想求第几项？").pack()#本作品作者吴宇航
    #             var3 = Entry(dengchawin1)#本作品作者吴宇航
    #             var3.pack()#本作品作者吴宇航
    #             def idengcha1():#本作品作者吴宇航
    #                 try:#本作品作者吴宇航
    #                     messagebox.showwarning("","第" + var3.get() + "项是" + str(dengchashulie(1,int(var1.get()),int(var2.get()),int(var3.get()))))#本作品作者吴宇航
    #                 except:#本作品作者吴宇航
    #                     messagebox.showwarning("","请不要乱输")#本作品作者吴宇航
    #             Button(dengchawin1,text = "计算",command = idengcha1).pack(fill = BOTH,side = BOTTOM)#本作品作者吴宇航
    #             def sbsb11():#本作品作者吴宇航
    #                 dengchawin1.destroy()#本作品作者吴宇航
    #                 main()#本作品作者吴宇航
    #             dengchawin1.protocol("WM_DELETE_WINDOW",sbsb11)#本作品作者吴宇航
    #             dengchawin1.mainloop()#本作品作者吴宇航
    #         elif chooseuser == "求某个数的位置":#本作品作者吴宇航
    #             global dengchawin2#本作品作者吴宇航
    #             dengchawin2 = Tk()#本作品作者吴宇航
    #             dengchawin2.title("求某个数在等差数列的位置")#本作品作者吴宇航
    #             dengchawin2.geometry("400x300")#本作品作者吴宇航
    #             Label(dengchawin2,text = "请输入首项").pack()#本作品作者吴宇航
    #             var1 = Entry(dengchawin2)#本作品作者吴宇航
    #             var1.pack()#本作品作者吴宇航
    #             Label(dengchawin2,text = "请输入公差").pack()#本作品作者吴宇航
    #             var2 = Entry(dengchawin2)#本作品作者吴宇航
    #             var2.pack()#本作品作者吴宇航
    #             Label(dengchawin2,text = "你想求哪个数的位置？").pack()#本作品作者吴宇航
    #             var3 = Entry(dengchawin2)#本作品作者吴宇航
    #             var3.pack()#本作品作者吴宇航
    #             def idengcha2():#本作品作者吴宇航
    #                 try:#本作品作者吴宇航
    #                     jieguo1 = dengchashulie(2,int(var1.get()),int(var2.get()),int(var3.get()))#本作品作者吴宇航
    #                     if jieguo1 == "N":#本作品作者吴宇航
    #                         messagebox.showwarning("","这个数不在等差数列中！")#本作品作者吴宇航
    #                     else:#本作品作者吴宇航
    #                         messagebox.showwarning("",var3.get() + "是第" + str(jieguo1) + "项")#本作品作者吴宇航
    #                 except:#本作品作者吴宇航
    #                     messagebox.showwarning("","请不要乱输")#本作品作者吴宇航
    #             Button(dengchawin2,text = "计算",command = idengcha2).pack(fill = BOTH,side = BOTTOM)#本作品作者吴宇航
    #             def sbsb12():#本作品作者吴宇航
    #                 dengchawin2.destroy()#本作品作者吴宇航
    #                 main()#本作品作者吴宇航
    #             dengchawin2.protocol("WM_DELETE_WINDOW",sbsb12)#本作品作者吴宇航
    #             dengchawin2.mainloop()#本作品作者吴宇航
    #         elif chooseuser == "求和":#本作品作者吴宇航
    #             global dengchawin3#本作品作者吴宇航
    #             dengchawin3 = Tk()#本作品作者吴宇航
    #             dengchawin3.title("等差数列求和")#本作品作者吴宇航
    #             dengchawin3.geometry("400x300")#本作品作者吴宇航
    #             Label(dengchawin3,text = "请输入首项").pack()#本作品作者吴宇航
    #             var1 = Entry(dengchawin3)#本作品作者吴宇航
    #             var1.pack()#本作品作者吴宇航
    #             Label(dengchawin3,text = "请输入公差").pack()#本作品作者吴宇航
    #             var2 = Entry(dengchawin3)#本作品作者吴宇航
    #             var2.pack()#本作品作者吴宇航
    #             Label(dengchawin3,text = "请输入项数").pack()#本作品作者吴宇航
    #             var3 = Entry(dengchawin3)#本作品作者吴宇航
    #             var3.pack()#本作品作者吴宇航
    #             def idengcha3():#本作品作者吴宇航
    #                 try:#本作品作者吴宇航
    #                     jieguo1 = dengchashulie(3,int(var1.get()),int(var2.get()),int(var3.get()))#本作品作者吴宇航
    #                     messagebox.showwarning("","等差数列值和是" + str(jieguo1))#本作品作者吴宇航
    #                 except:#本作品作者吴宇航
    #                     messagebox.showwarning("","请不要乱输")#本作品作者吴宇航
    #             def sbsb13():#本作品作者吴宇航
    #                 dengchawin3.destroy()#本作品作者吴宇航
    #                 main()#本作品作者吴宇航
    #             dengchawin3.protocol("WM_DELETE_WINDOW",sbsb13)#本作品作者吴宇航
    #             Button(dengchawin3,text = "计算",command = idengcha3).pack(fill = BOTH,side = BOTTOM)        #本作品作者吴宇航
    #             dengchawin3.mainloop()#本作品作者吴宇航
    #         else:#本作品作者吴宇航
    #             main()#本作品作者吴宇航
    #     def size():#本作品作者吴宇航
    #         global sizewin#本作品作者吴宇航
    #         window.destroy()#本作品作者吴宇航
    #         sizewin = Tk()#本作品作者吴宇航
    #         sizewin.title("四则运算")#本作品作者吴宇航
    #         sizewin.geometry("400x300")#本作品作者吴宇航
    #         var1 = Entry(sizewin)#本作品作者吴宇航
    #         Label(sizewin,text = "在此输入算式").pack()#本作品作者吴宇航
    #         var1.pack()#本作品作者吴宇航
    #         def jj():#本作品作者吴宇航
    #             try:#本作品作者吴宇航
    #                 a = var1.get()#本作品作者吴宇航
    #                 if "^" in a:#本作品作者吴宇航
    #                     a = a.replace("^","**")#本作品作者吴宇航
    #                 messagebox.showwarning("","运算结果为" + str(eval(a)))#本作品作者吴宇航
    #             except:#本作品作者吴宇航
    #                 messagebox.showwarning("","请不要乱输")#本作品作者吴宇航
    #         def sbsb14():#本作品作者吴宇航
    #             sizewin.destroy()#本作品作者吴宇航
    #             main()#本作品作者吴宇航
    #         sizewin.protocol("WM_DELETE_WINDOW",sbsb14)#本作品作者吴宇航
    #         Button(sizewin,text = "计算",command = jj).pack(side = BOTTOM)#本作品作者吴宇航
    #         sizewin.mainloop()#本作品作者吴宇航
    #     afsd = {#本作品作者吴宇航
    #     "质数合数判断":izhihe1,#本作品作者吴宇航
    #     "最大公因数（整数）":izuida1,#本作品作者吴宇航
    #     "最小公倍数（整数）":izuixiao1,#本作品作者吴宇航
    #     "分数运算":fenshu1,#本作品作者吴宇航
    #     "分数比较大小":fenshu,#本作品作者吴宇航
    #     "斐波那契数列计算":ifeibonaqi,#本作品作者吴宇航
    #     "等差数列":dengcha,#本作品作者吴宇航
    #     "四则运算":size#本作品作者吴宇航
    #     }#本作品作者吴宇航
    #     def main():#本作品作者吴宇航
    #         global window#本作品作者吴宇航
    #         window = Tk()#本作品作者吴宇航
    #         window.title("数学作业神器")#本作品作者吴宇航
    #         window.geometry("400x300")#本作品作者吴宇航
    #         window.iconbitmap("金星.ico")#本作品作者吴宇航
    #         for k in afsd:#本作品作者吴宇航
    #             Button(window,text = k,command = afsd[k]).pack(fill = BOTH,side = TOP,expand = True)#本作品作者吴宇航
    #         def fanhui():#本作品作者吴宇航
    #             if messagebox.askokcancel("确定退出？","您确定要退出？（关闭主窗口后所有窗口将关闭）"):#本作品作者吴宇航
    #                 window.destroy()#本作品作者吴宇航
    #                 fasdasdf1()#本作品作者吴宇航
    #         window.protocol("WM_DELETE_WINDOW",fanhui)#本作品作者吴宇航
    #         window.mainloop()#本作品作者吴宇航
    #     main()#本作品作者吴宇航
    elif dakai == "huatu":#本作品作者吴宇航
        messagebox.showinfo("提示","该功能维护中，暂不开放")#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
        # def fasdasdf():#本作品作者吴宇航
        #     mainwin.destroy()#本作品作者吴宇航
        #     fasdasdf1()#本作品作者吴宇航
        # choose = buttonbox(msg = "你要使用哪种画图",title = "",choices = ["函数画图","折线统计图"])#本作品作者吴宇航
        # if choose == "折线统计图":#本作品作者吴宇航
        #     global s#本作品作者吴宇航
        #     mainwin = Tk()#本作品作者吴宇航
        #     mainwin.title("Night Star画图器")#本作品作者吴宇航
        #     mainwin.geometry("400x500")#本作品作者吴宇航
        #     mainwin.iconbitmap("金星.ico")#本作品作者吴宇航
        #     def lj(q):#本作品作者吴宇航
        #         mod = q % 10#本作品作者吴宇航
        #         if mod == 0:#本作品作者吴宇航
        #             return q#本作品作者吴宇航
        #         elif q > 0:#本作品作者吴宇航
        #             i = 1#本作品作者吴宇航
        #             while i * 10 < q:#本作品作者吴宇航
        #                 i += 1#本作品作者吴宇航
        #             return i * 10#本作品作者吴宇航
        #         else:#本作品作者吴宇航
        #             i = -1#本作品作者吴宇航
        #             while i * 10 > q:#本作品作者吴宇航
        #                 i -= 1#本作品作者吴宇航
        #             return (i + 1) * 10#本作品作者吴宇航
        #     def jl(q):#本作品作者吴宇航
        #         mod = q % 10#本作品作者吴宇航
        #         if mod == 0:#本作品作者吴宇航
        #             return q#本作品作者吴宇航
        #         elif q > 0:#本作品作者吴宇航
        #             i = 1#本作品作者吴宇航
        #             while i * 10 < q:#本作品作者吴宇航
        #                 i += 1#本作品作者吴宇航
        #             return (i - 1) * 10#本作品作者吴宇航
        #         else:#本作品作者吴宇航
        #             i = -1#本作品作者吴宇航
        #             while i * 10 > q:#本作品作者吴宇航
        #                 i -= 1#本作品作者吴宇航
        #             return i * 10#本作品作者吴宇航
        #     try:#本作品作者吴宇航
        #         sq = []#本作品作者吴宇航
        #         s = Label(mainwin,text = "在次输入第1个元素")#本作品作者吴宇航
        #         var = Entry(mainwin,widt = 20)#本作品作者吴宇航
        #         var.place(x = 150,y = 150,anchor = "center")#本作品作者吴宇航
        #         s.pack()#本作品作者吴宇航
        #         def a0458():#本作品作者吴宇航
        #             global s#本作品作者吴宇航
        #             sq.append(int(var.get()))#本作品作者吴宇航
        #             s.forget()#本作品作者吴宇航
        #             s = Label(mainwin,text = "在此输入第" + str(len(sq) + 1) + "个元素")#本作品作者吴宇航
        #             s.pack()#本作品作者吴宇航
        #         Button(mainwin,text = "添加",command = a0458).place(x = 300,y = 150,anchor = "center")#本作品作者吴宇航
        #         def hua():#本作品作者吴宇航
        #             plt.plot(sq)#本作品作者吴宇航
        #             plt.axis([0,len(sq) - 1,jl(min(sq)),lj(max(sq))])#本作品作者吴宇航
        #             plt.show()#本作品作者吴宇航
        #         Button(mainwin,text = "画图",command = hua).place(x = 200,y = 425,anchor = "center")#本作品作者吴宇航
        #         mainwin.protocol("WM_DELETE_WINDOW",fasdasdf)#本作品作者吴宇航
        #         mainwin.mainloop()#本作品作者吴宇航
        #     except:#本作品作者吴宇航
        #         messagebox.showerror("","matplotlib库未安装")#本作品作者吴宇航
        # elif choose == "函数画图":#本作品作者吴宇航
        #     mainwin = Tk()#本作品作者吴宇航
        #     mainwin.title("Night Star画图器")#本作品作者吴宇航
        #     mainwin.geometry("400x500")#本作品作者吴宇航
        #     mainwin.iconbitmap("金星.ico")#本作品作者吴宇航
        #     Label(mainwin,text = "y=").place(x = 125,y = 100,anchor = "center")#本作品作者吴宇航
        #     var = Entry(mainwin,width = 2)#本作品作者吴宇航
        #     var.place(x = 150,y = 100,anchor = "center")#本作品作者吴宇航
        #     Label(mainwin,text = "x²+").place(x = 175,y = 100,anchor = "center")#本作品作者吴宇航
        #     var2 = Entry(mainwin,width = 2)#本作品作者吴宇航
        #     var2.place(x = 200,y = 100,anchor = "center")#本作品作者吴宇航
        #     Label(mainwin,text = "x+").place(x = 225,y = 100,anchor = "center")#本作品作者吴宇航
        #     var3 = Entry(mainwin,width = 2)#本作品作者吴宇航
        #     var3.place(x = 250,y = 100,anchor = "center")#本作品作者吴宇航
        #     def hua():#本作品作者吴宇航
        #         x = np.arange(-10,11)#本作品作者吴宇航
        #         y = int(var.get()) * x ** 2 + int(var2.get()) * x + int(var3.get())#本作品作者吴宇航
        #         plt.plot(x,y)#本作品作者吴宇航
        #         plt.xlabel("x")#本作品作者吴宇航
        #         plt.ylabel("y")#本作品作者吴宇航
        #         plt.show()#本作品作者吴宇航
        #     Button(mainwin,text = "画图",command = hua).pack(side = BOTTOM)#本作品作者吴宇航
        #     mainwin.protocol("WM_DELETE_WINDOW",fasdasdf)#本作品作者吴宇航
        #     mainwin.mainloop()#本作品作者吴宇航
        # else:#本作品作者吴宇航
        #     fasdasdf1()#本作品作者吴宇航
    elif dakai == "qq":#本作品作者吴宇航
        app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.  #本作品作者吴宇航
        liaotianwin = wx.Frame(None, wx.ID_ANY, "聊天机器人") # A Frame is a top-level window.  #本作品作者吴宇航
        liaotianwin.Show(True)#本作品作者吴宇航
        global aba#本作品作者吴宇航
        var = wx.TextCtrl(liaotianwin,size = (200,20),pos = (100,15))#本作品作者吴宇航
        import json#本作品作者吴宇航
        import requests#本作品作者吴宇航
#本作品作者吴宇航
        api_url = "http://openapi.tuling123.com/openapi/api/v2"#本作品作者吴宇航
        def huifu(event):#本作品作者吴宇航
            global aba,first#本作品作者吴宇航
            try:#本作品作者吴宇航
                if first:#本作品作者吴宇航
                    wx.StaticText(liaotianwin, label='聊天机器人的回复',pos = (100,50))#本作品作者吴宇航
                    first = False#本作品作者吴宇航
            except:#本作品作者吴宇航
                wx.StaticText(liaotianwin, label='聊天机器人的回复',pos = (100,50))#本作品作者吴宇航
                first = False#本作品作者吴宇航
            data = {#本作品作者吴宇航
                "reqType": 0,#本作品作者吴宇航
                "perception":#本作品作者吴宇航
                {#本作品作者吴宇航
                    "inputText":#本作品作者吴宇航
                    {#本作品作者吴宇航
                        "text": var.GetValue()#本作品作者吴宇航
                    },#本作品作者吴宇航
                    # 可选参数#本作品作者吴宇航
                    # "inputImage": {#本作品作者吴宇航
                    #     "url": "imageUrl"#本作品作者吴宇航
                    # },#本作品作者吴宇航
                    # 可选参数#本作品作者吴宇航
                    # "selfInfo":#本作品作者吴宇航
                    # {#本作品作者吴宇航
                    #     "location":#本作品作者吴宇航
                    #     {#本作品作者吴宇航
                    #         "city": "上海",#本作品作者吴宇航
                    #         "province": "上海",#本作品作者吴宇航
                    #         "street": "文汇路"#本作品作者吴宇航
                    #     }#本作品作者吴宇航
                    #  }#本作品作者吴宇航
                },#本作品作者吴宇航
                "userInfo":#本作品作者吴宇航
                {#本作品作者吴宇航
                    "apiKey": "57e8a35bf9f349a1bb49f2da6d48d518",#本作品作者吴宇航
                    "userId": "586065"#本作品作者吴宇航
                }#本作品作者吴宇航
            }   #本作品作者吴宇航
            data = json.dumps(data).encode('utf8')#本作品作者吴宇航
            response_str = requests.post(api_url, data=data, headers={'content-type': 'application/json'})#本作品作者吴宇航
            response_dic = response_str.json()#本作品作者吴宇航
            # print('返回结果：' + response_str.text)#本作品作者吴宇航
            results_text = response_dic['results'][0]['values']['text']#本作品作者吴宇航
            try:#本作品作者吴宇航
                aba.forget()#本作品作者吴宇航
            except:#本作品作者吴宇航
                pass#本作品作者吴宇航
            aba = wx.StaticText(liaotianwin,label = results_text,pos = (100,50))#本作品作者吴宇航
            #本作品作者吴宇航
        btn = wx.Button(liaotianwin,label = "确定",pos = (300,10))#本作品作者吴宇航
        btn.Bind(wx.EVT_BUTTON, huifu)#本作品作者吴宇航
        app.MainLoop()#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
    elif dakai == "bmi":#本作品作者吴宇航
        bmi = Tk()#本作品作者吴宇航
        bmi.title("Night Star System")  # 设置标题#本作品作者吴宇航
        bmi.geometry("400x300")#本作品作者吴宇航
        Label(bmi, text="请输入你的体重（公斤kg为单位）").pack(expand=True)#本作品作者吴宇航
        var = Entry(bmi)#本作品作者吴宇航
        var.pack(expand=True)#本作品作者吴宇航
        Label(bmi, text="请输入你的身高（厘米cm为单位）").pack(expand=True)#本作品作者吴宇航
        var1 = Entry(bmi)#本作品作者吴宇航
        var1.pack(expand=True)#本作品作者吴宇航
        def jj():#本作品作者吴宇航
            try:#本作品作者吴宇航
                a = float(var.get())#本作品作者吴宇航
                jie = a * 10000 / (float(var1.get()) ** 2)#本作品作者吴宇航
                messagebox.showinfo("", "你的健康指数是" + str(jie))#本作品作者吴宇航
                if jie < 18.5:#本作品作者吴宇航
                    messagebox.showwarning("", "<18.5  偏瘦(建议多吃饭，保持营养均衡)")#本作品作者吴宇航
                elif jie <= 23.9:#本作品作者吴宇航
                    messagebox.showinfo("", ">=18.5~<=23.9  健康(坚持下去)")#本作品作者吴宇航
                else:#本作品作者吴宇航
                    messagebox.showwarning("", ">23.9  肥胖(管住嘴，迈开腿)")#本作品作者吴宇航
            except:#本作品作者吴宇航
                messagebox.showwarning("", "再乱输头给你拧歪了")#本作品作者吴宇航
#本作品作者吴宇航
        Button(bmi, text="计算", command=jj).pack()#本作品作者吴宇航
        bmi.mainloop()#本作品作者吴宇航
    elif dakai == "wuziqi":#本作品作者吴宇航
        #本作品作者吴宇航
        Chessman = namedtuple('Chessman', 'Name Value Color')#本作品作者吴宇航
        Point = namedtuple('Point', 'X Y')#本作品作者吴宇航
#本作品作者吴宇航
        BLACK_CHESSMAN = Chessman('黑子', 1, (50, 50, 50))#本作品作者吴宇航
        WHITE_CHESSMAN = Chessman('白子', 2, (220, 220, 220))#本作品作者吴宇航
#本作品作者吴宇航
        offset = [(1, 0), (0, 1), (1, 1), (1, -1),(-1, 1)]#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        class Checkerboard:#本作品作者吴宇航
            def __init__(self, line_points):#本作品作者吴宇航
                self._line_points = line_points#本作品作者吴宇航
                self._checkerboard = [[0] * line_points for _ in range(line_points)]#本作品作者吴宇航
#本作品作者吴宇航
            def _get_checkerboard(self):#本作品作者吴宇航
                return self._checkerboard#本作品作者吴宇航
#本作品作者吴宇航
            checkerboard = property(_get_checkerboard)#本作品作者吴宇航
#本作品作者吴宇航
            # 判断是否可落子#本作品作者吴宇航
            def can_drop(self, point):#本作品作者吴宇航
                return self._checkerboard[point.Y][point.X] == 0#本作品作者吴宇航
#本作品作者吴宇航
            def drop(self, chessman, point):#本作品作者吴宇航
                """#本作品作者吴宇航
                落子#本作品作者吴宇航
                :param chessman:#本作品作者吴宇航
                :param point:落子位置#本作品作者吴宇航
                :return:若该子落下之后即可获胜，则返回获胜方，否则返回 None#本作品作者吴宇航
                """#本作品作者吴宇航
                 #本作品作者吴宇航
                print(f'{chessman.Name} ({point.X}, {point.Y})')#本作品作者吴宇航
                self._checkerboard[point.Y][point.X] = chessman.Value#本作品作者吴宇航
#本作品作者吴宇航
                 #本作品作者吴宇航
                if self._win(point):#本作品作者吴宇航
                    print(f'{chessman.Name}获胜')#本作品作者吴宇航
                    return chessman#本作品作者吴宇航
#本作品作者吴宇航
             #本作品作者吴宇航
            def _win(self, point):#本作品作者吴宇航
                cur_value = self._checkerboard[point.Y][point.X]#本作品作者吴宇航
                for os in offset:#本作品作者吴宇航
                    if self._get_count_on_direction(point, cur_value, os[0], os[1]):#本作品作者吴宇航
                        return True#本作品作者吴宇航
#本作品作者吴宇航
             #本作品作者吴宇航
            def _get_count_on_direction(self, point, value, x_offset, y_offset):#本作品作者吴宇航
                count = 1#本作品作者吴宇航
                for step in range(1, 5):#本作品作者吴宇航
                    x = point.X + step * x_offset#本作品作者吴宇航
                    y = point.Y + step * y_offset#本作品作者吴宇航
                    if 0 <= x < self._line_points and 0 <= y < self._line_points and self._checkerboard[y][x] == value:#本作品作者吴宇航
                        count += 1#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        break#本作品作者吴宇航
                for step in range(1, 5):#本作品作者吴宇航
                    x = point.X - step * x_offset#本作品作者吴宇航
                    y = point.Y - step * y_offset#本作品作者吴宇航
                    if 0 <= x < self._line_points and 0 <= y < self._line_points and self._checkerboard[y][x] == value:#本作品作者吴宇航
                        count += 1#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        break#本作品作者吴宇航
#本作品作者吴宇航
                return count >= 5#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        SIZE = 30  #本作品作者吴宇航
        Line_Points = 19   #本作品作者吴宇航
        Outer_Width = 20  #本作品作者吴宇航
        Border_Width = 4 #本作品作者吴宇航
        Inside_Width = 4  #本作品作者吴宇航
        Border_Length = SIZE * (Line_Points - 1) + Inside_Width * 2 + Border_Width  #本作品作者吴宇航
        Start_X = Start_Y = Outer_Width + int(Border_Width / 2) + Inside_Width  #本作品作者吴宇航
        SCREEN_HEIGHT = SIZE * (Line_Points - 1) + Outer_Width * 2 + Border_Width + Inside_Width * 2  #本作品作者吴宇航
        SCREEN_WIDTH = SCREEN_HEIGHT + 200  #本作品作者吴宇航
#本作品作者吴宇航
        Stone_Radius = SIZE // 2 - 3  #本作品作者吴宇航
        Stone_Radius2 = SIZE // 2 + 3#本作品作者吴宇航
        Checkerboard_Color = (0xE3, 0x92, 0x65)  #本作品作者吴宇航
        BLACK_COLOR = (0, 0, 0)#本作品作者吴宇航
        WHITE_COLOR = (255, 255, 255)#本作品作者吴宇航
        RED_COLOR = (200, 30, 30)#本作品作者吴宇航
        BLUE_COLOR = (30, 30, 200)#本作品作者吴宇航
#本作品作者吴宇航
        RIGHT_INFO_POS_X = SCREEN_HEIGHT + Stone_Radius2 * 2 + 10#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        def print_text(screen, font, x, y, text, fcolor=(255, 255, 255)):#本作品作者吴宇航
            imgText = font.render(text, True, fcolor)#本作品作者吴宇航
            screen.blit(imgText, (x, y))#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        def main():#本作品作者吴宇航
            pygame.init()#本作品作者吴宇航
            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))#本作品作者吴宇航
            pygame.display.set_caption('五子棋')#本作品作者吴宇航
#本作品作者吴宇航
            font1 = pygame.font.SysFont('SimHei', 32)  #本作品作者吴宇航
            font2 = pygame.font.SysFont('SimHei', 72)  #本作品作者吴宇航
            fwidth, fheight = font2.size('黑方获胜')#本作品作者吴宇航
#本作品作者吴宇航
            checkerboard = Checkerboard(Line_Points)#本作品作者吴宇航
            cur_runner = BLACK_CHESSMAN#本作品作者吴宇航
            winner = None#本作品作者吴宇航
            computer = AI(Line_Points, WHITE_CHESSMAN)#本作品作者吴宇航
#本作品作者吴宇航
         #本作品作者吴宇航
            black_win_count = 0#本作品作者吴宇航
            white_win_count = 0#本作品作者吴宇航
#本作品作者吴宇航
            while True:#本作品作者吴宇航
                for event in pygame.event.get():#本作品作者吴宇航
                    if event.type == QUIT:#本作品作者吴宇航
                        pygame.quit()#本作品作者吴宇航
                        fasdasdf1()#本作品作者吴宇航
                    elif event.type == KEYDOWN  :#本作品作者吴宇航
                        if winner is None:#本作品作者吴宇航
                            print("清空")#本作品作者吴宇航
                            time.sleep(0.5)#本作品作者吴宇航
                            white_win_count += 1#本作品作者吴宇航
                        winner = None#本作品作者吴宇航
                        cur_runner = BLACK_CHESSMAN#本作品作者吴宇航
                        checkerboard = Checkerboard(Line_Points)#本作品作者吴宇航
                        computer = AI(Line_Points, WHITE_CHESSMAN)#本作品作者吴宇航
                    elif event.type == pygame.MOUSEBUTTONDOWN:  #本作品作者吴宇航
                        if winner is None:  #本作品作者吴宇航
                            pressed_array = pygame.mouse.get_pressed()#本作品作者吴宇航
                            if pressed_array[0]:#本作品作者吴宇航
                                mouse_pos = pygame.mouse.get_pos()#本作品作者吴宇航
                                click_point = _get_clickpoint(mouse_pos)#本作品作者吴宇航
                                if click_point is not None:   #本作品作者吴宇航
                                    if checkerboard.can_drop(click_point):#本作品作者吴宇航
                                        winner = checkerboard.drop(cur_runner, click_point)#本作品作者吴宇航
                                        if winner is None:   #本作品作者吴宇航
                                             #本作品作者吴宇航
                                            cur_runner = _get_next(cur_runner)#本作品作者吴宇航
                                            computer.get_opponent_drop(click_point)#本作品作者吴宇航
                                            AI_point = computer.AI_drop()#本作品作者吴宇航
                                            winner = checkerboard.drop(cur_runner, AI_point)#本作品作者吴宇航
                                            if winner is not None:#本作品作者吴宇航
                                                white_win_count += 1#本作品作者吴宇航
                                            cur_runner = _get_next(cur_runner)#本作品作者吴宇航
                                        else:#本作品作者吴宇航
                                            black_win_count += 1#本作品作者吴宇航
                                else:#本作品作者吴宇航
                                    print('超出棋盘区域')#本作品作者吴宇航
#本作品作者吴宇航
          #本作品作者吴宇航
                _draw_checkerboard(screen)#本作品作者吴宇航
#本作品作者吴宇航
                for i, row in enumerate(checkerboard.checkerboard):#本作品作者吴宇航
                    for j, cell in enumerate(row):#本作品作者吴宇航
                        if cell == BLACK_CHESSMAN.Value:#本作品作者吴宇航
                            _draw_chessman(screen, Point(j, i), BLACK_CHESSMAN.Color)#本作品作者吴宇航
                        elif cell == WHITE_CHESSMAN.Value:#本作品作者吴宇航
                            _draw_chessman(screen, Point(j, i), WHITE_CHESSMAN.Color)#本作品作者吴宇航
#本作品作者吴宇航
                _draw_left_info(screen, font1, cur_runner, black_win_count, white_win_count)#本作品作者吴宇航
#本作品作者吴宇航
                if winner:#本作品作者吴宇航
                    print_text(screen, font2, (SCREEN_WIDTH - fwidth) // 2, (SCREEN_HEIGHT - fheight) // 2, winner.Name + '获胜',#本作品作者吴宇航
                               RED_COLOR)#本作品作者吴宇航
#本作品作者吴宇航
                pygame.display.flip()#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        def _get_next(cur_runner):#本作品作者吴宇航
            if cur_runner == BLACK_CHESSMAN:#本作品作者吴宇航
                return WHITE_CHESSMAN#本作品作者吴宇航
            else:#本作品作者吴宇航
                return BLACK_CHESSMAN#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        def _draw_checkerboard(screen):#本作品作者吴宇航
           #本作品作者吴宇航
            screen.fill(Checkerboard_Color)#本作品作者吴宇航
            #本作品作者吴宇航
            pygame.draw.rect(screen, BLACK_COLOR, (Outer_Width, Outer_Width, Border_Length, Border_Length), Border_Width)#本作品作者吴宇航
            #本作品作者吴宇航
            for i in range(Line_Points):#本作品作者吴宇航
                pygame.draw.line(screen, BLACK_COLOR,#本作品作者吴宇航
                                 (Start_Y, Start_Y + SIZE * i),#本作品作者吴宇航
                                 (Start_Y + SIZE * (Line_Points - 1), Start_Y + SIZE * i),#本作品作者吴宇航
                                 1)#本作品作者吴宇航
            for j in range(Line_Points):#本作品作者吴宇航
                pygame.draw.line(screen, BLACK_COLOR,#本作品作者吴宇航
                                 (Start_X + SIZE * j, Start_X),#本作品作者吴宇航
                                 (Start_X + SIZE * j, Start_X + SIZE * (Line_Points - 1)),#本作品作者吴宇航
                                 1)#本作品作者吴宇航
          #本作品作者吴宇航
            for i in (3, 9, 15):#本作品作者吴宇航
                for j in (3, 9, 15):#本作品作者吴宇航
                    if i == j == 9:#本作品作者吴宇航
                        radius = 5#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        radius = 3#本作品作者吴宇航
                     #本作品作者吴宇航
                    pygame.gfxdraw.aacircle(screen, Start_X + SIZE * i, Start_Y + SIZE * j, radius, BLACK_COLOR)#本作品作者吴宇航
                    pygame.gfxdraw.filled_circle(screen, Start_X + SIZE * i, Start_Y + SIZE * j, radius, BLACK_COLOR)#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
         #本作品作者吴宇航
        def _draw_chessman(screen, point, stone_color):#本作品作者吴宇航
            # pygame.draw.circle(screen, stone_color, (Start_X + SIZE * point.X, Start_Y + SIZE * point.Y), Stone_Radius)#本作品作者吴宇航
            pygame.gfxdraw.aacircle(screen, Start_X + SIZE * point.X, Start_Y + SIZE * point.Y, Stone_Radius, stone_color)#本作品作者吴宇航
            pygame.gfxdraw.filled_circle(screen, Start_X + SIZE * point.X, Start_Y + SIZE * point.Y, Stone_Radius, stone_color)#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
         #本作品作者吴宇航
        def _draw_left_info(screen, font, cur_runner, black_win_count, white_win_count):#本作品作者吴宇航
            _draw_chessman_pos(screen, (SCREEN_HEIGHT + Stone_Radius2, Start_X + Stone_Radius2), BLACK_CHESSMAN.Color)#本作品作者吴宇航
            _draw_chessman_pos(screen, (SCREEN_HEIGHT + Stone_Radius2, Start_X + Stone_Radius2 * 4), WHITE_CHESSMAN.Color)#本作品作者吴宇航
#本作品作者吴宇航
            print_text(screen, font, RIGHT_INFO_POS_X, Start_X + 3, '玩家', BLUE_COLOR)#本作品作者吴宇航
            print_text(screen, font, RIGHT_INFO_POS_X, Start_X + Stone_Radius2 * 3 + 3, '电脑', BLUE_COLOR)#本作品作者吴宇航
#本作品作者吴宇航
            print_text(screen, font, SCREEN_HEIGHT, SCREEN_HEIGHT - Stone_Radius2 * 8, '战况：', BLUE_COLOR)#本作品作者吴宇航
            _draw_chessman_pos(screen, (SCREEN_HEIGHT + Stone_Radius2, SCREEN_HEIGHT - int(Stone_Radius2 * 4.5)),#本作品作者吴宇航
                               BLACK_CHESSMAN.Color)#本作品作者吴宇航
            _draw_chessman_pos(screen, (SCREEN_HEIGHT + Stone_Radius2, SCREEN_HEIGHT - Stone_Radius2 * 2), WHITE_CHESSMAN.Color)#本作品作者吴宇航
            print_text(screen, font, RIGHT_INFO_POS_X, SCREEN_HEIGHT - int(Stone_Radius2 * 5.5) + 3, f'{black_win_count} 胜',#本作品作者吴宇航
                       BLUE_COLOR)#本作品作者吴宇航
            print_text(screen, font, RIGHT_INFO_POS_X, SCREEN_HEIGHT - Stone_Radius2 * 3 + 3, f'{white_win_count} 胜',#本作品作者吴宇航
                       BLUE_COLOR)#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        def _draw_chessman_pos(screen, pos, stone_color):#本作品作者吴宇航
            pygame.gfxdraw.aacircle(screen, pos[0], pos[1], Stone_Radius2, stone_color)#本作品作者吴宇航
            pygame.gfxdraw.filled_circle(screen, pos[0], pos[1], Stone_Radius2, stone_color)#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        def _get_clickpoint(click_pos):#本作品作者吴宇航
            pos_x = click_pos[0] - Start_X#本作品作者吴宇航
            pos_y = click_pos[1] - Start_Y#本作品作者吴宇航
            if pos_x < -Inside_Width or pos_y < -Inside_Width:#本作品作者吴宇航
                return None#本作品作者吴宇航
            x = pos_x // SIZE#本作品作者吴宇航
            y = pos_y // SIZE#本作品作者吴宇航
            if pos_x % SIZE > Stone_Radius:#本作品作者吴宇航
                x += 1#本作品作者吴宇航
            if pos_y % SIZE > Stone_Radius:#本作品作者吴宇航
                y += 1#本作品作者吴宇航
            if x >= Line_Points or y >= Line_Points:#本作品作者吴宇航
                return None#本作品作者吴宇航
#本作品作者吴宇航
            return Point(x, y)#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        class AI:#本作品作者吴宇航
            def __init__(self, line_points, chessman):#本作品作者吴宇航
                self._line_points = line_points#本作品作者吴宇航
                self._my = chessman#本作品作者吴宇航
                self._opponent = BLACK_CHESSMAN if chessman == WHITE_CHESSMAN else WHITE_CHESSMAN#本作品作者吴宇航
                self._checkerboard = [[0] * line_points for _ in range(line_points)]#本作品作者吴宇航
#本作品作者吴宇航
            def get_opponent_drop(self, point):#本作品作者吴宇航
                self._checkerboard[point.Y][point.X] = self._opponent.Value#本作品作者吴宇航
#本作品作者吴宇航
            def AI_drop(self):#本作品作者吴宇航
                point = None#本作品作者吴宇航
                score = 0#本作品作者吴宇航
                for i in range(self._line_points):#本作品作者吴宇航
                    for j in range(self._line_points):#本作品作者吴宇航
                        if self._checkerboard[j][i] == 0:#本作品作者吴宇航
                            _score = self._get_point_score(Point(i, j))#本作品作者吴宇航
                            if _score > score:#本作品作者吴宇航
                                score = _score#本作品作者吴宇航
                                point = Point(i, j)#本作品作者吴宇航
                            elif _score == score:#本作品作者吴宇航
                                score = _score#本作品作者吴宇航
                                r = random.randint(0, 20)#本作品作者吴宇航
                                if r % 2 == 0:#本作品作者吴宇航
                                    point = Point(i, j)#本作品作者吴宇航
                self._checkerboard[point.Y][point.X] = self._my.Value#本作品作者吴宇航
                return point#本作品作者吴宇航
#本作品作者吴宇航
            def _get_point_score(self, point):#本作品作者吴宇航
                score = 0#本作品作者吴宇航
                for os in offset:#本作品作者吴宇航
                    score += self._get_direction_score(point, os[0], os[1])#本作品作者吴宇航
                return score#本作品作者吴宇航
#本作品作者吴宇航
            def _get_direction_score(self, point, x_offset, y_offset):#本作品作者吴宇航
                count = 0  #本作品作者吴宇航
                _count = 0  #本作品作者吴宇航
                space = None   #本作品作者吴宇航
                _space = None   #本作品作者吴宇航
                both = 0  #本作品作者吴宇航
                _both = 0   #本作品作者吴宇航
#本作品作者吴宇航
                 #本作品作者吴宇航
                flag = self._get_stone_color(point, x_offset, y_offset, True)#本作品作者吴宇航
                if flag != 0:#本作品作者吴宇航
                    for step in range(1, 6):#本作品作者吴宇航
                        x = point.X + step * x_offset#本作品作者吴宇航
                        y = point.Y + step * y_offset#本作品作者吴宇航
                        if 0 <= x < self._line_points and 0 <= y < self._line_points:#本作品作者吴宇航
                            if flag == 1:#本作品作者吴宇航
                                if self._checkerboard[y][x] == self._my.Value:#本作品作者吴宇航
                                    count += 1#本作品作者吴宇航
                                    if space is False:#本作品作者吴宇航
                                        space = True#本作品作者吴宇航
                                elif self._checkerboard[y][x] == self._opponent.Value:#本作品作者吴宇航
                                    _both += 1#本作品作者吴宇航
                                    break#本作品作者吴宇航
                                else:#本作品作者吴宇航
                                    if space is None:#本作品作者吴宇航
                                        space = False#本作品作者吴宇航
                                    else:#本作品作者吴宇航
                                        break   #本作品作者吴宇航
                            elif flag == 2:#本作品作者吴宇航
                                if self._checkerboard[y][x] == self._my.Value:#本作品作者吴宇航
                                    _both += 1#本作品作者吴宇航
                                    break#本作品作者吴宇航
                                elif self._checkerboard[y][x] == self._opponent.Value:#本作品作者吴宇航
                                    _count += 1#本作品作者吴宇航
                                    if _space is False:#本作品作者吴宇航
                                        _space = True#本作品作者吴宇航
                                else:#本作品作者吴宇航
                                    if _space is None:#本作品作者吴宇航
                                        _space = False#本作品作者吴宇航
                                    else:#本作品作者吴宇航
                                        break#本作品作者吴宇航
                        else:#本作品作者吴宇航
                             #本作品作者吴宇航
                            if flag == 1:#本作品作者吴宇航
                                both += 1#本作品作者吴宇航
                            elif flag == 2:#本作品作者吴宇航
                                _both += 1#本作品作者吴宇航
#本作品作者吴宇航
                if space is False:#本作品作者吴宇航
                    space = None#本作品作者吴宇航
                if _space is False:#本作品作者吴宇航
                    _space = None#本作品作者吴宇航
#本作品作者吴宇航
                _flag = self._get_stone_color(point, -x_offset, -y_offset, True)#本作品作者吴宇航
                if _flag != 0:#本作品作者吴宇航
                    for step in range(1, 6):#本作品作者吴宇航
                        x = point.X - step * x_offset#本作品作者吴宇航
                        y = point.Y - step * y_offset#本作品作者吴宇航
                        if 0 <= x < self._line_points and 0 <= y < self._line_points:#本作品作者吴宇航
                            if _flag == 1:#本作品作者吴宇航
                                if self._checkerboard[y][x] == self._my.Value:#本作品作者吴宇航
                                    count += 1#本作品作者吴宇航
                                    if space is False:#本作品作者吴宇航
                                        space = True#本作品作者吴宇航
                                elif self._checkerboard[y][x] == self._opponent.Value:#本作品作者吴宇航
                                    _both += 1#本作品作者吴宇航
                                    break#本作品作者吴宇航
                                else:#本作品作者吴宇航
                                    if space is None:#本作品作者吴宇航
                                        space = False#本作品作者吴宇航
                                    else:#本作品作者吴宇航
                                        break   #本作品作者吴宇航
                            elif _flag == 2:#本作品作者吴宇航
                                if self._checkerboard[y][x] == self._my.Value:#本作品作者吴宇航
                                    _both += 1#本作品作者吴宇航
                                    break#本作品作者吴宇航
                                elif self._checkerboard[y][x] == self._opponent.Value:#本作品作者吴宇航
                                    _count += 1#本作品作者吴宇航
                                    if _space is False:#本作品作者吴宇航
                                        _space = True#本作品作者吴宇航
                                else:#本作品作者吴宇航
                                    if _space is None:#本作品作者吴宇航
                                        _space = False#本作品作者吴宇航
                                    else:#本作品作者吴宇航
                                        break#本作品作者吴宇航
                        else:#本作品作者吴宇航
                             #本作品作者吴宇航
                            if _flag == 1:#本作品作者吴宇航
                                both += 1#本作品作者吴宇航
                            elif _flag == 2:#本作品作者吴宇航
                                _both += 1#本作品作者吴宇航
#本作品作者吴宇航
                #本作品作者吴宇航
                score = 0#本作品作者吴宇航
                if count == 4:#本作品作者吴宇航
                    score = 10000#本作品作者吴宇航
                elif _count == 4:#本作品作者吴宇航
                    score = 9000#本作品作者吴宇航
                elif count == 3:#本作品作者吴宇航
                    if both == 0:#本作品作者吴宇航
                        score = 1000#本作品作者吴宇航
                    elif both == 1:#本作品作者吴宇航
                        score = 100#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        score = 0#本作品作者吴宇航
                elif _count == 3:#本作品作者吴宇航
                    if _both == 0:#本作品作者吴宇航
                        score = 900#本作品作者吴宇航
                    elif _both == 1:#本作品作者吴宇航
                        score = 90#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        score = 0#本作品作者吴宇航
                elif count == 2:#本作品作者吴宇航
                    if both == 0:#本作品作者吴宇航
                        score = 100#本作品作者吴宇航
                    elif both == 1:#本作品作者吴宇航
                        score = 10#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        score = 0#本作品作者吴宇航
                elif _count == 2:#本作品作者吴宇航
                    if _both == 0:#本作品作者吴宇航
                        score = 90#本作品作者吴宇航
                    elif _both == 1:#本作品作者吴宇航
                        score = 9#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        score = 0#本作品作者吴宇航
                elif count == 1:#本作品作者吴宇航
                    score = 10#本作品作者吴宇航
                elif _count == 1:#本作品作者吴宇航
                    score = 9#本作品作者吴宇航
                else:#本作品作者吴宇航
                    score = 0#本作品作者吴宇航
#本作品作者吴宇航
                if space or _space:#本作品作者吴宇航
                    score /= 2#本作品作者吴宇航
                return score#本作品作者吴宇航
            def _get_stone_color(self, point, x_offset, y_offset, next):#本作品作者吴宇航
                x = point.X + x_offset#本作品作者吴宇航
                y = point.Y + y_offset#本作品作者吴宇航
                if 0 <= x < self._line_points and 0 <= y < self._line_points:#本作品作者吴宇航
                    if self._checkerboard[y][x] == self._my.Value:#本作品作者吴宇航
                        return 1#本作品作者吴宇航
                    elif self._checkerboard[y][x] == self._opponent.Value:#本作品作者吴宇航
                        return 2#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        if next:#本作品作者吴宇航
                            return self._get_stone_color(Point(x, y), x_offset, y_offset, False)#本作品作者吴宇航
                        else:#本作品作者吴宇航
                            return 0#本作品作者吴宇航
                else:#本作品作者吴宇航
                    return 0#本作品作者吴宇航
        if __name__ == '__main__':#本作品作者吴宇航
            print("-------------------------------")#本作品作者吴宇航
            main()#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
    elif dakai == "minecraft":#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        # 每秒帧数#本作品作者吴宇航
        TICKS_PER_SEC = 120#本作品作者吴宇航
#本作品作者吴宇航
        # 你可以走的大小#本作品作者吴宇航
        SECTOR_SIZE =5000#本作品作者吴宇航
#本作品作者吴宇航
        # 行走速度与飞行速度#本作品作者吴宇航
        WALKING_SPEED = 5.5#本作品作者吴宇航
        FLYING_SPEED = 15#本作品作者吴宇航
#本作品作者吴宇航
        # 重力与跳跃高度#本作品作者吴宇航
        GRAVITY = 20#本作品作者吴宇航
        MAX_JUMP_HEIGHT =1#本作品作者吴宇航
#本作品作者吴宇航
        # About the height of a block.#本作品作者吴宇航
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
        PLAYER_HEIGHT = 2#本作品作者吴宇航
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
            """ #本作品作者吴宇航
            Return the bounding vertices of the texture square.#本作品作者吴宇航
#本作品作者吴宇航
            """#本作品作者吴宇航
            m = 1.0 / n#本作品作者吴宇航
            dx = x * m#本作品作者吴宇航
            dy = y * m#本作品作者吴宇航
            return dx, dy, dx + m, dy, dx + m, dy + m, dx, dy + m#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        def tex_coords(top, bottom, side):#本作品作者吴宇航
            """ #本作品作者吴宇航
            Return a list of the texture squares for the top, bottom and side.#本作品作者吴宇航
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
        PURPLE = tex_coords((3, 1), (3, 1), (3, 1))#本作品作者吴宇航
        RED = tex_coords((3, 0), (3, 0), (3, 0))#本作品作者吴宇航
        GREEN = tex_coords((3, 2), (3, 2), (3, 2))#本作品作者吴宇航
        BLUE = tex_coords((1, 2), (1, 2), (1, 2))#本作品作者吴宇航
        BLACK = tex_coords((2, 2), (2, 2), (2, 2))#本作品作者吴宇航
        ORANGE = tex_coords((3, 2), (3, 2), (3, 2))#本作品作者吴宇航
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
                n = 200 # 1/2 width and height of world#本作品作者吴宇航
                s = 1  # step size#本作品作者吴宇航
                y =0   # initial y height#本作品作者吴宇航
                for x in xrange(-n, n + 1, s):#本作品作者吴宇航
                    for z in xrange(-n, n + 1, s):#本作品作者吴宇航
                        # create a layer stone an grass everywhere.#本作品作者吴宇航
                        self.add_block((x, y - 2, z), GRASS, immediate=False)#本作品作者吴宇航
                        self.add_block((x, y - 3, z), STONE, immediate=False)#本作品作者吴宇航
                        if x in (-n, n) or z in (-n, n):#本作品作者吴宇航
                            # create outer walls.#本作品作者吴宇航
                            for dy in xrange(-2, 3):#本作品作者吴宇航
                                self.add_block((x, y + dy, z), STONE, immediate=False)#本作品作者吴宇航
#本作品作者吴宇航
                # generate the hills randomly#本作品作者吴宇航
                o = n -15#本作品作者吴宇航
                for _ in xrange(120):#本作品作者吴宇航
                    a = random.randint(-o, o)  # x position of the hill#本作品作者吴宇航
                    b = random.randint(-o, o)  # z position of the hill#本作品作者吴宇航
                    c = -1  # base of the hill#本作品作者吴宇航
                    h = random.randint(2,6) # height of the hill#本作品作者吴宇航
                    s = random.randint(4,12)  # 2 * s is the side length of the hill#本作品作者吴宇航
                    d = 1  # how quickly to taper off the hills#本作品作者吴宇航
                    t = random.choice([GRASS, SAND,STONE])#本作品作者吴宇航
                    for y in xrange(c, c + h):#本作品作者吴宇航
                        for x in xrange(a - s, a + s + 1):#本作品作者吴宇航
                            for z in xrange(b - s, b + s + 1):#本作品作者吴宇航
                                if (x - a) ** 2 + (z - b) ** 2 > (s + 1) ** 2:#本作品作者吴宇航
                                    continue#本作品作者吴宇航
                                if (x - 0) ** 2 + (z - 0) ** 2 < 5 ** 2:#本作品作者吴宇航
                                    continue#本作品作者吴宇航
                                self.add_block((x, y, z), t, immediate=False)#本作品作者吴宇航
                        s -= d  # decrement side lenth so hills taper off#本作品作者吴宇航
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
                # start = time.time#本作品作者吴宇航
                # while self.queue and time.time < 1 / TICKS_PER_SEC:#本作品作者吴宇航
                #     self._dequeue()#本作品作者吴宇航
                pass#本作品作者吴宇航
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
                self.position = (0, 0, 0)#本作品作者吴宇航
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
                self.inventory = [BRICK, GRASS, SAND,STONE,RED,PURPLE,GREEN,BLUE,BLACK,ORANGE]#本作品作者吴宇航
#本作品作者吴宇航
                # The current block the user can place. Hit num keys to cycle.#本作品作者吴宇航
                self.block = self.inventory[0]#本作品作者吴宇航
#本作品作者吴宇航
                # Convenience list of num keys.#本作品作者吴宇航
                self.num_keys = [#本作品作者吴宇航
                    key._1, key._2, key._3, key._4, key._5,#本作品作者吴宇航
                    key._6, key._7, key._8, key._9, key._0,key.E,key.R]#本作品作者吴宇航
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
                speed = FLYING_SPEED if self.flying else WALKING_SPEED#本作品作者吴宇航
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
                x, y, z = self.position#本作品作者吴宇航
                x, y, z = self.collide((x + dx, y + dy, z + dz), PLAYER_HEIGHT)#本作品作者吴宇航
                self.position = (x, y, z)#本作品作者吴宇航
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
                pad = 0#本作品作者吴宇航
                p = list(position)#本作品作者吴宇航
                np = normalize(position)#本作品作者吴宇航
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
                            if face == (0, -1, 0) or face == (0, 1, 0):#本作品作者吴宇航
                                # You are colliding with the ground or ceiling, so stop#本作品作者吴宇航
                                # falling / rising.#本作品作者吴宇航
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
                elif symbol == key.SPACE:#本作品作者吴宇航
                    if self.dy == 0:#本作品作者吴宇航
                        self.dy = JUMP_SPEED#本作品作者吴宇航
                elif symbol == key.ESCAPE:#本作品作者吴宇航
                    self.set_exclusive_mouse(False)#本作品作者吴宇航
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
#本作品作者吴宇航
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
                gluPerspective(65.0, width / float(height), 0.1, 60.0)#本作品作者吴宇航
                glMatrixMode(GL_MODELVIEW)#本作品作者吴宇航
                glLoadIdentity()#本作品作者吴宇航
                x, y = self.rotation#本作品作者吴宇航
                glRotatef(x, 0, 1, 0)#本作品作者吴宇航
                glRotatef(-y, math.cos(math.radians(x)), 0, math.sin(math.radians(x)))#本作品作者吴宇航
                x, y, z = self.position#本作品作者吴宇航
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
            glFogfv(GL_FOG_COLOR, (GLfloat * 4)(0.5, 0.69, 1.0, 0))#本作品作者吴宇航
            # Say we have no preference between rendering speed and quality.#本作品作者吴宇航
            glHint(GL_FOG_HINT, GL_DONT_CARE)#本作品作者吴宇航
            # Specify the equation used to compute the blending factor.#本作品作者吴宇航
            glFogi(GL_FOG_MODE, GL_LINEAR)#本作品作者吴宇航
            # How close and far away fog starts and ends. The closer the start and end,#本作品作者吴宇航
            # the denser the fog in the fog range.#本作品作者吴宇航
            glFogf(GL_FOG_START, 20.0)#本作品作者吴宇航
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
            window = Window(width=800, height=450, caption='Pyglet', resizable=True)#本作品作者吴宇航
            # Hide the mouse cursor and prevent the mouse from leaving the window.#本作品作者吴宇航
            window.set_exclusive_mouse(True)#本作品作者吴宇航
            setup()#本作品作者吴宇航
            pyglet.app.run()#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        if __name__ == '__main__':#本作品作者吴宇航
            main()#本作品作者吴宇航
    elif dakai == "snake":#本作品作者吴宇航
        #!/usr/bin/env python #本作品作者吴宇航
        # -*- coding:utf-8 -*- #本作品作者吴宇航
         #本作品作者吴宇航
        """ #本作品作者吴宇航
        @version: v1.0 #本作品作者吴宇航
        @author: Harp#本作品作者吴宇航
        @contact: liutao25@baidu.com #本作品作者吴宇航
        @software: PyCharm #本作品作者吴宇航
        @file: MySnake.py #本作品作者吴宇航
        @time: 2018/1/15 0015 23:40 #本作品作者吴宇航
        """#本作品作者吴宇航
         #本作品作者吴宇航
         #本作品作者吴宇航
#本作品作者吴宇航
         #本作品作者吴宇航
         #本作品作者吴宇航
        def direction_check(moving_direction, change_direction):#本作品作者吴宇航
          directions = [['up', 'down'], ['left', 'right']]#本作品作者吴宇航
          if moving_direction in directions[0] and change_direction in directions[1]:#本作品作者吴宇航
            return change_direction#本作品作者吴宇航
          elif moving_direction in directions[1] and change_direction in directions[0]:#本作品作者吴宇航
            return change_direction#本作品作者吴宇航
          return moving_direction#本作品作者吴宇航
         #本作品作者吴宇航
         #本作品作者吴宇航
        class Snake:#本作品作者吴宇航
         #本作品作者吴宇航
          colors = list(product([0, 64, 128, 192, 255], repeat=3))[1:-1]#本作品作者吴宇航
         #本作品作者吴宇航
          def __init__(self):#本作品作者吴宇航
            self.map = {(x, y): 0 for x in range(32) for y in range(24)}#本作品作者吴宇航
            self.body = [[100, 100], [120, 100], [140, 100]]#本作品作者吴宇航
            self.head = [140, 100]#本作品作者吴宇航
            self.food = []#本作品作者吴宇航
            self.food_color = []#本作品作者吴宇航
            self.moving_direction = 'right'#本作品作者吴宇航
            self.speed = 4#本作品作者吴宇航
            self.generate_food()#本作品作者吴宇航
            self.game_started = False#本作品作者吴宇航
         #本作品作者吴宇航
          def check_game_status(self):#本作品作者吴宇航
            if self.body.count(self.head) > 1:#本作品作者吴宇航
              return True#本作品作者吴宇航
            if self.head[0] < 0 or self.head[0] > 620 or self.head[1] < 0 or self.head[1] > 460:#本作品作者吴宇航
              return True#本作品作者吴宇航
            return False#本作品作者吴宇航
         #本作品作者吴宇航
          def move_head(self):#本作品作者吴宇航
            moves = {#本作品作者吴宇航
              'right': (20, 0),#本作品作者吴宇航
              'up': (0, -20),#本作品作者吴宇航
              'down': (0, 20),#本作品作者吴宇航
              'left': (-20, 0)#本作品作者吴宇航
            }#本作品作者吴宇航
            step = moves[self.moving_direction]#本作品作者吴宇航
            self.head[0] += step[0]#本作品作者吴宇航
            self.head[1] += step[1]#本作品作者吴宇航
         #本作品作者吴宇航
          def generate_food(self):#本作品作者吴宇航
            self.speed = len(self.body) // 16 if len(self.body) // 16 > 4 else self.speed#本作品作者吴宇航
            for seg in self.body:#本作品作者吴宇航
              x, y = seg#本作品作者吴宇航
              self.map[x//20, y//20] = 1#本作品作者吴宇航
            empty_pos = [pos for pos in self.map.keys() if not self.map[pos]]#本作品作者吴宇航
            result = choice(empty_pos)#本作品作者吴宇航
            self.food_color = list(choice(self.colors))#本作品作者吴宇航
            self.food = [result[0]*20, result[1]*20]#本作品作者吴宇航
         #本作品作者吴宇航
         #本作品作者吴宇航
        def main():#本作品作者吴宇航
          key_direction_dict = {#本作品作者吴宇航
            119: 'up', # W#本作品作者吴宇航
            115: 'down', # S#本作品作者吴宇航
            97: 'left', # A#本作品作者吴宇航
            100: 'right', # D#本作品作者吴宇航
            273: 'up', # UP#本作品作者吴宇航
            274: 'down', # DOWN#本作品作者吴宇航
            276: 'left', # LEFT#本作品作者吴宇航
            275: 'right', # RIGHT#本作品作者吴宇航
          }#本作品作者吴宇航
         #本作品作者吴宇航
          fps_clock = pygame.time.Clock()#本作品作者吴宇航
          pygame.init()#本作品作者吴宇航
          pygame.mixer.init()#本作品作者吴宇航
          snake = Snake()#本作品作者吴宇航
          sound = False#本作品作者吴宇航
          if path.exists('eat.wav'):#本作品作者吴宇航
            sound_wav = pygame.mixer.Sound("eat.wav")#本作品作者吴宇航
            sound = True#本作品作者吴宇航
          title_font = pygame.font.SysFont('arial', 32)#本作品作者吴宇航
          welcome_words = title_font.render('Welcome to My Snake', True, (0, 0, 0), (255, 255, 255))#本作品作者吴宇航
          tips_font = pygame.font.SysFont('arial', 24)#本作品作者吴宇航
          start_game_words = tips_font.render('Click to Start Game', True, (0, 0, 0), (255, 255, 255))#本作品作者吴宇航
          close_game_words = tips_font.render('Press ESC to Close', True, (0, 0, 0), (255, 255, 255))#本作品作者吴宇航
          gameover_words = title_font.render('GAME OVER', True, (205, 92, 92), (255, 255, 255))#本作品作者吴宇航
          win_words = title_font.render('THE SNAKE IS LONG ENOUGH AND YOU WIN!', True, (0, 0, 205), (255, 255, 255))#本作品作者吴宇航
          screen = pygame.display.set_mode((640, 480), 0, 32)#本作品作者吴宇航
          pygame.display.set_caption('My Snake')#本作品作者吴宇航
          new_direction = snake.moving_direction#本作品作者吴宇航
          while 1:#本作品作者吴宇航
            for event in pygame.event.get():#本作品作者吴宇航
              if event.type == QUIT:#本作品作者吴宇航
                pygame.quit()#本作品作者吴宇航
                fasdasdf1()#本作品作者吴宇航
              elif event.type == KEYDOWN:#本作品作者吴宇航
                if event.key == 27:#本作品作者吴宇航
                  exit()#本作品作者吴宇航
                if snake.game_started and event.key in key_direction_dict:#本作品作者吴宇航
                  direction = key_direction_dict[event.key]#本作品作者吴宇航
                  new_direction = direction_check(snake.moving_direction, direction)#本作品作者吴宇航
              elif (not snake.game_started) and event.type == pygame.MOUSEBUTTONDOWN:#本作品作者吴宇航
                x, y = pygame.mouse.get_pos()#本作品作者吴宇航
                if 213 <= x <= 422 and 304 <= y <= 342:#本作品作者吴宇航
                  snake.game_started = True#本作品作者吴宇航
            screen.fill((255, 255, 255))#本作品作者吴宇航
            if snake.game_started:#本作品作者吴宇航
              snake.moving_direction = new_direction # 在这里赋值，而不是在event事件的循环中赋值，避免按键太快#本作品作者吴宇航
              snake.move_head()#本作品作者吴宇航
              snake.body.append(snake.head[:])#本作品作者吴宇航
              if snake.head == snake.food:#本作品作者吴宇航
                if sound:#本作品作者吴宇航
                  sound_wav.play()#本作品作者吴宇航
                snake.generate_food()#本作品作者吴宇航
              else:#本作品作者吴宇航
                snake.body.pop(0)#本作品作者吴宇航
              for seg in snake.body:#本作品作者吴宇航
                pygame.draw.rect(screen, [0, 0, 0], [seg[0], seg[1], 20, 20], 0)#本作品作者吴宇航
              pygame.draw.rect(screen, snake.food_color, [snake.food[0], snake.food[1], 20, 20], 0)#本作品作者吴宇航
              if snake.check_game_status():#本作品作者吴宇航
                screen.blit(gameover_words, (241, 310))#本作品作者吴宇航
                pygame.display.update()#本作品作者吴宇航
                snake = Snake()#本作品作者吴宇航
                new_direction = snake.moving_direction#本作品作者吴宇航
                sleep(3)#本作品作者吴宇航
              elif len(snake.body) == 512:#本作品作者吴宇航
                screen.blit(win_words, (33, 210))#本作品作者吴宇航
                pygame.display.update()#本作品作者吴宇航
                snake = Snake()#本作品作者吴宇航
                new_direction = snake.moving_direction#本作品作者吴宇航
                sleep(3)#本作品作者吴宇航
            else:#本作品作者吴宇航
              screen.blit(welcome_words, (188, 100))#本作品作者吴宇航
              screen.blit(start_game_words, (236, 310))#本作品作者吴宇航
              screen.blit(close_game_words, (233, 350))#本作品作者吴宇航
            pygame.display.update()#本作品作者吴宇航
            fps_clock.tick(snake.speed)#本作品作者吴宇航
         #本作品作者吴宇航
         #本作品作者吴宇航
        if __name__ == '__main__':#本作品作者吴宇航
          main()#本作品作者吴宇航
    elif dakai == "eluosi":#本作品作者吴宇航
#本作品作者吴宇航
        block_initial_position,score,times,gameover,press,all_block,background=[20,5],[0],0,[],False,[[[0,0],[0,-1],[0,1],[0,2]],[[0,0],[0,1],[-1,1],[-1,0]],[[0,0],[0,-1],[-1,0],[-1,1]],[[0,0],[0,1],[-1,-1],[-1,0]],[[0,0],[0,1],[1,0],[0,-1]],[[0,0],[1,0],[-1,0],[1,-1]],[[0,0],[1,0],[-1,0],[1,1]]],[[0 for column in range(0,10)]for row in range(0,22)]#本作品作者吴宇航
        background[0],select_block=[1 for column in range(0,10)],list(random.choice(all_block))#本作品作者吴宇航
        def move(n):#本作品作者吴宇航
            if n==100:#本作品作者吴宇航
                for row,column in select_block:#本作品作者吴宇航
                    pygame.draw.rect(screen,(255,165,0),((column+block_initial_position[1])*40,800-(row+block_initial_position[0])*40,38,38))#本作品作者吴宇航
                for row in range(0,20):#本作品作者吴宇航
                    for column in range(0,10):#本作品作者吴宇航
                        if background[row][column]:pygame.draw.rect(screen,(0,0,255),(column*40,800-row*40,38,38))#本作品作者吴宇航
            y_drop,x_move=block_initial_position#本作品作者吴宇航
            if n==1 or n==-1:#本作品作者吴宇航
                x_move+=n#本作品作者吴宇航
                for row,column in select_block:#本作品作者吴宇航
                    if (column+x_move)<0 or (column+x_move)>9 or background[row+y_drop][column+x_move]:break#本作品作者吴宇航
                else:block_initial_position.clear(),block_initial_position.extend([y_drop,x_move])#本作品作者吴宇航
            if n==0:#本作品作者吴宇航
                rotating_position=[(-column,row)for row,column in select_block]#本作品作者吴宇航
                for row,column in rotating_position:#本作品作者吴宇航
                    if (column+x_move)<0 or (column+x_move)>9 or background[row+y_drop][column+x_move]:break#本作品作者吴宇航
                else:select_block.clear(),select_block.extend(rotating_position)#本作品作者吴宇航
            if n==10:#本作品作者吴宇航
                y_drop-=1#本作品作者吴宇航
                for row,column in select_block:#本作品作者吴宇航
                    if background[row+y_drop][column+x_move]==1:break#本作品作者吴宇航
                else:#本作品作者吴宇航
                    block_initial_position.clear()#本作品作者吴宇航
                    block_initial_position.extend([y_drop,x_move])#本作品作者吴宇航
                    return#本作品作者吴宇航
                for row,column in select_block:background[block_initial_position[0]+row][block_initial_position[1]+column]=1#本作品作者吴宇航
                complete_row=[]#本作品作者吴宇航
                for row in range(1,21):#本作品作者吴宇航
                    if 0 not in background[row]:complete_row.append(row)#本作品作者吴宇航
                complete_row.sort(reverse=True)#本作品作者吴宇航
                for row in complete_row:#本作品作者吴宇航
                    background.pop(row)#本作品作者吴宇航
                    background.append([0 for column in range(0,10)])#本作品作者吴宇航
                score[0]+=len(complete_row)#本作品作者吴宇航
                pygame.display.set_caption('Tetris,Score:'+str(score[0])+' Robin5')#本作品作者吴宇航
                select_block.clear(),select_block.extend(list(random.choice(all_block)))#本作品作者吴宇航
                block_initial_position.clear(),block_initial_position.extend([20,4])#本作品作者吴宇航
                for row,column in select_block:#本作品作者吴宇航
                    if background[row+block_initial_position[0]][column+block_initial_position[1]]:gameover.append(1)#本作品作者吴宇航
        pygame.init()#本作品作者吴宇航
        screen=pygame.display.set_mode((400,800))   #set_mode((400,800)) 修改数值可以修改窗口大小 但第7行和第10行要做相应的改动#本作品作者吴宇航
        while True:#本作品作者吴宇航
            screen.fill((255,255,255))#本作品作者吴宇航
            for event in pygame.event.get():#本作品作者吴宇航
                if event.type==pygame.QUIT:#本作品作者吴宇航
                    pygame.quit()#本作品作者吴宇航
                    fasdasdf1()#本作品作者吴宇航
                elif event.type==pygame.KEYDOWN and event.key==pygame.K_LEFT:move(-1)#本作品作者吴宇航
                elif event.type==pygame.KEYDOWN and event.key==pygame.K_RIGHT:move(1)#本作品作者吴宇航
                elif event.type==pygame.KEYDOWN and event.key==pygame.K_UP:move(0)#本作品作者吴宇航
                elif event.type==pygame.KEYDOWN and event.key==pygame.K_DOWN:press=True#本作品作者吴宇航
                elif event.type==pygame.KEYUP and event.key==pygame.K_DOWN:press=False#本作品作者吴宇航
            if press:times+=10#本作品作者吴宇航
            if times>=50:#本作品作者吴宇航
                move(10)#本作品作者吴宇航
                times=0#本作品作者吴宇航
            else:times+=1#本作品作者吴宇航
            if gameover:sys.exit()#本作品作者吴宇航
            move(100)#本作品作者吴宇航
            pygame.time.Clock().tick(200)   #tick(200)修改数字可以修改游戏的整体速率#本作品作者吴宇航
            pygame.display.flip()#本作品作者吴宇航
         #本作品作者吴宇航
        #记分系统在窗口标题上#本作品作者吴宇航
    elif dakai == "twofour":#本作品作者吴宇航
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
        fangwen("https://livefile.xesimg.com/programme/python_assets/898bc70929aa00fcadb7311fc7f02013.html")#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
    elif dakai == "huarong":#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        FPS = 60#本作品作者吴宇航
        SHAPE = 4         # 棋盘shape#本作品作者吴宇航
        CELL_SIZE = 100   # 方格大小#本作品作者吴宇航
        CELL_GAP_SIZE = 10  # 方格间距#本作品作者吴宇航
        MARGIN = 10  # 方格的margin#本作品作者吴宇航
        PADDING = 10  # 方格的padding#本作品作者吴宇航
        SCREEN_WIDTH = (CELL_SIZE + MARGIN) * SHAPE + MARGIN  # 屏幕宽度#本作品作者吴宇航
        SCREEN_HEIGHT = (CELL_SIZE + MARGIN) * SHAPE + MARGIN  # 屏幕高度#本作品作者吴宇航
#本作品作者吴宇航
        BACKGROUND_COLOR = "#92877d"  # 背景颜色#本作品作者吴宇航
        BACKGROUND_EMPTY_CELL_COLOR = "#9e948a"  # 空方格颜色#本作品作者吴宇航
        BACKGROUND_CELL_COLOR = "#edc22e"  # 方格颜色#本作品作者吴宇航
#本作品作者吴宇航
        # 定义两个元组相加#本作品作者吴宇航
        def tuple_add(t1, t2):#本作品作者吴宇航
            return (t1[0] + t2[0], t1[1] + t2[1])#本作品作者吴宇航
        class Logic:#本作品作者吴宇航
            def __init__(self, shape=4):#本作品作者吴宇航
                self.shape = int(shape) if shape > 2 else 4  # 初始化形状#本作品作者吴宇航
                self.tiles = OrderedDict()  # 初始化数据#本作品作者吴宇航
                self.neighbors = [  # 定义方向矢量#本作品作者吴宇航
                    [1, 0],  # 下#本作品作者吴宇航
                    [-1, 0],  # 上#本作品作者吴宇航
                    [0, 1],  # 右#本作品作者吴宇航
                    [0, -1],  # 左#本作品作者吴宇航
                ]#本作品作者吴宇航
                self.click_dict = {'x': {}, 'y': {}}  # 定义鼠标点击坐标转换下标的数据#本作品作者吴宇航
                self.init_load()  # 初始化加载#本作品作者吴宇航
#本作品作者吴宇航
            def init_load(self):#本作品作者吴宇航
                count = 1#本作品作者吴宇航
                # 生成正确的序列#本作品作者吴宇航
                for x in range(self.shape):#本作品作者吴宇航
                    for y in range(self.shape):#本作品作者吴宇航
                        mark = tuple([x, y])#本作品作者吴宇航
                        self.tiles[mark] = count#本作品作者吴宇航
                        count += 1#本作品作者吴宇航
                self.tiles[mark] = 0#本作品作者吴宇航
#本作品作者吴宇航
                for count in range(1000):  # 随机移动一千次#本作品作者吴宇航
                    neighbor = random.choice(self.neighbors)#本作品作者吴宇航
                    spot = tuple_add(mark, neighbor)#本作品作者吴宇航
#本作品作者吴宇航
                    if spot in self.tiles:#本作品作者吴宇航
                        number = self.tiles[spot]#本作品作者吴宇航
                        self.tiles[spot] = 0#本作品作者吴宇航
                        self.tiles[mark] = number#本作品作者吴宇航
                        mark = spot#本作品作者吴宇航
#本作品作者吴宇航
                self.init_click_dict()#本作品作者吴宇航
#本作品作者吴宇航
            def init_click_dict(self):#本作品作者吴宇航
                # 初始化点击坐标转换下标的数据#本作品作者吴宇航
                for r in range(self.shape):#本作品作者吴宇航
                    for c in range(self.shape):#本作品作者吴宇航
                        x = MARGIN * (c + 1) + c * CELL_SIZE#本作品作者吴宇航
                        x1 = x + CELL_SIZE#本作品作者吴宇航
                        click_x = tuple(range(x, x1))#本作品作者吴宇航
#本作品作者吴宇航
                        self.click_dict['x'][click_x] = c#本作品作者吴宇航
                        y = MARGIN * (r + 1) + r * CELL_SIZE#本作品作者吴宇航
                        y1 = y + CELL_SIZE#本作品作者吴宇航
                        click_y = tuple(range(y, y1))#本作品作者吴宇航
                        self.click_dict['y'][click_y] = r#本作品作者吴宇航
#本作品作者吴宇航
            def move(self, mark):#本作品作者吴宇航
                # 移动数据#本作品作者吴宇航
                for neighbor in self.neighbors:#本作品作者吴宇航
                    spot = tuple_add(mark, neighbor)#本作品作者吴宇航
#本作品作者吴宇航
                    if spot in self.tiles and self.tiles[spot] == 0:#本作品作者吴宇航
                        self.tiles[spot], self.tiles[mark] = self.tiles[#本作品作者吴宇航
                            mark], self.tiles[spot]#本作品作者吴宇航
                        break#本作品作者吴宇航
#本作品作者吴宇航
            def click_to_move(self, x, y):#本作品作者吴宇航
                # 点击移动#本作品作者吴宇航
                x1 = None#本作品作者吴宇航
                for k, v in self.click_dict['x'].items():#本作品作者吴宇航
                    if x in k:#本作品作者吴宇航
                        x1 = v#本作品作者吴宇航
#本作品作者吴宇航
                if x1 is None:#本作品作者吴宇航
                    return#本作品作者吴宇航
                y1 = None#本作品作者吴宇航
                for k, v in self.click_dict['y'].items():#本作品作者吴宇航
                    if y in k:#本作品作者吴宇航
                        y1 = v#本作品作者吴宇航
#本作品作者吴宇航
                if y1 is None:#本作品作者吴宇航
                    return#本作品作者吴宇航
                self.move((y1, x1))#本作品作者吴宇航
#本作品作者吴宇航
            def is_win(self):#本作品作者吴宇航
                # 游戏结束判定#本作品作者吴宇航
                if self.tiles[(self.shape - 1, self.shape - 1)] != 0:#本作品作者吴宇航
                    return False#本作品作者吴宇航
                values = list(self.tiles.values())#本作品作者吴宇航
                for index in range(values.__len__() - 1):#本作品作者吴宇航
                    if index + 1 != values[index]:#本作品作者吴宇航
                        return False#本作品作者吴宇航
                return True#本作品作者吴宇航
        def init_game():#本作品作者吴宇航
            # 初始化游戏#本作品作者吴宇航
            pygame.init()#本作品作者吴宇航
            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))#本作品作者吴宇航
            pygame.display.set_caption('数字华容道 -- 0')#本作品作者吴宇航
            return screen#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        def draw_num(logic, screen):#本作品作者吴宇航
            for r in range(logic.shape):#本作品作者吴宇航
                for c in range(logic.shape):#本作品作者吴宇航
                    num = logic.tiles[(r, c)]#本作品作者吴宇航
                    if num != 0:#本作品作者吴宇航
                        color = pygame.Color(BACKGROUND_CELL_COLOR)#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        color = pygame.Color(BACKGROUND_EMPTY_CELL_COLOR)#本作品作者吴宇航
#本作品作者吴宇航
                    x = MARGIN * (c + 1) + c * CELL_SIZE#本作品作者吴宇航
                    y = MARGIN * (r + 1) + r * CELL_SIZE#本作品作者吴宇航
                    pygame.draw.rect(screen, color, (x, y, CELL_SIZE, CELL_SIZE))#本作品作者吴宇航
                    if num != 0:#本作品作者吴宇航
                        font_size = int((CELL_SIZE - PADDING) / 1.3)#本作品作者吴宇航
                        font = pygame.font.SysFont('arialBlod', font_size)#本作品作者吴宇航
                        font_width, font_height = font.size(str(num))#本作品作者吴宇航
                        screen.blit(font.render(str(num), True, (255, 255, 255)),#本作品作者吴宇航
                                    (x + (CELL_SIZE - font_width) / 2, y +#本作品作者吴宇航
                                     (CELL_SIZE - font_height) / 2 + 5))#本作品作者吴宇航
        def press(is_game_over, logic, COUNT, counts):#本作品作者吴宇航
            for event in pygame.event.get():#本作品作者吴宇航
                if event.type == COUNT and not is_game_over:  # 设置定时器，记录时间#本作品作者吴宇航
                    counts += 1#本作品作者吴宇航
                    pygame.display.set_caption('数字华容道 -- {}'.format(counts))#本作品作者吴宇航
                if event.type == pygame.QUIT:  # 点击关闭按钮退出#本作品作者吴宇航
                    pygame.quit()#本作品作者吴宇航
                    fasdasdf1()#本作品作者吴宇航
                elif event.type == pygame.MOUSEBUTTONUP:  # 鼠标点击#本作品作者吴宇航
                    if event.button == 1 and not is_game_over:#本作品作者吴宇航
                        x, y = event.pos#本作品作者吴宇航
                        logic.click_to_move(int(x), int(y))  # 点击移动#本作品作者吴宇航
                elif event.type == pygame.KEYDOWN and event.key == 13:  # 游戏结束，回车重开#本作品作者吴宇航
                    return True#本作品作者吴宇航
            if COUNT:#本作品作者吴宇航
                return counts#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        def game_win(screen, logic, clock, text='You Win!'):#本作品作者吴宇航
            font = pygame.font.SysFont('Blod', int(SCREEN_WIDTH / 4))#本作品作者吴宇航
            font_width, font_height = font.size(str(text))#本作品作者吴宇航
            while True:#本作品作者吴宇航
                if press(True, logic, None, None):#本作品作者吴宇航
                    break#本作品作者吴宇航
                screen.fill(pygame.Color(BACKGROUND_COLOR))#本作品作者吴宇航
                draw_num(logic, screen)#本作品作者吴宇航
                screen.blit(font.render(str(text), True, (0, 0, 0)),#本作品作者吴宇航
                            ((SCREEN_WIDTH - font_width) / 2,#本作品作者吴宇航
                             (SCREEN_HEIGHT - font_height) / 2))#本作品作者吴宇航
                pygame.display.update()#本作品作者吴宇航
                clock.tick(FPS)#本作品作者吴宇航
        def main():#本作品作者吴宇航
            screen = init_game()#本作品作者吴宇航
            clock = pygame.time.Clock()#本作品作者吴宇航
            logic = Logic(SHAPE)#本作品作者吴宇航
            COUNT = pygame.USEREVENT + 1#本作品作者吴宇航
            pygame.time.set_timer(COUNT, 1000)#本作品作者吴宇航
            seconds = 0  # 记录时间#本作品作者吴宇航
            while True:#本作品作者吴宇航
                if logic.is_win():  # 判断游戏是否胜利#本作品作者吴宇航
                    break#本作品作者吴宇航
                seconds = press(False, logic, COUNT, seconds)  # 监控按键#本作品作者吴宇航
                screen.fill(pygame.Color(BACKGROUND_COLOR))  # 填充背景#本作品作者吴宇航
                draw_num(logic, screen)  # 画数字#本作品作者吴宇航
                pygame.display.update()#本作品作者吴宇航
                clock.tick(FPS)#本作品作者吴宇航
            game_win(screen, logic, clock, text='Time:' + str(seconds))#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        if __name__ == "__main__":#本作品作者吴宇航
            while True:#本作品作者吴宇航
                main()#本作品作者吴宇航
    elif dakai == "shudu":#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        def print_matrix(matrix):#本作品作者吴宇航
            print('—'*19)#本作品作者吴宇航
            for row in matrix:#本作品作者吴宇航
                print('|'+' '.join([str(col) for col in row])+'|')#本作品作者吴宇航
            print('—'*19)#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        def shuffle_number(_list):#本作品作者吴宇航
            random.shuffle(_list)#本作品作者吴宇航
            return _list#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        def check(matrix,i,j,number):#本作品作者吴宇航
            if number in matrix[i]:#本作品作者吴宇航
                return False#本作品作者吴宇航
            if number in [row[j] for row in matrix]:#本作品作者吴宇航
                return False#本作品作者吴宇航
            group_i,group_j = int(i/3),int(j/3)#本作品作者吴宇航
            if number in [matrix[i][j] for i in range(group_i*3,(group_i+1)*3) for j in range(group_j*3,(group_j+1)*3)]:#本作品作者吴宇航
                return False#本作品作者吴宇航
            return True#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        def build_game(matrix,i,j,number):#本作品作者吴宇航
            if i>8 or j>8:#本作品作者吴宇航
                return matrix#本作品作者吴宇航
            if check(matrix,i,j,number):#本作品作者吴宇航
                _matrix = [[col for col in row] for row in matrix]#本作品作者吴宇航
                _matrix[i][j] = number#本作品作者吴宇航
                next_i,next_j = (i+1,0) if j==8 else (i,j+1)#本作品作者吴宇航
                for _number in shuffle_number(number_list):#本作品作者吴宇航
                    #_matrixs.append(build_game(_matrix,next_i,next_j,_number))#本作品作者吴宇航
                    __matrix = build_game(_matrix,next_i,next_j,_number)#本作品作者吴宇航
                    if __matrix and sum([sum(row) for row in __matrix])==(sum(range(1,10))*9):#本作品作者吴宇航
                        return __matrix#本作品作者吴宇航
            #return _matrixs#本作品作者吴宇航
            return None#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        def give_me_a_game(blank_size=9):#本作品作者吴宇航
            matrix_all = build_game(matrix,0,0,random.choice(number_list))#本作品作者吴宇航
            set_ij = set()#本作品作者吴宇航
            while len(list(set_ij))<blank_size:#本作品作者吴宇航
                set_ij.add(str(random.choice([0,1,2,3,4,5,6,7,8]))+','+str(random.choice([0,1,2,3,4,5,6,7,8])))#本作品作者吴宇航
            matrix_blank = [[col for col in row] for row in matrix_all]#本作品作者吴宇航
            blank_ij = []#本作品作者吴宇航
            for ij in list(set_ij):#本作品作者吴宇航
                i,j = int(ij.split(',')[0]),int(ij.split(',')[1])#本作品作者吴宇航
                blank_ij.append((i,j))#本作品作者吴宇航
                matrix_blank[i][j] = 0#本作品作者吴宇航
            return matrix_all,matrix_blank,blank_ij#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        number_list = [1,2,3,4,5,6,7,8,9]#本作品作者吴宇航
        matrix = [([0]*9) for i in range(9)]#本作品作者吴宇航
        if __name__ == "__main__":#本作品作者吴宇航
            print_matrix(build_game(matrix,0,0,random.choice(number_list)))#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        def draw_background():#本作品作者吴宇航
            BG_COLOR = (40, 40, 60)  #本作品作者吴宇航
            screen.fill(BG_COLOR)#本作品作者吴宇航
            pygame.display.set_caption('数独游戏')#本作品作者吴宇航
            pygame.draw.rect(screen, COLORS['black'], (0, 0, 300, 900), 5)#本作品作者吴宇航
            pygame.draw.rect(screen, COLORS['black'], (300, 0, 300, 900), 5)#本作品作者吴宇航
            pygame.draw.rect(screen, COLORS['black'], (600, 0, 300, 900), 5)#本作品作者吴宇航
            pygame.draw.rect(screen, COLORS['black'], (0, 0, 900, 300), 5)#本作品作者吴宇航
            pygame.draw.rect(screen, COLORS['black'], (0, 300, 900, 300), 5)#本作品作者吴宇航
            pygame.draw.rect(screen, COLORS['black'], (0, 600, 900, 300), 5)#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        def draw_choose():#本作品作者吴宇航
            BLOCK_COLOR = (20, 128, 200)  #本作品作者吴宇航
            pygame.draw.rect(screen, BLOCK_COLOR, (cur_j * 100 + 5, cur_i * 100 + 5, 100 - 10, 100 - 10), 0)#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        def check_win(matrix_all, matrix):#本作品作者吴宇航
            if matrix_all == matrix:#本作品作者吴宇航
                return True#本作品作者吴宇航
            return False#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        def check_color(matrix, i, j):#本作品作者吴宇航
            _matrix = [[col for col in row] for row in matrix]#本作品作者吴宇航
            _matrix[i][j] = 0#本作品作者吴宇航
            if check(_matrix, i, j, matrix[i][j]):#本作品作者吴宇航
                return COLORS['green']#本作品作者吴宇航
            return COLORS['red']#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        def draw_number():#本作品作者吴宇航
            for i in range(len(MATRIX)):#本作品作者吴宇航
                for j in range(len(MATRIX[0])):#本作品作者吴宇航
                    _color = check_color(MATRIX, i, j) if (i, j) in BLANK_IJ else COLORS['gray']#本作品作者吴宇航
                    txt = font80.render(str(MATRIX[i][j] if MATRIX[i][j] not in [0, '0'] else ''), True, _color)#本作品作者吴宇航
                    x, y = j * 100 + 30, i * 100 + 10#本作品作者吴宇航
                    screen.blit(txt, (x, y))#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        def draw_context():#本作品作者吴宇航
            txt = font100.render('Blank:' + str(cur_blank_size) + '   Change:' + str(cur_change_size), True, COLORS['black'])#本作品作者吴宇航
            x, y = 10, 900#本作品作者吴宇航
            screen.blit(txt, (x, y))#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        if __name__ == "__main__":#本作品作者吴宇航
#本作品作者吴宇航
            pygame.init()#本作品作者吴宇航
            font80 = pygame.font.SysFont('Times', 80)#本作品作者吴宇航
            font100 = pygame.font.SysFont('Times', 90)#本作品作者吴宇航
            screen = pygame.display.set_mode((900,1000))#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
            cur_i, cur_j = 0, 0#本作品作者吴宇航
            cur_blank_size = 5 #本作品作者吴宇航
            cur_change_size = 0#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
            MATRIX_ANSWER, MATRIX, BLANK_IJ = give_me_a_game(blank_size=cur_blank_size)#本作品作者吴宇航
            print(BLANK_IJ)#本作品作者吴宇航
            print_matrix(MATRIX)#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
            running = True#本作品作者吴宇航
            while running:#本作品作者吴宇航
                for event in pygame.event.get():#本作品作者吴宇航
                    if event.type == pygame.QUIT:#本作品作者吴宇航
                        running = False#本作品作者吴宇航
                        break#本作品作者吴宇航
                    elif event.type == pygame.MOUSEBUTTONDOWN:#本作品作者吴宇航
                        cur_j, cur_i = int(event.pos[0] / 100), int(event.pos[1] / 100)#本作品作者吴宇航
                    elif event.type == event.type == pygame.KEYUP:#本作品作者吴宇航
                        if chr(event.key) in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] and (cur_i, cur_j) in BLANK_IJ:#本作品作者吴宇航
                            MATRIX[cur_i][cur_j] = int(chr(event.key))#本作品作者吴宇航
                            cur_blank_size = sum([1 if col == 0 or col == '0' else 0 for row in MATRIX for col in row])#本作品作者吴宇航
                            cur_change_size += 1#本作品作者吴宇航
                            #本作品作者吴宇航
                draw_background()#本作品作者吴宇航
                draw_choose()#本作品作者吴宇航
                draw_number()#本作品作者吴宇航
                draw_context()#本作品作者吴宇航
                pygame.display.flip()#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
                if check_win(MATRIX_ANSWER, MATRIX):#本作品作者吴宇航
                    print('You win, smarty ass!!!')#本作品作者吴宇航
                    break#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
            pygame.quit()#本作品作者吴宇航
            fasdasdf1()#本作品作者吴宇航
    elif dakai == "shapan":#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        # 设定每一个角色的宽度#本作品作者吴宇航
        image_width = 80#本作品作者吴宇航
        # 屏幕大小宽为8个角色宽度，高为8个角色宽度#本作品作者吴宇航
        width_num = 8#本作品作者吴宇航
        height_num = 9#本作品作者吴宇航
        WIDTH, HEIGHT = width_num * image_width, height_num * image_width#本作品作者吴宇航
        # 初始化方格计数器#本作品作者吴宇航
        counts_x = 0#本作品作者吴宇航
        counts_y = 0#本作品作者吴宇航
        # 初始化标志#本作品作者吴宇航
        flag = 0#本作品作者吴宇航
        # 初始化选中的图形#本作品作者吴宇航
        img_show = 0#本作品作者吴宇航
        # 初始化沙盘，使用字典避免格子重复,字典键为元组，存储空位置，99表示该位置为空，0表示该位置没有汽车#本作品作者吴宇航
        sandbox = {}#本作品作者吴宇航
        for i in range(width_num):#本作品作者吴宇航
            for j in range(height_num - 1):#本作品作者吴宇航
                sandbox[(i, j)] = [99,0]#本作品作者吴宇航
        # 占位计数器，用于将要占据的格子是否为空#本作品作者吴宇航
        count = 0#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        # #字典定义每个物体大小,使用两个数据，代表宽和高#本作品作者吴宇航
        img_size = {0: [2, 2], 1: [1, 1], 2: [1, 1], 3: [2, 2], 4: [3, 3], 5: [3, 3], 6: [3, 3], 7: [1, 1]}#本作品作者吴宇航
#本作品作者吴宇航
        pygame.init()#本作品作者吴宇航
        screen = pygame.display.set_mode((WIDTH, HEIGHT))#本作品作者吴宇航
        # 加载图片#本作品作者吴宇航
        background = pygame.image.load("background.png")#本作品作者吴宇航
        background = pygame.transform.scale(background, (WIDTH, HEIGHT))#本作品作者吴宇航
        img_list = []#本作品作者吴宇航
        for i in range(8):#本作品作者吴宇航
            img = pygame.image.load("{}1.png".format(i)).convert_alpha()#本作品作者吴宇航
            # #加载图片后，调整为需要的方格大小#本作品作者吴宇航
            img = pygame.transform.scale(img, (image_width * img_size[i][0], image_width * img_size[i][1]))#本作品作者吴宇航
            img_list.append(img)#本作品作者吴宇航
#本作品作者吴宇航
        def mouse_square(x, y):#本作品作者吴宇航
            """#本作品作者吴宇航
            判断鼠标位于哪个方格中，x/y为鼠标坐标#本作品作者吴宇航
            """#本作品作者吴宇航
            # 判断鼠标位于哪个方格#本作品作者吴宇航
            conuts_x = (x // image_width)#本作品作者吴宇航
            conuts_y = (y // image_width)#本作品作者吴宇航
            return conuts_x, conuts_y#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        while True:#本作品作者吴宇航
            for event in pygame.event.get():#本作品作者吴宇航
                if event.type == pygame.QUIT:#本作品作者吴宇航
                    pygame.quit()#本作品作者吴宇航
                    fasdasdf1()#本作品作者吴宇航
                if event.type == pygame.MOUSEBUTTONDOWN:#本作品作者吴宇航
                    # 如果鼠标在最下方，将标志设为1，可以拖动图形#本作品作者吴宇航
                    if counts_y == (height_num - 1):#本作品作者吴宇航
                        flag = 1#本作品作者吴宇航
                        # 固定选中的图案不变化#本作品作者吴宇航
                        img_show = counts_x#本作品作者吴宇航
                    # else:#本作品作者吴宇航
                    #     flag = 2#本作品作者吴宇航
                    #     # 如果选中沙盘中的图案进行移动#本作品作者吴宇航
                    #     if (counts_x,counts_y) in sandbox.keys():#本作品作者吴宇航
                    #         img_show = sandbox[(counts_x,counts_y)]#本作品作者吴宇航
                    #         del sandbox[(counts_x,counts_y)]#本作品作者吴宇航
#本作品作者吴宇航
                # 按下鼠标之后检测鼠标抬起#本作品作者吴宇航
                if flag == 1 or flag == 2:#本作品作者吴宇航
                    if event.type == pygame.MOUSEBUTTONUP:#本作品作者吴宇航
                        flag = 3#本作品作者吴宇航
#本作品作者吴宇航
            # 获取鼠标位置，获得格子坐标#本作品作者吴宇航
            x, y = pygame.mouse.get_pos()#本作品作者吴宇航
            counts_x, counts_y = mouse_square(x, y)#本作品作者吴宇航
#本作品作者吴宇航
            screen.blit(background, (0, 0))#本作品作者吴宇航
            # 刷新沙盒中已经放置的图案#本作品作者吴宇航
            for k, values in sandbox.items():#本作品作者吴宇航
                if values[0] < 20:#本作品作者吴宇航
                    screen.blit(img_list[values[0]], (k[0] * image_width, k[1] * image_width))#本作品作者吴宇航
                # #刷新汽车#本作品作者吴宇航
                if values[1] == 1:#本作品作者吴宇航
                    screen.blit(img_list[7], (k[0] * image_width, k[1] * image_width))#本作品作者吴宇航
#本作品作者吴宇航
            # 标志为1或者2时图案跟随鼠标移动#本作品作者吴宇航
            if flag == 1 or flag == 2:#本作品作者吴宇航
                screen.blit(img_list[img_show], (int(x - image_width / 2), int(y - image_width / 2)))#本作品作者吴宇航
#本作品作者吴宇航
            # 标志为3时，表明鼠标松开，将当前位置和选中的图形存储到字典中#本作品作者吴宇航
            elif flag == 3:#本作品作者吴宇航
                # #如果放置的到沙盘外，取消之#本作品作者吴宇航
                if ((counts_y + img_size[img_show][1])<height_num)  and ((counts_x + img_size[img_show][0])<(width_num+1)):#本作品作者吴宇航
                    #判断所有要填入的格子是否为空#本作品作者吴宇航
                    for i in range(img_size[img_show][0]):#本作品作者吴宇航
                        for j in range(img_size[img_show][1]):#本作品作者吴宇航
                            if sandbox[(counts_x + i, counts_y + j)][0] == 99:#本作品作者吴宇航
                                count += 1#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
                    # #如果所有要占据的格子都为空，那么填充沙盘#本作品作者吴宇航
                    if img_show != 7:#本作品作者吴宇航
                        if count ==  img_size[img_show][0]**2:#本作品作者吴宇航
                            for i in range(img_size[img_show][0]):#本作品作者吴宇航
                                for j in range(img_size[img_show][1]):#本作品作者吴宇航
                                    if i or j:#本作品作者吴宇航
                                        sandbox[(counts_x + i, counts_y + j)][0] = img_show + 20#本作品作者吴宇航
                            sandbox[(counts_x, counts_y)][0] = img_show#本作品作者吴宇航
                    else:#本作品作者吴宇航
                    # #汽车只能放置在路上#本作品作者吴宇航
                        if  sandbox[(counts_x, counts_y)][0] == 1:#本作品作者吴宇航
                            sandbox[(counts_x, counts_y)][1] = 1#本作品作者吴宇航
                    count = 0#本作品作者吴宇航
#本作品作者吴宇航
                # 初始化标志#本作品作者吴宇航
                flag = 0#本作品作者吴宇航
            # print(sandbox)#本作品作者吴宇航
            pygame.display.flip()#本作品作者吴宇航
            pygame.time.Clock().tick(120)#本作品作者吴宇航
    elif dakai == "flybird":#本作品作者吴宇航
        num=0#本作品作者吴宇航
        score=0#本作品作者吴宇航
        #本作品作者吴宇航
        class Bird(object):#本作品作者吴宇航
            #本作品作者吴宇航
            def __init__(self):#本作品作者吴宇航
                self.birdRect=pygame.Rect(65,50,50,50)#本作品作者吴宇航
                a=random.choice([1,4,7])#本作品作者吴宇航
                self.birdStatus=[pygame.image.load(str(a)+".png"),#本作品作者吴宇航
                                pygame.image.load(str(a+1)+".png"),#本作品作者吴宇航
                                pygame.image.load(str(a+2)+".png")]#本作品作者吴宇航
                self.dead=False#本作品作者吴宇航
                self.status=0#本作品作者吴宇航
                self.birdX=120#本作品作者吴宇航
                self.birdY=350#本作品作者吴宇航
                self.jump=False#本作品作者吴宇航
                self.jumpSpeed=10#本作品作者吴宇航
                self.gravity=5#本作品作者吴宇航
                #本作品作者吴宇航
                #本作品作者吴宇航
            def birdUpdate(self):#本作品作者吴宇航
                global num#本作品作者吴宇航
                num1 = 0#本作品作者吴宇航
                self.birdStatus#本作品作者吴宇航
                num1+=1#本作品作者吴宇航
                self.status=num1%3#本作品作者吴宇航
                if self.jump:#本作品作者吴宇航
                    self.jumpSpeed-=0.5#本作品作者吴宇航
                    self.birdY-=self.jumpSpeed#本作品作者吴宇航
                else:#本作品作者吴宇航
                    self.gravity+=0.2#本作品作者吴宇航
                    self.birdY+=self.gravity#本作品作者吴宇航
                    #本作品作者吴宇航
                self.birdRect[1]=self.birdY#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        class Pipeline(object):#本作品作者吴宇航
#本作品作者吴宇航
            def __init__(self):#本作品作者吴宇航
                self.wallx=400#本作品作者吴宇航
                self.wally=random.randint(-100,0)#本作品作者吴宇航
                s=random.randint(1,2)#本作品作者吴宇航
                aUp=pygame.image.load("p"+str(s)+".png")#本作品作者吴宇航
                self.pineUp=pygame.transform.flip(aUp,False,True)#本作品作者吴宇航
                self.pineDown=pygame.image.load("p"+str(s)+".png")#本作品作者吴宇航
#本作品作者吴宇航
                #本作品作者吴宇航
            def updatePipeline(self):#本作品作者吴宇航
                global score#本作品作者吴宇航
                global score1#本作品作者吴宇航
                score1 = 0#本作品作者吴宇航
#本作品作者吴宇航
                self.wallx-=5#本作品作者吴宇航
                if self.wallx==20 and not Bird.dead:#本作品作者吴宇航
                    score1+=1#本作品作者吴宇航
                    #本作品作者吴宇航
                if self.wallx<-80:#本作品作者吴宇航
                    self.wally=random.randint(-100,0)#本作品作者吴宇航
                    self.wallx=400#本作品作者吴宇航
                    #本作品作者吴宇航
#本作品作者吴宇航
        def createMap():#本作品作者吴宇航
            #本作品作者吴宇航
            screen.fill((255,255,255))#本作品作者吴宇航
            screen.blit(background,(0,0)) #本作品作者吴宇航
            #管道#本作品作者吴宇航
            screen.blit(Pipeline.pineUp,(Pipeline.wallx,Pipeline.wally))#本作品作者吴宇航
            screen.blit(Pipeline.pineDown,(Pipeline.wallx,Pipeline.wally+500))#本作品作者吴宇航
            Pipeline.updatePipeline()#本作品作者吴宇航
            #鸟#本作品作者吴宇航
            if Bird.dead:#本作品作者吴宇航
                Bird.status=2#本作品作者吴宇航
            screen.blit(Bird.birdStatus[Bird.status],(Bird.birdX,Bird.birdY))#本作品作者吴宇航
            Bird.birdUpdate()#本作品作者吴宇航
            #分数#本作品作者吴宇航
#本作品作者吴宇航
            # screen.blit(font.render(str(score1),-1,(255,255,255)),(190,50))#本作品作者吴宇航
            pygame.display.update()#本作品作者吴宇航
#本作品作者吴宇航
        def checkDead():#本作品作者吴宇航
            upRect=pygame.Rect(Pipeline.wallx,Pipeline.wally,Pipeline.pineDown.get_width()-20,Pipeline.pineDown.get_height()-5)#本作品作者吴宇航
            downRect=pygame.Rect(Pipeline.wallx,Pipeline.wally+500,Pipeline.pineDown.get_width()-20,Pipeline.pineDown.get_height()-5)#本作品作者吴宇航
            if upRect.colliderect(Bird.birdRect) or downRect.colliderect(Bird.birdRect):#本作品作者吴宇航
                Bird.dead=True#本作品作者吴宇航
            if not 0<Bird.birdRect[1]<height:#本作品作者吴宇航
                Bird.dead=True#本作品作者吴宇航
                #本作品作者吴宇航
                return True#本作品作者吴宇航
            else:#本作品作者吴宇航
                return False#本作品作者吴宇航
#本作品作者吴宇航
        def getResult():#本作品作者吴宇航
            final_text1="Good game"#本作品作者吴宇航
            final_text2="Your final score is:"+str(score1)#本作品作者吴宇航
            ft1_font=pygame.font.SysFont("微软雅黑",70)#本作品作者吴宇航
            ft1_surf=font.render(final_text1,1,(242,3,36))#本作品作者吴宇航
            ft2_font=pygame.font.SysFont("微软雅黑",50)#本作品作者吴宇航
            ft2_surf=font.render(final_text2,1,(253,177,6))#本作品作者吴宇航
            screen.blit(ft1_surf,[(screen.get_width()-ft1_surf.get_width())/2,100])#本作品作者吴宇航
            # screen.blit(ft2_surf,[(screen.get_width()-ft2_surf.get_width())/2,200])#本作品作者吴宇航
            pygame.display.flip()#本作品作者吴宇航
        ###本作品作者吴宇航
        def nice(emoji_str):#本作品作者吴宇航
            return ''.join(c if c <= '\uffff' else ''.join(chr(x) for x in struct.unpack('>2H', c.encode('utf-16be'))) for c in emoji_str)#本作品作者吴宇航
        def run_app(pid):#本作品作者吴宇航
            pid=pid.split("&")[1].split("=")[1]#本作品作者吴宇航
            import requests,time,random,os#本作品作者吴宇航
            def load(url,name):#本作品作者吴宇航
                import requests as req#本作品作者吴宇航
                response = req.get(url)#本作品作者吴宇航
                try:#本作品作者吴宇航
                    a=open(name,"wb")#本作品作者吴宇航
                    a.write(response.content)#本作品作者吴宇航
                    a.close()#本作品作者吴宇航
                except:#本作品作者吴宇航
                    a=open(name,"w")#本作品作者吴宇航
                    a.write(response.text)#本作品作者吴宇航
                    a.close()#本作品作者吴宇航
            def enter(k):#本作品作者吴宇航
                url="http://code.xueersi.com/api/compilers/"+k+"?id="+k#本作品作者吴宇航
                headers = {'Content-Type':'application/json'}#本作品作者吴宇航
                a=requests.get(url=url, headers=headers)#本作品作者吴宇航
                z=eval(a.text.replace("false","False").replace("true","True").replace("null","None"))#本作品作者吴宇航
                return nice(z["data"]["xml"])#本作品作者吴宇航
            def load_img(k):#本作品作者吴宇航
                url="http://code.xueersi.com/api/compilers/"+k+"?id="+k#本作品作者吴宇航
                headers = {'Content-Type':'application/json'}#本作品作者吴宇航
                a=requests.get(url=url, headers=headers)#本作品作者吴宇航
                z=eval(a.text.replace("false","False").replace("true","True").replace("null","None"))#本作品作者吴宇航
#本作品作者吴宇航
                k=z["data"]["assets"]["assets"]#本作品作者吴宇航
                for x in k:#本作品作者吴宇航
                    load(("https://livefile.xesimg.com/programme/python_assets/"+x["md5ext"]),x["name"])#本作品作者吴宇航
            import time#本作品作者吴宇航
            load_img(pid)#本作品作者吴宇航
            time.sleep(1)#本作品作者吴宇航
            clear_os()#本作品作者吴宇航
            #本作品作者吴宇航
            return enter(pid)#本作品作者吴宇航
        def clear_os():#本作品作者吴宇航
            import sys#本作品作者吴宇航
            sys.stdout.write("\033[2J\033[00H")#本作品作者吴宇航
        ###本作品作者吴宇航
            #本作品作者吴宇航
        flag=True#本作品作者吴宇航
        if __name__=="__main__":#本作品作者吴宇航
            #本作品作者吴宇航
            pygame.init()#本作品作者吴宇航
            font=pygame.font.SysFont(None,50)#本作品作者吴宇航
            size=width,height=400,650#本作品作者吴宇航
            screen=pygame.display.set_mode(size)#本作品作者吴宇航
            pygame.display.set_caption("小饼干")#本作品作者吴宇航
            clock=pygame.time.Clock()#本作品作者吴宇航
            Pipeline=Pipeline()#本作品作者吴宇航
            Bird=Bird()#本作品作者吴宇航
            #本作品作者吴宇航
            #本作品作者吴宇航
            ss=random.randint(1,2)#本作品作者吴宇航
            #本作品作者吴宇航
            key=False#本作品作者吴宇航
            while True:#本作品作者吴宇航
                clock.tick(60)#本作品作者吴宇航
                for event in pygame.event.get():#本作品作者吴宇航
                    if event.type==pygame.QUIT:#本作品作者吴宇航
                        pygame.quit()#本作品作者吴宇航
                        fasdasdf1()#本作品作者吴宇航
                    if(event.type==pygame.KEYDOWN or event.type==pygame.MOUSEBUTTONDOWN) and not Bird.dead:#本作品作者吴宇航
                        key =True#本作品作者吴宇航
                        Bird.jump=True#本作品作者吴宇航
                        Bird.gravity=5#本作品作者吴宇航
                        Bird.jumpSpeed=10#本作品作者吴宇航
                if key:#本作品作者吴宇航
                    background=pygame.image.load("bg"+str(ss)+".png")#本作品作者吴宇航
                    background=pygame.transform.scale(background,(400,650))#本作品作者吴宇航
                    if checkDead():#本作品作者吴宇航
                        getResult()#本作品作者吴宇航
                        if flag:#本作品作者吴宇航
                            #本作品作者吴宇航
                            flag=not flag#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        createMap()#本作品作者吴宇航
                else:#本作品作者吴宇航
                    a=pygame.image.load("bg"+str(ss)+".png")#本作品作者吴宇航
                    background1=pygame.transform.scale(a,(400,650))#本作品作者吴宇航
                    b=pygame.image.load("message.png")#本作品作者吴宇航
                    background=pygame.transform.scale(b,(184,267))#本作品作者吴宇航
                    screen.blit(background1,(0,0))#本作品作者吴宇航
                    screen.blit(background,((400-184)/2,(650-267)/2))#本作品作者吴宇航
                    screen.blit(Bird.birdStatus[Bird.status],(Bird.birdX,Bird.birdY))#本作品作者吴宇航
                    pygame.display.update()#本作品作者吴宇航
            #本作品作者吴宇航
    elif dakai == "huihua":#本作品作者吴宇航
        #本作品作者吴宇航
        #本作品作者吴宇航
#本作品作者吴宇航
        # 2011/08/27 Version 1, first imported#本作品作者吴宇航
#本作品作者吴宇航
        class Brush():#本作品作者吴宇航
         def __init__(self, screen):#本作品作者吴宇航
          self.screen = screen#本作品作者吴宇航
          self.color = (0, 0, 0)#本作品作者吴宇航
          self.size = 1#本作品作者吴宇航
          self.drawing = False#本作品作者吴宇航
          self.last_pos = None#本作品作者吴宇航
          self.space = 1#本作品作者吴宇航
          # if style is True, normal solid brush#本作品作者吴宇航
          # if style is False, png brush#本作品作者吴宇航
          self.style = False#本作品作者吴宇航
          # load brush style png#本作品作者吴宇航
          self.brush = pygame.image.load("brush.png").convert_alpha()#本作品作者吴宇航
          # set the current brush depends on size#本作品作者吴宇航
          self.brush_now = self.brush.subsurface((0,0), (1, 1))#本作品作者吴宇航
#本作品作者吴宇航
         def start_draw(self, pos):#本作品作者吴宇航
          self.drawing = True#本作品作者吴宇航
          self.last_pos = pos#本作品作者吴宇航
         def end_draw(self):#本作品作者吴宇航
          self.drawing = False#本作品作者吴宇航
#本作品作者吴宇航
         def set_brush_style(self, style):#本作品作者吴宇航
          if style == True:#本作品作者吴宇航
            print('已开启刷子')#本作品作者吴宇航
          if style == False:#本作品作者吴宇航
            print('已关闭刷子')#本作品作者吴宇航
          self.style = style#本作品作者吴宇航
         def get_brush_style(self):#本作品作者吴宇航
          return self.style#本作品作者吴宇航
#本作品作者吴宇航
         def get_current_brush(self):#本作品作者吴宇航
          return self.brush_now#本作品作者吴宇航
#本作品作者吴宇航
         def set_size(self, size):#本作品作者吴宇航
          if size < 1: size = 1#本作品作者吴宇航
          elif size > 32: size = 32#本作品作者吴宇航
          print("设置画笔大小为", size)#本作品作者吴宇航
          self.size = size#本作品作者吴宇航
          self.brush_now = self.brush.subsurface((0,0), (size*2, size*2))#本作品作者吴宇航
         def get_size(self):#本作品作者吴宇航
          return self.size#本作品作者吴宇航
#本作品作者吴宇航
         def set_color(self, color):#本作品作者吴宇航
          self.color = color#本作品作者吴宇航
          for i in range(self.brush.get_width()):#本作品作者吴宇航
           for j in range(self.brush.get_height()):#本作品作者吴宇航
            self.brush.set_at((i, j),#本作品作者吴宇航
              color + (self.brush.get_at((i, j)).a,))#本作品作者吴宇航
         def get_color(self):#本作品作者吴宇航
          return self.color#本作品作者吴宇航
#本作品作者吴宇航
         def draw(self, pos):#本作品作者吴宇航
          if self.drawing:#本作品作者吴宇航
           for p in self._get_points(pos):#本作品作者吴宇航
            # draw eveypoint between them#本作品作者吴宇航
            if self.style == False:#本作品作者吴宇航
             pygame.draw.circle(self.screen, self.color, p, self.size)#本作品作者吴宇航
            else:#本作品作者吴宇航
             self.screen.blit(self.brush_now, p)#本作品作者吴宇航
#本作品作者吴宇航
           self.last_pos = pos#本作品作者吴宇航
#本作品作者吴宇航
         def _get_points(self, pos):#本作品作者吴宇航
          """ Get all points between last_point ~ now_point. """#本作品作者吴宇航
          points = [ (self.last_pos[0], self.last_pos[1]) ]#本作品作者吴宇航
          len_x = pos[0] - self.last_pos[0]#本作品作者吴宇航
          len_y = pos[1] - self.last_pos[1]#本作品作者吴宇航
          length = sqrt(len_x ** 2 + len_y ** 2)#本作品作者吴宇航
          step_x = len_x / length#本作品作者吴宇航
          step_y = len_y / length#本作品作者吴宇航
          for i in range(int(length)):#本作品作者吴宇航
           points.append(#本作品作者吴宇航
             (points[-1][0] + step_x, points[-1][1] + step_y))#本作品作者吴宇航
          points = map(lambda x:(int(0.5+x[0]), int(0.5+x[1])), points)#本作品作者吴宇航
          # return light-weight, uniq integer point list#本作品作者吴宇航
          return list(set(points))#本作品作者吴宇航
#本作品作者吴宇航
        class Menu():#本作品作者吴宇航
         def __init__(self, screen):#本作品作者吴宇航
          self.screen = screen#本作品作者吴宇航
          self.brush = None#本作品作者吴宇航
          self.colors = [#本作品作者吴宇航
            (0xff, 0x00, 0xff), (0x80, 0x00, 0x80),#本作品作者吴宇航
            (0x00, 0x00, 0xff), (0x00, 0x00, 0x80),#本作品作者吴宇航
            (0x00, 0xff, 0xff), (0x00, 0x80, 0x80),#本作品作者吴宇航
            (0x00, 0xff, 0x00), (0x00, 0x80, 0x00),#本作品作者吴宇航
            (0xff, 0xff, 0x00), (0x80, 0x80, 0x00),#本作品作者吴宇航
            (0xff, 0x00, 0x00), (0x80, 0x00, 0x00),#本作品作者吴宇航
            (0xc0, 0xc0, 0xc0), (0xff, 0xff, 0xff),#本作品作者吴宇航
            (0x00, 0x00, 0x00), (0x80, 0x80, 0x80),#本作品作者吴宇航
           ]#本作品作者吴宇航
          self.colors_rect = []#本作品作者吴宇航
          for (i, rgb) in enumerate(self.colors):#本作品作者吴宇航
           rect = pygame.Rect(10 + i % 2 * 32, 254 + i / 2 * 32, 32, 32)#本作品作者吴宇航
           self.colors_rect.append(rect)#本作品作者吴宇航
#本作品作者吴宇航
          self.pens = [#本作品作者吴宇航
            pygame.image.load("pen1.png").convert_alpha(),#本作品作者吴宇航
            pygame.image.load("brush.png").convert_alpha()#本作品作者吴宇航
           ]#本作品作者吴宇航
          self.pens_rect = []#本作品作者吴宇航
          for (i, img) in enumerate(self.pens):#本作品作者吴宇航
           rect = pygame.Rect(10, 10 + i * 64, 64, 64)#本作品作者吴宇航
           self.pens_rect.append(rect)#本作品作者吴宇航
#本作品作者吴宇航
          self.sizes = [#本作品作者吴宇航
            pygame.image.load("big.png").convert_alpha(),#本作品作者吴宇航
            pygame.image.load("small.png").convert_alpha()#本作品作者吴宇航
           ]#本作品作者吴宇航
          self.sizes_rect = []#本作品作者吴宇航
          for (i, img) in enumerate(self.sizes):#本作品作者吴宇航
           rect = pygame.Rect(10 + i * 32, 138, 32, 32)#本作品作者吴宇航
           self.sizes_rect.append(rect)#本作品作者吴宇航
#本作品作者吴宇航
         def set_brush(self, brush):#本作品作者吴宇航
          self.brush = brush#本作品作者吴宇航
#本作品作者吴宇航
         def draw(self):#本作品作者吴宇航
          # draw pen style button#本作品作者吴宇航
          for (i, img) in enumerate(self.pens):#本作品作者吴宇航
           self.screen.blit(img, self.pens_rect[i].topleft)#本作品作者吴宇航
          # draw < > buttons#本作品作者吴宇航
          for (i, img) in enumerate(self.sizes):#本作品作者吴宇航
           self.screen.blit(img, self.sizes_rect[i].topleft)#本作品作者吴宇航
          # draw current pen / color#本作品作者吴宇航
          self.screen.fill((255, 255, 255), (10, 180, 64, 64))#本作品作者吴宇航
          pygame.draw.rect(self.screen, (0, 0, 0), (10, 180, 64, 64), 1)#本作品作者吴宇航
          size = self.brush.get_size()#本作品作者吴宇航
          x = 10 + 32#本作品作者吴宇航
          y = 180 + 32#本作品作者吴宇航
          if self.brush.get_brush_style():#本作品作者吴宇航
           x = x - size#本作品作者吴宇航
           y = y - size#本作品作者吴宇航
           self.screen.blit(self.brush.get_current_brush(), (x, y))#本作品作者吴宇航
          else:#本作品作者吴宇航
           pygame.draw.circle(self.screen,#本作品作者吴宇航
             self.brush.get_color(), (x, y), size)#本作品作者吴宇航
          # draw colors panel#本作品作者吴宇航
          for (i, rgb) in enumerate(self.colors):#本作品作者吴宇航
           pygame.draw.rect(self.screen, rgb, self.colors_rect[i])#本作品作者吴宇航
#本作品作者吴宇航
         def click_button(self, pos):#本作品作者吴宇航
          # pen buttons#本作品作者吴宇航
          for (i, rect) in enumerate(self.pens_rect):#本作品作者吴宇航
           if rect.collidepoint(pos):#本作品作者吴宇航
            self.brush.set_brush_style(bool(i))#本作品作者吴宇航
            return True#本作品作者吴宇航
          # size buttons#本作品作者吴宇航
          for (i, rect) in enumerate(self.sizes_rect):#本作品作者吴宇航
           if rect.collidepoint(pos):#本作品作者吴宇航
            if i: # i == 1, size down#本作品作者吴宇航
             self.brush.set_size(self.brush.get_size() - 1)#本作品作者吴宇航
            else:#本作品作者吴宇航
             self.brush.set_size(self.brush.get_size() + 1)#本作品作者吴宇航
            return True#本作品作者吴宇航
          # color buttons#本作品作者吴宇航
          for (i, rect) in enumerate(self.colors_rect):#本作品作者吴宇航
           if rect.collidepoint(pos):#本作品作者吴宇航
            self.brush.set_color(self.colors[i])#本作品作者吴宇航
            return True#本作品作者吴宇航
          return False#本作品作者吴宇航
#本作品作者吴宇航
        class Painter():#本作品作者吴宇航
         def __init__(self):#本作品作者吴宇航
          self.screen = pygame.display.set_mode((800, 600))#本作品作者吴宇航
          pygame.display.set_caption("Pygame画板")#本作品作者吴宇航
          self.clock = pygame.time.Clock()#本作品作者吴宇航
          self.brush = Brush(self.screen)#本作品作者吴宇航
          self.menu = Menu(self.screen)#本作品作者吴宇航
          self.menu.set_brush(self.brush)#本作品作者吴宇航
#本作品作者吴宇航
         def run(self):#本作品作者吴宇航
          self.screen.fill((255, 255, 255))#本作品作者吴宇航
          while True:#本作品作者吴宇航
           # max fps limit#本作品作者吴宇航
           self.clock.tick(30)#本作品作者吴宇航
           for event in pygame.event.get():#本作品作者吴宇航
            if event.type == QUIT:#本作品作者吴宇航
             return#本作品作者吴宇航
            elif event.type == KEYDOWN:#本作品作者吴宇航
             # press esc to clear screen#本作品作者吴宇航
             if event.key == K_ESCAPE:#本作品作者吴宇航
              self.screen.fill((255, 255, 255))#本作品作者吴宇航
            elif event.type == MOUSEBUTTONDOWN:#本作品作者吴宇航
             # <= 74, coarse judge here can save much time#本作品作者吴宇航
             if ((event.pos)[0] <= 74 and#本作品作者吴宇航
               self.menu.click_button(event.pos)):#本作品作者吴宇航
              # if not click on a functional button, do drawing#本作品作者吴宇航
              pass#本作品作者吴宇航
             else:#本作品作者吴宇航
              self.brush.start_draw(event.pos)#本作品作者吴宇航
            elif event.type == MOUSEMOTION:#本作品作者吴宇航
             self.brush.draw(event.pos)#本作品作者吴宇航
            elif event.type == MOUSEBUTTONUP:#本作品作者吴宇航
             self.brush.end_draw()#本作品作者吴宇航
#本作品作者吴宇航
           self.menu.draw()#本作品作者吴宇航
           pygame.display.update()#本作品作者吴宇航
#本作品作者吴宇航
        if __name__ == '__main__':#本作品作者吴宇航
         app = Painter()#本作品作者吴宇航
         app.run()#本作品作者吴宇航
         fasdasdf1()#本作品作者吴宇航
    elif dakai == "wenben":#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        app = wx.App()#本作品作者吴宇航
        win = wx.Frame(None, title="TXT Editor", size=(1000, 666))#本作品作者吴宇航
#本作品作者吴宇航
        bkg = wx.Panel(win)#本作品作者吴宇航
#本作品作者吴宇航
        def openFile(evt):#本作品作者吴宇航
            dlg = wx.FileDialog(#本作品作者吴宇航
                win,#本作品作者吴宇航
                "Open",#本作品作者吴宇航
                "",#本作品作者吴宇航
                "",#本作品作者吴宇航
                "All files (*.*)|*.*",#本作品作者吴宇航
                wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)#本作品作者吴宇航
            filepath = ''#本作品作者吴宇航
            if dlg.ShowModal() == wx.ID_OK:#本作品作者吴宇航
                filepath = dlg.GetPath()#本作品作者吴宇航
            else:#本作品作者吴宇航
                return#本作品作者吴宇航
            filename.SetValue(filepath)#本作品作者吴宇航
            fopen = open(filepath)#本作品作者吴宇航
            fcontent = fopen.read()#本作品作者吴宇航
            contents.SetValue(fcontent)#本作品作者吴宇航
            fopen.close()#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        def saveFile(evt):#本作品作者吴宇航
#本作品作者吴宇航
            fcontent = contents.GetValue()#本作品作者吴宇航
            fopen = open(filename.GetValue(), 'w')#本作品作者吴宇航
            fopen.write(fcontent)#本作品作者吴宇航
            fopen.close()#本作品作者吴宇航
            win = wx.Frame(None, title='TXT Editor')#本作品作者吴宇航
            button = wx.Button(win, label='保存成功')#本作品作者吴宇航
            win.Show()#本作品作者吴宇航
#本作品作者吴宇航
        openBtn = wx.Button(bkg, label='浏览')#本作品作者吴宇航
        openBtn.Bind(wx.EVT_BUTTON, openFile)#本作品作者吴宇航
#本作品作者吴宇航
        saveBtn = wx.Button(bkg, label='保存')#本作品作者吴宇航
        saveBtn.Bind(wx.EVT_BUTTON, saveFile)#本作品作者吴宇航
#本作品作者吴宇航
        filename = wx.TextCtrl(bkg, style=wx.TE_READONLY)#本作品作者吴宇航
        contents = wx.TextCtrl(bkg, style=wx.TE_MULTILINE)#本作品作者吴宇航
#本作品作者吴宇航
        hbox = wx.BoxSizer()#本作品作者吴宇航
        hbox.Add(openBtn, proportion=0, flag=wx.LEFT | wx.ALL, border=5)#本作品作者吴宇航
        hbox.Add(filename, proportion=1, flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=5)#本作品作者吴宇航
        hbox.Add(saveBtn, proportion=0, flag=wx.LEFT | wx.ALL, border=5)#本作品作者吴宇航
#本作品作者吴宇航
        bbox = wx.BoxSizer(wx.VERTICAL)#本作品作者吴宇航
        bbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.ALL)#本作品作者吴宇航
        bbox.Add(contents, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)#本作品作者吴宇航
#本作品作者吴宇航
        bkg.SetSizer(bbox)#本作品作者吴宇航
        win.Show()#本作品作者吴宇航
        app.MainLoop()#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
        # #新建根窗口#本作品作者吴宇航
        # root=Tk()#本作品作者吴宇航
        # #新建Menu实例#本作品作者吴宇航
        # menu_bar=Menu(root)#本作品作者吴宇航
        # file_menu=Menu(menu_bar,tearoff=0)#本作品作者吴宇航
        # edit_menu=Menu(menu_bar,tearoff=0)#本作品作者吴宇航
        # view_menu=Menu(menu_bar,tearoff=0)#本作品作者吴宇航
        # about_menu=Menu(menu_bar,tearoff=0)#本作品作者吴宇航
        # themes_menu=Menu(menu_bar,tearoff=0)#本作品作者吴宇航
         #本作品作者吴宇航
        # file_name = None#本作品作者吴宇航
        # #获取文本行数#本作品作者吴宇航
        # def get_line_numbers():#本作品作者吴宇航
        #     output = ''#本作品作者吴宇航
        #     if show_line_number.get():#本作品作者吴宇航
        #         row, col = content_text.index("end").split('.')#本作品作者吴宇航
        #         for i in range(1, int(row)):#本作品作者吴宇航
        #             output +=str(i)+ '\n'#本作品作者吴宇航
        #     return output#本作品作者吴宇航
        # #更新文本行数#本作品作者吴宇航
        # def update_line_numbers(event = None):#本作品作者吴宇航
        #     line_numbers = get_line_numbers()#本作品作者吴宇航
        #     line_number_bar.config(state='normal')#本作品作者吴宇航
        #     line_number_bar.delete('1.0', 'end')#本作品作者吴宇航
        #     line_number_bar.insert('1.0', line_numbers)#本作品作者吴宇航
        #     line_number_bar.config(state='disabled')#本作品作者吴宇航
        # #高亮当前行    #本作品作者吴宇航
        # def highlight_line(interval=100):#本作品作者吴宇航
        #     content_text.tag_remove("active_line", 1.0, "end")#本作品作者吴宇航
        #     content_text.tag_add("active_line", "insert linestart", "insert lineend+1c")#本作品作者吴宇航
        #     content_text.after(interval, toggle_highlight)#本作品作者吴宇航
        # #非高亮当前行    #本作品作者吴宇航
        # def undo_highlight():#本作品作者吴宇航
        #     content_text.tag_remove("active_line", 1.0, "end")#本作品作者吴宇航
        # #高亮状态切换#本作品作者吴宇航
        # def toggle_highlight(event=None):#本作品作者吴宇航
        #     if to_highlight_line.get():#本作品作者吴宇航
        #         highlight_line()#本作品作者吴宇航
        #     else:#本作品作者吴宇航
        #         undo_highlight()#本作品作者吴宇航
        # #显示光标信息#本作品作者吴宇航
        # def show_cursor_info_bar():#本作品作者吴宇航
        #     show_cursor_info_checked = show_cursor_info.get()#本作品作者吴宇航
        #     if show_cursor_info_checked:#本作品作者吴宇航
        #         cursor_info_bar.pack(expand='no', fill=None, side='right', anchor='se')#本作品作者吴宇航
        #     else:#本作品作者吴宇航
        #         cursor_info_bar.pack_forget()#本作品作者吴宇航
        # #更新光标信息#本作品作者吴宇航
        # def update_cursor_info_bar(event=None):#本作品作者吴宇航
        #     row, col = content_text.index(INSERT).split('.')#本作品作者吴宇航
        #     line_num, col_num = str(int(row)), str(int(col)+1) #本作品作者吴宇航
        #     infotext = "Line: {0} | Column: {1}".format(line_num, col_num)#本作品作者吴宇航
        #     cursor_info_bar.config(text=infotext)#本作品作者吴宇航
        # #当文本内容改变时触发#本作品作者吴宇航
        # def on_content_changed(event=None):#本作品作者吴宇航
        #     update_line_numbers()#本作品作者吴宇航
        #     update_cursor_info_bar()#本作品作者吴宇航
        # #打开文件#本作品作者吴宇航
        # def open_file(event=None):#本作品作者吴宇航
        #     input_file_name=tkinter.filedialog.askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents","*.txt")])#本作品作者吴宇航
        #     if input_file_name:#本作品作者吴宇航
        #         global file_name#本作品作者吴宇航
        #         file_name = input_file_name#本作品作者吴宇航
        #         root.title('{} - {}'.format(os.path.basename(file_name), PROGRAM_NAME))#本作品作者吴宇航
        #         content_text.delete(1.0, END)#本作品作者吴宇航
        #         with open(file_name,encoding = "utf-8") as _file:#本作品作者吴宇航
        #             content_text.insert(1.0, _file.read())#本作品作者吴宇航
        #         on_content_changed()#本作品作者吴宇航
        # #保存文件#本作品作者吴宇航
        # def save(event=None):#本作品作者吴宇航
        #     global file_name#本作品作者吴宇航
        #     if not file_name:#本作品作者吴宇航
        #         save_as()#本作品作者吴宇航
        #     else:#本作品作者吴宇航
        #         write_to_file(file_name)#本作品作者吴宇航
        #     return "break"#本作品作者吴宇航
        # #保存文件为#本作品作者吴宇航
        # def save_as(event=None):#本作品作者吴宇航
        #     input_file_name = tkinter.filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])#本作品作者吴宇航
        #     if input_file_name:#本作品作者吴宇航
        #         global file_name#本作品作者吴宇航
        #         file_name = input_file_name#本作品作者吴宇航
        #         write_to_file(file_name)#本作品作者吴宇航
        #         root.title('{} - {}'.format(os.path.basename(file_name),PROGRAM_NAME))#本作品作者吴宇航
        #     return "break"#本作品作者吴宇航
        # #写入磁盘#本作品作者吴宇航
        # def write_to_file(file_name):#本作品作者吴宇航
        #     try:#本作品作者吴宇航
        #         content = content_text.get(1.0, 'end')#本作品作者吴宇航
        #         with open(file_name, 'w') as the_file:#本作品作者吴宇航
        #             the_file.write(content)#本作品作者吴宇航
        #     except IOError:#本作品作者吴宇航
        #         pass#本作品作者吴宇航
        # #新建文件#本作品作者吴宇航
        # def new_file(event=None):#本作品作者吴宇航
        #     root.title("Untitled")#本作品作者吴宇航
        #     global file_name#本作品作者吴宇航
        #     file_name = None#本作品作者吴宇航
        #     content_text.delete(1.0,END)#本作品作者吴宇航
        #     on_content_changed()#本作品作者吴宇航
        # #退出编辑器#本作品作者吴宇航
        # def exit_editor(event=None):#本作品作者吴宇航
        #     if tkinter.messagebox.askokcancel("Quit?", "Really quit?"):#本作品作者吴宇航
        #         root.destroy()#本作品作者吴宇航
        # #剪切#本作品作者吴宇航
        # def cut():#本作品作者吴宇航
        #     content_text.event_generate("<<Cut>>")#本作品作者吴宇航
        #     on_content_changed()#本作品作者吴宇航
        # #复制#本作品作者吴宇航
        # def copys():#本作品作者吴宇航
        #     content_text.event_generate("<<Copy>>")#本作品作者吴宇航
        # #粘贴#本作品作者吴宇航
        # def paste():#本作品作者吴宇航
        #     content_text.event_generate("<<Paste>>")#本作品作者吴宇航
        #     on_content_changed()#本作品作者吴宇航
        # #恢复#本作品作者吴宇航
        # def redo(event=None):#本作品作者吴宇航
        #     content_text.event_generate("<<Redo>>")#本作品作者吴宇航
        #     on_content_changed()#本作品作者吴宇航
        #     return 'break'#本作品作者吴宇航
        # #撤销#本作品作者吴宇航
        # def undo(event=None):#本作品作者吴宇航
        #     content_text.event_generate("<<Undo>>")#本作品作者吴宇航
        #     on_content_changed()#本作品作者吴宇航
        #     return 'break'#本作品作者吴宇航
        # #全选#本作品作者吴宇航
        # def select_all(event=None):#本作品作者吴宇航
        #     content_text.tag_add('sel', '1.0', 'end')#本作品作者吴宇航
        #     return "break"#本作品作者吴宇航
        # #查找#本作品作者吴宇航
        # def find_text(event=None):#本作品作者吴宇航
        #     search_toplevel=Toplevel(root)#本作品作者吴宇航
        #     search_toplevel.title('Find Text')#本作品作者吴宇航
        #     search_toplevel.transient(root)#本作品作者吴宇航
        #     search_toplevel.resizable(False, False)#本作品作者吴宇航
        #     Label(search_toplevel, text="Find All:").grid(row=0, column=0, sticky='e')#本作品作者吴宇航
        #     search_entry_widget = Entry(search_toplevel, width=50)#本作品作者吴宇航
        #     search_entry_widget.grid(row=0, column=1, padx=2, pady=2, sticky='we')#本作品作者吴宇航
        #     search_entry_widget.focus_set()#本作品作者吴宇航
        #     ignore_case_value = IntVar()#本作品作者吴宇航
        #     Checkbutton(search_toplevel, text='Ignore  Case',variable=ignore_case_value).grid(row=1, column=1, sticky='e', padx=2, pady=2)#本作品作者吴宇航
        #     Button(search_toplevel, text="Find All", underline=0,command=lambda: search_output( search_entry_widget.get(), ignore_case_value.get(), content_text, search_toplevel,search_entry_widget)).grid(row=0, column=2, sticky='e' +'w', padx=2, pady=2)#本作品作者吴宇航
        # #关闭查找窗口#本作品作者吴宇航
        # def close_search_window():#本作品作者吴宇航
        #     content_text.tag_remove('match', '1.0', END)#本作品作者吴宇航
        #     search_toplevel.destroy()#本作品作者吴宇航
        #     search_toplevel.protocol('WM_DELETE_WINDOW', close_search_window)#本作品作者吴宇航
        #     return "break"#本作品作者吴宇航
        # #查找结果输出#本作品作者吴宇航
        # def search_output(needle, if_ignore_case, content_text,search_toplevel, search_box):#本作品作者吴宇航
        #     content_text.tag_remove('match', '1.0', END)#本作品作者吴宇航
        #     matches_found = 0#本作品作者吴宇航
        #     if needle:#本作品作者吴宇航
        #          start_pos = '1.0'#本作品作者吴宇航
        #          while True:#本作品作者吴宇航
        #              start_pos = content_text.search(needle, start_pos, nocase=if_ignore_case, stopindex=END)#本作品作者吴宇航
        #              if not start_pos:#本作品作者吴宇航
        #                  break#本作品作者吴宇航
        #              end_pos = '{}+{}c'.format(start_pos, len(needle))#本作品作者吴宇航
        #              content_text.tag_add('match', start_pos, end_pos)#本作品作者吴宇航
        #              matches_found += 1#本作品作者吴宇航
        #              start_pos = end_pos#本作品作者吴宇航
        #          content_text.tag_config( 'match', foreground='red', background='yellow')#本作品作者吴宇航
        #     search_box.focus_set()#本作品作者吴宇航
        #     search_toplevel.title('{} matches found'.format(matches_found)) #本作品作者吴宇航
        # #显示about#本作品作者吴宇航
        # def display_about_messagebox(event=None):#本作品作者吴宇航
        #     tkinter.messagebox.showinfo("About", "{}{}".format(PROGRAM_NAME, "\nTkinter GUI Application\n Development Blueprints"))#本作品作者吴宇航
        # #显示help#本作品作者吴宇航
        # def display_help_messagebox(event=None):#本作品作者吴宇航
        #     tkinter.messagebox.showinfo("Help", "Help Book: \nTkinter GUI Application\n Development Blueprints", icon='question')#本作品作者吴宇航
        # #变量初始化#本作品作者吴宇航
        # show_cursor_info=BooleanVar()#本作品作者吴宇航
        # to_highlight_line = BooleanVar() #本作品作者吴宇航
        # theme_choice=StringVar()#本作品作者吴宇航
        # show_line_number = IntVar()#本作品作者吴宇航
        # show_line_number.set(1)#本作品作者吴宇航
        # #主题#本作品作者吴宇航
        # color_schemes = { 'Default': '#000000.#FFFFFF',#本作品作者吴宇航
        #                   'Greygarious':'#83406A.#D1D4D1',#本作品作者吴宇航
        #                   'Aquamarine': '#5B8340.#D1E7E0',#本作品作者吴宇航
        #                   'Bold Beige': '#4B4620.#FFF0E1',#本作品作者吴宇航
        #                   'Cobalt Blue':'#ffffBB.#3333aa',#本作品作者吴宇航
        #                   'Olive Green': '#D1E7E0.#5B8340',#本作品作者吴宇航
        #                   'Night Mode': '#FFFFFF.#000000'} #本作品作者吴宇航
        # #更换主题#本作品作者吴宇航
        # def change_theme(event=None):#本作品作者吴宇航
        #     selected_theme = theme_choice.get()#本作品作者吴宇航
        #     fg_bg_colors = color_schemes.get(selected_theme)#本作品作者吴宇航
        #     foreground_color, background_color = fg_bg_colors.split('.')#本作品作者吴宇航
        #     content_text.config(background=background_color,fg=foreground_color) #本作品作者吴宇航
        # #File#本作品作者吴宇航
        # file_menu.add_command(label="New", accelerator='Ctrl+N',    compound='left', underline=0,command=new_file)#本作品作者吴宇航
        # file_menu.add_command(label="Open", accelerator='Ctrl+O',    compound='left', underline=0,command=open_file)#本作品作者吴宇航
        # file_menu.add_command(label="Save", accelerator='Ctrl+S',    compound='left', underline=0 ,command= save)#本作品作者吴宇航
        # file_menu.add_command(label="Save as", accelerator='Shift+Ctrl+S',    compound='left', underline=0, command= save_as)#本作品作者吴宇航
        # file_menu.add_separator()#本作品作者吴宇航
        # file_menu.add_command(label="Exit", accelerator='Alt+F4',    compound='left', underline=0, command= exit_editor)#本作品作者吴宇航
        # #Edit#本作品作者吴宇航
        # edit_menu.add_command(label="Undo", accelerator='Ctrl + Z',    compound='left',command=undo)#本作品作者吴宇航
        # edit_menu.add_command(label="Redo", accelerator='Ctrl + Y',    compound='left',command=redo)#本作品作者吴宇航
        # edit_menu.add_separator()#本作品作者吴宇航
        # edit_menu.add_command(label="Cut", accelerator='Ctrl + X',    compound='left',command=cut)#本作品作者吴宇航
        # edit_menu.add_command(label="Copy", accelerator='Ctrl + C',    compound='left',command=copy)#本作品作者吴宇航
        # edit_menu.add_command(label="Paste", accelerator='Ctrl + V',    compound='left',command=paste)#本作品作者吴宇航
        # edit_menu.add_separator()#本作品作者吴宇航
        # edit_menu.add_command(label="Find",underline=0, accelerator='Ctrl + F',    compound='left',command=find_text)#本作品作者吴宇航
        # edit_menu.add_separator()#本作品作者吴宇航
        # edit_menu.add_command(label="Select All",underline=7, accelerator='Ctrl + A',    compound='left',command=select_all)#本作品作者吴宇航
        # #View#本作品作者吴宇航
        # view_menu.add_checkbutton(label="Show Line Number",    variable=show_line_number)#本作品作者吴宇航
        # view_menu.add_checkbutton(label="Show Cursor Location at Bottom",variable=show_cursor_info, command=show_cursor_info_bar)#本作品作者吴宇航
        # view_menu.add_checkbutton(label='Highlight Current Line',    onvalue=1, offvalue=0, variable=to_highlight_line,command=toggle_highlight)#本作品作者吴宇航
        # #Themes#本作品作者吴宇航
        # themes_menu.add_radiobutton(label="Default",  variable=theme_choice,command=change_theme)#本作品作者吴宇航
        # themes_menu.add_radiobutton(label="Aquamarine", variable=theme_choice,command=change_theme)#本作品作者吴宇航
        # themes_menu.add_radiobutton(label="Bold Beige", variable=theme_choice,command=change_theme)#本作品作者吴宇航
        # themes_menu.add_radiobutton(label="Cobalt Blue", variable=theme_choice,command=change_theme)#本作品作者吴宇航
        # themes_menu.add_radiobutton(label="Greygarious", variable=theme_choice,command=change_theme)#本作品作者吴宇航
        # themes_menu.add_radiobutton(label="Night Mode", variable=theme_choice,command=change_theme)#本作品作者吴宇航
        # themes_menu.add_radiobutton(label="Olive Green", variable=theme_choice,command=change_theme)#本作品作者吴宇航
        # view_menu.add_cascade(label="Themes", menu=themes_menu)#本作品作者吴宇航
        # #About#本作品作者吴宇航
        # about_menu.add_command(label="About", compound='left', command=display_about_messagebox)#本作品作者吴宇航
        # about_menu.add_command(label="Help", compound='left', command=display_help_messagebox)#本作品作者吴宇航
        # #主菜单栏#本作品作者吴宇航
        # menu_bar.add_cascade(label='File',menu=file_menu)#本作品作者吴宇航
        # menu_bar.add_cascade(label='Edit',menu=edit_menu)#本作品作者吴宇航
        # menu_bar.add_cascade(label='View',menu=view_menu)#本作品作者吴宇航
        # menu_bar.add_cascade(label='About',menu=about_menu)#本作品作者吴宇航
        # #窗口名称#本作品作者吴宇航
        # PROGRAM_NAME = " Footprint Editor "#本作品作者吴宇航
        # root.title(PROGRAM_NAME)#本作品作者吴宇航
        # #工具栏#本作品作者吴宇航
        # shortcut_bar = Frame(root,  height=25, background='light sea green')#本作品作者吴宇航
        # shortcut_bar.pack(expand='no', fill='x')#本作品作者吴宇航
        # #图标名称#本作品作者吴宇航
        # names = ["新建","打开","保存","剪切","复制","粘贴","撤销","恢复","查找"]#本作品作者吴宇航
        # icons = ['new_file', 'open_file', 'save', 'cut', 'copys', 'paste','undo', 'redo', 'find_text']#本作品作者吴宇航
        # for i in range(len(icons)):#本作品作者吴宇航
        #     # tool_bar_icon = PhotoImage(file='icons/{}.gif'.format(icon))#图标文件路径#本作品作者吴宇航
        #     cmd = eval(icons[i])#本作品作者吴宇航
        #     tool_bar = Button(shortcut_bar,text = names[i],command=cmd)#本作品作者吴宇航
            #本作品作者吴宇航
        #     tool_bar.pack(side='left')#本作品作者吴宇航
        # #左侧行数区    #本作品作者吴宇航
        # line_number_bar = Text(root, width=4, padx=3, takefocus=0,    border=0, background='khaki', state='disabled', wrap='none')#本作品作者吴宇航
        # line_number_bar.pack(side='left', fill='y')#本作品作者吴宇航
        # #文本内容区和右侧滚动条#本作品作者吴宇航
        # content_text = Text(root, wrap='word',undo=1)#本作品作者吴宇航
        # content_text.tag_configure('active_line', background='ivory2')#本作品作者吴宇航
        # content_text.bind('<Any-KeyPress>', on_content_changed)#本作品作者吴宇航
        # content_text.pack(expand='yes', fill='both')#本作品作者吴宇航
        # scroll_bar = Scrollbar(content_text)#本作品作者吴宇航
        # content_text.configure(yscrollcommand=scroll_bar.set)#本作品作者吴宇航
        # scroll_bar.config(command=content_text.yview)#本作品作者吴宇航
        # scroll_bar.pack(side='right', fill='y')#本作品作者吴宇航
        # #右键下拉菜单#本作品作者吴宇航
        # popup_menu = Menu(content_text)#本作品作者吴宇航
        # for i in ('cut', 'copy', 'paste', 'undo', 'redo'):#本作品作者吴宇航
        #     cmd = eval(i)#本作品作者吴宇航
        #     popup_menu.add_command(label=i, compound='left', command=cmd)#本作品作者吴宇航
        # popup_menu.add_separator()#本作品作者吴宇航
        # popup_menu.add_command(label='Select All', underline=7,    command=select_all)#本作品作者吴宇航
        # def show_popup_menu(event):#本作品作者吴宇航
        #     popup_menu.tk_popup(event.x_root, event.y_root)#本作品作者吴宇航
        # content_text.bind('<Button-3>', show_popup_menu)#本作品作者吴宇航
        # #右下侧光标信息显示#本作品作者吴宇航
        # cursor_info_bar = Label(content_text, text='Line: 1 | Column: 1')#本作品作者吴宇航
        # cursor_info_bar.pack(expand=NO, fill=None, side='right',    anchor='se')#本作品作者吴宇航
         #本作品作者吴宇航
        # root.config(menu=menu_bar)#本作品作者吴宇航
        # root.mainloop()#本作品作者吴宇航
        # fasdasdf1()#本作品作者吴宇航
    elif dakai == "code":#本作品作者吴宇航
        def clean(file):#本作品作者吴宇航
            os.remove(file)#本作品作者吴宇航
            with open(file, "w+"):#本作品作者吴宇航
                pass#本作品作者吴宇航
        class Saver(object):#本作品作者吴宇航
            def __init__(self, file):#本作品作者吴宇航
                self.file = file#本作品作者吴宇航
                self.terminal = sys.stdout#本作品作者吴宇航
#本作品作者吴宇航
            def write(self, message):#本作品作者吴宇航
                self.terminal.write(message)#本作品作者吴宇航
#本作品作者吴宇航
                with open(self.file, "a") as logger:#本作品作者吴宇航
                    logger.write(message)#本作品作者吴宇航
#本作品作者吴宇航
            def flush(self):#本作品作者吴宇航
                pass#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        def save(file):#本作品作者吴宇航
            sys.stdout = Saver(file)#本作品作者吴宇航
        def do(code):#本作品作者吴宇航
            try:#本作品作者吴宇航
                exec(code)#本作品作者吴宇航
            except BaseException as Errors:#本作品作者吴宇航
                print(Errors)#本作品作者吴宇航
        def read(file):#本作品作者吴宇航
            with open(file, "r+") as f:#本作品作者吴宇航
                return f.read()#本作品作者吴宇航
        class BaseFrame(Frame):#本作品作者吴宇航
#本作品作者吴宇航
            def __init__(self, title, size, icon, kind="default", background_color="GREY"):#本作品作者吴宇航
                super(BaseFrame, self).__init__(parent=None, title=title, size=size, style=DEFAULT_FRAME_STYLE ^ MAXIMIZE_BOX)#本作品作者吴宇航
#本作品作者吴宇航
                if kind == "default":#本作品作者吴宇航
                    self.panel = Panel(parent=self)#本作品作者吴宇航
                elif kind == "split-v":#本作品作者吴宇航
                    self.splitter = SplitterWindow(self, style=SP_3DSASH)#本作品作者吴宇航
                    self.left_p = Panel(self.splitter)#本作品作者吴宇航
                    self.right_p = Panel(self.splitter)#本作品作者吴宇航
                    self.splitter.SplitVertically(self.left_p, self.right_p, size[0] / 5 * 3)#本作品作者吴宇航
                    self.splitter.SetMinimumPaneSize(size[0] / 10)#本作品作者吴宇航
                elif kind == "split-h":#本作品作者吴宇航
                    self.splitter = SplitterWindow(self, style=SP_3DSASH)#本作品作者吴宇航
                    self.top_panel = Panel(self.splitter)#本作品作者吴宇航
                    self.bottom_panel = Panel(self.splitter)#本作品作者吴宇航
                    self.splitter.SplitHorizontally(self.top_panel, self.bottom_panel, size[1] / 5 * 3)#本作品作者吴宇航
                    self.splitter.SetMinimumPaneSize(size[1] / 10)#本作品作者吴宇航
#本作品作者吴宇航
                icon = Icon(icon[0], icon[1])#本作品作者吴宇航
#本作品作者吴宇航
                self.Center()#本作品作者吴宇航
                self.SetBackgroundColour(background_color)#本作品作者吴宇航
                self.SetIcon(icon)#本作品作者吴宇航
                self.SetSizeHints((size[0], size[1]), (size[0], size[1]))#本作品作者吴宇航
#本作品作者吴宇航
                self.Bind(EVT_CLOSE, self.doing_close)#本作品作者吴宇航
#本作品作者吴宇航
            def doing_close(self, event):#本作品作者吴宇航
                md_md = MessageDialog(None, "确定关闭?", caption="提示", style=YES_NO | ICON_EXCLAMATION)#本作品作者吴宇航
#本作品作者吴宇航
                if md_md.ShowModal() == ID_YES:#本作品作者吴宇航
                    self.Destroy()#本作品作者吴宇航
                    sys.exit(0)#本作品作者吴宇航
                else:#本作品作者吴宇航
                    md_md.Destroy()#本作品作者吴宇航
        class MainFrame(BaseFrame):#本作品作者吴宇航
            def __init__(self):#本作品作者吴宇航
                super(MainFrame, self).__init__(title="Python代码IDE工具", size=(750, 750),#本作品作者吴宇航
                                                icon=["icon.jpg", BITMAP_TYPE_JPEG],#本作品作者吴宇航
                                                kind="split-h", background_color="MEDIUM TURQUOISE")#本作品作者吴宇航
#本作品作者吴宇航
                self.isrunning = True#本作品作者吴宇航
                self.top()#本作品作者吴宇航
                self.bottom()#本作品作者吴宇航
            def top(self):#本作品作者吴宇航
                global editor_tc#本作品作者吴宇航
                top_bs_h = BoxSizer(HORIZONTAL)#本作品作者吴宇航
                editor_tc = TextCtrl(self.top_panel, id=-1, style=TE_MULTILINE | HSCROLL)#本作品作者吴宇航
                editor_tc.SetBackgroundColour("BLUE")#本作品作者吴宇航
                editor_tc.SetForegroundColour("YELLOW")#本作品作者吴宇航
                top_bs_v = BoxSizer(VERTICAL)#本作品作者吴宇航
                run_b_b = Bitmap("run.jpg", BITMAP_TYPE_JPEG)#本作品作者吴宇航
                stop_b_b = Bitmap("stop.jpg", BITMAP_TYPE_JPEG)#本作品作者吴宇航
                run_b = BitmapButton(self.top_panel, id=1, bitmap=run_b_b)#本作品作者吴宇航
                stop_b = BitmapButton(self.top_panel, id=12, bitmap=stop_b_b)#本作品作者吴宇航
                top_bs_v.Add(run_b, proportion=1, flag=RIGHT, border=20)#本作品作者吴宇航
                top_bs_v.Add(stop_b, proportion=1, flag=RIGHT, border=20)#本作品作者吴宇航
                top_bs_h.Add(editor_tc, proportion=20, flag=EXPAND | LEFT | RIGHT, border=20)#本作品作者吴宇航
                top_bs_h.Add(top_bs_v, proportion=1, flag=LEFT, border=50)#本作品作者吴宇航
                self.top_panel.SetSizer(top_bs_h)#本作品作者吴宇航
                self.Bind(EVT_BUTTON, MainFrame.run, id=1)#本作品作者吴宇航
                self.Bind(EVT_BUTTON, self.stop, id=12)#本作品作者吴宇航
            def bottom(self):#本作品作者吴宇航
                global return_tc#本作品作者吴宇航
                bottom_bs = BoxSizer()#本作品作者吴宇航
                return_tc = TextCtrl(self.bottom_panel, id=-1, style=TE_READONLY | TE_MULTILINE | TE_WORDWRAP)#本作品作者吴宇航
                return_tc.SetBackgroundColour("YELLOW")#本作品作者吴宇航
                return_tc.SetForegroundColour("DARK STATE BLUE")#本作品作者吴宇航
                bottom_bs.Add(return_tc, proportion=1, flag=EXPAND | ALL, border=10)#本作品作者吴宇航
                self.bottom_panel.SetSizer(bottom_bs)#本作品作者吴宇航
            @staticmethod#本作品作者吴宇航
            def run(event):#本作品作者吴宇航
                do(editor_tc.GetValue())#本作品作者吴宇航
                return_tc.SetValue(read("result.txt"))#本作品作者吴宇航
                clean("result.txt")#本作品作者吴宇航
                #本作品作者吴宇航
            def stop(self, event):#本作品作者吴宇航
                return_tc.SetValue("EXIT")#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        class MainApp(App):#本作品作者吴宇航
#本作品作者吴宇航
            def OnInit(self):#本作品作者吴宇航
                frame = MainFrame()#本作品作者吴宇航
                frame.Show()#本作品作者吴宇航
                return True#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        if __name__ == "__main__":#本作品作者吴宇航
            clean("result.txt")#本作品作者吴宇航
            save("result.txt")#本作品作者吴宇航
#本作品作者吴宇航
            myapp = MainApp()#本作品作者吴宇航
            myapp.MainLoop()#本作品作者吴宇航
            fasdasdf1()#本作品作者吴宇航
    elif dakai == "migong":#本作品作者吴宇航
        # class UnionSet(object):#本作品作者吴宇航
        #     """#本作品作者吴宇航
        #     并查集实现，构造函数中的matrix是一个numpy类型#本作品作者吴宇航
        #     """#本作品作者吴宇航
#本作品作者吴宇航
        #     def __init__(self, arr):#本作品作者吴宇航
        #         self.parent = {pos: pos for pos in arr}#本作品作者吴宇航
        #         self.count = len(arr)#本作品作者吴宇航
#本作品作者吴宇航
        #     def find(self, root):#本作品作者吴宇航
        #         if root == self.parent[root]:#本作品作者吴宇航
        #             return root#本作品作者吴宇航
        #         return self.find(self.parent[root])#本作品作者吴宇航
#本作品作者吴宇航
        #     def union(self, root1, root2):#本作品作者吴宇航
        #         self.parent[self.find(root1)] = self.find(root2)#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        # class Maze(object):#本作品作者吴宇航
        #     """#本作品作者吴宇航
        #     迷宫生成类#本作品作者吴宇航
        #     """#本作品作者吴宇航
#本作品作者吴宇航
        #     def __init__(self, width=11, height=11):#本作品作者吴宇航
        #         assert width >= 5 and height >= 5, "Length of width or height must be larger than 5."#本作品作者吴宇航
#本作品作者吴宇航
        #         self.width = (width // 2) * 2 + 1#本作品作者吴宇航
        #         self.height = (height // 2) * 2 + 1#本作品作者吴宇航
        #         self.start = [1, 0]#本作品作者吴宇航
        #         self.destination = [self.height - 2, self.width - 1]#本作品作者吴宇航
        #         self.matrix = None#本作品作者吴宇航
        #         self.path = []#本作品作者吴宇航
#本作品作者吴宇航
        #     def print_matrix(self):#本作品作者吴宇航
        #         matrix = deepcopy(self.matrix)#本作品作者吴宇航
        #         for p in self.path:#本作品作者吴宇航
        #             matrix[p[0]][p[1]] = 1#本作品作者吴宇航
        #         for i in range(self.height):#本作品作者吴宇航
        #             for j in range(self.width):#本作品作者吴宇航
        #                 if matrix[i][j] == -1:#本作品作者吴宇航
        #                     print('□', end='')#本作品作者吴宇航
        #                 elif matrix[i][j] == 0:#本作品作者吴宇航
        #                     print('  ', end='')#本作品作者吴宇航
        #                 elif matrix[i][j] == 1:#本作品作者吴宇航
        #                     print('■', end='')#本作品作者吴宇航
        #             print('')#本作品作者吴宇航
#本作品作者吴宇航
        #     def generate_matrix_dfs(self):#本作品作者吴宇航
        #         # 地图初始化，并将出口和入口处的值设置为0#本作品作者吴宇航
        #         self.matrix = -np.ones((self.height, self.width))#本作品作者吴宇航
        #         self.matrix[self.start[0], self.start[1]] = 0#本作品作者吴宇航
        #         self.matrix[self.destination[0], self.destination[1]] = 0#本作品作者吴宇航
#本作品作者吴宇航
        #         visit_flag = [[0 for i in range(self.width)] for j in range(self.height)]#本作品作者吴宇航
#本作品作者吴宇航
        #         def check(row, col, row_, col_):#本作品作者吴宇航
        #             temp_sum = 0#本作品作者吴宇航
        #             for d in [[0, 1], [0, -1], [1, 0], [-1, 0]]:#本作品作者吴宇航
        #                 temp_sum += self.matrix[row_ + d[0]][col_ + d[1]]#本作品作者吴宇航
        #             return temp_sum <= -3#本作品作者吴宇航
#本作品作者吴宇航
        #         def dfs(row, col):#本作品作者吴宇航
        #             visit_flag[row][col] = 1#本作品作者吴宇航
        #             self.matrix[row][col] = 0#本作品作者吴宇航
        #             if row == self.start[0] and col == self.start[1] + 1:#本作品作者吴宇航
        #                 return#本作品作者吴宇航
#本作品作者吴宇航
        #             directions = [[0, 2], [0, -2], [2, 0], [-2, 0]]#本作品作者吴宇航
        #             random.shuffle(directions)#本作品作者吴宇航
        #             for d in directions:#本作品作者吴宇航
        #                 row_, col_ = row + d[0], col + d[1]#本作品作者吴宇航
        #                 if row_ > 0 and row_ < self.height - 1 and col_ > 0 and col_ < self.width - 1 and visit_flag[row_][#本作品作者吴宇航
        #                     col_] == 0 and check(row, col, row_, col_):#本作品作者吴宇航
        #                     if row == row_:#本作品作者吴宇航
        #                         visit_flag[row][min(col, col_) + 1] = 1#本作品作者吴宇航
        #                         self.matrix[row][min(col, col_) + 1] = 0#本作品作者吴宇航
        #                     else:#本作品作者吴宇航
        #                         visit_flag[min(row, row_) + 1][col] = 1#本作品作者吴宇航
        #                         self.matrix[min(row, row_) + 1][col] = 0#本作品作者吴宇航
        #                     dfs(row_, col_)#本作品作者吴宇航
#本作品作者吴宇航
        #         dfs(self.destination[0], self.destination[1] - 1)#本作品作者吴宇航
        #         self.matrix[self.start[0], self.start[1] + 1] = 0#本作品作者吴宇航
#本作品作者吴宇航
        #     # 虽然说是prim算法，但是我感觉更像随机广度优先算法#本作品作者吴宇航
        #     def generate_matrix_prim(self):#本作品作者吴宇航
        #         # 地图初始化，并将出口和入口处的值设置为0#本作品作者吴宇航
        #         self.matrix = -np.ones((self.height, self.width))#本作品作者吴宇航
#本作品作者吴宇航
        #         def check(row, col):#本作品作者吴宇航
        #             temp_sum = 0#本作品作者吴宇航
        #             for d in [[0, 1], [0, -1], [1, 0], [-1, 0]]:#本作品作者吴宇航
        #                 temp_sum += self.matrix[row + d[0]][col + d[1]]#本作品作者吴宇航
        #             return temp_sum < -3#本作品作者吴宇航
#本作品作者吴宇航
        #         queue = []#本作品作者吴宇航
        #         row, col = (np.random.randint(1, self.height - 1) // 2) * 2 + 1, (#本作品作者吴宇航
        #                     np.random.randint(1, self.width - 1) // 2) * 2 + 1#本作品作者吴宇航
        #         queue.append((row, col, -1, -1))#本作品作者吴宇航
        #         while len(queue) != 0:#本作品作者吴宇航
        #             row, col, r_, c_ = queue.pop(np.random.randint(0, len(queue)))#本作品作者吴宇航
        #             if check(row, col):#本作品作者吴宇航
        #                 self.matrix[row, col] = 0#本作品作者吴宇航
        #                 if r_ != -1 and row == r_:#本作品作者吴宇航
        #                     self.matrix[row][min(col, c_) + 1] = 0#本作品作者吴宇航
        #                 elif r_ != -1 and col == c_:#本作品作者吴宇航
        #                     self.matrix[min(row, r_) + 1][col] = 0#本作品作者吴宇航
        #                 for d in [[0, 2], [0, -2], [2, 0], [-2, 0]]:#本作品作者吴宇航
        #                     row_, col_ = row + d[0], col + d[1]#本作品作者吴宇航
        #                     if row_ > 0 and row_ < self.height - 1 and col_ > 0 and col_ < self.width - 1 and self.matrix[row_][#本作品作者吴宇航
        #                         col_] == -1:#本作品作者吴宇航
        #                         queue.append((row_, col_, row, col))#本作品作者吴宇航
#本作品作者吴宇航
        #         self.matrix[self.start[0], self.start[1]] = 0#本作品作者吴宇航
        #         self.matrix[self.destination[0], self.destination[1]] = 0#本作品作者吴宇航
#本作品作者吴宇航
        #     # 递归切分算法，还有问题，现在不可用#本作品作者吴宇航
        #     def generate_matrix_split(self):#本作品作者吴宇航
        #         # 地图初始化，并将出口和入口处的值设置为0#本作品作者吴宇航
        #         self.matrix = -np.zeros((self.height, self.width))#本作品作者吴宇航
        #         self.matrix[0, :] = -1#本作品作者吴宇航
        #         self.matrix[self.height - 1, :] = -1#本作品作者吴宇航
        #         self.matrix[:, 0] = -1#本作品作者吴宇航
        #         self.matrix[:, self.width - 1] = -1#本作品作者吴宇航
#本作品作者吴宇航
        #         # 随机生成位于(start, end)之间的偶数#本作品作者吴宇航
        #         def get_random(start, end):#本作品作者吴宇航
        #             rand = np.random.randint(start, end)#本作品作者吴宇航
        #             if rand & 0x1 == 0:#本作品作者吴宇航
        #                 return rand#本作品作者吴宇航
        #             return get_random(start, end)#本作品作者吴宇航
#本作品作者吴宇航
        #         # split函数的四个参数分别是左上角的行数、列数，右下角的行数、列数，墙壁只能在偶数行，偶数列#本作品作者吴宇航
        #         def split(lr, lc, rr, rc):#本作品作者吴宇航
        #             if rr - lr < 2 or rc - lc < 2:#本作品作者吴宇航
        #                 return#本作品作者吴宇航
#本作品作者吴宇航
        #             # 生成墙壁,墙壁只能是偶数点#本作品作者吴宇航
        #             cur_row, cur_col = get_random(lr, rr), get_random(lc, rc)#本作品作者吴宇航
        #             for i in range(lc, rc + 1):#本作品作者吴宇航
        #                 self.matrix[cur_row][i] = -1#本作品作者吴宇航
        #             for i in range(lr, rr + 1):#本作品作者吴宇航
        #                 self.matrix[i][cur_col] = -1#本作品作者吴宇航
#本作品作者吴宇航
        #             # 挖穿三面墙得到连通图，挖孔的点只能是偶数点#本作品作者吴宇航
        #             wall_list = [#本作品作者吴宇航
        #                 ("left", cur_row, [lc + 1, cur_col - 1]),#本作品作者吴宇航
        #                 ("right", cur_row, [cur_col + 1, rc - 1]),#本作品作者吴宇航
        #                 ("top", cur_col, [lr + 1, cur_row - 1]),#本作品作者吴宇航
        #                 ("down", cur_col, [cur_row + 1, rr - 1])#本作品作者吴宇航
        #             ]#本作品作者吴宇航
        #             random.shuffle(wall_list)#本作品作者吴宇航
        #             for wall in wall_list[:-1]:#本作品作者吴宇航
        #                 if wall[2][1] - wall[2][0] < 1:#本作品作者吴宇航
        #                     continue#本作品作者吴宇航
        #                 if wall[0] in ["left", "right"]:#本作品作者吴宇航
        #                     self.matrix[wall[1], get_random(wall[2][0], wall[2][1] + 1) + 1] = 0#本作品作者吴宇航
        #                 else:#本作品作者吴宇航
        #                     self.matrix[get_random(wall[2][0], wall[2][1] + 1), wall[1] + 1] = 0#本作品作者吴宇航
#本作品作者吴宇航
        #             # self.print_matrix()#本作品作者吴宇航
        #             # time.sleep(1)#本作品作者吴宇航
        #             # 递归#本作品作者吴宇航
        #             split(lr + 2, lc + 2, cur_row - 2, cur_col - 2)#本作品作者吴宇航
        #             split(lr + 2, cur_col + 2, cur_row - 2, rc - 2)#本作品作者吴宇航
        #             split(cur_row + 2, lc + 2, rr - 2, cur_col - 2)#本作品作者吴宇航
        #             split(cur_row + 2, cur_col + 2, rr - 2, rc - 2)#本作品作者吴宇航
#本作品作者吴宇航
        #             self.matrix[self.start[0], self.start[1]] = 0#本作品作者吴宇航
        #             self.matrix[self.destination[0], self.destination[1]] = 0#本作品作者吴宇航
#本作品作者吴宇航
        #         split(0, 0, self.height - 1, self.width - 1)#本作品作者吴宇航
#本作品作者吴宇航
        #     # 最小生成树算法-kruskal（选边法）思想生成迷宫地图，这种实现方法最复杂。#本作品作者吴宇航
        #     def generate_matrix_kruskal(self):#本作品作者吴宇航
        #         # 地图初始化，并将出口和入口处的值设置为0#本作品作者吴宇航
        #         self.matrix = -np.ones((self.height, self.width))#本作品作者吴宇航
#本作品作者吴宇航
        #         def check(row, col):#本作品作者吴宇航
        #             ans, counter = [], 0#本作品作者吴宇航
        #             for d in [[0, 1], [0, -1], [1, 0], [-1, 0]]:#本作品作者吴宇航
        #                 row_, col_ = row + d[0], col + d[1]#本作品作者吴宇航
        #                 if row_ > 0 and row_ < self.height - 1 and col_ > 0 and col_ < self.width - 1 and self.matrix[#本作品作者吴宇航
        #                     row_, col_] == -1:#本作品作者吴宇航
        #                     ans.append([d[0] * 2, d[1] * 2])#本作品作者吴宇航
        #                     counter += 1#本作品作者吴宇航
        #             if counter <= 1:#本作品作者吴宇航
        #                 return []#本作品作者吴宇航
        #             return ans#本作品作者吴宇航
#本作品作者吴宇航
        #         nodes = set()#本作品作者吴宇航
        #         row = 1#本作品作者吴宇航
        #         while row < self.height:#本作品作者吴宇航
        #             col = 1#本作品作者吴宇航
        #             while col < self.width:#本作品作者吴宇航
        #                 self.matrix[row, col] = 0#本作品作者吴宇航
        #                 nodes.add((row, col))#本作品作者吴宇航
        #                 col += 2#本作品作者吴宇航
        #             row += 2#本作品作者吴宇航
#本作品作者吴宇航
        #         unionset = UnionSet(nodes)#本作品作者吴宇航
        #         while unionset.count > 1:#本作品作者吴宇航
        #             row, col = nodes.pop()#本作品作者吴宇航
        #             directions = check(row, col)#本作品作者吴宇航
        #             if len(directions):#本作品作者吴宇航
        #                 random.shuffle(directions)#本作品作者吴宇航
        #                 for d in directions:#本作品作者吴宇航
        #                     row_, col_ = row + d[0], col + d[1]#本作品作者吴宇航
        #                     if unionset.find((row, col)) == unionset.find((row_, col_)):#本作品作者吴宇航
        #                         continue#本作品作者吴宇航
        #                     nodes.add((row, col))#本作品作者吴宇航
        #                     unionset.count -= 1#本作品作者吴宇航
        #                     unionset.union((row, col), (row_, col_))#本作品作者吴宇航
#本作品作者吴宇航
        #                     if row == row_:#本作品作者吴宇航
        #                         self.matrix[row][min(col, col_) + 1] = 0#本作品作者吴宇航
        #                     else:#本作品作者吴宇航
        #                         self.matrix[min(row, row_) + 1][col] = 0#本作品作者吴宇航
        #                     break#本作品作者吴宇航
#本作品作者吴宇航
        #         self.matrix[self.start[0], self.start[1]] = 0#本作品作者吴宇航
        #         self.matrix[self.destination[0], self.destination[1]] = 0#本作品作者吴宇航
#本作品作者吴宇航
        #     # 迷宫寻路算法dfs#本作品作者吴宇航
        #     def find_path_dfs(self, destination):#本作品作者吴宇航
        #         visited = [[0 for i in range(self.width)] for j in range(self.height)]#本作品作者吴宇航
#本作品作者吴宇航
        #         def dfs(path):#本作品作者吴宇航
        #             visited[path[-1][0]][path[-1][1]] = 1#本作品作者吴宇航
        #             if path[-1][0] == destination[0] and path[-1][1] == destination[1]:#本作品作者吴宇航
        #                 self.path = path[:]#本作品作者吴宇航
        #                 return#本作品作者吴宇航
        #             for d in [[0, 1], [0, -1], [1, 0], [-1, 0]]:#本作品作者吴宇航
        #                 row_, col_ = path[-1][0] + d[0], path[-1][1] + d[1]#本作品作者吴宇航
        #                 if row_ > 0 and row_ < self.height - 1 and col_ > 0 and col_ < self.width and visited[row_][#本作品作者吴宇航
        #                     col_] == 0 and self.matrix[row_][col_] == 0:#本作品作者吴宇航
        #                     dfs(path + [[row_, col_]])#本作品作者吴宇航
#本作品作者吴宇航
        #         dfs([[self.start[0], self.start[1]]])#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        # if __name__ == '__main__':#本作品作者吴宇航
        #     maze = Maze(51, 51)#本作品作者吴宇航
        #     maze.generate_matrix_kruskal()#本作品作者吴宇航
        #     maze.print_matrix()#本作品作者吴宇航
        #     maze.find_path_dfs(maze.destination)#本作品作者吴宇航
        #     print("answer", maze.path)#本作品作者吴宇航
        #     maze.print_matrix()#本作品作者吴宇航
#本作品作者吴宇航
        # import copy#本作品作者吴宇航
        # import math#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        # def draw_cell(canvas, row, col, color="#F2F2F2"):#本作品作者吴宇航
        #     x0, y0 = col * cell_width, row * cell_width#本作品作者吴宇航
        #     x1, y1 = x0 + cell_width, y0 + cell_width#本作品作者吴宇航
        #     canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline=color, width=0)#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        # def draw_path(canvas, matrix, row, col, color, line_color):#本作品作者吴宇航
        #     # 列#本作品作者吴宇航
        #     if row + 1 < rows and matrix[row - 1][col] >= 1 and matrix[row + 1][col] >= 1:#本作品作者吴宇航
        #         x0, y0 = col * cell_width + 2 * cell_width / 5, row * cell_width#本作品作者吴宇航
        #         x1, y1 = x0 + cell_width / 5, y0 + cell_width#本作品作者吴宇航
        #     # 行#本作品作者吴宇航
        #     elif col + 1 < cols and matrix[row][col - 1] >= 1 and matrix[row][col + 1] >= 1:#本作品作者吴宇航
        #         x0, y0 = col * cell_width, row * cell_width + 2 * cell_width / 5#本作品作者吴宇航
        #         x1, y1 = x0 + cell_width, y0 + cell_width / 5#本作品作者吴宇航
        #     # 左上角#本作品作者吴宇航
        #     elif col + 1 < cols and row + 1 < rows and matrix[row][col + 1] >= 1 and matrix[row + 1][col] >= 1:#本作品作者吴宇航
        #         x0, y0 = col * cell_width + 2 * cell_width / 5, row * cell_width + 2 * cell_width / 5#本作品作者吴宇航
        #         x1, y1 = x0 + 3 * cell_width / 5, y0 + cell_width / 5#本作品作者吴宇航
        #         canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline=line_color, width=0)#本作品作者吴宇航
        #         x0, y0 = col * cell_width + 2 * cell_width / 5, row * cell_width + 2 * cell_width / 5#本作品作者吴宇航
        #         x1, y1 = x0 + cell_width / 5, y0 + 3 * cell_width / 5#本作品作者吴宇航
        #     # 右上角#本作品作者吴宇航
        #     elif row + 1 < rows and matrix[row][col - 1] >= 1 and matrix[row + 1][col] >= 1:#本作品作者吴宇航
        #         x0, y0 = col * cell_width, row * cell_width + 2 * cell_width / 5#本作品作者吴宇航
        #         x1, y1 = x0 + 3 * cell_width / 5, y0 + cell_width / 5#本作品作者吴宇航
        #         canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline=line_color, width=0)#本作品作者吴宇航
        #         x0, y0 = col * cell_width + 2 * cell_width / 5, row * cell_width + 2 * cell_width / 5#本作品作者吴宇航
        #         x1, y1 = x0 + cell_width / 5, y0 + 3 * cell_width / 5#本作品作者吴宇航
        #     # 左下角#本作品作者吴宇航
        #     elif col + 1 < cols and matrix[row - 1][col] >= 1 and matrix[row][col + 1] >= 1:#本作品作者吴宇航
        #         x0, y0 = col * cell_width + 2 * cell_width / 5, row * cell_width#本作品作者吴宇航
        #         x1, y1 = x0 + cell_width / 5, y0 + 3 * cell_width / 5#本作品作者吴宇航
        #         canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline=line_color, width=0)#本作品作者吴宇航
        #         x0, y0 = col * cell_width + 2 * cell_width / 5, row * cell_width + 2 * cell_width / 5#本作品作者吴宇航
        #         x1, y1 = x0 + 3 * cell_width / 5, y0 + cell_width / 5#本作品作者吴宇航
        #     # 右下角#本作品作者吴宇航
        #     elif matrix[row - 1][col] >= 1 and matrix[row][col - 1] >= 1:#本作品作者吴宇航
        #         x0, y0 = col * cell_width, row * cell_width + 2 * cell_width / 5#本作品作者吴宇航
        #         x1, y1 = x0 + 3 * cell_width / 5, y0 + cell_width / 5#本作品作者吴宇航
        #         canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline=line_color, width=0)#本作品作者吴宇航
        #         x0, y0 = col * cell_width + 2 * cell_width / 5, row * cell_width#本作品作者吴宇航
        #         x1, y1 = x0 + cell_width / 5, y0 + 3 * cell_width / 5#本作品作者吴宇航
        #     else:#本作品作者吴宇航
        #         x0, y0 = col * cell_width + 2 * cell_width / 5, row * cell_width + 2 * cell_width / 5#本作品作者吴宇航
        #         x1, y1 = x0 + cell_width / 5, y0 + cell_width / 5#本作品作者吴宇航
        #     canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline=line_color, width=0)#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        # def draw_maze(canvas, matrix, path, moves):#本作品作者吴宇航
#本作品作者吴宇航
        #     for r in range(rows):#本作品作者吴宇航
        #         for c in range(cols):#本作品作者吴宇航
        #             if matrix[r][c] == 0:#本作品作者吴宇航
        #                 draw_cell(canvas, r, c)#本作品作者吴宇航
        #             elif matrix[r][c] == -1:#本作品作者吴宇航
        #                 draw_cell(canvas, r, c, '#525288')#本作品作者吴宇航
        #             elif matrix[r][c] == 1:#本作品作者吴宇航
        #                 draw_cell(canvas, r, c)#本作品作者吴宇航
        #                 draw_path(canvas, matrix, r, c, '#bc84a8', '#bc84a8')#本作品作者吴宇航
        #             elif matrix[r][c] == 2:#本作品作者吴宇航
        #                 draw_cell(canvas, r, c)#本作品作者吴宇航
        #                 draw_path(canvas, matrix, r, c, '#ee3f4d', '#ee3f4d')#本作品作者吴宇航
        #     for p in path:#本作品作者吴宇航
        #         matrix[p[0]][p[1]] = 1#本作品作者吴宇航
        #     for move in moves:#本作品作者吴宇航
        #         matrix[move[0]][move[1]] = 2#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        # def update_maze(canvas, matrix, path, moves):#本作品作者吴宇航
        #     canvas.delete("all")#本作品作者吴宇航
        #     matrix = copy.copy(matrix)#本作品作者吴宇航
        #     for p in path:#本作品作者吴宇航
        #         matrix[p[0]][p[1]] = 1#本作品作者吴宇航
        #     for move in moves:#本作品作者吴宇航
        #         matrix[move[0]][move[1]] = 2#本作品作者吴宇航
#本作品作者吴宇航
        #     row, col = movement_list[-1]#本作品作者吴宇航
        #     colors = ['#525288', '#F2F2F2', '#525288', '#F2F2F2', '#525288', '#F2F2F2', '#525288', '#F2F2F2']#本作品作者吴宇航
        #     if level > 2:#本作品作者吴宇航
        #         colors = ['#232323', '#252525', '#2a2a32', '#424242', '#434368', '#b4b4b4', '#525288', '#F2F2F2']#本作品作者吴宇航
#本作品作者吴宇航
        #     for r in range(rows):#本作品作者吴宇航
        #         for c in range(cols):#本作品作者吴宇航
        #             distance = (row - r) * (row - r) + (col - c) * (col - c)#本作品作者吴宇航
        #             if distance >= 100:#本作品作者吴宇航
        #                 color = colors[0:2]#本作品作者吴宇航
        #             elif distance >= 60:#本作品作者吴宇航
        #                 color = colors[2:4]#本作品作者吴宇航
        #             elif distance >= 30:#本作品作者吴宇航
        #                 color = colors[4:6]#本作品作者吴宇航
        #             else:#本作品作者吴宇航
        #                 color = colors[6:8]#本作品作者吴宇航
#本作品作者吴宇航
        #             if matrix[r][c] == 0:#本作品作者吴宇航
        #                 draw_cell(canvas, r, c, color[1])#本作品作者吴宇航
        #             elif matrix[r][c] == -1:#本作品作者吴宇航
        #                 draw_cell(canvas, r, c, color[0])#本作品作者吴宇航
        #             elif matrix[r][c] == 1:#本作品作者吴宇航
        #                 draw_cell(canvas, r, c, color[1])#本作品作者吴宇航
        #                 draw_path(canvas, matrix, r, c, '#bc84a8', '#bc84a8')#本作品作者吴宇航
        #             elif matrix[r][c] == 2:#本作品作者吴宇航
        #                 draw_cell(canvas, r, c, color[1])#本作品作者吴宇航
        #                 draw_path(canvas, matrix, r, c, '#ee3f4d', '#ee3f4d')#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        # def check_reach():#本作品作者吴宇航
        #     global next_maze_flag#本作品作者吴宇航
        #     if movement_list[-1] == maze.destination:#本作品作者吴宇航
        #         print("Congratulations! You reach the goal! The step used: {}".format(click_counter))#本作品作者吴宇航
        #         x0, y0 = width / 2 - 200, 30#本作品作者吴宇航
        #         x1, y1 = x0 + 400, y0 + 40#本作品作者吴宇航
        #         canvas.create_rectangle(x0, y0, x1, y1, fill='#F2F2F2', outline='#525288', width=3)#本作品作者吴宇航
        #         canvas.create_text(width / 2, y0 + 20,#本作品作者吴宇航
        #                            text="Congratulations! You reach the goal! Steps used: {}".format(click_counter),#本作品作者吴宇航
        #                            fill="#525288")#本作品作者吴宇航
        #         next_maze_flag = True#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        # def _eventHandler(event):#本作品作者吴宇航
        #     global movement_list#本作品作者吴宇航
        #     global click_counter#本作品作者吴宇航
        #     global next_maze_flag#本作品作者吴宇航
        #     global level#本作品作者吴宇航
#本作品作者吴宇航
        #     if not next_maze_flag and event.keysym in ['Left', 'Right', 'Up', 'Down']:#本作品作者吴宇航
        #         click_counter += 1#本作品作者吴宇航
        #         windows.title("Maze Level-{} Steps-{}".format(level, click_counter))#本作品作者吴宇航
        #         cur_pos = movement_list[-1]#本作品作者吴宇航
        #         ops = {'Left': [0, -1], 'Right': [0, 1], 'Up': [-1, 0], 'Down': [1, 0]}#本作品作者吴宇航
        #         r_, c_ = cur_pos[0] + ops[event.keysym][0], cur_pos[1] + ops[event.keysym][1]#本作品作者吴宇航
        #         if len(movement_list) > 1 and [r_, c_] == movement_list[-2]:#本作品作者吴宇航
        #             movement_list.pop()#本作品作者吴宇航
        #             while True:#本作品作者吴宇航
        #                 cur_pos = movement_list[-1]#本作品作者吴宇航
        #                 counter = 0#本作品作者吴宇航
        #                 for d in [[0, 1], [0, -1], [1, 0], [-1, 0]]:#本作品作者吴宇航
        #                     r_, c_ = cur_pos[0] + d[0], cur_pos[1] + d[1]#本作品作者吴宇航
        #                     if c_ >= 0 and maze.matrix[r_][c_] == 0:#本作品作者吴宇航
        #                         counter += 1#本作品作者吴宇航
        #                 if counter != 2:#本作品作者吴宇航
        #                     break#本作品作者吴宇航
        #                 movement_list.pop()#本作品作者吴宇航
        #         elif r_ < maze.height and c_ < maze.width and maze.matrix[r_][c_] == 0:#本作品作者吴宇航
        #             while True:#本作品作者吴宇航
        #                 movement_list.append([r_, c_])#本作品作者吴宇航
        #                 temp_list = []#本作品作者吴宇航
        #                 for d in [[0, 1], [0, -1], [1, 0], [-1, 0]]:#本作品作者吴宇航
        #                     r__, c__ = r_ + d[0], c_ + d[1]#本作品作者吴宇航
        #                     if c__ < maze.width and maze.matrix[r__][c__] == 0 and [r__, c__] != cur_pos:#本作品作者吴宇航
        #                         temp_list.append([r__, c__])#本作品作者吴宇航
        #                 if len(temp_list) != 1:#本作品作者吴宇航
        #                     break#本作品作者吴宇航
        #                 cur_pos = [r_, c_]#本作品作者吴宇航
        #                 r_, c_ = temp_list[0]#本作品作者吴宇航
        #         update_maze(canvas, maze.matrix, maze.path, movement_list)#本作品作者吴宇航
        #         check_reach()#本作品作者吴宇航
        #     elif next_maze_flag:#本作品作者吴宇航
        #         next_maze_flag = False#本作品作者吴宇航
        #         movement_list = [maze.start]#本作品作者吴宇航
        #         click_counter = 0#本作品作者吴宇航
        #         maze.generate_matrix_kruskal()#本作品作者吴宇航
        #         maze.path = []#本作品作者吴宇航
        #         draw_maze(canvas, maze.matrix, maze.path, movement_list)#本作品作者吴宇航
        #         level += 1#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        # def _paint(event):#本作品作者吴宇航
        #     x, y = math.floor((event.y - 1) / cell_width), math.floor((event.x - 1) / cell_width)#本作品作者吴宇航
        #     if maze.matrix[x][y] == 0:#本作品作者吴宇航
        #         maze.find_path_dfs([x, y])#本作品作者吴宇航
        #         update_maze(canvas, maze.matrix, maze.path, movement_list)#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        # def _reset(event):#本作品作者吴宇航
        #     maze.path = []#本作品作者吴宇航
        #     update_maze(canvas, maze.matrix, maze.path, movement_list)#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        # if __name__ == '__main__':#本作品作者吴宇航
        #     # 基础参数#本作品作者吴宇航
        #     cell_width = 20#本作品作者吴宇航
        #     rows = 30#本作品作者吴宇航
        #     cols = 44#本作品作者吴宇航
        #     height = cell_width * rows#本作品作者吴宇航
        #     width = cell_width * cols#本作品作者吴宇航
        #     level = 1#本作品作者吴宇航
        #     click_counter = 0#本作品作者吴宇航
        #     next_maze_flag = False#本作品作者吴宇航
#本作品作者吴宇航
        #     windows = tk.Tk()#本作品作者吴宇航
        #     windows.title("迷宫小游戏")#本作品作者吴宇航
        #     canvas = tk.Canvas(windows, background="#F2F2F2", width=width, height=height)#本作品作者吴宇航
        #     canvas.pack()#本作品作者吴宇航
#本作品作者吴宇航
        #     maze = Maze(cols, rows)#本作品作者吴宇航
        #     movement_list = [maze.start]#本作品作者吴宇航
        #     maze.generate_matrix_kruskal()#本作品作者吴宇航
        #     draw_maze(canvas, maze.matrix, maze.path, movement_list)#本作品作者吴宇航
#本作品作者吴宇航
        #     canvas.bind("<Button-1>", _paint)#本作品作者吴宇航
        #     canvas.bind("<Button-3>", _reset)#本作品作者吴宇航
        #     canvas.bind_all("<KeyPress>", _eventHandler)#本作品作者吴宇航
        #     windows.mainloop()#本作品作者吴宇航
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
        fangwen("https://livefile.xesimg.com/programme/python_assets/996c33f4bd5a6f3563afe0c5d45b8cbe.html")#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
    elif dakai == "xiaoqiu":#本作品作者吴宇航
        class GameWindow(object):#本作品作者吴宇航
            '''创建游戏窗口类'''#本作品作者吴宇航
            def __init__(self,*args,**kw):      #本作品作者吴宇航
                self.window_length = 600#本作品作者吴宇航
                self.window_wide = 500#本作品作者吴宇航
                #绘制游戏窗口，设置窗口尺寸#本作品作者吴宇航
                self.game_window = pygame.display.set_mode((self.window_length,self.window_wide))#本作品作者吴宇航
                #设置游戏窗口标题#本作品作者吴宇航
                pygame.display.set_caption("CatchBallGame")#本作品作者吴宇航
                #定义游戏窗口背景颜色参数#本作品作者吴宇航
                self.window_color = (135,206,250)#本作品作者吴宇航
#本作品作者吴宇航
            def backgroud(self):#本作品作者吴宇航
                #绘制游戏窗口背景颜色#本作品作者吴宇航
                self.game_window.fill(self.window_color)#本作品作者吴宇航
#本作品作者吴宇航
        class Ball(object):#本作品作者吴宇航
            '''创建球类'''#本作品作者吴宇航
            def __init__(self,*args,**kw):#本作品作者吴宇航
                #设置球的半径、颜色、移动速度参数#本作品作者吴宇航
                self.ball_color = (255,215,0)       #本作品作者吴宇航
                self.move_x = 1#本作品作者吴宇航
                self.move_y = 1#本作品作者吴宇航
                self.radius = 10#本作品作者吴宇航
#本作品作者吴宇航
            def ballready(self):#本作品作者吴宇航
                #设置球的初始位置、#本作品作者吴宇航
                self.ball_x = self.mouse_x#本作品作者吴宇航
                self.ball_y = self.window_wide-self.rect_wide-self.radius#本作品作者吴宇航
                #绘制球，设置反弹触发条件           #本作品作者吴宇航
                pygame.draw.circle(self.game_window,self.ball_color,(self.ball_x,self.ball_y),self.radius)#本作品作者吴宇航
#本作品作者吴宇航
            def ballmove(self):#本作品作者吴宇航
                #绘制球，设置反弹触发条件           #本作品作者吴宇航
                pygame.draw.circle(self.game_window,self.ball_color,(self.ball_x,self.ball_y),self.radius)      #本作品作者吴宇航
                self.ball_x += self.move_x#本作品作者吴宇航
                self.ball_y -= self.move_y#本作品作者吴宇航
                #调用碰撞检测函数#本作品作者吴宇航
                self.ball_window()#本作品作者吴宇航
                self.ball_rect()#本作品作者吴宇航
                #每接5次球球速增加一倍#本作品作者吴宇航
                if self.distance < self.radius:#本作品作者吴宇航
                    self.frequency += 1#本作品作者吴宇航
                    if self.frequency == 5:#本作品作者吴宇航
                        self.frequency = 0#本作品作者吴宇航
                        self.move_x += self.move_x#本作品作者吴宇航
                        self.move_y += self.move_y#本作品作者吴宇航
                        self.point += self.point#本作品作者吴宇航
                #设置游戏失败条件#本作品作者吴宇航
                if self.ball_y > 520:#本作品作者吴宇航
                    self.gameover = self.over_font.render("Game Over",False,(0,0,0))#本作品作者吴宇航
                    self.game_window.blit(self.gameover,(100,130))#本作品作者吴宇航
                    self.over_sign = 1#本作品作者吴宇航
#本作品作者吴宇航
        class Rect(object):#本作品作者吴宇航
            '''创建球拍类'''#本作品作者吴宇航
            def __init__(self,*args,**kw):#本作品作者吴宇航
                #设置球拍颜色参数#本作品作者吴宇航
                self.rect_color = (255,0,0)#本作品作者吴宇航
                self.rect_length = 100#本作品作者吴宇航
                self.rect_wide = 10#本作品作者吴宇航
#本作品作者吴宇航
            def rectmove(self):#本作品作者吴宇航
                #获取鼠标位置参数#本作品作者吴宇航
                self.mouse_x,self.mouse_y = pygame.mouse.get_pos()#本作品作者吴宇航
                #绘制球拍，限定横向边界                    #本作品作者吴宇航
                if self.mouse_x >= self.window_length-self.rect_length//2:#本作品作者吴宇航
                    self.mouse_x = self.window_length-self.rect_length//2#本作品作者吴宇航
                if self.mouse_x <= self.rect_length//2:#本作品作者吴宇航
                    self.mouse_x = self.rect_length//2#本作品作者吴宇航
                pygame.draw.rect(self.game_window,self.rect_color,((self.mouse_x-self.rect_length//2),(self.window_wide-self.rect_wide),self.rect_length,self.rect_wide))#本作品作者吴宇航
#本作品作者吴宇航
        class Brick(object):#本作品作者吴宇航
            def __init__(self,*args,**kw):#本作品作者吴宇航
                #设置砖块颜色参数#本作品作者吴宇航
                self.brick_color = (139,126,102)#本作品作者吴宇航
                self.brick_list = [[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1]]#本作品作者吴宇航
                self.brick_length = 80#本作品作者吴宇航
                self.brick_wide = 20#本作品作者吴宇航
#本作品作者吴宇航
            def brickarrange(self):     #本作品作者吴宇航
                for i in range(5):#本作品作者吴宇航
                    for j in range(6):#本作品作者吴宇航
                        self.brick_x = j*(self.brick_length+24)#本作品作者吴宇航
                        self.brick_y = i*(self.brick_wide+20)+40#本作品作者吴宇航
                        if self.brick_list[i][j] == 1:#本作品作者吴宇航
                            #绘制砖块#本作品作者吴宇航
                            pygame.draw.rect(self.game_window,self.brick_color,(self.brick_x,self.brick_y,self.brick_length,self.brick_wide))                   #本作品作者吴宇航
                            #调用碰撞检测函数#本作品作者吴宇航
                            self.ball_brick()                                       #本作品作者吴宇航
                            if self.distanceb < self.radius:#本作品作者吴宇航
                                self.brick_list[i][j] = 0#本作品作者吴宇航
                                self.score += self.point#本作品作者吴宇航
                #设置游戏胜利条件#本作品作者吴宇航
                if self.brick_list == [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]:#本作品作者吴宇航
                    self.win = self.win_font.render("You Win",False,(0,0,0))#本作品作者吴宇航
                    self.game_window.blit(self.win,(100,130))#本作品作者吴宇航
                    self.win_sign = 1#本作品作者吴宇航
#本作品作者吴宇航
        class Score(object):#本作品作者吴宇航
            '''创建分数类'''#本作品作者吴宇航
            def __init__(self,*args,**kw):      #本作品作者吴宇航
                #设置初始分数#本作品作者吴宇航
                self.score = 0#本作品作者吴宇航
                #设置分数字体#本作品作者吴宇航
                self.score_font = pygame.font.SysFont('arial',20)#本作品作者吴宇航
                #设置初始加分点数#本作品作者吴宇航
                self.point = 1#本作品作者吴宇航
                #设置初始接球次数#本作品作者吴宇航
                self.frequency = 0#本作品作者吴宇航
#本作品作者吴宇航
            def countscore(self):#本作品作者吴宇航
                #绘制玩家分数         #本作品作者吴宇航
                my_score = self.score_font.render(str(self.score),False,(255,255,255))#本作品作者吴宇航
                self.game_window.blit(my_score,(555,15))#本作品作者吴宇航
#本作品作者吴宇航
        class GameOver(object):#本作品作者吴宇航
            '''创建游戏结束类'''#本作品作者吴宇航
            def __init__(self,*args,**kw):#本作品作者吴宇航
                #设置Game Over字体#本作品作者吴宇航
                self.over_font = pygame.font.SysFont('arial',80)#本作品作者吴宇航
                #定义GameOver标识#本作品作者吴宇航
                self.over_sign = 0#本作品作者吴宇航
#本作品作者吴宇航
        class Win(object):#本作品作者吴宇航
            '''创建游戏胜利类'''#本作品作者吴宇航
            def __init__(self,*args,**kw):#本作品作者吴宇航
                #设置You Win字体#本作品作者吴宇航
                self.win_font = pygame.font.SysFont('arial',80)#本作品作者吴宇航
                #定义Win标识#本作品作者吴宇航
                self.win_sign = 0#本作品作者吴宇航
#本作品作者吴宇航
        class Collision(object):#本作品作者吴宇航
            '''碰撞检测类'''#本作品作者吴宇航
            #球与窗口边框的碰撞检测#本作品作者吴宇航
            def ball_window(self):#本作品作者吴宇航
                if self.ball_x <= self.radius or self.ball_x >= (self.window_length-self.radius):#本作品作者吴宇航
                    self.move_x = -self.move_x#本作品作者吴宇航
                if self.ball_y <= self.radius:#本作品作者吴宇航
                    self.move_y = -self.move_y#本作品作者吴宇航
#本作品作者吴宇航
            #球与球拍的碰撞检测#本作品作者吴宇航
            def ball_rect(self):#本作品作者吴宇航
                #定义碰撞标识#本作品作者吴宇航
                self.collision_sign_x = 0#本作品作者吴宇航
                self.collision_sign_y = 0#本作品作者吴宇航
#本作品作者吴宇航
                if self.ball_x < (self.mouse_x-self.rect_length//2):#本作品作者吴宇航
                    self.closestpoint_x = self.mouse_x-self.rect_length//2#本作品作者吴宇航
                    self.collision_sign_x = 1#本作品作者吴宇航
                elif self.ball_x > (self.mouse_x+self.rect_length//2):#本作品作者吴宇航
                    self.closestpoint_x = self.mouse_x+self.rect_length//2#本作品作者吴宇航
                    self.collision_sign_x = 2#本作品作者吴宇航
                else:#本作品作者吴宇航
                    self.closestpoint_x = self.ball_x#本作品作者吴宇航
                    self.collision_sign_x = 3#本作品作者吴宇航
#本作品作者吴宇航
                if self.ball_y < (self.window_wide-self.rect_wide):#本作品作者吴宇航
                    self.closestpoint_y = (self.window_wide-self.rect_wide)#本作品作者吴宇航
                    self.collision_sign_y = 1#本作品作者吴宇航
                elif self.ball_y > self.window_wide:#本作品作者吴宇航
                    self.closestpoint_y = self.window_wide#本作品作者吴宇航
                    self.collision_sign_y = 2#本作品作者吴宇航
                else:#本作品作者吴宇航
                    self.closestpoint_y = self.ball_y#本作品作者吴宇航
                    self.collision_sign_y = 3#本作品作者吴宇航
                #定义球拍到圆心最近点与圆心的距离#本作品作者吴宇航
                self.distance = sqrt(pow(self.closestpoint_x-self.ball_x,2)+pow(self.closestpoint_y-self.ball_y,2))#本作品作者吴宇航
                #球在球拍上左、上中、上右3种情况的碰撞检测#本作品作者吴宇航
                if self.distance < self.radius and self.collision_sign_y == 1 and (self.collision_sign_x == 1 or self.collision_sign_x == 2):#本作品作者吴宇航
                    if self.collision_sign_x == 1 and self.move_x > 0:#本作品作者吴宇航
                        self.move_x = - self.move_x#本作品作者吴宇航
                        self.move_y = - self.move_y#本作品作者吴宇航
                    if self.collision_sign_x == 1 and self.move_x < 0:#本作品作者吴宇航
                        self.move_y = - self.move_y#本作品作者吴宇航
                    if self.collision_sign_x == 2 and self.move_x < 0:#本作品作者吴宇航
                        self.move_x = - self.move_x#本作品作者吴宇航
                        self.move_y = - self.move_y#本作品作者吴宇航
                    if self.collision_sign_x == 2 and self.move_x > 0:#本作品作者吴宇航
                        self.move_y = - self.move_y#本作品作者吴宇航
                if self.distance < self.radius and self.collision_sign_y == 1 and self.collision_sign_x == 3:#本作品作者吴宇航
                    self.move_y = - self.move_y#本作品作者吴宇航
                #球在球拍左、右两侧中间的碰撞检测#本作品作者吴宇航
                if self.distance < self.radius and self.collision_sign_y == 3:#本作品作者吴宇航
                    self.move_x = - self.move_x#本作品作者吴宇航
#本作品作者吴宇航
            #球与砖块的碰撞检测#本作品作者吴宇航
            def ball_brick(self):#本作品作者吴宇航
                #定义碰撞标识#本作品作者吴宇航
                self.collision_sign_bx = 0#本作品作者吴宇航
                self.collision_sign_by = 0#本作品作者吴宇航
#本作品作者吴宇航
                if self.ball_x < self.brick_x:#本作品作者吴宇航
                    self.closestpoint_bx = self.brick_x#本作品作者吴宇航
                    self.collision_sign_bx = 1#本作品作者吴宇航
                elif self.ball_x > self.brick_x+self.brick_length:#本作品作者吴宇航
                    self.closestpoint_bx = self.brick_x+self.brick_length#本作品作者吴宇航
                    self.collision_sign_bx = 2#本作品作者吴宇航
                else:#本作品作者吴宇航
                    self.closestpoint_bx = self.ball_x#本作品作者吴宇航
                    self.collision_sign_bx = 3#本作品作者吴宇航
#本作品作者吴宇航
                if self.ball_y < self.brick_y:#本作品作者吴宇航
                    self.closestpoint_by = self.brick_y#本作品作者吴宇航
                    self.collision_sign_by = 1#本作品作者吴宇航
                elif self.ball_y > self.brick_y+self.brick_wide:#本作品作者吴宇航
                    self.closestpoint_by = self.brick_y+self.brick_wide#本作品作者吴宇航
                    self.collision_sign_by = 2#本作品作者吴宇航
                else:#本作品作者吴宇航
                    self.closestpoint_by = self.ball_y#本作品作者吴宇航
                    self.collision_sign_by = 3#本作品作者吴宇航
                #定义砖块到圆心最近点与圆心的距离#本作品作者吴宇航
                self.distanceb = sqrt(pow(self.closestpoint_bx-self.ball_x,2)+pow(self.closestpoint_by-self.ball_y,2))#本作品作者吴宇航
                #球在砖块上左、上中、上右3种情况的碰撞检测#本作品作者吴宇航
                if self.distanceb < self.radius and self.collision_sign_by == 1 and (self.collision_sign_bx == 1 or self.collision_sign_bx == 2):#本作品作者吴宇航
                    if self.collision_sign_bx == 1 and self.move_x > 0:#本作品作者吴宇航
                        self.move_x = - self.move_x#本作品作者吴宇航
                        self.move_y = - self.move_y#本作品作者吴宇航
                    if self.collision_sign_bx == 1 and self.move_x < 0:#本作品作者吴宇航
                        self.move_y = - self.move_y#本作品作者吴宇航
                    if self.collision_sign_bx == 2 and self.move_x < 0:#本作品作者吴宇航
                        self.move_x = - self.move_x#本作品作者吴宇航
                        self.move_y = - self.move_y#本作品作者吴宇航
                    if self.collision_sign_bx == 2 and self.move_x > 0:#本作品作者吴宇航
                        self.move_y = - self.move_y#本作品作者吴宇航
                if self.distanceb < self.radius and self.collision_sign_by == 1 and self.collision_sign_bx == 3:#本作品作者吴宇航
                    self.move_y = - self.move_y#本作品作者吴宇航
                #球在砖块下左、下中、下右3种情况的碰撞检测#本作品作者吴宇航
                if self.distanceb < self.radius and self.collision_sign_by == 2 and (self.collision_sign_bx == 1 or self.collision_sign_bx == 2):#本作品作者吴宇航
                    if self.collision_sign_bx == 1 and self.move_x > 0:#本作品作者吴宇航
                        self.move_x = - self.move_x#本作品作者吴宇航
                        self.move_y = - self.move_y#本作品作者吴宇航
                    if self.collision_sign_bx == 1 and self.move_x < 0:#本作品作者吴宇航
                        self.move_y = - self.move_y#本作品作者吴宇航
                    if self.collision_sign_bx == 2 and self.move_x < 0:#本作品作者吴宇航
                        self.move_x = - self.move_x#本作品作者吴宇航
                        self.move_y = - self.move_y#本作品作者吴宇航
                    if self.collision_sign_bx == 2 and self.move_x > 0:#本作品作者吴宇航
                        self.move_y = - self.move_y#本作品作者吴宇航
                if self.distanceb < self.radius and self.collision_sign_by == 2 and self.collision_sign_bx == 3:#本作品作者吴宇航
                    self.move_y = - self.move_y#本作品作者吴宇航
                #球在砖块左、右两侧中间的碰撞检测#本作品作者吴宇航
                if self.distanceb < self.radius and self.collision_sign_by == 3:#本作品作者吴宇航
                    self.move_x = - self.move_x#本作品作者吴宇航
#本作品作者吴宇航
        class Main(GameWindow,Rect,Ball,Brick,Collision,Score,Win,GameOver):#本作品作者吴宇航
            '''创建主程序类'''#本作品作者吴宇航
            def __init__(self,*args,**kw):      #本作品作者吴宇航
                super(Main,self).__init__(*args,**kw)#本作品作者吴宇航
                super(GameWindow,self).__init__(*args,**kw)#本作品作者吴宇航
                super(Rect,self).__init__(*args,**kw)#本作品作者吴宇航
                super(Ball,self).__init__(*args,**kw)#本作品作者吴宇航
                super(Brick,self).__init__(*args,**kw)#本作品作者吴宇航
                super(Collision,self).__init__(*args,**kw)      #本作品作者吴宇航
                super(Score,self).__init__(*args,**kw)#本作品作者吴宇航
                super(Win,self).__init__(*args,**kw)#本作品作者吴宇航
                #定义游戏开始标识#本作品作者吴宇航
                start_sign = 0#本作品作者吴宇航
#本作品作者吴宇航
                while True:         #本作品作者吴宇航
                    self.backgroud()#本作品作者吴宇航
                    self.rectmove()#本作品作者吴宇航
                    self.countscore()           #本作品作者吴宇航
                    #本作品作者吴宇航
                    if self.over_sign == 1 or self.win_sign == 1:#本作品作者吴宇航
                        break#本作品作者吴宇航
                    #获取游戏窗口状态#本作品作者吴宇航
                    for event in pygame.event.get():#本作品作者吴宇航
                        if event.type == pygame.QUIT:#本作品作者吴宇航
                            pygame.quit()#本作品作者吴宇航
                            fasdasdf1()#本作品作者吴宇航
                        if event.type == MOUSEBUTTONDOWN:#本作品作者吴宇航
                            pressed_array = pygame.mouse.get_pressed()#本作品作者吴宇航
                            if pressed_array[0]:#本作品作者吴宇航
                                start_sign = 1#本作品作者吴宇航
                    if start_sign == 0:#本作品作者吴宇航
                        self.ballready()#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        self.ballmove()#本作品作者吴宇航
#本作品作者吴宇航
                    self.brickarrange()#本作品作者吴宇航
#本作品作者吴宇航
                    #更新游戏窗口#本作品作者吴宇航
                    pygame.display.update()#本作品作者吴宇航
                    #控制游戏窗口刷新频率#本作品作者吴宇航
                    time.sleep(0.010)#本作品作者吴宇航
#本作品作者吴宇航
        if __name__ == '__main__':#本作品作者吴宇航
            pygame.init()#本作品作者吴宇航
            pygame.font.init()#本作品作者吴宇航
            catchball = Main()#本作品作者吴宇航
    elif dakai == "music":#本作品作者吴宇航
         #本作品作者吴宇航
        #本作品作者吴宇航
#本作品作者吴宇航
        class MP3Player(QWidget):#本作品作者吴宇航
            def __init__(self):#本作品作者吴宇航
                super().__init__()#本作品作者吴宇航
#本作品作者吴宇航
                self.startTimeLabel = QLabel('00:00')#本作品作者吴宇航
                self.endTimeLabel = QLabel('00:00')#本作品作者吴宇航
                self.slider = QSlider(Qt.Horizontal, self)#本作品作者吴宇航
                self.PlayModeBtn = QPushButton(self)#本作品作者吴宇航
                self.playBtn = QPushButton(self)#本作品作者吴宇航
                self.prevBtn = QPushButton(self)#本作品作者吴宇航
                self.nextBtn = QPushButton(self)#本作品作者吴宇航
                self.openBtn = QPushButton(self)#本作品作者吴宇航
                self.musicList = QListWidget()#本作品作者吴宇航
                self.song_formats = ['mp3', 'm4a', 'flac', 'wav', 'ogg']#本作品作者吴宇航
                self.songs_list = []#本作品作者吴宇航
                self.cur_playing_song = ''#本作品作者吴宇航
                self.is_pause = True#本作品作者吴宇航
                self.player = QMediaPlayer()#本作品作者吴宇航
                self.is_switching = False#本作品作者吴宇航
                self.playMode = 0#本作品作者吴宇航
                self.settingfilename = 'config.ini'#本作品作者吴宇航
                self.textLable = QLabel('前进的路上，也要记得欣赏沿途的风景呀!')#本作品作者吴宇航
                self.infoLabel = QLabel('Mculover666 v2.0.0')#本作品作者吴宇航
#本作品作者吴宇航
                self.playBtn.setStyleSheet("QPushButton{border-image: url(resource/image/play.png)}")#本作品作者吴宇航
                self.playBtn.setFixedSize(48, 48)#本作品作者吴宇航
                self.nextBtn.setStyleSheet("QPushButton{border-image: url(resource/image/next.png)}")#本作品作者吴宇航
                self.nextBtn.setFixedSize(48, 48)#本作品作者吴宇航
                self.prevBtn.setStyleSheet("QPushButton{border-image: url(resource/image/prev.png)}")#本作品作者吴宇航
                self.prevBtn.setFixedSize(48, 48)#本作品作者吴宇航
                self.openBtn.setStyleSheet("QPushButton{border-image: url(resource/image/open.png)}")#本作品作者吴宇航
                self.openBtn.setFixedSize(24, 24)#本作品作者吴宇航
                self.PlayModeBtn.setStyleSheet("QPushButton{border-image: url(resource/image/sequential.png)}")#本作品作者吴宇航
                self.PlayModeBtn.setFixedSize(24, 24)#本作品作者吴宇航
#本作品作者吴宇航
                self.timer = QTimer(self)#本作品作者吴宇航
                self.timer.start(1000)#本作品作者吴宇航
                self.timer.timeout.connect(self.playByMode)#本作品作者吴宇航
#本作品作者吴宇航
                self.hBoxSlider = QHBoxLayout()#本作品作者吴宇航
                self.hBoxSlider.addWidget(self.startTimeLabel)#本作品作者吴宇航
                self.hBoxSlider.addWidget(self.slider)#本作品作者吴宇航
                self.hBoxSlider.addWidget(self.endTimeLabel)#本作品作者吴宇航
#本作品作者吴宇航
                self.hBoxButton = QHBoxLayout()#本作品作者吴宇航
                self.hBoxButton.addWidget(self.PlayModeBtn)#本作品作者吴宇航
                self.hBoxButton.addStretch(1)#本作品作者吴宇航
                self.hBoxButton.addWidget(self.prevBtn)#本作品作者吴宇航
                self.hBoxButton.addWidget(self.playBtn)#本作品作者吴宇航
                self.hBoxButton.addWidget(self.nextBtn)#本作品作者吴宇航
                self.hBoxButton.addStretch(1)#本作品作者吴宇航
                self.hBoxButton.addWidget(self.openBtn)#本作品作者吴宇航
#本作品作者吴宇航
                self.vBoxControl = QVBoxLayout()#本作品作者吴宇航
                self.vBoxControl.addLayout(self.hBoxSlider)#本作品作者吴宇航
                self.vBoxControl.addLayout(self.hBoxButton)#本作品作者吴宇航
#本作品作者吴宇航
                self.hBoxAbout = QHBoxLayout()#本作品作者吴宇航
                self.hBoxAbout.addWidget(self.textLable)#本作品作者吴宇航
                self.hBoxAbout.addStretch(1)#本作品作者吴宇航
                self.hBoxAbout.addWidget(self.infoLabel)#本作品作者吴宇航
#本作品作者吴宇航
                self.vboxMain = QVBoxLayout()#本作品作者吴宇航
                self.vboxMain.addWidget(self.musicList)#本作品作者吴宇航
                self.vboxMain.addLayout(self.vBoxControl)#本作品作者吴宇航
                self.vboxMain.addLayout(self.hBoxAbout)#本作品作者吴宇航
                #本作品作者吴宇航
                self.setLayout(self.vboxMain)#本作品作者吴宇航
#本作品作者吴宇航
                self.openBtn.clicked.connect(self.openMusicFloder)#本作品作者吴宇航
                self.playBtn.clicked.connect(self.playMusic)#本作品作者吴宇航
                self.prevBtn.clicked.connect(self.prevMusic)#本作品作者吴宇航
                self.nextBtn.clicked.connect(self.nextMusic)#本作品作者吴宇航
                self.musicList.itemDoubleClicked.connect(self.doubleClicked)#本作品作者吴宇航
                self.slider.sliderMoved[int].connect(lambda: self.player.setPosition(self.slider.value()))#本作品作者吴宇航
                self.PlayModeBtn.clicked.connect(self.playModeSet)#本作品作者吴宇航
#本作品作者吴宇航
                self.loadingSetting()#本作品作者吴宇航
#本作品作者吴宇航
                self.initUI()#本作品作者吴宇航
#本作品作者吴宇航
            # 初始化界面#本作品作者吴宇航
            def initUI(self):#本作品作者吴宇航
                self.resize(600, 400)#本作品作者吴宇航
                self.center()#本作品作者吴宇航
                self.setWindowTitle('音乐播放器')   #本作品作者吴宇航
                self.setWindowIcon(QIcon('resource/image/favicon.ico'))#本作品作者吴宇航
                self.show()#本作品作者吴宇航
                #本作品作者吴宇航
            # 窗口显示居中#本作品作者吴宇航
            def center(self):#本作品作者吴宇航
                qr = self.frameGeometry()#本作品作者吴宇航
                cp = QDesktopWidget().availableGeometry().center()#本作品作者吴宇航
                qr.moveCenter(cp)#本作品作者吴宇航
                self.move(qr.topLeft())#本作品作者吴宇航
#本作品作者吴宇航
            # 打开文件夹#本作品作者吴宇航
            def openMusicFloder(self):#本作品作者吴宇航
                self.cur_path = QFileDialog.getExistingDirectory(self, "选取音乐文件夹", './')#本作品作者吴宇航
                if self.cur_path:#本作品作者吴宇航
                    self.showMusicList()#本作品作者吴宇航
                    self.cur_playing_song = ''#本作品作者吴宇航
                    self.startTimeLabel.setText('00:00')#本作品作者吴宇航
                    self.endTimeLabel.setText('00:00')#本作品作者吴宇航
                    self.slider.setSliderPosition(0)#本作品作者吴宇航
                    self.updateSetting()#本作品作者吴宇航
                    self.is_pause = True#本作品作者吴宇航
                    self.playBtn.setStyleSheet("QPushButton{border-image: url(resource/image/play.png)}")#本作品作者吴宇航
            #本作品作者吴宇航
            # 显示音乐列表#本作品作者吴宇航
            def showMusicList(self):#本作品作者吴宇航
                self.musicList.clear()#本作品作者吴宇航
                for song in os.listdir(self.cur_path):#本作品作者吴宇航
                    if song.split('.')[-1] in self.song_formats:#本作品作者吴宇航
                        self.songs_list.append([song, os.path.join(self.cur_path, song).replace('\\', '/')])#本作品作者吴宇航
                        self.musicList.addItem(song)#本作品作者吴宇航
                self.musicList.setCurrentRow(0)#本作品作者吴宇航
                if self.songs_list:#本作品作者吴宇航
                        self.cur_playing_song = self.songs_list[self.musicList.currentRow()][-1]#本作品作者吴宇航
#本作品作者吴宇航
            # 提示#本作品作者吴宇航
            def Tips(self, message):#本作品作者吴宇航
                QMessageBox.about(self, "提示", message)#本作品作者吴宇航
#本作品作者吴宇航
            # 设置当前播放的音乐#本作品作者吴宇航
            def setCurPlaying(self):#本作品作者吴宇航
                self.cur_playing_song = self.songs_list[self.musicList.currentRow()][-1]#本作品作者吴宇航
                self.player.setMedia(QMediaContent(QUrl(self.cur_playing_song)))#本作品作者吴宇航
#本作品作者吴宇航
            # 播放/暂停播放#本作品作者吴宇航
            def playMusic(self):#本作品作者吴宇航
                if self.musicList.count() == 0:#本作品作者吴宇航
                        self.Tips('当前路径内无可播放的音乐文件')#本作品作者吴宇航
                        return#本作品作者吴宇航
                if not self.player.isAudioAvailable():#本作品作者吴宇航
                        self.setCurPlaying()#本作品作者吴宇航
                if self.is_pause or self.is_switching:#本作品作者吴宇航
                        self.player.play()#本作品作者吴宇航
                        self.is_pause = False#本作品作者吴宇航
                        self.playBtn.setStyleSheet("QPushButton{border-image: url(resource/image/pause.png)}")#本作品作者吴宇航
                elif (not self.is_pause) and (not self.is_switching):#本作品作者吴宇航
                        self.player.pause()#本作品作者吴宇航
                        self.is_pause = True#本作品作者吴宇航
                        self.playBtn.setStyleSheet("QPushButton{border-image: url(resource/image/play.png)}")#本作品作者吴宇航
            #本作品作者吴宇航
            # 上一曲#本作品作者吴宇航
            def prevMusic(self):#本作品作者吴宇航
                self.slider.setValue(0)#本作品作者吴宇航
                if self.musicList.count() == 0:#本作品作者吴宇航
                    self.Tips('当前路径内无可播放的音乐文件')#本作品作者吴宇航
                    return#本作品作者吴宇航
                pre_row = self.musicList.currentRow()-1 if self.musicList.currentRow() != 0 else self.musicList.count() - 1#本作品作者吴宇航
                self.musicList.setCurrentRow(pre_row)#本作品作者吴宇航
                self.is_switching = True#本作品作者吴宇航
                self.setCurPlaying()#本作品作者吴宇航
                self.playMusic()#本作品作者吴宇航
                self.is_switching = False#本作品作者吴宇航
#本作品作者吴宇航
            # 下一曲#本作品作者吴宇航
            def nextMusic(self):#本作品作者吴宇航
                self.slider.setValue(0)#本作品作者吴宇航
                if self.musicList.count() == 0:#本作品作者吴宇航
                    self.Tips('当前路径内无可播放的音乐文件')#本作品作者吴宇航
                    return#本作品作者吴宇航
                next_row = self.musicList.currentRow()+1 if self.musicList.currentRow() != self.musicList.count()-1 else 0#本作品作者吴宇航
                self.musicList.setCurrentRow(next_row)#本作品作者吴宇航
                self.is_switching = True#本作品作者吴宇航
                self.setCurPlaying()#本作品作者吴宇航
                self.playMusic()#本作品作者吴宇航
                self.is_switching = False  #本作品作者吴宇航
#本作品作者吴宇航
            # 双击歌曲名称播放音乐#本作品作者吴宇航
            def doubleClicked(self):#本作品作者吴宇航
                self.slider.setValue(0)#本作品作者吴宇航
                self.is_switching = True#本作品作者吴宇航
                self.setCurPlaying()#本作品作者吴宇航
                self.playMusic()#本作品作者吴宇航
                self.is_switching = False#本作品作者吴宇航
#本作品作者吴宇航
            # 根据播放模式自动播放，并刷新进度条#本作品作者吴宇航
            def playByMode(self):#本作品作者吴宇航
                # 刷新进度条#本作品作者吴宇航
                if (not self.is_pause) and (not self.is_switching):#本作品作者吴宇航
                    self.slider.setMinimum(0)#本作品作者吴宇航
                    self.slider.setMaximum(self.player.duration())#本作品作者吴宇航
                    self.slider.setValue(self.slider.value() + 1000)#本作品作者吴宇航
                #本作品作者吴宇航
                # 顺序播放#本作品作者吴宇航
                if (self.playMode == 0) and (not self.is_pause) and (not self.is_switching):#本作品作者吴宇航
                    if self.musicList.count() == 0:#本作品作者吴宇航
                        return#本作品作者吴宇航
                    if self.player.position() == self.player.duration():#本作品作者吴宇航
                        self.nextMusic()#本作品作者吴宇航
                # 单曲循环#本作品作者吴宇航
                elif (self.playMode == 1) and (not self.is_pause) and (not self.is_switching):#本作品作者吴宇航
                    if self.musicList.count() == 0:#本作品作者吴宇航
                        return#本作品作者吴宇航
                    if self.player.position() == self.player.duration():#本作品作者吴宇航
                        self.is_switching = True#本作品作者吴宇航
                        self.setCurPlaying()#本作品作者吴宇航
                        self.slider.setValue(0)#本作品作者吴宇航
                        self.playMusic()#本作品作者吴宇航
                        self.is_switching = False#本作品作者吴宇航
                # 随机播放#本作品作者吴宇航
                elif (self.playMode == 2) and (not self.is_pause) and (not self.is_switching):#本作品作者吴宇航
                    if self.musicList.count() == 0:#本作品作者吴宇航
                        return#本作品作者吴宇航
                    if self.player.position() == self.player.duration():#本作品作者吴宇航
                        self.is_switching = True#本作品作者吴宇航
                        self.musicList.setCurrentRow(random.randint(0, self.musicList.count()-1))#本作品作者吴宇航
                        self.setCurPlaying()#本作品作者吴宇航
                        self.slider.setValue(0)#本作品作者吴宇航
                        self.playMusic()#本作品作者吴宇航
                        self.is_switching = False#本作品作者吴宇航
#本作品作者吴宇航
            # 更新配置文件#本作品作者吴宇航
            def updateSetting(self):#本作品作者吴宇航
                config = configparser.ConfigParser()#本作品作者吴宇航
                config.read(self.settingfilename)#本作品作者吴宇航
                if not os.path.isfile(self.settingfilename):#本作品作者吴宇航
                    config.add_section('MP3Player')#本作品作者吴宇航
                config.set('MP3Player', 'PATH', self.cur_path)#本作品作者吴宇航
                config.write(open(self.settingfilename, 'w'))#本作品作者吴宇航
#本作品作者吴宇航
            # 加载配置文件#本作品作者吴宇航
            def loadingSetting(self):#本作品作者吴宇航
                config = configparser.ConfigParser()#本作品作者吴宇航
                config.read(self.settingfilename)#本作品作者吴宇航
                if not os.path.isfile(self.settingfilename):#本作品作者吴宇航
                    return#本作品作者吴宇航
                self.cur_path = config.get('MP3Player', 'PATH')#本作品作者吴宇航
                self.showMusicList()#本作品作者吴宇航
            #本作品作者吴宇航
            # 播放模式设置#本作品作者吴宇航
            def playModeSet(self):#本作品作者吴宇航
                # 设置为单曲循环模式#本作品作者吴宇航
                if self.playMode == 0:#本作品作者吴宇航
                    self.playMode = 1#本作品作者吴宇航
                    self.PlayModeBtn.setStyleSheet("QPushButton{border-image: url(resource/image/circulation.png)}")#本作品作者吴宇航
                # 设置为随机播放模式#本作品作者吴宇航
                elif self.playMode == 1:#本作品作者吴宇航
                    self.playMode = 2#本作品作者吴宇航
                    self.PlayModeBtn.setStyleSheet("QPushButton{border-image: url(resource/image/random.png)}")#本作品作者吴宇航
                # 设置为顺序播放模式#本作品作者吴宇航
                elif self.playMode == 2:#本作品作者吴宇航
                    self.playMode = 0#本作品作者吴宇航
                    self.PlayModeBtn.setStyleSheet("QPushButton{border-image: url(resource/image/sequential.png)}")#本作品作者吴宇航
#本作品作者吴宇航
            # 确认用户是否要真正退出#本作品作者吴宇航
            def closeEvent(self, event):#本作品作者吴宇航
                reply = QMessageBox.question(self, 'Message',#本作品作者吴宇航
                    "确定要退出吗？", QMessageBox.Yes | #本作品作者吴宇航
                    QMessageBox.No, QMessageBox.No)#本作品作者吴宇航
                if reply == QMessageBox.Yes:#本作品作者吴宇航
                    event.accept()#本作品作者吴宇航
                    fasdasdf1()#本作品作者吴宇航
                else:#本作品作者吴宇航
                    event.ignore()#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
        from PyQt5.QtWidgets import (QApplication)#本作品作者吴宇航
#本作品作者吴宇航
        if __name__ == '__main__':#本作品作者吴宇航
            app = QApplication(sys.argv)#本作品作者吴宇航
            ex = MP3Player()#本作品作者吴宇航
            sys.exit(app.exec_())#本作品作者吴宇航
            #本作品作者吴宇航
    elif dakai == "dazi":#本作品作者吴宇航
        # pygame初始化#本作品作者吴宇航
        pygame.init()#本作品作者吴宇航
        pygame.display.set_caption("打字游戏")#本作品作者吴宇航
        screen = pygame.display.set_mode((800, 300))#本作品作者吴宇航
#本作品作者吴宇航
        # 加载游戏所需要的各项图片素材#本作品作者吴宇航
        bgimg = pygame.image.load("bg3.png")#本作品作者吴宇航
        bgimg = pygame.transform.scale(bgimg, (800, 300))#本作品作者吴宇航
#本作品作者吴宇航
        # 加载声音特效#本作品作者吴宇航
        #本作品作者吴宇航
        mytext = pygame.font.SysFont("kaiti",30)#本作品作者吴宇航
        # 加载和播放背景音乐#本作品作者吴宇航
    #本作品作者吴宇航
#本作品作者吴宇航
        letterFont = pygame.font.SysFont(None, 80)#本作品作者吴宇航
        letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",#本作品作者吴宇航
                   "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]#本作品作者吴宇航
#本作品作者吴宇航
        word = random.choice(letters)#本作品作者吴宇航
        x = random.randint(100, 700)#本作品作者吴宇航
        y = 300  # 中间位置#本作品作者吴宇航
        letter = {"word": word, "color": "blue", "x": x, "y": y}#本作品作者吴宇航
        fenshu = 0#本作品作者吴宇航
        letterWait = []  # 字母在letterWait中等待被消除#本作品作者吴宇航
        letterWait.append(letter)#本作品作者吴宇航
        add_time = time.time()  # 记录初始添加时间#本作品作者吴宇航
#本作品作者吴宇航
        while True:#本作品作者吴宇航
            for event in pygame.event.get():#本作品作者吴宇航
                if event.type == pygame.QUIT:#本作品作者吴宇航
                    pygame.quit()#本作品作者吴宇航
                    fasdasdf1()#本作品作者吴宇航
#本作品作者吴宇航
                if event.type == pygame.KEYDOWN:#本作品作者吴宇航
                    #本作品作者吴宇航
                    for letter in letterWait:#本作品作者吴宇航
                        #作答区域 补全48行代码,按键消除字母#本作品作者吴宇航
                        # ================================================================#本作品作者吴宇航
                        if chr(event.key) == letter["word"]:#本作品作者吴宇航
                            fenshu = fenshu + 1#本作品作者吴宇航
                            letterWait.remove(letter)#本作品作者吴宇航
                        else:#本作品作者吴宇航
                            fenshu = fenshu - 1#本作品作者吴宇航
                        # ================================================================#本作品作者吴宇航
            screen.blit(bgimg, (0, 0))#本作品作者吴宇航
#本作品作者吴宇航
            now = time.time()  # 当前时间#本作品作者吴宇航
            if now - add_time > 2:  # 如果时间间隔超过两秒，就制作一个新的字母，添加到letterWait中#本作品作者吴宇航
                word = random.choice(letters)#本作品作者吴宇航
                x = random.randint(100, 700)#本作品作者吴宇航
                y = 300#本作品作者吴宇航
                letter = {"word": word, "x": x, "y": y}#本作品作者吴宇航
                letterWait.append(letter)#本作品作者吴宇航
                add_time = now  # 每次向letterWait中添加一个新字母，就更新添加时间为当前时间#本作品作者吴宇航
#本作品作者吴宇航
            # 遍历letterWait，绘制每一个字母#本作品作者吴宇航
            for letter in letterWait:#本作品作者吴宇航
                word = letter["word"]#本作品作者吴宇航
                x = letter["x"]#本作品作者吴宇航
                y = letter["y"]#本作品作者吴宇航
                textImage = letterFont.render(word, True, (255, 255, 255))#本作品作者吴宇航
                screen.blit(textImage, (x, y))#本作品作者吴宇航
#本作品作者吴宇航
                # 字母上移#本作品作者吴宇航
                #作答区域 补充第73行代码：完成字母上移（y值减去一个数字）#本作品作者吴宇航
                # ================================================================#本作品作者吴宇航
                letter["y"] = y - 1#本作品作者吴宇航
                # ================================================================#本作品作者吴宇航
#本作品作者吴宇航
                #作答区域 补充78行代码，当字母（y值）超出画布时，列表移除字母字典#本作品作者吴宇航
                # ================================================================#本作品作者吴宇航
                if y <= 0:#本作品作者吴宇航
                    fenshu = fenshu - 1#本作品作者吴宇航
                    letterWait.remove(letter)#本作品作者吴宇航
            if fenshu <= 0:#本作品作者吴宇航
                fenshu = 0#本作品作者吴宇航
            if fenshu >= 100:#本作品作者吴宇航
                pygame.quit()#本作品作者吴宇航
                print("你赢了！")#本作品作者吴宇航
                # ================================================================#本作品作者吴宇航
            text = mytext.render("分数" + str(fenshu),True,(0,0,0))#本作品作者吴宇航
            screen.blit(text,(20,20))#本作品作者吴宇航
            pygame.display.update()#本作品作者吴宇航
            time.sleep(0.02)#本作品作者吴宇航
    elif dakai == "shijian":#本作品作者吴宇航
        def print_text(font,x,y,text,color=(255,255,255)):#本作品作者吴宇航
            imgText=font.render(text,True,color)#本作品作者吴宇航
            screen.blit(imgText,(x,y))#本作品作者吴宇航
        def wrap_angle(angle):#本作品作者吴宇航
            return angle % 360#本作品作者吴宇航
        pygame.init()#本作品作者吴宇航
        screen=pygame.display.set_mode([600,500])#本作品作者吴宇航
        pygame.display.set_caption("AnalogClock")#本作品作者吴宇航
        font = pygame.font.Font(None,36)#本作品作者吴宇航
        orange=220,180,0#本作品作者吴宇航
        white=255,255,255#本作品作者吴宇航
        yellow=255,255,0#本作品作者吴宇航
        pink=255,100,100#本作品作者吴宇航
        pos_x=300#本作品作者吴宇航
        pos_y=250#本作品作者吴宇航
        radius=250#本作品作者吴宇航
        angle=260#本作品作者吴宇航
        while True:#本作品作者吴宇航
            screen.fill([0,0,0])#本作品作者吴宇航
            for event in pygame.event.get():#本作品作者吴宇航
                if event.type==QUIT:#本作品作者吴宇航
                    sys.exit()#本作品作者吴宇航
            keys=pygame.key.get_pressed()#本作品作者吴宇航
            if keys[K_ESCAPE]:#本作品作者吴宇航
                sys.exit()#本作品作者吴宇航
                screen.fill([0,0,100])#本作品作者吴宇航
            pygame.draw.circle(screen,white,(pos_x,pos_y),radius,6)#本作品作者吴宇航
            for n in range(1,13):#本作品作者吴宇航
                angle=radians(n*(360/12)-90)#本作品作者吴宇航
                x=cos(angle)*(radius-20)-10#本作品作者吴宇航
                y=sin(angle)*(radius-20)-10#本作品作者吴宇航
                print_text(font, pos_x+x, pos_y+y, str(n))#本作品作者吴宇航
            today=datetime.today()#本作品作者吴宇航
            hours=today.hour % 12#本作品作者吴宇航
            minutes=today.minute#本作品作者吴宇航
            seconds=today.second#本作品作者吴宇航
            hour_angle=wrap_angle(hours*(360/12)-90)#本作品作者吴宇航
            hour_angle=radians(hour_angle)#本作品作者吴宇航
            hour_x=cos(hour_angle)*(radius-80)#本作品作者吴宇航
            hour_y=sin(hour_angle)*(radius-80)#本作品作者吴宇航
            target=(pos_x+hour_x,pos_y+hour_y)#本作品作者吴宇航
            pygame.draw.line(screen,pink,(pos_x,pos_y),target,25)#本作品作者吴宇航
            min_angle=wrap_angle(minutes*(260/60)-90)#本作品作者吴宇航
            min_angle=radians(min_angle)#本作品作者吴宇航
            min_x=cos(min_angle)*(radius-60)#本作品作者吴宇航
            min_y=sin(min_angle)*(radius-60)#本作品作者吴宇航
            target=(pos_x+min_x,pos_y+min_y)#本作品作者吴宇航
            pygame.draw.line(screen,orange,(pos_x,pos_y),target,12)#本作品作者吴宇航
            sec_angle=wrap_angle(seconds*(360/60)-90)#本作品作者吴宇航
            sec_angle=radians(sec_angle)#本作品作者吴宇航
            sec_x=cos(sec_angle)*(radius-40)#本作品作者吴宇航
            sec_y=sin(sec_angle)*(radius-40)#本作品作者吴宇航
            target=(pos_x+sec_x,pos_y+sec_y)#本作品作者吴宇航
            pygame.draw.line(screen,yellow,(pos_x,pos_y),target,6)#本作品作者吴宇航
            pygame.draw.circle(screen,white,(pos_x,pos_y),20)#本作品作者吴宇航
            print_text(font, 0, 0, str(hours)+":"+str(minutes)+":"+str(seconds))#本作品作者吴宇航
            pygame.display.update()#本作品作者吴宇航
    elif dakai == "shipin":#本作品作者吴宇航
        messagebox.showinfo("提示","该功能维护中，暂不开放")#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
    #     class Pro:#本作品作者吴宇航
    #         header_ai={'Referer': 'http://www.iqiyi.com/',#本作品作者吴宇航
    #                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.17 Safari/537.36'#本作品作者吴宇航
#本作品作者吴宇航
    #         }#本作品作者吴宇航
    #         header_you={'Referer': 'http://list.youku.com/category/video','User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}#本作品作者吴宇航
    #         header_pp = {'Referer': 'http://list.pptv.com/',#本作品作者吴宇航
    #                   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}#本作品作者吴宇航
    #         way=False#本作品作者吴宇航
    #         def __init__(self):#本作品作者吴宇航
    #             pass#本作品作者吴宇航
#本作品作者吴宇航
    #         def search_movies_type(self,u_name,u_type,page):#两个参数 根据状态输出规则#本作品作者吴宇航
    #             dic1 = {'m': 1, 't': 2, 'z': 6, 'd': 4, 'j': 3}#本作品作者吴宇航
    #             dic2 = {'m': 96, 't': 97, 'z': 85, 'd': 100, 'j': 84}#本作品作者吴宇航
    #             dic3 = {'m': 1, 't': 2, 'z': 4, 'd': 3, 'j': 210548}#本作品作者吴宇航
    #             headers={}#本作品作者吴宇航
    #             #爱奇艺 a/电影m:1 t:2 z:6 d:4 j:3  优酷y / m:96 t:97 z:85 d:100 j:84 pptv  p/m:1 t:2 z:4 d:3 j:210548#本作品作者吴宇航
    #             url, pa_movie_title, pa_movie_url, pa_move_pic='','','',''#本作品作者吴宇航
    #             url_aiqiyi='http://list.iqiyi.com/www/{}/-------------24-{}-1-iqiyi--.html'.format(dic1[u_type],page)#本作品作者吴宇航
    #             url_youku='https://list.youku.com/category/show/c_{}_s_1_d_1_p_{}.html'.format(dic2[u_type],page)#本作品作者吴宇航
    #             # url_pptv='http://list.pptv.com/category/type_{}.html'.format(dic3[u_type])#本作品作者吴宇航
    #             url_pptv='http://list.pptv.com/channel_list.html?page={}&type={}'.format(page,dic3[u_type])#本作品作者吴宇航
    #             pa_ai_movie_title = '//div[@class="site-piclist_pic"]/a[@class="site-piclist_pic_link"]/@title'#本作品作者吴宇航
    #             pa_ai_movie_url = '//div[@class="site-piclist_pic"]/a[@class="site-piclist_pic_link"]/@href'#本作品作者吴宇航
    #             pa_ai_movie_pic = '//div[@class="site-piclist_pic"]/a[@class="site-piclist_pic_link"]/img/@src'#本作品作者吴宇航
    #             pa_you_movie_title='//div[@class="p-thumb"]/a/@title'#本作品作者吴宇航
    #             pa_you_movie_url='//div[@class="p-thumb"]/a/@href'#本作品作者吴宇航
    #             pa_you_movie_pic='//div[@class="p-thumb"]/img[@class="quic"]/@src'#本作品作者吴宇航
    #             pa_pp_movie_title='//li/a[@class="ui-list-ct"]/@title'#本作品作者吴宇航
    #             pa_pp_movie_url='//li/a[@class="ui-list-ct"]/@href'#本作品作者吴宇航
    #             pa_pp_movie_pic='//li/a[@class="ui-list-ct"]/p[@class="ui-pic"]/img/@data-src2'#本作品作者吴宇航
    #             if u_name=="a":#如果是爱奇艺#本作品作者吴宇航
    #                 url=url_aiqiyi#本作品作者吴宇航
    #                 pa_movie_title=pa_ai_movie_title#本作品作者吴宇航
    #                 pa_movie_url=pa_ai_movie_url#本作品作者吴宇航
    #                 pa_move_pic=pa_ai_movie_pic#本作品作者吴宇航
    #                 headers=self.header_ai#本作品作者吴宇航
    #             elif u_name=="y":#如果是优酷#本作品作者吴宇航
    #                 url=url_youku#本作品作者吴宇航
    #                 pa_movie_title=pa_you_movie_title#本作品作者吴宇航
    #                 pa_movie_url=pa_you_movie_url#本作品作者吴宇航
    #                 pa_move_pic=pa_you_movie_pic#本作品作者吴宇航
    #                 headers=self.header_you#本作品作者吴宇航
#本作品作者吴宇航
    #             elif u_name=="p":#如果是PPTV#本作品作者吴宇航
    #                 url=url_pptv#本作品作者吴宇航
    #                 pa_movie_title=pa_pp_movie_title#本作品作者吴宇航
    #                 pa_movie_url=pa_pp_movie_url#本作品作者吴宇航
    #                 pa_move_pic=pa_pp_movie_pic#本作品作者吴宇航
    #                 headers=self.header_pp#本作品作者吴宇航
#本作品作者吴宇航
    #             return url,pa_movie_title,pa_movie_url,pa_move_pic,headers#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
    #         def get_movie_res(self,u_name,u_type,page):#输出电影名 链接 图片#本作品作者吴宇航
    #             url, pa_movie_title, pa_movie_url, pa_move_pic,headers=self.search_movies_type(u_name,u_type,page)#本作品作者吴宇航
    #             res=requests.get(url=url,headers=headers).content.decode('utf-8')#本作品作者吴宇航
    #             # print(res)#本作品作者吴宇航
    #             html=etree.HTML(res)#本作品作者吴宇航
    #             movie_url=html.xpath(pa_movie_url)#本作品作者吴宇航
    #             movie_title=html.xpath(pa_movie_title)#本作品作者吴宇航
    #             movie_src_pic=html.xpath(pa_move_pic)#本作品作者吴宇航
    #             print(len(movie_title),movie_title)#本作品作者吴宇航
    #             print(len(movie_url),movie_url)#本作品作者吴宇航
    #             print(len(movie_src_pic),movie_src_pic)#本作品作者吴宇航
    #             return movie_url,movie_title,movie_src_pic#本作品作者吴宇航
#本作品作者吴宇航
    #         def change_urlink(self,lis):#本作品作者吴宇航
    #             for i in range(len(lis)):#本作品作者吴宇航
    #                 if '\\' in lis[i]:#本作品作者吴宇航
    #                     lis[i] = lis[i].replace('\\', '')#本作品作者吴宇航
    #             # print(lis)#本作品作者吴宇航
    #             return lis#本作品作者吴宇航
#本作品作者吴宇航
    #         def change_youku_link(self,urls):#本作品作者吴宇航
    #             pa_link='//.+[.]html'#本作品作者吴宇航
    #             if re.match(pa_link,urls):#本作品作者吴宇航
    #                 urls='http:'+urls#本作品作者吴宇航
    #             return urls#本作品作者吴宇航
#本作品作者吴宇航
    #         def get_more_tv_urls(self,url,u_name,u_type):#获取电视剧分集链接#本作品作者吴宇航
    #             tv_dic_new = {}#本作品作者吴宇航
    #             if u_name == 'y':#本作品作者吴宇航
    #                 url=self.change_youku_link(url)#本作品作者吴宇航
    #                 res = requests.get(url, headers=self.header_you).text.encode(encoding='utf-8').decode('utf-8')#本作品作者吴宇航
    #                 html = etree.HTML(res)#本作品作者吴宇航
    #                 print(res)#本作品作者吴宇航
    #                 if u_type=="m" or u_type=="t":#本作品作者吴宇航
    #                     self.tv_more_title = html.xpath('//div[@class="item item-num"]/@title')#本作品作者吴宇航
    #                     self.tv_more_url = html.xpath('//div[@class="item item-num"]/a[@class="sn"]/@href')#本作品作者吴宇航
    #                 elif u_type=="d":#本作品作者吴宇航
    #                     self.tv_more_title = html.xpath('//div[@class="item item-txt"]/@title')#本作品作者吴宇航
    #                     self.tv_more_url = html.xpath('//div[@class="item item-txt"]/a[@class="sn"]/@href')#本作品作者吴宇航
    #                 elif u_type=="z":#本作品作者吴宇航
    #                     self.tv_more_title = html.xpath('//div[@class="item item-cover"]/@title')#本作品作者吴宇航
    #                     self.tv_more_url = html.xpath('//div[@class="item item-cover"]/a/@href')#本作品作者吴宇航
    #                 elif u_type == "j":#本作品作者吴宇航
    #                     self.tv_more_title = html.xpath('//div[@class="item item-cover current"]/@title')#本作品作者吴宇航
    #                     self.tv_more_url = html.xpath('//div[@class="item item-cover current"]/a/@href')#本作品作者吴宇航
    #             elif u_name == 'a':#本作品作者吴宇航
    #                 res = requests.get(url, headers=self.header_ai).text.encode(encoding='utf-8').decode('utf-8')#本作品作者吴宇航
    #                 html = etree.HTML(res)#本作品作者吴宇航
    #                 print(res)#本作品作者吴宇航
    #                 if u_type=="m" or u_type=="t" or u_type=='d':#本作品作者吴宇航
    #                     self.tv_more_title = html.xpath(#本作品作者吴宇航
    #                         '//ul/li[@data-albumlist-elem="playItem"]/div[@class="site-piclist_pic"]/a[1]/@title')#本作品作者吴宇航
    #                     self.tv_more_url = html.xpath(#本作品作者吴宇航
    #                         '//ul/li[@data-albumlist-elem="playItem"]/div[@class="site-piclist_pic"]/a[1]/@href')#本作品作者吴宇航
    #                 elif u_type=="z" or u_type=="j":#本作品作者吴宇航
    #                     self.tv_more_title = html.xpath('//div[@class="recoAlbumTit"]/a[1]/@title')#本作品作者吴宇航
    #                     self.tv_more_url = html.xpath('//div[@class="recoAlbumTit"]/a[1]/@href')#本作品作者吴宇航
    #             elif u_name == 'p':#本作品作者吴宇航
    #                 res = requests.get(url, headers=self.header_pp).text.encode(encoding='utf-8').decode('utf-8')#本作品作者吴宇航
    #                 # html = etree.HTML(res)#本作品作者吴宇航
    #                 self.tv_more_url2 = re.compile('{"url":"(.+?)"').findall(res)#本作品作者吴宇航
    #                 self.tv_more_url = self.change_urlink(self.tv_more_url2)#本作品作者吴宇航
    #                 self.tv_more_title = ["第{}集".format(x) for x in range(1, len(self.tv_more_url) + 1)]#本作品作者吴宇航
    #             for i, j in zip(self.tv_more_title, self.tv_more_url):#本作品作者吴宇航
    #                 tv_dic_new[i] = j#本作品作者吴宇航
    #             print(len(self.tv_more_title), self.tv_more_title)#本作品作者吴宇航
    #             print(len(self.tv_more_url), self.tv_more_url)#本作品作者吴宇航
    #             print(tv_dic_new)#本作品作者吴宇航
    #             return tv_dic_new#本作品作者吴宇航
#本作品作者吴宇航
    #         def url_change(self,url,flag):#本作品作者吴宇航
    #             pa_url='http://www.iqiyi.com/a_[.+].html'#本作品作者吴宇航
    #             if flag=="0":#通道1#本作品作者吴宇航
    #                 if re.match(pa_url, url):#本作品作者吴宇航
    #                     _url = url.replace('a', 'v')#本作品作者吴宇航
    #                 else:#本作品作者吴宇航
    #                     _url=url#本作品作者吴宇航
    #                 # new_url='http://www.wq114.org/weixin.php?url={}'.format(_url[21:])#本作品作者吴宇航
    #                 new_url='http://www.wq114.org/weixin.php?url={}'.format(_url)#本作品作者吴宇航
    #                 return new_url#本作品作者吴宇航
    #             elif flag == "1":#本作品作者吴宇航
    #                 if re.match(pa_url, url):#本作品作者吴宇航
    #                     _url = url.replace('a', 'v')#本作品作者吴宇航
    #                 else:#本作品作者吴宇航
    #                     _url = url#本作品作者吴宇航
    #                 new_url='http://www.wmxz.wang/video.php?url={}'.format(_url)#本作品作者吴宇航
    #                 return new_url#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
    #         def play_movie(self,url,flag):#本作品作者吴宇航
    #             play_url=self.url_change(url,flag)#本作品作者吴宇航
    #             webbrowser.open(play_url)#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
    #     if __name__ == '__main__':#本作品作者吴宇航
    #         p=Pro()#本作品作者吴宇航
#本作品作者吴宇航
    #     # from urllib.request import urlopen#本作品作者吴宇航
#本作品作者吴宇航
    #     class Movie_app:#本作品作者吴宇航
    #         def __init__(self):#本作品作者吴宇航
    #             self.win=Tk()#本作品作者吴宇航
    #             self.win.geometry('600x420')#本作品作者吴宇航
    #             self.win.title("爱奇艺-优酷-PPTV视频播放下载器V3.1")#本作品作者吴宇航
    #             self.creat_res()#本作品作者吴宇航
    #             self.creat_radiores()#本作品作者吴宇航
    #             self.config()#本作品作者吴宇航
    #             self.page=1#本作品作者吴宇航
    #             self.p=Pro()#本作品作者吴宇航
    #             self.win.mainloop()#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
    #         def creat_res(self):#本作品作者吴宇航
    #             self.temp=StringVar()#url地址#本作品作者吴宇航
    #             self.temp2=StringVar()#本作品作者吴宇航
    #             self.t1=StringVar()#通道#本作品作者吴宇航
    #             self.t3=StringVar()#爱奇艺，优酷，PPTV#本作品作者吴宇航
    #             self.La_title=Label(self.win,text="地址:")#本作品作者吴宇航
    #             self.La_way=Label(self.win,text="选择视频通道:")#本作品作者吴宇航
    #             self.R_way1=Radiobutton(self.win,text="通道A",variable=self.t1,value=True)#本作品作者吴宇航
    #             self.R_way2=Radiobutton(self.win,text="通道B",variable=self.t1,value=False)#本作品作者吴宇航
    #             self.R_aiqiyi=Radiobutton(self.win,text="爱奇艺",variable=self.t3,value="a")#本作品作者吴宇航
    #             self.R_youku=Radiobutton(self.win,text="优酷",variable=self.t3,value="y")#本作品作者吴宇航
    #             self.R_pptv=Radiobutton(self.win,text="PPTV",variable=self.t3,value="p")#本作品作者吴宇航
    #             self.B_play=Button(self.win,text="播放▶")#本作品作者吴宇航
    #             self.B_uppage=Button(self.win,text="上页")#本作品作者吴宇航
    #             self.B_nextpage=Button(self.win,text="下页")#本作品作者吴宇航
    #             self.B_search=Button(self.win,text="♣搜索全站♠")#本作品作者吴宇航
    #             self.La_mesasge=Label(self.win,text="☜  ⇠☸⇢  ☞",bg="pink")#本作品作者吴宇航
    #             self.La_page=Label(self.win,bg="#BFEFFF")#本作品作者吴宇航
    #             self.S_croll=Scrollbar(self.win)#本作品作者吴宇航
    #             self.L_box=Listbox(self.win,bg="#BFEFFF",selectmode=SINGLE)#本作品作者吴宇航
    #             self.E_address=Entry(self.win,textvariable=self.temp)#本作品作者吴宇航
    #             self.La_title.place(x=10,y=50,width=50,height=30)#本作品作者吴宇航
    #             self.E_address.place(x=70,y=50,width=200,height=30)#本作品作者吴宇航
    #             self.B_play.place(x=300,y=50,width=50,height=30)#本作品作者吴宇航
    #             self.R_way1.place(x=160,y=10,width=70,height=30)#本作品作者吴宇航
    #             self.R_way2.place(x=240,y=10,width=70,height=30)#本作品作者吴宇航
    #             self.La_way.place(x=10,y=10,width=100,height=30)#本作品作者吴宇航
    #             self.R_aiqiyi.place(x=20,y=100,width=70,height=30)#本作品作者吴宇航
    #             self.R_youku.place(x=90,y=100,width=70,height=30)#本作品作者吴宇航
    #             self.R_pptv.place(x=160,y=100,width=70,height=30)#本作品作者吴宇航
    #             self.B_search.place(x=252,y=140,width=100,height=30)#本作品作者吴宇航
    #             self.La_mesasge.place(x=80,y=125,width=90,height=20)#本作品作者吴宇航
    #             self.L_box.place(x=10,y=180,width=252,height=230)#本作品作者吴宇航
    #             self.S_croll.place(x=260,y=180,width=20,height=230)#本作品作者吴宇航
    #             self.B_uppage.place(x=10,y=140,width=50,height=30)#本作品作者吴宇航
    #             self.B_nextpage.place(x=180,y=140,width=50,height=30)#本作品作者吴宇航
    #             self.La_page.place(x=80,y=150,width=90,height=28)#本作品作者吴宇航
#本作品作者吴宇航
    #         def creat_radiores(self):#本作品作者吴宇航
    #             self.movie=StringVar()#电影#本作品作者吴宇航
    #             self.S_croll2=Scrollbar()#分集#本作品作者吴宇航
    #             self.La_pic=Label(self.win,bg="#E6E6FA")#本作品作者吴宇航
    #             self.La_movie_message=Listbox(self.win,bg="#7EC0EE")#本作品作者吴宇航
    #             self.R_movie=Radiobutton(self.win,text="电影",variable=self.movie,value="m")#本作品作者吴宇航
    #             self.tv=Radiobutton(self.win,text="电视剧",variable=self.movie,value="t")#本作品作者吴宇航
    #             self.zhongyi=Radiobutton(self.win,text="综艺",variable=self.movie,value="z")#本作品作者吴宇航
    #             self.dongman=Radiobutton(self.win,text="动漫",variable=self.movie,value="d")#本作品作者吴宇航
    #             self.jilupian=Radiobutton(self.win,text="纪录片",variable=self.movie,value="j")#本作品作者吴宇航
    #             self.B_view=Button(self.win,text="✤查看✤")#本作品作者吴宇航
    #             self.B_info=Button(self.win,text="使用说明")#本作品作者吴宇航
    #             self.B_clearbox=Button(self.win,text="清空列表")#本作品作者吴宇航
    #             self.B_add=Button(self.win,text="添加到播放列表")#本作品作者吴宇航
    #             self.R_movie.place(x=290,y=180,width=80,height=30)#本作品作者吴宇航
    #             self.B_view.place(x=290,y=330,width=70,height=30)#本作品作者吴宇航
    #             self.B_add.place(x=370,y=255,width=100,height=30)#本作品作者吴宇航
    #             self.B_clearbox.place(x=500,y=255,width=70,height=30)#本作品作者吴宇航
    #             self.tv.place(x=290,y=210,width=80,height=30)#本作品作者吴宇航
    #             self.zhongyi.place(x=290,y=240,width=80,height=30)#本作品作者吴宇航
    #             self.dongman.place(x=290,y=270,width=80,height=30)#本作品作者吴宇航
    #             self.jilupian.place(x=290,y=300,width=80,height=30)#本作品作者吴宇航
    #             self.La_movie_message.place(x=370,y=290,width=200,height=120)#本作品作者吴宇航
    #             self.La_pic.place(x=370,y=10,width=200,height=240)#本作品作者吴宇航
    #             self.B_info.place(x=290,y=370,width=70,height=30)#本作品作者吴宇航
    #             self.S_croll2.place(x=568,y=290,width=20,height=120)#本作品作者吴宇航
#本作品作者吴宇航
    #         def show_info(self):#本作品作者吴宇航
    #             msg="""#本作品作者吴宇航
    #             1.输入视频播放地址，即可播放#本作品作者吴宇航
    #               选择A或者B可切换视频源#本作品作者吴宇航
    #             2.选择视频网，选择电视剧或者电影，#本作品作者吴宇航
    #               搜索全网后选择想要看得影片，点#本作品作者吴宇航
    #               查看，在右方list里选择分集视频#本作品作者吴宇航
    #               添加到播放列表里点选播放#本作品作者吴宇航
    #             """#本作品作者吴宇航
    #             messagebox.showinfo(title="使用说明",message=msg)#本作品作者吴宇航
#本作品作者吴宇航
    #         def config(self):#本作品作者吴宇航
    #             self.t1.set(True)#本作品作者吴宇航
    #             self.B_play.config(command=self.play_url_movie)#本作品作者吴宇航
    #             self.B_search.config(command=self.search_full_movie)#本作品作者吴宇航
    #             self.B_info.config(command=self.show_info)#本作品作者吴宇航
    #             self.S_croll.config(command=self.L_box.yview)#本作品作者吴宇航
    #             self.L_box['yscrollcommand']=self.S_croll.set#本作品作者吴宇航
    #             self.S_croll2.config(command=self.La_movie_message.yview)#本作品作者吴宇航
    #             self.La_movie_message['yscrollcommand']=self.S_croll2.set#本作品作者吴宇航
    #             self.B_view.config(command=self.view_movies)#本作品作者吴宇航
    #             self.B_add.config(command=self.add_play_list)#本作品作者吴宇航
    #             self.B_clearbox.config(command=self.clear_lisbox2)#本作品作者吴宇航
    #             self.B_uppage.config(command=self.uppage_)#本作品作者吴宇航
    #             self.B_nextpage.config(command=self.nextpage_)#本作品作者吴宇航
#本作品作者吴宇航
    #         def uppage_(self):#本作品作者吴宇航
    #             print('---------上一页---------')#本作品作者吴宇航
    #             self.page-=1#本作品作者吴宇航
    #             print(self.page)#本作品作者吴宇航
    #             if self.page<1:#本作品作者吴宇航
    #                 self.page=1#本作品作者吴宇航
#本作品作者吴宇航
    #         def nextpage_(self):#本作品作者吴宇航
    #             print('----------下一页--------')#本作品作者吴宇航
    #             self.page+=1#本作品作者吴宇航
    #             print(self.page)#本作品作者吴宇航
    #             if self.t3=="a" or self.t3=="y":#本作品作者吴宇航
    #                 if self.page>30:#本作品作者吴宇航
    #                     self.page=30#本作品作者吴宇航
    #             elif self.t3=="p":#本作品作者吴宇航
    #                 if self.movie=="m":#本作品作者吴宇航
    #                     if self.page>165:#本作品作者吴宇航
    #                         self.page=165#本作品作者吴宇航
    #                 elif self.movie == "t":#本作品作者吴宇航
    #                     if self.page > 85:#本作品作者吴宇航
    #                         self.page = 85#本作品作者吴宇航
    #                 elif self.movie == "z":#本作品作者吴宇航
    #                     if self.page > 38:#本作品作者吴宇航
    #                         self.page = 38#本作品作者吴宇航
    #                 elif self.movie == "d":#本作品作者吴宇航
    #                     if self.page > 146:#本作品作者吴宇航
    #                         self.page = 146#本作品作者吴宇航
    #                 elif self.movie == "j":#本作品作者吴宇航
    #                     if self.page > 40:#本作品作者吴宇航
    #                         self.page = 40#本作品作者吴宇航
#本作品作者吴宇航
    #         def clear_lisbox(self):#本作品作者吴宇航
    #             self.L_box.delete(0,END)#本作品作者吴宇航
#本作品作者吴宇航
    #         def clear_lisbox2(self):#本作品作者吴宇航
    #             self.La_movie_message.delete(0,END)#本作品作者吴宇航
#本作品作者吴宇航
    #         def search_full_movie(self):#本作品作者吴宇航
    #             print("-----search----")#本作品作者吴宇航
    #             self.La_page.config(text="当前页:{}".format(self.page))#本作品作者吴宇航
    #             self.clear_lisbox()#本作品作者吴宇航
    #             try:#本作品作者吴宇航
    #                 movie_url, movie_title, movie_src_pic=self.p.get_movie_res(self.t3.get(),self.movie.get(),self.page)#本作品作者吴宇航
    #                 self.movie_dic={}#本作品作者吴宇航
    #                 for i,j,k in zip(movie_title,movie_url,movie_src_pic):#本作品作者吴宇航
    #                     self.movie_dic[i]=[j,k]#本作品作者吴宇航
    #                 for title in movie_title:#本作品作者吴宇航
    #                     self.L_box.insert(END,title)#本作品作者吴宇航
    #                 print(self.movie_dic)#本作品作者吴宇航
    #                 return self.movie_dic#本作品作者吴宇航
    #             except:#本作品作者吴宇航
    #                 messagebox.showerror(title='警告',message='请选择电影或者电视剧')#本作品作者吴宇航
#本作品作者吴宇航
    #         def add_play_list(self):#本作品作者吴宇航
    #             print('---------playlist----------')#本作品作者吴宇航
    #             print(self.movie_dic)#本作品作者吴宇航
    #             if self.La_movie_message.get(self.La_movie_message.curselection())=="":#本作品作者吴宇航
    #                 messagebox.showwarning(title="警告",message='请在列表选择影片')#本作品作者吴宇航
    #             else:#本作品作者吴宇航
    #                 print("电影名字:",self.La_movie_message.get(self.La_movie_message.curselection()))#本作品作者吴宇航
    #                 if self.movie.get()!="m":#本作品作者吴宇航
    #                     self.temp.set(self.new_more_dic[self.La_movie_message.get(self.La_movie_message.curselection())])#本作品作者吴宇航
    #                 else:#本作品作者吴宇航
    #                     self.temp.set(self.movie_dic[self.La_movie_message.get(self.La_movie_message.curselection())][0])#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
    #         def view_pic(self,pic_url):#本作品作者吴宇航
    #             print('--------viewpic---------')#本作品作者吴宇航
    #             pa_url_check=r'//.+[.]jpg'#本作品作者吴宇航
    #             if re.match(pa_url_check,pic_url):#本作品作者吴宇航
    #                 print("ok")#本作品作者吴宇航
    #                 pic_url="http:"+pic_url#本作品作者吴宇航
    #             print(pic_url)#本作品作者吴宇航
    #             data=requests.get(pic_url).content#本作品作者吴宇航
    #             # data=urlopen(pic_url).read()#本作品作者吴宇航
    #             io_data=io.BytesIO(data)#本作品作者吴宇航
    #             self.img=Image.open(io_data)#本作品作者吴宇航
    #             self.u=ImageTk.PhotoImage(self.img)#本作品作者吴宇航
    #             self.La_pic.config(image=self.u)#本作品作者吴宇航
#本作品作者吴宇航
    #         def view_movies(self):#本作品作者吴宇航
    #             print("--------viewmovie----------")#本作品作者吴宇航
    #             cur_index=self.L_box.curselection()#本作品作者吴宇航
    #             print(self.L_box.get(cur_index))#本作品作者吴宇航
    #             if self.movie.get()!="m":#非电影类#本作品作者吴宇航
    #                 self.new_more_dic=self.p.get_more_tv_urls(self.movie_dic[self.L_box.get(cur_index)][0],self.t3.get(),self.movie.get())#本作品作者吴宇航
    #                 print(self.new_more_dic)#本作品作者吴宇航
    #                 for i,fenji_url in self.new_more_dic.items():#本作品作者吴宇航
    #                     self.La_movie_message.insert(END, i)#本作品作者吴宇航
    #             else:#电影类#本作品作者吴宇航
    #                 self.La_movie_message.insert(END,self.L_box.get(cur_index))#本作品作者吴宇航
    #             self.view_pic(self.movie_dic[self.L_box.get(self.L_box.curselection())][1])#加载图片#本作品作者吴宇航
#本作品作者吴宇航
    #         def play_url_movie(self):#本作品作者吴宇航
    #             print("--------ok-----------")#本作品作者吴宇航
    #             # print(type(self.t1.get()),self.t1.get())#本作品作者吴宇航
    #             if self.temp.get()=="":#本作品作者吴宇航
    #                 messagebox.showwarning(title="警告",message="请先输入视频地址")#本作品作者吴宇航
    #             else:#本作品作者吴宇航
    #                 if self.t1.get()!="":#本作品作者吴宇航
    #                     self.p.play_movie(self.temp.get(),self.t1.get())#本作品作者吴宇航
    #                 else:#本作品作者吴宇航
    #                     messagebox.showwarning(title='警告',message='请选择通道')#本作品作者吴宇航
#本作品作者吴宇航
#本作品作者吴宇航
    #     m=Movie_app()#本作品作者吴宇航
    elif dakai == "cortana":#本作品作者吴宇航
        #本作品作者吴宇航
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
        fasdasdf1()   #本作品作者吴宇航
    elif dakai == "mofang":#本作品作者吴宇航
        #本作品作者吴宇航
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
        fangwen("https://livefile.xesimg.com/programme/python_assets/76d2c8e1bf727054db00233b7020d52b.html")#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
    elif dakai == "tuixiang":#本作品作者吴宇航
        FPS = 100 # frames per second to update the screen#本作品作者吴宇航
        WINWIDTH = 800 # width of the program's window, in pixels#本作品作者吴宇航
        WINHEIGHT = 600 # height in pixels#本作品作者吴宇航
        HALF_WINWIDTH = int(WINWIDTH / 2)#本作品作者吴宇航
        HALF_WINHEIGHT = int(WINHEIGHT / 2)#本作品作者吴宇航
         #本作品作者吴宇航
        # The total width and height of each tile in pixels.#本作品作者吴宇航
        TILEWIDTH = 50#本作品作者吴宇航
        TILEHEIGHT = 85#本作品作者吴宇航
        TILEFLOORHEIGHT = 40#本作品作者吴宇航
         #本作品作者吴宇航
        CAM_MOVE_SPEED = 5 # how many pixels per frame the camera moves#本作品作者吴宇航
         #本作品作者吴宇航
        # The percentage of outdoor tiles that have additional#本作品作者吴宇航
        # decoration on them, such as a tree or rock.#本作品作者吴宇航
        OUTSIDE_DECORATION_PCT = 20#本作品作者吴宇航
         #本作品作者吴宇航
        BRIGHTBLUE = (  0, 170, 255)#本作品作者吴宇航
        WHITE      = (255, 255, 255)#本作品作者吴宇航
        BGCOLOR = BRIGHTBLUE#本作品作者吴宇航
        TEXTCOLOR = WHITE#本作品作者吴宇航
         #本作品作者吴宇航
        UP = 'up'#本作品作者吴宇航
        DOWN = 'down'#本作品作者吴宇航
        LEFT = 'left'#本作品作者吴宇航
        RIGHT = 'right'#本作品作者吴宇航
         #本作品作者吴宇航
         #本作品作者吴宇航
        def main():#本作品作者吴宇航
            global FPSCLOCK, DISPLAYSURF, IMAGESDICT, TILEMAPPING, OUTSIDEDECOMAPPING, BASICFONT, PLAYERIMAGES, currentImage#本作品作者吴宇航
         #本作品作者吴宇航
            # Pygame initialization and basic set up of the global variables.#本作品作者吴宇航
            pygame.init()#本作品作者吴宇航
            FPSCLOCK = pygame.time.Clock()#本作品作者吴宇航
         #本作品作者吴宇航
            # Because the Surface object stored in DISPLAYSURF was returned#本作品作者吴宇航
            # from the pygame.display.set_mode() function, this is the#本作品作者吴宇航
            # Surface object that is drawn to the actual computer screen#本作品作者吴宇航
            # when pygame.display.update() is called.#本作品作者吴宇航
            DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))#本作品作者吴宇航
         #本作品作者吴宇航
            pygame.display.set_caption('Star Pusher')#本作品作者吴宇航
            BASICFONT = pygame.font.Font('freesansbold.ttf', 18)#本作品作者吴宇航
         #本作品作者吴宇航
            # A global dict value that will contain all the Pygame#本作品作者吴宇航
            # Surface objects returned by pygame.image.load().#本作品作者吴宇航
            IMAGESDICT = {'uncovered goal': pygame.image.load('RedSelector.png'),#本作品作者吴宇航
                          'covered goal': pygame.image.load('Selector.png'),#本作品作者吴宇航
                          'star': pygame.image.load('Star.png'),#本作品作者吴宇航
                          'corner': pygame.image.load('Wall_Block_Tall.png'),#本作品作者吴宇航
                          'wall': pygame.image.load('Wood_Block_Tall.png'),#本作品作者吴宇航
                          'inside floor': pygame.image.load('Plain_Block.png'),#本作品作者吴宇航
                          'outside floor': pygame.image.load('Grass_Block.png'),#本作品作者吴宇航
                          'title': pygame.image.load('star_title.png'),#本作品作者吴宇航
                          'solved': pygame.image.load('star_solved.png'),#本作品作者吴宇航
                          'princess': pygame.image.load('princess.png'),#本作品作者吴宇航
                          'boy': pygame.image.load('boy.png'),#本作品作者吴宇航
                          'catgirl': pygame.image.load('catgirl.png'),#本作品作者吴宇航
                          'horngirl': pygame.image.load('horngirl.png'),#本作品作者吴宇航
                          'pinkgirl': pygame.image.load('pinkgirl.png'),#本作品作者吴宇航
                          'rock': pygame.image.load('Rock.png'),#本作品作者吴宇航
                          'short tree': pygame.image.load('Tree_Short.png'),#本作品作者吴宇航
                          'tall tree': pygame.image.load('Tree_Tall.png'),#本作品作者吴宇航
                          'ugly tree': pygame.image.load('Tree_Ugly.png')}#本作品作者吴宇航
         #本作品作者吴宇航
            # These dict values are global, and map the character that appears#本作品作者吴宇航
            # in the level file to the Surface object it represents.#本作品作者吴宇航
            TILEMAPPING = {'x': IMAGESDICT['corner'],#本作品作者吴宇航
                           '#': IMAGESDICT['wall'],#本作品作者吴宇航
                           'o': IMAGESDICT['inside floor'],#本作品作者吴宇航
                           ' ': IMAGESDICT['outside floor']}#本作品作者吴宇航
            OUTSIDEDECOMAPPING = {'1': IMAGESDICT['rock'],#本作品作者吴宇航
                                  '2': IMAGESDICT['short tree'],#本作品作者吴宇航
                                  '3': IMAGESDICT['tall tree'],#本作品作者吴宇航
                                  '4': IMAGESDICT['ugly tree']}#本作品作者吴宇航
         #本作品作者吴宇航
            # PLAYERIMAGES is a list of all possible characters the player can be.#本作品作者吴宇航
            # currentImage is the index of the player's current player image.#本作品作者吴宇航
            currentImage = 0#本作品作者吴宇航
            PLAYERIMAGES = [IMAGESDICT['princess'],#本作品作者吴宇航
                            IMAGESDICT['boy'],#本作品作者吴宇航
                            IMAGESDICT['catgirl'],#本作品作者吴宇航
                            IMAGESDICT['horngirl'],#本作品作者吴宇航
                            IMAGESDICT['pinkgirl']]#本作品作者吴宇航
         #本作品作者吴宇航
            startScreen() # show the title screen until the user presses a key#本作品作者吴宇航
         #本作品作者吴宇航
            # Read in the levels from the text file. See the readLevelsFile() for#本作品作者吴宇航
            # details on the format of this file and how to make your own levels.#本作品作者吴宇航
            levels = readLevelsFile('starPusherLevels.txt')#本作品作者吴宇航
            currentLevelIndex = 0#本作品作者吴宇航
         #本作品作者吴宇航
            # The main game loop. This loop runs a single level, when the user#本作品作者吴宇航
            # finishes that level, the next/previous level is loaded.#本作品作者吴宇航
            while True: # main game loop#本作品作者吴宇航
                # Run the level to actually start playing the game:#本作品作者吴宇航
                result = runLevel(levels, currentLevelIndex)#本作品作者吴宇航
         #本作品作者吴宇航
                if result in ('solved', 'next'):#本作品作者吴宇航
                    # Go to the next level.#本作品作者吴宇航
                    currentLevelIndex += 1#本作品作者吴宇航
                    if currentLevelIndex >= len(levels):#本作品作者吴宇航
                        # If there are no more levels, go back to the first one.#本作品作者吴宇航
                        currentLevelIndex = 0#本作品作者吴宇航
                elif result == 'back':#本作品作者吴宇航
                    # Go to the previous level.#本作品作者吴宇航
                    currentLevelIndex -= 1#本作品作者吴宇航
                    if currentLevelIndex < 0:#本作品作者吴宇航
                        # If there are no previous levels, go to the last one.#本作品作者吴宇航
                        currentLevelIndex = len(levels)-1#本作品作者吴宇航
                #本作品作者吴宇航
                elif result == 'reset':#本作品作者吴宇航
                    pass # Do nothing. Loop re-calls runLevel() to reset the level#本作品作者吴宇航
         #本作品作者吴宇航
         #本作品作者吴宇航
        def runLevel(levels, levelNum):#本作品作者吴宇航
            global currentImage#本作品作者吴宇航
            levelObj = levels[levelNum]#本作品作者吴宇航
            mapObj = decorateMap(levelObj['mapObj'], levelObj['startState']['player'])#本作品作者吴宇航
            gameStateObj = copy.deepcopy(levelObj['startState'])#本作品作者吴宇航
            mapNeedsRedraw = True # set to True to call drawMap()#本作品作者吴宇航
            levelSurf = BASICFONT.render('Level %s of %s' % (levelNum + 1, len(levels)), 1, TEXTCOLOR)#本作品作者吴宇航
            levelRect = levelSurf.get_rect()#本作品作者吴宇航
            levelRect.bottomleft = (20, WINHEIGHT - 35)#本作品作者吴宇航
            mapWidth = len(mapObj) * TILEWIDTH#本作品作者吴宇航
            mapHeight = (len(mapObj[0]) - 1) * TILEFLOORHEIGHT + TILEHEIGHT#本作品作者吴宇航
            MAX_CAM_X_PAN = abs(HALF_WINHEIGHT - int(mapHeight / 2)) + TILEWIDTH#本作品作者吴宇航
            MAX_CAM_Y_PAN = abs(HALF_WINWIDTH - int(mapWidth / 2)) + TILEHEIGHT#本作品作者吴宇航
         #本作品作者吴宇航
            levelIsComplete = False#本作品作者吴宇航
            # Track how much the camera has moved:#本作品作者吴宇航
            cameraOffsetX = 0#本作品作者吴宇航
            cameraOffsetY = 0#本作品作者吴宇航
            # Track if the keys to move the camera are being held down:#本作品作者吴宇航
            cameraUp = False#本作品作者吴宇航
            cameraDown = False#本作品作者吴宇航
            cameraLeft = False#本作品作者吴宇航
            cameraRight = False#本作品作者吴宇航
         #本作品作者吴宇航
            while True: # main game loop#本作品作者吴宇航
                # Reset these variables:#本作品作者吴宇航
                playerMoveTo = None#本作品作者吴宇航
                keyPressed = False#本作品作者吴宇航
         #本作品作者吴宇航
                for event in pygame.event.get(): # event handling loop#本作品作者吴宇航
                    if event.type == QUIT:#本作品作者吴宇航
                        # Player clicked the "X" at the corner of the window.#本作品作者吴宇航
                        terminate()#本作品作者吴宇航
         #本作品作者吴宇航
                    elif event.type == KEYDOWN:#本作品作者吴宇航
                        # Handle key presses#本作品作者吴宇航
                        keyPressed = True#本作品作者吴宇航
                        if event.key == K_LEFT:#本作品作者吴宇航
                            playerMoveTo = LEFT#本作品作者吴宇航
                        elif event.key == K_RIGHT:#本作品作者吴宇航
                            playerMoveTo = RIGHT#本作品作者吴宇航
                        elif event.key == K_UP:#本作品作者吴宇航
                            playerMoveTo = UP#本作品作者吴宇航
                        elif event.key == K_DOWN:#本作品作者吴宇航
                            playerMoveTo = DOWN#本作品作者吴宇航
         #本作品作者吴宇航
                        # Set the camera move mode.#本作品作者吴宇航
                        elif event.key == K_a:#本作品作者吴宇航
                            cameraLeft = True#本作品作者吴宇航
                        elif event.key == K_d:#本作品作者吴宇航
                            cameraRight = True#本作品作者吴宇航
                        elif event.key == K_w:#本作品作者吴宇航
                            cameraUp = True#本作品作者吴宇航
                        elif event.key == K_s:#本作品作者吴宇航
                            cameraDown = True#本作品作者吴宇航
         #本作品作者吴宇航
                        elif event.key == K_n:#本作品作者吴宇航
                            return 'next'#本作品作者吴宇航
                        elif event.key == K_b:#本作品作者吴宇航
                            return 'back'#本作品作者吴宇航
         #本作品作者吴宇航
                        elif event.key == K_ESCAPE:#本作品作者吴宇航
                            terminate() # Esc key quits.#本作品作者吴宇航
                        elif event.key == K_BACKSPACE:#本作品作者吴宇航
                            return 'reset' # Reset the level.#本作品作者吴宇航
                        elif event.key == K_p:#本作品作者吴宇航
                            # Change the player image to the next one.#本作品作者吴宇航
                            currentImage += 1#本作品作者吴宇航
                            if currentImage >= len(PLAYERIMAGES):#本作品作者吴宇航
                                # After the last player image, use the first one.#本作品作者吴宇航
                                currentImage = 0#本作品作者吴宇航
                            mapNeedsRedraw = True#本作品作者吴宇航
         #本作品作者吴宇航
                    elif event.type == KEYUP:#本作品作者吴宇航
                        # Unset the camera move mode.#本作品作者吴宇航
                        if event.key == K_a:#本作品作者吴宇航
                            cameraLeft = False#本作品作者吴宇航
                        elif event.key == K_d:#本作品作者吴宇航
                            cameraRight = False#本作品作者吴宇航
                        elif event.key == K_w:#本作品作者吴宇航
                            cameraUp = False#本作品作者吴宇航
                        elif event.key == K_s:#本作品作者吴宇航
                            cameraDown = False#本作品作者吴宇航
         #本作品作者吴宇航
                if playerMoveTo != None and not levelIsComplete:#本作品作者吴宇航
                    # If the player pushed a key to move, make the move#本作品作者吴宇航
                    # (if possible) and push any stars that are pushable.#本作品作者吴宇航
                    moved = makeMove(mapObj, gameStateObj, playerMoveTo)#本作品作者吴宇航
         #本作品作者吴宇航
                    if moved:#本作品作者吴宇航
                        # increment the step counter.#本作品作者吴宇航
                        gameStateObj['stepCounter'] += 1#本作品作者吴宇航
                        mapNeedsRedraw = True#本作品作者吴宇航
         #本作品作者吴宇航
                    if isLevelFinished(levelObj, gameStateObj):#本作品作者吴宇航
                        # level is solved, we should show the "Solved!" image.#本作品作者吴宇航
                        levelIsComplete = True#本作品作者吴宇航
                        keyPressed = False#本作品作者吴宇航
         #本作品作者吴宇航
                DISPLAYSURF.fill(BGCOLOR)#本作品作者吴宇航
         #本作品作者吴宇航
                if mapNeedsRedraw:#本作品作者吴宇航
                    mapSurf = drawMap(mapObj, gameStateObj, levelObj['goals'])#本作品作者吴宇航
                    mapNeedsRedraw = False#本作品作者吴宇航
         #本作品作者吴宇航
                if cameraUp and cameraOffsetY < MAX_CAM_X_PAN:#本作品作者吴宇航
                    cameraOffsetY += CAM_MOVE_SPEED#本作品作者吴宇航
                elif cameraDown and cameraOffsetY > -MAX_CAM_X_PAN:#本作品作者吴宇航
                    cameraOffsetY -= CAM_MOVE_SPEED#本作品作者吴宇航
                if cameraLeft and cameraOffsetX < MAX_CAM_Y_PAN:#本作品作者吴宇航
                    cameraOffsetX += CAM_MOVE_SPEED#本作品作者吴宇航
                elif cameraRight and cameraOffsetX > -MAX_CAM_Y_PAN:#本作品作者吴宇航
                    cameraOffsetX -= CAM_MOVE_SPEED#本作品作者吴宇航
         #本作品作者吴宇航
                # Adjust mapSurf's Rect object based on the camera offset.#本作品作者吴宇航
                mapSurfRect = mapSurf.get_rect()#本作品作者吴宇航
                mapSurfRect.center = (HALF_WINWIDTH + cameraOffsetX, HALF_WINHEIGHT + cameraOffsetY)#本作品作者吴宇航
         #本作品作者吴宇航
                # Draw mapSurf to the DISPLAYSURF Surface object.#本作品作者吴宇航
                DISPLAYSURF.blit(mapSurf, mapSurfRect)#本作品作者吴宇航
         #本作品作者吴宇航
                DISPLAYSURF.blit(levelSurf, levelRect)#本作品作者吴宇航
                stepSurf = BASICFONT.render('Steps: %s' % (gameStateObj['stepCounter']), 1, TEXTCOLOR)#本作品作者吴宇航
                stepRect = stepSurf.get_rect()#本作品作者吴宇航
                stepRect.bottomleft = (20, WINHEIGHT - 10)#本作品作者吴宇航
                DISPLAYSURF.blit(stepSurf, stepRect)#本作品作者吴宇航
         #本作品作者吴宇航
                if levelIsComplete:#本作品作者吴宇航
                    # is solved, show the "Solved!" image until the player#本作品作者吴宇航
                    # has pressed a key.#本作品作者吴宇航
                    solvedRect = IMAGESDICT['solved'].get_rect()#本作品作者吴宇航
                    solvedRect.center = (HALF_WINWIDTH, HALF_WINHEIGHT)#本作品作者吴宇航
                    DISPLAYSURF.blit(IMAGESDICT['solved'], solvedRect)#本作品作者吴宇航
         #本作品作者吴宇航
                    if keyPressed:#本作品作者吴宇航
                        return 'solved'#本作品作者吴宇航
         #本作品作者吴宇航
                pygame.display.update() # draw DISPLAYSURF to the screen.#本作品作者吴宇航
                FPSCLOCK.tick()#本作品作者吴宇航
         #本作品作者吴宇航
         #本作品作者吴宇航
        def isWall(mapObj, x, y):#本作品作者吴宇航
            """Returns True if the (x, y) position on#本作品作者吴宇航
            the map is a wall, otherwise return False."""#本作品作者吴宇航
            if x < 0 or x >= len(mapObj) or y < 0 or y >= len(mapObj[x]):#本作品作者吴宇航
                return False # x and y aren't actually on the map.#本作品作者吴宇航
            elif mapObj[x][y] in ('#', 'x'):#本作品作者吴宇航
                return True # wall is blocking#本作品作者吴宇航
            return False#本作品作者吴宇航
         #本作品作者吴宇航
         #本作品作者吴宇航
        def decorateMap(mapObj, startxy):#本作品作者吴宇航
            """Makes a copy of the given map object and modifies it.#本作品作者吴宇航
            Here is what is done to it:#本作品作者吴宇航
                * Walls that are corners are turned into corner pieces.#本作品作者吴宇航
                * The outside/inside floor tile distinction is made.#本作品作者吴宇航
                * Tree/rock decorations are randomly added to the outside tiles.#本作品作者吴宇航
            Returns the decorated map object."""#本作品作者吴宇航
         #本作品作者吴宇航
            startx, starty = startxy # Syntactic sugar#本作品作者吴宇航
         #本作品作者吴宇航
            # Copy the map object so we don't modify the original passed#本作品作者吴宇航
            mapObjCopy = copy.deepcopy(mapObj)#本作品作者吴宇航
         #本作品作者吴宇航
            # Remove the non-wall characters from the map data#本作品作者吴宇航
            for x in range(len(mapObjCopy)):#本作品作者吴宇航
                for y in range(len(mapObjCopy[0])):#本作品作者吴宇航
                    if mapObjCopy[x][y] in ('$', '.', '@', '+', '*'):#本作品作者吴宇航
                        mapObjCopy[x][y] = ' '#本作品作者吴宇航
         #本作品作者吴宇航
            # Flood fill to determine inside/outside floor tiles.#本作品作者吴宇航
            floodFill(mapObjCopy, startx, starty, ' ', 'o')#本作品作者吴宇航
         #本作品作者吴宇航
            # Convert the adjoined walls into corner tiles.#本作品作者吴宇航
            for x in range(len(mapObjCopy)):#本作品作者吴宇航
                for y in range(len(mapObjCopy[0])):#本作品作者吴宇航
         #本作品作者吴宇航
                    if mapObjCopy[x][y] == '#':#本作品作者吴宇航
                        if (isWall(mapObjCopy, x, y-1) and isWall(mapObjCopy, x+1, y)) or \
                           (isWall(mapObjCopy, x+1, y) and isWall(mapObjCopy, x, y+1)) or \
                           (isWall(mapObjCopy, x, y+1) and isWall(mapObjCopy, x-1, y)) or \
                           (isWall(mapObjCopy, x-1, y) and isWall(mapObjCopy, x, y-1)):#本作品作者吴宇航
                            mapObjCopy[x][y] = 'x'#本作品作者吴宇航
         #本作品作者吴宇航
                    elif mapObjCopy[x][y] == ' ' and random.randint(0, 99) < OUTSIDE_DECORATION_PCT:#本作品作者吴宇航
                        mapObjCopy[x][y] = random.choice(list(OUTSIDEDECOMAPPING.keys()))#本作品作者吴宇航
         #本作品作者吴宇航
            return mapObjCopy#本作品作者吴宇航
         #本作品作者吴宇航
         #本作品作者吴宇航
        def isBlocked(mapObj, gameStateObj, x, y):#本作品作者吴宇航
            """Returns True if the (x, y) position on the map is#本作品作者吴宇航
            blocked by a wall or star, otherwise return False."""#本作品作者吴宇航
         #本作品作者吴宇航
            if isWall(mapObj, x, y):#本作品作者吴宇航
                return True#本作品作者吴宇航
         #本作品作者吴宇航
            elif x < 0 or x >= len(mapObj) or y < 0 or y >= len(mapObj[x]):#本作品作者吴宇航
                return True # x and y aren't actually on the map.#本作品作者吴宇航
         #本作品作者吴宇航
            elif (x, y) in gameStateObj['stars']:#本作品作者吴宇航
                return True # a star is blocking#本作品作者吴宇航
         #本作品作者吴宇航
            return False#本作品作者吴宇航
         #本作品作者吴宇航
         #本作品作者吴宇航
        def makeMove(mapObj, gameStateObj, playerMoveTo):#本作品作者吴宇航
            """Given a map and game state object, see if it is possible for the#本作品作者吴宇航
            player to make the given move. If it is, then change the player's#本作品作者吴宇航
            position (and the position of any pushed star). If not, do nothing.#本作品作者吴宇航
            Returns True if the player moved, otherwise False."""#本作品作者吴宇航
         #本作品作者吴宇航
            # Make sure the player can move in the direction they want.#本作品作者吴宇航
            playerx, playery = gameStateObj['player']#本作品作者吴宇航
         #本作品作者吴宇航
            # This variable is "syntactic sugar". Typing "stars" is more#本作品作者吴宇航
            # readable than typing "gameStateObj['stars']" in our code.#本作品作者吴宇航
            stars = gameStateObj['stars']#本作品作者吴宇航
         #本作品作者吴宇航
            # The code for handling each of the directions is so similar aside#本作品作者吴宇航
            # from adding or subtracting 1 to the x/y coordinates. We can#本作品作者吴宇航
            # simplify it by using the xOffset and yOffset variables.#本作品作者吴宇航
            if playerMoveTo == UP:#本作品作者吴宇航
                xOffset = 0#本作品作者吴宇航
                yOffset = -1#本作品作者吴宇航
            elif playerMoveTo == RIGHT:#本作品作者吴宇航
                xOffset = 1#本作品作者吴宇航
                yOffset = 0#本作品作者吴宇航
            elif playerMoveTo == DOWN:#本作品作者吴宇航
                xOffset = 0#本作品作者吴宇航
                yOffset = 1#本作品作者吴宇航
            elif playerMoveTo == LEFT:#本作品作者吴宇航
                xOffset = -1#本作品作者吴宇航
                yOffset = 0#本作品作者吴宇航
         #本作品作者吴宇航
            # See if the player can move in that direction.#本作品作者吴宇航
            if isWall(mapObj, playerx + xOffset, playery + yOffset):#本作品作者吴宇航
                return False#本作品作者吴宇航
            else:#本作品作者吴宇航
                if (playerx + xOffset, playery + yOffset) in stars:#本作品作者吴宇航
                    # There is a star in the way, see if the player can push it.#本作品作者吴宇航
                    if not isBlocked(mapObj, gameStateObj, playerx + (xOffset*2), playery + (yOffset*2)):#本作品作者吴宇航
                        # Move the star.#本作品作者吴宇航
                        ind = stars.index((playerx + xOffset, playery + yOffset))#本作品作者吴宇航
                        stars[ind] = (stars[ind][0] + xOffset, stars[ind][1] + yOffset)#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        return False#本作品作者吴宇航
                # Move the player upwards.#本作品作者吴宇航
                gameStateObj['player'] = (playerx + xOffset, playery + yOffset)#本作品作者吴宇航
                return True#本作品作者吴宇航
         #本作品作者吴宇航
         #本作品作者吴宇航
        def startScreen():#本作品作者吴宇航
            """Display the start screen (which has the title and instructions)#本作品作者吴宇航
            until the player presses a key. Returns None."""#本作品作者吴宇航
         #本作品作者吴宇航
            # Position the title image.#本作品作者吴宇航
            titleRect = IMAGESDICT['title'].get_rect()#本作品作者吴宇航
            topCoord = 50 # topCoord tracks where to position the top of the text#本作品作者吴宇航
            titleRect.top = topCoord#本作品作者吴宇航
            titleRect.centerx = HALF_WINWIDTH#本作品作者吴宇航
            topCoord += titleRect.height#本作品作者吴宇航
         #本作品作者吴宇航
            # Unfortunately, Pygame's font & text system only shows one line at#本作品作者吴宇航
            # a time, so we can't use strings with \n newline characters in them.#本作品作者吴宇航
            # So we will use a list with each line in it.#本作品作者吴宇航
            instructionText = ['Push the stars over the marks.',#本作品作者吴宇航
                               'Arrow keys to move, WASD for camera control, P to change character.',#本作品作者吴宇航
                               'Backspace to reset level, Esc to quit.',#本作品作者吴宇航
                               'N for next level, B to go back a level.']#本作品作者吴宇航
         #本作品作者吴宇航
            # Start with drawing a blank color to the entire window:#本作品作者吴宇航
            DISPLAYSURF.fill(BGCOLOR)#本作品作者吴宇航
         #本作品作者吴宇航
            # Draw the title image to the window:#本作品作者吴宇航
            DISPLAYSURF.blit(IMAGESDICT['title'], titleRect)#本作品作者吴宇航
         #本作品作者吴宇航
            # Position and draw the text.#本作品作者吴宇航
            for i in range(len(instructionText)):#本作品作者吴宇航
                instSurf = BASICFONT.render(instructionText[i], 1, TEXTCOLOR)#本作品作者吴宇航
                instRect = instSurf.get_rect()#本作品作者吴宇航
                topCoord += 10 # 10 pixels will go in between each line of text.#本作品作者吴宇航
                instRect.top = topCoord#本作品作者吴宇航
                instRect.centerx = HALF_WINWIDTH#本作品作者吴宇航
                topCoord += instRect.height # Adjust for the height of the line.#本作品作者吴宇航
                DISPLAYSURF.blit(instSurf, instRect)#本作品作者吴宇航
         #本作品作者吴宇航
            while True: # Main loop for the start screen.#本作品作者吴宇航
                for event in pygame.event.get():#本作品作者吴宇航
                    if event.type == QUIT:#本作品作者吴宇航
                        terminate()#本作品作者吴宇航
                    elif event.type == KEYDOWN:#本作品作者吴宇航
                        if event.key == K_ESCAPE:#本作品作者吴宇航
                            terminate()#本作品作者吴宇航
                        return # user has pressed a key, so return.#本作品作者吴宇航
         #本作品作者吴宇航
                # Display the DISPLAYSURF contents to the actual screen.#本作品作者吴宇航
                pygame.display.update()#本作品作者吴宇航
                FPSCLOCK.tick()#本作品作者吴宇航
         #本作品作者吴宇航
         #本作品作者吴宇航
        def readLevelsFile(filename):#本作品作者吴宇航
            assert os.path.exists(filename), 'Cannot find the level file: %s' % (filename)#本作品作者吴宇航
            mapFile = open(filename, 'r')#本作品作者吴宇航
            # Each level must end with a blank line#本作品作者吴宇航
            content = mapFile.readlines() + ['\r\n']#本作品作者吴宇航
            mapFile.close()#本作品作者吴宇航
         #本作品作者吴宇航
            levels = [] # Will contain a list of level objects.#本作品作者吴宇航
            levelNum = 0#本作品作者吴宇航
            mapTextLines = [] # contains the lines for a single level's map.#本作品作者吴宇航
            mapObj = [] # the map object made from the data in mapTextLines#本作品作者吴宇航
            for lineNum in range(len(content)):#本作品作者吴宇航
                # Process each line that was in the level file.#本作品作者吴宇航
                line = content[lineNum].rstrip('\r\n')#本作品作者吴宇航
         #本作品作者吴宇航
                if ';' in line:#本作品作者吴宇航
                    # Ignore the ; lines, they're comments in the level file.#本作品作者吴宇航
                    line = line[:line.find(';')]#本作品作者吴宇航
         #本作品作者吴宇航
                if line != '':#本作品作者吴宇航
                    # This line is part of the map.#本作品作者吴宇航
                    mapTextLines.append(line)#本作品作者吴宇航
                elif line == '' and len(mapTextLines) > 0:#本作品作者吴宇航
                    # A blank line indicates the end of a level's map in the file.#本作品作者吴宇航
                    # Convert the text in mapTextLines into a level object.#本作品作者吴宇航
         #本作品作者吴宇航
                    # Find the longest row in the map.#本作品作者吴宇航
                    maxWidth = -1#本作品作者吴宇航
                    for i in range(len(mapTextLines)):#本作品作者吴宇航
                        if len(mapTextLines[i]) > maxWidth:#本作品作者吴宇航
                            maxWidth = len(mapTextLines[i])#本作品作者吴宇航
                    # Add spaces to the ends of the shorter rows. This#本作品作者吴宇航
                    # ensures the map will be rectangular.#本作品作者吴宇航
                    for i in range(len(mapTextLines)):#本作品作者吴宇航
                        mapTextLines[i] += ' ' * (maxWidth - len(mapTextLines[i]))#本作品作者吴宇航
         #本作品作者吴宇航
                    # Convert mapTextLines to a map object.#本作品作者吴宇航
                    for x in range(len(mapTextLines[0])):#本作品作者吴宇航
                        mapObj.append([])#本作品作者吴宇航
                    for y in range(len(mapTextLines)):#本作品作者吴宇航
                        for x in range(maxWidth):#本作品作者吴宇航
                            mapObj[x].append(mapTextLines[y][x])#本作品作者吴宇航
         #本作品作者吴宇航
                    # Loop through the spaces in the map and find the @, ., and $#本作品作者吴宇航
                    # characters for the starting game state.#本作品作者吴宇航
                    startx = None # The x and y for the player's starting position#本作品作者吴宇航
                    starty = None#本作品作者吴宇航
                    goals = [] # list of (x, y) tuples for each goal.#本作品作者吴宇航
                    stars = [] # list of (x, y) for each star's starting position.#本作品作者吴宇航
                    for x in range(maxWidth):#本作品作者吴宇航
                        for y in range(len(mapObj[x])):#本作品作者吴宇航
                            if mapObj[x][y] in ('@', '+'):#本作品作者吴宇航
                                # '@' is player, '+' is player & goal#本作品作者吴宇航
                                startx = x#本作品作者吴宇航
                                starty = y#本作品作者吴宇航
                            if mapObj[x][y] in ('.', '+', '*'):#本作品作者吴宇航
                                # '.' is goal, '*' is star & goal#本作品作者吴宇航
                                goals.append((x, y))#本作品作者吴宇航
                            if mapObj[x][y] in ('$', '*'):#本作品作者吴宇航
                                # '$' is star#本作品作者吴宇航
                                stars.append((x, y))#本作品作者吴宇航
         #本作品作者吴宇航
                    # Basic level design sanity checks:#本作品作者吴宇航
                    assert startx != None and starty != None, 'Level %s (around line %s) in %s is missing a "@" or "+" to mark the start point.' % (levelNum+1, lineNum, filename)#本作品作者吴宇航
                    assert len(goals) > 0, 'Level %s (around line %s) in %s must have at least one goal.' % (levelNum+1, lineNum, filename)#本作品作者吴宇航
                    assert len(stars) >= len(goals), 'Level %s (around line %s) in %s is impossible to solve. It has %s goals but only %s stars.' % (levelNum+1, lineNum, filename, len(goals), len(stars))#本作品作者吴宇航
         #本作品作者吴宇航
                    # Create level object and starting game state object.#本作品作者吴宇航
                    gameStateObj = {'player': (startx, starty),#本作品作者吴宇航
                                    'stepCounter': 0,#本作品作者吴宇航
                                    'stars': stars}#本作品作者吴宇航
                    levelObj = {'width': maxWidth,#本作品作者吴宇航
                                'height': len(mapObj),#本作品作者吴宇航
                                'mapObj': mapObj,#本作品作者吴宇航
                                'goals': goals,#本作品作者吴宇航
                                'startState': gameStateObj}#本作品作者吴宇航
         #本作品作者吴宇航
                    levels.append(levelObj)#本作品作者吴宇航
         #本作品作者吴宇航
                    # Reset the variables for reading the next map.#本作品作者吴宇航
                    mapTextLines = []#本作品作者吴宇航
                    mapObj = []#本作品作者吴宇航
                    gameStateObj = {}#本作品作者吴宇航
                    levelNum += 1#本作品作者吴宇航
            return levels#本作品作者吴宇航
         #本作品作者吴宇航
         #本作品作者吴宇航
        def floodFill(mapObj, x, y, oldCharacter, newCharacter):#本作品作者吴宇航
            """Changes any values matching oldCharacter on the map object to#本作品作者吴宇航
            newCharacter at the (x, y) position, and does the same for the#本作品作者吴宇航
            positions to the left, right, down, and up of (x, y), recursively."""#本作品作者吴宇航
         #本作品作者吴宇航
            # In this game, the flood fill algorithm creates the inside/outside#本作品作者吴宇航
            # floor distinction. This is a "recursive" function.#本作品作者吴宇航
            # For more info on the Flood Fill algorithm, see:#本作品作者吴宇航
            #   http://en.wikipedia.org/wiki/Flood_fill#本作品作者吴宇航
            if mapObj[x][y] == oldCharacter:#本作品作者吴宇航
                mapObj[x][y] = newCharacter#本作品作者吴宇航
         #本作品作者吴宇航
            if x < len(mapObj) - 1 and mapObj[x+1][y] == oldCharacter:#本作品作者吴宇航
                floodFill(mapObj, x+1, y, oldCharacter, newCharacter) # call right#本作品作者吴宇航
            if x > 0 and mapObj[x-1][y] == oldCharacter:#本作品作者吴宇航
                floodFill(mapObj, x-1, y, oldCharacter, newCharacter) # call left#本作品作者吴宇航
            if y < len(mapObj[x]) - 1 and mapObj[x][y+1] == oldCharacter:#本作品作者吴宇航
                floodFill(mapObj, x, y+1, oldCharacter, newCharacter) # call down#本作品作者吴宇航
            if y > 0 and mapObj[x][y-1] == oldCharacter:#本作品作者吴宇航
                floodFill(mapObj, x, y-1, oldCharacter, newCharacter) # call up#本作品作者吴宇航
         #本作品作者吴宇航
         #本作品作者吴宇航
        def drawMap(mapObj, gameStateObj, goals):#本作品作者吴宇航
            """Draws the map to a Surface object, including the player and#本作品作者吴宇航
            stars. This function does not call pygame.display.update(), nor#本作品作者吴宇航
            does it draw the "Level" and "Steps" text in the corner."""#本作品作者吴宇航
         #本作品作者吴宇航
            # mapSurf will be the single Surface object that the tiles are drawn#本作品作者吴宇航
            # on, so that it is easy to position the entire map on the DISPLAYSURF#本作品作者吴宇航
            # Surface object. First, the width and height must be calculated.#本作品作者吴宇航
            mapSurfWidth = len(mapObj) * TILEWIDTH#本作品作者吴宇航
            mapSurfHeight = (len(mapObj[0]) - 1) * TILEFLOORHEIGHT + TILEHEIGHT#本作品作者吴宇航
            mapSurf = pygame.Surface((mapSurfWidth, mapSurfHeight))#本作品作者吴宇航
            mapSurf.fill(BGCOLOR) # start with a blank color on the surface.#本作品作者吴宇航
         #本作品作者吴宇航
            # Draw the tile sprites onto this surface.#本作品作者吴宇航
            for x in range(len(mapObj)):#本作品作者吴宇航
                for y in range(len(mapObj[x])):#本作品作者吴宇航
                    spaceRect = pygame.Rect((x * TILEWIDTH, y * TILEFLOORHEIGHT, TILEWIDTH, TILEHEIGHT))#本作品作者吴宇航
                    if mapObj[x][y] in TILEMAPPING:#本作品作者吴宇航
                        baseTile = TILEMAPPING[mapObj[x][y]]#本作品作者吴宇航
                    elif mapObj[x][y] in OUTSIDEDECOMAPPING:#本作品作者吴宇航
                        baseTile = TILEMAPPING[' ']#本作品作者吴宇航
         #本作品作者吴宇航
                    # First draw the base ground/wall tile.#本作品作者吴宇航
                    mapSurf.blit(baseTile, spaceRect)#本作品作者吴宇航
         #本作品作者吴宇航
                    if mapObj[x][y] in OUTSIDEDECOMAPPING:#本作品作者吴宇航
                        # Draw any tree/rock decorations that are on this tile.#本作品作者吴宇航
                        mapSurf.blit(OUTSIDEDECOMAPPING[mapObj[x][y]], spaceRect)#本作品作者吴宇航
                    elif (x, y) in gameStateObj['stars']:#本作品作者吴宇航
                        if (x, y) in goals:#本作品作者吴宇航
                            # A goal AND star are on this space, draw goal first.#本作品作者吴宇航
                            mapSurf.blit(IMAGESDICT['covered goal'], spaceRect)#本作品作者吴宇航
                        # Then draw the star sprite.#本作品作者吴宇航
                        mapSurf.blit(IMAGESDICT['star'], spaceRect)#本作品作者吴宇航
                    elif (x, y) in goals:#本作品作者吴宇航
                        # Draw a goal without a star on it.#本作品作者吴宇航
                        mapSurf.blit(IMAGESDICT['uncovered goal'], spaceRect)#本作品作者吴宇航
         #本作品作者吴宇航
                    # Last draw the player on the board.#本作品作者吴宇航
                    if (x, y) == gameStateObj['player']:#本作品作者吴宇航
                        # Note: The value "currentImage" refers#本作品作者吴宇航
                        # to a key in "PLAYERIMAGES" which has the#本作品作者吴宇航
                        # specific player image we want to show.#本作品作者吴宇航
                        mapSurf.blit(PLAYERIMAGES[currentImage], spaceRect)#本作品作者吴宇航
         #本作品作者吴宇航
            return mapSurf#本作品作者吴宇航
         #本作品作者吴宇航
         #本作品作者吴宇航
        def isLevelFinished(levelObj, gameStateObj):#本作品作者吴宇航
            """Returns True if all the goals have stars in them."""#本作品作者吴宇航
            for goal in levelObj['goals']:#本作品作者吴宇航
                if goal not in gameStateObj['stars']:#本作品作者吴宇航
                    # Found a space with a goal but no star on it.#本作品作者吴宇航
                    return False#本作品作者吴宇航
            return True#本作品作者吴宇航
         #本作品作者吴宇航
         #本作品作者吴宇航
        def terminate():#本作品作者吴宇航
            pygame.quit()#本作品作者吴宇航
            fasdasdf1()#本作品作者吴宇航
         #本作品作者吴宇航
         #本作品作者吴宇航
        if __name__ == '__main__':#本作品作者吴宇航
            main()#本作品作者吴宇航
    elif dakai == "chidou":#本作品作者吴宇航
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
        fangwen("https://livefile.xesimg.com/programme/python_assets/8defd98dfc8abb86ca99a4868e7c0ca9.html")#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
    elif dakai == "golf":#本作品作者吴宇航
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
        fangwen("https://livefile.xesimg.com/programme/python_assets/eef5e6e99eab6aa5cd835d37af7cd917.html")#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
    elif dakai == "paoku":#本作品作者吴宇航
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
        fangwen("https://livefile.xesimg.com/programme/python_assets/b6ae97d07cd81d80fb34936befab82a9.html")#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
    elif dakai == "saolei":#本作品作者吴宇航
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
        fangwen("https://livefile.xesimg.com/programme/python_assets/e29d9731f6f375a43b3b9850969de32a.html")#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
    elif dakai == "saiche":#本作品作者吴宇航
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
        fangwen("https://livefile.xesimg.com/programme/python_assets/30ba9fcfcbc6579e0ac0b87857cc09a9.html")#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
    elif dakai == "dongwu":#本作品作者吴宇航
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
        fangwen("https://livefile.xesimg.com/programme/python_assets/075dc7de1161e72b1829cb1dee36236e.html")#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
    elif dakai == "fanpai":#本作品作者吴宇航
        #本作品作者吴宇航
        FPS = 20 # frames per second, the general speed of the program#本作品作者吴宇航
        WINDOWWIDTH = 640 # size of window's width in pixels#本作品作者吴宇航
        WINDOWHEIGHT = 480 # size of windows' height in pixels#本作品作者吴宇航
        REVEALSPEED = 8 # speed boxes' sliding reveals and covers#本作品作者吴宇航
        BOXSIZE = 40 # size of box height & width in pixels#本作品作者吴宇航
        GAPSIZE = 10 # size of gap between boxes in pixels#本作品作者吴宇航
        BOARDWIDTH = 10 # number of columns of icons#本作品作者吴宇航
        BOARDHEIGHT = 7 # number of rows of icons#本作品作者吴宇航
        assert (BOARDWIDTH * BOARDHEIGHT) % 2 == 0, 'Board needs to have an even number of boxes for pairs of matches.'#本作品作者吴宇航
        XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)#本作品作者吴宇航
        YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)#本作品作者吴宇航
        #本作品作者吴宇航
        #            R    G    B#本作品作者吴宇航
        GRAY     = (100, 100, 100)#本作品作者吴宇航
        NAVYBLUE = ( 60,  60, 100)#本作品作者吴宇航
        WHITE    = (255, 255, 255)#本作品作者吴宇航
        RED      = (255,   0,   0)#本作品作者吴宇航
        GREEN    = (  0, 255,   0)#本作品作者吴宇航
        BLUE     = (  0,   0, 255)#本作品作者吴宇航
        YELLOW   = (255, 255,   0)#本作品作者吴宇航
        ORANGE   = (255, 128,   0)#本作品作者吴宇航
        PURPLE   = (255,   0, 255)#本作品作者吴宇航
        CYAN     = (  0, 255, 255)#本作品作者吴宇航
        #本作品作者吴宇航
        BGCOLOR = NAVYBLUE#本作品作者吴宇航
        LIGHTBGCOLOR = GRAY#本作品作者吴宇航
        BOXCOLOR = WHITE#本作品作者吴宇航
        HIGHLIGHTCOLOR = BLUE#本作品作者吴宇航
        #本作品作者吴宇航
        DONUT = 'donut'#本作品作者吴宇航
        SQUARE = 'square'#本作品作者吴宇航
        DIAMOND = 'diamond'#本作品作者吴宇航
        LINES = 'lines'#本作品作者吴宇航
        OVAL = 'oval'#本作品作者吴宇航
        #本作品作者吴宇航
        ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)#本作品作者吴宇航
        ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)#本作品作者吴宇航
        assert len(ALLCOLORS) * len(ALLSHAPES) * 2 >= BOARDWIDTH * BOARDHEIGHT, "Board is too big for the number of shapes/colors defined."#本作品作者吴宇航
        #本作品作者吴宇航
        def main():#本作品作者吴宇航
            global FPSCLOCK, DISPLAYSURF#本作品作者吴宇航
            pygame.init()#本作品作者吴宇航
            FPSCLOCK = pygame.time.Clock()#本作品作者吴宇航
            DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))#本作品作者吴宇航
        #本作品作者吴宇航
            mousex = 0 # used to store x coordinate of mouse event#本作品作者吴宇航
            mousey = 0 # used to store y coordinate of mouse event#本作品作者吴宇航
            pygame.display.set_caption('Memory Game')#本作品作者吴宇航
        #本作品作者吴宇航
            mainBoard = getRandomizedBoard()#本作品作者吴宇航
            revealedBoxes = generateRevealedBoxesData(False)#本作品作者吴宇航
        #本作品作者吴宇航
            firstSelection = None # stores the (x, y) of the first box clicked.#本作品作者吴宇航
        #本作品作者吴宇航
            DISPLAYSURF.fill(BGCOLOR)#本作品作者吴宇航
            startGameAnimation(mainBoard)#本作品作者吴宇航
        #本作品作者吴宇航
            while True: # main game loop#本作品作者吴宇航
                mouseClicked = False#本作品作者吴宇航
        #本作品作者吴宇航
                DISPLAYSURF.fill(BGCOLOR) # drawing the window#本作品作者吴宇航
                drawBoard(mainBoard, revealedBoxes)#本作品作者吴宇航
        #本作品作者吴宇航
                for event in pygame.event.get(): # event handling loop#本作品作者吴宇航
                    if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):#本作品作者吴宇航
                        pygame.quit()#本作品作者吴宇航
                        sys.exit()#本作品作者吴宇航
                    elif event.type == MOUSEMOTION:#本作品作者吴宇航
                        mousex, mousey = event.pos#本作品作者吴宇航
                    elif event.type == MOUSEBUTTONUP:#本作品作者吴宇航
                        mousex, mousey = event.pos#本作品作者吴宇航
                        mouseClicked = True#本作品作者吴宇航
        #本作品作者吴宇航
                boxx, boxy = getBoxAtPixel(mousex, mousey)#本作品作者吴宇航
                if boxx != None and boxy != None:#本作品作者吴宇航
                    # The mouse is currently over a box.#本作品作者吴宇航
                    if not revealedBoxes[boxx][boxy]:#本作品作者吴宇航
                        drawHighlightBox(boxx, boxy)#本作品作者吴宇航
                    if not revealedBoxes[boxx][boxy] and mouseClicked:#本作品作者吴宇航
                        revealBoxesAnimation(mainBoard, [(boxx, boxy)])#本作品作者吴宇航
                        revealedBoxes[boxx][boxy] = True # set the box as "revealed"#本作品作者吴宇航
                        if firstSelection == None: # the current box was the first box clicked#本作品作者吴宇航
                            firstSelection = (boxx, boxy)#本作品作者吴宇航
                        else: # the current box was the second box clicked#本作品作者吴宇航
                            # Check if there is a match between the two icons.#本作品作者吴宇航
                            icon1shape, icon1color = getShapeAndColor(mainBoard, firstSelection[0], firstSelection[1])#本作品作者吴宇航
                            icon2shape, icon2color = getShapeAndColor(mainBoard, boxx, boxy)#本作品作者吴宇航
        #本作品作者吴宇航
                            if icon1shape != icon2shape or icon1color != icon2color:#本作品作者吴宇航
                                # Icons don't match. Re-cover up both selections.#本作品作者吴宇航
                                pygame.time.wait(1000) # 1000 milliseconds = 1 sec#本作品作者吴宇航
                                coverBoxesAnimation(mainBoard, [(firstSelection[0], firstSelection[1]), (boxx, boxy)])#本作品作者吴宇航
                                revealedBoxes[firstSelection[0]][firstSelection[1]] = False#本作品作者吴宇航
                                revealedBoxes[boxx][boxy] = False#本作品作者吴宇航
                            elif hasWon(revealedBoxes): # check if all pairs found#本作品作者吴宇航
                                gameWonAnimation(mainBoard)#本作品作者吴宇航
                                pygame.time.wait(2000)#本作品作者吴宇航
        #本作品作者吴宇航
                                # Reset the board#本作品作者吴宇航
                                mainBoard = getRandomizedBoard()#本作品作者吴宇航
                                revealedBoxes = generateRevealedBoxesData(False)#本作品作者吴宇航
        #本作品作者吴宇航
                                # Show the fully unrevealed board for a second.#本作品作者吴宇航
                                drawBoard(mainBoard, revealedBoxes)#本作品作者吴宇航
                                pygame.display.update()#本作品作者吴宇航
                                pygame.time.wait(1000)#本作品作者吴宇航
        #本作品作者吴宇航
                                # Replay the start game animation.#本作品作者吴宇航
                                startGameAnimation(mainBoard)#本作品作者吴宇航
                            firstSelection = None # reset firstSelection variable#本作品作者吴宇航
        #本作品作者吴宇航
                # Redraw the screen and wait a clock tick.#本作品作者吴宇航
                pygame.display.update()#本作品作者吴宇航
                FPSCLOCK.tick(FPS)#本作品作者吴宇航
        #本作品作者吴宇航
        #本作品作者吴宇航
        def generateRevealedBoxesData(val):#本作品作者吴宇航
            revealedBoxes = []#本作品作者吴宇航
            for i in range(BOARDWIDTH):#本作品作者吴宇航
                revealedBoxes.append([val] * BOARDHEIGHT)#本作品作者吴宇航
            return revealedBoxes#本作品作者吴宇航
        #本作品作者吴宇航
        #本作品作者吴宇航
        def getRandomizedBoard():#本作品作者吴宇航
            # Get a list of every possible shape in every possible color.#本作品作者吴宇航
            icons = []#本作品作者吴宇航
            for color in ALLCOLORS:#本作品作者吴宇航
                for shape in ALLSHAPES:#本作品作者吴宇航
                    icons.append( (shape, color) )#本作品作者吴宇航
        #本作品作者吴宇航
            random.shuffle(icons) # randomize the order of the icons list#本作品作者吴宇航
            numIconsUsed = int(BOARDWIDTH * BOARDHEIGHT / 2) # calculate how many icons are needed#本作品作者吴宇航
            icons = icons[:numIconsUsed] * 2 # make two of each#本作品作者吴宇航
            random.shuffle(icons)#本作品作者吴宇航
        #本作品作者吴宇航
            # Create the board data structure, with randomly placed icons.#本作品作者吴宇航
            board = []#本作品作者吴宇航
            for x in range(BOARDWIDTH):#本作品作者吴宇航
                column = []#本作品作者吴宇航
                for y in range(BOARDHEIGHT):#本作品作者吴宇航
                    column.append(icons[0])#本作品作者吴宇航
                    del icons[0] # remove the icons as we assign them#本作品作者吴宇航
                board.append(column)#本作品作者吴宇航
            return board#本作品作者吴宇航
        #本作品作者吴宇航
        #本作品作者吴宇航
        def splitIntoGroupsOf(groupSize, theList):#本作品作者吴宇航
            # splits a list into a list of lists, where the inner lists have at#本作品作者吴宇航
            # most groupSize number of items.#本作品作者吴宇航
            result = []#本作品作者吴宇航
            for i in range(0, len(theList), groupSize):#本作品作者吴宇航
                result.append(theList[i:i + groupSize])#本作品作者吴宇航
            return result#本作品作者吴宇航
        #本作品作者吴宇航
        #本作品作者吴宇航
        def leftTopCoordsOfBox(boxx, boxy):#本作品作者吴宇航
            # Convert board coordinates to pixel coordinates#本作品作者吴宇航
            left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN#本作品作者吴宇航
            top = boxy * (BOXSIZE + GAPSIZE) + YMARGIN#本作品作者吴宇航
            return (left, top)#本作品作者吴宇航
        #本作品作者吴宇航
        #本作品作者吴宇航
        def getBoxAtPixel(x, y):#本作品作者吴宇航
            for boxx in range(BOARDWIDTH):#本作品作者吴宇航
                for boxy in range(BOARDHEIGHT):#本作品作者吴宇航
                    left, top = leftTopCoordsOfBox(boxx, boxy)#本作品作者吴宇航
                    boxRect = pygame.Rect(left, top, BOXSIZE, BOXSIZE)#本作品作者吴宇航
                    if boxRect.collidepoint(x, y):#本作品作者吴宇航
                        return (boxx, boxy)#本作品作者吴宇航
            return (None, None)#本作品作者吴宇航
        #本作品作者吴宇航
        #本作品作者吴宇航
        def drawIcon(shape, color, boxx, boxy):#本作品作者吴宇航
            quarter = int(BOXSIZE * 0.25) # syntactic sugar#本作品作者吴宇航
            half =    int(BOXSIZE * 0.5)  # syntactic sugar#本作品作者吴宇航
        #本作品作者吴宇航
            left, top = leftTopCoordsOfBox(boxx, boxy) # get pixel coords from board coords#本作品作者吴宇航
            # Draw the shapes#本作品作者吴宇航
            if shape == DONUT:#本作品作者吴宇航
                pygame.draw.circle(DISPLAYSURF, color, (left + half, top + half), half - 5)#本作品作者吴宇航
                pygame.draw.circle(DISPLAYSURF, BGCOLOR, (left + half, top + half), quarter - 5)#本作品作者吴宇航
            elif shape == SQUARE:#本作品作者吴宇航
                pygame.draw.rect(DISPLAYSURF, color, (left + quarter, top + quarter, BOXSIZE - half, BOXSIZE - half))#本作品作者吴宇航
            elif shape == DIAMOND:#本作品作者吴宇航
                pygame.draw.polygon(DISPLAYSURF, color, ((left + half, top), (left + BOXSIZE - 1, top + half), (left + half, top + BOXSIZE - 1), (left, top + half)))#本作品作者吴宇航
            elif shape == LINES:#本作品作者吴宇航
                for i in range(0, BOXSIZE, 4):#本作品作者吴宇航
                    pygame.draw.line(DISPLAYSURF, color, (left, top + i), (left + i, top))#本作品作者吴宇航
                    pygame.draw.line(DISPLAYSURF, color, (left + i, top + BOXSIZE - 1), (left + BOXSIZE - 1, top + i))#本作品作者吴宇航
            elif shape == OVAL:#本作品作者吴宇航
                pygame.draw.ellipse(DISPLAYSURF, color, (left, top + quarter, BOXSIZE, half))#本作品作者吴宇航
        #本作品作者吴宇航
        #本作品作者吴宇航
        def getShapeAndColor(board, boxx, boxy):#本作品作者吴宇航
            # shape value for x, y spot is stored in board[x][y][0]#本作品作者吴宇航
            # color value for x, y spot is stored in board[x][y][1]#本作品作者吴宇航
            return board[boxx][boxy][0], board[boxx][boxy][1]#本作品作者吴宇航
        #本作品作者吴宇航
        #本作品作者吴宇航
        def drawBoxCovers(board, boxes, coverage):#本作品作者吴宇航
            # Draws boxes being covered/revealed. "boxes" is a list#本作品作者吴宇航
            # of two-item lists, which have the x & y spot of the box.#本作品作者吴宇航
            for box in boxes:#本作品作者吴宇航
                left, top = leftTopCoordsOfBox(box[0], box[1])#本作品作者吴宇航
                pygame.draw.rect(DISPLAYSURF, BGCOLOR, (left, top, BOXSIZE, BOXSIZE))#本作品作者吴宇航
                shape, color = getShapeAndColor(board, box[0], box[1])#本作品作者吴宇航
                drawIcon(shape, color, box[0], box[1])#本作品作者吴宇航
                if coverage > 0: # only draw the cover if there is an coverage#本作品作者吴宇航
                    pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, coverage, BOXSIZE))#本作品作者吴宇航
            pygame.display.update()#本作品作者吴宇航
            FPSCLOCK.tick(FPS)#本作品作者吴宇航
        #本作品作者吴宇航
        #本作品作者吴宇航
        def revealBoxesAnimation(board, boxesToReveal):#本作品作者吴宇航
            # Do the "box reveal" animation.#本作品作者吴宇航
            for coverage in range(BOXSIZE, (-REVEALSPEED) - 1, -REVEALSPEED):#本作品作者吴宇航
                drawBoxCovers(board, boxesToReveal, coverage)#本作品作者吴宇航
        #本作品作者吴宇航
        #本作品作者吴宇航
        def coverBoxesAnimation(board, boxesToCover):#本作品作者吴宇航
            # Do the "box cover" animation.#本作品作者吴宇航
            for coverage in range(0, BOXSIZE + REVEALSPEED, REVEALSPEED):#本作品作者吴宇航
                drawBoxCovers(board, boxesToCover, coverage)#本作品作者吴宇航
        #本作品作者吴宇航
        #本作品作者吴宇航
        def drawBoard(board, revealed):#本作品作者吴宇航
            # Draws all of the boxes in their covered or revealed state.#本作品作者吴宇航
            for boxx in range(BOARDWIDTH):#本作品作者吴宇航
                for boxy in range(BOARDHEIGHT):#本作品作者吴宇航
                    left, top = leftTopCoordsOfBox(boxx, boxy)#本作品作者吴宇航
                    if not revealed[boxx][boxy]:#本作品作者吴宇航
                        # Draw a covered box.#本作品作者吴宇航
                        pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, BOXSIZE, BOXSIZE))#本作品作者吴宇航
                    else:#本作品作者吴宇航
                        # Draw the (revealed) icon.#本作品作者吴宇航
                        shape, color = getShapeAndColor(board, boxx, boxy)#本作品作者吴宇航
                        drawIcon(shape, color, boxx, boxy)#本作品作者吴宇航
        #本作品作者吴宇航
        #本作品作者吴宇航
        def drawHighlightBox(boxx, boxy):#本作品作者吴宇航
            left, top = leftTopCoordsOfBox(boxx, boxy)#本作品作者吴宇航
            pygame.draw.rect(DISPLAYSURF, HIGHLIGHTCOLOR, (left - 5, top - 5, BOXSIZE + 10, BOXSIZE + 10), 4)#本作品作者吴宇航
        #本作品作者吴宇航
        #本作品作者吴宇航
        def startGameAnimation(board):#本作品作者吴宇航
            # Randomly reveal the boxes 8 at a time.#本作品作者吴宇航
            coveredBoxes = generateRevealedBoxesData(False)#本作品作者吴宇航
            boxes = []#本作品作者吴宇航
            for x in range(BOARDWIDTH):#本作品作者吴宇航
                for y in range(BOARDHEIGHT):#本作品作者吴宇航
                    boxes.append( (x, y) )#本作品作者吴宇航
            random.shuffle(boxes)#本作品作者吴宇航
            boxGroups = splitIntoGroupsOf(8, boxes)#本作品作者吴宇航
        #本作品作者吴宇航
            drawBoard(board, coveredBoxes)#本作品作者吴宇航
            for boxGroup in boxGroups:#本作品作者吴宇航
                revealBoxesAnimation(board, boxGroup)#本作品作者吴宇航
                coverBoxesAnimation(board, boxGroup)#本作品作者吴宇航
        #本作品作者吴宇航
        #本作品作者吴宇航
        def gameWonAnimation(board):#本作品作者吴宇航
            # flash the background color when the player has won#本作品作者吴宇航
            coveredBoxes = generateRevealedBoxesData(True)#本作品作者吴宇航
            color1 = LIGHTBGCOLOR#本作品作者吴宇航
            color2 = BGCOLOR#本作品作者吴宇航
        #本作品作者吴宇航
            for i in range(13):#本作品作者吴宇航
                color1, color2 = color2, color1 # swap colors#本作品作者吴宇航
                DISPLAYSURF.fill(color1)#本作品作者吴宇航
                drawBoard(board, coveredBoxes)#本作品作者吴宇航
                pygame.display.update()#本作品作者吴宇航
                pygame.time.wait(300)#本作品作者吴宇航
        #本作品作者吴宇航
        #本作品作者吴宇航
        def hasWon(revealedBoxes):#本作品作者吴宇航
            # Returns True if all the boxes have been revealed, otherwise False#本作品作者吴宇航
            for i in revealedBoxes:#本作品作者吴宇航
                if False in i:#本作品作者吴宇航
                    return False # return False if any boxes are covered.#本作品作者吴宇航
            return True#本作品作者吴宇航
        #本作品作者吴宇航
        #本作品作者吴宇航
        if __name__ == '__main__':#本作品作者吴宇航
            main()#本作品作者吴宇航
    elif dakai == "qiangzhan":#本作品作者吴宇航
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
        fangwen("https://livefile.xesimg.com/programme/python_assets/99259bb0f6cc822179339fa14675dc46.html")#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
    elif dakai == "tafang":#本作品作者吴宇航
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
        fangwen("https://livefile.xesimg.com/programme/python_assets/ee2195a882836455b058569b7d65e92b.html")#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
    elif dakai == "taila":#本作品作者吴宇航
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
        fangwen("https://livefile.xesimg.com/programme/python_assets/86304eb307810bb22c4fe7e57a2c5895.html")#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
    elif dakai == "baowei":#本作品作者吴宇航
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
        fangwen("https://livefile.xesimg.com/programme/python_assets/c80acba2086c3f1fdf15f004af9d1e99.html")#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
    elif dakai == "renzhe":#本作品作者吴宇航
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
        fangwen("https://livefile.xesimg.com/programme/python_assets/68eea5a0578fc1c2b683e8e827fccf5a.html")#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
    elif dakai == "feiji":#本作品作者吴宇航
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
        fangwen("https://livefile.xesimg.com/programme/python_assets/96b7d9a35d4f8faf9f1bf8c0797b0f77.html")#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
    elif dakai == "secai":#本作品作者吴宇航
        # There are different box sizes, number of boxes, and#本作品作者吴宇航
        # life depending on the "board size" setting selected.#本作品作者吴宇航
        SMALLBOXSIZE  = 60 # size is in pixels#本作品作者吴宇航
        MEDIUMBOXSIZE = 20#本作品作者吴宇航
        LARGEBOXSIZE  = 11#本作品作者吴宇航
        #本作品作者吴宇航
        SMALLBOARDSIZE  = 6 # size is in boxes#本作品作者吴宇航
        MEDIUMBOARDSIZE = 17#本作品作者吴宇航
        LARGEBOARDSIZE  = 30#本作品作者吴宇航
        #本作品作者吴宇航
        SMALLMAXLIFE  = 10 # number of turns#本作品作者吴宇航
        MEDIUMMAXLIFE = 30#本作品作者吴宇航
        LARGEMAXLIFE  = 64#本作品作者吴宇航
        #本作品作者吴宇航
        FPS = 30#本作品作者吴宇航
        WINDOWWIDTH = 640#本作品作者吴宇航
        WINDOWHEIGHT = 480#本作品作者吴宇航
        boxSize = MEDIUMBOXSIZE#本作品作者吴宇航
        PALETTEGAPSIZE = 10#本作品作者吴宇航
        PALETTESIZE = 45#本作品作者吴宇航
        EASY = 0   # arbitrary but unique value#本作品作者吴宇航
        MEDIUM = 1 # arbitrary but unique value#本作品作者吴宇航
        HARD = 2   # arbitrary but unique value#本作品作者吴宇航
        #本作品作者吴宇航
        difficulty = MEDIUM # game starts in "medium" mode#本作品作者吴宇航
        maxLife = MEDIUMMAXLIFE#本作品作者吴宇航
        boardWidth = MEDIUMBOARDSIZE#本作品作者吴宇航
        boardHeight = MEDIUMBOARDSIZE#本作品作者吴宇航
        #本作品作者吴宇航
        #本作品作者吴宇航
        #            R    G    B#本作品作者吴宇航
        WHITE    = (255, 255, 255)#本作品作者吴宇航
        DARKGRAY = ( 70,  70,  70)#本作品作者吴宇航
        BLACK    = (  0,   0,   0)#本作品作者吴宇航
        RED      = (255,   0,   0)#本作品作者吴宇航
        GREEN    = (  0, 255,   0)#本作品作者吴宇航
        BLUE     = (  0,   0, 255)#本作品作者吴宇航
        YELLOW   = (255, 255,   0)#本作品作者吴宇航
        ORANGE   = (255, 128,   0)#本作品作者吴宇航
        PURPLE   = (255,   0, 255)#本作品作者吴宇航
        #本作品作者吴宇航
        # The first color in each scheme is the background color, the next six are the palette colors.#本作品作者吴宇航
        COLORSCHEMES = (((150, 200, 255), RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE),#本作品作者吴宇航
                        ((0, 155, 104),  (97, 215, 164),  (228, 0, 69),  (0, 125, 50),   (204, 246, 0),   (148, 0, 45),    (241, 109, 149)),#本作品作者吴宇航
                        ((195, 179, 0),  (255, 239, 115), (255, 226, 0), (147, 3, 167),  (24, 38, 176),   (166, 147, 0),   (197, 97, 211)),#本作品作者吴宇航
                        ((85, 0, 0),     (155, 39, 102),  (0, 201, 13),  (255, 118, 0),  (206, 0, 113),   (0, 130, 9),     (255, 180, 115)),#本作品作者吴宇航
                        ((191, 159, 64), (183, 182, 208), (4, 31, 183),  (167, 184, 45), (122, 128, 212), (37, 204, 7),    (88, 155, 213)),#本作品作者吴宇航
                        ((200, 33, 205), (116, 252, 185), (68, 56, 56),  (52, 238, 83),  (23, 149, 195),  (222, 157, 227), (212, 86, 185)))#本作品作者吴宇航
        for i in range(len(COLORSCHEMES)):#本作品作者吴宇航
            assert len(COLORSCHEMES[i]) == 7, 'Color scheme %s does not have exactly 7 colors.' % (i)#本作品作者吴宇航
        bgColor = COLORSCHEMES[0][0]#本作品作者吴宇航
        paletteColors =  COLORSCHEMES[0][1:]#本作品作者吴宇航
        #本作品作者吴宇航
        def main():#本作品作者吴宇航
            global FPSCLOCK, DISPLAYSURF, LOGOIMAGE, SPOTIMAGE, SETTINGSIMAGE, SETTINGSBUTTONIMAGE, RESETBUTTONIMAGE#本作品作者吴宇航
        #本作品作者吴宇航
            pygame.init()#本作品作者吴宇航
            FPSCLOCK = pygame.time.Clock()#本作品作者吴宇航
            DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))#本作品作者吴宇航
        #本作品作者吴宇航
            # Load images#本作品作者吴宇航
            LOGOIMAGE = pygame.image.load('inkspilllogo.png')#本作品作者吴宇航
            SPOTIMAGE = pygame.image.load('inkspillspot.png')#本作品作者吴宇航
            SETTINGSIMAGE = pygame.image.load('inkspillsettings.png')#本作品作者吴宇航
            SETTINGSBUTTONIMAGE = pygame.image.load('inkspillsettingsbutton.png')#本作品作者吴宇航
            RESETBUTTONIMAGE = pygame.image.load('inkspillresetbutton.png')#本作品作者吴宇航
        #本作品作者吴宇航
            pygame.display.set_caption('Ink Spill')#本作品作者吴宇航
            mousex = 0#本作品作者吴宇航
            mousey = 0#本作品作者吴宇航
            mainBoard = generateRandomBoard(boardWidth, boardHeight, difficulty)#本作品作者吴宇航
            life = maxLife#本作品作者吴宇航
            lastPaletteClicked = None#本作品作者吴宇航
        #本作品作者吴宇航
            while True: # main game loop#本作品作者吴宇航
                paletteClicked = None#本作品作者吴宇航
                resetGame = False#本作品作者吴宇航
        #本作品作者吴宇航
                # Draw the screen.#本作品作者吴宇航
                DISPLAYSURF.fill(bgColor)#本作品作者吴宇航
                drawLogoAndButtons()#本作品作者吴宇航
                drawBoard(mainBoard)#本作品作者吴宇航
                drawLifeMeter(life)#本作品作者吴宇航
                drawPalettes()#本作品作者吴宇航
        #本作品作者吴宇航
                checkForQuit()#本作品作者吴宇航
                for event in pygame.event.get(): # event handling loop#本作品作者吴宇航
                    if event.type == MOUSEBUTTONUP:#本作品作者吴宇航
                        mousex, mousey = event.pos#本作品作者吴宇航
                        if pygame.Rect(WINDOWWIDTH - SETTINGSBUTTONIMAGE.get_width(),#本作品作者吴宇航
                                       WINDOWHEIGHT - SETTINGSBUTTONIMAGE.get_height(),#本作品作者吴宇航
                                       SETTINGSBUTTONIMAGE.get_width(),#本作品作者吴宇航
                                       SETTINGSBUTTONIMAGE.get_height()).collidepoint(mousex, mousey):#本作品作者吴宇航
                            resetGame = showSettingsScreen() # clicked on Settings button#本作品作者吴宇航
                        elif pygame.Rect(WINDOWWIDTH - RESETBUTTONIMAGE.get_width(),#本作品作者吴宇航
                                         WINDOWHEIGHT - SETTINGSBUTTONIMAGE.get_height() - RESETBUTTONIMAGE.get_height(),#本作品作者吴宇航
                                         RESETBUTTONIMAGE.get_width(),#本作品作者吴宇航
                                         RESETBUTTONIMAGE.get_height()).collidepoint(mousex, mousey):#本作品作者吴宇航
                            resetGame = True # clicked on Reset button#本作品作者吴宇航
                        else:#本作品作者吴宇航
                            # check if a palette button was clicked#本作品作者吴宇航
                            paletteClicked = getColorOfPaletteAt(mousex, mousey)#本作品作者吴宇航
        #本作品作者吴宇航
                if paletteClicked != None and paletteClicked != lastPaletteClicked:#本作品作者吴宇航
                    # a palette button was clicked that is different from the#本作品作者吴宇航
                    # last palette button clicked (this check prevents the player#本作品作者吴宇航
                    # from accidentally clicking the same palette twice)#本作品作者吴宇航
                    lastPaletteClicked = paletteClicked#本作品作者吴宇航
                    floodAnimation(mainBoard, paletteClicked)#本作品作者吴宇航
                    life -= 1#本作品作者吴宇航
        #本作品作者吴宇航
                    resetGame = False#本作品作者吴宇航
                    if hasWon(mainBoard):#本作品作者吴宇航
                        for i in range(4): # flash border 4 times#本作品作者吴宇航
                            flashBorderAnimation(WHITE, mainBoard)#本作品作者吴宇航
                        resetGame = True#本作品作者吴宇航
                        pygame.time.wait(2000) # pause so the player can bask in victory#本作品作者吴宇航
                    elif life == 0:#本作品作者吴宇航
                        # life is zero, so player has lost#本作品作者吴宇航
                        drawLifeMeter(0)#本作品作者吴宇航
                        pygame.display.update()#本作品作者吴宇航
                        pygame.time.wait(400)#本作品作者吴宇航
                        for i in range(4):#本作品作者吴宇航
                            flashBorderAnimation(BLACK, mainBoard)#本作品作者吴宇航
                        resetGame = True#本作品作者吴宇航
                        pygame.time.wait(2000) # pause so the player can suffer in their defeat#本作品作者吴宇航
        #本作品作者吴宇航
                if resetGame:#本作品作者吴宇航
                    # start a new game#本作品作者吴宇航
                    mainBoard = generateRandomBoard(boardWidth, boardHeight, difficulty)#本作品作者吴宇航
                    life = maxLife#本作品作者吴宇航
                    lastPaletteClicked = None#本作品作者吴宇航
        #本作品作者吴宇航
                pygame.display.update()#本作品作者吴宇航
                FPSCLOCK.tick(FPS)#本作品作者吴宇航
        #本作品作者吴宇航
        #本作品作者吴宇航
        def checkForQuit():#本作品作者吴宇航
            # Terminates the program if there are any QUIT or escape key events.#本作品作者吴宇航
            for event in pygame.event.get(QUIT): # get all the QUIT events#本作品作者吴宇航
                pygame.quit() # terminate if any QUIT events are present#本作品作者吴宇航
                sys.exit()#本作品作者吴宇航
            for event in pygame.event.get(KEYUP): # get all the KEYUP events#本作品作者吴宇航
                if event.key == K_ESCAPE:#本作品作者吴宇航
                    pygame.quit() # terminate if the KEYUP event was for the Esc key#本作品作者吴宇航
                    sys.exit()#本作品作者吴宇航
                pygame.event.post(event) # put the other KEYUP event objects back#本作品作者吴宇航
        #本作品作者吴宇航
        #本作品作者吴宇航
        def hasWon(board):#本作品作者吴宇航
            # if the entire board is the same color, player has won#本作品作者吴宇航
            for x in range(boardWidth):#本作品作者吴宇航
                for y in range(boardHeight):#本作品作者吴宇航
                    if board[x][y] != board[0][0]:#本作品作者吴宇航
                        return False # found a different color, player has not won#本作品作者吴宇航
            return True#本作品作者吴宇航
        #本作品作者吴宇航
        #本作品作者吴宇航
        def showSettingsScreen():#本作品作者吴宇航
            global difficulty, boxSize, boardWidth, boardHeight, maxLife, paletteColors, bgColor#本作品作者吴宇航
        #本作品作者吴宇航
            # The pixel coordinates in this function were obtained by loading#本作品作者吴宇航
            # the inkspillsettings.png image into a graphics editor and reading#本作品作者吴宇航
            # the pixel coordinates from there. Handy trick.#本作品作者吴宇航
        #本作品作者吴宇航
            origDifficulty = difficulty#本作品作者吴宇航
            origBoxSize = boxSize#本作品作者吴宇航
            screenNeedsRedraw = True#本作品作者吴宇航
        #本作品作者吴宇航
            while True:#本作品作者吴宇航
                if screenNeedsRedraw:#本作品作者吴宇航
                    DISPLAYSURF.fill(bgColor)#本作品作者吴宇航
                    DISPLAYSURF.blit(SETTINGSIMAGE, (0,0))#本作品作者吴宇航
        #本作品作者吴宇航
                    # place the ink spot marker next to the selected difficulty#本作品作者吴宇航
                    if difficulty == EASY:#本作品作者吴宇航
                        DISPLAYSURF.blit(SPOTIMAGE, (30, 4))#本作品作者吴宇航
                    if difficulty == MEDIUM:#本作品作者吴宇航
                        DISPLAYSURF.blit(SPOTIMAGE, (8, 41))#本作品作者吴宇航
                    if difficulty == HARD:#本作品作者吴宇航
                        DISPLAYSURF.blit(SPOTIMAGE, (30, 76))#本作品作者吴宇航
        #本作品作者吴宇航
                    # place the ink spot marker next to the selected size#本作品作者吴宇航
                    if boxSize == SMALLBOXSIZE:#本作品作者吴宇航
                        DISPLAYSURF.blit(SPOTIMAGE, (22, 150))#本作品作者吴宇航
                    if boxSize == MEDIUMBOXSIZE:#本作品作者吴宇航
                        DISPLAYSURF.blit(SPOTIMAGE, (11, 185))#本作品作者吴宇航
                    if boxSize == LARGEBOXSIZE:#本作品作者吴宇航
                        DISPLAYSURF.blit(SPOTIMAGE, (24, 220))#本作品作者吴宇航
        #本作品作者吴宇航
                    for i in range(len(COLORSCHEMES)):#本作品作者吴宇航
                        drawColorSchemeBoxes(500, i * 60 + 30, i)#本作品作者吴宇航
        #本作品作者吴宇航
                    pygame.display.update()#本作品作者吴宇航
        #本作品作者吴宇航
                screenNeedsRedraw = False # by default, don't redraw the screen#本作品作者吴宇航
                for event in pygame.event.get(): # event handling loop#本作品作者吴宇航
                    if event.type == QUIT:#本作品作者吴宇航
                        pygame.quit()#本作品作者吴宇航
                        sys.exit()#本作品作者吴宇航
                    elif event.type == KEYUP:#本作品作者吴宇航
                        if event.key == K_ESCAPE:#本作品作者吴宇航
                            # Esc key on settings screen goes back to game#本作品作者吴宇航
                            return not (origDifficulty == difficulty and origBoxSize == boxSize)#本作品作者吴宇航
                    elif event.type == MOUSEBUTTONUP:#本作品作者吴宇航
                        screenNeedsRedraw = True # screen should be redrawn#本作品作者吴宇航
                        mousex, mousey = event.pos # syntactic sugar#本作品作者吴宇航
        #本作品作者吴宇航
                        # check for clicks on the difficulty buttons#本作品作者吴宇航
                        if pygame.Rect(74, 16, 111, 30).collidepoint(mousex, mousey):#本作品作者吴宇航
                            difficulty = EASY#本作品作者吴宇航
                        elif pygame.Rect(53, 50, 104, 29).collidepoint(mousex, mousey):#本作品作者吴宇航
                            difficulty = MEDIUM#本作品作者吴宇航
                        elif pygame.Rect(72, 85, 65, 31).collidepoint(mousex, mousey):#本作品作者吴宇航
                            difficulty = HARD#本作品作者吴宇航
        #本作品作者吴宇航
                        # check for clicks on the size buttons#本作品作者吴宇航
                        elif pygame.Rect(63, 156, 84, 31).collidepoint(mousex, mousey):#本作品作者吴宇航
                            # small board size setting:#本作品作者吴宇航
                            boxSize = SMALLBOXSIZE#本作品作者吴宇航
                            boardWidth = SMALLBOARDSIZE#本作品作者吴宇航
                            boardHeight = SMALLBOARDSIZE#本作品作者吴宇航
                            maxLife = SMALLMAXLIFE#本作品作者吴宇航
                        elif pygame.Rect(52, 192, 106,32).collidepoint(mousex, mousey):#本作品作者吴宇航
                            # medium board size setting:#本作品作者吴宇航
                            boxSize = MEDIUMBOXSIZE#本作品作者吴宇航
                            boardWidth = MEDIUMBOARDSIZE#本作品作者吴宇航
                            boardHeight = MEDIUMBOARDSIZE#本作品作者吴宇航
                            maxLife = MEDIUMMAXLIFE#本作品作者吴宇航
                        elif pygame.Rect(67, 228, 58, 37).collidepoint(mousex, mousey):#本作品作者吴宇航
                            # large board size setting:#本作品作者吴宇航
                            boxSize = LARGEBOXSIZE#本作品作者吴宇航
                            boardWidth = LARGEBOARDSIZE#本作品作者吴宇航
                            boardHeight = LARGEBOARDSIZE#本作品作者吴宇航
                            maxLife = LARGEMAXLIFE#本作品作者吴宇航
                        elif pygame.Rect(14, 299, 371, 97).collidepoint(mousex, mousey):#本作品作者吴宇航
                            # clicked on the "learn programming" ad#本作品作者吴宇航
                            webbrowser.open('http://inventwithpython.com') # opens a web browser#本作品作者吴宇航
                        elif pygame.Rect(178, 418, 215, 34).collidepoint(mousex, mousey):#本作品作者吴宇航
                            # clicked on the "back to game" button#本作品作者吴宇航
                            return not (origDifficulty == difficulty and origBoxSize == boxSize)#本作品作者吴宇航
        #本作品作者吴宇航
                        for i in range(len(COLORSCHEMES)):#本作品作者吴宇航
                            # clicked on a color scheme button#本作品作者吴宇航
                            if pygame.Rect(500, 30 + i * 60, MEDIUMBOXSIZE * 3, MEDIUMBOXSIZE * 2).collidepoint(mousex, mousey):#本作品作者吴宇航
                                bgColor = COLORSCHEMES[i][0]#本作品作者吴宇航
                                paletteColors  = COLORSCHEMES[i][1:]#本作品作者吴宇航
        #本作品作者吴宇航
        #本作品作者吴宇航
        def drawColorSchemeBoxes(x, y, schemeNum):#本作品作者吴宇航
            # Draws the color scheme boxes that appear on the "Settings" screen.#本作品作者吴宇航
            for boxy in range(2):#本作品作者吴宇航
                for boxx in range(3):#本作品作者吴宇航
                    pygame.draw.rect(DISPLAYSURF, COLORSCHEMES[schemeNum][3 * boxy + boxx + 1], (x + MEDIUMBOXSIZE * boxx, y + MEDIUMBOXSIZE * boxy, MEDIUMBOXSIZE, MEDIUMBOXSIZE))#本作品作者吴宇航
                    if paletteColors == COLORSCHEMES[schemeNum][1:]:#本作品作者吴宇航
                        # put the ink spot next to the selected color scheme#本作品作者吴宇航
                        DISPLAYSURF.blit(SPOTIMAGE, (x - 50, y))#本作品作者吴宇航
        #本作品作者吴宇航
        #本作品作者吴宇航
        def flashBorderAnimation(color, board, animationSpeed=30):#本作品作者吴宇航
            origSurf = DISPLAYSURF.copy()#本作品作者吴宇航
            flashSurf = pygame.Surface(DISPLAYSURF.get_size())#本作品作者吴宇航
            flashSurf = flashSurf.convert_alpha()#本作品作者吴宇航
            for start, end, step in ((0, 256, 1), (255, 0, -1)):#本作品作者吴宇航
                # the first iteration on the outer loop will set the inner loop#本作品作者吴宇航
                # to have transparency go from 0 to 255, the second iteration will#本作品作者吴宇航
                # have it go from 255 to 0. This is the "flash".#本作品作者吴宇航
                for transparency in range(start, end, animationSpeed * step):#本作品作者吴宇航
                    DISPLAYSURF.blit(origSurf, (0, 0))#本作品作者吴宇航
                    r, g, b = color#本作品作者吴宇航
                    flashSurf.fill((r, g, b, transparency))#本作品作者吴宇航
                    DISPLAYSURF.blit(flashSurf, (0, 0))#本作品作者吴宇航
                    drawBoard(board) # draw board ON TOP OF the transparency layer#本作品作者吴宇航
                    pygame.display.update()#本作品作者吴宇航
                    FPSCLOCK.tick(FPS)#本作品作者吴宇航
            DISPLAYSURF.blit(origSurf, (0, 0)) # redraw the original surface#本作品作者吴宇航
        #本作品作者吴宇航
        #本作品作者吴宇航
        def floodAnimation(board, paletteClicked, animationSpeed=25):#本作品作者吴宇航
            origBoard = copy.deepcopy(board)#本作品作者吴宇航
            floodFill(board, board[0][0], paletteClicked, 0, 0)#本作品作者吴宇航
        #本作品作者吴宇航
            for transparency in range(0, 255, animationSpeed):#本作品作者吴宇航
                # The "new" board slowly become opaque over the original board.#本作品作者吴宇航
                drawBoard(origBoard)#本作品作者吴宇航
                drawBoard(board, transparency)#本作品作者吴宇航
                pygame.display.update()#本作品作者吴宇航
                FPSCLOCK.tick(FPS)#本作品作者吴宇航
        #本作品作者吴宇航
        #本作品作者吴宇航
        def generateRandomBoard(width, height, difficulty=MEDIUM):#本作品作者吴宇航
            # Creates a board data structure with random colors for each box.#本作品作者吴宇航
            board = []#本作品作者吴宇航
            for x in range(width):#本作品作者吴宇航
                column = []#本作品作者吴宇航
                for y in range(height):#本作品作者吴宇航
                    column.append(random.randint(0, len(paletteColors) - 1))#本作品作者吴宇航
                board.append(column)#本作品作者吴宇航
        #本作品作者吴宇航
            # Make board easier by setting some boxes to same color as a neighbor.#本作品作者吴宇航
        #本作品作者吴宇航
            # Determine how many boxes to change.#本作品作者吴宇航
            if difficulty == EASY:#本作品作者吴宇航
                if boxSize == SMALLBOXSIZE:#本作品作者吴宇航
                    boxesToChange = 100#本作品作者吴宇航
                else:#本作品作者吴宇航
                    boxesToChange = 1500#本作品作者吴宇航
            elif difficulty == MEDIUM:#本作品作者吴宇航
                if boxSize == SMALLBOXSIZE:#本作品作者吴宇航
                    boxesToChange = 5#本作品作者吴宇航
                else:#本作品作者吴宇航
                    boxesToChange = 200#本作品作者吴宇航
            else:#本作品作者吴宇航
                boxesToChange = 0#本作品作者吴宇航
        #本作品作者吴宇航
            # Change neighbor's colors:#本作品作者吴宇航
            for i in range(boxesToChange):#本作品作者吴宇航
                # Randomly choose a box whose color to copy#本作品作者吴宇航
                x = random.randint(1, width-2)#本作品作者吴宇航
                y = random.randint(1, height-2)#本作品作者吴宇航
        #本作品作者吴宇航
                # Randomly choose neighbors to change.#本作品作者吴宇航
                direction = random.randint(0, 3)#本作品作者吴宇航
                if direction == 0: # change left and up neighbor#本作品作者吴宇航
                    board[x-1][y] = board[x][y]#本作品作者吴宇航
                    board[x][y-1] = board[x][y]#本作品作者吴宇航
                elif direction == 1: # change right and down neighbor#本作品作者吴宇航
                    board[x+1][y] = board[x][y]#本作品作者吴宇航
                    board[x][y+1] = board[x][y]#本作品作者吴宇航
                elif direction == 2: # change right and up neighbor#本作品作者吴宇航
                    board[x][y-1] = board[x][y]#本作品作者吴宇航
                    board[x+1][y] = board[x][y]#本作品作者吴宇航
                else: # change left and down neighbor#本作品作者吴宇航
                    board[x][y+1] = board[x][y]#本作品作者吴宇航
                    board[x-1][y] = board[x][y]#本作品作者吴宇航
            return board#本作品作者吴宇航
        #本作品作者吴宇航
        #本作品作者吴宇航
        def drawLogoAndButtons():#本作品作者吴宇航
            # draw the Ink Spill logo and Settings and Reset buttons.#本作品作者吴宇航
            DISPLAYSURF.blit(LOGOIMAGE, (WINDOWWIDTH - LOGOIMAGE.get_width(), 0))#本作品作者吴宇航
            DISPLAYSURF.blit(SETTINGSBUTTONIMAGE, (WINDOWWIDTH - SETTINGSBUTTONIMAGE.get_width(), WINDOWHEIGHT - SETTINGSBUTTONIMAGE.get_height()))#本作品作者吴宇航
            DISPLAYSURF.blit(RESETBUTTONIMAGE, (WINDOWWIDTH - RESETBUTTONIMAGE.get_width(), WINDOWHEIGHT - SETTINGSBUTTONIMAGE.get_height() - RESETBUTTONIMAGE.get_height()))#本作品作者吴宇航
        #本作品作者吴宇航
        #本作品作者吴宇航
        def drawBoard(board, transparency=255):#本作品作者吴宇航
            # The colored squares are drawn to a temporary surface which is then#本作品作者吴宇航
            # drawn to the DISPLAYSURF surface. This is done so we can draw the#本作品作者吴宇航
            # squares with transparency on top of DISPLAYSURF as it currently is.#本作品作者吴宇航
            tempSurf = pygame.Surface(DISPLAYSURF.get_size())#本作品作者吴宇航
            tempSurf = tempSurf.convert_alpha()#本作品作者吴宇航
            tempSurf.fill((0, 0, 0, 0))#本作品作者吴宇航
        #本作品作者吴宇航
            for x in range(boardWidth):#本作品作者吴宇航
                for y in range(boardHeight):#本作品作者吴宇航
                    left, top = leftTopPixelCoordOfBox(x, y)#本作品作者吴宇航
                    r, g, b = paletteColors[board[x][y]]#本作品作者吴宇航
                    pygame.draw.rect(tempSurf, (r, g, b, transparency), (left, top, boxSize, boxSize))#本作品作者吴宇航
            left, top = leftTopPixelCoordOfBox(0, 0)#本作品作者吴宇航
            pygame.draw.rect(tempSurf, BLACK, (left-1, top-1, boxSize * boardWidth + 1, boxSize * boardHeight + 1), 1)#本作品作者吴宇航
            DISPLAYSURF.blit(tempSurf, (0, 0))#本作品作者吴宇航
        #本作品作者吴宇航
        #本作品作者吴宇航
        def drawPalettes():#本作品作者吴宇航
            # Draws the six color palettes at the bottom of the screen.#本作品作者吴宇航
            numColors = len(paletteColors)#本作品作者吴宇航
            xmargin = int((WINDOWWIDTH - ((PALETTESIZE * numColors) + (PALETTEGAPSIZE * (numColors - 1)))) / 2)#本作品作者吴宇航
            for i in range(numColors):#本作品作者吴宇航
                left = xmargin + (i * PALETTESIZE) + (i * PALETTEGAPSIZE)#本作品作者吴宇航
                top = WINDOWHEIGHT - PALETTESIZE - 10#本作品作者吴宇航
                pygame.draw.rect(DISPLAYSURF, paletteColors[i], (left, top, PALETTESIZE, PALETTESIZE))#本作品作者吴宇航
                pygame.draw.rect(DISPLAYSURF, bgColor,   (left + 2, top + 2, PALETTESIZE - 4, PALETTESIZE - 4), 2)#本作品作者吴宇航
        #本作品作者吴宇航
        #本作品作者吴宇航
        def drawLifeMeter(currentLife):#本作品作者吴宇航
            lifeBoxSize = int((WINDOWHEIGHT - 40) / maxLife)#本作品作者吴宇航
        #本作品作者吴宇航
            # Draw background color of life meter.#本作品作者吴宇航
            pygame.draw.rect(DISPLAYSURF, bgColor, (20, 20, 20, 20 + (maxLife * lifeBoxSize)))#本作品作者吴宇航
        #本作品作者吴宇航
            for i in range(maxLife):#本作品作者吴宇航
                if currentLife >= (maxLife - i): # draw a solid red box#本作品作者吴宇航
                    pygame.draw.rect(DISPLAYSURF, RED, (20, 20 + (i * lifeBoxSize), 20, lifeBoxSize))#本作品作者吴宇航
                pygame.draw.rect(DISPLAYSURF, WHITE, (20, 20 + (i * lifeBoxSize), 20, lifeBoxSize), 1) # draw white outline#本作品作者吴宇航
        #本作品作者吴宇航
        #本作品作者吴宇航
        def getColorOfPaletteAt(x, y):#本作品作者吴宇航
            # Returns the index of the color in paletteColors that the x and y parameters#本作品作者吴宇航
            # are over. Returns None if x and y are not over any palette.#本作品作者吴宇航
            numColors = len(paletteColors)#本作品作者吴宇航
            xmargin = int((WINDOWWIDTH - ((PALETTESIZE * numColors) + (PALETTEGAPSIZE * (numColors - 1)))) / 2)#本作品作者吴宇航
            top = WINDOWHEIGHT - PALETTESIZE - 10#本作品作者吴宇航
            for i in range(numColors):#本作品作者吴宇航
                # Find out if the mouse click is inside any of the palettes.#本作品作者吴宇航
                left = xmargin + (i * PALETTESIZE) + (i * PALETTEGAPSIZE)#本作品作者吴宇航
                r = pygame.Rect(left, top, PALETTESIZE, PALETTESIZE)#本作品作者吴宇航
                if r.collidepoint(x, y):#本作品作者吴宇航
                    return i#本作品作者吴宇航
            return None # no palette exists at these x, y coordinates#本作品作者吴宇航
        #本作品作者吴宇航
        #本作品作者吴宇航
        def floodFill(board, oldColor, newColor, x, y):#本作品作者吴宇航
            # This is the flood fill algorithm.#本作品作者吴宇航
            if oldColor == newColor or board[x][y] != oldColor:#本作品作者吴宇航
                return#本作品作者吴宇航
        #本作品作者吴宇航
            board[x][y] = newColor # change the color of the current box#本作品作者吴宇航
        #本作品作者吴宇航
            # Make the recursive call for any neighboring boxes:#本作品作者吴宇航
            if x > 0:#本作品作者吴宇航
                floodFill(board, oldColor, newColor, x - 1, y) # on box to the left#本作品作者吴宇航
            if x < boardWidth - 1:#本作品作者吴宇航
                floodFill(board, oldColor, newColor, x + 1, y) # on box to the right#本作品作者吴宇航
            if y > 0:#本作品作者吴宇航
                floodFill(board, oldColor, newColor, x, y - 1) # on box to up#本作品作者吴宇航
            if y < boardHeight - 1:#本作品作者吴宇航
                floodFill(board, oldColor, newColor, x, y + 1) # on box to down#本作品作者吴宇航
        #本作品作者吴宇航
        #本作品作者吴宇航
        def leftTopPixelCoordOfBox(boxx, boxy):#本作品作者吴宇航
            # Returns the x and y of the left-topmost pixel of the xth & yth box.#本作品作者吴宇航
            xmargin = int((WINDOWWIDTH - (boardWidth * boxSize)) / 2)#本作品作者吴宇航
            ymargin = int((WINDOWHEIGHT - (boardHeight * boxSize)) / 2)#本作品作者吴宇航
            return (boxx * boxSize + xmargin, boxy * boxSize + ymargin)#本作品作者吴宇航
        #本作品作者吴宇航
        #本作品作者吴宇航
        if __name__ == '__main__':#本作品作者吴宇航
            main()#本作品作者吴宇航
    elif dakai == "heping":#本作品作者吴宇航
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
        fangwen("https://livefile.xesimg.com/programme/python_assets/0570f61570c7e6b3b02d4007c9d8bf19.html")#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
    elif dakai == "wangzhe":#本作品作者吴宇航
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
        fangwen("https://livefile.xesimg.com/programme/python_assets/75eb463230104eb7cc467e49c869409b.html")#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
    elif dakai == "off":#本作品作者吴宇航
        caidanlan = Tk()#本作品作者吴宇航
        caidanlan.geometry("250x350")#本作品作者吴宇航
        caidanlan.title("开始菜单")#本作品作者吴宇航
#本作品作者吴宇航
        applb = Listbox(caidanlan, width = 90, height = 30, bg = "grey", fg = "blue")#本作品作者吴宇航
        for i in range(len(applist)):#本作品作者吴宇航
            applb.insert(0,applist[i])#本作品作者吴宇航
            #本作品作者吴宇航
        #本作品作者吴宇航
        applb.pack()#本作品作者吴宇航
        caidanlan.mainloop()#本作品作者吴宇航
        fasdasdf1()#本作品作者吴宇航
fasdasdf1()#curselection()#本作品作者吴宇航
