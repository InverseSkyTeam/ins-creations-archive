import requests
import hashlib
import os
import json

class CloudCDN():
    def __init__(self) -> None:
        self.xesurl = 'https://livefile.xesimg.com/programme/python_assets/{}.{}'
        self.ossurl = 'https://xueersifile.oss-cn-beijing.aliyuncs.com/programme/python_assets/{}.{}'
        self.internalurl = 'https://xueersifile.oss-cn-beijing-internal.aliyuncs.com/programme/python_assets/{}.{}'

    def __getFileURL(self,hash:str,ext:str,method:int) -> str:
        methoddict = {
            "1":self.xesurl,
            "2":self.ossurl,
            "3":self.internalurl
        }
        url = methoddict[str(method)].format(hash,ext)
        return url

    def __getAbs(self,path:str) -> str:
        if os.path.isabs(path):
            return path
        else:
            return os.getcwd() + "/" + path

    def __getFileContent(self,file:str) -> bytes:
        if os.path.isfile(file):
            fp = open(file, 'rb')
            contents = fp.read()
            fp.close()
            return contents
        else:
            raise Exception('文件不存在')

    def __uploadFile(self, filepath):
        filepath = self.__getAbs(filepath)
        contents = self.__getFileContent(filepath)
        md5 = hashlib.md5(contents).hexdigest()
        url = 'https://code.xueersi.com/api/assets/get_oss_upload_params'
        params = {"scene": "offline_python_assets", "md5": md5, "filename": filepath}
        response = requests.get(url=url, params=params)
        uploadParams = json.loads(response.text)
        requests.request(method="PUT", url=uploadParams['data']['host'], data=contents, headers=uploadParams['data']['headers'])
        return uploadParams

    def getFileHash(self,filepath:str):
        data = self.__uploadFile(filepath)
        data = data['data']['host']
        data = data.split('/')[-1].split('.')[0]
        return data

    def readFile4Hash(self,hash:str,ext:str,method:int) -> bytes:
        """
        :param hash:文件的唯一标识符
        :param ext:文件的后缀
        :param method:读取文件的地址,1为XesCDN,2为AliyunOSS,3为AliyunOSS-Internal
        """
        headers = {
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
        }
        url = self.__getFileURL(hash,ext,method)
        data = requests.get(url=url,headers=headers).content
        return data

    def readFile4URL(self,url:str) -> bytes:
        headers = {
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
        }
        data = requests.get(url=url,headers=headers).content
        return data
    
    def saveFile4Hash(self,filename:str,hash:str,ext:str,method:str) -> int:
        try:
            with open(filename,"wb") as file:
                file.write(self.readFile4Hash(hash,ext,method))
            return 1
        except:
            return 0

    def saveFile4URL(self,filename:str,url:str) -> int:
        try:
            with open(filename,"wb") as file:
                file.write(self.readFile4URL(url))
            return 1
        except:
            return 0