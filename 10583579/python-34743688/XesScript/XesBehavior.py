# Xes的操作、行为
# 作者:吴宇航
from urllib import parse
import requests
import json
class XesBehavior:
    def __init__(self, cookie: str) -> None:
        self.cookie = cookie
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33',
            'Cookie': cookie
        }

    def parseWorkURL(self, url: str) -> dict:
        url = parse.urlparse(url)
        parad = parse.parse_qs(url.query)
        return parad

    def getTopicID(self, workurl: str):
        urldata = self.parseWorkURL(workurl)
        pid = urldata['pid'][0]
        lang = urldata['lang'][0]
        if lang == 'scratch':
            topic_id = f'CS_{pid}'
        else:
            form = urldata['form'][0]
            if form == "cpp":
                topic_id = f'CC_{pid}'
            else:
                topic_id = f'CP_{pid}'
        return topic_id

    def doLike(self, workurl: str):
        urldata = self.parseWorkURL(workurl)
        pid = urldata['pid'][0]
        lang = urldata['lang'][0]
        if lang == "scratch":
            url = f'https://code.xueersi.com/api/projects/{pid}/like'
            payload = {
                "id": pid,
                "lang": "scratch"
            }
        else:
            form = urldata['form'][0]
            if form == "cpp":
                url = f'https://code.xueersi.com/api/compilers/{pid}/like'
                payload = {
                    "form": "cpp",
                    "id": pid,
                    "lang": "code"
                }
            else:
                url = f'https://code.xueersi.com/api/python/{pid}/like'
                payload = {
                    "form": form,
                    "id": pid,
                    "lang": "code"
                }
        response = requests.post(url, headers=self.headers, json=payload)

    def doCannellike(self, workurl: str):
        urldata = self.parseWorkURL(workurl)
        pid = urldata['pid'][0]
        lang = urldata['lang'][0]
        if lang == "scratch":
            url = f'https://code.xueersi.com/api/projects/{pid}/cancel_like'
            payload = {
                "id": pid,
                "lang": "scratch"
            }
        else:
            form = urldata['form'][0]
            if form == "cpp":
                url = f'https://code.xueersi.com/api/compilers/{pid}/cancel_like'
                payload = {
                    "form": "cpp",
                    "id": pid,
                    "lang": "code"
                }
            else:
                url = f'https://code.xueersi.com/api/python/{pid}/cancel_like'
                payload = {
                    "form": form,
                    "id": pid,
                    "lang": "code"
                }
        response = requests.post(url, headers=self.headers, json=payload)

    def doUnlike(self, workurl: str):
        urldata = self.parseWorkURL(workurl)
        pid = urldata['pid'][0]
        lang = urldata['lang'][0]
        if lang == "scratch":
            url = f'https://code.xueersi.com/api/projects/{pid}/unlike'
            payload = {
                "id": pid,
                "lang": "scratch"
            }
        else:
            form = urldata['form'][0]
            if form == "cpp":
                url = f'https://code.xueersi.com/api/compilers/{pid}/unlike'
                payload = {
                    "form": "cpp",
                    "id": pid,
                    "lang": "code"
                }
            else:
                url = f'https://code.xueersi.com/api/python/{pid}/unlike'
                payload = {
                    "form": form,
                    "id": pid,
                    "lang": "code"
                }
        response = requests.post(url, headers=self.headers, json=payload)

    def doCannelunlike(self, workurl: str):
        urldata = self.parseWorkURL(workurl)
        pid = urldata['pid'][0]
        lang = urldata['lang'][0]
        if lang == "scratch":
            url = f'https://code.xueersi.com/api/projects/{pid}/cancel_unlike'
            payload = {
                "id": pid,
                "lang": "scratch"
            }
        else:
            form = urldata['form'][0]
            if form == "cpp":
                url = f'https://code.xueersi.com/api/compilers/{pid}/cancel_unlike'
                payload = {
                    "form": "cpp",
                    "id": pid,
                    "lang": "code"
                }
            else:
                url = f'https://code.xueersi.com/api/python/{pid}/cancel_unlike'
                payload = {
                    "form": form,
                    "id": pid,
                    "lang": "code"
                }
        response = requests.post(url, headers=self.headers, json=payload)

    def doFavorite(self, workurl: str, state: int):
        topic_id = self.getTopicID()
        payload = {
            "state": state,
            "topic_id": topic_id
        }
        requests.post('https://code.xueersi.com/api/space/favorite', headers=self.headers, json=payload)

    def sendComment(self, workurl: str, text: str, targetid: int):
        """
        :param targetid:回复作品时targetid为0,回复作品下的评论时targetid为评论的id号
        """
        if len(text) > 200:
            raise ValueError("The length of the text argument cannot be greater than 200")
        topic_id = self.getTopicID(workurl)
        payload = {
            "appid": '1001108',
            "content": text,
            "target_id": targetid,
            "topic_id": topic_id
        }
        requests.post('https://code.xueersi.com/api/comments/submit', headers=self.headers, json=payload)

    def followUser(self, userid: int, state: int):
        payload = {
            "followed_user_id": str(userid),
            "state": state
        }
        requests.post('https://code.xueersi.com/api/space/follow', headers=self.headers, json=payload)