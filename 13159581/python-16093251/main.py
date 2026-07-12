try:
    f = open("a.txt")
    print(f.read())
    f.close()
except OSError as a:
    print("T_T这里出错了，出错原因是：" + str(a))