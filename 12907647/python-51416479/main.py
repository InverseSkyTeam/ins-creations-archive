import sys

'''
code:
3*(1+1)
tokenize:
[3,*,(,1,+,1,)]
ast:
("*",c(3),("+",c(1),c(1)))
flatstack:
[("*",2),("Const",3),("+",2),("Const",1),("Const",1),]
res:
6
'''
token_stack = [('*',2),('Const',3),('+',2),('Const',1),('Const',1),]
value_stack = []
scope = [{}]

built_in = {
    '+': (lambda a, b: a + b),
    '-': (lambda a, b: a - b),
    '*': (lambda a, b: a * b),
    '/': (lambda a, b: a / b),
    '%': (lambda a, b: a % b),
    '//': (lambda a, b: a // b),
    '<<': (lambda a, b: a << b),
    '>>': (lambda a, b: a >> b),
    '^': (lambda a, b: a ^ b),
    '|': (lambda a, b: a | b),
    '&': (lambda a, b: a & b),
    '+u': (lambda e: +e),
    '-u': (lambda e: -e),
    '~u': (lambda e: ~e),
    'not': (lambda e: not e),
}

while token_stack:
    token = token_stack.pop()
    
    if token[0] == 'Const':
        value_stack.append(token[1])
        continue
    
    # op: 操作符
    # pn: param_num, 操作参数个数
    op, pn = token
    args = []
    for i in range(pn):
        arg = value_stack.pop()
        args.append(arg)
    res = built_in[op](*args)
    value_stack.append(res)

print(value_stack[0])
print('程序猿的痛苦和电脑的快乐成正比')
print('编写速度和执行速度成反比')
print('我宁可找到一个优化的解')
print('解越简洁，解越简单，解越困难')
print('-'*40)
print('''欢迎来到【简单“洁”构】工程
我将尽我所能提供一个简洁的解释器！
（原理：前缀表达式、常量-函数构造原理。没了！简单！）
此版本已经实现了expr的运算。
（另：特别感谢吴宇航大佬的指点和帮助，他每天晚上和我在vscode里开share.不过我这次要走一条新道路，和pl有一些不同。）
（另：付开霁大佬和鱼翔浅底大佬现在打算怎么写语言呢？）''')