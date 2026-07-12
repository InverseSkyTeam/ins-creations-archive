from game import *

life = 5
score = 0
#作答区域，请补充第7行代码，设计满足游戏运行的分数和生命值规则
#例如：分数(score)小于10同时生命值(life)大于0
while score < 10 and life > 0:
    meet = meet_what()
    if meet == "shoe":
        score = score + 1
        life = life + 1
    #作答区域，请在第15行设置人物在碰到墙时的扣血规则
    #例如：碰到墙时，生命值都减少1
    if meet == "wall":
        score = score - 1
    show_score(score)
    show_life(life)    
    play()

if score >= 10:
    game_win()
if life <= 0:
    game_fail()