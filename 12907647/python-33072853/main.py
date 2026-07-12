from jhx import *
d = dictionary.sort_data(dictionary.English_word)
for i in d:
    print("'"+i+"':"+"'"+d[i]+"',")
print('这是jhx库V0.6.0(build 111)版本，欢迎大家三连！用法看代码（帮助还在准备框架）。此库已经自动下载/升级，以后可以直接导入使用')
x = install.download()
if x == 0:
    print('更新成功！')
else:
    print('下载成功！')
# helpbook()