#补充第26行代码，实现“机械”+“爆钻”组合的彩蛋吧！
#[小提示1]使用录音功能，为彩蛋配上特色语音！
#[小提示2]使用“埋彩蛋秘籍”，丰富你的彩蛋效果吧！
from run import *
from random import *
print("欢迎来到未来星球第999届酷跑比赛！")
print("比赛场地包括【森林】、【花丛】、【餐桌】、【机械】。")
x = input("请选择：")
place(x)
print("比赛选手包括【可多】、【兰朵】、【卡普】、【爆钻】。")
y = input("请选择：")
hero(y)

if x == "森林" and y == "可多":
    hero_voice("可多.mp3")
    hero_life(6)
    hero_high(5)
    hero_size(2)
if x == "森林":
    place_enemy("enemy-森林.png")
    place_music("森林.mp3")
if x == "花丛" and y == "兰朵":
    hero_voice("兰朵.mp3")
    hero_life(5)
    hero_high(7)
    hero_size(3)
if x == "花丛":
    place_enemy("enemy-花丛.png")
    place_music("花丛.mp3")
if x == "餐桌" and y == "卡普":
    hero_voice("卡普.mp3")
    hero_life(4)
    hero_high(2)
    hero_size(3)
if x == "餐桌":
    place_enemy("enemy-餐桌.png")
    place_music("餐桌.mp3")
if x == "机械" and y == "爆钻":
    hero_voice("爆钻.mp3")
    hero_life(9)
    hero_high(3)
    hero_size(2)
if x == "机械":
    place_enemy("enemy-机械.png")
    place_music("机械.mp3")
#设置金币频率
place_gold(2)

#修改背景音乐

#设置障碍物样式

#设定获胜金币数
score(randint(10,15))

#设定游戏时长
time(randint(60,100))

play()