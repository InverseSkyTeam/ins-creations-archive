from cefpython3 import cefpython as cef

def cw(x='https://code.xueersi.com/space/12907647',t='窗口'):
    cef.Initialize()
    cef.CreateBrowserSync(url=x,window_title=t)
    cef.MessageLoop()
    cef.Shutdown()

cw(x="https://code.xueersi.com/")