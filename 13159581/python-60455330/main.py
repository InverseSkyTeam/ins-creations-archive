import pygame
import sys
import websocket
import _thread as thread
import json
import time

pygame.init()
user = input("Id (1 or 2):")
room = input("Room:")
fast_get = {"1": 2, "2": 1}

pygame.display.set_caption(f"Game {room} - Player {user}")
screen = pygame.display.set_mode((400, 600))
player1_y = 335
player2_y = 265
wined = False
started = False

def heartbeat():
    while ws:
        ws.send("heartbeat")
        time.sleep(10)
def on_open(ws: websocket.WebSocketApp):
    # ws.send(json.dumps({"user": f"Game-{room}-{user}"}))
    thread.start_new_thread(heartbeat, ())
def on_message(ws: websocket.WebSocketApp, message: str):
    global player1_y, player2_y, started
    message = json.loads(message)
    # print(message)
    if "a" in message and message["a"] == "inputName":
        ws.send(json.dumps({"name": f"Game-{room}-{user}"}))
    if "list" in message and message["list"]["event"] == "del":
        started = False
        return
    if "list" in message and message["list"]["event"] == "add":
        ws.send(json.dumps({"msg": "I'm ready"}))
        # started = True
        return
    if message["msg"]["name"] == f"Game-{room}-{fast_get[user]}" and message["msg"]["content"] == "I&#039;m ready" and not started:
        started = True
        ws.send(json.dumps({"msg": "I'm ready"}))
        return
    if message["msg"]["name"] == f"Game-{room}-{fast_get[user]}" and message["msg"]["content"] == "Player 2 clicked":
        player1_y += 10
        player2_y += 10
    if message["msg"]["name"] == f"Game-{room}-{fast_get[user]}" and message["msg"]["content"] == "Player 1 clicked":
        player1_y -= 10
        player2_y -= 10

ws = websocket.WebSocketApp("wss://ws.asilu.com:8090/", on_open=on_open, on_message=on_message)
thread.start_new_thread(ws.run_forever, ())

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if ws:
                ws.close()
                del ws
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not wined and started:
            ws.send(json.dumps({"msg": f"Player {user} clicked"}))
            if user == "1":
                player1_y -= 10
                player2_y -= 10
            if user == "2":
                player1_y += 10
                player2_y += 10

    screen.fill((255, 255, 255))

    player1 = pygame.draw.circle(screen, (255, 0, 0), (200, player1_y), 35)
    player2 = pygame.draw.circle(screen, (0, 0, 255), (200, player2_y), 35)
    arena = pygame.draw.circle(screen, (100, 100, 100), (200, 300), 200, 5)
    if player2_y == 65:
        screen.blit(pygame.font.SysFont(['kaiti', 'harmonyossanssc'], 50).render("玩家1获胜！", True, (0, 0, 0)), (100, 300))
        wined = True
    if player1_y == 535:
        screen.blit(pygame.font.SysFont(['kaiti', 'harmonyossanssc'], 50).render("玩家2获胜！", True, (0, 0, 0)), (100, 300))
        wined = True

    if not started and not wined:
        screen.blit(pygame.font.SysFont(['kaiti', 'harmonyossanssc'], 30).render("等待下一个人的到来...", True, (0, 0, 0)), (50, 300))

    pygame.display.flip()
    clock.tick(60)