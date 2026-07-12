from hitmouse import *

n = int(input("请输入年兽洞排数："))
m = int(input("请输入年兽洞列数："))

#TODO初级改编：可改变年兽洞穴的样式
add_hole("洞穴6.png")
#TODO初级改编：可修改年兽的外观
add_pic("年兽1.png","年兽1",)
add_pic("年兽2.png","年兽2")
add_pic("年兽3.png","年兽3")
add_pic("年兽4.png","年兽4")
#{
set_map([['h' for i in range(m)] for j in range(n)])
#}

#击打的年兽数量
count = 0
while True:
    m = hit()
    #TODO高级改编1：修改击打年兽后的结果
    if m == '年兽1':
        count = count + 1
    elif m == '年兽2':
        #让锤子变小或变大
        # big()
        # small()
        count = count + 1
    elif m == '年兽3':
        count = count + 1
    elif m == '年兽4':
        #全屏爆炸
        boom()
        count = 0
    else:
        pass
        
    #TODO高级改编2：修改难度区间
    if count <= 20:
        #控制游戏难度，数字越大游戏越难
        mouse(2)
    elif count <= 40:
        mouse(4)
    else:
        mouse(6)
    # 开始游戏
    play()
    # 显示击打的年兽数
    show_beast(count)