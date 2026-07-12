import websocket
import json

player = "player1"
x = 0
y = 0
rx = None
ry = None
message = {"method": "handshake",
    "user": 17025146,
    "project_id": 21267487
    }
while True:
    ws = websocket.create_connection(f'wss://api.xueersi.com/codecloudvariable/ws:80',timeout=10)
    while True:
        ws.send(json.dumps(message))
        r = ws.recv()
        value = str(json.loads(r)['value'])
        name = str(json.loads(r)['name']).replace("☁ ","")
        if name == f"{player}-x":
            rx = value
        elif name == f"{player}-y":
            ry = value
        if rx and ry:
            break
    ws.close()
    if rx == x and ry == y:
        pass
    else:
        print((rx,ry))
        x = rx
        y = ry
        rx,ry = None,None