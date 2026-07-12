# -*- coding:utf-8 -*-

import tkinter,pygame,webbrowser as w
from time import *
pygame.init()
bgMusic = pygame.mixer.music.load('BGM.mp3')
pygame.mixer.music.play(-1)
Side_length_range = 4
fill2_many = 2
walk = 0
srart_root = tkinter.Tk()
srart_root.geometry('300x200')
def root_main():
    global entry,entry2,label,Side_length_range,fill2_many
    Side_length_range = entry.get()
    fill2_many = entry2.get()
    try:
        Side_length_range=int(Side_length_range)
        if Side_length_range >= 3 and Side_length_range <= 6:
            pass
        else:
            label['text'] = '请输入3~6的整数！'
    except:
        label['text'] = '请输入阿拉伯数字！'
    else:
        try:
            fill2_many=int(fill2_many)
            if fill2_many <= Side_length_range**2:
                label['text'] = '输入成功，请关闭窗口！'
            else:
                label['text'] = '输入的整数要小于格数的平方！'
        except:
            label['text'] = '请输入阿拉伯数字！'
    finally:
        pass
def SpaceOffice():
    w.open('https://code.xueersi.com/home/project/detail?lang=code&pid=8525531&version=offline&form=python&langType=python')
label = tkinter.Label(srart_root,text='请在第一条输入框里输入此游戏的宽度，最大为6。\n最小为3，单位为格子，输入3，边长就是3格。\n第二条输入框输入刚开始出现几个"2"模块\n直接关掉窗口则选择默认！')
label.pack()
entry = tkinter.Entry(srart_root,font=('微软雅黑',15),bd = 3)
entry.pack()
entry2 = tkinter.Entry(srart_root,font=('微软雅黑',15),bd = 3)
entry2.pack()
button = tkinter.Button(srart_root,text='设置完毕，开始游戏！',command=root_main)
button.pack()
button2 = tkinter.Button(srart_root,text='宇宙工作室招人告示',command=SpaceOffice)
button2.pack()
srart_root.mainloop()
del tkinter


import random
import math

__mataclass__ = type
class map2048():       # 此类为2048地图模块封装的类
    def reset(self):
        global fill2_many
        self.fill2_many = fill2_many
        self.__row = Side_length_range  # 行数
        self.__col = Side_length_range  # 列数
        self.data = [
            [0 for x in range(self.__col)]
            for y in range(self.__row)
        ]
        for i in range(self.fill2_many):self.fill2()
    def __init__(self):
        self.reset()
    def get_space_count(self):
        count = 0
        for r in self.data:
            count += r.count(0)
        return count
    def get_score(self):
        s = 0
        for r in self.data:
            for c in r:
                s += 0 if c < Side_length_range else c * int((math.log(c, 2) - 1.0))
        return s
    def fill2(self):
        blank_count = self.get_space_count()
        if 0 == blank_count:
            return False
        pos = random.randrange(0, blank_count)
        offset = 0
        for r in self.data:
            for ci in range(self.__col):
                if 0 == r[ci]:
                    if offset == pos:
                        r[ci] = 2
                        return True
                    offset += 1
    def fill4(self):
        blank_count = self.get_space_count()
        if 0 == blank_count:
            return False
        pos = random.randrange(0, blank_count)
        offset = 0
        for r in self.data:
            for ci in range(self.__col):
                if 0 == r[ci]:
                    if offset == pos:
                        r[ci] = 4
                        return True
                    offset += 1
    def more_fill(self):
        blank_count = self.get_space_count()
        if 0 == blank_count:
            return False
        pos = random.randrange(0, blank_count)
        offset = 0
        for r in self.data:
            for ci in range(self.__col):
                if 0 == r[ci]:
                    if offset == pos:
                        r[ci] = random.choice([8,8,8,8,16,16,32,32,64,128])
                        return True
                    offset += 1
    # 判断游戏是否结束
    def is_gameover(self):
        for r in self.data:
            # 如果水平方向还有0,则游戏没有结束
            if r.count(0):
                return False
            # 水平方向如果有两个相邻的元素相同，则没有游戏结束
            for i in range(self.__col - 1):
                if r[i] == r[i + 1]:
                    return False
        for c in range(self.__col - 1):
            # 竖直方向如果有两个相邻的元素相同，则没有游戏结束
            for r in range(self.__row - 1):
                if self.data[r][c] == self.data[r + 1][c]:
                    return False
        # 以上都没有，则游戏结束
        return True
 
    # 2048游戏的左移动
    def left(self):
        # moveflag 是否成功移动数字标志位,如果有移动则为真值,原地图不变则为假值
        moveflag = False
        # 将所有数字向左移动来填补左侧空格
        for times in range(self.__col - 1):
            for r in self.data:
                for c in range(self.__col - 1):
                    if 0 == r[c]:
                        moveflag = True
                        r[c] = r[c + 1]
                        r[c + 1] = 0
        # 判断是否发生碰幢，如果有碰撞则合并,合并结果靠左，右则填充空格
        for r in self.data:
            for c in range(self.__col - 1):
                if r[c] == r[c + 1]:
                    moveflag = True
                    r[c] *= 2
                    r[c + 1] = 0
        # 再将所有数字向左移动来填补左侧空格
        for times in range(self.__col - 1):
            for r in self.data:
                for c in range(self.__col - 1):
                    if 0 == r[c]:
                        moveflag = True
                        r[c] = r[c + 1]
                        r[c + 1] = 0
        return moveflag
    # 游戏右移操作,和左移相反
    def right(self):
        for r in self.data:
            r.reverse()
        moveflag = self.left()
        for r in self.data:
            r.reverse()
        return moveflag
    # 游戏上移操作
    def up(self):
        moveflag = False
        for times in range(self.__row - 1):
            for c in range(self.__col):
                for r in range(self.__row - 1):
                    if 0 == self.data[r][c]:
                        moveflag = True
                        self.data[r][c] = self.data[r + 1][c]
                        self.data[r + 1][c] = 0
        for c in range(self.__col):
            for r in range(self.__row - 1):
                if self.data[r][c] == self.data[r + 1][c]:
                    moveflag = True
                    self.data[r][c] *= 2
                    self.data[r + 1][c] = 0
        for times in range(self.__row - 1):
            for c in range(self.__col):
                for r in range(self.__row - 1):
                    if 0 == self.data[r][c]:
                        moveflag = True
                        self.data[r][c] = self.data[r + 1][c]
                        self.data[r + 1][c] = 0
        return moveflag
    # 游戏下移操作，和上移相反
    def down(self):
        self.data.reverse()
        moveflag = self.up()
        self.data.reverse()
        return moveflag

import sys
if (sys.version_info > (3, 0)):
    from tkinter import *
    from tkinter import messagebox
else:
    from Tkinter import *

game = map2048()

# 刷新界面函数,更改各个Label的各个设置
def update_ui():
    global walk
    for r in range(len(game.data)):
        for c in range(len(game.data[0])):
            number = game.data[r][c]
            label = map_labels[r][c]
            label['text'] = str(number) if number else ''
            label['bg'] = mapcolor[number][0]
            label['foreground'] = mapcolor[number][1]
    label_score['text'] = str(game.get_score())
    label_walk['text'] = str(walk)+'步'
def reset_game():
    global walk
    walk = 0
    game.reset()
    update_ui()
keymap = {
    'a': game.left,
    'd': game.right,
    'w': game.up,
    's': game.down,
    'r': reset_game,
    'Left': game.left,
    'Right': game.right,
    'Up': game.up,
    'Down': game.down
}
game_bg_color = "#bbada0"
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
    16384: ("green", "red")
}
map_labels = []
def on_key_down(event):
    global walk
    walk += 1
    keysym = event.keysym
    if keysym in keymap:
        if keymap[keysym]():
            a = random.randint(1,100)
            if a <= 70:
                game.fill2()
            elif a <= 95:
                game.fill4()
            else:
                game.more_fill()
    update_ui()
    if game.is_gameover():
        mb = messagebox.askyesno(title='gameover', message='游戏结束!\n你得了'+str(game.get_score())+'分，走了'+str(walk)+'步\n是否结束游戏?')
        if mb:
            exit()
        else:
            walk = 0
            game.reset()
            update_ui()



# 以下为2048的界面
root = Tk()
root.title('2048py')
root.geometry(str(600+(Side_length_range-4)*100)+'x'+str(440+(Side_length_range-4)*100))
frame = Frame(root, width=300, height=300, bg=game_bg_color)
frame.grid(sticky=N+E+W+S)
frame.focus_set()
frame.bind("<Key>", on_key_down)

# 初始化图形界面
for r in range(len(game.data)):
    row = []
    for c in range(len(game.data[0])):
        value = game.data[r][c]
        text = '' if 0 == value else str(value)
        label = Label(frame, text=text, width=4, height=2,font=("黑体", 30, "bold"))
        label.grid(row=r, column=c, padx=5, pady=5, sticky=N+E+W+S)
        row.append(label)
    map_labels.append(row)
bottom_row = len(game.data)
print("wasd,上下左右键操控")
label = Label(frame, text='分数', font=("黑体", 30, "bold"),bg="#bbada0", fg="#eee4da")
label.grid(row=bottom_row, column=0, padx=5, pady=5)
label_score = Label(frame, text='0', font=("黑体", 30, "bold"),bg="#bbada0", fg="#ffffff")
label_score.place(x=100,y=Side_length_range*100-10)
label_walk = Label(root, text='0步', font=("黑体", 30), fg="blue")
label_walk.place(x=420+(Side_length_range-4)*100,y=5)
restart_button = Button(frame, text='重新开始', font=("黑体", 16, "bold"),bg="blue", fg="orange", command=reset_game)
restart_button.grid(row=bottom_row, column=Side_length_range-1, padx=5, pady=5)
update_ui()
root.mainloop()