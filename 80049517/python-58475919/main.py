from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import filedialog

from utils import get_uid_from_url
from api import ProjectAPI
from logger import Logger

import _thread
import pickle
import requests
import os
import sys


class MainWindow(Tk):
    def __init__(self):
        super().__init__()

        self.title_text = None
        self.sub_title_text = None
        self.coo_kie_frame = None
        self.coo_kie_input = None
        self.get_coo_kie = None
        self.url_frame = None
        self.url_input = None
        self.submit = None
        self.config = {}
        self.logger = Logger("CCDown")

        self.title("CCDown")
        self.setup_ui()
        self.load_config()

    def load_config(self):
        try:
            file = open("config.pickle", "rb")
            file.close()
        except FileNotFoundError:
            self.logger.info("配置文件不存在，正在创建")
            self.config = {"coo" + "kie": ""}
            self.save_config()
        else:
            self.logger.info("正在读取配置文件")
            with open("config.pickle", "rb") as file:
                self.config = pickle.load(file)
        self.config_widgets()

    def save_config(self):
        self.logger.info("正在保存配置文件")
        with open("config.pickle", "wb") as file:
            pickle.dump(self.config, file)

    def signin_event(self):
        self.logger.info("采用 webview2 登录")
        try:
            import xes_login
        except Exception as e:
            self.logger.format_exc()
            self.logger.error("发生了个错误，错误信息为：", e)
            messagebox.showerror(title="错误", message="你没有在库管理安装 pywebview")
            return
        else:
            messagebox.showinfo(title="提示", message="请在即将弹出的窗口进行登录")
            coo_kie = xes_login.login_to_get_coo_kie()

        if coo_kie:
            self.config["coo" + "kie"] = coo_kie
            self.save_config()
            self.logger.info("获取 coo" + "kie 成功")
            messagebox.showinfo(title="成功", message="成功获取 coo" + "kie，请重启程序")
            sys.exit()
        else:
            messagebox.showerror(title="错误", message="你没有在弹出的窗口登录")

    def save_project(self):
        if not self.url_input.get():
            messagebox.showerror(title="错误", message="未输入作品链接")
            return

        messagebox.showinfo(title="提示",
                            message="请在即将弹出的弹窗选择要保存的位置，将在这个位置下载而不是再新建一个文件夹")
        save_to = filedialog.askdirectory(title="在何处保存作品？")
        if not save_to:
            self.logger.error("未选择保存位置")
            messagebox.showerror(title="错误", message="未选择保存位置")
            return

        coo_kie = self.config["coo" + "kie"]
        header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61'
        }

        uid = get_uid_from_url(self.url_input.get())
        self.logger.debug(f"作品ID为 {uid}，将要保存到 {save_to}")
        if uid == 0:
            self.logger.error("错误的作品链接")
            messagebox.showerror(title="错误", message="错误的作品链接")
            return

        api = ProjectAPI(coo_kie, header)
        data = api.get_project(uid)

        if data.get("main.py") is None:
            self.logger.error(data["message"])
            messagebox.showerror("错误", data["message"])
            return
        else:
            self.logger.debug(data["message"])
            

        self.logger.info("正在保存 /main.py")
        with open(save_to + "/main.py", "w", encoding="utf-8") as file:
            file.write(data["main.py"])

        for i in data["assets"]:
            need_make_dirs = i["saveto"].split("/")
            need_make_dirs.pop(0)
            current_path = ""
            for j in need_make_dirs:
                current_path = current_path + "/" + j
                if not os.path.exists(save_to + current_path):
                    self.logger.info(f"正在创建 {current_path} 文件夹")
                    os.mkdir(save_to + current_path)

            self.logger.info(f"正在下载 {i['path']}")
            with open(save_to + i["path"], "wb") as file:
                res = requests.get(i["url"], headers=header)
                file.write(res.content)

        self.logger.info("下载完毕")
        messagebox.showinfo(title="成功", message="下载完成")

    def setup_ui(self):
        normal_font = ("Microsoft YaHei UI", 10)
        self.logger.info("正在配置UI")

        self.title_text = Label(self, text="CCDown", font=("Microsoft YaHei UI", 30))
        self.title_text.pack()

        self.sub_title_text = Label(self, text="为下载完整学而思编程 Python 作品而生", font=("Microsoft YaHei UI", 12))
        self.sub_title_text.pack()

        self.coo_kie_frame = LabelFrame(self, text="coo" + "kie 配置")

        self.coo_kie_input = Entry(self.coo_kie_frame, font=normal_font, state="readonly")
        self.coo_kie_input.pack(side=LEFT, fill=X, expand=True)

        self.get_coo_kie = Button(self.coo_kie_frame, text="获取 coo" + "kie",
                                 command=self.signin_event)
        self.get_coo_kie.pack(side=RIGHT)

        self.coo_kie_frame.pack()

        self.url_frame = LabelFrame(self, text="url 设置")

        self.url_input = Entry(self.url_frame, font=normal_font)
  
        self.url_input.pack()

        self.url_frame.pack()

        self.submit = Button(self, text="开始爬取作品文件",
                             command=lambda: _thread.start_new_thread(self.save_project, tuple()))
        self.submit.pack()

    def config_widgets(self):
        self.logger.info("正在配置控件")
        self.coo_kie_input.config(state="normal")
        self.coo_kie_input.delete(0, END)
        self.coo_kie_input.insert(0, self.config['coo' + 'kie'])
        self.coo_kie_input.config(state="readonly")


if __name__ == "__main__":
    # set_config()  # 手动设置coo-kie
    root = MainWindow()
    root.mainloop()
    
    # debug the logger - the better logger
    # logger = Logger("dbg")
    # logger.info("info")
    # logger.warning("warning")
    # logger.error("error\ntraceback\n...")
    # logger.debug("debug")
    # try:
    #     raise Exception("I am a exception")
    # except:
    #     logger.format_exc()
