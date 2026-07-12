import tkinter as tk
from tkinter import ttk,filedialog
import websocket
import requests
import re
import json
import hashlib
import os
import sys
import random
from PIL import Image,ImageTk
from time import localtime,strftime
from ctypes import windll
import webbrowser

appellation = [("",""),(r"\粗\红C红\\浅红a浅红\\橙r橙\\黄r黄\\绿r绿\\浅绿r浅绿\\浅蓝r浅蓝\\青r青\\蓝r蓝\\纯蓝r纯蓝\\粉r粉\\紫r紫\r\灰1r灰1\\灰2r灰2\\紫r紫\\粉r粉\\纯蓝r纯蓝\\蓝r蓝\\青r青\\浅蓝r浅蓝\\浅绿r浅绿\\绿r绿\\黄r黄\\橙r橙\\红y红\\黄全场≈▶黄\粗\ "," \\黄\\粗≈▶节奏黄\\粗\\"),("\\黄\\粗【编程王者】粗\\黄\\[","]"),(r"\浅红1浅红\\红2红\\黄3黄\\橙4橙\\浅绿5浅绿\\绿6绿\\浅蓝7浅蓝\\青8青\\蓝9蓝\\蓝8蓝\\粉7粉\\紫6紫\\浅蓝5浅蓝\\浅绿4浅绿\\黄3黄\\浅红2浅红\\粉1粉\ ≈▶ ","≈▶"),(r"\粗\浅红【浅红\\浅绿社区浅绿\\浅红】浅红\粗\\黄元老黄\[","]"),(r"\浅蓝高手浅蓝\[","]"),(r"\粉极客粉\[","]"),("\\粗\\浅绿666666浅绿\\粗\\[","]\\粗\\浅绿666666浅绿\\粗\\")]
THE_NUMBER_OF_APPELLATION = len(appellation)
WIDTH,HEIGHT=windll.user32.GetSystemMetrics(0),windll.user32.GetSystemMetrics(1)

def upload(filepath):
    filepath = absolutePath = os.getcwd() + "/" + filepath
    md5 = None
    contents = None
    if os.path.isfile(filepath):
        fp = open(filepath, 'rb')
        contents = fp.read()
        fp.close()
        md5 = hashlib.md5(contents).hexdigest()
    if md5 is None or contents is None:
        raise Exception("文件不存在")
    url = 'https://code.xueersi.com/api/assets/get_oss_upload_params'
    params = {"scene": "offline_python_assets", "md5": md5, "filename": filepath}
    response = requests.get(url=url, params=params)
    uploadParams = json.loads(response.text)['data']
    requests.request(method="PUT", url=uploadParams['host'], data=contents, headers=uploadParams['headers'])
    return uploadParams['url']
def save_to_cloud(name, content, userid, project_id = 23266215,mode = 0):
    with open(name + ".txt", "w", encoding="utf-8") as f:
        f.write(str(content))
    f.close()
    ws = websocket.create_connection('wss://api.xueersi.com/codecloudvariable/ws:80', timeout=5)
    if mode:
        msg = {
            "method": "set",
            "user": userid,
            "project_id": project_id,
            "name": "☁ " + name,
            "value": content
        }
        ws.send(json.dumps(msg))
    else:
        hashtext = upload(name + ".txt").replace("https://livefile.xesimg.com/programme/python_assets/","").replace(".txt", "")
        os.remove(name + ".txt")
        textArr = re.findall('.{' + str(8) + '}', hashtext)
        textArr.append(hashtext[(len(textArr) * 8):])
        xlist = textArr[0:-1] if len(hashtext) % 8 == 0 else textArr
        for i in range(4):
            msg = {
                "method": "set",
                "user": userid,
                "project_id": project_id,
                "name": "☁ " + name + str(i + 1),
                "value": int(xlist[i], 16)
            }
            ws.send(json.dumps(msg))
    ws.close()
def read_from_cloud(name,userid,project_id=20619483,mode = 0):
    message = {
        "method": "handshake",
        "user": str(userid),
        "project_id": str(project_id)
    }
    ws = websocket.create_connection(f'wss://api.xueersi.com/codecloudvariable/ws:80', timeout=5)
    dic = {}
    while True:
        ws.send(json.dumps(message))
        r = ws.recv()
        try:
            value = str(json.loads(r)['value'])
        except:
            continue
        name = str(json.loads(r)['name'])
        if name in dic:
            break
        dic[name] = value
    if mode:
        return dic[name]
    value1 = dic[f"☁ {name}1"]
    value2 = dic[f"☁ {name}2"]
    value3 = dic[f"☁ {name}3"]
    value4 = dic[f"☁ {name}4"]
    vlist = [value1, value2, value3, value4]
    nr = ''
    for i in vlist:
        t = str(hex(int(i)))[2:]
        nr += (8 - len(t)) * '0' + t
    head1 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'}
    zh = nr
    response = requests.get("https://livefile.xesimg.com/programme/python_assets/" + zh + ".txt",
                            headers=head1).content
    nrs = response.decode("utf-8")
    return "".join(nrs.split("\r"))


def get_id():
    cookie = ""
    try:
        cookie = json.loads(sys.argv[1])["cookies"]
    except:
        print("未登录")
        sys.exit(0)
    user_id = ""
    for i in cookie.split(";"):
        user_id = i[8:] if i[1:7] == "stu_id" else user_id
    return user_id
def get_name(uid):
    url = f"https://code.xueersi.com/api/space/profile?user_id={uid}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.52"
        }
    realname = requests.get(url,headers = headers).json()["data"]["realname"]
    return realname

realname = get_name(get_id())

class Group:
    def __init__(self,leader_id:int,project_id = 23266215) -> None:
        # 基本信息
        self.project_id = project_id
        self.leader_id = leader_id
        data = self.read_data()
        self.name = data["name"]
        self.leader_name = data["leader_name"]
        self.admin = data["admin"]
        self.group = data["group"]
        self.prohibition = data["prohibition"]
        self.message = data["message"]
        self.length = self.read_length()

    def is_leader(self,user:int) -> bool:
        return self.leader_id == user

    def add_user(self,user:int) -> bool:
        user_name = get_name(user)
        if user not in self.group:
            self.group[user] = user_name
            return True
        return False
    
    def remove_user(self,user:int) -> bool:
        if user in self.group:
            del self.group[user]
            return True
        return False

    def prohibit_user(self,user:int) -> bool:
        if user not in self.prohibition:
            self.prohibition.append(user)
            return True
        return False
    
    def unprohibit_user(self,user:int) -> bool:
        if user in self.prohibition:
            self.prohibition.remove(user)
            return True
        return False
    
    def is_prohibited(self,user:int) -> bool:
        return (user in self.prohibition)

    def add_admin(self,user:int) -> bool:
        user_name = get_name(user)
        if user not in self.admin:
            self.admin[user] = user_name
            return True
        return False
    
    def remove_admin(self,user:int) -> bool:
        if user in self.admin:
            del self.admin[user]
            return True
        return False
    
    def is_admin(self,user:int) -> bool:
        return (user in self.admin)

    def change_name(self,name:str) -> None:
        self.name = name

    def send_message(self,user_id:int,content:str,_type:str = "text") -> bool:
        # 设置发送消息的条件,备后面用
        condition = True
        if condition:
            msg = {
                "user_id":user_id,
                "user_name":get_name(user_id),
                "type":_type,
                "content":content
            }
            self.message.append(msg)
            return True
        else:
            return False
    
    def save(self) -> None:
        data = {
            "leader_id":self.leader_id,
            "name":self.name,
            "leader_name":self.leader_name,
            "admin":self.admin,
            "group":self.group,
            "prohibition":self.prohibition,
            "message":self.message
        }
        save_to_cloud("data",json.dumps(data),self.leader_id,self.project_id)
        save_to_cloud("length",self.length,self.leader_id,self.project_id,1)

    def read_data(self) -> dict:
        data = json.loads(read_from_cloud("data",self.leader_id,self.project_id))
        return data

    def read_length(self) -> int:
        length = read_from_cloud("length",self.leader_id,self.project_id,1)
        return length

    def get_message(self,data) -> list:
        length = self.read_length()
        if length > self.length:
            return data["message"][:length - self.length]
        else:
            return []
        
    @classmethod
    def create(cls,leader_id:int,project_id = 23266215,name = "新的群聊"):
        admin_name = get_name(leader_id)
        data = {
            "leader_id":leader_id,
            "name":name,
            "leader_name":admin_name,
            "group":{leader_id:admin_name},
            "admin":{leader_id:admin_name},
            "prohibition":[],
            "message":[]
        }
        new = {leader_id:0}
        save_to_cloud("data",json.dumps(data),leader_id,project_id)
        save_to_cloud("length",0,leader_id,project_id,1)
        return cls(leader_id,project_id)

class User:
    def __init__(self,user_id:int,project_id:int = 0) -> None:
        self.project_id = project_id
        self.user_id = user_id
        self.name = get_name(self.user_id)
        data = self.read()
        self.group_list = data["groups"]
        self.friends = []

    def add_group(self,project_id:int,leader_id:int,group_name:str) -> bool:
        if (project_id,leader_id) not in self.group_list:
            self.group_list[(project_id,leader_id)] = [group_name,1]
            return True
        return False

    def remove_group(self,project_id:int,leader_id:int) -> bool:
        if (project_id,leader_id) in self.group_list:
            del self.group_list[(project_id,leader_id)]
            return True
        return False

    def prohibit_group(self,project_id:int,leader_id:int) -> bool:
        if (project_id,leader_id) in self.group_list:
            self.group_list[(project_id,leader_id)][1] = 0
            return True
        return False

    def unprohibit_group(self,project_id:int,leader_id:int) -> bool:
        if (project_id,leader_id) in self.group_list:
            self.group_list[(project_id,leader_id)][1] = 1
            return True
        return False

    def is_prohibited(self,project_id:int,leader_id:int) -> bool:
        return self.group_list[(project_id,leader_id)][1]
    
    def get_admin(self,project_id:int,leader_id:int) -> bool:
        if (project_id,leader_id) in self.group_list:
            self.group_list[(project_id,leader_id)][2] = 1
            return True
        return False
    
    def cancel_admin(self,project_id:int,leader_id:int) -> bool:
        if (project_id,leader_id) in self.group_list:
            self.group_list[(project_id,leader_id)][2] = 0
            return True
        return False
    
    def is_admin(self,project_id:int,leader_id:int) -> bool:
        return self.group_list[(project_id,leader_id)][2]
    
    def change_group_name(self,project_id:int,leader_id:int,name:str) -> bool:
        if (project_id,leader_id) in self.group_list:
            self.group_list[(project_id,leader_id)][0] = name
            return True
        return False
    
    def save(self) -> None:
        # 为以后的更多用户数据做准备
        data = {
            "groups":self.group_list
        }
        save_to_cloud("user_data",json.dumps(data),self.user_id,self.project_id)

    def read(self) -> dict:
        data = read_from_cloud("user_data",self.user_id,self.project_id)
        return data
    
    @classmethod
    def create(cls,user_id:int,project_id:int = 0):
        # 公共群的projcet_id和leader_id(均待定)
        public_project = 0
        public_leader = 0
        data = {
            "groups":{(public_project,public_leader):["公共群",1,0]} # [group_name,is_prohibited,is_admin]
        }
        save_to_cloud("user_data",json.dumps(data),user_id,project_id)
        return cls(user_id,project_id)
        
class UI:
    pass

class Manager:
    def __init__(self,ui:UI) -> None:
        self.ui = ui

class GroupManager(Manager):
    def __init__(self,group:Group) -> None:
        self.group = group

    def add_user(self,user_id) -> bool:
        if self.group.add_user(user_id):
            user = User(user_id)
            return user.add_group(self.group.project_id,self.group.leader_id,self.group.name)

    def remove_user(self,user_id) -> bool:
        if self.group.remove_user(user_id):
            user = User(user_id)
            return user.remove_group(self.group.project_id,self.group.leader_id)

    def prohibit_user(self,user_id) -> bool:
        if self.group.prohibit_user(user_id):
            user = User(user_id)
            return user.prohibit_group(self.group.project_id,self.group.leader_id)
        
    def unprohibit_user(self,user_id) -> bool:
        if self.group.unprohibit_user(user_id):
            user = User(user_id)
            return user.prohibit_group(self.group.project_id,self.group.leader_id)

    def add_admin(self,user_id) -> bool:
        if self.group.add_admin(user_id):
            user = User(user_id)
            return user.get_admin(self.group.project_id,self.group.leader_id)

    def remove_admin(self,user_id) -> bool:
        if self.group.remove_admin(user_id):
            user = User(user_id)
            return user.cancel_admin(self.group.project_id,self.group.leader_id)
        
    def change_name(self,name:str) -> None:
            self.group.change_name(name)
            for user_id in self.group.group:
                user = User(user_id)
                user.change_group_name(self.group.project_id,self.group.leader_id,name)

    def send_message(self,user_id,content,_type = "text") -> bool:
        user = User(user_id)
        if not user.is_prohibited(self.group,user_id):
            return self.group.send_message(user_id,content,_type)

class UserManager(Manager):
    def __init__(self,user:User) -> None:
        self.user = user