import webbrowser as wb,time,sys
a=input("请问您要玩哪个版本 1.植物大战僵尸js版原版  2.植物大战僵尸js版kac改版（输入1或2）")
a=int(a)
if a==1:
    print('这个版本代码需自行下载')
    time.sleep(1)
    wb.open('https://s1.asytech.cn/s/RifTYzqWm9f3gJW')
    sys.exit()
if a==2:
    print('''这个版本代码需自行下载,验证码：HPNY
    特别鸣谢这个版本的作者：我是帅（b站：我不知道啊啊啊真是六）''')
    time.sleep(1)
    wb.open('https://wway.lanzoub.com/iZ4sw13el2ob')
    sys.exit()
