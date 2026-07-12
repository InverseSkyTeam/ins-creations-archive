# cloudlib
from xes import uploader
import requests
import json
import re
from xes.common import getCookies as get_cookies

try:
    import websocket
except:
    print('您还未安装websocket-client库，请手动安装')

def find_url(string):
    return re.findall('(https?://[ -~]+)', string)

def get_id(cookie=get_cookies()):
    uid = ''
    for i in cookie.split(";"):
        uid = i[8:] if i[1:7] == "stu_id" else uid
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

def save_to_cloud(name,content,userid,project_id):
    try:
        with open(name + ".txt", "w", encoding="utf-8") as f:
            f.write(str(content))
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
    
def read_from_cloud(filename,userid,to_get='file',project_id=114514):
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
    head1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'}
    zh = nr
    response = requests.get("https://livefile.xesimg.com/programme/python_assets/" + zh + ".txt",
                            headers=head1).content
    nrs = response.decode("utf-8")
    return "".join(nrs.split("\r"))
def get_name(id=get_id()):
    return requests.get(f"https://code.xueersi.com/api/space/profile?user_id={id}",headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'}).json()["data"]["realname"]
def get_profile(path,id=get_id(get_cookies())):
    profile = requests.get(f"https://code.xueersi.com/api/space/profile?user_id={id}",headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'}).json()["data"]["avatar_path"]
    scheme = profile.split(".")[-1]
    with open(path+"/profile."+scheme,"wb") as f:
        f.write(requests.get(profile,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'}).content)
    f.close()
    return scheme