from threading import Thread
import time

print('看源码+素材、、、')

text = False

def in_():
    global text
    text = input('请输入')

t = Thread(target=in_)
t.setDaemon(1)
t.start()

now = begin = time.time()

while now - begin < 5:
    now = time.time()
    if text:
        print(f'接收到: {text}\n耗时: {now-begin}')
        break
else:
    print('\n未接收到')