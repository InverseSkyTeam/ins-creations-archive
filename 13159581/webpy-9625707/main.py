#┌──────────────────────?──────────────────────────────┐
#│            使用秘籍，控制游戏难度                   │
#│          ???秘籍参考在左侧                          │
#└─────────────────────────────────────────────────────┘
from invadera import *
move()
theme_c()
bg_skin("bg3.png")
enemy_skin("enemy.png")
player_skin("player.png")
base_skin("base.png")
bullet_color(0,204,0)
e_bullet_color(0,204,0)
life_skin("life.png")
print("请选择难度：")
print("a.cjy b.普通 c.噩梦 d.松果老师 e.小爱老师")

t = input("请选择：")

#补全if条件判断语句，实现不同难度选择。
if t == "a":
    ans = input("请输入暗号:")
    print("cjy模式已开启")
    if ans == "135790":
        player_skin("1.jpg")
        bullet_rate(250)  #修改玩家子弹数量
        e_bullet_rate(5) #修改敌机子弹数量
        player_life(100)  #修改生命值
    if ans != "135790":
        print("暗号错误")
if t == "b":
    print("普通模式已开启")
    bullet_rate(10)  #修改玩家子弹数量
    e_bullet_rate(10)#修改敌机子弹数量    
    player_life(3)   #修改生命值
    
if t == "c":
    print("噩梦难度已开启")
    bullet_rate(1)   #修改玩家子弹数量
    e_bullet_rate(20)#修改敌机子弹数量   
    player_life(1)   #修改生命值
if t == "d":
    print("松果老师模式已开启")
    enemy_skin("3.jpg")
    bullet_rate(5633645376543764537)   #修改玩家子弹数量
    e_bullet_rate(3563465243)#修改敌机子弹数量   
    player_life(10) #修改生命值
if t == "e":
    print("小爱老师模式已开启")
    enemy_skin("player1.png")
    bullet_rate(5633645376543764537)   #修改玩家子弹数量
    e_bullet_rate(3563465243)#修改敌机子弹数量   
    player_life(10) #修改生命值
play()