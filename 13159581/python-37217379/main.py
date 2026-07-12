import requests as r
import bs4
from tkinter import *

root = Tk()
f = Frame(root,width=500,height=500)
a = Label(root,text="记得去E盘看结果")
a.pack()
url = "https://static0.xesimg.com/pythonweb/bat/index.html"
head = {
    "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11"
}
res = r.get(url, headers=head)
res.encoding = res.apparent_encoding
soup = bs4.BeautifulSoup(res.text,"html.parser")
bat = soup.find_all("p",class_="content")
for b in bat:
    with open("E:\\关机.bat", "w") as f:
        f.write(b.text + "\n")
url2 = "https://static0.xesimg.com/pythonweb/bat/cancel.html"
head2 = {
    "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11"
}
res2 = r.get(url2, headers=head2)
res2.encoding = res2.apparent_encoding
soup2 = bs4.BeautifulSoup(res2.text,"html.parser")
bat2 = soup2.find_all("p",class_="content")
for b2 in bat2:
    with open("E:\\取消关机.bat", "w") as f2:
        f2.write(b2.text + "\n")

mainloop()