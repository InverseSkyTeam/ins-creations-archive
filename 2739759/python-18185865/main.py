import webbrowser
from time import*
from xes.ext import*
def p(a):
    print(a)

from sys import *
def pr(line):
    for i in line:
        print(i,end="")
        stdout.flush()
        sleep(0.1)
    print("")
from os import*
def clear():
    import sys
    sys.stdout.write("\033[2J\033[00H")
pr("""关于我的小号和中号：
首先他们是干什么用的？我的小号呢是给大家讲一些社区里面的事情，还有跟大家分享一下我的日常。我的中号呢是给大家讲一些关于科技的东西，大家可以关注，然后我都会更新。
然后这里是我小号和中号的网址。大家输入1跳转到小号,2跳转到中号。
1.小号：https://code.xueersi.com/space/67387635
2.中号：https://code.xueersi.com/space/69643728""")
a = input("")
if(a == "1"):
    webbrowser.open("https://code.xueersi.com/space/67387635")
if(a == "2"):
    webbrowser.open("https://code.xueersi.com/space/69643728")