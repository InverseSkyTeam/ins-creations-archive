import sys
said = []
# -*- coding: utf-8 -*-
#author:zxy
#Date:2018-10-19


import requests
import re
HEADERS={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                 "Chrome/69.0.3497.100 Safari/537.36"
}


def parse_url(url):
    response=requests.get(url,headers=HEADERS)
    text=response.text
    titles=re.findall(r'<div\sclass="cont">.*?<b>(.*?)</b>',text,re.DOTALL) #r raw
    dynasties=re.findall(r'<p\sclass="source">.*?<a.*?>(.*?)</a>',text,re.DOTALL)
    authors=re.findall(r'<p\sclass="source">.*?<a.*?<a.*?>(.*?)</a>',text,re.DOTALL)
    content_tags=re.findall(r'<div\sclass="contson".*?>(.*?)</div>',text,re.DOTALL)
    contents=[]
    for content_tag in content_tags:
        x=re.sub('<.*?>','',content_tag)
        xx=re.sub('。', '。\n',x)
        contents.append(xx.strip())
    poems=[]
    for value in zip(titles,dynasties,authors,contents):
        title,dynasty,author,content=value
        poem={
            "title":title,
            "dynasty":dynasty,
            "author":author,
            "content":content
        }
        poems.append(poem)

    with open('poems.txt','w',encoding="utf-8") as f:
        for poem in poems:
            for (key,value) in poem.items():
                if(key=="title"):
                    f.write("{}\n".format(value))
                if (key == "dynasty"):
                    f.write("\t{}\n".format(value))
                if(key=="author"):
                    str="\t{}\n"
                    f.write(str.format(value))
                if(key=="content"):
                    for i in list:
                    
                                said.append(value)
                    f.write("{}\n\n\n".format(value))
                    # print(x+"{}\n\n\n".format(value))
while True:    
    a = input()
    url="https://so.gushiwen.cn/search.aspx?value="+a
    parse_url(url)