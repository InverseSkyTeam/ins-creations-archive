'''
Update Data
build 0 新版ij的诞生
build 8 正则表达式识别代码
build 11 新增lex函数，遍历tokens且返回
build 16 新增+ - * / % // **这些运算
build 17 新增InsjhxError错误
build 20 新增括号、命名空间
build 25 新增符号打表、优先级打表、正负符号、多个函数
build 27 新增正负符号类，模拟符号，简化正负读入，测试编译结果成功
build 28 ij第三版第一次发布
'''

import re

lex_split = r'[\w\.]+|[\n\(\)\[\]\{\}\+\-\*\/\!\?\@\#\$\%\^\&\|\~\<\>\=\,\:\;\.\'\"]'
oplist = [
    '+','-','*','/','**','//','%','<<','>>','~','!','..',
    '==','!=','>=','<=','<','>',
    '=','+=','-=','*=','/=','**=','//=','%=','<<=','>>=',
    '&','|','^',
    '\n','end',' ',
    ':',',',';','.',
]
priority_dict = {
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
}
namespace = {}

class InsjhxError(Exception):
    ...

class UnaryPlus:pass    # +
class UnaryMinus:pass   # -
class UnaryBitivs:pass  # ~
unaryplus = UnaryPlus()
unaryminus = UnaryMinus()
unarybitivs = UnaryBitivs()

def leftfind(l,x):
    return l.index(x)
def rightfind(l,x):
    for i in range(len(l)-1,-1,-1):
        if l[i] == x:
            return i
    raise ValueError(str(x)+' is not in list')

def findop(l,*tokens,func=leftfind):
    if func == leftfind:
        cmpfunc = min
        mindex = len(l)    # m: min和max的量子叠加态
    else:
        cmpfunc = max
        mindex = 0
    for t in tokens:
        if t in l:
            mindex = cmpfunc(mindex,func(l,t))
    return mindex

def lex(code):
    tokens = re.findall(lex_split,code+'\nend')
    tokenl = []
    for i in range(len(tokens)):
        t = tokens[i]
        if t.isdigit():
            tokenl.append(int(t))
            continue
        if '.' in t:
            tt = t.split('.')
            if len(tt) == 2:
                if tt[0].isdigit() or tt[1].isdigit():
                    tokenl.append(float(t))
                    continue
        if tokens[i-1] + t in oplist:   # 当字符索引为0时，上一个字符就是end结尾，不会报错
            tokenl[-1] += t
            continue
        if (tokens[i-1] in oplist):
            if t == '+':
                tokenl.append(unaryplus)
                continue
            if t == '-':
                tokenl.append(unaryminus)
                continue
            if t == '~':
                tokenl.append(unarybitivs)
                continue
        tokenl.append(t)
    return tokenl

def calc_expr(l,thisindex):
    # this: l[thisindex]
    # left: l[thisindex-1]
    # right: l[thisindex+1]
    if l[thisindex] == '+':
        l[thisindex] = l[thisindex-1] + l[thisindex+1]
    elif l[thisindex] == '-':
        l[thisindex] = l[thisindex-1] - l[thisindex+1]
    elif l[thisindex] == '*':
        l[thisindex] = l[thisindex-1] * l[thisindex+1]
    elif l[thisindex] == '/':
        l[thisindex] = l[thisindex-1] / l[thisindex+1]
    elif l[thisindex] == '**':
        l[thisindex] = l[thisindex-1] ** l[thisindex+1]
    elif l[thisindex] == '//':
        l[thisindex] = l[thisindex-1] // l[thisindex+1]
    elif l[thisindex] == '%':
        l[thisindex] = l[thisindex-1] % l[thisindex+1]
    elif l[thisindex] == unaryplus:
        l[thisindex] = +l[thisindex+1]
        del l[thisindex+1]
        return
    elif l[thisindex] == unaryminus:
        l[thisindex] = -l[thisindex+1]
        del l[thisindex+1]
        return
    elif l[thisindex] == unarybitivs:
        l[thisindex] = ~l[thisindex+1]
        del l[thisindex+1]
        return
    del l[thisindex+1], l[thisindex-1]

def executable(tokenlist):
    while '(' in tokenlist:
        l_prn = tokenlist.index('(')
        prns = 1
        distance = l_prn
        while True:
            distance += 1
            if tokenlist[distance] == '(':
                prns += 1
            if tokenlist[distance] == ')':
                prns -= 1
                if prns == 0:
                    inside = tokenlist[l_prn+1:distance]
                    executable(inside)
                    tokenlist[l_prn] = inside[0]
                    del tokenlist[l_prn+1:distance+1]
                    break
    
    total = tokenlist.count(unaryplus) + tokenlist.count(unaryminus) + tokenlist.count(unarybitivs)
    for i in range(total):
        firstindex = findop(tokenlist,unaryplus,unaryminus,unarybitivs,func=rightfind)
        calc_expr(tokenlist,firstindex)
    
    total = tokenlist.count('**')
    for i in range(total):
        firstindex = findop(tokenlist,'**',func=rightfind)
        calc_expr(tokenlist,firstindex)
    
    total = tokenlist.count('*') + tokenlist.count('/') + tokenlist.count('%') + tokenlist.count('//')
    for i in range(total):
        firstindex = findop(tokenlist,'*','/','%','//')
        calc_expr(tokenlist,firstindex)
    
    total = tokenlist.count('+') + tokenlist.count('-')
    for i in range(total):
        firstindex = findop(tokenlist,'+','-')
        calc_expr(tokenlist,firstindex)
    
code = '''
((1--1+0*-+-1)*5)+2.+.6
114514*1919810+666
'''

tokenlist = lex(code)
executable(tokenlist)
print('begin main.ij')
for res in tokenlist:
    if res != '\n':
        print(res)
print('\x1b[1A\x1b[3C main.ij')
print()
print('编译完成。之后由于需要逐行读入就要改成解释器了。')