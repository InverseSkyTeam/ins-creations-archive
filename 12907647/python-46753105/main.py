import re,time

def regex_to_code(regex,stream,tp):
    newstream = []
    for expr in stream:
        if expr[1] == 'expr':
            _split = re.split(regex,expr[0])
            for _expr in range(len(_split)):
                if _expr % 2:
                    newstream.append([_split[_expr],tp])
                else:
                    newstream.append([_split[_expr],'expr'])
        else:
            newstream.append(expr)
    return newstream

# 用remove的算法显然不如直接推导式
clear_stream = lambda stream: [expr for expr in stream if (expr[0] != '')]

code = '''
out(1+1+1*2+(5//1))
a = int("666")+3
out a
'''*10000

print('正在编译代码为代码流...')
print('编译目标: 30000行代码 440000个字符')

# 小轩的正则大军
r1 = '\\'.join(['(',')','+','-','*','/','%','>','<'])
RE_LINE     = '(\n)'                              # 分行
RE_STRING   = '(".*"|' + "'.*')"                  # 分字符串
RE_INTEGER  = '(\d+\.?\d*|\d*\.?\d+)'             # 分数字
RE_PAREN    = '(//|>=|<=|==|['+r1+'])'       # 分括号

t = time.time()

# cstream是code_stream，代码流
cstream = [[code,'expr']]
cstream = regex_to_code(RE_LINE,cstream,'space')
cstream = regex_to_code(RE_STRING,cstream,'str')
cstream = regex_to_code(RE_INTEGER,cstream,'int')
cstream = regex_to_code(RE_PAREN,cstream,'symbol')
retime = time.time() - t

cstream = clear_stream(cstream)

cstime = time.time() - t

print(f'\n正则解析用时: {retime*1000}ms\n清理io流用时: {(cstime-retime)*1000}ms')
print('\033[32m编译成功')
# print('\n',cstream)