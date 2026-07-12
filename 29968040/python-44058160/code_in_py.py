import requests,re
import json
class CloudCodeRun():
    '''
    language说明
        python3：15
        python2：0
        c++/c：7
        c#：10
        node.js：4
        Groovy:88
        Assembly:45
        R:80
        VB.NET:84
        TypeslScript:1001
        Kotlin:19
        Pascal:1
        Lua:17
        Go:6
        Swift:16
        RUST:9
        Bash:11
        Perl:14
        Erlang:12
        Scala:5
        Ruby:1
        Java:8
        PHP:3
    fileext说明
         python3：py3
         Python2：py
         c++：cpp
         c：c
         c#：cs
         node.js：node.js
         Groovy:groovy
         Assembly:asm
         R:R
        VB.NET:vb
         TypeslScript:ts
        Kotlin:kt
        Pascal:pas
         Lua:lua
         Go:go
         Swift:swift
         RUST:rs
         Bash:sh
         Perl:pl
         Erlang:erl
        Scala:scala
         Ruby:rb
         Java:java
         PHP:php
    '''
    def __init__(self,language,fileext):
        self.head = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11"}
        self.language = language
        self.fileext = fileext
    def pretreatmentCode(self,precode):
        code=""
        for i in precode:
            if i=="\'":
                code+="\'"
            elif i=="\"":
                code+="\""
            else:
                code+=i
        return code
    def get_token(self):
        u="token = '";d="';";b=re.findall(u+'.*?'+d,requests.get('https://c.runoob.com/compile/12/').text,flags=0);return b[0].replace(u,'').replace(d,'')
    def run(self,code,stdin=""):
        url = "https://tool.runoob.com/compile2.php"
        payload={
            "code": self.pretreatmentCode(code),
            "token": self.get_token(),
            "stdin": stdin,
            "language": self.language,
            "fileext": self.fileext
        }
        r=requests.post(url,headers=self.head,data=payload)
        try:
            r.json()
        except:
            return "token出错，请报告作者"
        if(r.json()!=''):
            #print(r.json()['output'])
            #print(r.json()['errors'])
            return (r.json()['output'],r.json()['errors'])
        else:
            return "数据有误，请按照上边填写数据"