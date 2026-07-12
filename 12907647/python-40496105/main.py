'''
-+公开测试数据+-
10^(3*10^6)个2组合成的大数字
py  1.40s
ij  1.51s
i32 1.68s
df1.8  7.21s

10^(5*10^6)个2组合成的大数字
py  4.21s
ij  4.53s
i32 12.89s
df1.8  63.40s

10^(7*10^6)个2组合成的大数字
py  8.54s
ij  9.002s
i32 48.71s
df1.8  *s(未能在100s内正常运行出结果)

完胜！！！！！！！！！！！！！！！！！！！！！！！！！！
'''


import sys

token_dict = {
    ' ': ('space',' '),
    'integer': ('int',None),
    'string': ('str',None),
    'floating': ('float',None),
    '+': ('operator','+'),
    '-': ('operator','-'),
    '*': ('operator','*'),
    '/': ('operator','/'),
    '//': ('operator','//'),
    '%': ('operator','%'),
    '|': ('operator','|'),
    '&': ('operator','&'),
    '^': ('operator','^'),
    '<': ('operator','<'),
    '>': ('operator','>'),
    '.': ('symbol','.'),
    '(': ('symbol','('),
    ')': ('symbol',')'),
    '[': ('symbol','['),
    ']': ('symbol',']'),
    '\n': ('EOF','\n'),
    'ENDEOF': ('EOF','ENDEOF'),
}

keyword_list = [
    'read',   # 导库
    'in',     # stdin
    'out',    # stdout
    'if',
    'elif',
    'else',
    'while',
    'for',
    'conti',
    'break',
    'let',
    'fun',
    'class',
    'struct',
    'db',
    'cfg',
    'true',
    'false',
    'null',
    'because',
]

integer_replacelist = [   # 不要加进小数点
    '!','@','#','$','%','^','&','*','(',')',
    '[',']','{','}','+','-','/','=','|',',',
    '\'','\"',';',':','<','>','?','\\',
    '~','·','`',
]

operatorlist = {
    '(': 3,
    ')': 3,
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
}

namespace = {}
database = []

class Token(object):
    def __init__(self,name,tp,value):
        self.name = name
        self.tp = tp
        self.value = value
    def __str__(self):
        return self.name+'|'+self.tp+'|'+str(self.value)
    __repr__ = __str__

class Interpreter(object):
    def __init__(self,code):
        self.code = code
        self.codelength = len(self.code)
        self.codelastindex = self.codelength - 1
        self.line = 0
        self.position = -1
        self.lineposition = -1
        self.current_word = ''
        self.current_token = None
        self.token_stack = []
    
    def error(self,msg):
        raise Exception(msg)
    
    def is_end(self):
        return self.position >= self.codelength
    
    def advance(self):
        self.position += 1
        self.lineposition += 1
        if self.is_end():
            return 'end'
        self.current_word += self.code[self.position]
        return 'normal'
    
    def get_near(self,index=1):
        try:
            return self.code[self.position+index]
        except:
            return 'out index'
    
    def isnum_or_point(self,string):
        return string.isdigit() or string == '.'
    
    def isnum(self,string):
        left = string
        right = self.get_near()
        return (left.isdigit() and right.isdigit()) \
            or (left.isdigit() and right == '.') \
            or (left == '.' and right.isdigit()) \
    
    def get_next_token(self):
        
        if self.advance() == 'end':
            return Token('ENDEOF','EOF','ENDEOF')
        
        if self.isnum(self.current_word):   # 很多位数字，字符串分割最快
            linestring = self.code.split('\n')[self.line][self.lineposition:]
            for i in integer_replacelist:
                linestring = linestring.replace(i,' ')
            linestring = linestring.split()[0]
            if '.' in linestring:   # 如果有小数点
                try:    # 报错，可能是因为出现两个小数点
                    self.current_token = Token('floating','float',float(linestring))
                except:
                    self.error('浮点数'+linestring+'不正确')
            else:
                self.current_token = Token('integer','int',int(linestring))
            self.position += len(linestring) - 1
            self.lineposition += len(linestring) - 1
            self.current_word = ''
            return self.current_token
        
        if self.current_word.isdigit():  # 一位数字
            self.current_token = Token('integer','int',int(self.current_word))
            self.current_word = ''
            return self.current_token
        
        if self.current_word in token_dict:    # 特定符号
            self.current_token = Token(self.current_word,
                                       token_dict[self.current_word][0],
                                       token_dict[self.current_word][1])
            self.current_word = ''
            return self.current_token
        
        self.current_word = ''
        return self.get_next_token()
    
    def calc_unary(self,name,expression):   # 一元运算
        if name == '+':
            return (+expression, 'integer', 'int')
        if name == '-':
            return (-expression, 'integer', 'int')
    
    def calc_binary(self,name,left,right):   # 二元运算
        if name == '+':
            result = left + right
        if name == '-':
            result = left - right
        if name == '*':
            result = left * right
        if name == '/':
            result = left / right
        if name == '//':
            result = left // right
        if name == '%':
            result = left % right
        if name == '**':
            result = left ** right
        tp = str(type(result))[8:-2]
        if tp == 'int':
            name = 'integer'
        elif tp == 'float':
            name = 'floating'
            result = round(result,15)
        return (result,name,tp)
    
    def calc_ternary(self,name,expr1,expr2,expr3):   # 三元运算
        pass
    
    def revisit(self,stack):     # 交互式递归突破python限制
        return self.visit(stack)
    
    def visit(self,stack):
        token = -1     # 括号
        parenthese_inside = 0
        parenthese_beginpos = 0
        parenthese_stack = []
        while token < len(stack)-1:
            token += 1
            tn = stack[token].name
            if parenthese_inside:
                parenthese_stack.append(stack[token])
            if tn in operatorlist:
                if operatorlist[tn] == 3:
                    if tn == '(':
                        parenthese_inside += 1
                        if parenthese_inside == 1:
                            parenthese_beginpos = token
                    elif tn == ')':
                        parenthese_inside -= 1
                        if parenthese_inside == 0:    # 最外层括号结束
                            parenthese_stack.remove(parenthese_stack[-1])
                            result = self.revisit(parenthese_stack)
                            stack[token] = result[0]
                            stack = stack[:parenthese_beginpos]+stack[token:]
                            parenthese_stack = []
                            # parenthese_inside = 0
                    
        token = -1   # 乘除
        while token < len(stack)-1:
            token += 1
            tn = stack[token].name
            if tn in operatorlist:
                if operatorlist[tn] == 2:
                    left = stack[token-1]
                    right = stack[token+1]
                    result = self.calc_binary(tn,left.value,right.value)
                    stack[token].value, stack[token].name, stack[token].tp = result
                    stack.remove(left)
                    stack.remove(right)
                    token -= 2
        
        token = len(stack)   # 加减、正负
        while token > -1:
            token -= 1
            tn = stack[token].name
            if tn in operatorlist:
                if operatorlist[tn] == 1:
                    left = stack[token-1]
                    right = stack[token+1]
                    if left.name not in ('integer','floating'):
                        result = self.calc_unary(tn,right.value)
                        stack[token].value, stack[token].name, stack[token].tp = result
                        stack.remove(right)
                        token += 1
                    else:
                        result = self.calc_binary(tn,left.value,right.value)
                        stack[token].value, stack[token].name, stack[token].tp = result
                        stack.remove(left)
                        stack.remove(right)
                        token += 1
        return stack
    
    def add_token(self):
        self.current_token = self.get_next_token()
        self.token_stack.append(self.current_token)
        if self.current_token.name == 'ENDEOF':
            return False
        if self.current_token.name == '\n':
            self.line += 1
            self.lineposition = -1
        return True
    
    def expr(self):
        while self.add_token():
            if self.current_token.name == '\n':
                self.token_stack = self.visit(self.token_stack)
                print(self.token_stack)
                # self.token_stack.clear()   # 一行运行结束清除session(bushi+doge
                # pass
        self.token_stack = self.visit(self.token_stack)
        # self.token_stack.clear()
            
        return self.token_stack
    
    def run(self):
        return self.expr()

code = input('输入算式:')
# import time
# t = time.time()
# code = '2'*300000
# interpreter = Interpreter(code=code)
# interpreter.run()
# print(time.time()-t)

interpreter = Interpreter(code=code)
result = str(interpreter.run()[0]).split('|')
# print(interpreter.run())
print('insjhx类型:'+result[0],
      'python类型:'+result[1],
      '计算结果:'+result[2],
    sep='\n')