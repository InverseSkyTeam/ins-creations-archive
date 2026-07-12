# import requests as rq
# from bs4 import BeautifulSoup

# URL = 'http://top.baidu.com/buzz?b=1'
# headers = {
#     'host': 'top.baidu.com',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
# }
# def getNews():
#     news = {}
#     try:
#         res = rq.get(URL,headers = headers)
#         res.encoding = 'gbk'    
#         soup = BeautifulSoup(res.text,'lxml')
#         hot = soup.find_all('a',class_='list-title')
#         for h in hot:
#             news[h.text] = h['href']     
        
#     except:
#         with open("./static/news.txt",encoding='utf-8') as f:
#             contents = f.readlines()
#         for content in contents:
#             content = content.split(",")
#             news[content[0]] = content[1] 
 
#     return news


def get_news():
    news = {}
    with open("./static/news.txt",encoding='utf-8') as f:
        contents = f.readlines()
        for content in contents:
            content = content.split(",")
            news[content[0]] = content[1] 
    return news