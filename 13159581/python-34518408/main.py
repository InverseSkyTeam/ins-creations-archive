import requests
import bs4
from xes.tool import *
print("今天，期末考试考完了，我very开心，打开电脑爬了亿小会儿虫：")
path = xopen("mc")
url = "https://mc.163.com/wjzp/"
res = requests.get(url)
res.encoding = "UTF-8"
soup = bs4.BeautifulSoup(res.text, "lxml")
image = soup.find_all("div", class_="works_dl")
# 展示结果
for n in image:
    print(n.p.text)
    print(n.img["src"])
    # 获取图片数据
    res = requests.get(n.img["src"])
    pic = res.content
    file_name = path + n.p.text + ".jpg"
    with open(file_name, "wb") as file:
        file.write(pic)