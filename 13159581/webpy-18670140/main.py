#补充第17、29行代码，完善泡泡大作战程序吧
#小提示:根据你的喜好设置其他内容
#比如录制提示音、把自己的照片作为机器人等
from bubble import *

bubble_size(5,120) #设置泡泡大小范围(≥5)
set_bgm("bgm3.mp3") #设置背景音乐
player_pic("robot1.png")
size = 50
player_size(size)

while True:
    eat = eat_what()
    if eat == "small":
        voice_tip("eat.mp3") #设置提示音
        #(1)让机器人吃到小泡泡后大小增加10
        size = size + 10
        player_size(size)
        
    if eat == "big":
        voice_tip("fail.mp3")
        game_fail()
        break
    
    if size >= 150:
        voice_tip("win.mp3")
        game_win()
        #(2)游戏胜利后终止while True无限循环
        break
    
    if eat == "red":
        voice_tip("eat.mp3") #设置提示音
        size = size + 50
        player_size(size)

    if eat == "white":
        voice_tip("eat.mp3") #设置提示音
        all_clear() #清屏
        
    play()