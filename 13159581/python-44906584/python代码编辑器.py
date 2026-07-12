from easygui import *
while True:
    try:
        a = textbox("请输入你的代码")
        b = buttonbox("你要保存还是运行？(如果报错且代码未保存，代码会全部消失)",choices=["保存","运行","退出"])
        if b == "运行":
            exec(a)
        elif b == "退出":
            break
        else:
            c = filesavebox("请选择保存的路径",filetypes=["*.py"],default="新建Python文件.py")
            f = open(c,"w")
            f.write(a)
            f.close()
    except:
        msgbox("出错啦")
