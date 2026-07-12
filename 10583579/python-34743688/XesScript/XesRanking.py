# Xes排行榜
# 作者:何嘉晨
from .XesCloud import *
from typing import Union
import json
import sys
import requests
class XesRanking:
    def __init__(self,id=Union[str,int]):
        self.client = self.__getUserName()
        self.id = str(id)
        self.cloud = XesCloud(self.client,self.id)
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.52"}
        try:
            self.last_score = self.cloud.read()
        except:
            self.cloud.create()
    def setScore(self,value) -> None:
        """
        :param value:the value you want to set
        :return: None
        """
        self.cloud.write(value)
    def startMenu(self) -> str:
        dic = self.cloud.readAll()
        rank = sorted(dic.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
        text = ""
        index = 0
        for k,v in rank:
            index += 1
            text = text + str(index) + "\r" + k + "\r" + v + "\n" if index >= 10 else text + "0" + str(index) + "\r" + k + "\r" + v + "\n"
        return text
    def __getUserName(self) -> str:
        cookies = ""
        if len(sys.argv) > 1:
            try:
                cookies = json.loads(sys.argv[1])["cookies"]
            except:
                print("未登录")
                sys.exit(0)
        for i in cookie.split(";"):
            id = i[8:] if i[1:7] == "stu_id" else id
        username = requests.get(f"https://code.xueersi.com/api/space/profile?user_id={id}",headers=self.headers).json()["data"]["realname"]
        return username
"""
调用示例
rank = XesRanking(10583579)
rank.setScore(111)
rank.StartMenu()
"""