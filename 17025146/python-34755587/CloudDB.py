import sys
import json
import types
from typing import Optional, Union
import requests
import hashlib
import base64
import os
import time
from Crypto.Cipher import AES
import re
from binascii import b2a_hex, a2b_hex
try:
    import websocket
except:
    raise ImportError("您未安装websocket-client库")
    
class CloudVar():
    def __init__(self,cloudid:int,userid:int):
        """
        :param name:Variable Name
        """
        self.userid = userid
        self.cloudid = cloudid
        self.varname = None

    def open(self,varname:str) -> None:
        if isinstance(varname,str):
            self.varname = varname
        else:
            raise ValueError('变量名必须为字符串')

    def close(self) -> None:
        if self.varname:
            self.varname = None
        else:
            raise Exception('没有已打开的连接')

    def create(self,original:int = 0) -> None:
        if self.varname:
            ws = websocket.create_connection(f'wss://api.xueersi.com/codecloudvariable/ws:80',timeout=10)
            message = {
                "method": "create",
                "user": self.userid,
                "project_id": self.cloudid,
                "name": "☁ "+self.varname,
                "value": original
            }
            ws.send(json.dumps(message))
            ws.close()
        else:
            raise Exception('没有已打开的连接')

    def remove(self) -> None:
        if self.varname:
            ws = websocket.create_connection(f'wss://api.xueersi.com/codecloudvariable/ws:80',timeout=10)
            message = {
                "method": "delete",
                "name": "☁ " + self.varname,
                "project_id": self.cloudid,
                "user": str(self.userid)
            }
            ws.send(json.dumps(message))
            ws.close()
        else:
            raise Exception('没有已打开的连接')

    def write(self,value:int) -> None:
        if self.varname:
            ws = websocket.create_connection(f'wss://api.xueersi.com/codecloudvariable/ws:80',timeout=10)
            """
            :param value:Value
            """
            message = {
                "method": "set",
                "user": str(self.userid),
                "project_id": self.cloudid,
                "name": "☁ " + self.varname,
                "value": value
            }
            ws.send(json.dumps(message))
            ws.close()
        else:
            raise Exception('没有已打开的连接')

    def read(self) -> int:
        if self.varname:    
            ws = websocket.create_connection(f'wss://api.xueersi.com/codecloudvariable/ws:80',timeout=10)
            message = {"method": "handshake",
                "user": str(self.userid),
                "project_id": self.cloudid
                }
            dic = {}
            while True:
                ws.send(json.dumps(message))
                r = ws.recv()
                value = str(json.loads(r)['value'])
                name = str(json.loads(r)['name'])
                if name in dic:
                    break
                dic[name] = value
            ws.close()
            return int(dic["☁ "+self.varname])
        else:
            raise Exception('没有已打开的连接')

    def readAll(self) -> dict:
        if self.varname:
            ws = websocket.create_connection(f'wss://api.xueersi.com/codecloudvariable/ws:80',timeout=10)
            message = {"method": "handshake",
                        "user": str(self.userid),
                        "project_id": self.cloudid
                        }
            dic = {}
            while True:
                ws.send(json.dumps(message))
                r = ws.recv()
                value = str(json.loads(r)['value'])
                name = str(json.loads(r)['name'])
                if name.replace('☁ ','') in dic:
                    break
                dic[name.replace('☁ ','')] = value
            ws.close()
            return dic
        else:
            raise Exception('没有已打开的连接')

class CloudCDN():
    def __init__(self) -> None:
        self.xesurl = 'https://livefile.xesimg.com/programme/python_assets/{}.{}'
        self.ossurl = 'https://xueersifile.oss-cn-beijing.aliyuncs.com/programme/python_assets/{}.{}'
        self.internalurl = 'https://xueersifile.oss-cn-beijing-internal.aliyuncs.com/programme/python_assets/{}.{}'

    def getFileURL(self,hash:str,ext:str,method:int) -> str:
        methoddict = {
            "1":self.xesurl,
            "2":self.ossurl,
            "3":self.internalurl
        }
        url = methoddict[str(method)].format(hash,ext)
        return url

    def getAbs(self,path:str) -> str:
        if os.path.isabs(path):
            return path
        else:
            return os.getcwd() + "/" + path

    def getFileContent(self,file:str) -> bytes:
        if os.path.isfile(file):
            fp = open(file, 'rb')
            contents = fp.read()
            fp.close()
            return contents
        else:
            raise Exception('文件不存在')

    def uploadFile(self, filepath):
        filepath = self.getAbs(filepath)
        contents = self.getFileContent(filepath)
        md5 = hashlib.md5(contents).hexdigest()
        url = 'https://code.xueersi.com/api/assets/get_oss_upload_params'
        params = {"scene": "offline_python_assets", "md5": md5, "filename": filepath}
        response = requests.get(url=url, params=params)
        uploadParams = json.loads(response.text)
        requests.request(method="PUT", url=uploadParams['data']['host'], data=contents, headers=uploadParams['data']['headers'])
        return uploadParams

    def getFileHash(self,filepath:str):
        data = self.uploadFile(filepath)
        data = data['data']['host']
        data = data.split('/')[-1].split('.')[0]
        return data

    def readFile4Hash(self,hash:str,ext:str,method:int) -> bytes:
        """
        :param hash:文件的唯一标识符
        :param ext:文件的后缀
        :param method:读取文件的地址,1为XesCDN,2为AliyunOSS,3为AliyunOSS-Internal
        """
        headers = {
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
        }
        url = self.getFileURL(hash,ext,method)
        data = requests.get(url=url,headers=headers).content
        return data

    def readFile4URL(self,url:str) -> bytes:
        headers = {
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
        }
        data = requests.get(url=url,headers=headers).content
        return data
    
    def saveFile4Hash(self,filename:str,hash:str,ext:str,method:str) -> int:
        try:
            with open(filename,"wb") as file:
                file.write(self.readFile4Hash(hash,ext,method))
            return 1
        except:
            return 0

    def saveFile4URL(self,filename:str,url:str) -> int:
        try:
            with open(filename,"wb") as file:
                file.write(self.readFile4URL(url))
            return 1
        except:
            return 0
            
class IXDB():
    def __init__(self,dbname:str) -> None:
        self.dbname = dbname
        self.db = {}

    def init(self) -> None:
        self.db = {}

    def add(self,method:int,data:Union[list,dict],key:Optional[str] = None) -> None:
        """
        :param method:0为添加一行,1为添加一列
        """
        if method == 1: #添加一列
            ###TODO 这里if嵌套太多了,代码结构不够优雅,以后想到了更好的算法再来修改
            if key:
                if isinstance(data,list):
                    self.db[key] = data
                else:
                    raise Exception('添加一列时,data必须以列表形式呈现')
            else:
                raise Exception('添加一列时,key不能为空')
        elif method == 0: #添加一行
            if isinstance(data,dict):
                for i in self.db:
                    self.db[i].append(data[i])
            else:
                raise Exception("添加一列时,data必须以字典形式呈现")

    def remove(self,method:int,x:Optional[str] = None,y:Optional[int] = None):
        """
        :param method:0为删除一行,1为删除一列
        """
        if method == 1: #删除一列
            if x:
                del self.db[x]
            else:
                raise Exception('当删除一行时,x参数不能为空')
        elif method == 0: #删除一列
            if y:
                for i in self.db:
                    del self.db[i][y]
            else:
                raise Exception('当删除一列时,y参数不能为空')

    def revice(self,value:Union[str,int,float,bool,list,dict],x:Optional[str] = None,y:Optional[int] = None) -> None:
        ### 此处不可使用if x and y
        if x != None and y != None:
            if (not isinstance(value,(dict,list))):
                try:
                    self.db[x][y] = value
                except:
                    raise ValueError('不存在的值')
            else:
                raise Exception('value不能为list或dict')
        elif x != None and y == None:
            if isinstance(value,list):
                try:
                    self.db[x] = value
                except:
                    raise ValueError('不存在的值')
            else:
                raise Exception('value必须为list')
        elif x == None and y != None:
            if isinstance(value,dict):
                try:
                    for i in self.db:
                        self.db[i][y] = value[i]
                except:
                    raise ValueError('不存在的值')
            else:
                raise Exception('value必须为dict')

    def query(self,x:Optional[str] = None,y:Optional[int] = None) -> Union[int,str,float,bool]:
        if x != None and y != None:
            try:
                return self.db[x][y]
            except:
                    raise ValueError('不存在的值')
        elif x != None and y == None:
            try:
                return self.db[x]
            except:
                    raise ValueError('不存在的值')
        elif x == None and y != None:
            try:
                target = {}
                for i in self.db:
                    target[i] = self.db[i][y]
                return target
            except:
                    raise ValueError('不存在的值')

    def formatout(self) -> dict:
        data = json.dumps(self.db)
        t = time.time()
        md5 = hashlib.md5(data.encode('utf-8')).hexdigest()
        column = len(self.db.keys())
        line = len(self.db[list(self.db.keys())[0]])
        ixdb = {
            'head':{
                'md5':md5,
                'column':column,
                'line':line
            },
            'body':self.db
        }
        return json.dumps(ixdb)

    def formatin(self,ixdb:str) -> dict:
        return json.loads(ixdb)['body']

    def writeout(self,filename:str) -> None:
        with open(filename,"w") as file:
            file.write(self.formatout())

    def readin(self,filename:str) -> None:
        with open(filename,'r') as file:
            data = file.read()
        self.db = self.formatin(data)
    
    

class CloudDB():
    def __init__(self,cloudid:int,userid:int) -> None:
        """
        :param db:绑定一个IXDB对象
        """
        self.cloudvar = CloudVar(cloudid,userid)
        self.cloudcdn = CloudCDN()
        self.dbname = None
        self.db = None

    def getDBName(self,filename:str):
        with open(filename,'r') as file:
            text = file.read()
        return json.loads(text)['head']['name']

    def cutText(self,text,lenth): 
        textArr = re.findall('.{'+str(lenth)+'}', text) 
        textArr.append(text[(len(textArr)*lenth):]) 
        if len(text) % lenth == 0:
            return textArr[0:-1]
        else:
            return textArr 

    def pull(self):
        self.cloudvar.open("xxx")
        dbdict = self.cloudvar.readAll()
        if self.dbname + '1' in dbdict:
            dbhash = ''
            for i in range(4):
                value = self.cloudvar.readAll()[self.dbname + str(i + 1)]
                dbhash += str(hex(int(value)))[2:]
            self.cloudcdn.saveFile4Hash(f'{self.dbname}.ixdb',dbhash,'ixdb',1)
            self.db = IXDB(self.dbname)
            self.db.readin(f'{self.dbname}.ixdb')
        else:
            raise Exception(f'云端不存在{self.dbname}这个数据库')

    def open(self,dbname:str):
        self.dbname = dbname

    def create(self,original:IXDB) -> int:
        if not self.db:
            self.db = original
            original.writeout(self.dbname + '.ixdb')
            filehash = self.cloudcdn.getFileHash(f'./{self.dbname}.ixdb')
            numlist = []
            for x in self.cutText(filehash,8):
                filenum = int(x,16)
                numlist.append(filenum)
            for i in range(len(numlist)):
                self.cloudvar.open(f'{self.dbname}{i+1}')
                self.cloudvar.create()
                self.cloudvar.write(numlist[i])
            self.cloudvar.close()
        else:
            raise Exception('云端已存在该数据库,无法重复创建')

    def add(self,method:int,data:Union[list,dict],key:Optional[str] = None) -> None:
        if self.db:
            self.db.add(method,data,key)
        else:
            raise Exception('没有已开启的数据库')

    def remove(self,method:int,x:Optional[str],y:Optional[int]) -> None:
        if self.db:
            self.db.remove(method,x,y)
        else:
            raise Exception('没有已开启的数据库')

    def revice(self,value:Union[str,int,float,bool,list,dict],x:Optional[str] = None,y:Optional[int] = None) -> None:
        if self.db:
            self.db.revice(value,x,y)
        else:
            raise Exception('没有已开启的数据库')

    def query(self,x:Optional[str] = None,y:Optional[int] = None) -> Union[int,str,float,bool]:
        if self.db:
            return self.db.query(x,y)
        else:
            raise Exception('没有已开启的数据库')

    def push(self):
        if self.db:
            self.db.writeout(self.dbname + '.ixdb')
            filehash = self.cloudcdn.getFileHash(f'./{self.dbname}.ixdb')
            numlist = []
            for x in self.cutText(filehash,8):
                filenum = int(x,16)
                numlist.append(filenum)
            for i in range(len(numlist)):
                self.cloudvar.open(f'{self.dbname}{i+1}')
                self.cloudvar.create()
                self.cloudvar.write(numlist[i])
            self.cloudvar.close()
        else:
            raise Exception('没有已开启的数据库')

    def read(self):
        if self.db:
            return self.db
        else:
            raise Exception('没有已开启的数据库')

    def write(self,db:IXDB):
        if self.db:
            self.db = db
        else:
            raise Exception('没有已开启的数据库')

    def close(self):
        if self.dbname:
            self.dbname = None
        else:
            raise Exception('没有已建立的连接')