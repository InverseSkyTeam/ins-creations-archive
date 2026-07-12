import requests
import json
import websocket
import sys
import re


USER = "29968040"
CLOUD_API = 'wss://api.xueersi.com/codecloudvariable/ws:80'

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' + \
             'Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33'


def get_user_name(user_id) -> str:
    headers = {
        'User-Agent': user_agent,
        'coo'+'kie': ''
    }
    _output = requests.get('https://code.xueersi.com/api/space/profile?user_id=%s' % user_id, headers=headers)
    return json.loads(_output.text)['data']['realname']


def get_coo_kies():
    coo_kies = ""
    if len(sys.argv) > 1:
        try:
            coo_kies = json.loads(sys.argv[1])["coo"+"kies"]
        except:
            print("未登录")
            sys.exit(0)
    return coo_kies


def get_my_id():
    return re.search(r'stu_id=(\d+)', get_coo_kies()).group(1)


class CloudVariable:
    def __init__(self, max_players, project):
        self.ws = None
        self.max_players = max_players
        self.PROJECT = str(project)

        self.init_cloud()

    def open_new_project(self):
        self.open()
        # variables = ws.get_variable_all()
        for index in range(1, self.max_players+1):
            self.send_variable(index, ['0', '0', '0'])
        self.close()

    def init_cloud(self):
        temp_m = {
            "method": "set",
            "user": USER,
            "project_id": self.PROJECT,
            "name": chr(9729) + ' ' + 'temp',
            "value": 0
        }
        self.ws = websocket.create_connection(CLOUD_API, timeout=100)
        self.ws.send(json.dumps(temp_m))
        self.ws.close()

    def open(self):
        self.ws.connect(CLOUD_API)
        # print(objgraph.show_backrefs(self.ws.sock_opt, filename='backrefs_graph.png'))
        # self.ws = websocket.create_connection(CLOUD_API, timeout=100, skip_utf8_validation=True)

    def close(self):
        self.ws.close()

    def get_variable_all(self):
        m2 = {
            "method": "handshake",
            "user": USER,
            "project_id": self.PROJECT
        }
        dic = {}
        while True:
            self.ws.send(json.dumps(m2))
            r = self.ws.recv()
            value = str(json.loads(r)['value'])
            name = str(json.loads(r)['name'])[2:]
            if name in dic:
                break
            dic[name] = value
        return dic

    def get_variable(self):
        m2 = {
            "method": "handshake",
            "user": USER,
            "project_id": self.PROJECT
        }
        dic = {}
        self.ws.send(json.dumps(m2))
        for i in range(self.max_players * 3 + 1):
            r = self.ws.recv()
            value = str(json.loads(r)['value'])
            name = str(json.loads(r)['name'])[2:]
            dic[name] = value
        return dic

    def send_variable(self, player_index, values):
        for i, char in enumerate(('a', 'b', 'c')):
            name = f'P{player_index}_{char}'
            m = {
                "method": "set",
                "user": USER,
                "project_id": self.PROJECT,
                "name": chr(9729) + ' ' + name,
                "value": values[i]
            }
            self.ws.send(json.dumps(m))

    def send_variable_hp(self, player_index, values):
        m = {
            "method": "set",
            "user": USER,
            "project_id": self.PROJECT,
            "name": chr(9729) + ' ' + f'P{player_index}_b',
            "value": values[1]
        }
        self.ws.send(json.dumps(m))
