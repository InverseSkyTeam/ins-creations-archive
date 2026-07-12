from CloudMemorizer.kernel.variable import *
import time

player = "player1"
# var = CloudVar(20574944,17025146)
# var.open(f"{player}-online")
# k = 0
# while True:
#     var.write(time.time())
#     k += 1
#     print(k)
#     if k == 100:
#         break
x = 0
y = 0
var = CloudVar(20574944,17025146)
while True:
    operate = input("操作:")
    if operate == "w":
        y += 1
    elif operate == "s":
        y -= 1
    elif operate == "a":
        x -= 1
    elif operate == "d":
        x += 1
    var.open(f"{player}-x")
    var.write(x)
    var.close()
    var.open(f"{player}-y")
    var.write(y)
    var.close()