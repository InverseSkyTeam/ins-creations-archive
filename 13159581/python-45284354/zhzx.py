from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import Combobox
from urllib.parse import quote

class MainWindow():
    # 初始化
    def __init__(self):
        top_button_width = 10 
        button_relief = RAISED 

        root = Tk()
        self.src_filename = None
        self.count = StringVar()
        self.count.set('0')
        root.title('本地记事本')
        root.resizable(width=False, height=False)

        # 上部控件
        Button(root, text='打开', relief=button_relief, width=top_button_width, command=self.open_button_event).grid(row=0, column=0)
        Button(root, text='新建', relief=button_relief, width=top_button_width, command=self.new_button_event).grid(row=0, column=1)
        Button(root, text='保存', relief=button_relief, width=top_button_width,
               command=self.save_button_event).grid(row=0, column=3)
        Button(root, text='另存为', relief=button_relief, width=top_button_width,
               command=self.other_save_button_event).grid(row=0, column=4)
        Button(root, text='清空', width=top_button_width, command=self.clear_button).grid(row=0, column=5)

        # 空一行
        Label(root, text='').grid(row=1)

        # 左侧控件
        Button(root, text='查找', relief=button_relief, width=top_button_width, command=self.find_button_event) \
            .grid(row=2, column=0, sticky=N)
        self.find_text = Text(root, width=top_button_width, height=2)
        self.find_text.grid(row=2, column=1)
        Label(root, text='查找总数').grid(row=3, column=0, sticky=N)
        self.count_label = Label(root, textvariable=self.count)
        self.count_label.grid(row=3, column=1)
        Button(root, text='替换成', relief=button_relief, width=top_button_width, command=self.replace_button_event).grid(
            row=4, column=0, sticky=N)
        self.replace_text = Text(root, width=top_button_width, height=2)
        self.replace_text.grid(row=4, column=1, sticky=N)
        Button(root, text='大写', relief=button_relief, width=top_button_width, command=self.upper_button_event).grid(
            row=5, column=0, sticky=N)
        Button(root, text='小写', relief=button_relief, width=top_button_width, command=self.lower_button_event).grid(
            row=5, column=1, sticky=N)
        #右侧文本框
        self.text = Text(root)
        self.text.grid(row=2, column=2, columnspan=6, rowspan=15)
    #打开
    def open_button_event(self):
        self.new_button_event()
        # 获取文件名
        self.src_filename = filedialog.askopenfilename(filetypes=[('txt格式', 'txt')])
        if self.src_filename:
            # 获取数据
            data = open(self.src_filename).read()
            # 填充到text控件
            #self.text.delete(1.0, END)
            self.text.insert(INSERT, data)
    #新建
    def new_button_event(self):
        data = self.__get()
        if data and messagebox.askokcancel('提示', '当前内容要进行保存吗？'):
            if self.src_filename:
                self.__sava_data(self.src_filename)
            else:
                self.other_save_button_event()
        self.text.delete(1.0, END)
    #保存按钮
    def save_button_event(self):
        filename = self.src_filename if self.src_filename else filedialog.askopenfilename(filetypes=[('txt格式', 'txt')])
        if filename:
            self.__sava_data(filename)
    #另存为
    def other_save_button_event(self):
        f = filedialog.asksaveasfile(filetypes=[('txt格式', 'txt')])
        if f:
            f.write(self.__get())
    #查找
    def find_button_event(self):
        data = self.__get()
        find_data = self.find_text.get(1.0, END).strip()
        if find_data not in data:
            messagebox.showinfo('提示', '搜索的字符不存在')
        else:
            self.count.set(str(data.count(find_data)))
    #替换
    def replace_button_event(self):
        find_data = self.find_text.get(1.0, END).strip()
        replace_data = self.replace_text.get(1.0, END).strip()
        data = self.__get()
        data = data.replace(find_data, replace_data)
        self.__del_and_set(data)
    #大写
    def upper_button_event(self):
        data = self.__get().upper()
        self.__del_and_set(data)
    #小写
    def lower_button_event(self):
        data = self.__get().lower()
        self.__del_and_set(data)
    #清空
    def clear_button(self):
        self.text.delete(1.0, END)
    #保存文件
    def __sava_data(self, filename):
        with open(filename, 'w') as f:
            f.write(self.__get())
        messagebox.showinfo('提示', '保存成功')
    #获取文本
    def __get(self):
        # 这里一定要有strip
        return self.text.get(1.0, END).strip()
    #更新
    def __del_and_set(self, data):
        self.text.delete(1.0, END)
        self.text.insert(INSERT, data)

MainWindow()
mainloop()
