from CloudMemorizer.kernel.variable import *
import time

var = CloudVar(20574944,17025146)
var.open("online")
while True:
    now = var.read()
    if time.time() - int(now) >= 2:
        break
    print("online")
print("quit")