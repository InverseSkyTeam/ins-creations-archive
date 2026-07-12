"""
待开发
"""
from kernel.ranking import *

class User():
    def __init__(self,cloudid:Union[str,int],userid:Union[str,int]) -> None:
        self.cloudid = str(cloudid)
        self.userid = str(userid)
        self.user = None

    def open(self,user:int) -> None:
        if self.user:
            raise Exception('存在未关闭的连接')
        else:
            self.user = user
            
    def close(self) -> None:
        if self.user:
            self.user = None
        else:
            raise Exception('没有已开启的连接')

    def setUserData(self,data:Union[str,int]):
        pass