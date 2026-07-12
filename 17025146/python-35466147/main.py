from typing import Optional,Union
import requests
import json
import base64

class DooccnRun():
    def __init__(self, headers:Optional[dict] = None,langdict:Optional[dict] = None) -> None:
        if headers:
            self.headers= headers
        else:
            self.headers = {
                "Accept": "*/*",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                "Connection": "keep-alive",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Origin": "https://www.dooccn.com",
                "Referer": "https://www.dooccn.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62",
                "sec-ch-ua": "\" Not;A Brand\";v=\"99\", \"Microsoft Edge\";v=\"103\", \"Chromium\";v=\"103\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\""
            }
        if langdict:
            self.langdict = langdict
        else:
            self.langdict = {
                "php5.3":15,
                "php5.4":16,
                "php5.5":3,
                "php5.6":17,
                "php7":18,
                "php7.4":37,
                "python2.7":19,
                "python3":20,
                "csharp":10,
                "c#":10,
                "fsharp":22,
                "f#":22,
                "java1.7":8,
                "java1.8":23,
                "shell":11,
                "c":7,
                "cpp":7,
                "c++":7,
                "nasm":24,
                "go":6,
                "golang":6,
                "lua":25,
                "perl":14,
                "ruby":1,
                "nodejs":4,
                "node.js":4,
                "node":4,
                "objective-c":12,
                "swift":21,
                "erlang":26,
                "rust":27,
                "r":28,
                "scala":5,
                "hackell":29,
                "d":30,
                "clojure":2,
                "groovy":31,
                "lisp":32,
                "ocaml":33,
                "coffeescript":34,
                "coffee":34,
                "racket":35,
                "nim":36
            }

    def runCode(self,languge:int,code:str) -> dict:
        code = str(base64.b64encode(code.encode('utf-8')))[2:-1]
        data = {
            "language": str(languge),
            "code": code,
            "stdin": "123\nhaha2\n"
        }
        res = requests.post(
            "https://runcode-api2-ng.dooccn.com/compile2",
            headers=self.headers,
            data=data
        )
        returndata = json.loads(res.text)
        return returndata

    def getLangID(self,lang:str) -> int:
        lang = lang.lower()
        if lang in self.langdict:
            return self.langdict[lang]
        else:
            raise ValueError('不存在的语言')

    def run(self,languge:str,code:str) -> dict:
        langid = self.getLangID(languge)
        return self.runCode(langid,code)

class RunoobRun():
    def __init__(self,headers:Optional[dict] = None,langdict:Optional[dict] = None) -> None:
        if headers:
            self.headers = headers
        else:
            self.headers = {
                "Accept": "*/*",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                "Connection": "keep-alive",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Origin": "https://c.runoob.com",
                "Referer": "https://c.runoob.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62",
                "sec-ch-ua": "\" Not;A Brand\";v=\"99\", \"Microsoft Edge\";v=\"103\", \"Chromium\";v=\"103\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\""
            }
        if langdict:
            self.langdict = langdict
        else:
            pass

    def runCode(self,languge:int,code:str,fileext:str) -> dict:
        data = {
            "code": code,
            "token": "4381fe197827ec87cbac9552f14ec62a",
            "stdin": "",
            "language": str(languge),
            "fileext": fileext
        }
        res = requests.post(
            "https://tool.runoob.com/compile2.php",
            headers=self.headers,
            data=data)
        return json.loads(res.text)

    def run(self,languge:str,code:str) -> dict:
        langid = self.langdict[languge][0]
        langext = self.langdict[languge][1]
        return self.runCode(langid,code,langext)

class BejsonRun():
    def __init__(self,headers:Optional[dict] = None,langdict:Optional[dict] = None) -> None:
        if headers:
            self.headers = headers
        else:
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
        if langdict:
            self.langdict = langdict
        else:
            pass

    def getToken(self,code:str,languge:int) -> str:
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

    def getResult(self,token:str) -> dict:
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

    def runCode(self,languge:int,code:str) -> dict:
        token = self.getToken(code,languge)
        results = self.getResult(token)
        return results

    def run(self,languge:str,code:str) -> dict:
        if languge in self.langdict:
            langid = self.langdict[languge]
            return self.runCode(langid,code)
        else:
            raise ValueError('不存在的语言')
    