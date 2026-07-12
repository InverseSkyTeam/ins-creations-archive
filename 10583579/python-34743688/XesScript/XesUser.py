# Xes用户信息
# 作者:吴宇航
import requests,json
from typing import Union,Optional
class XesUser:
    def __init__(self,userid = Union[int,str],cookie:Optional[str] = None) -> None:
        self.headers = self.getHeaders(cookie)
        self.userid = userid
        datas = self.getUserData()
        self.primary = datas['primary']
        self.index = datas['index']
        self.webcover = datas['webcover']

    def getHeaders(self,cookie:str):
        if cookie:
            headers = {
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33',
                'Cookie':cookie
                }
        else:
            headers = {
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33',
                }
        return headers

    def extractData(self,urldict:dict,urlkey:str,formattext:object) -> dict:
        url = urldict[urlkey].format(formattext)
        data = requests.get(url,headers=self.headers).text
        targetdata = json.loads(data)
        return targetdata

    def extractContact(self,urldict:dict,urlkey:str,format1:object,format2:object) -> dict:
        url = urldict[urlkey].format(format1,format2)
        data = requests.get(url,headers=self.headers).text
        targetdata = json.loads(data)
        return targetdata

    def getUserData(self) -> dict:
        urldict = {
            "primary":"https://code.xueersi.com/api/space/profile?user_id={}",
            "index":"https://code.xueersi.com/api/space/index?user_id={}",
            "webcover":"https://code.xueersi.com/api/space/web_cover?user_id={}"
        }
        primary = self.extractData(urldict,"primary",self.userid)
        index = self.extractData(urldict,"index",self.userid)
        webcover = self.extractData(urldict,"webcover",self.userid)
        targetdict = {"primary":primary,"index":index,"webcover":webcover}
        return targetdict

    def getUserContact(self,page:int) -> dict:
        urldict ={
            "favorite":"https://code.xueersi.com/api/space/favorites?user_id={}&page={}&per_page=20",
            "follow":"https://code.xueersi.com/api/space/follows?user_id={}&page={}&per_page=10",
            "fans":"https://code.xueersi.com/api/space/fans?user_id={}&page={}&per_page=10",
            "medal":"https://code.xueersi.com/api/incentive/medals?user_id={}&page={}&per_page=15"
        }
        favorite = self.extractContact(urldict,"favorite",self.userid,page)
        follow = self.extractContact(urldict,"follow",self.userid,page)
        fans = self.extractContact(urldict,"fans",self.userid,page)
        medal = self.extractContact(urldict,"medal",self.userid,page)
        targetdict = {"favorite":favorite,"follow":follow,"fans":fans,"medal":medal}
        return targetdict

    def getUserWork(self,page:int,order:str) -> dict:
        url = f"https://code.xueersi.com/api/space/works?user_id={self.userid}&page={page}&per_page=20&order_type={order}"
        response = requests.get(url,headers=self.headers).text
        data = json.loads(response)
        return data