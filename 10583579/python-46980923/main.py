# cloudlib
from xes import uploader
import requests
import json
import sys
import re
from xes.common import getCookies as get_cookies
import time

try:
    import websocket
except:
    print('您还未安装websocket-client库\n1.自动安装(需要安装过pip,不然不行)\n2.手动安装\n输入编号:')
    if input() == "1":
        check_output([sys.executable, "-m", "pip", "install", "websocket-client","-i","https://pypi.tuna.tsinghua.edu.cn/simple"])
    else:
        sys.exit()
    import websocket

def find_url(string):
    return re.findall('(https?://[ -~]+)', string)

def get_id(cookie):
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

def save_to_cloud(name,content,userid,project_id=20619483):
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
    head1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'}
    zh = nr
    response = requests.get("https://livefile.xesimg.com/programme/python_assets/" + zh + ".txt",
                            headers=head1).content
    nrs = response.decode("utf-8")
    return "".join(nrs.split("\r"))
def get_name(id=get_id(get_cookies())):
    return requests.get(f"https://code.xueersi.com/api/space/profile?user_id={id}",headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'}).json()["data"]["realname"]
def get_profile(path,id=get_id(get_cookies())):
    profile = requests.get(f"https://code.xueersi.com/api/space/profile?user_id={id}",headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'}).json()["data"]["avatar_path"]
    scheme = profile.split(".")[-1]
    with open(path+"/profile."+scheme,"wb") as f:
        f.write(requests.get(profile,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'}).content)
    f.close()
    return scheme

# 测速
p = 23266327

# 测试内容
dic = {
    "1":"11451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810",
    "2":"11451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810",
    "3":"11451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810",
    "4":"11451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810",
    "5":"11451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810114514191981011451419198101145141919810"
}
t = time.time()
save_to_cloud("dic",json.dumps(dic),114514,p)
print("单个字典储存",time.time()-t)

p1 = 23266293
t = time.time()
for i in range(1,6):
    save_to_cloud(str(i),dic[str(i)],114514,p1)
print("多个变量储存",time.time()-t)

t = time.time()
save_to_cloud(str(1),dic[str(1)],114514,p1)
print("单个变量储存",time.time()-t)

t = time.time()
read_from_cloud("dic",114514,"file",p)
print("单个字典读取",time.time()-t)

t = time.time()
for i in range(1,6):
    read_from_cloud(str(i),114514,"file",p1)
print("多个变量读取",time.time()-t)

t = time.time()
read_from_cloud(str(1),114514,"file",p1)
print("单个变量读取",time.time()-t)