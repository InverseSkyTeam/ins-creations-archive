# coding:utf-8
# CloudLibrary Version 1.0 --(clib)
# 制作：吴宇航、何嘉晨
# 辅助：冀厚锦
# 修改：小轩
# 封装：吴宇航、小轩
# 最终版权归逆天团队所有
# 根据AGPL开源协议，本库所有内容改编自吴宇航、何嘉晨的作品
# 附上链接：https://code.xueersi.com/ide/code/34879515(吴宇航-修复版)
# 附上链接：https://code.xueersi.com/ide/code/34697919(何嘉晨-云变量)

from files.lib import uploader
import requests
import json
import sys
import re

try:
    import websocket
except:
    print('您还未安装websocket-client库。正在安装，请稍等...')
    check_output([sys.executable, "-m", "pip", "install", "websocket-client","-i","https://pypi.tuna.tsinghua.edu.cn/simple"])
    import websocket

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
    if uid == '':
        return '12907647'
    return uid

def cutText(text,lenth): 
    textArr = re.findall('.{'+str(lenth)+'}', text) 
    textArr.append(text[(len(textArr)*lenth):]) 
    if len(text) % lenth == 0:
        return textArr[0:-1]
    else:
        return textArr
        
def fillto8(text):
    if len(text) == 8:
        return text
    elif len(text) < 8:
        return (8 - len(text)) * '0' + text

def save_to_cloud(name,content,userid,project_id=20619483):
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
    
def read_from_cloud(filename,userid,to_get='file',project_id=20619483):
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