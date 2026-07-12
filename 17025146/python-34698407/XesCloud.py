import json,sys
'''
请先安装websocket-client库,不是websocket
'''
#爬cookie
try:
    import websocket
except:
    raise ImportError("您未安装websocket-client库")
def get_cookies():
    cookies = ""
    if len(sys.argv) > 1:
        try:
            cookies = json.loads(sys.argv[1])["cookies"]
        except:
            print("未登录")
            sys.exit(0)
    return cookies


#爬取你的id
def get_id():
    cookie = get_cookies()
    id = ''
    for i in cookie.split(";"):
        id = i[8:] if i[1:7] == "stu_id" else id
    return id
class XesCloud:
    def __init__(self,name):
        """
        :param name:Variable Name
        """
        if isinstance(name,str):
            self.name = name
        else:
            raise TypeError("变量名只能用字符串")
    def open(self) -> None:
        self.ws = websocket.create_connection(f'wss://api.xueersi.com/codecloudvariable/ws:80',timeout=10)
    def close(self) -> None:
        try:
            self.ws.close()
        except NameError:
            raise Exception("连接不存在,您没有建立过连接,请使用open函数建立连接\neg.\ncloud=XesCloud('num')\ncloud.open()")
    def create(self) -> None:
        message = {
            "method": "create",
            "user": str(get_id()),
            "project_id": "20547605",
            "name": "☁ "+self.name,
            "value": 0
        }
        try:
            self.ws.send(json.dumps(message))
        except NameError:
            raise Exception("连接不存在,您没有建立过连接,请使用open函数建立连接\neg.\ncloud=XesCloud('num')\ncloud.open()")
    def remove(self) -> None:
        message = {
            "method": "delete",
            "name": "☁ "+self.name,
            "project_id": "20547605",
            "user": str(get_id())
        }
        try:
            self.ws.send(json.dumps(message))
        except NameError:
            raise Exception("连接不存在,您没有建立过连接,请使用open函数建立连接\neg.\ncloud=XesCloud('num')\ncloud.open()")
    def write(self,value) -> None:
        """
        :param value:Value
        """
        message = {
            "method":"set",
            "user":str(get_id()),
            "project_id":"20547605",
            "name":"☁ "+self.name,
            "value":value
        }
        try:
            self.ws.send(json.dumps(message))
        except NameError:
            raise Exception("连接不存在,您没有建立过连接,请使用open函数建立连接\neg.\ncloud=XesCloud('num')\ncloud.open()")
        self.close()

    def read(self) -> int:
        self.ws = websocket.create_connection(f'wss://api.xueersi.com/codecloudvariable/ws:80',timeout=10)
        message = {"method": "handshake", 
            "user": str(get_id()),
            "project_id": "20547605"
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
                return int(dic["☁ "+self.name])
            except:
                raise Exception("变量不存在")
        except NameError:
            raise Exception("连接不存在,您没有建立过连接,请使用open函数建立连接\neg.\ncloud=XesCloud('num')\ncloud.open()")