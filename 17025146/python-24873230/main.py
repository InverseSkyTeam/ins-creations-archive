import time,pygame,sys,tkinter,os,hashlib
from xes import uploader
from tkinter import *
import shutil,requests,json,bs4
class up(object):
    def _getUploadParams(self, filename, md5):
        url = 'https://code.xueersi.com/api/assets/get_oss_upload_params'
        params = {"scene": "offline_python_assets", "md5": md5, "filename": filename}
        response = requests.get(url=url, params=params)
        data = json.loads(response.text)['data']
        return data
    def uploadAbsolutePath(self, filepath):
        md5 = None
        contents = None
        fp = open(filepath, 'rb')
        contents = fp.read()
        fp.close()
        md5 = hashlib.md5(contents).hexdigest()

        if md5 is None or contents is None:
            raise Exception("文件不存在")

        uploadParams = self._getUploadParams(filepath, md5)
        requests.request(method="PUT", url=uploadParams['host'], data=contents, headers=uploadParams['headers'])
        return uploadParams['url']
def selectfile(filenm):
    if filenm:
        file=open(filenm)
        myuploader=up()
        url=myuploader.uploadAbsolutePath(filenm)
    return url
print("1、读取 2、上传")
fy = input("")
if fy == "2":
    password = input("设置密码：")
    nr = input("输入要上传的内容：")
    with open("user.txt","w") as az:
        az.write(f"password:{password}\nnr:{nr}")
    users = selectfile("user.txt")
    usernm = users.replace("https://livefile.xesimg.com/programme/python_assets/","").replace(".txt","")
    print(f"你的存档码是：{usernm}")
elif fy == "1":
    head1 = {
    	    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
        }
    zh = input("输入存档码：")
    response = requests.get("https://livefile.xesimg.com/programme/python_assets/" + zh + ".txt",headers = head1).content

    with open("x.txt","wb") as h:
        h.write(response)
    with open("x.txt","r") as h:
        ss = h.read()
    pw = ss.split("\n")[0].replace("password:","")
    nrs = ss.split("\n")[1].replace("nr:","")
    u = input("输入密码：")
    if u == pw:
        print("密码正确！")
        print("存档内容为:")
        print(nrs)
    else:
        print("密码错误！")