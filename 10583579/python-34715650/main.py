from tkinter import filedialog,messagebox
import websocket
import json
import sys
import requests
from xes import uploader
class XesIde:#类名可以改一下
    def __init__(self):
        #这里做界面
        pass
    def save_as(self,content):
        savefilename = filedialog.asksaveasfilename(defaultextension='.py',filetypes=[("Python files", "*.py;*.pyw"), ("Text files", "*.txt"), ("所有文件", "*")])
        if savefilename != '':
            try:
                with open(savefilename, 'w', encoding='utf-8') as file:
                    file.write(content)
            except Exception as e:
                print(str(e))#方便查看错误
            else:
                print(time.strftime('[%Y-%m-%d %H:%M:%S]') + 'Save as file successful,path' + savefilename)
                messagebox.showinfo('提示', '代码文件成功导出至' + savefilename)
    def save_in_cloud(self,content,name):
        """
        :param content:代码内容
        :param name:文件名称
        :return:None
        """
        #project_id=20553603
        with open(name+".txt","w",encoding = "utf-8") as f:
            f.write(content)
        f.close()
        self.ws = websocket.create_connection('wss://api.xueersi.com/codecloudvariable/ws:80',timeout=5)
        #使用云端存档
        myuploader = uploader.XesUploader()
        hashtext = myuploader.upload(name+".txt").replace("https://livefile.xesimg.com/programme/python_assets/","").replace(".txt","")
        for n in range(1,6):
            c = eval('{"method":"set","user":'+'"'+str(self.get_id())+'"'+',"project_id":"20553603","name":"☁ ' + name + str(n) + '",' + '"value"' + ':' + str(n)+str(int(hashtext, 16))[(n - 1) * 8:n * 8] + "}")
            self.ws.send(json.dumps(c))#转json并上传#这里因为数据太大会被xes取近似数所以截断存储，懒得写那么多字典，所以直接eval
            print(self.ws.recv())
        self.ws.close()
    def read_from_cloud(self,filename):
        message = {
            "method": "handshake", 
            "user": str(self.get_id()),
            "project_id": "20553603"#填作品id
        }
        ws = websocket.create_connection(f'wss://api.xueersi.com/codecloudvariable/ws:80',timeout=30)
        dic = {}
        f = open("hello.txt","rb")
        while True:
            ws.send(json.dumps(message))
            r = ws.recv()
            value = str(json.loads(r)['value'])
            name = str(json.loads(r)['name'])
            if name in dic:
                break
            dic[name] = value
        value1 = dic[f"\u2601 {filename}1"][1:]
        value2 = dic[f"\u2601 {filename}2"][1:]
        value3 = dic[f"\u2601 {filename}3"][1:]
        value4 = dic[f"\u2601 {filename}4"][1:]
        value5 = dic[f"\u2601 {filename}5"][1:]
        nr = value1+value2+value3+value4+value5
        nr = hex(int(nr))[2:]
        head1 = {
	    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
        }
        zh = nr
        response = requests.get("https://livefile.xesimg.com/programme/python_assets/" + zh + ".txt",headers = head1).content
        nrs = response.decode("utf-8")
        print("代码:")
        print("".join(nrs.split("\r")))
    #获取cookie
    def get_cookies(self):
        cookies = ""
        if len(sys.argv) > 1:
            try:
                cookies = json.loads(sys.argv[1])["cookies"]
            except:
                print("未登录")
                sys.exit(0)
        return cookies
    # 爬取你的id
    def get_id(self):
        cookie = self.get_cookies()
        id = ''
        for i in cookie.split(";"):
            id = i[8:] if i[1:7] == "stu_id" else id
        return id
code = """from tkinter import filedialog,messagebox
import websocket
import json
import sys
import requests
from xes import uploader
class XesIde:#类名可以改一下
    def __init__(self):
        #这里做界面
        pass
    def save_as(self,content):
        savefilename = filedialog.asksaveasfilename(defaultextension='.py',filetypes=[("Python files", "*.py;*.pyw"), ("Text files", "*.txt"), ("所有文件", "*")])
        if savefilename != '':
            try:
                with open(savefilename, 'w', encoding='utf-8') as file:
                    file.write(content)
            except Exception as e:
                print(str(e))#方便查看错误
            else:
                print(time.strftime('[%Y-%m-%d %H:%M:%S]') + 'Save as file successful,path' + savefilename)
                messagebox.showinfo('提示', '代码文件成功导出至' + savefilename)
    def save_in_cloud(self,content,name):
        '''
        :param content:代码内容
        :param name:文件名称
        :return:None
        '''
        #project_id=20553603
        with open(name+".txt","w") as f:
            f.write(content)
        f.close()
        self.ws = websocket.create_connection('wss://api.xueersi.com/codecloudvariable/ws:80',timeout=5)
        #使用云端存档
        myuploader = uploader.XesUploader()
        hashtext = myuploader.upload(name+".txt").replace("https://livefile.xesimg.com/programme/python_assets/","").replace(".txt","")
        for n in range(1,6):
            c = eval('{"method":"set","user":'+'"'+str(self.get_id())+'"'+',"project_id":"20553603","name":"☁ ' + name + str(n) + '",' + '"value"' + ':' + str(n)+str(int(hashtext, 16))[(n - 1) * 8:n * 8] + "}")
            self.ws.send(json.dumps(c))#转json并上传#这里因为数据太大会被xes取近似数所以截断存储，懒得写那么多字典，所以直接eval
            print(self.ws.recv())
        self.ws.close()
    def read_from_cloud(self,filename):
        message = {
            "method": "handshake", 
            "user": str(self.get_id()),
            "project_id": "20553603"#填作品id
        }
        ws = websocket.create_connection(f'wss://api.xueersi.com/codecloudvariable/ws:80',timeout=30)
        dic = {}
        f = open("hello.txt","rb")
        while True:
            ws.send(json.dumps(message))
            r = ws.recv()
            value = str(json.loads(r)['value'])
            name = str(json.loads(r)['name'])
            if name in dic:
                break
            dic[name] = value
        value1 = dic[f"\u2601 {filename}1"][1:]
        value2 = dic[f"\u2601 {filename}2"][1:]
        value3 = dic[f"\u2601 {filename}3"][1:]
        value4 = dic[f"\u2601 {filename}4"][1:]
        value5 = dic[f"\u2601 {filename}5"][1:]
        nr = value1+value2+value3+value4+value5
        nr = hex(int(nr))[2:]
        head1 = {
	    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
        }
        zh = nr
        response = requests.get("https://livefile.xesimg.com/programme/python_assets/" + zh + ".txt",headers = head1).content
        nrs = response.decode("gb18030")
        print("代码:")
        print("".join(nrs.split("\r")))
    #获取cookie
    def get_cookies(self):
        cookies = ""
        if len(sys.argv) > 1:
            try:
                cookies = json.loads(sys.argv[1])["cookies"]
            except:
                print("未登录")
                sys.exit(0)
        return cookies
    # 爬取你的id
    def get_id(self):
        cookie = self.get_cookies()
        id = ''
        for i in cookie.split(";"):
            id = i[8:] if i[1:7] == "stu_id" else id
        return id
ide = XesIde()
ide.save_in_cloud('print("hello world")\nprint("hello webpy")',"hello")
ide.read_from_cloud("hello")"""
ide = XesIde()
ide.save_in_cloud(code,"hello")
ide.read_from_cloud("hello")