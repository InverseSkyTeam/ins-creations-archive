from jhx import *
print('这是jhx库V0.7.5(build 317)版本，欢迎大家三连！用法看代码（帮助还在编写中）。此库已经自动下载/升级，以后可以直接导入使用')
x = install.download()
if x == 0:
    print('更新成功！')
else:
    print('下载成功！')
helpbook()

# app = dsui.App()
# dsui.TextLabel(app)
# dsui.Button(app)
# dsui.Entry(app)
# f = dsui.Frame(app)
# dsui.TextBox(f,height=5)
# app.loop()