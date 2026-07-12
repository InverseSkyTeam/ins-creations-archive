import requests
from xes.tool import *
xopen()
for i in range(1,51): # good = [5,11,33,66,133]
    print('\033[2J\033[100A\033[3J\033[100A'*2,'下载'+str(i)+'/50首ing...('+str(i*2)+'%)')
    referer='http://www.htqyy.com/play/6'
    headers={'Referer':referer,'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'}
    response = requests.get('http://f3.htqyy.com/play9/'+str(i)+'/mp3/6',headers=headers)
    with open(str(i)+".mp3",'wb') as file:
        file.write(response.content)
print('在弹出的窗口中查看爬取的音乐！')