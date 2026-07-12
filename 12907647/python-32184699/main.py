from cefpython3 import cefpython as cef
import tkinter as tk,webbrowser as w
root = tk.Tk()
root.title('INS-SkyLight浏览器')
root.configure(background="lightgreen")
def cw(x='https://code.xueersi.com/space/12907647',t='窗口'):
    cef.Initialize()
    cef.CreateBrowserSync(url=x,window_title=t)
    cef.MessageLoop()
def search_b():
    text = search_entry.get()
    cw(x='https://www.baidu.com/s?wd='+text)
def search_360():
    text = search_entry.get()
    cw(x='https://www.so.com/s?ie=utf-8&fr=so.com&src=home_so.com&nlpv=basest&q='+text)
def search_s():
    text = search_entry.get()
    cw(x='https://www.sogou.com/web?query='+text)
def search_by():
    text = search_entry.get()
    cw(x='https://cn.bing.com/search?q='+text)
def search_y():
    text = search_entry.get()
    cw(x='http://youdao.com/w/eng/'+text+'/#keyfrom=dict2.index')
def search_g():
    text = search_entry.get()
    cw(x='https://translate.google.cn/?sourceid=cnhp&sl=auto&tl=zh-CN&text='+text+'&op=translate')
def search_ok():
    text = search_entry.get()
    if ('http' not in text) and ('://' not in text):
        Tip['text']='请输入完整链接再点击(检查是否缺少http/https/www/字母等)'
    else:
        Tip['text']='小轩浏览器，无敌的浏览器'
        cw(x=text)
def search_insxe():   # ins是逆天团队，x是小轩，e是浏览器
    cw(x='http://127.0.0.1:55824/index.html')
    
search_entry = tk.Entry(root,background='lightyellow',border=4,width=100)
search_entry.grid(row=0,column=0,columnspan=7)
Tip = tk.Label(root,text='小轩浏览器，无敌的浏览器。调出的网页可以左/右键单击')
Tip.grid(row=1,column=0,columnspan=7)
SearchButton_Baidu = tk.Button(root,text='百度搜索',width=21,border=4,command=search_b)
SearchButton_Baidu.grid(row=2,column=0)
SearchButton_360 = tk.Button(root,text='360搜索',width=21,border=4,command=search_360)
SearchButton_360.grid(row=2,column=1)
SearchButton_Sougou = tk.Button(root,text='搜狗搜索',width=21,border=4,command=search_s)
SearchButton_Sougou.grid(row=2,column=2)
SearchButton_Bing = tk.Button(root,text='必应搜索',width=21,border=4,command=search_by)
SearchButton_Bing.grid(row=2,column=3)
SearchButton_Youdao = tk.Button(root,text='有道翻译',width=21,border=4,command=search_y)
SearchButton_Youdao.grid(row=2,column=4)
SearchButton_Googlef = tk.Button(root,text='谷歌翻译',width=21,border=4,command=search_g)
SearchButton_Googlef.grid(row=2,column=5)
SearchButton_OK = tk.Button(root,text='查找输入的网址(输入错误则没有网页)',width=30,border=4,command=search_ok)
SearchButton_OK.grid(row=2,column=6)
SearchButton_INSXE = tk.Button(root,text='SkyLight大浏览器（李官阳/小轩主要制作）,点击后稍等',width=100,border=4,command=search_insxe)
SearchButton_INSXE.grid(row=3,column=0,columnspan=7)
root.mainloop()