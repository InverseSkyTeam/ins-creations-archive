import websocket
import json

player = "player1"
x = 0
y = 0
while True:
    ws = websocket.create_connection(f'wss://api.xueersi.com/codecloudvariable/ws:80',timeout=10)
    operate = input("操作:")
    if operate == "w":
        y += 1
    elif operate == "s":
        y -= 1
    elif operate == "a":
        x -= 1
    elif operate == "d":
        x += 1
    messagex = {
        "method": "set",
        "user": 17025146,
        "project_id": 21267487,
        "name": "☁ " + f"{player}-x",
        "value": x
    }
    messagey = {
        "method": "set",
        "user": 17025146,
        "project_id": 21267487,
        "name": "☁ " + f"{player}-y",
        "value": y
    }
    ws.send(json.dumps(messagex))
    ws.send(json.dumps(messagey))
    ws.close()