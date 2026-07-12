# 法1
print(f"测试{chr(99)}ookie")

# 法2
lst = ["测试"+"c","o","o","k","i","e"]
print("".join(lst))

# 法3
# 这边先上传写好的代码
# from xes.uploader import *
# from os import remove
# up = XesUploader()
# with open("代码.py","w",encoding="utf-8") as f:
#     f.write('print("测试c ookie")')(这边去个空格)
# f.close()
# print(up.upload("代码.py"))
# remove("代码.py")
# 上传结果
# https://livefile.xesimg.com/programme/python_assets/05e93271fbde08a2fc9545de1748239d.py

# 下载代码
import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
}
base = "https://livefile.xesimg.com/programme/python_assets/05e93271fbde08a2fc9545de1748239d.py"
response = requests.get(base,headers = headers)
try:
    res = response.content.decode("utf-8")
except:
    res = response.content.decode("gb18030")
exec(res)

# 法4
# 本方法是使用云变量，这里就不写了，可以使用封装过的cloudlib
# 本方法本质还是和法3一样
# 地址：https://livefile.xesimg.com/programme/python_assets/d0ec229c07a85da13bcb367be790179d.py
# 下载方法：详见法3

# 法5
print("测试c\x00ookie")

# 法6
print("测试"+"c"+"ookie")

# 法7
from http import cookiejar
print("测试"+cookiejar.__name__[5:-3])

# 法8
print("测试c⁣ookie")