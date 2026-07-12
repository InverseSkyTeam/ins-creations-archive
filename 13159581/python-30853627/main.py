#随堂练习,填写第17,19,20行代码,填写第32行代码
from random import *
from pgzrun import *
music.play("bgm.mp3")
WIDTH = 900
HEIGHT = 756

bg = Actor("bg.png")
start = Actor("start.png",[319,585])
end = Actor("end.png",[573,585])

#作答区域创意区:可以修改抽奖列表里的内容
lucklist = ["0","10","50", "100"]

winner = ''
#作答区域:定义luck()函数
def luck():
    #作答区域:填写下两行代码,用global声明变量winner,并用choice(列表)方法选取元素并赋值给winner
    global winner
    winner = choice(lucklist)
    sounds.start.play()

def draw():
    bg.draw()
    screen.draw.text(winner, fontname='ziti.ttf', fontsize=80, center=(445, 445), color = "black")
    #作答区域创意区:可以修改抽奖的标题
    screen.draw.text("爸爸明天给我的零花钱", fontname='ziti.ttf', fontsize=40, center=(445, 313), color= "gold")

def on_mouse_down(pos):
    global winner
    #作答区域:填写角色start和鼠标的碰撞检测
    if start.collidepoint(pos):
        clock.schedule_interval(luck,0.1)
        bg.image = "bg.png"
        
    elif end.collidepoint(pos):
        clock.unschedule(luck)
        winner = "100"
        bg.image = "win.png"
        sounds.win.play()


go()