import tkinter as tk,sys
name = 'INS jhx DreamSky simple easy GUI maker-V0.01'

class DreamSkyUI_Error(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return str(self.msg)

class App:
    def __init__(self):
        self.root = tk.Tk()
    def apploop(self,tp='mainloop'):
        if tp == 'mainloop':
            self.root.mainloop()
        elif tp == 'alwaysloop':
            try:
                self.root.update()
            except:
                self.root.destroy()
                sys.exit()
        else:
            raise DreamSkyUI_Error('apploop 函数的tp参数必须是字符串mainloop或者alwaysloop')