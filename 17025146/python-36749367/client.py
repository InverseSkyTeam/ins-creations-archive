import time
from CloudMemorizer.kernel.variable import *

var = CloudVar(21272427,17025146)
var.open("17025146")
while True:
    onlinelist = []
    alluser = var.readAll()
    for i in alluser:
        if time.time() - float(alluser[i]) <= 2.5:
            onlinelist.append(i)
    if onlinelist:
        print(f"{onlinelist}这些用户在线")
    else:
        print(f"无人在线")