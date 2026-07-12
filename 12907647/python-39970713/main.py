import requests
import base64
import json

class RunoobRun:
    def __init__(self):
        self.headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,zh-TW;q=0.6,eo;q=0.5',
            'Connection': 'keep-alive',
            'Content-Length': '86',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'tool.runoob.com',
            'Origin': 'https://c.runoob.com',
            'Referer': 'https://c.runoob.com/',
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        }
        self.langdict = {
            'Python3': (15,'py3'),
            'C': (7,'c'),
            'C++': (7,'cpp'),
            'Bash': (11,'sh'),
            'C#': (10,'cs'),
            'Java': (8,'java'),
            'R': (80,'R'),
            'Node.js': (4,'node.js'),
            # '': (,''),
            # '': (,''),
            # '': (,''),
            # '': (,''),
            # '': (,''),
            # '': (,''),
            # '': (,''),
            # '': (,''),
            # '': (,''),
            # '': (,''),
            # '': (,''),
            # '': (,''),
            # '': (,''),
            # '': (,''),
            # '': (,''),
            # '': (,''),
            # '': (,''),
            # '': (,''),
        }
    def runCode(self,languge,code,fileext,stdin):
        data = {
            "code": code,
            "token": "b6365362a90ac2ac7098ba52c13e352b",
            "stdin": stdin,
            "language": str(languge),
            "fileext": fileext
        }
        res = requests.post(
            "https://tool.runoob.com/compile2.php",
            headers=self.headers,
            data=data)
        result = json.loads(res.text)
        return [result['output'],result['errors']]

    def run(self,languge,code,stdin):
        langid = self.langdict[languge][0]
        langext = self.langdict[languge][1]
        return self.runCode(langid,code,langext,stdin)

run = RunoobRun()
print(run.run(languge='Python3',code='print(input())',stdin='这里是输入的内容:小轩yyds!'))





















class BejsonRun():
    def __init__(self):
        self.headers = headers = {
            "authority": "runcode.bejson.com",
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "origin": "https://www.bejson.com",
            "referer": "https://www.bejson.com/",
            "sec-ch-ua": "\" Not;A Brand\";v=\"99\", \"Microsoft Edge\";v=\"103\", \"Chromium\";v=\"103\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62"
        }
        # self.langdict = langdict

    def getToken(self,code,languge):
        params = {
            "action": "get_token"
        }
        data = {
            "source_code": code,
            "language_id": str(languge),
            "command_line_arguments": "",
            "stdin": ""
        }
        res = requests.post(
            "https://runcode.bejson.com/try_run",
            params=params,
            headers=self.headers,
            data=data
        )
        token = json.loads(res.text)['token']
        return token

    def getResult(self,token):
        params = {
            "action": "get_result",
            "token": token
        }
        while True:
            res = requests.get(
                "https://runcode.bejson.com/try_run",
                headers=self.headers,
                params=params
            )
            result = json.loads(res.text)
            if result['status']['description'] == 'Accepted':
                break
        return result

    def runCode(self,languge,code):
        token = self.getToken(code,languge)
        results = self.getResult(token)
        return str(base64.b64decode(results['stdout']))[2:-1]

    def run(self,languge,code):
        if languge in self.langdict:
            langid = self.langdict[languge]
            return self.runCode(langid,code)
        else:
            raise ValueError('不存在的语言')

run = BejsonRun()
print(run.runCode(languge=71,code='print(666)'))