a = input('选择递归模式：1=一次函数递归 2=二次函数递归 其他=结束（虽然效果一样）')
if a == '1':
    def OK():
        print('\033[1;32m666')
        st()
    def st():
        print('\033[1;33mnbb')
        OK()
    try:
        OK()
    except:
        print('\033[1;31m用py也能实现递归。你们看，代码里莫有循环代码')
if a == '2':
    def OK():
        print('\033[1;32m666')
        print('\033[1;33mnbb')
        OK()
    try:
        OK()
    except:
        print('\033[1;31m用py也能实现递归。你们看，代码里莫有循环代码')