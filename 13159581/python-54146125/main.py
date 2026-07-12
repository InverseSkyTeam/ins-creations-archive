from tkinter import filedialog,font,messagebox
from tkhtmlview import HTMLLabel
from markdown2 import Markdown
import tkinter as tk
import markdown
import os
 
def markdown_to_html(text):
    return markdown.markdown(text)

class TextEditor:
    def __init__(self):
        self.root = tk.Tk()
        self.myfont = font.Font(family='Helvetica',size=14)
        self.root.geometry("700x630")
        self.root.title("CIDE-md")

        self.frame = tk.Frame(self.root)
        self.text_widget = tk.Text(self.frame,width=1,font=self.myfont)
        self.text_widget.pack(fill=tk.BOTH,expand=1,side=tk.LEFT)
        self.output = HTMLLabel(self.frame,width='1',background='white',html='<h1>hhh</h1>')
        self.output.pack(fill=tk.BOTH,expand=1,side=tk.RIGHT)
        self.output.fit_height()
        self.frame.pack(fill=tk.X)

        self.save_button = tk.Button(self.root, text="保存", command=self.save_file, bd=0, background="grey", activebackground='gold', foreground='lightgreen')
        self.save_button.pack(fill=tk.X)

        self.open_button = tk.Button(self.root, text="打开", command=self.open_file, bd=0, background="grey", activebackground='gold', foreground='lightgreen')
        self.open_button.pack(fill=tk.X)

        self.open_button = tk.Button(self.root, text="转为HTML文件运行", command=self.to_HTML, bd=0, background="grey", activebackground='gold', foreground='lightgreen')
        self.open_button.pack(fill=tk.X)

        self.open_button = tk.Button(self.root, text="就地预览", command=self.output_change, bd=0, background="grey", activebackground='gold', foreground='lightgreen')
        self.open_button.pack(fill=tk.X)

        self.root.protocol("WM_DELETE_WINDOW", self.callback)

    def save_file(self):
        content = self.text_widget.get("1.0", tk.END)
        file_path = filedialog.asksaveasfilename(defaultextension=".md")

        if file_path:
            with open(file_path, "w") as file:
                file.write(content)

    def open_file(self):
        file_path = tk.filedialog.askopenfilename()

        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_widget.delete("1.0", tk.END)
                self.text_widget.insert(tk.END, content)
    
    def to_HTML(self):
        content = self.text_widget.get("1.0", tk.END)
        with open("./md_to_html.html", "w") as file:
            file.write(markdown_to_html(content))
        os.startfile("md_to_html.html")
    
    def output_change(self):
        self.text_widget.edit_modified(False)
        md2html = Markdown()
        self.output.set_html(md2html.convert(self.text_widget.get('1.0',tk.END)))
    
    def run(self):
        self.root.mainloop()

    def callback(self):
        if messagebox.askyesno('关闭', '您确定要关闭CIDE-md吗?'):
            self.root.destroy()
        else:
            pass

# 创建 TextEditor 对象并运行
editor = TextEditor()
editor.run()
