import webbrowser as w
if __name__ == '__main__':
    print("如果你想加入我们，在留言区回复，打出等级如：L1")
    print("工作室介绍见https://code.xueersi.com/home/project/detail?lang=code&pid=8525531&version=offline&form=python&langType=python,右键复制即可复制,Ctrl无效")
    print("如果您加入，现在可以开始聊天了")
    print("聊天默认为加入")
    pp = input('若直接进入工作室介绍作品，回车即可,查看我最好作品打1，不动就输别的，关注、查看我点我头像')
    if pp == '':
        w.open('https://code.xueersi.com/home/project/detail?lang=code&pid=8525531&version=offline&form=python&langType=python')
    if pp == '1':
        w.open('https://code.xueersi.com/home/project/detail?lang=code&pid=8946083&version=offline&form=python&langType=python')
