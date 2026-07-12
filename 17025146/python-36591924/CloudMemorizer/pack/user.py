from kernel.cdn import CloudCDN
from kernel.ranking import *
import re

class User():
    def __init__(self,cloudid:Union[str,int]) -> None:
        self.cloudid = str(cloudid)
        self.user = None
        self.cloudcdn = CloudCDN()

    def __uploadtext(self,text:str,name:str = "untitled") -> str:
        with open(f"{name}.ctext","w",encoding="utf-8") as file:
            file.write(text)
        filehash = self.cloudcdn.getFileHash(f"./{name}.ctext")
        return filehash


    def __cutText(self,text:str,lenth:int) -> list: 
        textArr = re.findall('.{'+str(lenth)+'}', text) 
        textArr.append(text[(len(textArr)*lenth):]) 
        if len(text) % lenth == 0:
            return textArr[0:-1]
        else:
            return textArr
            
    def __fillto8(self,text:str) -> str:
        if len(text) == 8:
            return text
        elif len(text) < 8:
            return (8 - len(text)) * '0' + text

    def __splithash(self,text:str) -> list:
        textlist = self.__cutText(text,8)
        numlist = []
        for i in textlist:
            numlist.append(int(i,16))
        return numlist

    def __inttohash(self,num:int) -> str:
        hashtxt = str(hex(int(num)))[2:]
        hashtxt = self.__fillto8(hashtxt)
        return hashtxt

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

    def writeInt(self,varname:str,value:int) -> None:
        ranking = CloudRanking(self.cloudid,varname)
        ranking.open(self.user)
        ranking.setScore(value)
        ranking.close()

    def writeText(self,varname:str,text:str) -> None:
        filehash = self.__uploadtext(text)
        hashlist = self.__splithash(filehash)
        for i in range(4):
            var = f'{varname}{i + 1}'
            ranking = CloudRanking(self.cloudid,var)
            ranking.open(self.user)
            ranking.setScore(hashlist[i])
            ranking.close()
        

    def writeUserData(self,data:Union[str,int],varname:str,method:str = 'text') -> bool:
        if self.user:
            if method == 'text':
                if isinstance(data,str):
                    self.writeText(varname,data)
                    return True
                else:
                    self.writeText(varname,str(data))
                    return True
            elif method == 'int':
                if isinstance(data,int):
                    self.writeInt(varname,data)
                    return True
                else:
                    try:
                        value = int(data)
                        self.writeInt(varname,value)
                        return True
                    except:
                        return False
        else:
            raise Exception('没有已开启的连接')

    def readInt(self,varname:str) -> dict:
        ranking = CloudRanking(self.cloudid,varname)
        ranklist = ranking.readRanking()
        ranklist = json.loads(ranklist)
        return ranklist['my']

    def readText(self,varname:str) -> str:
        filehash = ''
        for i in range(4):
            var = f'{varname}{i + 1}'
            ranking = CloudRanking(self.cloudid,var)
            ranking.open(self.user)
            ranklist = ranking.readRanking()
            ranklist = json.loads(ranklist)
            num = ranklist['my']['value']
            hashtext = self.__inttohash(num)
            filehash += hashtext
        text = self.cloudcdn.readFile4Hash(filehash,'ctext',1).decode('utf-8')
        return text

    def readUserData(self,varname:str,method:str = 'text') -> Union[str,int]:
        if self.user:
            if method == 'text':
                return self.readText(varname)
            elif method == 'int':
                return self.readInt(varname)
        else:
            raise Exception('没有已开启的连接')

    def getAllUserData(self,varname:str) -> list:
        ranking = CloudRanking(self.cloudid,varname)
        ranking.open(self.user)
        return ranking.readRanking()['items']

    def isExist(self,varname:str) -> bool:
        alldata = self.getAllUserData(varname)
        for i in alldata:
            if int(i['user_id']) == self.user:
                return True
        return False