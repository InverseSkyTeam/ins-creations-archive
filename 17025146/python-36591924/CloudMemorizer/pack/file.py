import os
from kernel.cdn import *
import json
import time
from typing import Union,Optional
from .io import *

class File():
    def __init__(self,cloudid:Union[int,str],userid:Union[int,str]) -> None:
        self.cloudid = str(cloudid)
        self.userid = str(userid)

    def __getFileSize(self,filepath:str,norm:str) -> int:
        sizedict = {'b':0,'kb':1,'mb':2,'gb':3,'tb':4,'pb':5,'eb':6,'zb':7,'yb':8}
        norm = norm.lower()
        if 'b' in norm:
            size = 1024 ** sizedict[norm]
        else:
            size = 1024 ** sizedict[norm + 'b']
        filesize = os.path.getsize(filepath)
        return filesize // size + 1 # 向上取整

    def __splitFile(self,filepath:str,length:int,norm:str) -> list:
        """
        :return:返回值为一个列表,列表中每一项均为bytes类型
        """
        sizedict = {'b':0,'kb':1,'mb':2,'gb':3,'tb':4,'pb':5,'eb':6,'zb':7,'yb':8}
        norm = norm.lower()
        if 'b' in norm:
            size = 1024 ** sizedict[norm]
        else:
            size = 1024 ** sizedict[norm + 'b']
        byteslist = []
        fsize = self.__getFileSize(filepath,'B')
        length = length * size
        num = fsize // length + 1 # 向上取整
        with open(filepath,'rb') as file:
            for i in range(num):
                file.seek(i * length)
                data = file.read(length)
                byteslist.append(data)
        return byteslist

    def uploadZones(self,filepath:str,length:int,norm:str) -> str:
        """
        :param length:每个文件分片的大小
        :param norm:length的单位与标准,如B、KB、MB等
        """
        zones = []
        zonelist = self.__splitFile(filepath,length,norm)
        cdn = CloudCDN()
        for i in range(len(zonelist)):
            with open(f'{i + 1}.filezone','wb') as f:
                f.write(zonelist[i])
            fhash = cdn.getFileHash(f'{i + 1}.filezone')
            zones.append(fhash)
        return zones
    
    def saveFileIndex(self,fileindex:Union[dict,list]) -> str:
        cdn = CloudCDN()
        with open('file.json','w') as file:
            file.write(json.dumps(fileindex))
        jsonhash = cdn.getFileHash('file.json')
        return jsonhash

    def uploadFile(self,filepath:str,length:int,norm:str) -> str:
        zones = self.uploadZones(filepath,length,norm)
        filehash = self.saveFileIndex(zones)
        return filehash

    def getFileIndex(self,jsonhash:str) -> Union[dict,list]:
        cdn = CloudCDN()
        content = cdn.readFile4Hash(jsonhash,'json',1)
        data = json.loads(content.decode('utf-8'))
        return data

    def parseData(self,data:Union[dict,list]) -> bytes:
        filecontent = b''
        cdn = CloudCDN()
        for i in data:
            fcontent = cdn.readFile4Hash(i,'filezone',1)
            filecontent += fcontent
        return filecontent

    def downloadFile(self,jsonhash:str) -> bytes:
        data = self.getFileIndex(jsonhash)
        content = self.parseData(data)
        return content

    def addCloudFile(self,filehash:str) -> int:
        io = IO(self.cloudid,self.userid,'text')
        io.open('files')
        data = json.loads(io.read())
        fileid = int(data['new']) + 1
        data['new'] = fileid
        data['data'][str(fileid)] = filehash
        io.write(json.dumps(data))
        io.close()
        return fileid

    def saveFileToCloud(self,filepath:str) -> int:
        filezones = self.uploadFile(filepath,20,'MB')
        filehash = self.saveFileIndex(filezones)
        fileid = self.addCloudFile(filehash)
        return fileid

    def downloadFileForCloud(self,fileid:int) -> bytes:
        io = IO(self.cloudid,self.userid,'text')
        io.open('files')
        data = json.loads(io.read())['data']
        filehash = data[str(fileid)]
        return self.downloadFile(filehash)