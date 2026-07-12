import requests
import json
import websocket
import time
import sys
import re


USER = "29968040"
PROJECT = '25150510'


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33'


def get_user_name(user_id, cookie='') -> str:
    headers = {
        'User-Agent': user_agent,
        'cookie': cookie
    }
    if cookie != '':
        _output = requests.get('https://code.xueersi.com/api/space/profile?user_id=%s' % user_id, headers=headers)
    else:
        _output = requests.get('https://code.xueersi.com/api/space/profile?user_id=%s' % user_id, headers=headers)
    return json.loads(_output.text)['data']['realname']


def get_cookies():
    cookies = ""
    if len(sys.argv) > 1:
        try:
            cookies = json.loads(sys.argv[1])["cookies"]
        except:
            print("未登录")
            sys.exit(0)
    return cookies


def get_my_id():
    return re.search(r'stu_id=(\d+)', get_cookies()).group(1)


class CloudVariable:
    def __init__(self):
        self.ws = websocket.create_connection(f'wss://api.xueersi.com/codecloudvariable/ws:80', timeout=30)
        self.ws1 = websocket.create_connection(f'wss://api.xueersi.com/codecloudvariable/ws:80', timeout=30)
        m1 = {
            "method": "set",
            "user": USER,
            "project_id": PROJECT,
            "name": chr(9729) + ' ' + 'temp',
            "value": int(0)
        }
        self.ws1.send(json.dumps(m1))
        self.ws1.close()

    def get_variable(self):
        m2 = {
            "method": "handshake",
            "user": USER,
            "project_id": PROJECT
        }
        dic = {}
        # a = time.time()
        self.ws = websocket.create_connection(f'wss://api.xueersi.com/codecloudvariable/ws:80', timeout=30)
        # c = time.time()
        while True:
            # a1 = time.time()
            self.ws.send(json.dumps(m2))
            r = self.ws.recv()
            # print(time.time() - a1, r)
            value = str(json.loads(r)['value'])
            name = str(json.loads(r)['name'])[2:]
            if name in dic:
                break
            dic[name] = value
        self.ws.close()
        # b = time.time()
        # print('get: ', b-a, b-c, '连接:', c-a)
        return dic

    def send_variable(self, name, value, name1, value1, name2, value2):
        m1 = {
            "method": "set",
            "user": USER,
            "project_id": PROJECT,
            "name": chr(9729) + ' ' + name,
            "value": int(value)
        }
        m2 = {
            "method": "set",
            "user": USER,
            "project_id": PROJECT,
            "name": chr(9729) + ' ' + name1,
            "value": int(value1)
        }
        m3 = {
            "method": "set",
            "user": USER,
            "project_id": PROJECT,
            "name": chr(9729) + ' ' + name2,
            "value": int(value2)
        }
        # a = time.time()
        self.ws1 = websocket.create_connection(f'wss://api.xueersi.com/codecloudvariable/ws:80', timeout=30)
        # c = time.time()
        self.ws1.send(json.dumps(m1))
        self.ws1.send(json.dumps(m2))
        self.ws1.send(json.dumps(m3))
        self.ws1.close()
        # b = time.time()
        # print('send:', b-a, b-c, '连接:', c-a)

    def variable_close(self):
        self.ws.close()
        self.ws1.close()


cloud_variable = CloudVariable()
get_variable = cloud_variable.get_variable
send_variable = cloud_variable.send_variable
variable_close = cloud_variable.variable_close
