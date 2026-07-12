from file.AISPEAK import (aispeak as speak,setmode,setspeed)
from tkinter import messagebox as msg
from webbrowser import open as wopen
from file.baidu import query
from urllib import request
from xes.common import *
from file.cf import *
from time import *
import file.data as databases
import tkinter as tk
import requests
import struct
import random
import urllib
import pygame
import jieba
import json
import sys
import os
import re

gametips_str='''
使用代码以及语言：编程语言-python
代码编辑：小轩
主代码编写：小轩
素材征集：小轩
修饰、代码格式等：小轩
代码量统计：小轩
彩蛋：小轩
exe打包：暂无
建议，鼓励与协助：CSDN资料 胡锦辉 吴宇航 徐一茗 李俊鑫 张颢译 王玎珰 刘炳毅 yzy（严子昱）
python语言开发：Guido van Rossum
python编译器支持：学而思网校-学而思编程(——每天进步一点点——)
python教学：学而思网校-学而思编程(——每天进步一点点——)
第三方库支持：学而思网校-学而思编程(——每天进步一点点——)
灵感激发：李俊鑫 Toby Fox^传说之下 杨浩轩 太空狼人杀 胡锦辉 火焰工作室 yzy（严子昱） B站
特殊库支持：
baidu.py      |百度
cf.py         |CSDN
AISPEAK.py    |学而思网校-学而思编程(——每天进步一点点——)
对此3库改动   |小轩

小轩@宇宙工作室(SPC) 版权所有 侵权必究
人生苦短，我用python
抵制不良游戏，拒绝盗版游戏。
注意自我保护，谨防受骗上当。
适度游戏益脑，沉迷游戏伤身。
合理安排时间，享受健康生活。
把你在游戏里的智慧用到现实里。
发现抄袭立即采取举报等措施
未成年人用户游戏时间不得超过一小时，请自行遵守。
'''
print(gametips_str)

most_random_game_value = random.randint(1,100)
'''
游戏决定值：
1.游戏标题
2.AI聊天框65%可能性是青色，其他是黄色
'''

def game_lent_video():
    os.system('start file/video/小A背景故事.mp4')


# import user_login
def dataload(emoji_str):
	return ''.join(c if c <= '\uffff' else ''.join(chr(x) for x in struct.unpack('>2H', c.encode('utf-16be'))) for c in emoji_str)
def getinfo(id):
	s = requests.Session()
	headers = {'Accept': 'application/json, text/plain, */*', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'Cookie': 'xesId=b524835904a4a420cba3dde34890bade; user-select=scratch;  xes_run_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiIuY29kZS54dWVlcnNpLmNvbSIsImF1ZCI6Ii5jb2RlLnh1ZWVyc2kuY29tIiwiaWF0IjoxNjAxODA5NDcxLCJuYmYiOjE2MDE4MDk0NzEsImV4cCI6MTYwMTgyMzg3MSwidXNlcl9pZCI6bnVsbCwidWEiOiJNb3ppbGxhXC81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXRcLzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZVwvODUuMC40MTgzLjEyMSBTYWZhcmlcLzUzNy4zNiBFZGdcLzg1LjAuNTY0LjY4IiwiaXAiOiIxMTIuNDkuNzIuMTc1In0.9bXcb813GhSPhoUJkezZpV8O50ynm0hhYvszNyczznQ; prelogid=ef8f6d12febabf75bf9599744b73c6f5; xes-code-id=87f66376f1afd34f70339baeca61b7a1.8dbd833da9122d69a17f91054066dbb3; X-Request-Id=82f1c3968c8ff01ee151a0413f56aa84; Hm_lpvt_a8a78faf5b3e92f32fe42a94751a74f1=1601809487', 'Host': 'code.xueersi.com', 'Proxy-Connection': 'keep-alive', 'Referer': 'http://code.xueersi.com/space/11909587', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.68'}
	total = json.loads(dataload(s.get("http://code.xueersi.com/api/space/profile?user_id=" + str(id), headers=headers).text))["data"]
	return total["realname"]
try:
    num=getCookies().index("stu_id=")+7
    id=""
    for i in range(num,num+111):
        if getCookies()[i]!=";":
            id=id+getCookies()[i]
        else:
            break
    username = str(getinfo(id))
except:
    username = '未登录编程社区游客'
print(username+'已登录并进入游戏')

root = tk.Tk()
if most_random_game_value <= 90: # 90%可能是这个标题
    root.title('小轩的人工智能机器人小A')
else:
    root.title('小A人工智能机器人-小轩[智]造')
root.iconbitmap('file/img/gameicon/小轩头像.ico')
root.geometry('1400x900+120+60')
root.resizable(0,0)
root.config(cursor="none")
pgw = tk.Frame(root,width = 1400, height = 900)
pgw.pack()
os.environ['SDL_WINDOWID'] = str(pgw.winfo_id())
talkstartStringVar = tk.StringVar()
talkstartStringVar.set('想说什么...')
entry = tk.Entry(root,font=('楷体',25),textvariable=talkstartStringVar)

pygame.init()
pygame.display.set_caption("AI机器人|小A|")
screen = pygame.display.set_mode((1400,900),pygame.NOFRAME)

start_logo1 = pygame.image.load('file/img/gameicon/开始logo1.png').convert()
start_logo2 = pygame.image.load('file/img/gameicon/开始logo2.png').convert()
okButton = pygame.image.load('file/img/确认.png')
morningbg = pygame.transform.scale(pygame.image.load('file/img/客厅.jpg'),(1400,900))
eveningbg = pygame.transform.scale(pygame.image.load('file/img/客厅夜晚.jpg'),(1400,900))
AIalways = pygame.transform.scale(pygame.image.load('file/img/AI平常.png'),(488,368))
AIhello = pygame.transform.scale(pygame.image.load('file/img/AI招手.png'),(488,368))
if most_random_game_value > 35: # 65%可能性是青色
    talk_blank = pygame.image.load('file/img/talk_blank.png').convert()
else:
    talk_blank = pygame.image.load('file/img/talk_blank_yellow.png').convert()
handc = pygame.image.load('file/img/手指鼠标.png')
arrowc = pygame.image.load('file/img/鼠标.png')
goto_lang = pygame.image.load('file/img/去长廊.png')
long_lang = pygame.image.load('file/img/长廊.png')
long_lang_pic_lie = pygame.image.load('file/img/长廊隐藏彩蛋图片遮挡物质.png')
lang_door1 = pygame.image.load('file/img/长廊门1.png')
lang_door2 = pygame.image.load('file/img/长廊门2.png')
AIroom_bgpic = pygame.image.load('file/img/机器人室.png')
study_bgpic = pygame.image.load('file/img/书房.png')
AIjieba = pygame.image.load('file/img/智能分词.png')
AIcalculation = pygame.image.load('file/img/四则运算.png')
AIread_again = pygame.image.load('file/img/复读.png')
AI_baidu = pygame.image.load('file/img/百度一下图片.png')
AIagotalk = pygame.image.load('file/img/聊天记录.png')
AIgamehelp = pygame.transform.scale2x(pygame.image.load('file/img/游戏帮助.png'))
study_hide_book = pygame.image.load('file/img/书房隐藏书.png')
secretroom0014 = pygame.image.load('file/img/书房后的密室.png')
mice_text = pygame.image.load('file/img/老鼠洞里的字条.png')
password_lock = pygame.image.load('file/img/密码锁.png')
secret_file_background = pygame.image.load('file/img/秘密文件.png')
secret_file_square = pygame.image.load('file/img/秘密文件-正方形.png')
secret_file_triangle = pygame.image.load('file/img/秘密文件-三角形.png')
bigbg_lightbg = pygame.image.load('file/img/大背景-明亮区抠图.png')
bigbg_convertbg = pygame.image.load('file/img/大背景-明亮区黑屏屏风遮挡物质.png').convert()
bigbg_me_img = pygame.image.load('file/img/bigbg_me.png')
sknow_bar = pygame.image.load('file/img/奇识小市.png')
sknow_door_bg = pygame.image.load('file/img/奇识小市门口背景.png')
sknow_ask = pygame.image.load('file/img/开始答题.png')
talk_blank.set_alpha(151)
talk_blank.set_colorkey((0,0,0))
bigbg_convertbg.set_alpha(183)
electronic_clock_screen_rect = pygame.Rect(695,16,390,70)
AIalwaysRect = AIalways.get_rect()
AIhelloRect = AIhello.get_rect()
okButtonRect = okButton.get_rect()
okButtonRect.center = (500,okButtonRect.height-30)
goto_lang_rect = goto_lang.get_rect()
goto_lang_rect.topleft = (1111,16)
lang_door1rect = lang_door1.get_rect()
lang_door1rect.bottomleft = (280,643)
lang_door2rect = lang_door2.get_rect()
lang_door2rect.bottomleft = (480,643)
AIjiebarect = AIjieba.get_rect()
AIjiebarect.topleft = (100,88)
AIcalculationrect = AIcalculation.get_rect()
AIcalculationrect.topleft = (220,88)
AIread_againrect = AIread_again.get_rect()
AIread_againrect.topleft = (340,88)
AI_baidurect = AI_baidu.get_rect()
AI_baidurect.topleft = (879,58)
AIagotalkrect = AIagotalk.get_rect()
AIagotalkrect.topleft = (625,40)
AIroom_interval_rect = pygame.Rect(566,8,30,172)
AIgamehelprect = AIgamehelp.get_rect()
AIgamehelprect.topleft = (1111,8)
study_hide_bookrect = study_hide_book.get_rect()
study_hide_bookrect.bottomright = (1300,380)
mice_textrect = mice_text.get_rect()
mice_textrect.topleft = (1111,841)
password_lockrect = password_lock.get_rect()
password_lockrect.topleft = (73,489)
secret_file_squarerect = secret_file_square.get_rect()
secret_file_squarerect.topleft = (1091,407)
secret_file_trianglerect = secret_file_triangle.get_rect()
secret_file_trianglerect.topleft = (627,735)
bigbg_me_imgrect = bigbg_me_img.get_rect()
bigbg_me_imgrect.midbottom = (700,450)
sknow_bar_rect = sknow_bar.get_rect()
sknow_bar_rect.topleft = (17,35)
sknow_ask_rect = sknow_ask.get_rect()
sknow_ask_rect.topleft = (803,532)

# 音效
pms = pygame.mixer.Sound
archive_sound = pms('file/music/存档声音.wav')        # 存档声音171KB
cilck_key_sound = pms('file/music/机灵.wav')        # 存档声音108KB
# 音效

t1 = 0
t2 = 1
talk_speak = 100
mouseccut = 'ok'
eventpos = (0,0)
am_or_pm = None
bigbg_X = 0
bigbg_Y = 0
bigbg_KEYDOWN = False
talk = True
task1 = False                 # 任务1：打开帮助
task2 = False                 # 任务2：打开书房绝密隐藏书
task3 = False                 # 任务3：打开湖畔密室0014的保险柜
task4_mode1 = False           # 任务4-1：按下d
task4_mode2 = False           # 任务4-2：把五角星（三角形）拖到正方形里面
task4_mode3_n = False         # 任务4-3-1：按下n
task4_mode3_u = False         # 任务4-3-2：按下u
task4_mode3_m = False         # 任务4-3-3：按下m
task4_mode3_b = False         # 任务4-3-4：按下b
task4_mode3_e = False         # 任务4-3-5：按下e
task4_mode3_r = False         # 任务4-3-6：按下r
task4_mode3_s = False         # 任务4-3-7：按下s
task4_mode4 = False           # 任务4-4：点击正方形
task4 = False                 # 任务4-5：按下L
task5 = False                 # 任务5：再次打开书房绝密隐藏书
task6_mode = 0                # 任务6-模式：大背景里按下的机关数
task6 = False                 # 任务6：大背景机关完成后按下A
task7 = False                 # 任务7：书房按下e
task8 = False                 # 任务8：奇识小市入口答题成功
secret_file_trianglerect_is_check_mode = False
mice_text_word = False
part = '主客厅'
AI_talk_list = []

# 彩蛋----------------------
'''
我们有如下彩蛋：
1.鼠冷知识
2.鼠你最吱洞
3.小小书虫
'''
colorful_eggs = []
# 彩蛋----------------------

try:
    with open('D:/system_jhxc/my_game/gamebox/myAI_small_A_game/what to talk.txt','r') as f:
        AI_talk_list = eval(f.read())
        talk_thing = random.choice(['哇，主人你又来了','欢迎再次到来','主人你回来啦','太棒了，主人回来了','额，主人我好想你，呜呜呜','I am very happy to see you'])
        AI_talk_list.append(talk_thing)
        f.close()
except:
    try:
        mkdir('D:\\system_jhxc\\my_game\\gamebox\\myAI_small_A_game')
        talk_thing = 'Hi，我是小A人工智能机器人^_^，我可以查天气，讲笑话哦~ ………………我还有很多好玩实用的功能哦~ ………………快来试试吧'
        AI_talk_list.append(talk_thing)
    except:
        print('恭喜你，没有D盘（或D盘被锁、D盘不能存文件），无法存档，直接退出游戏，请三连谢谢（很简单，点一下嘛，不会是不敢3连吧）\n你可以试试有D盘的电脑哦，没有D盘的就太落后了~')
        sys.exit()
try:
    with open('D:/system_jhxc/my_game/gamebox/myAI_small_A_game/游戏进度.txt','r') as f:
        exec(f.read())
        f.close()
    print('检测到了你的存档，已经打开并运行，即将继续你的游戏')
except:
    print('没有检测到你的存档，无法读档，即将开始新游戏')

try:import ntpath
except:font = pygame.font.SysFont('kaittf', 30)
else:font = pygame.font.SysFont('kaiti', 30);del ntpath

def tk_callback():
    global part
    if part == '主客厅':
        print('服务关闭中……')
        print('解除堆栈中……')
        print('聊天记录存档中……')
        with open('D:/system_jhxc/my_game/gamebox/myAI_small_A_game/what to talk.txt','w') as f:
            f.write(str(AI_talk_list))
            f.close()
        print('运行完毕')
        root.destroy()
        print('exit command...')
        print('file exit.')
        print('exe cut')
        print('tkinter WM_DELETE_WINDOW openning...')
        print('exit..')
        print('com link exit...')
        sys.exit()
    elif part == '长廊':
        part = '主客厅'
    elif part == '机器人室':
        part = '长廊'
    elif part == '书房':
        part = '长廊'
    elif part == '书架后的密室':
        part = '书房'
    elif part == '大背景':
        part = '书房'
    elif part == '奇识小市':
        part = '长廊'

root.protocol("WM_DELETE_WINDOW",tk_callback)
def show_text(text,color=(0,0,0),pos=(0,0)):
    screen.blit(font.render((text),True,color),pos)
def show_bg(img):
    screen.blit(img,(0,0))
def AImapGo(xy,map=AIalways,maprect=AIalwaysRect):
    global myAI,myAIrect
    myAI = map
    myAIrect = maprect
    if xy == 'center':
        myAIrect.center = (700,450)
    if type(xy) != str:
        myAIrect.center = xy
def jieba_cut_word(word):
    if word != '':
        word = '  '.join(jieba.lcut(word))
        msg.showinfo('智能分词',word)
    else:
        msg.showerror('空内容','空空如也~')
def entry_del_text():
    global entry
    entry.delete(entry.index(tk.INSERT)-1)
button = tk.Button(root,text='  退格  ',command=entry_del_text,border=5,activebackground='cyan',relief=tk.RIDGE)
def top_archive():
    global colorful_eggs,task1,task2,task3,task4,task5
    archive_sound.play()
    with open('D:/system_jhxc/my_game/gamebox/myAI_small_A_game/游戏进度.txt','w') as f:
        f.write('colorful_eggs = '+str(colorful_eggs)+'\n')
        if task1 == True:f.write('task1 = True\n')
        else:f.write('task1 = False\n')
        if task2 == True:f.write('task2 = True\n')
        else:f.write('task2 = False\n')
        if task3 == True:f.write('task3 = True\n')
        else:f.write('task3 = False\n')
        if task4 == True:f.write('task4 = True\n')
        else:f.write('task4 = False\n')
        if task5 == True:f.write('task5 = True\n')
        else:f.write('task5 = False\n')
        if task6 == True:f.write('task6 = True\n')
        else:f.write('task6 = False\n')
        if task7 == True:f.write('task7 = True\n')
        else:f.write('task7 = False\n')
        if task8 == True:f.write('task8 = True\n')
        else:f.write('task8 = False\n')
        f.close()
def game_acc_die():
    wopen('https://www.bilibili.com/video/BV1NZ4y1j7nw/')
def tk_ago_talk():
    global AI_talk_list
    ago_talk_window = tk.Toplevel(root)
    ago_talk_window.title('聊天记录')
    ago_talk_window.attributes('-alpha',0.85)
    def tk_del_ago_talk():
        global AI_talk_list
        AI_talk_list = ['Hi，我是小A人工智能机器人^_^，我可以查天气，讲笑话哦~ ………………我还有很多好玩实用的功能哦~ ………………快来试试吧']
        ago_talk_window.destroy()
    sbar_y = tk.Scrollbar(ago_talk_window)
    sbar_y.pack(side=tk.RIGHT,fill=tk.Y)
    textbox = tk.Text(ago_talk_window,height=35,width=100,font=('黑体',14),yscrollcommand=sbar_y.set)
    textbox.insert('1.0','越接近顶部的聊天消息越新哦~\n')
    for i in AI_talk_list:
        textbox.insert('2.0',i+'\n')
    sbar_y.config(command=textbox.yview)
    textbox.pack()
    delbutton = tk.Button(ago_talk_window,text='清空（解除内存）',command=tk_del_ago_talk)
    delbutton.pack()
def gamehelp():
    global task1
    task1 = True
    gamehelp_window = tk.Toplevel(root)
    gamehelp_window.title('新手必读系列-游戏帮助')
    textbox = tk.Text(gamehelp_window,height=35,width=100,font=('黑体',14))
    textbox.insert('end','新手必读系列-游戏帮助\n')
    textbox.insert('end','你发现了帮助，还挺聪明。本游戏有多种玩法：\n')
    textbox.insert('end','1.AI聊聊*玩法：把小A当成你的朋友，只在客厅与小A聊天\n')
    textbox.insert('end','2.统治AI*玩法：把小A当成你的仆人，在客厅、机器人室等有用地区为你服务\n')
    textbox.insert('end','3.闯关-不为人知的秘密*玩法：从你打开此帮助开始，你就可以见到书房的门，进书房后，找到一些特殊的地方，然后达成任务（你进去就知道是啥任务了）。之后，你就可以进入隐藏的密室3rd room玩游戏\n')
    textbox.insert('end','4.自由*玩法：想怎么玩就怎么玩\n')
    textbox.insert('end','5.彩蛋*玩法：专门寻找游戏里的彩蛋（多在玩法3里），并回复在评论区，目前作者已经安排了3个彩蛋\n')
    textbox.insert('end','在主客厅点屏幕右上角的X关闭游戏，其他房间点它会回到上一个界面\n')
    textbox.insert('end','更多玩法，请您研究！\n')
    textbox.insert('end','有意见请反馈在评论区\n')
    textbox.insert('end','这是【版权@小轩-超大型游戏】研发的游戏哦\n')
    textbox.insert('end','代码目前1000多行，而且是个超大型游戏，所以不是一下就能玩完的，可以存档哦~到存档点就有存档按钮供存档~书房有一个总存档点哦~\n')
    textbox.insert('end','要攻略问我\n')
    textbox.insert('end','帮助内容往后还会增多，祝您玩得开心！\n')
    textbox.pack()
def study_hide_book_text():
    global task2,task4,task5,colorful_eggs
    if task4 == False:
        task2 = True
        gamehelp_window = tk.Toplevel(root)
        gamehelp_window.title('绝密隐藏书')
        textbox = tk.Text(gamehelp_window,height=35,width=100,font=('黑体',14))
        textbox.insert('end','绝密隐藏书\n')
        textbox.insert('end','这里有一些机关，本书就是一个\n')
        textbox.insert('end','第一个任务是帮助，第二个就是此书\n')
        textbox.insert('end','先夸你一句眼力好\n')
        textbox.insert('end','还是说正事吧，我这个机关已经打开了，任务2也就完成了\n')
        textbox.insert('end','从打开我开始，在书房按q就能进入书架后面的一个密室\n')
        textbox.insert('end','对了，我……好像…忘了……什么——在书房按w可以存档\n')
        textbox.insert('end','合上书开始执行吧\n')
        textbox.pack()
    else:
        if task5 != True:
            task5 = True
            gamehelp_window = tk.Toplevel(root)
            gamehelp_window.title('绝密隐藏书')
            textbox = tk.Text(gamehelp_window,height=35,width=100,font=('黑体',14))
            textbox.insert('end','绝密隐藏书\n')
            textbox.insert('end','什么？你完成任务4之后又打开了我？！\n')
            textbox.insert('end','第3个任务是打开保险柜，第4个是完成秘密文件上的指令，第5个就是再次打开此书\n')
            textbox.insert('end','牛啊\n')
            textbox.insert('end','我这个机关已经打开了，任务5也就完成了\n')
            textbox.insert('end','从现在开始，在书房按q就能进入下一个任务：大背景\n')
            textbox.insert('end','别忘了按w可以存档，不要逞能不存档\n')
            textbox.insert('end','合上书开始执行吧\n')
            textbox.pack()
        else:
            gamehelp_window = tk.Toplevel(root)
            gamehelp_window.title('绝密隐藏书')
            textbox = tk.Text(gamehelp_window,height=35,width=100,font=('黑体',14))
            textbox.insert('end','绝密隐藏书\n')
            textbox.insert('end','wc!!!\n')
            textbox.insert('end','(脑子有病！！！)\n')
            textbox.insert('end','好吧，等会按e，然后去长廊\n')
            textbox.insert('end','你找到了彩蛋——“小小书虫”\n')
            textbox.insert('end','真\n')
            textbox.insert('end','  没\n')
            textbox.insert('end','    了\n')
            textbox.insert('end','  啊\n')
            textbox.insert('end','，\n')
            textbox.insert('end','不信自己看\n')
            textbox.insert('end','别来\n')
            textbox.insert('end','我这\n')
            textbox.insert('end','闹了\n')
            textbox.insert('end','…………\n')
            textbox.insert('end','……………………\n')
            textbox.insert('end','…………………………………………\n')
            textbox.insert('end','……………………………………………………………………………………\n')
            textbox.insert('end','…………………………………………………………………………………………………………………………………………………………………………\n')
            textbox.insert('end','.\n')
            textbox.insert('end','呃(⊙o⊙)……\n')
            textbox.insert('end','再见了，我要背书了。sin cos tan atan -x x -y y i -i fx sqrt...\n')
            colorful_eggs.append('小小书虫')
            textbox.pack()
def show_mice_text():
    global mice_text_word,colorful_eggs
    mice_window = tk.Toplevel(root)
    mice_window.title('新手禁读-老鼠们的提示')
    textbox = tk.Text(mice_window,height=35,width=100,font=('黑体',14))
    if mice_text_word == False:
        textbox.insert('end','新手禁读-老鼠们的提示 第1页\n')
        textbox.insert('end','恭喜找到彩蛋——鼠你最吱洞——我们是一群住在老鼠洞里的老鼠，吱吱……\n')
        textbox.insert('end','什么？你想要提示？额。没有。\n')
        textbox.insert('end','az，这仅仅是一个彩蛋，别追问了\n')
        colorful_eggs.append('鼠你最吱洞')
        mice_text_word = '别追问了'
    elif mice_text_word == '别追问了':
        textbox.insert('end','新手禁读-老鼠们的提示 第2页\n')
        textbox.insert('end','吱吱，你怎么又来了？\n')
        textbox.insert('end','你傻了吗？\n')
        textbox.insert('end','识时务的快走\n')
        mice_text_word = '快走'
    elif mice_text_word == '快走':
        textbox.insert('end','新手禁读-老鼠们的提示 第3页\n')
        textbox.insert('end','你在搞什么？我们还要睡觉呢！\n')
        textbox.insert('end','信不信我关机？\n')
        textbox.insert('end','你不该看的，这个一般禁读\n')
        mice_text_word = '不该看'
    elif mice_text_word == '不该看':
        textbox.insert('end','新手禁读-老鼠们的提示 第4页\n')
        textbox.insert('end','你 不 死 心 是 吗\n')
        textbox.insert('end','你不怕「关机」？\n')
        textbox.insert('end','吱吱吱吱吱吱！\n')
        mice_text_word = '关机吧'
    elif mice_text_word == '关机吧':
        textbox.insert('end','新手禁读-老鼠们的提示 第5页\n')
        textbox.insert('end','呵呵\n')
        textbox.insert('end','呵呵\n')
        textbox.insert('end','吱吱，你这么有耐心，我就告诉你吧\n')
        textbox.insert('end','不过……\n')
        textbox.insert('end','吱吱\n')
        textbox.insert('end','吱吱吱吱吱吱\n')
        textbox.insert('end','你还要再点几遍！\n')
        mice_text_word = '再点点'
    elif mice_text_word == '再点点':
        textbox.insert('end','新手禁读-老鼠们的提示 第6页\n')
        textbox.insert('end','这里似乎空空如也\n')
        mice_text_word = '再点点2'
    elif mice_text_word == '再点点2':
        textbox.insert('end','新手禁读-老鼠们的提示 第7页\n')
        mice_text_word = '再点点3'
    elif mice_text_word == '再点点3':
        textbox.insert('end','新手禁读-老鼠们的提示 第8页\n')
        textbox.insert('end','吱——\n')
        mice_text_word = '再点点end'
    elif mice_text_word == '再点点end':
        textbox.insert('end','新手禁读-老鼠们的提示 第9页\n')
        textbox.insert('end','算你有耐心，算你伟大！\n')
        textbox.insert('end','密码的前五位是256×256-1的答案\n')
        textbox.insert('end','最后一位是汉字，我们的称呼，“鼠”\n')
        textbox.insert('end','以上是保险柜的六位密码\n')
        mice_text_word = '结束1'
    elif mice_text_word == '结束1':
        textbox.insert('end','新手禁读-老鼠们的提示 第10页\n')
        textbox.insert('end','我们已经说完了，这是最后一页。\n')
        mice_text_word = '结束2'
    elif mice_text_word == '结束2':
        textbox.insert('end','新手禁读-老鼠们的提示 第10页\n')
        textbox.insert('end','我们已经说完了，这是最后一页。\n')
        mice_text_word = '结束3'
    elif mice_text_word == '结束3':
        textbox.insert('end','新手禁读-老鼠们的提示 第10页\n')
        textbox.insert('end','我们已经说完了，这是最后一页。\n')
        mice_text_word = '结束4'
    else:
        textbox.insert('end','新手禁读-老鼠们的提示 第11页\n')
        textbox.insert('end','好吧，你找到了又一个彩蛋——鼠冷知识。告诉你几个冷知识：\n')
        textbox.insert('end','1.我们老鼠有的被抓去当“警鼠”，用于缉毒、防爆、扫雷等\n')
        textbox.insert('end','2.我们老鼠从5楼摔下来不会死\n')
        textbox.insert('end','3.我们老鼠可以在水里待3天\n')
        textbox.insert('end','然后真的没了\n')
        colorful_eggs.append('鼠冷知识')
    textbox.pack()
def password_lock_input():
    global task3
    def submit_pwd():
        global task3
        # print(pwd_entry.get(),pwd_entry.get() == '65535鼠')
        if pwd_entry.get() == '65535鼠':
            task3 = True
            pwd_lock.destroy()
        else:
            os.remove('D:/system_jhxc/my_game/gamebox/myAI_small_A_game/游戏进度.txt')
            print('\033[1;31m Game over')
            print('YOU DIED - YOU LOSE')
            print('原因：密码错误，小A接收到警报，经过最高指挥官小轩命令，把你K了')
            print('所有存档已经清空并删除，请等待并重新开始（复活）')
            print('\033[0m 小轩@宇宙工作室 出版')
            root.destroy()
            sys.exit()
    pwd_lock = tk.Toplevel(root)
    pwd_lock.title('一块液晶屏密码锁')
    label = tk.Label(pwd_lock,text='我是一块液晶屏密码锁')
    label.pack()
    pwd_entry = tk.Entry(pwd_lock)
    pwd_entry.pack()
    btn = tk.Button(pwd_lock,text='\n    确认    \n',command=submit_pwd)
    btn.pack()
    
def AAtalk(MyInputWord):
    global AI_talk_list,username
    if (username in MyInputWord) and (username != '小轩'):
        Aword_X = '我知道你叫'+username+'呀，小轩告诉过我了'
        AI_talk_list.append('我：'+MyInputWord)
        AI_talk_list.append('小A：'+Aword_X)
        return Aword_X
    api_url = "http://openapi.tuling123.com/openapi/api/v2"
    data = {
        "reqType": 0,
        "perception":
        {
            "inputText":
            {
                "text": MyInputWord
            },
        },
        "userInfo":
        {
            "apiKey": "57e8a35bf9f349a1bb49f2da6d48d518",
            "userId": "586065"
        }
    }
    data = json.dumps(data).encode('utf8')
    response_str = requests.post(api_url, data=data, headers={'content-type': 'application/json'})
    response_dic = response_str.json()
    Aword = response_dic['results'][0]['values']['text']
    try:Aword = Aword.replace('贾维斯','小A')
    except:pass
    try:Aword = Aword.replace('宝宝','主人')
    except:pass
    try:Aword = Aword.replace('杜伯忱',username)
    except:pass
    try:Aword = Aword.replace('伯忱',username)
    except:pass
    if ('不明白' in Aword) or ('不懂' in Aword) or ('不知道' in Aword) or ('不会' in Aword) or ('请求次数超限制' in Aword) or ('太难了' in Aword) or ('没学会' in Aword) or ('未学会' in Aword) or ('没听说过' in Aword):
        x = urllib.parse.quote(MyInputWord)
        link = request.urlopen("http://nlp.xiaoi.com/robot/webrobot?&callback=__webrobot_processMsg&data=%7B%22sessionId%22%3A%22ff725c236e5245a3ac825b2dd88a7501%22%2C%22robotId%22%3A%22webbot%22%2C%22userId%22%3A%227cd29df3450745fbbdcf1a462e6c58e6%22%2C%22body%22%3A%7B%22content%22%3A%22" + x + "%22%7D%2C%22type%22%3A%22txt%22%7D")
        try:Aword = re.findall(r'\"content\":\"(.+?)\\r\\n\"',link.read().decode())[-1]
        except:Aword = 'defaultReply'
        try:Aword = Aword.replace('小i','小A')
        except:pass
        try:Aword = Aword.replace('袁辉','小轩')
        except:pass
        try:Aword = Aword.replace(r'\n',' ')
        except:pass
        try:Aword = Aword.replace(r'\t',' ')
        except:pass
        try:Aword = Aword.replace(r'\r',' ')
        except:pass
        try:Aword = Aword.replace('订机票','')
        except:pass
        if Aword == 'defaultReply':
            Aword = query(MyInputWord)
            if Aword == '':
                Aword = '我太难了，回答不上！'
    try:
        if '我：'+MyInputWord == AI_talk_list[-2]:
            Aword = random.choice(['这个问题你不是已经问过一遍了吗','额额，你刚刚才问过','小主人，不要犯糊涂哦，你问过我啦','你问过啦'])
            if '我：'+MyInputWord == AI_talk_list[-4]:
                Aword = random.choice(['这个问题你不是已经问过两遍了吗','咦，小主人你是傻了吗','小主人，你犯糊涂了，你问了我两遍啦'])
                if '我：'+MyInputWord == AI_talk_list[-6]:
                    Aword = random.choice(['小主人不要皮了','你别开玩笑了吧','憨憨，你有没有得老年痴呆症呀'])
                    if '我：'+MyInputWord == AI_talk_list[-8]:
                        Aword = random.choice(['好了好了','别这样我好难受','小主人，你问了好多遍'])
                        if '我：'+MyInputWord == AI_talk_list[-10]:
                            Aword = random.choice(['我可不高兴了','你问过5遍了，还不满意'])
                            if '我：'+MyInputWord == AI_talk_list[-12]:
                                Aword = random.choice(['哎呀哎呀','别问这个了，我好头大'])
                                if '我：'+MyInputWord == AI_talk_list[-14]:
                                    Aword = random.choice(['你不敢换个话题试试','你只会这样了'])
                                    if '我：'+MyInputWord == AI_talk_list[-16]:
                                        Aword = '小主人，我不想生气'
                                        if '我：'+MyInputWord == AI_talk_list[-18]:
                                            Aword = '算了，看你可怜的样子我帮你关机吧，要吗，再说一遍我就真的关了'
                                            if '我：'+MyInputWord == AI_talk_list[-20]:
                                                os.system('shutdown/s /c 叫你皮 /t 5')
    except:
        pass
    AI_talk_list.append('我：'+MyInputWord)
    AI_talk_list.append('小A：'+Aword)
    return Aword

class bigbg_rect(object):
    def __init__(self):
        self.x = random.randint(0,2500)
        self.y = random.randint(0,1000)
        self.rect = pygame.Rect(self.x,self.y,random.randint(150,300),random.randint(80,200))
        self.color = random.choice([(255,0,0),(255,130,0),(255,255,0),(255,111,80)])
    def config_color(self):
        self.color = (0,255,0)
    def draw(self,screen,addx,addy):
        self.rect.x = self.x + addx
        self.rect.y = self.y + addy
        pygame.draw.rect(screen,self.color,self.rect,0)
bigbg_rect_list = [bigbg_rect() for i in range(11)]

pygame.mouse.set_visible(False)
setspeed(0.8)
AImapGo((546,511))
logo_action = False
a = 255 # a可不是无意义，这是alpha(α)透明度函数的首字母，别搞错哦，可读性很高！！！

while True:                         # logo
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            eventpos = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            logo_action = True
        if event.type == pygame.KEYDOWN:
            logo_action = True
    screen.fill((0,0,0))
    screen.blit(start_logo1,(0,0))
    if logo_action == True:
        a -= 1
        start_logo1.set_alpha(a)
        if a == 0:
            break
    screen.blit(arrowc,eventpos)
    pygame.time.delay(8)
    pygame.display.flip()
    try:
        root.update()
    except:
        sys.exit()

while True:                         # logo2
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            eventpos = event.pos
    screen.fill((0,0,0))
    screen.blit(start_logo2,(0,0))
    a += 1
    start_logo2.set_alpha(a)
    if a == 255:
        break
    screen.blit(arrowc,eventpos)
    pygame.time.delay(8)
    pygame.display.flip()
    try:
        root.update()
    except:
        sys.exit()
    


while True:
    if part == '主客厅':
        button.place(x=40,y=20)
        entry.place(x=100,y=20)
    while part == '主客厅':
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                eventpos = event.pos
                if okButtonRect.collidepoint(eventpos) or goto_lang_rect.collidepoint(eventpos):
                    mouseccut = 'hand'
                else:
                    mouseccut = 'ok'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if okButtonRect.collidepoint(eventpos):
                        if t2-t1 > talk_speak[1]:
                            talk_thing = AAtalk(entry.get())
                            talk = True
                    if goto_lang_rect.collidepoint(eventpos):
                        part = '长廊'
        screen.fill((0,0,0))
        nowtime = localtime()
        nowh = nowtime[3]
        if nowh > 4 and nowh < 18:
            am_or_pm = 'am'
        else:
            am_or_pm = 'pm'
        if am_or_pm == 'am':
            show_bg(morningbg)
        else:
            show_bg(eveningbg)
        if nowh > 12:
            nowh -= 12
        nowm = nowtime[4]
        if nowm >= 10:
            nowm2 = str(nowm)
        else:
            nowm2 = '0'+str(nowm)
        nows = nowtime[5]
        if nows >= 10:
            nows2 = str(nows)
        else:
            nows2 = '0'+str(nows)
        wday = nowtime[6]
        if wday == 0:
            weekday = '星期一'
        elif wday == 1:
            weekday = '星期二'
        elif wday == 2:
            weekday = '星期三'
        elif wday == 3:
            weekday = '星期四'
        elif wday == 4:
            weekday = '星期五'
        elif wday == 5:
            weekday = '星期六'
        elif wday == 6:
            weekday = '星期日'
        pygame.draw.rect(screen,(0,0,0),electronic_clock_screen_rect,0)
        show_text(str(localtime()[0])+'-'+str(localtime()[1])+'-'+str(localtime()[2])+' '+str(localtime()[3])+':'+nowm2+':'+nows2,color=(23,255,255),pos=(700,21))
        show_text(weekday+'   ▼东八区标准时间',color=(23,255,255),pos=(700,51))
        screen.blit(okButton,okButtonRect)
        screen.blit(goto_lang,goto_lang_rect)
        screen.blit(myAI,myAIrect)
        if mouseccut == 'hand':
            screen.blit(handc,eventpos)
        else:
            screen.blit(arrowc,eventpos)
        if talk:
            AImapGo((546,511),AIhello,AIhelloRect)
            if len(talk_thing) < 32 or talk_thing == 'Hi，我是小A人工智能机器人^_^，我可以查天气，讲笑话哦~ ………………我还有很多好玩实用的功能哦~ ………………快来试试吧':
                talk_speak = speak(talk_thing)
            else:
                talk_speak = speak('一言难尽~请在聊天记录里查看~')
            t1 = time()
            pygame.mixer.Sound(talk_speak[0]).play()
            os.remove(talk_speak[0])
            talk = False
        else:
            t2 = time()
            if t2-t1 < talk_speak[-1]:
                screen.blit(talk_blank,(myAIrect.x+368,myAIrect.y+40))
                if talk_thing == 'Hi，我是小A人工智能机器人^_^，我可以查天气，讲笑话哦~ ………………我还有很多好玩实用的功能哦~ ………………快来试试吧':
                    show_text('我是小A机器人',color=(0,0,0),pos=(myAIrect.x+368,myAIrect.y+40))
                else:
                    if len(talk_thing) < 11:
                        show_text(talk_thing,color=(0,0,0),pos=(myAIrect.x+368,myAIrect.y+40))
                    else:
                        show_text('内容稍长显示不下~',color=(0,0,0),pos=(myAIrect.x+368,myAIrect.y+40))
            else:
                AImapGo((546,511))
        pygame.display.flip()
        try:
            root.update()
        except:
            sys.exit()
    
    if part == '长廊':
        button.place_forget()
        entry.place_forget()
    while part == '长廊':
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                eventpos = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if lang_door1rect.collidepoint(eventpos):
                        part = '机器人室'
                    if lang_door2rect.collidepoint(eventpos) and task1 == True:
                        part = '书房'
                    if sknow_bar_rect.collidepoint(eventpos) and task7 == True:
                        part = '奇识小市'
            if event.type == pygame.KEYDOWN:
                cilck_key_sound.play()
        screen.fill((255,255,255))
        show_bg(long_lang)
        screen.blit(long_lang_pic_lie,(623,5))
        screen.blit(lang_door1,lang_door1rect)
        if task1 == True:
            screen.blit(lang_door2,lang_door2rect)
        if task7 == True:
            screen.blit(sknow_bar,sknow_bar_rect)
        screen.blit(arrowc,eventpos)
        pygame.display.flip()
        try:
            root.update()
        except:
            sys.exit()
    
    if part == '机器人室':
        button.place(x=40,y=20)
        entry.place(x=100,y=20)
    while part == '机器人室':
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                eventpos = event.pos
                if okButtonRect.collidepoint(eventpos) or AIjiebarect.collidepoint(eventpos) or AIcalculationrect.collidepoint(eventpos) or AIread_againrect.collidepoint(eventpos) or AIagotalkrect.collidepoint(eventpos) or AIgamehelprect.collidepoint(eventpos):
                    mouseccut = 'hand'
                else:
                    mouseccut = 'ok'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if okButtonRect.collidepoint(eventpos):
                        if t2-t1 > talk_speak[1]:
                            talk_thing = AAtalk(entry.get())
                            talk = True
                    if AIjiebarect.collidepoint(eventpos):
                        jieba_cut_word(entry.get())
                    if AIcalculationrect.collidepoint(eventpos):
                        if t2-t1 > talk_speak[1]:
                            talk_thing = entry.get()
                            try:talk_thing = talk_thing.replace('（','(')
                            except:pass
                            try:talk_thing = talk_thing.replace('）',')')
                            except:pass
                            try:talk_thing = talk_thing.replace('[','(')
                            except:pass
                            try:talk_thing = talk_thing.replace(']',')')
                            except:pass
                            try:talk_thing = talk_thing.replace('{','(')
                            except:pass
                            try:talk_thing = talk_thing.replace('}',')')
                            except:pass
                            try:talk_thing = str(eval(talk_thing))
                            except:talk_thing = '无法对输入内容进行四则运算'
                            talk = True
                    if AIread_againrect.collidepoint(eventpos):
                        if t2-t1 > talk_speak[1]:
                            talk_thing = entry.get()
                            if '我' in talk_thing:
                                if talk_thing[0] == '我':
                                    talk_thing = talk_thing.replace('我','对的，你')
                                else:
                                    talk_thing = talk_thing.replace('我','你')
                            if talk_thing == '':
                                talk_thing = '无内容'
                            elif talk_thing == '叫爸爸' or talk_thing == '叫妈妈':
                                talk_thing = '我是不会中你的套路的'
                            elif talk_thing == '我是你爸爸':
                                talk_thing = '小轩才是我爸爸，而你的爸爸是我'
                            elif talk_thing == '我是你妈妈':
                                talk_thing = '别撒娇调情了我hode不住'
                            elif talk_thing == '滑稽':
                                talk_thing = '憨憨'
                            elif talk_thing == '爸爸':
                                talk_thing = '诶！'
                            elif talk_thing == '妈妈':
                                talk_thing = '你搞什么，好好说话'
                            talk = True
                    if AIagotalkrect.collidepoint(eventpos):
                        tk_ago_talk()
                    if AIgamehelprect.collidepoint(eventpos):
                        gamehelp()
                    if AI_baidurect.collidepoint(eventpos):
                        wopen('https://www.baidu.com/s?wd='+entry.get())
            if event.type == pygame.KEYDOWN:
                cilck_key_sound.play()
        screen.fill((255,255,255))
        show_bg(AIroom_bgpic)
        screen.blit(okButton,okButtonRect)
        screen.blit(myAI,myAIrect)
        screen.blit(AIjieba,AIjiebarect)
        screen.blit(AIcalculation,AIcalculationrect)
        screen.blit(AIread_again,AIread_againrect)
        screen.blit(AI_baidu,AI_baidurect)
        pygame.draw.rect(screen,(255,143,255),AIroom_interval_rect,0)
        screen.blit(AIagotalk,AIagotalkrect)
        screen.blit(AIgamehelp,AIgamehelprect)
        if mouseccut == 'hand':
            screen.blit(handc,eventpos)
        else:
            screen.blit(arrowc,eventpos)
        if talk:
            AImapGo((546,511),AIhello,AIhelloRect)
            if len(talk_thing) < 36 or talk_thing == 'Hi，我是小A人工智能机器人^_^，我可以查天气，讲笑话哦~ ………………我还有很多好玩实用的功能哦~ ………………快来试试吧':
                talk_speak = speak(talk_thing)
            else:
                talk_speak = speak('一言难尽~请在聊天记录里查看~')
            t1 = time()
            pygame.mixer.Sound(talk_speak[0]).play()
            os.remove(talk_speak[0])
            talk = False
        else:
            t2 = time()
            if t2-t1 < talk_speak[-1]:
                screen.blit(talk_blank,(myAIrect.x+368,myAIrect.y+40))
                if talk_thing == 'Hi，我是小A人工智能机器人^_^，我可以查天气，讲笑话哦~ ………………我还有很多好玩实用的功能哦~ ………………快来试试吧':
                    show_text('我是小A机器人',color=(0,0,0),pos=(myAIrect.x+368,myAIrect.y+40))
                else:
                    if len(talk_thing) < 11:
                        show_text(talk_thing,color=(0,0,0),pos=(myAIrect.x+368,myAIrect.y+40))
                    else:
                        show_text('内容稍长显示不下~',color=(0,0,0),pos=(myAIrect.x+368,myAIrect.y+40))
            else:
                AImapGo((546,511))
        pygame.display.flip()
        try:
            root.update()
        except:
            sys.exit()
    
    if part == '书房':
        button.place_forget()
        entry.place_forget()
    while part == '书房':
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                eventpos = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if study_hide_bookrect.collidepoint(eventpos):
                        study_hide_book_text()
            if event.type == pygame.KEYDOWN:
                cilck_key_sound.play()
                if event.key == ord('q') and task2 == True and task5 == False:
                    part = '书架后的密室'
                if event.key == ord('q') and task5 == True and task6 == False:
                    part = '大背景'
                if event.key == ord('w') and task2 == True:
                    top_archive()
                if event.key == ord('e') and task6 == True:
                    task7 = True
        screen.fill((255,255,255))
        show_bg(study_bgpic)
        screen.blit(study_hide_book,study_hide_bookrect)
        screen.blit(arrowc,eventpos)
        pygame.display.flip()
        try:
            root.update()
        except:
            sys.exit()
    
    if part == '书架后的密室':
        button.place_forget()
        entry.place_forget()
    while part == '书架后的密室':
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                eventpos = event.pos
                if secret_file_trianglerect_is_check_mode == True and task4_mode1 == True and secret_file_trianglerect.center != secret_file_squarerect.center:
                    secret_file_trianglerect.center = eventpos
                    if secret_file_trianglerect.collidepoint(secret_file_squarerect.center):
                        secret_file_trianglerect.center = secret_file_squarerect.center
                        task4_mode2 = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if mice_textrect.collidepoint(eventpos):
                        show_mice_text()
                    if password_lockrect.collidepoint(eventpos) and task3 == False:
                        password_lock_input()
                    if secret_file_squarerect.collidepoint(eventpos) and task4_mode3_s == True:
                        task4_mode4 = True
                    secret_file_trianglerect_is_check_mode = True
            if event.type == pygame.MOUSEBUTTONUP:
                secret_file_trianglerect_is_check_mode = False
            if event.type == pygame.KEYDOWN:
                cilck_key_sound.play()
                if event.key == 100 and task3 == True:
                    task4_mode1 = True
                if event.key == ord('n') and task4_mode2 == True:
                    task4_mode3_n = True
                if event.key == ord('u') and task4_mode3_n == True:
                    task4_mode3_u = True
                if event.key == ord('m') and task4_mode3_u == True:
                    task4_mode3_m = True
                if event.key == ord('b') and task4_mode3_m == True:
                    task4_mode3_b = True
                if event.key == ord('e') and task4_mode3_b == True:
                    task4_mode3_e = True
                if event.key == ord('r') and task4_mode3_e == True:
                    task4_mode3_r = True
                if event.key == ord('s') and task4_mode3_r == True:
                    task4_mode3_s = True
                if event.key == ord('l') and task4_mode4 == True:
                    task4 = True
                    part = '书房'
        screen.fill((255,255,255))
        show_bg(secretroom0014)
        screen.blit(mice_text,mice_textrect)
        if task3 == False:
            screen.blit(password_lock,password_lockrect)
        else:
            show_bg(secret_file_background)
        if task4_mode1 == True and task4_mode4 == False:
            screen.blit(secret_file_square,secret_file_squarerect)
            screen.blit(secret_file_triangle,secret_file_trianglerect)
        screen.blit(arrowc,eventpos)
        pygame.display.flip()
        try:
            root.update()
        except:
            sys.exit()
    
    if part == '大背景':
        button.place_forget()
        entry.place_forget()
    while part == '大背景':
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                eventpos = event.pos
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    bigbg_KEYDOWN = 1
                if event.key == pygame.K_RIGHT:
                    bigbg_KEYDOWN = 2
                if event.key == pygame.K_UP:
                    bigbg_KEYDOWN = 3
                if event.key == pygame.K_DOWN:
                    bigbg_KEYDOWN = 4
                if event.key == ord('a') and task6_mode:
                    task6 = True
                    part = '书房'
            if event.type == pygame.KEYUP:
                bigbg_KEYDOWN = False
        if bigbg_KEYDOWN == 1:
            bigbg_X += 11
        if bigbg_KEYDOWN == 2:
            bigbg_X -= 11
        if bigbg_KEYDOWN == 3:
            bigbg_Y += 11
        if bigbg_KEYDOWN == 4:
            bigbg_Y -= 11
        if bigbg_X <= -6000:
            bigbg_X = -6000
        if bigbg_X >= 1000:
            bigbg_X = 1000
        if bigbg_Y <= -3000:
            bigbg_Y = -3000
        if bigbg_Y >= 500:
            bigbg_Y = 500
        screen.fill((255,255,255))
        for i in bigbg_rect_list:
            if i.rect.collidepoint((700,450)) and i.color != (0,255,0):
                i.config_color()
                task6_mode += 1
            i.draw(screen,bigbg_X,bigbg_Y)
        show_text('上下左右箭头移动，右边、下边有11个按钮任务',color=(255,255,0),pos=(183+bigbg_X,392+bigbg_Y))
        show_bg(bigbg_lightbg)
        show_bg(bigbg_convertbg)
        show_text('位置：横向：'+str(-bigbg_X)+'，纵向：'+str(-bigbg_Y),color=(255,255,255),pos=(11,11))
        if task6_mode <= 10:
            show_text('任务达成：'+str(task6_mode)+'/11',color=(255,255,255),pos=(11,51))
        else:
            show_text('任务已完成，按下A',color=(255,0,0),pos=(11,51))
        screen.blit(bigbg_me_img,bigbg_me_imgrect)
        screen.blit(arrowc,eventpos)
        pygame.display.flip()
        try:
            root.update()
        except:
            sys.exit()
    
    if part == '奇识小市':
        button.place_forget()
        entry.place_forget()
    while part == '奇识小市':
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                eventpos = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if sknow_ask_rect.collidepoint(eventpos):
                        db = databases.database
                        xT = 0
                        for xi in range(20):
                            try:
                                question = random.randint(0,len(db)-1)
                            except:
                                print('次数用完，请重新运行')
                                game_acc_die()
                                sys.exit()
                            for i in db:
                                if list(db).index(i) == question:
                                    question = i
                            ask = input(question+'\n1.'+db[question][0]+'\n2.'+db[question][1]+'\n3.'+db[question][2]+'\n4.'+db[question][3])
                            if ask == str(db[question][4]):
                                print('答对了')
                                xT += 1
                            else:
                                print('答错了')
                            del db[question]
                        del xi
                        if xT <= 15:
                            print('你算了吧你！别想进去！')
                        else:
                            print('欢迎你，智者！')
                            task8 = True
                        del xT
        screen.fill((255,255,255))
        if task8 == False:
            show_bg(sknow_door_bg)
            screen.blit(sknow_ask,sknow_ask_rect)
        screen.blit(arrowc,eventpos)
        pygame.display.flip()
        try:
            root.update()
        except:
            sys.exit()