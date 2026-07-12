import pygame
import sys
import websocket
import _thread as thread

pygame.init()
user = input("Id (1 or 2):")
room = input("Room:")

pygame.display.set_caption(f"Game {room} - Player {user}")
screen = pygame.display.set_mode((400, 600))
player1_y = 335
player2_y = 265
wined = False
started = False
def on_message(ws: websocket.WebSocketApp, message: str):
    global player1_y, player2_y, started
    # print(message)
    message = message.strip()
    if message == "Username:":
        ws.send(f"Player {user}")
    if message == "Room:":
        ws.send(f"Game {room}")
    if message == "Player 2: Player 2 clicked":
        player1_y += 10
        player2_y += 10
    if message == "Player 1: Player 1 clicked":
        player1_y -= 10
        player2_y -= 10
    if "加入了频道" in message:
        ws.send("I'm ready")
        started = True
    if "I'm ready" in message:
        started = True

def on_error(ws: websocket.WebSocketApp, error: str):
    print(error)

ws = websocket.WebSocketApp("wss://xiaochen-chat.up.railway.app/", on_message=on_message, on_error=on_error)
thread.start_new_thread(ws.run_forever, ())

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if ws:
                ws.close()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not wined and started:
            ws.send(f"Player {user} clicked\n\n")
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
    if player2_y <= 65:
        player2_y = 65
        player1_y = 135
        screen.blit(pygame.font.SysFont(['kaiti', 'harmonyossanssc'], 50).render("玩家1获胜！", True, (0, 0, 0)), (100, 300))
        wined = True
        ws.on_message = None
    if player1_y >= 535:
        player1_y = 535
        player2_y = 465
        screen.blit(pygame.font.SysFont(['kaiti', 'harmonyossanssc'], 50).render("玩家2获胜！", True, (0, 0, 0)), (100, 300))
        wined = True
        ws.on_message = None

    if not started and not wined:
        screen.blit(pygame.font.SysFont(['kaiti', 'harmonyossanssc'], 30).render("等待下一个人的到来...", True, (0, 0, 0)), (50, 300))

    pygame.display.flip()
    clock.tick(60)
