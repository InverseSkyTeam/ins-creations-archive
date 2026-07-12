# Xes云变量
# 作者:何嘉晨
import sys
import json
try:
    import websocket
except:
    raise ImportError("您未安装websocket-client库")

class XesCloud:
    def __init__(self,name,p="20547605"):
        """
        :param name:Variable Name
        """
        self.p = str(p)
        if isinstance(name,str):
            self.name = name
        else:
            raise TypeError("变量名只能用字符串")

    def getCookies(self):
        cookies = ""
        if len(sys.argv) > 1:
            try:
                cookies = json.loads(sys.argv[1])["cookies"]
            except:
                print("未登录")
                sys.exit(0)
        return cookies

    def getID(self):
        cookie = self.getCookies()
        id = ''
        for i in cookie.split(";"):
            id = i[8:] if i[1:7] == "stu_id" else id
        return id

    def open(self) -> None:
        self.ws = websocket.create_connection(f'wss://api.xueersi.com/codecloudvariable/ws:80',timeout=10)

    def close(self) -> None:
        try:
            self.ws.close()
        except NameError:
            raise Exception("连接不存在,您没有建立过连接,请使用open函数建立连接\neg.\ncloud=XesCloud('num')\ncloud.open()")

    def create(self) -> None:
        self.open()
        message = {
            "method": "create",
            "user": str(self.getID()),
            "project_id": self.p,
            "name": "☁ "+self.name,
            "value": 0
        }
        try:
            self.ws.send(json.dumps(message))
            self.close()
        except NameError:
            raise Exception("连接不存在,您没有建立过连接,请使用open函数建立连接\neg.\ncloud=XesCloud('num')\ncloud.open()")

    def remove(self) -> None:
        self.open()
        message = {
            "method": "delete",
            "name": "☁ "+self.name,
            "project_id": self.p,
            "user": str(self.getID())
            }
        try:
            self.ws.send(json.dumps(message))
            self.close()
        except NameError:
            raise Exception("连接不存在,您没有建立过连接,请使用open函数建立连接\neg.\ncloud=XesCloud('num')\ncloud.open()")

    def write(self,value) -> None:
        self.open()
        """
        :param value:Value
        """
        message = {
            "method":"set",
            "user":str(self.getID()),
            "project_id":self.p,
            "name":"☁ "+self.name,
            "value":value
        }
        try:
            self.ws.send(json.dumps(message))
        except NameError:
            raise Exception("连接不存在,您没有建立过连接,请使用open函数建立连接\neg.\ncloud=XesCloud('num')\ncloud.open()")
        self.close()

    def read(self) -> int:
        self.open()
        message = {"method": "handshake",
            "user": str(self.getID()),
            "project_id": self.p
        }
        dic = {}
        try:
            while True:
                self.ws.send(json.dumps(message))
                r = self.ws.recv()
                value = str(json.loads(r)['value'])
                name = str(json.loads(r)['name'])
                if name in dic:
                    break
                dic[name] = value
            try:
                self.close()
                return int(dic["☁ "+self.name])
            except:
                raise Exception("变量不存在")
        except NameError:
            raise Exception("连接不存在,您没有建立过连接,请使用open函数建立连接\neg.\ncloud=XesCloud('num')\ncloud.open()")
    def readAll(self) -> dict:
        self.open()
        message = {"method": "handshake",
           "user": str(self.getID()),
           "project_id": self.p
        }
        dic = {}
        try:
            while True:
                self.ws.send(json.dumps(message))
                r = self.ws.recv()
                value = str(json.loads(r)['value'])
                name = str(json.loads(r)['name'])
                if name in dic:
                    break
                dic[name] = value
            try:
                self.close()
                return dic
            except:
                raise Exception("变量不存在")
        except NameError:
            raise Exception("连接不存在,您没有建立过连接,请使用open函数建立连接\neg.\ncloud=XesCloud('num')\ncloud.open()")
"""
调用示例
cloud = XesCloud("num")
cloud.open()
cloud.create()
cloud.write(122334)
cloud.read()
cloud.close()
"""