# coding:utf-8
# CloudLibrary Version 1.4 --(clib)
# 制作：吴宇航、何嘉晨、小轩
# 辅助：冀厚锦
# 最终版权归逆天团队所有
# 贡献链接：https://code.xueersi.com/ide/code/34879515(吴宇航-修复版)
# 贡献链接：https://code.xueersi.com/ide/code/34697919(何嘉晨-云变量)
# 贡献链接：https://code.xueersi.com/ide/code/21663768(王若宇-文链器)

import uploader
import requests
import json
import sys
import re

try:
    import websocket
except:
    print('请您先点击右上角的库管理，搜索websocket-client库并安装，再运行~')

def find_url(string):
    return re.findall('(https?://[ -~]+)', string)

def upfile(f):
    return uploader.XesUploader().uploadAbsolutePath(f)

def get_cookies() -> str:
    cookies = ""
    if len(sys.argv) > 1:
        try:
            cookies = json.loads(sys.argv[1])["cookies"]
        except:
            cookies = 'uncookie'
    return cookies

def get_id(cookie) -> str:
    uid = ''
    if cookie == 'uncookie':
        return '000000'
    for i in cookie.split(";"):
        uid = i[8:] if i[1:7] == "stu_id" else uid
    if uid == '':
        return '000000'
    return uid

def cutText(text,lenth) -> str: 
    textArr = re.findall('.{'+str(lenth)+'}', text) 
    textArr.append(text[(len(textArr)*lenth):]) 
    if len(text) % lenth == 0:
        return textArr[0:-1]
    else:
        return textArr
        
def fillto8(text) -> str:
    if len(text) == 8:
        return text
    elif len(text) < 8:
        return (8 - len(text)) * '0' + text

def save_to_cloud(name,content,userid,project_id=21170915):
    try:
        with open(name + ".txt", "w", encoding="utf-8") as f:
            f.write(content)
        f.close()
        ws = websocket.create_connection('wss://api.xueersi.com/codecloudvariable/ws:80', timeout=5)
        myuploader = uploader.XesUploader()
        hashtext = myuploader.upload(name + ".txt").replace("https://livefile.xesimg.com/programme/python_assets/","").replace(".txt", "")
        xlist = cutText(hashtext,8)
        for i in range(4):
            msg = {
                "method": "set",
                "user": userid,
                "project_id": project_id,
                "name": "☁ " + name + str(i + 1),
                "value": int(xlist[i],16)
            }
            ws.send(json.dumps(msg))
        ws.close()
        return True
    except Exception as e:
        print(e)
    return False
    
def read_from_cloud(filename,userid,to_get='file',project_id=21170915):
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
    value1 = dic[f"☁ {filename}1"]
    value2 = dic[f"☁ {filename}2"]
    value3 = dic[f"☁ {filename}3"]
    value4 = dic[f"☁ {filename}4"]
    vlist = [value1,value2,value3,value4]
    nr = ''
    for i in vlist:
        nr += fillto8(str(hex(int(i)))[2:])
    head1 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
    }
    zh = nr
    response = requests.get("https://livefile.xesimg.com/programme/python_assets/" + zh + ".txt",
                            headers=head1).content
    nrs = response.decode("utf-8")
    return "".join(nrs.split("\r"))