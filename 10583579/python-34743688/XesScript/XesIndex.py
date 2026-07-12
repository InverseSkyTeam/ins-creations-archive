# Xes首页
# 作者:何嘉晨
import requests,json
from typing import Optional
class XesIndex:
    def __init__(self,cookie:str) -> None:
        self.Follows = self.follows(cookie)
        self.Index = self.modules(1,cookie)
        self.Classroom = self.modules(1,cookie)
        self.Teacher = self.modules(3,cookie)

    @classmethod
    def getHeaders(self,cookie:str) -> dict:
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

    class follows:
        def __init__(self,cookie:str):
            self.cookie = cookie
            self.headers = XesIndex.getHeaders(self.cookie)
            self.primary = self.getFollows()
        def getFollows(self):
            return json.loads(requests.get('https://code.xueersi.com/api/index/works/follows', headers=self.headers).text)
        def getLikes(self) -> int:
            return [i['likes'] for i in self.primary['data']]
        def getUnlikes(self) -> int:
            return [i['unlikes'] for i in self.primary['data']]
        def getFavorites(self) -> int:
            return [i['favorites'] for i in self.primary['data']]
        def getUserid(self) -> int:
            return [i['user_id'] for i in self.primary['data']]
        def getUsername(self) -> int:
            return [i['username'] for i in self.primary['data']]
        def getCommentsnum(self) -> int:
            return [i['comments'] for i in self.primary['data']]
        def getCreatedat(self) -> str:
            return [i['created_at'] for i in self.primary['data']]
        def getDeletedat(self) -> str:
            return [i['deleted_at'] for i in self.primary['data']]
        def getHiddencode(self) -> int:
            return [i['hidden_code'] for i in self.primary['data']]
        def getManual(self) -> int:
            return [i['manual_weight'] for i in self.primary['data']]
        def getModifiedat(self) -> str:
            return [i['modified_at'] for i in self.primary['data']]
        def getWorkname(self) -> str:
            return [i['name'] for i in self.primary['data']]
        def getLang(self) -> str:
            return [i['lang'] for i in self.primary['data']]
        def getID(self) -> int:
            return [i['id'] for i in self.primary['data']]
        def getOriginalid(self) -> int:
            return [i['original_id'] for i in self.primary['data']]
        def getScore(self) -> float:
            lst = []
            for i in self.primary['data']:
                try:
                    lst.append(i["popular_score"])
                except:
                    lst.append('NaN')
        def getIspublic(self) -> int:
            return [i['published'] for i in self.primary['data']]
        def getPublishedat(self) -> str:
            return [i['published_at'] for i in self.primary['data']]
        def getRemoved(self) -> int:
            return [i['removed'] for i in self.primary['data']]
        def getSourceview(self) -> int:
            return [i['source_code_views'] for i in self.primary['data']]
        def getThumbnail(self) -> str:
            return [i['thumbnail'] for i in self.primary['data']]
        def getTopic(self) -> str:
            return [i['topic_id'] for i in self.primary['data']]
        def getType(self) -> str:
            return [i['type'] for i in self.primary['data']]
        def getUpdatedat(self) -> str:
            return [i['updated_at'] for i in self.primary['data']]
        def getVersion(self) -> str:
            return [i['version'] for i in self.primary['data']]
        def getViews(self) -> int:
            return [i['views'] for i in self.primary['data']]

    class modules:
        def __init__(self,input_index:int,cookie:Optional[str] = None):
            """
            :param cookie:Cookie
            :param input_index:
                   1 -> 首页
                   2 -> 开眼课堂
                   3 -> 老师的作品
            """
            self.cookie = cookie
            self.headers = XesIndex.getHeaders(self.cookie)
            if input_index == 1:index1 = 0
            elif input_index == 2:index1 = 1
            else:index1 = 4
            self.primary = self.getModules()["data"][index1]["items"]

        def getModules(self) -> dict:
            url = "https://code.xueersi.com/api/index/works/modules"
            response = requests.get(url,headers=self.headers).text
            data = json.loads(response)
            return data
        def getLikes(self) -> int:
            return [i['likes'] for i in self.primary]
        def getUnlikes(self) -> int:
            return [i['unlikes'] for i in self.primary]
        def getFavorites(self) -> int:
            return [i['favorites'] for i in self.primary]
        def getUserid(self) -> int:
            return [i['user_id'] for i in self.primary]
        def getUsername(self) -> int:
            return [i['username'] for i in self.primary]
        def getCommentsnum(self) -> int:
            return [i['comments'] for i in self.primary]
        def getCreatedat(self) -> str:
            return [i['created_at'] for i in self.primary]
        def getDeletedat(self) -> str:
            return [i['deleted_at'] for i in self.primary]
        def getHiddencode(self) -> int:
            return [i['hidden_code'] for i in self.primary]
        def getManual(self) -> int:
            return [i['manual_weight'] for i in self.primary]
        def getModifiedat(self) -> str:
            return [i['modified_at'] for i in self.primary]
        def getWorkname(self) -> str:
            return [i['name'] for i in self.primary]
        def getLang(self) -> str:
            return [i['lang'] for i in self.primary]
        def getID(self) -> int:
            return [i['id'] for i in self.primary]
        def getOriginalid(self) -> int:
            return [i['original_id'] for i in self.primary]
        def getScore(self) -> float:
            lst = []
            for i in self.primary:
                try:
                    lst.append(i["popular_score"])
                except:
                    lst.append('NaN')
        def getIspublic(self) -> int:
            return [i['published'] for i in self.primary]
        def getPublishedat(self) -> str:
            return [i['published_at'] for i in self.primary]
        def getRemoved(self) -> int:
            return [i['removed'] for i in self.primary]
        def getSourceview(self) -> int:
            return [i['source_code_views'] for i in self.primary]
        def getThumbnail(self) -> str:
            return [i['thumbnail'] for i in self.primary]
        def getTopic(self) -> str:
            return [i['topic_id'] for i in self.primary]
        def getType(self) -> str:
            return [i['type'] for i in self.primary]
        def getUpdatedat(self) -> str:
            return [i['updated_at'] for i in self.primary]
        def getVersion(self) -> str:
            return [i['version'] for i in self.primary]
        def getViews(self) -> int:
            return [i['views'] for i in self.primary]

    class foryou:
        def __init__(self,cookie:str):
            self.cookie = cookie
            self.headers = XesIndex.getHeaders(self.cookie)
            self.primary = self.getFor_you()['data']['projects']
        def getFor_you(self):
            return json.loads(requests.get('https://code.xueersi.com/api/pai/projects/for_you', headers=self.headers).text)
        def getLikes(self) -> int:
            return [i['likes'] for i in self.primary]
        def getUnlikes(self) -> int:
            return [i['unlikes'] for i in self.primary]
        def getFavorites(self) -> int:
            return [i['favorites'] for i in self.primary]
        def getUserid(self) -> int:
            return [i['user_id'] for i in self.primary]
        def getUsername(self) -> int:
            return [i['username'] for i in self.primary]
        def getCommentsnum(self) -> int:
            return [i['comments'] for i in self.primary]
        def getCreatedat(self) -> str:
            return [i['created_at'] for i in self.primary]
        def getDeletedat(self) -> str:
            return [i['deleted_at'] for i in self.primary]
        def getHiddencode(self) -> int:
            return [i['hidden_code'] for i in self.primary]
        def getManual(self) -> int:
            return [i['manual_weight'] for i in self.primary]
        def getModifiedat(self) -> str:
            return [i['modified_at'] for i in self.primary]
        def getWorkname(self) -> str:
            return [i['name'] for i in self.primary]
        def getLang(self) -> str:
            return [i['lang'] for i in self.primary]
        def getID(self) -> int:
            return [i['id'] for i in self.primary]
        def getOriginalid(self) -> int:
            return [i['original_id'] for i in self.primary]
        def getScore(self) -> float:
            lst = []
            for i in self.primary:
                try:
                    lst.append(i["popular_score"])
                except:
                    lst.append('NaN')
        def getIspublic(self) -> int:
            return [i['published'] for i in self.primary]
        def getPublishedat(self) -> str:
            return [i['published_at'] for i in self.primary]
        def getRemoved(self) -> int:
            return [i['removed'] for i in self.primary]
        def getSourceview(self) -> int:
            return [i['source_code_views'] for i in self.primary]
        def getThumbnail(self) -> str:
            return [i['thumbnail'] for i in self.primary]
        def getTopic(self) -> str:
            return [i['topic_id'] for i in self.primary]
        def getType(self) -> str:
            return [i['type'] for i in self.primary]
        def getUpdatedat(self) -> str:
            return [i['updated_at'] for i in self.primary]
        def getVersion(self) -> str:
            return [i['version'] for i in self.primary]
        def getViews(self) -> int:
            return [i['views'] for i in self.primary]