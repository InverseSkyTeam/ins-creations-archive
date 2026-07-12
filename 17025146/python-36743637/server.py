from CloudMemorizer.kernel.variable import *
import time

var = CloudVar(20574944,17025146)
var.open("online")
k = 0
while True:
    var.write(time.time())
    k += 1
    print(k)
    if k == 30:
        break