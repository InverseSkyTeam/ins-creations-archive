import wx
import wx.html2 as html
kernel = html.WebViewBackendEdge

class MyFrame(wx.Frame):
    def __init__(self,title,size):
        wx.Frame.__init__(self,parent=None,title=title,size=size)
        self.Centre()
        self.panel = wx.Panel(parent=self)
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.pwdText = wx.TextCtrl(self.panel,-1,"https://www.baidu.com",size=(200,-1),style=wx.TE_PROCESS_ENTER)
        self.browser = html.WebView.New(self.panel,backend=kernel)
        self.browser.EnableHistory(True)
        self.vbox.Add(self.pwdText,0,wx.ALL|wx.EXPAND,border=5)
        self.vbox.Add(self.browser,1,wx.ALL|wx.EXPAND,border=5)
        self.Bind(wx.EVT_TEXT_ENTER,self.go,self.pwdText)
        self.panel.SetSizer(self.vbox)
        
    def loadurl(self,url):
        self.browser.LoadURL(url)
    
    def go(self,event):
        self.loadurl(self.pwdText.GetValue())

class App(wx.App):
    def OnInit(self):
        frame = MyFrame('DreamSky Broser',(1300,800))
        frame.loadurl('https://www.baidu.com')
        frame.Show()
        return True
    def OnExit(self):
        print('浏览器已退出')
        return 0

if __name__ == '__main__':
    app = App()
    app.MainLoop()
