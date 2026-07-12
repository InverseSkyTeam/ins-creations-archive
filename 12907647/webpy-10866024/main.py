from random import *
from superball import *
from time import *

# ————————挑战一 超级英雄——————————————————
# 修改球球的图片，移动速度，初始大小，长大的速度grow
# ——————————————————————————————————————————
# 修改球球的图片
h = "wangmin.png"  
# 修改球球的移动速度
hspeed = 10  
# 修改球球的大小
hscale = 50  
# 修改球球长大的速度
grow = 5  



# ————————挑战二 克敌制胜——————————————————
# 修改敌人出现的频率ef，移动的速度，初始大小
# ——————————————————————————————————————————
# 修改ef, 可以修改敌人的出现频率 
ef = 30

def random_speed():
    # 修改speedx的值, 可以修改敌人的横向移动速度
    speedx = randint(-2, 2) 
    # 修改speedy的值, 可以修改敌人的横向移动速度
    speedy = randint(-2, 2)  
    return speedx, speedy

def random_scale():
    # 修改scale的值, 可以修改敌人的大小
    scale = randint(20, 250) 
    return scale



# ————————挑战三 释放“大招”——————————————
# 游戏有三个大招, 清屏炸弹, 增加时间，巨人蘑菇
# 修改大招出现的频率和大招的效果
# ——————————————————————————————————————————
# 修改sf，控制大招出现的频率
sf = 300
# 修改add_time, 控制吃掉时间武器时增加的时长
add_time = 10  
# 修改add_scale, 控制吃掉巨人蘑菇后长大的尺寸（负数减小）
add_scale = 30  



# ————————挑战四 化身“得分王”——————————————
# 修改每次得分的数量
# ——————————————————————————————————————————
# 修改sp，控制每次得分的数量
sp = 10  



# ————————挑战五 精益求精——————————————————
# 控制背景图片bgimg
# 背景音乐的选择bgm
# ——————————————————————————————————————————
# 修改背景图片
bgimg = "bg1.png"  
# 修改背景音乐文件
bgm = "bgm2.wav"  










while True:
    start(h, hspeed, hscale, grow, ef, random_speed, random_scale, sf, sp, bgimg, bgm, add_time, add_scale)
    sleep(1.5)