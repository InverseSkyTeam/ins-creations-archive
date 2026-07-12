import requests
import bs4
import time
head = {
    "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11"
}

print("洛谷题号：例如：P1000")

name = input()

url = "https://www.luogu.com.cn/problem/"+name

res = requests.get(url, headers=head)
res.encoding = res.apparent_encoding 

soup = bs4.BeautifulSoup(res.text, "lxml")  

text = soup.find_all("script", class_="")[0]

text = str(text)


    
a = text[61:-78]    

from urllib.parse import unquote_to_bytes
import json

b = unquote_to_bytes(a.encode()).decode()
text = json.loads(b)['currentData']['problem']['description']

print(text)


    
