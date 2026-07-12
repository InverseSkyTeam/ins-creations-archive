#补充第14、29行代码，完善垃圾分类的程序吧
#提示：可修改第20行代码调整垃圾的个数
from garbage import *

set_time(75)  #可修改游戏时间，数字要求大于0
show_score()  #不需要修改，仅显示正确投放垃圾的数目

dry = ["猫砂", "干燥剂", "编织袋"]       # 干垃圾
harm = ["过期药", "电池", "杀虫剂"]      # 有害垃圾
rec = ["废纸", "啤酒瓶", "易拉罐"]       # 可回收物

#(1)创建湿垃圾列表
#湿垃圾，比如："果皮", "菜根", "鱼鳞"
wet = ["果皮","菜根","鱼鳞"]


show_garbage(dry,harm,rec,wet)


for i in range(10):    
    g = get_garbage()
    if g in dry:
        result(dry)
    if g in harm:
        result(harm)
    if g in rec:
        result(rec)
    #(2)判断输入的垃圾 g 是否属于湿垃圾
    if g in  wet:
        result(wet)
        
honor()#不需要修改，显示获得了什么称号