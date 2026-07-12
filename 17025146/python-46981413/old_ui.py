group = Group(114514,23266222)

class old_UI:
    def __init__(self):
        self.root = tk.Tk()
        self.root["bg"] = "#222222"
        self.root.title('EasyChat-Dev')
        self.root.geometry(f'1000x720+{(WIDTH-1000)//2}+{(HEIGHT-720)//2-50}')

        self.leftframe = tk.Frame(self.root,width=50,bg='#333333')
        self.rightframe = tk.Frame(self.root,bg='#222222')
        self.leftframe.pack(side='left',fill='y')
        self.rightframe.pack(side='right',expand=True,fill="both")
        self.bottomframe = tk.Frame(self.rightframe,bg="#787878",height=100)
        self.bottomframe.pack(fill="x",side="bottom")
        self.scrollbar = tk.Scrollbar(self.bottomframe)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.msg_entry = tk.Text(self.bottomframe,height=8,bg="#E8E8E8",font=("宋体",18))
        self.msg_entry.config(yscrollcommand=self.scrollbar.set)
        self.msg_entry.pack(fill='both')
        self.scrollbar1 = tk.Scrollbar(self.rightframe)
        self.scrollbar1.pack(side=tk.RIGHT, fill=tk.Y)
        self.msg_box = tk.Text(self.rightframe,bg="#222222",font=("宋体",15),fg='white')
        self.msg_box.pack(side='left',fill='both',expand=True)
        self.msg_box.config(yscrollcommand=self.scrollbar1.set)

        self.msg_box = tk.Text(self.rightframe,bg="#222222",font=("宋体",15),fg='white')
        self.msg_box.pack(side='left',fill='both',expand=True)
        self.msg_box.config(yscrollcommand=self.scrollbar1.set)

        self.msg_box.insert(tk.END,last)
        self.msg_box.config(state=tk.DISABLED)

        self.msg_box.tag_config("red_fg",foreground="red")
        self.msg_box.tag_config("orange_fg",foreground="orange")
        self.msg_box.tag_config("yellow_fg",foreground="yellow")
        self.msg_box.tag_config("light_green_fg",foreground="#80FF40")
        self.msg_box.tag_config("green_fg",foreground='green')
        self.msg_box.tag_config("light_blue_fg",foreground="cyan")
        self.msg_box.tag_config("blue_fg",foreground="blue")
        self.msg_box.tag_config("purple_fg",foreground="purple")
        self.msg_box.tag_config("gray_fg",foreground="gray")
        self.msg_box.tag_config("black_fg",foreground="#222222")
        self.msg_box.tag_config("pink_fg",foreground="#BC6CC3")
        self.msg_box.tag_config("light_red_fg",foreground="#FF6060")
        self.msg_box.tag_config("cyan_fg",foreground="#009080")
        self.msg_box.tag_config("bold_fg",font=("宋体",18,'bold'))
        self.msg_box.tag_config("thin_fg",font=("宋体",11))
        self.msg_box.tag_config("pure_blue_fg",foreground="#4750E9")
        self.msg_box.tag_config("gray1_fg",foreground="#ACACAC")
        self.msg_box.tag_config("gray2_fg",foreground="#575757")

        self.color_dict = {
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
        self.search_label = tk.Label(self.leftframe,text="搜",bg="#333333",fg="#828282",font=("宋体",25),cursor="hand2")
        self.search_label.pack(padx=7,pady=7)

        self.appellation_image = ImageTk.PhotoImage(Image.open(os.getcwd()+"\\Image/称号.png").resize((50,50)))
        self.appellation_label = tk.Label(self.leftframe,cursor="hand2",image=self.appellation_image)
        self.appellation_label.pack(side="bottom")

        self.notice_image = ImageTk.PhotoImage(Image.open(os.getcwd()+"\\Image/公告.png").resize((33,33)))
        self.notice_change_image = ImageTk.PhotoImage(Image.open(os.getcwd()+"\\Image/公告高亮版.png").resize((33,33)))
        self.notice_label = tk.Label(self.leftframe,cursor="hand2",image=self.notice_image,borderwidth=0)
        self.notice_label.pack(padx=7,pady=7)

        self.sendfile_image = ImageTk.PhotoImage(Image.open(os.getcwd()+"\\Image/文件图标.png").resize((33,33)))
        self.sendfile_change_image = ImageTk.PhotoImage(Image.open(os.getcwd()+"\\Image/文件图标高亮版.png").resize((33,33)))
        self.sendfile_label = tk.Label(self.leftframe,cursor="hand2",image=self.sendfile_image,borderwidth=0)
        self.sendfile_label.pack(padx=7,pady=18)

        self.link_label = tk.Label(self.leftframe,text="链",bg="#333333",fg="#828282",font=("宋体",25),cursor="hand2")
        self.link_label.pack(padx=7,pady=7)

        self.word_icon = ImageTk.PhotoImage(Image.open(os.getcwd()+"\\Image/word.ico").resize((50,50)))
        self.pdf_icon = ImageTk.PhotoImage(Image.open(os.getcwd()+"\\Image/pdf.png").resize((38,50)))
        self.picture_icon = 0#ImageTk.PhotoImage(Image.open(os.getcwd()+"\\Image/picture.png").resize((52,52)))
        self.extended_name_list = {'word':self.word_icon,'pdf':self.pdf_icon,"png":self.picture_icon,"jpg":self.picture_icon,"gif":self.picture_icon,"jpeg":self.picture_icon,"ico":self.picture_icon}

class UI:
    def __init__(self) -> None:
        pass

msg_box,entry = 0,0
ui = UI(msg_box,entry)



class Manager:
    def __init__(self,ui:UI) -> None:
        self.ui = ui
    
    def AnalysisColor(self,color):
        try:
            row,column = msg_box.search(f'\\{self.ui.color_dict[color]}',1.0,'end').split(".")
            row1,column1 = msg_box.search(f'{self.ui.color_dict[color]}\\',1.0,'end').split(".")
            if row < row1:
                if len(self.ui.color_dict[color]) == 1:
                    msg_box.delete(f"{row}.{column}",f"{row}.{int(column)+2}")
                else:
                    msg_box.delete(f"{row}.{column}",f"{row}.{int(column)+3}")
            elif row1 < row:
                if len(self.ui.color_dict[color]) == 1:
                    msg_box.delete(f"{row1}.{int(column1)}",f"{row1}.{int(column1)+2}")
                else:
                    msg_box.delete(f"{row1}.{int(column1)}",f"{row1}.{int(column1)+3}")
            else:
                if len(self.ui.color_dict[color]) == 1:
                    msg_box.delete(row+"."+column,row+"."+str(int(column)+2))
                    msg_box.delete(row+"."+str(int(column1)-2),row+"."+column1)
                    column1 = str(int(column1)-2)
                else:
                    msg_box.delete(row+"."+column,row+"."+str(int(column)+3))
                    msg_box.delete(row+"."+str(int(column1)-3),row+"."+column1)
                    column1 = str(int(column1)-3)
                target_string = msg_box.get(row+"."+column,row+"."+column1)
                msg_box.tag_add(f'{color}_fg',f'{row}.{column}',f'{row}.{column}+{len(target_string)}c')
            self.AnalysisColor(color)
        except:
            pass

    def AnalysisFile(self):
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
            if extended_name in self.ui.extended_name_list and not self.ui.extended_name_list[extended_name]:
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
                self.ui.file_label_list.append(tk.Label(msg_box,compound='right',cursor="hand2",borderwidth=10,text=filepath[-len(extended_name)-33:-len(extended_name)-1]+" ",image=self.ui.extended_name_list[extended_name] if extended_name in self.ui.extended_name_list else None))
                self.ui.file_label_list[-1].bind("<Button-1>",lambda event:webbrowser.open(filepath))
                msg_box.window_create(f"{row}.{column}",window=self.ui.file_label_list[-1])
            self.AnalysisFile()
        except:
            pass
    
    def change_color(self,event,target,color):
        global using_search_flag
        if not using_search_flag:
            target["fg"] = color

    def search(self,event):
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
            using_search_flag = False
            self.ui.search_label["fg"] = "#828282"
        else:
            using_search_flag = True
            self.ui.search_label["fg"] = "white"
            search_window = tk.Toplevel(self.self.root)
            search_window.geometry(f"600x400+{(WIDTH-600)//2}+{(HEIGHT-400)//2-50}")
            search_window.overrideredirect(True)
            search_window_background = tk.Toplevel(self.root)
            search_window_background.geometry(f"600x400+{(WIDTH-600)//2}+{(HEIGHT-400)//2-50}")
            search_window_background.overrideredirect(True)
            search_window_background.attributes("-topmost",'true')
            background_index = random.randint(2,20)
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
                _chat_last = last #这个是消息
                for _ in self.color_dict:
                    _chat_last = _chat_last.replace(f"\\{self.color_dict[_]}","")
                    _chat_last = _chat_last.replace(f"{self.color_dict[_]}\\","")
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
                self.ui.search_label["fg"] = "#828282"
                using_search_flag = False

            search_entry.bind("<Return>",fn)
            close_label.bind("<Button-1>",close)
            search_window_background.update()
            search_window.attributes("-topmost",'true')
            while True:
                try:
                    search_window.update()
                except:
                    break
    def search(self,msg_box:tk.Text,message:str,target_string:str):
        _chat_last = message
        for i in self.color_dict:
            _chat_last = _chat_last.replace(f"\\{self.color_dict[i]}","")
            _chat_last = _chat_last.replace(f"{self.color_dict[i]}\\","")
        for k in _chat_last.split("\n"):
            if target_string in k:
                msg_box.insert('end',k+"\n")
        pos = '1.0'
        while True:
            idx = msg_box.search(target_string,pos,'end')
            if not idx:
                break
            pos = f"{idx}+{len(target_string)}c"
            msg_box.tag_add("style1",idx,pos)


    def choose_appellation(event):
        global using_search_flag
        global using_choose_appellation_flag
        global a_win
        if using_search_flag:
            return
        if using_choose_appellation_flag:
            a_win.destroy()
            using_choose_appellation_flag = False
        else:
            using_choose_appellation_flag = True
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
                using_choose_appellation_flag = False
                a_win.destroy()
            a_win.protocol("WM_DELETE_WINDOW",close_appellation_window)
            a_win.mainloop()

    def notice_change(self,event,data):
        if not using_notice_flag:
            if data:
                self.notice_label.configure(image=self.notice_change_image)
                return
            self.notice_label.configure(image=self.notice_image)

    def notice(self,event):
        global using_notice_flag,n_win
        if using_choose_appellation_flag or using_search_flag:
            return
        if using_notice_flag:
            using_notice_flag = False
            n_win.destroy()
            self.notice_change(0,0)
            return
        self.notice_change(0,1)
        using_notice_flag = True
        n_win = tk.Toplevel(self.root)
        n_win.title("公告")
        n_win["bg"] = "white"
        n_win.geometry(f"400x300+{(WIDTH-400)//2}+{(HEIGHT-300)//2-50}")
        self.notice_data = {}
        pro = tk.Label(n_win,image=eval(self.notice_data["profile"]),borderwidth=0,compound="left",text=" "+self.notice_data["user"]+"\n "+self.notice_data["time"],bg="white")
        pro.pack(padx=7,pady=7,anchor="nw")
        self.noticeboard = tk.Text(n_win,font=("宋体",15),width=40,height=10)
        self.noticeboard.insert('end',self.notice_data["text"])
        self.noticeboard.pack(padx=5,pady=5,anchor="w")
        self.noticeboard.config(state=tk.DISABLED)
        style = ttk.Style()
        style.configure("编辑.TButton",background="white",foreground="green")
        style.configure("保存.TButton",background="white",foreground="green")
        def edit():
            self.noticeboard.config(state=tk.NORMAL)
            self.notice_button.pack_forget()
            save_button = ttk.Button(n_win,text="保存",style="保存.TButton",command=lambda:save(self.noticeboard.get(1.0,'end')[:-1]))
            save_button.pack()
        def save(text):
            data = {"text":text,"time":strftime('%Y-%m-%d', localtime()),"user":realname}
            data["profile"] = "profile"
            save_to_cloud("公告",str(data),10583579,123456)
            self.noticeboard.config(state=tk.DISABLED)
            n_win.destroy()
            self.notice(None)
        def close_notice_window():
            global using_notice_flag
            using_notice_flag = False
            self.notice_change(0,0)
            n_win.destroy()

        self.notice_button = ttk.Button(n_win,style="编辑.TButton",text="编辑",command=edit)
        self.notice_button.pack()
        n_win.protocol("WM_DELETE_WINDOW",close_notice_window)

        n_win.mainloop()

    def send_file(self,event):
        if using_search_flag or using_choose_appellation_flag or using_notice_flag:
            return
        file_path = filedialog.askopenfilename(title="发送文件")
        if not file_path:
            return
        file_link = upload(file_path)
        self.ui.msg_entry.insert('end',"文件{"+file_link+"}")

    def send_file_logo_change(self,event,data):
        if not self.using_send_file_flag:
            if data:
                self.ui.sendfile_label.configure(image=self.sendfile_change_image)
                return
            self.ui.sendfile_label.configure(image=self.ui.sendfile_image)