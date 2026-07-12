info = '''本作品为#ICTVAR SERVER 6的客户端
网址：https://code.xueersi.com/scratch3/index.html?pid=22168235&version=3.0&env=community
本作品尝试小轩研制的新云方法：置换存储
同时废除了每次重新链接的臃肿的麻烦'''

import websocket
import json

class CloudVar(object):
    def __init__(self,spaceid,userid):
        self.spaceid = str(spaceid)
        self.userid = str(userid)
        self.is_connect = False
        self.ws = None
        self.postto = 'wss://api.xueersi.com/codecloudvariable/ws:90'
    
    def connect(self):
        self.ws = websocket.create_connection(self.postto,timeout=5)
        self.is_connect = True
    
    def close(self):
        self.ws.close()
        self.is_connect = False
    
    def send(self,data):
        self.ws.send(json.dumps(data))
    
    def recv(self):
        return json.loads(self.ws.recv())
    
    def save(self,index,msg):
        if index > 100000:     # 可用变量数限制在10万以内
            raise Exception('index is too large.\nindexes must in range[0-100000]')
        data = {
            'method': 'set',
            'name': str(msg),
            'user': self.userid,
            'project_id': self.spaceid,
            'value': str(index),
        }
        self.send(data)
    
    def read(self):
        data = {
            'method': 'handshake',
            'user': self.userid,
            'project_id': self.spaceid,
        }
        resultdict = {}
        while True:
            self.send(data)
            result = self.recv()
            if result['method'] == 'set':
                msg = str(result['name'])
                index = int(result['value'])
                if index in resultdict:
                    if resultdict[index][-1] == msg:
                        break
                    resultdict[index].append(msg)
                else:
                    resultdict[index] = [msg]
        return resultdict



import time
pid = 22168480    # 云六号服务器id，云六号你辛苦了
uid = 10000000    # id=10000000的用户，你辛苦了
cloud = CloudVar(pid,uid)
cloud.connect()

tb = time.time()
for i in range(101):  # 改变者千万不要让数据大于500！否则你的运行会很慢。
    cloud.save(i,'这是第'+str(i)+'号消息')
r = cloud.read()
te = time.time()

rl = []
for i,j in r.items():
    print(i,j)
    rl.append(i)
rl.sort()
print(rl)
print('众神归位','逆天云翼计划成功。云六号正常运行。自我感觉良好。联机毫无压力。',sep='\n')
print('100次云上的存入+读取总时间:',round(te-tb,6))


cloud.close()   # 第一次发布忘了关闭节省资源。