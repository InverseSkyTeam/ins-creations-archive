from os import*
cx={}
while 1:
    print("\033[1;0m",end='')
    cho=int(input("0、停止\n1、编写程序\n2、编写程序并运行\n3、修改程序\n4、运行旧程序\n请输入模式："))
    if cho==0:
        break
    if cho==1:
        a=''
        while True:
            b=input()
            if b=="programingend" or b=="end":
                b=input("请为您的程序命名：")
                cx[b]=a
                print("您的程序已经保存完毕！")
                break
            a=a+'\n'+b
    if cho==2:
        a=""
        while 1:
            b=input()
            if b=="programingend" or b=="end":
                b=input("请为您的程序命名：")
                cx[b]=a
                print("您的程序已经保存完毕！")
                break
            a=a+'\n'+b
        try:
            exec(a)
        except:
            print("您的程序可能有问题或出现了本程序不支持的语法")
    if cho==3:
        c=input("请输入要修改的程序名：")
        try:
            cx[c]
        except:
            print("没有此程序！")
        else:
            print("您的旧程序如下：",end='')
            a=cx[c]
            print(a)
            while 1:
                b=input()
                if b=="programingend" or b=="end":
                    print("修改完毕！")
                    cx[c]=a
                    break
                a=a+'\n'+b
    if cho==4:
        c=input("请输入要运行的程序名：")
        try:
            cx[c]
        except:
            print("没有此程序！")
        else:
            try:
                exec(a)
            except:
                print("您的程序可能有问题或出现了本程序不支持的语法")