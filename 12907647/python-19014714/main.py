import textbreaker as tbr
a = input('1.加密 2.解密')
if a == '1':
    textl = input('文件加密器，加密文字：')
    times = input('加密密码(推荐1-5位数，否则容易加密失败)：')
    # text = tbr.add_ASCLL(textl,times,'+')
    text = tbr.add_INS_ec04(textl,times)
    print(text)
    print('\033[1;31m别忘了，右键复制密文哦！')

else:
    print('\033[1;31m右键粘贴密文哦！\033[0m')
    textl = input('文件加密器，解密文字：')
    times = input('解密密码：')
    # text = tbr.add_ASCLL(textl,times,'-')
    text = tbr.readd_INS_ec04(textl,times)
    print(text)