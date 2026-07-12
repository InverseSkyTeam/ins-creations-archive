print(r'''
昨天我的insjhx语言速度被付开霁的newlang语言打败以后，我决定放弃了上一个insjhx系列.
可是我仍然不甘心，昨天十二点去睡觉，但是睡不着，一直在思考最优的算法，于是我到凌晨两点才睡着
思来想去，我就打算写了这样一个作品

exec版ij遗址(Edition -2.1):
https://code.xueersi.com/home/project/detail?lang=code&pid=37980375&version=offline&form=python&langType=python

解释器版ij遗址(Edition -1.0):
https://code.xueersi.com/home/project/detail?lang=code&pid=40457109&version=offline&form=python&langType=python

token栈版ij遗址(Edition -0.1):
https://code.xueersi.com/home/project/detail?lang=code&pid=41062980&version=offline&form=python&langType=python

它们，都是过往。
新的版本将会是：字符串版ij(非遗文化/doge曲解)

字符串版的ij将会是从0.0开始连载
接下来简要说明各大算法

1.读入
在读入这方面，token版ij做得很好，竟然超越了python本身，快速的分割、读取把复杂度降到了O(n-x)左右，x是数字、字符串的位数总和
这使得ij的读入速度一度碾压吴宇航和付开霁之前的所有语言，因为他们的复杂度至少是O(n)，大数据测量(如100000位的数字)时，他们的会报废到几十几百秒，我则只要一秒
在字符串ij中，这个速度将进一步提升到旧版ij的120倍左右，甚至超过python.
它的读入速度是，1亿字符/s左右。你可能觉得，这不太可能，因为连c++都很难做到
但实际上，我已经做好了。那就是正则表达式！由于内置的转义很多不匹配，所以我拉长把所有符号写了一遍
实测：141000000字符用了1.5s不到
正则：r'[\w\.]+|[\n\(\)\[\]\{\}]|[\+\-\*\/\!\?\@\#\$\%\^\&\|\~\<\>\=\,\:\;\.\'\"]+'
代码（内含苛刻代码）：
import re
string = """
a=1+1 (b =  666.66)
if a {
    a
} elif b==true {
    b
}else{
    666
}
c = a <= b
cycle b with i {
    out b
}
d = 5/((1+2)**3+4)
d >>= c
"""
to_split = r'[\w\.]+|[\n\(\)\[\]\{\}]|[\+\-\*\/\!\?\@\#\$\%\^\&\|\~\<\>\=\,\:\;\.\'\"]+'
result = re.findall(to_split,string)
for i in result:
    print(i,end=' ')
print(result)

2.执行
原以为我的ij很快了，但是执行速度竟然被付开霁的newlang碾压了，阶乘速度只有它的1/15
所以我下决心，一定要碾压付开霁。于是我做完就思考了各种算法。
这个代码既要突破一定的递归限制，又要快速
我想到了一个方法，就是前缀表达式
new i
end new
give i 0
end give
if
condition
same i 0
end same
end condition
then
give
i
plus 1 1
end give
end then
end if
out i
end out
这个的分析简单很多，但是，我做的是insjhx，不是汇编啊！
转前缀后缀则都有很多问题，时间复杂度也高达O(xn)
于是打算用两种方法，均为O(n)：
(1)优先级从高到低依次计算
(2)优先级从低到高，把左右分别作为枝干计算
具体后期优化

大家也来讨论一下！
''')