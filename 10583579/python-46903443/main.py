#coding:utf-8
import requests
import json
import websocket
import hashlib
import tkinter as tk
import os
import sys
from re import findall
from time import localtime, strftime, sleep
from threading import Thread
from ctypes import windll
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import filedialog
from random import randint
from webbrowser import open as webopen

appellation = [("",""),(r"\粗\红C红\\浅红a浅红\\橙r橙\\黄r黄\\绿r绿\\浅绿r浅绿\\浅蓝r浅蓝\\青r青\\蓝r蓝\\纯蓝r纯蓝\\粉r粉\\紫r紫\r\灰1r灰1\\灰2r灰2\\紫r紫\\粉r粉\\纯蓝r纯蓝\\蓝r蓝\\青r青\\浅蓝r浅蓝\\浅绿r浅绿\\绿r绿\\黄r黄\\橙r橙\\红y红\\黄全场≈▶黄\粗\ "," \\黄\\粗≈▶节奏黄\\粗\\"),("\\黄\\粗【编程王者】粗\\黄\\[","]"),(r"\浅红1浅红\\红2红\\黄3黄\\橙4橙\\浅绿5浅绿\\绿6绿\\浅蓝7浅蓝\\青8青\\蓝9蓝\\蓝8蓝\\粉7粉\\紫6紫\\浅蓝5浅蓝\\浅绿4浅绿\\黄3黄\\浅红2浅红\\粉1粉\ ≈▶ ","≈▶"),(r"\粗\浅红【浅红\\浅绿社区浅绿\\浅红】浅红\粗\\黄元老黄\[","]"),(r"\浅蓝高手浅蓝\[","]"),(r"\粉极客粉\[","]"),("\\粗\\浅绿666666浅绿\\粗\\[","]\\粗\\浅绿666666浅绿\\粗\\")]
THE_NUMBER_OF_APPELLATION = len(appellation)
WIDTH,HEIGHT=windll.user32.GetSystemMetrics(0),windll.user32.GetSystemMetrics(1)

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

def cutText(text, lenth):
    textArr = findall('.{' + str(lenth) + '}', text)
    textArr.append(text[(len(textArr) * lenth):])
    if len(text) % lenth == 0:
        return textArr[0:-1]
    else:
        return textArr


def fillto8(text):
    if len(text) == 8:
        return text
    elif len(text) < 8:
        return (8 - len(text)) * '0' + text


def save_to_cloud(name, content, userid, project_id=20619483):
    try:
        with open(name + ".txt", "w", encoding="utf-8") as f:
            f.write(str(content))
        f.close()
        ws = websocket.create_connection('wss://api.xueersi.com/codecloudvariable/ws:80', timeout=5)
        myuploader = XesUploader()
        hashtext = myuploader.upload(name + ".txt").replace("https://livefile.xesimg.com/programme/python_assets/",
                                                            "").replace(".txt", "")
        os.remove(name + ".txt")
        xlist = cutText(hashtext, 8)
        for i in range(4):
            msg = {
                "method": "set",
                "user": userid,
                "project_id": project_id,
                "name": "☁ " + name + str(i + 1),
                "value": int(xlist[i], 16)
            }
            ws.send(json.dumps(msg))
        ws.close()
        return True
    except Exception as e:
        print(e)
    return False


def read_from_cloud(filename, userid, to_get='file', project_id=20619483):
    message = {
        "method": "handshake",
        "user": str(userid),
        "project_id": str(project_id)
    }
    ws = websocket.create_connection(f'wss://api.xueersi.com/codecloudvariable/ws:80', timeout=5)
    dic = {}
    while True:
        ws.send(json.dumps(message))
        r = ws.recv()
        try:
            value = str(json.loads(r)['value'])
        except:
            continue
        name = str(json.loads(r)['name'])
        if name in dic:
            break
        dic[name] = value
    if to_get == 'dictionary':
        return dic
    value1 = dic[f"☁ {filename}1"]
    value2 = dic[f"☁ {filename}2"]
    value3 = dic[f"☁ {filename}3"]
    value4 = dic[f"☁ {filename}4"]
    vlist = [value1, value2, value3, value4]
    nr = ''
    for i in vlist:
        nr += fillto8(str(hex(int(i)))[2:])
    head1 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'}
    zh = nr
    response = requests.get("https://livefile.xesimg.com/programme/python_assets/" + zh + ".txt",
                            headers=head1).content
    nrs = response.decode("utf-8")
    return "".join(nrs.split("\r"))


class XesUploader:

    # 文件相对路径
    def upload(self, relativeFilePath):
        absolutePath = os.getcwd() + "/" + relativeFilePath
        return self.uploadAbsolutePath(absolutePath)

    # 文件绝对路径
    def uploadAbsolutePath(self, filepath):
        md5 = None
        contents = None
        if os.path.isfile(filepath):
            fp = open(filepath, 'rb')
            contents = fp.read()
            fp.close()
            md5 = hashlib.md5(contents).hexdigest()

        if md5 is None or contents is None:
            raise Exception("文件不存在")

        uploadParams = self._getUploadParams(filepath, md5)
        requests.request(method="PUT", url=uploadParams['host'], data=contents, headers=uploadParams['headers'])
        return uploadParams['url']

    # 获取上传签名
    def _getUploadParams(self, filename, md5):
        url = 'https://code.xueersi.com/api/assets/get_oss_upload_params'
        params = {"scene": "offline_python_assets", "md5": md5, "filename": filename}
        response = requests.get(url=url, params=params)
        data = json.loads(response.text)['data']

        return data

headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53"
}

realname = requests.get(f"https://code.xueersi.com/api/space/profile?user_id={get_id()}",headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.52"}).json()["data"]["realname"]

try:
    f = open(r"D:\EasyChat-Dev/appellation.dat","r")
except:
    os.mkdir(r"D:\EasyChat-Dev")
    f1 = open(r"D:\EasyChat-Dev/appellation.dat","w")
    f1.write("0")
    f1.close()
    f = open(r"D:\EasyChat-Dev/appellation.dat","r")

appellation_index = int(f.read())
f.close()
name = appellation[appellation_index][0]+"\\青"+realname+"青\\"+appellation[appellation_index][1]

flag = False
project_id = 22388238

def send_msg(event,mode='normal',content=None):
    global flag
    if mode == 'normal':
        writein = msg_entry.get(1.0,tk.END)[:-1]
    else:
        writein = content
    if writein == "清空聊天记录":
        save_to_cloud("聊天记录", "欢迎来到聊天室\n\n更新内容:制作了UI界面、称号系统、搜索消息、输入exit即可退出(也可以直接点击\"×\")\n\n支持的文字颜色有:浅红,浅蓝,浅绿,红,橙,黄,绿,蓝,紫,灰,黑,粗,粉,青\n\nEnter(回车)发送消息\n", 10583579, project_id)
    elif writein == "exit":
        def changeto16(data):
            a = hex(data[0])[2:]
            b = hex(data[1])[2:]
            c = hex(data[2])[2:]
            a = (2-len(a))*"0"+a
            b = (2-len(b))*"0"+b
            c = (2-len(c))*"0"+c
            return f"#{a}{b}{c}"
        window = tk.Tk()
        window.overrideredirect(True)
        window["bg"] = "#FFFFFF"
        text1 = tk.Label(window,text="提示",bg="white",font=("宋体",14))
        text1.place(x=20,y=20)
        text2 = tk.Label(window,text="确定要退出吗？",bg="white",fg=changeto16((66,73,82)),font=("宋体",12))
        text2.place(x=20,y=70)
        text3 = tk.Label(window,text="确定",font=("宋体",13),bg=changeto16((245,246,247)),width=9,height=2,cursor="hand2")
        text3.place(x=280,y=120)
        text4 = tk.Label(window,text="取消",font=("宋体",13),fg="white",bg=changeto16((250,158,0)),width=9,height=2,cursor="hand2")
        text4.place(x=380,y=120)
        text5 = tk.Label(window,text="×",font=("宋体",20),fg=changeto16((46,53,62)),bg="#FFFFFF",width=2,height=1,cursor="hand2")
        text5.place(x=450,y=10)
        for i in range(1,11):
            window.geometry(f"500x180+{WIDTH//2-250}+{HEIGHT//2-(30-i)*15//2}")
            window.update()
            sleep(0.001)
        def quit(event):
            window.destroy()
        def newexit(event):
            os._exit(0)
        text3.bind("<Button-1>",newexit)
        text4.bind("<Button-1>",quit)
        text5.bind("<Button-1>",quit)
        window.mainloop()
    else:
        save_to_cloud("聊天记录", f"{last}\n[{strftime('%Y-%m-%d %H:%M:%S', localtime())}]" + name + ":" + writein + "\n",
                      10583579, project_id)
    flag = True

def AnalysisColor(color):
    try:
        row,column = msg_box.search(f'\\{color_dict[color]}',1.0,'end').split(".")
        row1,column1 = msg_box.search(f'{color_dict[color]}\\',1.0,'end').split(".")
        if row < row1:
            if len(color_dict[color]) == 1:
                msg_box.delete(f"{row}.{column}",f"{row}.{int(column)+2}")
            else:
                msg_box.delete(f"{row}.{column}",f"{row}.{int(column)+3}")
        elif row1 < row:
            if len(color_dict[color]) == 1:
                msg_box.delete(f"{row1}.{int(column1)}",f"{row1}.{int(column1)+2}")
            else:
                msg_box.delete(f"{row1}.{int(column1)}",f"{row1}.{int(column1)+3}")
        else:
            if len(color_dict[color]) == 1:
                msg_box.delete(row+"."+column,row+"."+str(int(column)+2))
                msg_box.delete(row+"."+str(int(column1)-2),row+"."+column1)
                column1 = str(int(column1)-2)
            else:
                msg_box.delete(row+"."+column,row+"."+str(int(column)+3))
                msg_box.delete(row+"."+str(int(column1)-3),row+"."+column1)
                column1 = str(int(column1)-3)
            target_string = msg_box.get(row+"."+column,row+"."+column1)
            msg_box.tag_add(f'{color}_fg',f'{row}.{column}',f'{row}.{column}+{len(target_string)}c')
        AnalysisColor(color)
    except:
        pass

def AnalysisFile():
    try:
        row,column = msg_box.search("文件{https://livefile.xesimg.com/",1.0,'end').split(".")
        row,column = int(row),int(column)
        msg_box.delete(f"{row}.{column}",f"{row}.{column+3}")
        filepath = msg_box.get(f"{row}.{column}",f"{row}.{column+85}")
        idx = 85
        content = msg_box.get(f"{row}.{column+idx}",f"{row}.{column+idx+1}")
        extended_name = ""
        while content != "}":
            idx += 1
            extended_name += content
            content = msg_box.get(f"{row}.{column+idx}",f"{row}.{column+idx+1}")
        filepath += extended_name
        msg_box.delete(f"{row}.{column}",f"{row}.{column+len(filepath)+1}")
        if extended_name in extended_name_list and not extended_name_list[extended_name]:
            headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
            }
            response = requests.get(filepath,headers=headers).content
            try:
                os.mkdir("D:\\EasyChat-Dev\\Images")
            except:
                pass
            filename = f"D:\\EasyChat-Dev\\Images/{filepath[-len(extended_name)-33:]}"
            f = open(filename,"wb")
            f.write(response)
            f.close()
            pic = Image.open(filename)
            pic = ImageTk.PhotoImage(pic.resize((300,int(pic.height/pic.width*300))))
            lab = tk.Label(msg_box,image=pic,cursor="hand2",borderwidth=0)
            lab.image = pic
            lab.bind("<Button-1>",lambda event:os.startfile(filename))
            msg_box.window_create(f"{row}.{column}",window=lab)
        else:
            file_label_list.append(tk.Label(msg_box,compound='right',cursor="hand2",borderwidth=10,text=filepath[-len(extended_name)-33:-len(extended_name)-1]+" ",image=extended_name_list[extended_name] if extended_name in extended_name_list else None))
            file_label_list[-1].bind("<Button-1>",lambda event:webopen(filepath))
            msg_box.window_create(f"{row}.{column}",window=file_label_list[-1])
        AnalysisFile()
    except:
        pass

def AnalysisUrl():
    try:
        row,column = msg_box.search("链接{",1.0,'end').split(".")
        row,column = int(row),int(column)
        msg_box.delete(f"{row}.{column}",f"{row}.{column+3}")
        url = ""
        idx = 0
        content = msg_box.get(f"{row}.{column+idx}",f"{row}.{column+idx+1}")
        while content != "}":
            idx += 1
            url += content
            content = msg_box.get(f"{row}.{column+idx}",f"{row}.{column+idx+1}")
        msg_box.delete(f"{row}.{column}",f"{row}.{column+len(url)+1}")
        if url.startswith("https://code.xueersi.com/home/project/detail?lang=code&pid="):
            headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
            }
            id = findall(r'\d+',url)[0]
            response = requests.get(f"https://code.xueersi.com/api/compilers/v2/{id}", headers=headers)
            name = response.json()["data"]["name"]
        else:
            name = url
        url_label_list.append(tk.Label(msg_box,text=name,fg="#3F9CD6",bg="#222222",cursor="hand2",font=("宋体",15,"underline")))
        url_label_list[-1].bind("<Button-1>",lambda event:webopen(url))
        msg_box.window_create(f"{row}.{column}",window=url_label_list[-1])
        AnalysisUrl()
    except:
        pass

def using_hot_key_to_close_root(event):
    global using_hot_key_to_close_root_flag
    using_hot_key_to_close_root_flag = 1
    root.destroy()

def loop():
    global last,flag,file_label_list,url_label_list
    last = ""
    while True:
        last1 = read_from_cloud("聊天记录", 10583579, 'file', project_id)
        if last1 != last:
            last = last1
            msg_box.config(state=tk.NORMAL)
            msg_box.delete(1.0,tk.END)
            msg_box.insert(tk.END,last)
            for k in color_dict:
                AnalysisColor(k)
            file_label_list = []
            url_label_list = []
            AnalysisFile()
            AnalysisUrl()
            msg_box.config(state=tk.DISABLED)
            msg_box.see('end')
            _pos = '1.0'
            _target_string = "≈▶"
            while True:
                _idx = msg_box.search(_target_string,_pos,'end')
                if not _idx:
                    break
                _pos = f"{_idx}+{len(_target_string)}c"
                msg_box.tag_add("thin_fg",_idx,_pos)
        if flag == True:
            msg_entry.delete(1.0,tk.END)
            flag = False


using_search_flag = 0
using_choose_appellation_flag = 0
using_notice_flag = 0
using_send_file_flag = 0
using_hot_key_to_close_root_flag = 0

p = Thread(target=loop)
p.start()

def insert_enter(event):
    pass

def change_color(event,target,color):
    global using_search_flag
    if not using_search_flag:
        target["fg"] = color

def search(event):
    global using_search_flag
    global using_choose_appellation_flag
    global using_notice_flag
    if using_choose_appellation_flag or using_notice_flag:
        return
    global search_window
    global search_window_background
    if using_search_flag:
        search_window.destroy()
        search_window_background.destroy()
        using_search_flag = 0
        search_label["fg"] = "#828282"
    else:
        using_search_flag = 1
        search_label["fg"] = "white"
        search_window = tk.Toplevel(root)
        search_window.geometry(f"600x400+{(WIDTH-600)//2}+{(HEIGHT-400)//2-50}")
        search_window.overrideredirect(True)
        search_window_background = tk.Toplevel(root)
        search_window_background.geometry(f"600x400+{(WIDTH-600)//2}+{(HEIGHT-400)//2-50}")
        search_window_background.overrideredirect(True)
        search_window_background.attributes("-topmost",'true')
        background_index = randint(2,20)
        if background_index > 1:
            search_background = ImageTk.PhotoImage(Image.open(os.getcwd()+f"\\image/搜索背景{background_index}.jpg").resize((711,400)))
            search_window.attributes("-alpha",0.5)
        else:
            search_background = ImageTk.PhotoImage(Image.open(os.getcwd()+f"\\image/搜索背景{background_index}.jpg"))
            search_window.attributes("-alpha",0.7)
        background_label = tk.Label(search_window_background,image=search_background,borderwidth=0)
        background_label.pack()
        search_window["bg"] = "#E0E0E0"
        top_frame = tk.Frame(search_window,height=20,bg="#E0E0E0")
        top_frame.pack(fill='x')
        close_label = tk.Label(top_frame,text="×",font=("宋体",15),bg="#E0E0E0",cursor="hand2")
        close_label.pack(side='right',ipadx=3,ipady=3)
        title = tk.Label(search_window,text="搜索消息",bg="#E0E0E0",font=("宋体",25,"bold"))
        title.pack()
        middle_frame = tk.Frame(search_window,height=40,bg="#E0E0E0")
        middle_frame.pack()
        search_entry = tk.Text(search_window,font=("宋体",20),width=30,height=8,bg="#E0E0E0")
        search_entry.pack()
        def fn(event):
            target_string = search_entry.get(1.0,'end')[:-1]
            if target_string == "":
                return
            title.pack_forget()
            middle_frame.pack_forget()
            search_entry.pack_forget()
            res_Label = tk.Label(search_window,text="搜索结果如下",bg="#E0E0E0",font=("宋体",25,"bold"))
            res_Label.pack(ipadx=6,ipady=6)
            res_text = tk.Text(search_window,font=("宋体",15),bg="#E0E0E0")
            res_text.pack()
            res_text.tag_config("style1",background="yellow",foreground="red")
            # search_window.tag_add()
            _chat_last = last
            for _ in color_dict:
                _chat_last = _chat_last.replace(f"\\{color_dict[_]}","")
                _chat_last = _chat_last.replace(f"{color_dict[_]}\\","")
            for k in _chat_last.split("\n"):
                if target_string in k:
                    res_text.insert('end',k+"\n")
            pos = '1.0'
            while True:
                idx = res_text.search(target_string,pos,'end')
                if not idx:
                    break
                pos = f"{idx}+{len(target_string)}c"
                res_text.tag_add("style1",idx,pos)

        def close(event):
            global using_search_flag
            search_window.destroy()
            search_window_background.destroy()
            search_label["fg"] = "#828282"
            using_search_flag = 0

        search_entry.bind("<Return>",fn)
        close_label.bind("<Button-1>",close)
        search_window_background.update()
        search_window.attributes("-topmost",'true')
        while True:
            try:
                search_window.update()
            except:
                break

def choose_appellation(event):
    global using_search_flag
    global using_choose_appellation_flag
    global a_win
    if using_search_flag:
        return
    if using_choose_appellation_flag:
        a_win.destroy()
        using_choose_appellation_flag = 0
    else:
        using_choose_appellation_flag = 1
        a_win = tk.Tk()
        a_win.title("称号设置")
        a_win.geometry(f"+{(WIDTH-a_win.winfo_reqwidth())//2}+{(HEIGHT-a_win.winfo_reqheight())//2-50}")
        appellation_var_list = {}
        checkbutton_list = {}
        appellation_list = ["无","Carry全场","编程王者","12345678987654321","【社区】元老","高手","极客","666666"]
        style = ttk.Style()
        style.configure("TCheckbutton",font=("宋体",28))
        def fn(_appellation_index):
            if appellation_var_list[f"v{_appellation_index+1}"].get() == 1:
                f = open("D:\\EasyChat-Dev/appellation.dat","w")
                f.write(str(_appellation_index))
                f.close()
                for _ in range(THE_NUMBER_OF_APPELLATION):
                    if _ != _appellation_index:
                        appellation_var_list[f"v{_+1}"].set(0)

        def ok():
            global name
            f = open("D:\\EasyChat-Dev/appellation.dat","r")
            _index = int(f.read())
            name = appellation[_index][0]+"\\青"+realname+"青\\"+appellation[_index][1]
            close_appellation_window()
        
        appellation_value = int(open("D:\\EasyChat-Dev/appellation.dat","r").read())

        for i in range(THE_NUMBER_OF_APPELLATION):
            appellation_var_list[f"v{i+1}"] = tk.IntVar(master=a_win)
            if i != appellation_value:
                appellation_var_list[f"v{i+1}"].set(0)
            else:
                appellation_var_list[f"v{i+1}"].set(1)
            checkbutton_list[f"c{i+1}"] = ttk.Checkbutton(a_win,text=appellation_list[i],variable=appellation_var_list[f"v{i+1}"],onvalue=1,offvalue=0,command=lambda _i=i:fn(_i))
            checkbutton_list[f"c{i+1}"].pack()
        a_button = ttk.Button(a_win,text="确定",command=ok)
        a_button.pack()
        def close_appellation_window():
            global using_choose_appellation_flag
            using_choose_appellation_flag = 0
            a_win.destroy()
        a_win.protocol("WM_DELETE_WINDOW",close_appellation_window)
        a_win.mainloop()

def notice_change(event,data):
    if not using_notice_flag:
        if data:
            notice_label.configure(image=notice_change_image)
            return
        notice_label.configure(image=notice_image)

def notice(event):
    global using_notice_flag,n_win
    if using_choose_appellation_flag or using_search_flag:
        return
    if using_notice_flag:
        using_notice_flag = 0
        n_win.destroy()
        notice_change(0,0)
        return
    notice_change(0,1)
    using_notice_flag = 1
    n_win = tk.Toplevel(root)
    n_win.title("公告")
    n_win["bg"] = "white"
    n_win.geometry(f"400x300+{(WIDTH-400)//2}+{(HEIGHT-300)//2-50}")
    notice_data = {}
    pro = tk.Label(n_win,image=eval(notice_data["profile"]),borderwidth=0,compound="left",text=" "+notice_data["user"]+"\n "+notice_data["time"],bg="white")
    pro.pack(padx=7,pady=7,anchor="nw")
    noticeboard = tk.Text(n_win,font=("宋体",15),width=40,height=10)
    noticeboard.insert('end',notice_data["text"])
    noticeboard.pack(padx=5,pady=5,anchor="w")
    noticeboard.config(state=tk.DISABLED)
    style = ttk.Style()
    style.configure("编辑.TButton",background="white",foreground="green")
    style.configure("保存.TButton",background="white",foreground="green")
    def edit():
        noticeboard.config(state=tk.NORMAL)
        notice_button.pack_forget()
        save_button = ttk.Button(n_win,text="保存",style="保存.TButton",command=lambda:save(noticeboard.get(1.0,'end')[:-1]))
        save_button.pack()
    def save(text):
        data = {"text":text,"time":strftime('%Y-%m-%d', localtime()),"user":realname}
        data["profile"] = "profile"
        save_to_cloud("公告",str(data),10583579,123456)
        noticeboard.config(state=tk.DISABLED)
        n_win.destroy()
        notice(None)
    def close_notice_window():
        global using_notice_flag
        using_notice_flag = 0
        notice_change(0,0)
        n_win.destroy()

    notice_button = ttk.Button(n_win,style="编辑.TButton",text="编辑",command=edit)
    notice_button.pack()
    n_win.protocol("WM_DELETE_WINDOW",close_notice_window)

    n_win.mainloop()

def send_file(event):
    if using_search_flag or using_choose_appellation_flag or using_notice_flag:
        return
    file_path = filedialog.askopenfilename(title="发送文件")
    if not file_path:
        return
    file_link = XesUploader().uploadAbsolutePath(file_path)
    msg_entry.insert('end',"文件{"+file_link+"}")

def send_file_logo_change(event,data):
    if not using_send_file_flag:
        if data:
            sendfile_label.configure(image=sendfile_change_image)
            return
        sendfile_label.configure(image=sendfile_image)

def chat_help():
    pass

def window_change(event):
    if root.state() == 'normal':
        root.iconify()
    else:
        root.state('normal')

def insert_link(event):
    link_window = tk.Toplevel(root)
    link_window.mainloop()

def main():
    global msg_box
    global msg_entry
    global color_dict
    global search_label
    global root
    global notice_label
    global notice_change_image
    global notice_image
    global sendfile_label
    global sendfile_image
    global sendfile_change_image
    global last
    global word_icon
    global pdf_icon
    global extended_name_list

    root = tk.Tk()
    root["bg"] = "#222222"
    root.title('EasyChat-Dev')
    root.geometry(f'1000x720+{(WIDTH-1000)//2}+{(HEIGHT-720)//2-50}')
    leftframe = tk.Frame(root,width=50,bg='#333333')
    rightframe = tk.Frame(root,bg='#222222')
    leftframe.pack(side='left',fill='y')
    rightframe.pack(side='right',expand=True,fill="both")
    bottomframe = tk.Frame(rightframe,bg="#787878",height=100)
    bottomframe.pack(fill="x",side="bottom")
    scrollbar = tk.Scrollbar(bottomframe)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    msg_entry = tk.Text(bottomframe,height=8,bg="#E8E8E8",font=("宋体",18))
    msg_entry.config(yscrollcommand=scrollbar.set)
    msg_entry.pack(fill='both')
    scrollbar1 = tk.Scrollbar(rightframe)
    scrollbar1.pack(side=tk.RIGHT, fill=tk.Y)
    msg_box = tk.Text(rightframe,bg="#222222",font=("宋体",15),fg='white')
    msg_box.pack(side='left',fill='both',expand=True)
    msg_box.config(yscrollcommand=scrollbar1.set)

    # last = ""
    # print(last)
    msg_box.insert(tk.END,last)
    msg_box.config(state=tk.DISABLED)

    msg_box.tag_config("red_fg",foreground="red")
    msg_box.tag_config("orange_fg",foreground="orange")
    msg_box.tag_config("yellow_fg",foreground="yellow")
    msg_box.tag_config("light_green_fg",foreground="#80FF40")
    msg_box.tag_config("green_fg",foreground='green')
    msg_box.tag_config("light_blue_fg",foreground="cyan")
    msg_box.tag_config("blue_fg",foreground="blue")
    msg_box.tag_config("purple_fg",foreground="purple")
    msg_box.tag_config("gray_fg",foreground="gray")
    msg_box.tag_config("black_fg",foreground="#222222")
    msg_box.tag_config("pink_fg",foreground="#BC6CC3")
    msg_box.tag_config("light_red_fg",foreground="#FF6060")
    msg_box.tag_config("cyan_fg",foreground="#009080")
    msg_box.tag_config("bold_fg",font=("宋体",18,'bold'))
    msg_box.tag_config("thin_fg",font=("宋体",11))
    msg_box.tag_config("pure_blue_fg",foreground="#4750E9")
    msg_box.tag_config("gray1_fg",foreground="#ACACAC")
    msg_box.tag_config("gray2_fg",foreground="#575757")


    color_dict = {
        'light_red': '浅红',
        'light_blue': '浅蓝',
        'light_green': '浅绿',
        'pure_blue': '纯蓝',
        'gray1':'灰1',
        'gray2':"灰2",
        'red': '红',
        'orange':'橙',
        'green': '绿',
        'blue': '蓝',
        'purple': '紫',
        'gray': '灰',
        "black": '黑',
        'bold': '粗',
        'pink': '粉',
        'cyan': '青',
        'yellow': '黄'
    }

    # 此行代码在学而思环境下无法正常工作，只能替换为汉字
    search_label = tk.Label(leftframe,text="搜",bg="#333333",fg="#828282",font=("宋体",25),cursor="hand2")
    search_label.pack(padx=7,pady=7)

    appellation_image = ImageTk.PhotoImage(Image.open(os.getcwd()+"\\Image/称号.png").resize((50,50)))
    appellation_label = tk.Label(leftframe,cursor="hand2",image=appellation_image)
    appellation_label.pack(side="bottom")

    notice_image = ImageTk.PhotoImage(Image.open(os.getcwd()+"\\Image/公告.png").resize((33,33)))
    notice_change_image = ImageTk.PhotoImage(Image.open(os.getcwd()+"\\Image/公告高亮版.png").resize((33,33)))
    notice_label = tk.Label(leftframe,cursor="hand2",image=notice_image,borderwidth=0)
    notice_label.pack(padx=7,pady=7)

    sendfile_image = ImageTk.PhotoImage(Image.open(os.getcwd()+"\\Image/文件图标.png").resize((33,33)))
    sendfile_change_image = ImageTk.PhotoImage(Image.open(os.getcwd()+"\\Image/文件图标高亮版.png").resize((33,33)))
    sendfile_label = tk.Label(leftframe,cursor="hand2",image=sendfile_image,borderwidth=0)
    sendfile_label.pack(padx=7,pady=18)

    link_label = tk.Label(leftframe,text="链",bg="#333333",fg="#828282",font=("宋体",25),cursor="hand2")
    link_label.pack(padx=7,pady=7)

    word_icon = ImageTk.PhotoImage(Image.open(os.getcwd()+"\\Image/word.ico").resize((50,50)))
    pdf_icon = ImageTk.PhotoImage(Image.open(os.getcwd()+"\\Image/pdf.png").resize((38,50)))
    picture_icon = 0#ImageTk.PhotoImage(Image.open(os.getcwd()+"\\Image/picture.png").resize((52,52)))
    extended_name_list = {'word':word_icon,'pdf':pdf_icon,"png":picture_icon,"jpg":picture_icon,"gif":picture_icon,"jpeg":picture_icon,"ico":picture_icon}

    msg_entry.bind("<Control-Return>",insert_enter)
    msg_entry.bind("<Return>",send_msg)
    search_label.bind("<Enter>",lambda event,target=search_label,color="white":change_color(event,target,color))
    search_label.bind("<Leave>",lambda event,target=search_label,color="#828282":change_color(event,target,color))
    search_label.bind("<Button-1>",search)
    link_label.bind("<Enter>",lambda event,target=link_label,color="white":change_color(event,target,color))
    link_label.bind("<Leave>",lambda event,target=link_label,color="#828282":change_color(event,target,color))
    link_label.bind("<Button-1>",insert_link)
    notice_label.bind("<Enter>",lambda event,_data=1:notice_change(event,_data))
    notice_label.bind("<Leave>",lambda event,_data=0:notice_change(event,_data))
    notice_label.bind("<Button-1>",notice)
    appellation_label.bind("<Button-1>",choose_appellation)
    sendfile_label.bind("<Button-1>",send_file)
    sendfile_label.bind("<Enter>",lambda event, data=1:send_file_logo_change(event,data))
    sendfile_label.bind("<Leave>",lambda event, data=0:send_file_logo_change(event,data))

    def root_close():
        if not using_hot_key_to_close_root_flag:
            root.destroy()
            os._exit(0)

    root.protocol("WM_DELETE_WINDOW",root_close)
    root.mainloop()

if __name__ == '__main__':
    main()