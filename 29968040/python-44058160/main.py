from code_in_py import *
cppcoder=CloudCodeRun(7,"cpp")
#cppcoder=CloudCodeRun(15,"py3")
import tkinter as tk
#import subprocess
"""from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import get_formatter_by_name
import subprocess

ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
tkinter_tags = {
    '30': 'black',
    '31': 'red',
    '32': 'green',
    '33': 'yellow',
    '34': 'blue',
    '35': 'magenta',
    '36': 'cyan',
    '37': 'white'
}

def ansi_to_tkinter(text):
    def replace(m):
        code = m.group(0)[2:-1]
        if code.startswith('['):
            code = code[1:]
        if code.endswith('m'):
            code = code[:-1]
        fgcolor = tkinter_tags.get(code, '')
        return f'<{fgcolor}>'

    return ansi_escape.sub(replace, text)
def on_code_change(code):
    lexer = get_lexer_by_name("cpp")
    formatter = get_formatter_by_name('terminal')
    highlighted_code = highlight(code, lexer, formatter)
    '''f=open('cs.txt','w')
    f.write(remove_color_code(highlighted_code))
    f.close()'''
    return highlighted_code

"""
def run_code():
    # 获取代码文本框中的内容
    code = code_text.get(1.0, tk.END)
    # 获取标准输入框中的内容
    stdin_text = stdin_entry.get()
    output_text.configure(state='normal',fg='white')
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, '代码正在运行中...')
    root.update()
    output=cppcoder.run(code,stdin_text)
    if output[0]=='':
        h='2'
    else:
        h=str(len(output[0].split('\n'))+1)
    #print(output[0].split('\n'))
    #print(h)
    output=output[0]+'\n'+output[1]
    # 在输出框中显示运行结果
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, output)
    output_text.tag_add("my_tag",float(h+'.0'),tk.END)
    output_text.tag_config("my_tag",foreground="red")
    output_text.configure(state='disabled')
def run_code1():
    import threading as thr
    tt=thr.Thread(target=run_code,name="T1")
    tt.start()
# 创建主窗口
"""print(on_code_change('''print(1)
print(123)'''))"""
#print(parse_color_string(r"\033[33mHello, World!\033[0m"))
root = tk.Tk()
root.title('C++代码运行')
width = 800
height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - width) // 2
y = (screen_height - height) // 2
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
# 创建代码文本框
code_label = tk.Label(root, text='代码区:')
code_label.place(x=10, y=10)
txt_c=tk.Scrollbar(root)
txt_c.place(x=490,y=30,height=550)
code_text = tk.Text(root, undo=True,yscrollcommand=txt_c.set,font=["微软雅黑",14])
code_text.place(x=10, y=30,height=550, width=480)
code_text.insert(tk.END, """#include <iostream>
using namespace std;

int main()
{
    cout << "Nice to meet you.";
    return 0;
}""")
#print(ansi_to_tkinter(on_code_change(code_text.get(1.0, tk.END))))
#code_text.insert(tk.END,)
#code_text.bind("<<Modified>>", on_code_change)

# 创建标准输入输入框
stdin_label = tk.Label(root, text='输入区:')
stdin_label.place(x=520, y=10)

stdin_entry = tk.Entry(root,width=38,)
stdin_entry.place(x=520, y=30)

# 创建输出框
output_label = tk.Label(root, text='输出区:')
output_label.place(x=520, y=60)
txt_s=tk.Scrollbar(root)
txt_s.place(x=770,y=80,height=500)
output_text = tk.Text(root,bg="black",fg="white",yscrollcommand=txt_s.set,font=["微软雅黑",14])
output_text.place(x=520, y=80,height=500,width=250)
output_text.configure(state='disabled')
# 创建运行按钮
run_button = tk.Button(root, text='运行', command=run_code1)
run_button.place(x=455, y=30)

# 运行主循环
root.mainloop()