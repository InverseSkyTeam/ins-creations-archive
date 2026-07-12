#填写第80行代码
#填写第81行代码
#填写第92行代码
#填写第97行代码
from pgzrun import *
name = input("给本哈士奇起个名儿：")
#{
sounds.bgm.play(-1)

WIDTH = 405
HEIGHT = 720

dog = Actor("待机0.png", [200, 360])
bg = Actor("背景.png")
nose = Actor("鼻子区域.png", [200, 280])
belly= Actor("肚子区域.png", [200, 420])
house = Actor("房子区域.png", [370, 350])
foot = Actor("脚部区域.png", [210, 540])

num = 0
def draw():
    bg.draw()
    dog.draw()
    screen.draw.text("点击不同地方,惊喜等着你!", center=[200, 50], fontsize = 20, color = "black",fontname = "ziti.ttf")
    screen.draw.text("可点区域：鼻子、肚子、脚丫、房子", center=[200, 80], fontsize = 20, color = "black",fontname = "ziti.ttf")
    screen.draw.text("俺叫" + name, center=[200, 120], fontsize = 50, color = "black",fontname = "ziti.ttf")
def wait():
    global num
    dog.image = "待机" + str(num) + ".png"
    num = num + 1
    if num > 134:
        num = 0
clock.schedule_interval(wait,0.03)

#创建点鼻子的函数
def touch_nose():
    global num
    dog.image = "点鼻子" + str(num) + ".png"
    num = num + 1
    if num > 99:
        num = 0
        clock.unschedule(touch_nose)
        clock.schedule_interval(wait,0.03)
#创建点肚子的函数
def touch_belly():
    global num
    dog.image = "点肚子" + str(num) + ".png"
    num = num + 1
    if num > 99:
        num = 0
        clock.unschedule(touch_belly)
        clock.schedule_interval(wait,0.03)
#}

#创建点脚的函数
def touch_foot():
    global num
    dog.image = "点脚" + str(num) + ".png"
    num = num + 1
    if num > 99:
        num = 0
        clock.unschedule(touch_foot)
        clock.schedule_interval(wait,0.03)

#创建点房子的函数
def touch_house():
    global num
    dog.image = "点房子" + str(num) + ".png"
    num = num + 1
    if num > 133:
        num = 0
        clock.unschedule(touch_house)
        clock.schedule_interval(wait,0.03)

def on_mouse_down(pos):
    clock.unschedule(wait)
    clock.unschedule(touch_nose)
    clock.unschedule(touch_belly)
    #作答区域:填写下两行,取消点脚和点房子的动作,点脚的函数是touch_foot,点房子的函数是touch_house
    clock.unschedule(touch_foot)
    clock.unschedule(touch_house)
    global num
    if nose.collidepoint(pos):
        num = 0
        clock.schedule_interval(touch_nose, 0.03)
        music.play_once("点鼻子.mp3")
    elif belly.collidepoint(pos):
        num = 0
        clock.schedule_interval(touch_belly, 0.03)
        music.play_once("点肚子.mp3")
    #作答区域:填写下一行,完成foot角色和鼠标的碰撞检测
    elif foot.collidepoint(pos):
        num = 0
        clock.schedule_interval(touch_foot, 0.03)
        music.play_once("点脚.mp3")
    #作答区域:填写下一行,完成house角色和鼠标的碰撞检测
    elif house.collidepoint(pos):
        num = 0
        clock.schedule_interval(touch_house, 0.03)
        music.play_once("点房子.mp3")
    else:
        clock.schedule_interval(wait,0.03)
        
go()
#神秘代码:下面的链接是课上布偶猫的程序
#----->https://code.xueersi.com/live/creator/1?template_project_id=24529618&work_type=xes_classwork&needShare=false&assets_diff=71f18e468631999c3527afe3ff600896