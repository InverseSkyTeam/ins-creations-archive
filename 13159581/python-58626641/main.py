from tkinter import *
import threading,sys,traceback,time

def run_code_in_window(code_text):
    frame3 = Tk()
    frame3.geometry("500x230+0+200")
    frame3.title("CIDE运行分窗口")
    frame3.attributes("-topmost", True)
    yscrollbar2 = Scrollbar(frame3)
    outtext = Text(frame3, height=200, font=(False, 14), bg="black", fg="white", insertbackground="white")
    outtext['state'] = 'disabled'
    yscrollbar2.pack(side=RIGHT, fill=Y)
    outtext.pack()
    yscrollbar2.config(command=outtext.yview)
    outtext.config(yscrollcommand=yscrollbar2.set)
    outtext['state'] = 'normal'
    outtext.delete('1.0', 'end')
    outtext['state'] = 'disabled'
    def submit():
        def print(*value, sep=' ', end='\n'):
            outtext['state'] = 'normal'
            for i in range(len(value)):
                outtext.insert('end', value[i])
                if i < len(value) - 1:
                    outtext.insert('end', sep)
                    
            outtext.insert('end', end)
            outtext.see('end')
            time.sleep(0.03)
            outtext['state'] = 'disabled'


        def input(value=''):
            print(value, end='')
            is_function_finished = BooleanVar()
            is_function_finished.set(False)
            submittext = ""

            def on_key_press(event):
                nonlocal is_function_finished
                nonlocal submittext
                text = event.widget
                line, column = map(int, text.index("insert").split('.'))
                current_line_content = text.get("{}.0".format(line), "{}.end".format(line))
                if event.keysym == "BackSpace":
                    if (not current_line_content.strip().replace(value, "")):
                        return "break"
                    else:
                        submittext = submittext[:-1]
                        last_char_index = 'end-1c'
                        outtext.delete(last_char_index)
                elif event.keysym == "Return":
                    is_function_finished.set(True)
                else:
                    submittext += event.char
                    # outtext.insert('end', event.char)

            outtext['state'] = 'normal'
            outtext.bind("<Key>", on_key_press)
            outtext.wait_variable(is_function_finished)
            outtext.unbind("<Key>")
            outtext["state"] = "disabled"
            return submittext
        
        try:
            sys.stdout.write = print
            sys.stdin.readline = input
            exec(code_text, globals(), locals())
        except Exception as b:
            bug = traceback.format_exc()
            try:
                print(bug)
            except:
                pass
    
    threada = threading.Thread(target=submit)
    threada.daemon = True
    threada.start()
    frame3.mainloop()

if __name__ == '__main__':
    code = "name = input('请输入你的名字：')\nprint('Hello!',name)"
    run_code_in_window(code)