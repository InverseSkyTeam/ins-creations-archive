import json,sys,requests
from time import sleep
from tkinter.messagebox import showinfo
import tkinter as tk
from threading import Thread
from subprocess import check_output
from xes import uploader
'''
请先安装websocket-client库,不是websocket
'''
#爬cookie
try:
    import websocket
except:
    check_output([sys.executable, "-m", "pip", "install", "websocket-client","-i","https://pypi.tuna.tsinghua.edu.cn/simple"])
    import websocket
def get_cookies():
    cookies = ""
    if len(sys.argv) > 1:
        try:
            cookies = json.loads(sys.argv[1])["cookies"]
        except:
            print("未登录")
            sys.exit(0)
    return cookies


#爬取你的id
def get_id():
    cookie = get_cookies()
    id = ''
    for i in cookie.split(";"):
        id = i[8:] if i[1:7] == "stu_id" else id
    return id
def selectfile(filenm):
    if filenm:
        myuploader=uploader.XesUploader()
        url=myuploader.upload(filenm)
    return url
head={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.52"}
user_name = requests.get(f"https://code.xueersi.com/api/space/profile?user_id={get_id()}",headers=head).json()["data"]["realname"]
def send_msg():
    global user_name
    content = user_name+":"+word.get() #获取用户输入的字符
    ascii_content = ""
    num = ""
    if content == "":
        showinfo("温馨提示","不要输入空字符哦")
    else:
        with open("text.txt","w") as f:
            f.write(content)
            f.close()
        users = selectfile("text.txt")
        usernm = users.replace("https://livefile.xesimg.com/programme/python_assets/","").replace(".txt","")
        
        """
        :param m1:字符内容
        :param m2:字符长度
        """
        for n in range(1,6):
            c = "m"+str(n)+''' = {
    "method":"set",
    "user":"15789959",
    "project_id":"20427358",
    "name":"☁ '''+"value"+str(n)+'",'+'''
    "value"'''+':'+str(n)+str(int(usernm,16))[(n-1)*8:n*8]+"""
}"""
            exec(c)
        ws = websocket.create_connection(f'wss://api.xueersi.com/codecloudvariable/ws:80',timeout=30)
        ws.send(json.dumps(locals()["m1"]))
        ws.send(json.dumps(locals()["m2"]))
        ws.send(json.dumps(locals()["m3"]))
        ws.send(json.dumps(locals()["m4"]))
        ws.send(json.dumps(locals()["m5"]))
        # f = open("text.txt","rb")
        #print(f.read().decode("gb18030"))
        #name1 = ws.recv()
        #ws.send(json.dumps(m3))
        #name2 = ws.recv()
        ws.close()
def get_msg():
    try:
        websocket.enableTrace(True)
        text1 = ""
        global user_name
        m2 = {
            "method": "handshake", 
            "user": "15789959",
            "project_id": "20427358"#填作品id
        }
        dic = {}
        
        while True:
            ws = websocket.create_connection('wss://api.xueersi.com/codecloudvariable/ws:80',timeout=5)
            dic = {}
            while True:
                ws.send(json.dumps(m2))
                r = ws.recv()
                value = str(json.loads(r)['value'])
                name = str(json.loads(r)['name'])
                if name in dic:
                    break
                dic[name] = value
            value1 = dic["☁ value1"]
            value2 = dic["☁ value2"]
            value3 = dic["☁ value3"]
            value4 = dic["☁ value4"]
            value5 = dic["☁ value5"]
            sorted_dic = {value1[0]:value1[1:],value2[0]:value2[1:],value3[0]:value3[1:],value4[0]:value4[1:],value4[0]:value4[1:],value5[0]:value5[1:]}
            nr = sorted_dic["1"]+sorted_dic["2"]+sorted_dic["3"]+sorted_dic["4"]+sorted_dic["5"]
            nr = hex(int(nr))[2:]
            head1 = {
    	    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
            }
            zh = nr
            response = requests.get("https://livefile.xesimg.com/programme/python_assets/" + zh + ".txt",headers = head1).content
    
            nrs = response.decode("gb18030")
            if nrs != text1:
                print(nrs)
                text1 = nrs
            ws.close()
        
    except Exception as e:
        print(e)
sys.stdout.write('\033[2J\033[00H')
print("\n")
a = Thread(target=get_msg).start()
root = tk.Tk()
root.title('发消息')
root.geometry('600x200')
frame1 = tk.Frame(root)
word = tk.StringVar()
entry = tk.Entry(frame1, textvariable=word, highlightcolor='Blue', highlightthickness=3, width=25).grid(row=0,column=1)
startbtn = tk.Button(frame1, text='发消息', font=('楷体', 18), fg='orange', width=10, height=2, command=send_msg).grid(row=1,column=0)
tk.Label(frame1, text='输入发的内容',fg="blue",font =("黑体",15)).grid(row=0,column=0)
# tk.Label(frame1, text='本作品作者何嘉晨',bg="red",font =("黑体",18)).grid(row=2,column=0)
frame1.pack()
root.mainloop()