import websocket
import json

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
            """
            ###此处的create方法失效,直接使用write方法就可以实现创建###
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
            """
            self.write(original)
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