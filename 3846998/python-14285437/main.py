print("本编辑器只支持print和input，且需要写一行出一行结果，如果代码中不包括input或print，程序直接结束运行")
while 1:
    a=input()
    if "print" in a:
        b=a[7:-2]
        print(b)
        continue
    elif "input" in a:
        b=a[7:-2]
        input(b)
        continue
    else:
        break