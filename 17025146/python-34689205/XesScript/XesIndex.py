import requests
from typing import Union,Optional
import json
from urllib import parse
import constant

# Xes首页
class XesIndex():
    def __init__(self,cookie:Optional[str] = None) -> None:
        self.cookie = cookie
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33',
            'Cookie':cookie
            }
    
    def getModules(self) -> dict:
        url = "https://code.xueersi.com/api/index/works/modules"
        response = requests.get(url,headers=self.headers).text
        data = json.loads(response)
        return data

    def getFollows(self) -> dict:
        url = "https://code.xueersi.com/api/index/works/follows"
        response = requests.get(url,headers=self.headers).text
        data = json.loads(response)
        return data

    def getForyou(self) -> dict:
        url = "https://code.xueersi.com/api/pai/projects/for_you"
        response = requests.get(url,headers=self.headers).text
        data = json.loads(response)
        return data