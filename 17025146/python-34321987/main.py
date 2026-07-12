import json,sys,requests
from time import sleep
from tkinter.messagebox import showinfo
import tkinter as tk
from threading import Thread
from subprocess import check_output
'''
请先安装websocket-client库,不是websocket
'''
#爬cookie
try:
    import websocket
except:
    check_output([sys.executable, "-m", "pip", "install", "websocket-client","-i","https://pypi.tuna.tsinghua.edu.cn/simple"])
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
head={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.52"}
user_name = requests.get(f"https://code.xueersi.com/api/space/profile?user_id={get_id()}",headers=head).json()["data"]["realname"]
def send_msg():
    content = word.get() #获取用户输入的字符
    print(content)
    ascii_content = ""
    num = ""
    if content == "":
        showinfo("温馨提示","不要输入空字符哦")
    else:
        for i in content:
            num += str(len(str(ord(i)))) #获取字符总长
            ascii_content += str(ord(i)) #获取全部字符
        
        """
        m1:字符内容
        m2:字符长度
        """
        m1 = {
            "method":"set",
            "user":"15789959",
            "project_id":"2040147",
            "name":"☁ 聊天内容",
            "value":int(ascii_content)
        }
        m3 = {
            "method":"set",
            "user":"15789959",
            "project_id":"2040147",
            "name":"☁ 占位",
            "value":int(num)
        }
        ws = websocket.create_connection(f'wss://api.xueersi.com/codecloudvariable/ws:80',timeout=30)
        ws.send(json.dumps(m1))
        name1 = ws.recv()
        ws.send(json.dumps(m3))
        name2 = ws.recv()
        ws.close()
def get_msg():
    global user_name
    m2 = {
        "method": "handshake", 
        "user": "15789959",
        "project_id": "2040147"#填作品id
    }
    value1,value2 = "",""
    ws = websocket.create_connection(f'wss://api.xueersi.com/codecloudvariable/ws:80',timeout=30)
    text = ""
    text1 = text
    while True:
        lst = []
        ws.send(json.dumps(m2))
        value1 = str(json.loads(ws.recv())['value'])
        ws.send(json.dumps(m2))
        value2 = str(json.loads(ws.recv())['value'])

        # 交换value1和value2
        """
        @ 何嘉晨
        你原来写的方法太晦涩难懂，其实目的就是交换value1和value2两个变量，没必要使用三方变量value3，所以我改了一下。
        """
        if len(value1) < len(value2):
            value1,value2 = value2,value1 # 这是专属于Python的方法，简洁优雅
        elif len(value1) == len(value2) and value1 == "111":
            value1,value2 = value2,value1

        for i in value2:
            try:
                lst.append(chr(int(value1[:int(i)])))
            except:
                lst.append(chr(int(value1[:int(i)+1])))
            value1 = value1[int(i):]
        text = "".join(lst)
        if text != "" and text == text1:
            continue
        else:
            print(user_name+":"+text)
        text1 = text
    ws.close()
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
tk.Label(frame1, text='本作品作者何嘉晨',bg="red",font =("黑体",18)).grid(row=2,column=0)
frame1.pack()
root.mainloop()