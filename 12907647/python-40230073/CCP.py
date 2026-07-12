# 原创吴宇航
# 感谢副室长吴宇航对逆天团队的巨大贡献。

import requests
import base64
import json

class BejsonRun():
    def __init__(self):
        self.headers = {
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
        self.langdict = {
            'C(GCC 7.4.0)': 48,
            'C(GCC 8.3.0)': 49,
            'C(GCC 9.2.0)': 50,
            'C#(Mono 6.6.0.161)': 51,
            'C++(GCC 7.4.0)': 52,
            'C++(GCC 8.3.0)': 53,
            'C++(GCC 9.2.0)': 54,
            'Python(2.7.17)': 70,
            'Python(3.8.1)': 71,
            'C(Clang 7.0.1)': 75,
            'C++(Clang 7.0.1)': 76,
        }

    def getToken(self,code,languge,stdin):
        params = {
            'action': 'get_token'
        }
        data = {
            'source_code': code,
            'language_id': str(languge),
            'command_line_arguments': '',
            'stdin': stdin
        }
        res = requests.post(
            'https://runcode.bejson.com/try_run',
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
            if result['status']['description'] not in ['In Queue','Processing']:
                break
        return result

    def runCode(self,languge,code,stdin):
        token = self.getToken(code,languge,stdin)
        results = self.getResult(token)
        return results
    
    def translate(self,code):
        return eval(str(base64.b64decode(code))[1:])
    
    def translate_all(self,data,stdin):
        stdout = data['stdout']
        error = data['stderr']
        msg = data['message']
        return {
            'stdin': stdin,
            'stdout': 'Nothing' if not stdout else self.translate(stdout),
            'error': 'Nothing' if not error else self.translate(error),
            'msg': 'Nothing' if not msg else self.translate(msg),
            'state': data['status']['description'],
        }

    def run(self,languge,code,stdin):
        langid = self.langdict[languge]
        jsondata = self.runCode(langid,code,stdin)
        dictdata = self.translate_all(jsondata,stdin)
        return dictdata

if __name__ == '__main__':
    runner = BejsonRun()
    print(runner.run(languge='Python(3.8.1)',code='print(1)',stdin=''))