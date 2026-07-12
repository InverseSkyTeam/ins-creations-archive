#随堂练习
from pgzrun import *
sounds.bgm.play(-1)

HEIGHT = 600
WIDTH = 1000

bg = Actor("bg.png")
over = Actor("结束页.png")
ninja = Actor("女忍者.png", [500,480])
trunk = Actor("trunk.png", [515,150])
again = Actor("again.png", [500,400])

speed = 2
fly = []
fixed = []
state = "run"

def draw(): 
    if state == "run":
        bg.draw()
        trunk.draw()
        for f in fly:
            f.draw()
        for d in fixed:
            d.draw()
        ninja.draw()
    if state == "end":
        over.draw()
        again.draw()
        screen.draw.text(str(len(fixed)), (500, 235),
                         fontsize=80, color='gold')


def update():
    global state
    for f in fly:
        f.y = f.y - 5
        #任务1作答区域 collidelist()
        if f.collidelist(fixed) >= 0:
            state = "end"
            fly.remove(f)
            sounds.bgm.stop()
        if f.colliderect(trunk):
            f.top = trunk.bottom
            #任务2作答区域 
            fixed.append(f)
            fly.remove(f)
        if f.bottom < 0:
            fly.remove(f)        

    # 忍者在屏幕内左右移动
    #{
    global speed
    ninja.x = ninja.x - speed
    if ninja.left < 0:
        speed = -speed
    if ninja.right > WIDTH:
        speed = -speed
    #}

def on_key_down():
    if keyboard.space == True:
        if state == "run":
            dart = Actor("dart.png")
            dart.x = ninja.x + 30
            dart.y = ninja.y - 115
            fly.append(dart)
            sounds.shoot.play()

#{
#重玩
def on_mouse_down(pos):
    global state,fly,fixed,score
    if again.collidepoint(pos):
        state = "run"
        fly = [] 
        fixed = []
        score = 0 
        sounds.bgm.play(-1)
#}
go()

