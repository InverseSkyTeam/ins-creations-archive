print("我穷尽了一生，也没能带来PySide6")
print("示例作品：学而思网盘lrs版本")
# 真是的，Qt闹鬼自动重新编译ui文件到py导致res_rc闹鬼，只好把res_rc.py复制到script下面。。。

import requests
import zipfile
import os
import shutil

version = 2
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
}
url = "https://livefile.xesimg.com/programme/python_assets/28bf75109878e73db5e54f6127679905.zip"
chunk_size = 2048

if not os.path.exists("../lrsXesPan"):
    os.mkdir("../lrsXesPan")

if not os.path.exists("../lrsXesPan/version.txt"):
    with open("../lrsXesPan/version.txt", "w", encoding="utf-8") as file:
        file.write("0")

with open("../lrsXesPan/version.txt", "r", encoding="utf-8") as file:
    try:
        current_version = int(file.read())
    except:
        current_version = 0

if current_version < version:
    with open("../lrsXesPan/version.txt", "w", encoding="utf-8") as file:
        file.write(str(version))

    if os.path.exists("../lrsXesPan/XesPanPack.zip"):
        os.remove("../lrsXesPan/XesPanPack.zip")
    if os.path.exists("../lrsXesPan/XesPanPack"):
        shutil.rmtree("../lrsXesPan/XesPanPack")

    print("正在下载 XesPanPack.zip")

    with open("../lrsXesPan/XesPanPack.zip", "wb") as file:
        res = requests.get(url, headers=header)
        file.write(res.content)
    
    print("下载成功！")

    with zipfile.ZipFile("../lrsXesPan/XesPanPack.zip") as zip:
        zip.extractall("../lrsXesPan")
    print("解压完毕！")
else:
    print("已存在最新的 XesPanPack.zip，无需下载")

print("开始运行...")
os.chdir("../lrsXesPan/XesPanPack")
os.system("runtime\\pythonw.e" + "xe script\\main.py")
print("已启动独立线程运行！希望你可以点一个免费的赞（")
