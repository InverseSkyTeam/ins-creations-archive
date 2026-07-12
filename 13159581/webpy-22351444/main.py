#请补充字典单词，并使用for遍历将其添加到游戏中
from Wordbook import *

#作答区域，请在7~9行将不认识的单词以键值对的形式存储到字典中
#例如："bus":"巴士"
sign = {
    "bus":"巴士",
    "left":"左",
    "right":"右",
    "exit":"出口",
    "flower":"花朵",
    "store":"商店"
}

#作答区域，请在第13行完整写出for遍历字典的语句
for k in sign:
    add(k,sign[k])
    
play()