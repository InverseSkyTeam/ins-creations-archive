import time
while True:
    a = time.strftime("%Y年%m月%H点%M分%S秒周%w",time.localtime())
    print(a)
    time.sleep(1)