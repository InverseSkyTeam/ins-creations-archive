try:
    import websocket
except:
    print('请在库管理安装websocket-client，记住一定要加上-client')
    exit()
import random
import json
import time

def on_message(ws, message):
    res = json.loads(message)
    if res['method'] == 'set' and res['name'] == 'cloud_test':
        value = res['value']
        print(f'收到: {value}')
        ws.count += 1
        if ws.count == 10:
            ws.close()

def on_error(ws, error):
    print(f'错误报告: {error}')

def on_close(ws, close_status_code, close_msg):
    print('连接断开')
    if close_status_code:
        print(f'Close status code: {close_status_code}')
    if close_msg:
        print(f'Close message: {close_msg}')

def on_open(ws):
    print('连接成功')
    ws.count = 0

    for i in range(10):
        r = random.randint(0, 2048)
        data = {
            'method': 'set',
            'name': 'cloud_test',
            'user': '10000000',
            'project_id': '22168480',
            'value': str(r),
        }
        ws.send(json.dumps(data))
        print(f'发送: {r}')

        handshake_data = {
            'method': 'handshake',
            'user': '10000000',
            'project_id': '22168480',
        }
        ws.send(json.dumps(handshake_data))

ws = websocket.WebSocketApp('wss://api.xueersi.com/codecloudvariable/ws:90',
                            on_message = on_message,
                            on_error = on_error,
                            on_close = on_close,
                            on_open = on_open)

t = time.time()
ws.run_forever()
print(f'\n\n总用时: 用时{time.time() - t}s')
print('感谢两年前的云翼计划。')
print('但今天，它不一样了，长连接联机时代将会到来。以前的webconnect保存资源close太慢，而长联机不需要反复connect和close.')
print('期待python制作的联机fps的3d游戏吧！')
print('提一句，短联机慢在close，长联机慢在message.所以快的还是不多，但是达到了0.14s/条')
print('黄羿杰研究认为这是scratch传输云变量的限制，所以没办法，之后找个新源应该会更好。')
print('*注: vscode的fitten code帮助我们搜集了一些关于websocket-client的信息，这非常好。')