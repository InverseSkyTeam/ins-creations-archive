from pickle import *
from easygui import *
import os
from time import *
import sys

try:
    s = strftime("%Y年%m月%d日")
    while True:
        a = buttonbox("欢迎来到来自cjy(名字首字母)的密码日记本",choices=('读','写','退出'))
        if a == "写":
            b = textbox("你要写入什么")
            c = os.getcwd() + "\\日记\\"+s+".txt"
            file = open(c,'wb')
            dump(b,file)
            file.close()
        if a == "读":
            msgbox("找到保存日记的位置，并选择日记即可。")
            d = fileopenbox(default="./日记/*.txt")
            file1 = open(d,"rb")
            e = load(file1)
            textbox(msg="你选择的文件的内容如下",text=e)
        if a == "退出":
            break
except:
    msgbox("错误关闭！！！！")
    sys.exit()
