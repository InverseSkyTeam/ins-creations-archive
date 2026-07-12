import json
import os, zipfile
import requests
import hashlib
import os
import json
import tkinter.filedialog
from pyperclip import *

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

    def __uploadFile(self, filepath,contents):
        md5 = hashlib.md5(contents).hexdigest()
        url = 'https://code.xueersi.com/api/assets/get_oss_upload_params'
        params = {"scene": "offline_python_assets", "md5": md5, "filename": filepath}
        response = requests.get(url=url, params=params)
        uploadParams = json.loads(response.text)
        requests.request(method="PUT", url=uploadParams['data']['host'], data=contents, headers=uploadParams['data']['headers'])
        return uploadParams

    def getFileHash4Path(self,filepath:str):
        filepath = self.__getAbs(filepath)
        contents = self.__getFileContent(filepath)
        data = self.__uploadFile(filepath,contents)
        data = data['data']['host']
        data = data.split('/')[-1].split('.')[0]
        return data

    def getFileHash4Content(self,filecontent:bytes,filepath:str) -> str:
        filepath = self.__getAbs(filepath)
        contents = filecontent
        data = self.__uploadFile(filepath,contents)
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

def zip_ya(startdir,file_news):
    z = zipfile.ZipFile(file_news,'w',zipfile.ZIP_DEFLATED)
    for dirpath, dirnames, filenames in os.walk(startdir):
        fpath = dirpath.replace(startdir,'')
        fpath = fpath and fpath + os.sep or ''
        for filename in filenames:
            z.write(os.path.join(dirpath, filename),fpath+filename)
    z.close()

def is_enable(path):
    if "main.py" in os.listdir(path):
        return True
    else:
        return False

print("使用教程：在弹出的窗口中选择项目文件夹（包含一个main.py和所有资源）,然后生成好的引导代码就会自动复制到剪贴板，打开一个新的项目，将代码粘贴到main.py中，然后发布，就可以了")
input("准备好了按回车确定:")
path = tkinter.filedialog.askdirectory()
enable = is_enable(path)
if enable:
    print('开始压缩')
    zip_ya(path,"./zip.zip")
    print("压缩完成")
    cdn = CloudCDN()
    fh = cdn.getFileHash4Path("./zip.zip")
    print("上传成功")
    with open("template.py","r",encoding="utf-8") as f:
        tem = f.read()
    tem = tem.replace("$$$filehash$$$",str(fh))
    copy(tem)
    print("代码已复制到剪贴板，快去粘贴吧")
else:
    print("选择的文件夹不符合要求")