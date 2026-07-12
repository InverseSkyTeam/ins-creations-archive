import random
stringdict = {
    '~': '0',
    '.': '1',
    '、': '2',
    '，': '3',
    '：': '4',
    '；': '5',
    '。': '6',
    '！': '7',
    '？': '8',
    '@': '9',
    '|': 'a',
    '&': 'b',
    '+': 'c',
    '-': 'd',
    '*': 'e',
    '/': 'f',
    '^': 'P',  # power，重复
    '#': 'S',  # sep，间隔
    '$': 'D',  # -翻译式- delete，删除
    '%': 'F',  # -翻译式- fill，互补，G-字符
    '=': 'U',  # -翻译式- unsep，撤销间隔
}
intdict = {
    '0': '~',
    '1': '.',
    '2': '、',
    '3': '，',
    '4': '：',
    '5': '；',
    '6': '。',
    '7': '！',
    '8': '？',
    '9': '@',
    'a': '|',
    'b': '&',
    'c': '+',
    'd': '-',
    'e': '*',
    'f': '/',
    'P': '^',
    'S': '#',
    'D': '$',
    'F': '%',
    'U': '=',
}

def to_symbol(string,d=intdict):
    asciistring = ''
    dkeys = list(d)
    dkeys.remove('D')    # 两个删除符号会出现删除到前一字节的问题
    for i in string:
        print(str(hex(ord(i)))[2:])
        asciistring += str(hex(ord(i)))[2:] + ' '
    asciistring = list(asciistring.replace(' ','S'))
    for i in range(len(asciistring)):
        tmp = d[asciistring[i]]
        if tmp == asciistring[i-1]:
            tmp = d['P']
        if random.randint(1,6) == 1:
            tmp += d[random.choice(dkeys)] + d['D']
        asciistring[i] = tmp
    asciistring = ''.join(asciistring)
    return asciistring

def to_chinese(string,d=stringdict):
    chistring = ''
    for i in range(len(string)):
        tmp = d[string[i]]
        if tmp == 'P':
            tmp = d[string[i-1]]
        if tmp == 'D':
            chistring = chistring[:-1]
            tmp = ''
        chistring += tmp
    chistring = chistring.split('S')[:-1]
    for i in range(len(chistring)):
        print(chistring[i])
        chistring[i] = chr(int('0x'+chistring[i],16))
        # 或者chistring[i] = chr(eval('0x'+chistring[i]))
    chistring = ''.join(chistring)
    return chistring

translatedict = {
    'symbol': to_symbol,
    'chinese': to_chinese,
}

def translate(string,to='symbol'):
    return translatedict[to](string)

tp = input('输入指令(不用中括号，仅仅是提示)：\n[symbol]语言转符号\n[chinese]符号转语言\nInput:')
ustring = input('输入文本:')
print('+'+'-'*20+'+')
print('翻译结果:')
print(translate(ustring,tp))
# import sys
# f=open("a.py","w+",encoding='utf-8')
# sys.stdout=f
# for i in range(10000):
#     if not i%100:
#         print('次数:',i)
#         x = translate('the next time，加上base64编码！')
#         print(x)
#         print('--------------------------')
#         print('llllllllllllllll',translate(x,to='chinese'))