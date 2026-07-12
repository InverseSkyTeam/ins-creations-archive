# -*- coding=utf-8 -*-
# import pdfkit
import parsel
import requests
import html2text as ht
import bs4
from xes.tool import *

def download_csdn(url,mdname,_type = "md"):
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
    </head>
    <body>
    {content}
    </body>
    </html>
    """

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
        'Host': 'blog.csdn.net',
        'Referer': 'https://blog.csdn.net',
    }


    def get_csdn_cookie():
        response = requests.get('https://www.csdn.net/', headers=headers)
        return response.cookies


    def get_html(url):
        """获取索引页"""
        response = requests.get(url, headers=headers)
        sel = parsel.Selector(response.text)
        list_a = sel.css('.article-list a')
        for i in list_a[2:]:
            article_index = i.css('a::attr(href)').get()
            yield article_index


    def csdn(url: str, cookie=get_csdn_cookie()):
        """下载 CSDN 文章html"""
        response = requests.get(url, headers=headers, cookies=cookie)
        # 获取文章标题内容
        sel = parsel.Selector(response.text)
        # print(response.text)
        title = sel.css('.title-article::text').get()
        article = sel.css('article').get()
        return title, article


    def html_to_md(filename_html, filename_md):
        with open(filename_html, mode='r', encoding='utf-8') as f:
            htmlpage = f.read()
        text_maker = ht.HTML2Text()
        text_maker.bypass_tables = False
        text = text_maker.handle(htmlpage)
        with open(filename_md,"w",encoding="utf-8") as f:
            f.write(text)
    title, article = csdn(url)
    html = html_template.format(content=article)
    if _type == "md":
        text_maker = ht.HTML2Text()
        text_maker.bypass_tables = False
        text = text_maker.handle(html)
        with open(mdname,"w",encoding="utf-8") as f:
            f.write(text)
    else:
        with open(mdname,"w",encoding="utf-8") as f:
            f.write(html)


def download_cnblog(url,mdname,_type = "md"):
    html_template1 = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        {styles}
    </head>
    <body>
    {content}
    </body>
    </html>
    """
    res = requests.get(url)
    res.encoding = "UTF-8"
    bs = bs4.BeautifulSoup(res.text,"lxml")
    jieguo = str(bs.find(id = "cnblogs_post_body"))
    stlslist = bs.find_all("link") + bs.find_all("style")
    for i in range(len(stlslist)):
        stlslist[i] = str(stlslist[i])
    stl = "".join(stlslist)
    txt = html_template1.format(content = jieguo,styles = stl)
    if _type == "md":
        text_maker = ht.HTML2Text()
        text_maker.bypass_tables = False
        text = text_maker.handle(txt)
        with open(mdname,"w",encoding="utf-8") as f:
            f.write(text)
    else:
        with open(mdname,"w",encoding="utf-8") as f:
            f.write(txt)
            
url = input("输入要下载的博客地址:")
path = input("输入要将博客下载到的路径:")
if "csdn" in url:
    download_csdn(url,f"{path}/blog.md")
else:
    download_cnblog(url,f"{path}/blog.md")
print("下载完成")