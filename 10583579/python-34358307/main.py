import json,sys
from tkinter.messagebox import showinfo
import tkinter as tk
from subprocess import check_output
'''
请先安装websocket-client库,不是websocket
'''
#爬cookie
try:
    import websocket
except:
    print("您未安装websocket-client库，正在帮您安装")
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
def send_num():
    p = "20463809"
    content = word.get()
    name = word1.get()
    if content == "":
        showinfo("温馨提示","不要输入空字符哦")
    m1 = {
        "method":"set",
        "user":str(get_id()),
        "project_id":p,
        "name":"☁ "+word1.get(),
        "value":int(word.get())
    }
    
    m2 = {"method": "handshake", 
        "user": str(get_id()),
        "project_id": p#填作品id
    }
    ws = websocket.create_connection(f'wss://api.xueersi.com/codecloudvariable/ws:80',timeout=30)
    ws.send(json.dumps(m1))
    name1 = ws.recv()
    ws.close()
    print("存储成功")
def get_num():
    p = "20463809"
    m2 = {
        "method": "handshake", 
        "user": str(get_id()),
        "project_id": p#填作品id
    }
    dic = {}
    ws1 = websocket.create_connection(f'wss://api.xueersi.com/codecloudvariable/ws:80',timeout=30)
    while True:
        ws1.send(json.dumps(m2))
        r = ws1.recv()
        value = str(json.loads(r)['value'])
        name = str(json.loads(r)['name'])
        if name in dic:
            break
        dic[name] = value
    ws1.close()
    print(word1.get()+":"+dic["☁ "+word1.get()])
sys.stdout.write('\033[2J\033[00H')
print("\n")
root = tk.Tk()
root.title('云变量')
root.geometry('600x200')
frame1 = tk.Frame(root)
word = tk.StringVar()
word1 = tk.StringVar()
entry = tk.Entry(frame1, textvariable=word, highlightcolor='Blue', highlightthickness=3, width=25).grid(row=0,column=1)
entry1 = tk.Entry(frame1, textvariable=word1, highlightcolor='Blue', highlightthickness=3, width=25).grid(row=1,column=1)
sendbtn = tk.Button(frame1, text='发送', font=('楷体', 18), fg='orange', width=10, height=2, command=send_num).grid(row=3,column=0)
readbtn = tk.Button(frame1, text='读取', font=('楷体', 18), fg='orange', width=10, height=2, command=get_num).grid(row=3,column=1)
tk.Label(frame1, text='输入发的内容',fg="blue",font =("黑体",15)).grid(row=0,column=0)
tk.Label(frame1, text='输入发/读取的变量名',fg="blue",font =("黑体",15)).grid(row=1,column=0)
# tk.Label(frame1, text='本作品作者何嘉晨',bg="red",font =("黑体",18)).grid(row=4,column=0)
frame1.pack()
root.mainloop()