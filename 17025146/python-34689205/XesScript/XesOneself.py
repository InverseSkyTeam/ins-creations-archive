import requests
from typing import Union,Optional
import json
from urllib import parse
import constant

# Xes自己的信息
class XesOneself():
    def __init__(self,uid:int,cookie:str) -> None:
        self.id = uid
        self.cookie = cookie
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33',
            'Cookie':cookie
            }

    def getMyWork(self,pulished:str,_type:str,page:int,lang:str) -> dict:
        urldict = {
            "python":'https://code.xueersi.com/api/python/my?published={}&type={}&page={}&per_page=20',
            "cpp":'https://code.xueersi.com/api/compilers/my?published={}&type={}&page={}&per_page=20',
            "scratch":'https://code.xueersi.com/api/projects/my?published={}&type={}&page={}&per_page=20',
        }
        url = urldict[lang].format(pulished,_type,page)
        response = requests.get(url,headers=self.headers).text
        data = json.loads(response)
        return data
    
    def getMyWebCover(self) -> dict:
        """获取自己已发布的可以作为封面的作品
        """
        url = "https://code.xueersi.com/api/space/web_cover/web_projects"
        response = requests.get(url,headers=self.headers).text
        data = json.loads(response)
        return data

    def getMessages(self,category:int,page:int,subtype:Optional[str] = None) -> dict:
        """
        :category:1为评论,2为点赞与收藏,3为反馈与审核(此选项需填subtype参数),4为系统消息,5为关注
        :subtype:feedback为建议反馈,report为举报,audit为审核,all为全部
        """
        if category != 3:
            url = f'https://code.xueersi.com/api/messages?category={category}&page={page}&per_page=10'
        else:
            if subtype:
                if subtype != 'all' and subtype != '':
                    url = f'https://code.xueersi.com/api/messages?category=3&sub_type=&page={page}&per_page=10'
                else:
                    url = f'https://code.xueersi.com/api/messages?category=3&sub_type={subtype}&page={page}&per_page=10'
            else:
                raise ValueError('If you want to retrieve messages, the subtype parameter cannot be null')
        response = requests.get(url,headers=self.headers).text
        data = json.loads(response)
        return data

    def setSignatrue(self,text:str) -> None:
        payloads = {
            "signature":text
        }
        url = "https://code.xueersi.com/api/space/edit_signature"
        response = requests.post(url,headers=self.headers,json = payloads)

    def setRepresentative(self,topic_id:str,state:int) -> None:
        """
        :state:0为取消代表作,1为设为代表作
        """
        payloads = {
            "state":state,
            "topic_id":topic_id
        }
        url = "https://code.xueersi.com/api/space/set_representative_work"
        response = requests.post(url,headers=self.headers,json = payloads)