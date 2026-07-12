from CloudMemorizer.kernel.variable import *
import time

userid = input("输入你的ID:")
var = CloudVar(21272427,17025146)
while True:
    var.open(f"{userid}")
    var.write(time.time())
    var.close()