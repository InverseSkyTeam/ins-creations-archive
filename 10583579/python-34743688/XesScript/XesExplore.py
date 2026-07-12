# Xes发现
# 作者:吴宇航
import requests
import json
from typing import Optional
class XesExplore:
    def __init__(self) -> None:
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33',
            }

    def getExplore(self,_type:str,page:int,lang:Optional[str] = None,tag:Optional[str] = None) -> dict:
        if not lang:
            lang = ''
        if not tag:
            tag = ''
        else:
            tag = parse.quote(tag)
        url = f'https://code.xueersi.com/api/works/{_type}?type={_type}&lang={lang}&tag={tag}&page={page}&per_page=50'
        response = requests.get(url,headers=self.headers).text
        data = json.loads(response)
        return data

    def getSearch(self,_type:str,page:int,keyword:str,lang:Optional[str] = None,order:Optional[str] = None):
        if (_type == "works" or _type == "videos") and order:
            order = order
        else:
            order = 'comprehensive'
        if _type == 'works' and lang:
            lang = lang
        else:
            lang = 'all'
        url = f'https://code.xueersi.com/api/search?keyword={parse.quote(keyword)}&search_type={_type}&order_type={order}&lang={lang}&page={page}&per_page=50'
        response = requests.get(url,headers=self.headers).text
        data = json.loads(response)
        return data