from tkinter import *
import requests,os
from time import sleep
root = Tk()
root.title("涨粉指南")
root.geometry("500x500")
sbar_y = Scrollbar(root)
sbar_y.pack(side='right', fill='y')
sbar_x = Scrollbar(root, orient=HORIZONTAL)
sbar_x.pack(side='bottom', fill='x')
text = Text(root,font=('微软雅黑',15),yscrollcommand=sbar_y.set, xscrollcommand=sbar_x.set)
txt = '''首先说一下涨粉的事项
1.不要一直发水作这样没人看,发一些高质量作品涨粉快一点
2.如果你想快速涨粉的话,就一定要互关\n
接下来说一下互关的好处和坏处
好处：涨粉较快
坏处：真粉丝比较少,大部分都是僵尸粉,作品观看数不会提升很多,如果全是凭高质量作品涨粉的话会稍微好一点

下面介绍一下刷关器
刷关器是通过爬虫调用社区接口实现的模拟手动关注
其实就是通过http协议里的post请求实现向服务器发送表单
刷关器代码我已经放在代码里了关闭此窗口就会自动运行
但是由于服务器已经限制了不能关注过快所以可能会失败
⚠️注意:不要使用多线程攻击服务器,会被封号的,如果被封号了和我没有任何关系!!!
刷关器我这里设的过几秒才刷一个不然容易封号,有1000多个人建议多分几次,或者挂机
使用刷关器后的效果:2个月1000粉丝,前提:要筛选一下关注的人我在素材里放了一个筛选过的文件
'''
text.insert("insert",txt)
text.pack(fill = BOTH)
sbar_y.config(command=text.yview)
sbar_x.config(command=text.xview)
root.mainloop()
def follow_person(cookie,id):
    
    head={
        'cookie':cookie,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.175 Safari/537.36'
    }
    payload={
        'followed_user_id': id,
        'state': 1#注意这里填上0就是取关了
    }
    response=requests.post("https://code.xueersi.com/api/space/follow",headers=head,data=payload)
    if response.status_code == 401:
        print("cookie有误,是否查看教程?(请输入是或否)")
        if input() == "是":
            os.startfile("帮助.docx")
            exit()
    status = "关注成功" if response.status_code == 200 else "关注失败"
    print(status)
f = open("关注列表.txt",'r')
follow_list = f.read().split('\n')[:-1]
cookie = input("请输入你的cookie,是否查看教程?(不会输入是):\n")
if cookie == "是":
    os.startfile("帮助.docx")
    exit()
for i in follow_list:
    follow_person(cookie,i)
    sleep(1)