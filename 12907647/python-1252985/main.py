import time
for i in range(100):
    time.sleep(0.00000000000000000000000000000005)
    print('已加载%',i)
    time.sleep(0.00000000000000000000000000001)
    print('\033[2J')
    print('\033[100A')
for i in range(100):
    time.sleep(10)
    print('已加载%',i)
    time.sleep(10)
    print('\033[2J')
    print('\033[100A')