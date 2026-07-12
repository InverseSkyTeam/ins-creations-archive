from tkinter import Frame,Tk
import ctypes
from uuid import uuid4
import clr
from webview.window import Window
from webview.platforms.edgechromium import EdgeChrome
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Threading')
from System.Windows.Forms import Control
from System.Threading import Thread,ApartmentState,ThreadStart


windows = []
user32=ctypes.windll.user32
class WebView2(Frame):
    '''tkinter的WebView2绑定，基于pywebview & pythonnet'''

    def __init__(self,parent,width:int,height:int,url:str='',**kw):
        Frame.__init__(self,parent,width=width,height=height,**kw)
        control=Control()
        uid = 'master' if len(windows) == 0 else 'child_' + uuid4().hex[:8]
        window=Window(uid,str(id(self)), url=None, html=None, js_api=None, width=width, height=height, x=None, y=None,
                      resizable=True, fullscreen=False, min_size=(200, 100), hidden=False,
                      frameless=False, easy_drag=True,
                      minimized=False, on_top=False, confirm_close=False, background_color='#FFFFFF',
                      transparent=False, text_select=False, localization=None)
        self.web_view=EdgeChrome(control,window)
        self.control=control
        self.web=self.web_view.web_view
        windows.append(window)
        self.width=width
        self.height=height
        self.parent=parent
        self.chwnd=int(str(self.control.Handle))
        user32.SetParent(self.chwnd,self.winfo_id())
        user32.MoveWindow(self.chwnd,0,0,width,height,True)
        self.__go_bind()

    def __go_bind(self):
        self.bind('<Destroy>',lambda event:self.web.Dispose())
        self.bind('<Configure>',self.__resize_webview)
    def __resize_webview(self,event):
        user32.MoveWindow(self.chwnd,0,0,self.winfo_width(),self.winfo_height(),True)

    def get_url(self):
        #返回当前url，若果没有则为空
        return self.web_view.get_current_url()

    def evaluate_js(self,script):
        #执行javascript代码，并返回最终结果
        return self.web_view.evaluate_js(script)

    def load_css(self,css):
        #加载css
        self.web_view.load_css(css)

    def load_html(self,content,base_uri=None):
        #加载HTML代码
        #content=HTML内容
        #base_uri=基本URL，默认为启动程序的目录
        self.web_view.load_html(content,base_uri)

    def load_url(self,url):
        #加载全新的URL
        self.web_view.load_url(url)

def have_runtime():#检测是否含义webview2 runtime
    from webview.platforms.winforms import _is_chromium
    return _is_chromium()

def install_runtime():#安装webview2 runtime
    from urllib import request
    import subprocess
    import os
    url=r'https://go.microsoft.com/fwlink/p/?LinkId=2124703'
    path=os.getcwd()+'\\webview2runtimesetup.exe'
    unit=request.urlopen(url).read()
    with open(path,mode='wb') as uf:
        uf.write(unit)
    cmd=path
    p=subprocess.Popen(cmd,shell=True)
    return_code=p.wait()#等待子进程结束
    os.remove(path)
    return return_code

def main():
    if not have_runtime():#没有webview2 runtime
        install_runtime()
    root=Tk()
    root.title('pywebview for tkinter test')
    root.geometry('1200x600+5+5')

    frame=WebView2(root,500,500)
    frame.pack(side='left',padx=20,fill='both',expand=True)
    frame.load_url('https://code.xueersi.com/')

    root.mainloop()

if __name__ == "__main__":
    print()
    t = Thread(ThreadStart(main))
    t.ApartmentState = ApartmentState.STA
    t.Start()
    t.Join()
