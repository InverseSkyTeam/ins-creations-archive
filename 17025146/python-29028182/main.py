#1、使用webview
import webview
webview.create_window("百度","https://www.baidu.com")
webview.start()

#2、通过多线程，实现在tkinter中内嵌cefpython组件
from cefpython3 import cefpython as cef
from tkinter import *
import threading
import sys
def embed_browser_thread(frame, _rect):
    sys.excepthook = cef.ExceptHook
    window_info = cef.WindowInfo(frame.winfo_id())
    window_info.SetAsChild(frame.winfo_id(), _rect)
    cef.Initialize()
    cef.CreateBrowserSync(window_info, url='http://www.baidu.com')
    cef.MessageLoop()


if __name__ == '__main__':
    root = Tk()
    root.geometry("800x600")

    frame1 = Frame(root,height=600)
    frame1.pack(side=TOP, fill=X)

    rect = [0, 0, 800, 600]
    thread = threading.Thread(target=embed_browser_thread, args=(frame1, rect))
    thread.start()

    root.mainloop()
    
#3、在tkinter中内嵌miniblink组件
from tkinter import *
from MBPython import miniblink


a=Tk()
a.geometry("1000x600")
a.update()#更新窗口状态和信息

mbpython=miniblink.Miniblink
mb=mbpython.init('node.dll')#操作核心

wke=mbpython(mb)#得到wke控制权
window=wke.window#miniblink的界面容器

webview=window.wkeCreateWebWindow(2,a.winfo_id(),0,0,1000,500)#核心组件
#webview=window.wkeCreateWebWindow(2,tk窗口id,x坐标,y坐标,宽度,高度)
mb.wkeLoadURLW(webview,'http://www.baidu.com/')#载入百度网页
window.wkeShowWindow(webview)#显示组件
# window.wkeRunMessageLoop()
a.mainloop()

#4、使用cefpython原生窗口
from cefpython3 import cefpython as cef
cef.Initialize()
cef.CreateBrowserSync(url="https://www.baidu.com",window_title="baidu")
cef.MessageLoop()

