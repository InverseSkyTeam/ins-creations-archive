import requests
import bs4
import time
import json

head={
    "Authorization": "token ",#这里加秘钥
    'Accept': 'application/vnd.github.v3+json',
    'Content-Type': 'application/json'
}
#登录github
login = requests.get("https://api.github.com/user", headers=head)
print(login)
'''
url = 'https://api.github.com/user/repos'
header={
        "Authorization": "token ",#这里加秘钥 
        'Accept': 'application/vnd.github.v3+json',
        'Content-Type': 'application/json',
}
data = json.dumps({"name": "%s" %"Xes_QA"})
r = requests.post(url, data=data, headers=header)
print(r)
'''
import base64

def file_base64(data):
    data_b64 = base64.b64encode(data).decode('utf-8')
    return data_b64
a=file_base64(json.dumps("hello").encode())
data2={
  "message": "无",#备注
  "content": a,#内容要base64编码
}
data2=json.dumps(data2)
url="https://api.github.com/repos/Zixuanyuan/Xes_QA/contents/yzx3.txt"

qw = requests.put(url, data=data2, headers=head)
print(qw)