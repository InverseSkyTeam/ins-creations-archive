'''
原版权：
何嘉晨50%
吴宇航30%
冀厚锦13%
小轩7%
(逆天团队 100%)
'''
from files.lib import uploader
import websocket
import requests
import json
import sys

def get_cookies():
    cookies = ""
    if len(sys.argv) > 1:
        try:
            cookies = json.loads(sys.argv[1])["cookies"]
        except:
            cookies = 'uncookie'
    return cookies

def get_id(cookie):
    uid = ''
    if cookie == 'uncookie':
        return '12907647'   # 未登录借用小轩的id
    for i in cookie.split(";"):
        uid = i[8:] if i[1:7] == "stu_id" else uid
    return uid

def save_to_cloud(name,content,userid,project_id=20553603):
    try:
        with open(name + ".txt", "w", encoding="utf-8") as f:
            f.write(content)
        f.close()
        ws = websocket.create_connection('wss://api.xueersi.com/codecloudvariable/ws:80', timeout=5)
        myuploader = uploader.XesUploader()
        hashtext = myuploader.upload(name + ".txt").replace("https://livefile.xesimg.com/programme/python_assets/","").replace(".txt", "")
        for n in range(1, 6):
            c = eval('{"method":"set","user":"' + str(userid) + '","project_id":"'+str(project_id)+'","name":"☁ ' + name + str(n) + '","value"' + ':' + str(n) + str(int(hashtext, 16))[(n - 1) * 8:n * 8] + "}")
            ws.send(json.dumps(c))
        ws.close()
        return True
    except Exception as e:
        print(e)
    return False
    
def read_from_cloud(filename,userid,to_get='file',project_id=20553603):
    message = {
        "method": "handshake",
        "user": str(userid),
        "project_id": str(project_id)
    }
    ws = websocket.create_connection(f'wss://api.xueersi.com/codecloudvariable/ws:80', timeout=30)
    dic = {}
    while True:
        ws.send(json.dumps(message))
        r = ws.recv()
        value = str(json.loads(r)['value'])
        name = str(json.loads(r)['name'])
        if name in dic:
            break
        dic[name] = value
    if to_get == 'dictionary':return dic
    value1 = dic[f"\u2601 {filename}1"][1:]
    value2 = dic[f"\u2601 {filename}2"][1:]
    value3 = dic[f"\u2601 {filename}3"][1:]
    value4 = dic[f"\u2601 {filename}4"][1:]
    value5 = dic[f"\u2601 {filename}5"][1:]
    nr = value1 + value2 + value3 + value4 + value5
    nr = hex(int(nr))[2:]
    head1 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
    }
    zh = nr
    response = requests.get("https://livefile.xesimg.com/programme/python_assets/" + zh + ".txt",
                            headers=head1).content
    nrs = response.decode("utf-8")
    return "".join(nrs.split("\r"))