import requests
import bs4
import time
import pyttsx3
import tkinter
import sys
import json
#青云客机器人http://api.qingyunke.com/#ui_guide_menu

text = pyttsx3.init()
voices = text.getProperty('voices')
text.setProperty('voice', voices[0].id)
def saysth(s):
    #添加语音文本：
    text.say(s)
    #运行：
    text.runAndWait()
    #当然它还可以调整声音的音量，频率，变声，当然设置方法都差不多，都是先拿到它对应功能的值然后在进行加减。
    #比如说音量调节：
    #vol=text.getProperty('volume')
    #text.setProperty('vol',vol+0.5)
    #对于发音，频率，变声则为 vioce，rate，vioces，是不是很好理解了？当然，如果你想让它循环播放，只需加一个事件驱动循环即可：\
    #pp.startLoop()一直说
temp=0
head = {
    "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11"
}
def getans(key):
    global head
    res = requests.get(f"http://api.qingyunke.com/api.php?key=free&appid=0&msg="+key, headers=head)
    return str(res.json()["content"])
i=0
def sold():
    global enter,listb,i,name,text,voices
    contents=enter.get()
    listb.insert(i,name+": "+contents)
    i+=1
    robsays=getans(contents)
    listb.insert(i,"青云の|竹|机器人: "+robsays)
    i+=1
    saysth(robsays)
    temp=0

def getCookies():
    cookies = ""
    if len(sys.argv) > 1:
        try:
            cookies = json.loads(sys.argv[1])["cookies"]
        except:
            pass
    return cookies

id=""
for i in range(getCookies().find("stu_id=")+7,getCookies().find("stu_id=")+17):
    if getCookies()[i].isdigit():
        id+=getCookies()[i]
    else:
        break

response=requests.get(f"https://code.xueersi.com/api/space/profile?user_id={id}",headers=head)
name=response.json()["data"]["realname"]


tk=tkinter.Tk()
tk.geometry("800x400")
tk.title("|竹|の聊天机器人")
tk.iconbitmap("robot.ico")
enter = tkinter.Entry(tk,bd=0,width=80)#输入框
enter.pack(expand=True,pady=10)
button =tkinter.Button(tk,text="输入完了戳这里提交哦(*^▽^*)",width=80,command=sold)
button.pack(expand=True,pady=10)
listb = tkinter.Listbox(tk,width=80,height=130)
listb.pack(expand=True,pady=10)


print("你好(*´▽｀)ノノ我是竹编程工作室的机器人")
print("请留意弹出的窗口，请在上方输入框留言(*^▽^*)")

text.say("你好"+name+"!我是竹编程工作室的聊天机器人")
text.runAndWait()
text.say("请留意弹出的窗口，请在上方输入框留言")
text.runAndWait()

t2=0
while True:
    if(temp==0):
        listb.insert(i,"青云の|竹|机器人:你好(*´▽｀)ノノ我是竹编程工作室的机器人")
        i+=1
        temp=1
    if(t2==0):
        tk.mainloop()
        t2=1