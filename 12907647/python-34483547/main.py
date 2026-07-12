import json,sys
from tkinter.messagebox import showinfo
import tkinter as tk
from subprocess import check_output

# 请先安装websocket-client库,不是websocket
try:
    import websocket
except:
    print("您未安装websocket-client库，正在帮您安装")
    check_output([sys.executable, "-m", "pip", "install", "pip","--upgrade"])
    check_output([sys.executable, "-m", "pip", "install", "websocket-client","-i","https://pypi.tuna.tsinghua.edu.cn/simple"])
    try:
        import websocket
    except:
        print("检测到安装异常，请手动输入websocket-client安装")

showinfo("温馨提示","本作品联合逆天团队版权所有，参与编辑：何嘉晨、冀厚锦、吴宇航、小轩，请注意改编时的版权")
# 爬cookie
def get_cookies():
    cookies = ""
    if len(sys.argv) > 1:
        try:
            cookies = json.loads(sys.argv[1])["cookies"]
        except:
            print("未登录")
            sys.exit(0)
    return cookies


# 爬取你的id
def get_id():
    cookie = get_cookies()
    id = ''
    for i in cookie.split(";"):
        id = i[8:] if i[1:7] == "stu_id" else id
    return id

# 发送
def send_num():
    p = "20426352"
    content = word_entry.get()
    name = variable_name_entry.get()
    if content == "":
        showinfo("温馨提示","不要输入空字符哦")
    m1 = {
        "method":"set",
        "user":str(get_id()),
        "project_id":p,
        "name":"☁ "+variable_name_entry.get(),
        "value":int(word_entry.get())
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

# 接收
def get_num():
    p = "20426352"
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
    # print(dic) 查看云字典
    print(variable_name_entry.get()+":"+dic["☁ "+variable_name_entry.get()])

sys.stdout.write('\033[2J\033[00H')
print("\n")

root = tk.Tk()
root.title('云变量')
root.geometry('600x200')

word = tk.StringVar()
variable_name = tk.StringVar()
word_entry = tk.Entry(root, textvariable=word, width=25)
word_entry.grid(row=0,column=1)
variable_name_entry = tk.Entry(root, textvariable=variable_name, width=25)
variable_name_entry.grid(row=1,column=1)

sendbtn = tk.Button(root, text='发送', font=('楷体', 18), fg='orange', width=10, height=2, command=send_num)
sendbtn.grid(row=3,column=0)
readbtn = tk.Button(root, text='读取', font=('楷体', 18), fg='orange', width=10, height=2, command=get_num)
readbtn.grid(row=3,column=1)
tk.Label(root, text='输入发的内容',fg="blue",font =("黑体",15)).grid(row=0,column=0)
tk.Label(root, text='输入发/读取的变量名',fg="blue",font =("黑体",15)).grid(row=1,column=0)
tk.Label(root, text='本作品逆天团队联合出版',fg="blue",font =("楷体",18)).grid(row=4,column=0)
root.mainloop()