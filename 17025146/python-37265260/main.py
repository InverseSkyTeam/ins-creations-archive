import time
import websocket
from formater import *
import json
from cloudvar import *


def get_all(userid:int,workid:int):
    message = {"method": "handshake",
        "user": userid,
        "project_id": workid
        }
    ws = websocket.create_connection(f'wss://api.xueersi.com/codecloudvariable/ws:80',timeout=10)
    valuedict = {}
    while True:
        ws.send(json.dumps(message))
        r = ws.recv()
        value = str(json.loads(r)['value'])
        name = str(json.loads(r)['name']).replace("☁ ","")
        if name in valuedict:
            break
        valuedict[name] = value
    ws.close()
    return valuedict

def get_user_data(all_user:dict,user:str) -> dict:
    xy = all_user[user + "-position"]
    rgb = all_user[user + "-color"]
    is_win = all_user[user + "-win"]
    return [xy,rgb,is_win]

def get_all_user_data(userid:int,workid:int) -> list:
    target = {}
    alluser = get_all(userid,workid)
    for i in alluser:
        if i.endswith("-position"):
            name = i.strip("-position")
        elif i.endswith("-color"):
            name = i.strip("-color")
        elif i.endswith("-win"):
            name = i.strip("-win")
        else:
            pass
        target[name] = get_user_data(alluser,name)
    return int2list(target)

def setdata(userid:int,workid: int,data:list) -> None:
    data = list2int(data)
    ws = websocket.create_connection(f'wss://api.xueersi.com/codecloudvariable/ws:80',timeout=10)
    for i in data:
        message1 = {
            "method": "set",
            "user": userid,
            "project_id": workid,
            "name": "☁ " + f"{i}-position",
            "value": data[i][0]
            }
        message2 = {
            "method": "set",
            "user": userid,
            "project_id": workid,
            "name": "☁ " + f"{i}-color",
            "value": data[i][1]
        }
        message3 = {
            "method": "set",
            "user": userid,
            "project_id": workid,
            "name": "☁ " + f"{i}-win",
            "value": data[i][2]
        }
        msglist = [message1,message2,message3]
        for k in msglist:
            ws.send(json.dumps(k))
    ws.close()

def set_online(userid:int,workid:int,user:str) -> None:
    var = CloudVar(workid,userid)
    var.open(f"{user}-online")
    var.write(time.time())
    var.close()

def get_online(workid:int,userid:int) -> list:
    userlist = []
    var = CloudVar(workid, userid)
    var.open("xxx")
    alluser = var.readAll()
    for i in alluser:
        if time.time() - float(alluser[i]) == 2.5:
            userlist.append(i)
    var.close()
    return userlist


"""
测试用例
读写的速度略有差异,但基本稳定在0.5s以下,速度很快了.
"""
if __name__ == "__main__":
    """
    # 读写操作
    userid = 0
    workid = 0
    # 此处的data为测试数据,完全按照游戏的数据结构来
    data = [
        ['1', [1, 1], (1, 1, 1), '1'], 
        ['7', [7, 7], (7, 7, 7), '7'], 
        ['2', [2, 2], (2, 2, 2), '2'], 
        ['5', [5, 5], (5, 5, 5), '5'], 
        ['0', [0, 0], (0, 0, 0), '0'], 
        ['6', [6, 6], (6, 6, 6), '6'], 
        ['3', [3, 3], (3, 3, 3), '3'], 
        ['4', [4, 4], (4, 4, 4), '4']
        ]
    import time
    t1 = time.time()
    setdata(userid,workid,data)
    t2 = time.time()
    print(t2 - t1)
    t3 = time.time()
    data = get_all_user_data(userid,workid)
    t4 = time.time()
    print(t4 - t3)
    """