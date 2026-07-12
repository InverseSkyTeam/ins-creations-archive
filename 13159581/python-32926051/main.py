#随堂练
from pgzrun import *

WIDTH = 1400
HEIGHT = 700
sounds.bg.play(-1)

bomb = Actor("bomb.png", [100, 625])
bg = Actor("bg.png")

dragon = Actor("dragon.png", [1350, 300])
lose = Actor("lose.png", [1500, 1500])
win = Actor("win.png", [1500, 1500])

#{
p_list = [[550, 575],[750, 175],[600, 325],[1100, 525]]    
barriers = []
for i in range(4):
    img = 'barrier' + str(0) +'.png'
    b = Actor(img, p_list[i])
    barriers.append(b)

position = [
    #第一排
    [150, 75],
    [200, 75],
    [250, 75],
    [300, 75],
    [350, 75],
    [400, 75],
    [450, 75],
    [500, 75],
    [550, 75],
    [600, 75],
    [650, 75],
    [700, 75],
    [750, 75],
    [800, 75],
    [850, 75],
    [900, 75],
    [950, 75],
    [1000, 75],
    [1050, 75],
    [1100, 75],
    [1150, 75],
    [1200, 75],
    #第二排
    [150, 125],
    [750, 125],
    [1200, 125],
    #第三排
    [150, 175],
    [300, 175],
    [350, 175],
    [400, 175],
    [450, 175],
    [500, 175],
    [550, 175],
    [600, 175],
    [650, 175],
    [850, 175],
    [900, 175],
    [950, 175],
    [1000, 175],
    [1050, 175],
    [1200, 175],
    #第四排
    [150, 225],
    [250, 225],
    [500, 225],
    [650, 225],
    [800, 225],
    [1050, 225],
    [1150, 225],
    [1200, 225],
    #第五排
    [150, 275],
    [250, 275],
    [650, 275],
    [800, 275],
    [900, 275],
    [1000, 275],
    [1050, 275],
    #第六排
    [150, 325],
    [250, 325],
    [350, 325],
    [400, 325],
    [450, 325],
    [500, 325],
    [550, 325],
    [650, 325],
    [750, 325],
    [800, 325],
    [900, 325],
    [1000, 325],
    [1050, 325],
    [1100, 325],
    [1150, 325],
    [1200, 325],
    #第七排
    [150, 375],
    [250, 375],
    [500, 375],
    [700, 375],
    [900, 375],
    [1100, 375],
    [1200, 375],
    #第八排
    [150, 425],
    [250, 425],
    [500, 425],
    [800, 425],
    [900, 425],
    [1100, 425],
    #第九排
    [150, 475],
    [250, 475],
    [350, 475],
    [400, 475],
    [450, 475],
    [500, 475],
    [550, 475],
    [600, 475],
    [650, 475],
    [700, 475],
    [750, 475],
    [800, 475],
    [900, 475],
    [1000, 475],
    [1050, 475],
    [1100, 475],
    [1200, 475],
    #第十排
    [150, 525],
    [550, 525],
    [900, 525],
    [1200, 525],
    #第十一排
    [150, 575],
    [200, 575],
    [250, 575],
    [300, 575],
    [350, 575],
    [400, 575],
    [650, 575],
    [700, 575],
    [750, 575],
    [800, 575],
    [850, 575],
    [900, 575],
    [950, 575],
    [1000, 575],
    [1050, 575],
    [1100, 575],
    [1200, 575],
    #第十二排
    [550, 625],
    [1200, 625],
    #第十三排
    [150, 675],
    [200, 675],
    [250, 675],
    [300, 675],
    [350, 675],
    [400, 675],
    [450, 675],
    [500, 675],
    [550, 675],
    [600, 675],
    [650, 675],
    [700, 675],
    [750, 675],
    [800, 675],
    [850, 675],
    [900, 675],
    [950, 675],
    [1000, 675],
    [1050, 675],
    [1100, 675],
    [1150, 675],
    [1200, 675],
]
#}
fires = []
for pos in position:
    s = Actor("fire.png", pos)
    fires.append(s)

time1 = 0
state = 0

def draw():
    bg.draw()
    dragon.draw()
    for s in fires:
        s.draw()
    for b in barriers:
        b.draw()
    bomb.draw()
    lose.draw()
    win.draw()
    if state == 1:
        screen.draw.text("time: " + str(time1), (600, 50), fontsize=80)

def on_key_down():
    global state
    music.play_once("walk.mp3")
    if keyboard.right == True:
        bomb.x = bomb.x + 50
    if keyboard.left == True:
        bomb.x = bomb.x - 50
    if keyboard.up == True:
        bomb.y = bomb.y - 50
    if keyboard.down == True:
        bomb.y = bomb.y + 50

    if bomb.collidelist(fires) >= 0:
        lose.pos = [700, 350]
        music.play_once("fail.mp3")
        sounds.bg.stop()

    if bomb.colliderect(dragon):
        win.pos = [700, 350]
        music.play_once("win.mp3")
        sounds.bg.stop()
        state = 1
        clock.unschedule(count)
    #作答区域 bomb和障碍物列表barriers的碰撞检测
    #作答区域 一对多的碰撞检测使用collidelist()
    if bomb.collidelist(barriers) >= 0:
        music.play_once("zizi.mp3")
        bomb.pos = [100, 625]
        





#{
def barriers_show():
    for i in range(4):
        barriers[i].pos = p_list[i]
    clock.schedule_unique(barriers_hide, 1)
    
    
def barriers_hide():
    for b in barriers:
        b.pos = [700, 1050]
    clock.schedule_unique(barriers_show, 1)

clock.schedule_unique(barriers_show, 0.2)
#}
#{
def count():
    global time1
    time1 += 1
    clock.schedule_unique(count, 1)  

count()
#}
go()