import websocket
import json
import time

def read_all(workid,userid):
    ws = websocket.create_connection(f'wss://api.xueersi.com/codecloudvariable/ws:80',timeout=10)
    message = {"method": "handshake",
                "user": userid,
                "project_id": workid
                }
    dic = {}
    while True:
        ws.send(json.dumps(message))
        r = ws.recv()
        value = json.loads(r)['value']
        name = str(json.loads(r)['name'])
        if name.replace('☁ ','') in dic:
            break
        dic[name.replace('☁ ','')] = value
    ws.close()
    return dic
def write_var(workid,userid,key,value):
    ws = websocket.create_connection(f'wss://api.xueersi.com/codecloudvariable/ws:80',timeout=10)
    message = {
        "method": "set",
        "user": userid,
        "project_id": workid,
        "name": "☁ " + key,
        "value": value
    }
    ws.send(json.dumps(message))
    ws.close()
def read_var(workid,userid,key):
    ws = websocket.create_connection(f'wss://api.xueersi.com/codecloudvariable/ws:80',timeout=10)
    message = {"method": "handshake",
        "user": userid,
        "project_id": workid
        }
    while True:
        ws.send(json.dumps(message))
        r = ws.recv()
        value = json.loads(r)['value']
        name = str(json.loads(r)['name'])
        if name == key:
            break
    ws.close()
    return value
def write(workid,userid,key,value):
    variables = read_all(workid,userid)
    maxindex = max(list(variables.values())) if variables else -1 # 取最大值
    index = maxindex + 1 # 得到当前索引
    write_var(workid,userid,key,index)
    write_var(workid,userid,value,index)
    
def read(workid,userid,key):
    variables = read_all(workid,userid) # 读取所有变量
    index = variables[key]
    del variables[key]
    value = list(variables.keys())[list(variables.values()).index(index)]
    return value
    
userid = 17025146
workid = 22168235
t1 = time.time()
write(workid,userid,"msg","我将这个项目命名为FasterCloud")
t2 = time.time()
value = read(workid,userid,"msg")
t3 = time.time()
print(value)
print("写入用时:",t2 - t1)
print("读取用时:",t3 - t2)