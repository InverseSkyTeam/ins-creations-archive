#随堂练习
from pgzrun import *
from random import *
sounds.bg.play(-1)

WIDTH = 350
HEIGHT = 700

bg1 = Actor("bg1.png")
over = Actor("bg3.png")
kd = Actor("keduo1.png",[180,270])
#任务1 作答区域
bg2 = Actor("bg2.png")
bg2.top = HEIGHT


#创建小鸟
bird = []
def create_bird():
    b = Actor("bird1.png")
    b.x = -150
    b.y = randint(20, 680)
    bird.append(b)
clock.schedule_interval(create_bird, 2)

state = "begin"

def draw():
    if state == "begin":
        bg1.draw()
        bg2.draw()
        for b in bird:
            b.draw()
        kd.draw()
    if state == "end":
        over.draw()
        screen.draw.text(str(time1), (185, 180), fontsize=55, color="gold")

#背景移动    
def move_bg():
    bg1.y = bg1.y - 10
    bg2.y = bg2.y - 10
    #任务2 作答区域
    if bg1.bottom < 0:
        bg1.top = HEIGHT
    if bg2.bottom < 0:
        bg2.top = HEIGHT


#小鸟移动
def move_bird():
    for b in bird:
        b.x = b.x + 2
        if b.left > WIDTH:
            bird.remove(b)
#可多移动
def move_kd():
    if keyboard.left == True:
        if kd.left > 0:
            kd.x = kd.x - 5
    if keyboard.right == True:
        if kd.right < WIDTH:
            kd.x = kd.x + 5
    if keyboard.up == True:
        if kd.top > 0:
            kd.y = kd.y - 5
    if keyboard.down == True:
        if kd.bottom < HEIGHT:
            kd.y = kd.y + 5

def update():
    global state
    if state == "begin":
        move_bg()
        move_bird()
        move_kd()
        
        #小鸟和可多碰撞检测
        index = kd.collidelist(bird)
        if index >= 0:
            music.play_once("hit.mp3")
            sounds.bg.stop()
            bird.pop(index)
            state = "end"

#{
def show1():
    if state == "begin":
        kd.image = "keduo2"
        for b in bird:
            b.image = "bird2"
        clock.schedule_unique(show2, 0.3)
    
    
def show2():
    if state == "begin":
        kd.image = "keduo1"
        for b in bird:
            b.image = "bird1"
        clock.schedule_unique(show1, 0.3)

clock.schedule_unique(show1, 0.2)
#}
#{
time1 = 0
def count():
    global time1
    if state == "begin":
        time1 += 1
        clock.schedule_unique(count, 1)  

count()
#}


go()