# Xes功能
# 作者:吴宇航
class XesSubmit:
    def __init__(self,cookie) -> None:
        self.cookie = cookie
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33',
            'Cookie':cookie
            }

    def submitFeedback(self,text:str,_type:str,contact:str = '',images:list = []):
        payload = {
            "contact":contact,
            "content":text,
            "images":images,
            "score":0,
            "source_type":_type
        }
        requests.post('https://code.xueersi.com/api/index/feedback/submit',headers=self.headers,json=payload)

    def submitReport(self):
        pass