#补充完整第7行、第24行和第29行代码，设计自己的娃娃机。
from dolls_mach import *
#补充完整第7行代码，设置娃娃机中的娃娃。
#注意：图片名称是键，积分是值。
#例如：dolls = {"柠檬.png":100}
#作答区域。
dolls = {
    "主讲.png":5,
    "康静静.png":543,
    "刘祥.png":64,
    "王雪.png":6456,
    "王立松.png":5635,
    "柯南.png":5645
}

set_dolls(dolls)

#设置抓力，数字从1到10，数字越大，抓力越大。
set_power(5)
#设置爪子移动速度，数字越大，移动速度越快。
set_speed(25)

score = 0

while True:
    key = catch()
    if key != '':
        #补充完整第24行代码（加号后内容），获取娃娃的积分。
        #提示：字典中值的访问 字典名[键]
        #作答区域。
        score = score + doll[key]
        show_score(score)
        #补充完整第29行代码，取出成功抓到的娃娃。
        #提示： del 字典名[键]
        #作答区域。
        del dolls[key]
    #设置游戏时间，修改数字。
    game_time(20)
    play()