import requests
import bs4
from urllib.parse import unquote_to_bytes
import json
head = {
    "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11"
}

name = input('请输入题目编号：')
url = "https://www.luogu.com.cn/problem/"+name
res = requests.get(url, headers=head)
res.encoding = res.apparent_encoding 
soup = bs4.BeautifulSoup(res.text, "lxml")  
text = soup.find_all("script", class_="")[0]
text = str(text)
a = text[61:-78]  
b = unquote_to_bytes(a.encode()).decode()
data = json.loads(b)['currentData']['problem']

text = '# ' + data['title'] + '\n'
dic = {'background': '题目背景', 
       'description': '题目描述',
       'inputFormat': '输入格式',
       'outputFormat': '输出格式',
       'hint': '提示'}
def add(name, text, data):
    if data[name] != '':
        text += '\n## ' + dic[name] + '\n\n' + data[name] + '\n'
    return text
text = add('background', text, data)
text = add('description', text, data)
text = add('inputFormat', text, data)
text = add('outputFormat', text, data)
for i, sam in enumerate(data['samples']):
    text += '\n## 样例 #' + str(i+1) + '\n\n### 样例输入 #'+str(i+1) + '\n\n```\n' + sam[0] + '\n```\n\n### 样例输出 #'+str(i+1)+'\n\n```\n'+sam[1]+'\n```\n'
text = add('hint', text, data)

print(text)


    
