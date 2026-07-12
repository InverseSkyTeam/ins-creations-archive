import time
text = input('输入序号:\n[1]简单线性同余法\n[2]低贱平方取中法')

if text == '1':
    s = int(input('输入随机种子(0-100000之间):'))
    
    rand = 1
    acknum = 2**24
    
    def setseed(seed):
        global rand
        rand = seed
    
    def newrand():
        global rand
        setseed((rand*1140671485+128201163)%acknum)
        return rand/acknum
    
    setseed(s)
    
    for i in range(1000):
        r = newrand()
        print(r)
        time.sleep(0.01)

else:
    s = int(input('输入种子(位数必须是偶数且至少4位):'))
    if s%10 == 0:
        s = int(str(s)[:-1]+'7')   # 7是奇质个位数，比较坚挺不重复呵呵
    if len(str(s))%2 != 0 or len(str(s))<4:
        raise SystemExit('种子位数必须是偶数且至少4位!\nhowever你乱写了个'+str(len(str(s)))+'位数!')
    
    def newrand(seed):
        power = seed**2
        digits = len(str(seed))*2
        power = str(power).zfill(digits)
        power = power[int(digits/4):int(-digits/4)]
        if power[0] == '0':
            up = seed%10
            if not up:
                up = 1
            power = str(up)+power[1:]
        power = int(power)
        if power%10 == 0:
            power = int(str(power)[:-1]+'7')
        return power
    
    for i in range(1000):
        s = newrand(s)
        print(s)
        time.sleep(0.01)