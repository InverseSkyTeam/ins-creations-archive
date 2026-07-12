string = input('粘贴吴宇航的恶毒unicode/doge')
colorfuldict = ['ij','Ij','iJ','IJ','insjhx','INSJHX','Insjhx']
if string in colorfuldict:  # 彩虹字典
    print('通过，饶吴宇航一次')
    raise SystemExit
for i in string:
    if 'l' == i or i > 'z' or i < 'A':
        print('吴宇航用unicode f**k insjhx语言！(bushi+doge)')
        raise SystemExit
print('吴宇航很有可能用unicode f**k insjhx语言！(bushi+doge)')