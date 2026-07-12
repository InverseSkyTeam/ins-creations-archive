from CloudMemorizer.kernel.variable import *
import time

# player = "player1"
# var = CloudVar(20574944,17025146)
# var.open(f"{player}-online")
# while True:
#     now = var.read()
#     if time.time() - int(now) >= 2:
#         break
# print("quit")
x,y = 0,0
player = "player1"
var = CloudVar(20574944,17025146)
while True:
    var.open(f"{player}-x")
    rx = var.read()
    var.close()
    var.open(f"{player}-y")
    ry = var.read()
    var.close()
    if rx == x and ry == y:
        pass
    else:
        print((rx,ry))
        x = rx
        y = ry