print('需要用到的三方库:\nwebsocket-client(不要忘记这个-client!!!这是客户端!!!!!)\nwebbrowser\n请自行安装',end='\n\n')
import websocket,json,time

site = 'https://cdn.asilu.com/ws/'

input('注意：该程序为客户端，网站为服务端，发送接收结果可在网页和本程序之间来回切换观看\n回车(Enter)打开聊天室网站')
import webbrowser
webbrowser.open(site)

# cloud #

ws = websocket.create_connection('wss://ws.asilu.com:8090/',timeout=5)

data = {
        'name': '小轩的机器人',
}
ws.send(json.dumps(data))

# +--------测试数据---------+
# 发送
# data = {'name': '小轩的机器人',}
# data = {"msg": "测试中",}
# 接收
# {'tips': '你已经有昵称了'}
# {"msg":{"name":"小轩的机器人","time":1674122022,"content":"测试中"}}
# +-------------------------+

t = 0
while True:
    t += 1
    r = json.loads(ws.recv())
    print('接收',r)
    data = {
        "msg": "我就是你运行的那个python程序哦，测试中\n如果你看到了这条消息，那就对了，这些消息都是用程序发送的，每秒一次发送接收\n发送次数:"+str(t),
    }
    ws.send(json.dumps(data))
    time.sleep(1)
    print()

ws.close()