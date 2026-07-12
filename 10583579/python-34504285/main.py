import json,sys,requests
import tkinter as tk
from tkinter.messagebox import showinfo
import sys
from random import randint
try:
    import websocket
except:
    print("您未安装websocket-client库，正在帮您安装")
    check_output([sys.executable, "-m", "pip", "install", "websocket-client","-i","https://pypi.tuna.tsinghua.edu.cn/simple"])
    try:
        import websocket
    except:
        print("检测到安装异常，请手动输入websocket-client安装")
showinfo("温馨提示","本作品作者何嘉晨,如要使用其中的代码请点击改编")
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
p = "20468291"
m1 = {
    "method":"set",
    "user":"10583579",
    "project_id":p,
    "name":"☁ "+user_name,
    "value":randint(100,500)
}
ws = websocket.create_connection(f'wss://api.xueersi.com/codecloudvariable/ws:80',timeout=30)
ws.send(json.dumps(m1))
name1 = ws.recv()
ws.close()
m2 = {
    "method": "handshake", 
    "user": "10583579",
    "project_id": p#填作品id
}
dic = {}
ws1 = websocket.create_connection(f'wss://api.xueersi.com/codecloudvariable/ws:80',timeout=30)
while True:
    ws1.send(json.dumps(m2))
    r = ws1.recv()
    value = int(str(json.loads(r)['value']))
    name = str(json.loads(r)['name'])[2:]
    if name in dic:
        break
    dic[name] = value
ws1.close()
d = sorted(dic.items(), key = lambda kv:(kv[1], kv[0]),reverse=True)
win = tk.Tk()
win.title("排行榜")
win.geometry("400x500")
i = 0
for k,v in d:
    tk.Label(win,text = "      "+k,font=("微软雅黑",18)).grid(row=i,column=0)
    tk.Label(win,text = "          "+str(v),font=("微软雅黑",18)).grid(row=i,column=1)
    i += 1
win.mainloop()