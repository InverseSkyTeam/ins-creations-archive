from pgzrun import *
from random import *
#{
music.play("bg.mp3")

WIDTH = 360
HEIGHT = 642

bg0 = Actor("bg0.png")
bg1 = Actor("bg1.png")
bg2 = Actor("bg2.png")
bg2.bottom = 0

plane = Actor("plane.png", [180, 570])
life_show = Actor("life.png", [300, 38])
score_show = Actor("score.png", [60, 38])
again = Actor("again.png",[180,375])
over = Actor("over.png")
boss = Actor("boss.png", [1000, 1000])
lucky = Actor("lucky.png",[1000, 1000])
#}
#任务1
me = Actor("me.png")

score = 0
life = 3

num = 0 #计数：子弹击中大boss的次数
kind = "1" #子弹类型

#{
#创建子弹
bullet = []
def create_bullet():
    b = Actor("bullet"+kind+".png")
    b.x = plane.x
    b.y = plane.y
    bullet.append(b)
clock.schedule_interval(create_bullet, 0.2)

#创建菜鸟
bird = []
def create_bird():
    b = Actor("bird.png")
    b.x = randint(20,330)
    b.y = randint(-100, -50)
    bird.append(b)
clock.schedule_interval(create_bird, 0.5)

#按空格键切换游戏状态为运行状态
state = "ready"
def on_key_down():
    global state
    if keyboard.space == True:
        state = "run"
        
def draw():
    global state
    
    #开始状态则绘制bg0
    if state == "ready":
        bg0.draw()
            
    #如果是运行状态，则绘制相关角色
    if state == "run":
        bg1.draw()
        bg2.draw()
            
        for b in bullet:
            b.draw()
        plane.draw()
        me.draw()   
        for a in bird:
            a.draw()
           
        life_show.draw()
        score_show.draw()
        
        boss.draw()
        lucky.draw()
                
        screen.draw.text(
            str(score), 
            fontsize=30, 
            center=[75, 38]
            )
        screen.draw.text(
            str(life), 
            fontsize=30, 
            center=[315, 38]
            )

    #如果是结束状态，则绘制结束页、重玩按钮、最终分数，结束音乐播放
    if state == "over":
        over.draw()
        again.draw()
        screen.draw.text(
            str(score), 
            fontsize=80, 
            center=[178, 310], 
            color=(138, 43, 226)
            )
        music.stop()

#背景滚动    
def move_bg():
    bg1.y = bg1.y + 10
    bg2.y = bg2.y + 10
    if bg1.top > HEIGHT:
        bg1.bottom = 0
    if bg2.top > HEIGHT:
        bg2.bottom = 0

#子弹移动
def move_bullet():
    global score, num, kind
    
    for b in bullet:
        b.y = b.y - 2
           
        #子弹击中boss后，计数，移除子弹  
        if b.colliderect(boss):
            num = num + 1
            bullet.remove(b)
            break
        
        for a in bird:
            #如果菜鸟和子弹相碰，则分别移除菜鸟和子弹，加分
            if b.colliderect(a):
                bird.remove(a)
                if b in bullet:
                    bullet.remove(b)
                score = score + 1
                sounds.hit.play()

        """
        如果子弹移出屏幕，则移除子弹，注意有可能子弹刚移出屏幕时
        和菜鸟碰撞，这时第123行已经将子弹移除，此时若再移除一遍
        则会报错，因此需要判断b是否在bullet中，即b是否已被移除
        """
        if b.bottom < 0:
            if b in bullet:
                bullet.remove(b)
    #}            
    #每得50分boss和幸运箱就出现一次 
    #任务2
    if score%50 == 0 and score > 0:
        boss.pos = [160,180]
        lucky.pos = [randint(24,330), -200]
    
    #子弹每击中boss 50下就加100分，boss消失，num归零下次重新计数，子弹复原
    if num == 50:
        score = score + 100
        boss.pos = [1000,1000]
        num = 0
        kind = "1"
        
#菜鸟移动            
def move_bird():
    global life, state
    for a in bird:
        a.y = a.y + 1
        #如果菜鸟碰到战机，则将菜鸟移除，同时战机损失一条生命
        if a.colliderect(plane):
            bird.remove(a)
            life = life - 1
            if life == 0:
                state = "over"
                
        #如果菜鸟移出屏幕，则移除菜鸟        
        if a.top > HEIGHT:
            bird.remove(a)

#幸运补给箱移动           
def move_lucky():
    global kind
    lucky.y = lucky.y + 5
    if lucky.top > HEIGHT:
        lucky.pos = [1000, 1000]
    if lucky.colliderect(plane):
        kind = "4"
        lucky.pos = [1000, 1000]
        sounds.lucky.play()

#角色自动连续移动、按键控制连续移动        
def update():
    #在运行状态下才移动背景、菜鸟、子弹、战机等
    if state == "run":
        move_bg()
        move_bullet()
        move_bird()
        move_lucky()
        me.pos = plane.pos
        if keyboard.left == True:
            if plane.left > 0:
                plane.x = plane.x - 2
        if keyboard.right == True:
            if plane.right < WIDTH:
                plane.x = plane.x + 2

#一键重玩（拓展、不讲）
def on_mouse_down(pos):
    global state, life, score, bullet, bird, num, kind
    if again.collidepoint(pos):
        state = "ready"
        life = 3
        score = 0
        bullet = []
        bird = []
        kind = "1"
        num = 0
        music.play("bg.mp3")
        
go()