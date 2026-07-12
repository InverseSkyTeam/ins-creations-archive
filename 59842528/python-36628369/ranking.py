from typing import Union
import json
import websocket
import random
from .variable import *

class CloudRanking():
    def __init__(self,cloudid:Union[str,int],rankingname:str) -> None:
        """
        :param rankingname:要开启的排行榜名称,与一个云变量名称对应
        """
        self.name = "☁ " + rankingname
        self.rankingname = rankingname
        self.cloudid = str(cloudid)
        self.userid:Union[int,str] = None

    def open(self,userid:Union[str,int]) -> None:
        if self.userid:
            raise Exception('有未关闭的连接')
        else:
            self.userid = userid

    def close(self) -> None:
        if self.userid:
            self.userid = None
        else:
            raise Exception('没有已开启的连接')

    def setScore(self,value:int) -> None:
        """
        :param value:设置的值
        """
        if self.userid:
            cloudvar = CloudVar(self.cloudid,self.userid)
            cloudvar.open(self.rankingname)
            cloudvar.write(value)
            cloudvar.close()
            msg = {
                'method': "ranking",
                'name': self.name,
                'project_id': str(self.cloudid),
                'user': str(self.userid),
                'value': str(random.randint(10000,99999)) # 随机五位数
            }
            ws = websocket.create_connection(f'wss://api.xueersi.com/codecloudvariable/ws:80',timeout=10)
            ws.send(json.dumps(msg))
            ws.close()
        else:
            raise Exception('没有已开启的连接')

    def readRanking(self) -> dict:
        if self.userid:
            msg = {
                'method': "ranking",
                'name': self.name,
                'project_id': str(self.cloudid),
                'user': str(self.userid),
                'value': str(random.randint(10000,99999)) # 随机五位数
            }
            ws = websocket.create_connection(f'wss://api.xueersi.com/codecloudvariable/ws:80',timeout=10)
            ws.send(json.dumps(msg))
            return json.loads(ws.recv())
        else:
            raise Exception('没有已开启的连接')

    def readUser(self) -> int:
        if self.userid:
            ranklist = self.readRanking()
            return ranklist['my']['value']
        else:
            raise Exception('没有已开启的连接')