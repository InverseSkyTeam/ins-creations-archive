import json
from random import randint
from time import time
try:
    import websocket
except:
    raise ImportError("您未安装websocket-client库")

class CloudVar:
    def __init__(self,user_id:str=f"player{randint(1,10)}{randint(1,10)}{randint(1,10)}{randint(1,10)}",project_id:str="p4-@作品.sb3"):
        """
        
        云变量,基于wss://clouddata.turbowarp.org
        
        :param name -> Variable Name
        :param user_id -> the ID of user
        :param project_id -> the name of the project
        """
        self.user_id = user_id
        self.project_id = project_id

    def open(self) -> None:
        """
        建立连接
        """
        self.ws = websocket.create_connection(f'wss://clouddata.turbowarp.org',timeout=10)

    def close(self) -> None:
        try:
            self.ws.close()
        except NameError:
            raise Exception("连接不存在,您没有建立过连接,请使用open函数建立连接。")

    def create(self,name) -> None:
        """
        创建云变量
        此方法无任何用处，等同于set
        """
        message = {
            "method": "create",
            "user": self.user_id,
            "project_id": self.project_id,
            "name": "☁ "+name,
            "value": 0
        }
        try:
            self.ws.send(json.dumps(message))
        except NameError:
            raise Exception("连接不存在,您没有建立过连接,请使用open函数建立连接。")

    def remove(self,name) -> None:
        """
        删除变量
        """
        message = {
            "method": "delete",
            "name": "☁ "+name,
            "project_id": self.project_id,
            "user": self.user_id
        }
        try:
            self.ws.send(json.dumps(message))
        except NameError:
            raise Exception("连接不存在,您没有建立过连接,请使用open函数建立连接。")

    def write(self,name,value) -> None:
        """
        往变量中写入值
        :param value -> Value
        """
        message = {
            "method":"set",
            "user":self.user_id,
            "project_id":self.project_id,
            "name":"☁ "+name,
            "value":value
        }
        try:
            self.ws.send(json.dumps(message))
        except NameError:
            raise Exception("连接不存在,您没有建立过连接,请使用open函数建立连接。")
        # self.close()

    def read(self,name) -> int:
        """
        读取变量
        """
        message = {"method": "handshake",
            "user": self.user_id,
            "project_id": self.project_id
        }
        try:
            self.ws.send(json.dumps(message))
            r = self.ws.recv().split("\n")
            for i in r:
                try:
                    _name = json.loads(i)["name"]
                    value = json.loads(i)["value"]
                    if _name == name:
                        break
                except:
                    continue
            try:
                return value
            except:
                raise Exception("变量不存在")
        except NameError:
            raise Exception("连接不存在,您没有建立过连接,请使用open函数建立连接。")
    def readAll(self) -> dict:
        message = {"method": "handshake",
            "user": self.user_id,
            "project_id": self.project_id
        }
        self.ws.send(json.dumps(message))
        return self.ws.recv().split("\n")


var = CloudVar()
var.open()
t = time()
value = var.read("2333")
print(f"read用时:{time()-t}秒")
i = ""
lst = []
while value:
    i=value[0]
    lst.append(chr(int(value[1:int(i)+1])))
    value=value[int(i)+1:]
print("".join(lst))
var.close()