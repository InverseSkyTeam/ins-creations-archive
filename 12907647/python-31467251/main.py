from cefpython3 import cefpython as cef
import tkinter as tk
root = tk.Tk()
root.title('INS-SkyLight浏览器')
root.geometry('1200x800+120+60')
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
search_entry = tk.Entry(root)
search_entry.pack()
SearchButton_Baidu = tk.Button(root,text='百度搜索',command=search_b)
SearchButton_Baidu.pack()
SearchButton_360 = tk.Button(root,text='360搜索',command=search_360)
SearchButton_360.pack()
SearchButton_Sougou = tk.Button(root,text='搜狗搜索',command=search_s)
SearchButton_Sougou.pack()
SearchButton_Bing = tk.Button(root,text='必应搜索',command=search_by)
SearchButton_Bing.pack()
SearchButton_Youdao = tk.Button(root,text='有道翻译',command=search_y)
SearchButton_Youdao.pack()
SearchButton_Googlef = tk.Button(root,text='谷歌翻译',command=search_g)
SearchButton_Googlef.pack()
root.mainloop()