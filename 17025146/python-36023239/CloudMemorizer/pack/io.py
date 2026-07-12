from kernel.cdn import *
from kernel.variable import *
from typing import Union,Optional
import re

class IO():
    def __init__(self,cloudid:Union[int,str],userid:Union[int,str]) -> None:
        self.cloudid = str(cloudid)
        self.userid = str(userid)
        self.varname = None
        self.cloudvar = CloudVar(self.cloudid,self.userid)
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

    def open(self,varname:str) -> None:
        if self.varname:
            raise Exception('存在未关闭的连接')
        else:
            self.varname = varname

    def close(self) -> None:
        if self.varname:
            self.varname = None
        else:
            raise Exception('没有已开启的连接')

    def writeText(self,value:str) -> None:
        filehash = self.__uploadtext(value)
        hashlist = self.__splithash(filehash)
        for i in range(4):
            self.cloudvar.open(f"{self.varname}{i + 1}")
            self.cloudvar.write(hashlist[i])
            self.cloudvar.close()

    def writeInt(self,value:int) -> None:
        self.cloudvar.open(self.varname)
        self.cloudvar.write(value)
        self.cloudvar.close()

    def write(self,value:Union[int,str],method:str = 'text') -> bool:
        if self.varname:
            if method == "text":
                if isinstance(value,str):
                    self.writeText(value)
                else:
                    value = str(value)
                    self.writeText(value)
            elif method == "int":
                if isinstance(value,int):
                    self.writeInt(value)
                    return True
                else:
                    try:
                        value = int(value)
                        self.writeInt(value)
                    except:
                        return False
        else:
            return False

    def readText(self) -> str:
        filehash = ''
        self.cloudvar.open(self.varname)
        vardict = self.cloudvar.readAll()
        for i in range(4):
            num = vardict[f'{self.varname}{i + 1}']
            hashtxt = self.__inttohash(num)
            filehash += hashtxt
        text = self.cloudcdn.readFile4Hash(filehash,'ctext',1).decode('utf-8')
        return text

    def readInt(self) -> int:
        self.cloudvar.open(self.varname)
        value = self.cloudvar.read()
        self.cloudvar.close()
        return int(value)

    def read(self,method:str = 'text') -> str:
        if self.varname:
            if method == 'text':
                text = self.readText()
                return text
            elif method == 'int':
                value = self.readInt()
                return value
        else:
            return None

    def __readAll(self) -> dict:
        return self.cloudvar.readAll()

    def isExist(self) -> bool:
        allvar = self.__readAll()
        for i in range(4):
            name = f'{self.varname}{i + 1}'
            if not (name in allvar):
                return False
        return True
