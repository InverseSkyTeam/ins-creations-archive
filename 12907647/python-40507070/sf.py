import sys
token_dict = {' ': ('space',' '),'integer': ('int',None),'floating': ('float',None),'bool': ('bool',None),'string': ('str',None),'null': ('NoneType',None),'+': ('operator','+'),'-': ('operator','-'),'*': ('operator','*'),'/': ('operator','/'),'**': ('operator','**'),'//': ('operator','//'),'%': ('operator','%'),'|': ('operator','|'),'&': ('operator','&'),'^': ('operator','^'),'<': ('operator','<'),'>': ('operator','>'),'<<': ('operator','<<'),'>>': ('operator','>>'),'==': ('operator','=='),'!=': ('operator','=='),'>=': ('operator','>='),'<=': ('operator','<='),'~': ('symbol','~'),'=': ('symbol','='),'.': ('symbol','.'),'\"': ('symbol','\"'),'\'': ('symbol','\''),'(': ('symbol','('),')': ('symbol',')'),'[': ('symbol','['),']': ('symbol',']'),'{': ('symbol','{'),'}': ('symbol','}'),'\n': ('EOF','\n'),'ENDEOF': ('EOF','ENDEOF'),}
varcharlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', 'z', '_','0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
tpdict = {'int': 'integer','str': 'string','float': 'floating','bool': 'bool','NoneType': 'null',}
keyword_list = ['read','in','out','if','elif','else','while','for','conti','break','let','fun','class','struct','db','cfg','true','false','null','because',]
integer_replacelist = ['!','@','#','$','%','^','&','*','(',')','[',']','{','}','+','-','/','=','|',',','\'','\"',';',':','<','>','?','\\','~','·','`',]
operatordict = {'(': (9,),')': (9,),'~': (8,),'**': (7,),'%': (6,),'//': (6,),'*': (6,),'/': (6,),'+': (5,8,),'-': (5,8,),'<<': (4,),'>>': (4,),'>': (3,),'<': (3,),'>=': (3,),'<=': (3,),'==': (2,),'!=': (2,),'=': (1,),}
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
        self.codelastindex = self.codelength - 1;self.line = 0;self.position = -1;self.lineposition = -1;self.inblocks = 0;self.current_char = '';self.current_word = '';self.current_token = None;self.token_stack = []
    def error(self,msg):
        msg = '[Error] File "main.insjhx":\nerror|'+msg
        raise SystemExit(msg)
    def is_end(self):return self.position >= self.codelength
    def advance(self):
        self.position += 1
        self.lineposition += 1
        if self.is_end():return 'end'
        self.current_char = self.code[self.position]
        self.current_word += self.current_char
        return 'normal'
    def get_near(self,index=1):
        try:return self.code[self.position+index]
        except:return 'out index'
    def get_nears(self,start=1,end=2):
        s = ''
        for i in range(start,end+1):s += self.get_near(index=i)
        return s
    def isnum_or_point(self,string):
        return string.isdigit() or string == '.'
    def isnum(self,string):
        left = string;right = self.get_near()
        return (left.isdigit() and right.isdigit()) or (left.isdigit() and right == '.') or (left == '.' and right.isdigit())
    def is_defined(self,string):
        return (string in token_dict) or (string in keyword_list) or (string in namespace)
    def get_next_token(self):
        if self.advance() == 'end':
            return Token('ENDEOF','EOF','ENDEOF')
        if (self.current_char not in varcharlist) and len(self.current_word) > 1:
            self.current_token = Token(self.current_word[:-1],'var',None)
            self.current_word = '';self.position -= 1;self.lineposition -= 1
            return self.current_token
        if self.isnum(self.current_word):   # 多位数字
            linestring = self.code.split('\n')[self.line][self.lineposition:]
            for i in integer_replacelist:
                linestring = linestring.replace(i,' ')
            linestring = linestring.split()[0]
            if '.' in linestring:
                try:token = Token('floating','float',float(linestring))
                except:self.error('浮点数'+linestring+'不正确')
            else:
                token = Token('integer','int',int(linestring))
            self.position += len(linestring) - 1
            self.lineposition += len(linestring) - 1
            self.current_word = ''
            return token
        if self.current_word.isdigit():  # 一位数字
            token = Token('integer','int',int(self.current_word))
            self.current_word = ''
            return token
        if self.current_word in token_dict:  # 特定符号
            near_char = self.current_word + self.get_near()
            if near_char in token_dict:
                self.current_word = near_char
                self.position += 1
                self.lineposition += 1
            else:     # 特殊处理
                if self.current_word == ' ':   # 最重要的语法：空格~
                    if (not self.token_stack) or self.token_stack[-1].name in ['\n',' ','=','}']:   # 跳过重复无用空格
                        self.current_word = ''
                        return self.get_next_token()
                    self.current_word = ''
                    return Token(' ','space',' ')
                elif self.current_word == '=':   # 变量赋值
                    if self.token_stack and self.token_stack[-1].name == ' ':   # 删除无用空格
                        self.token_stack = self.token_stack[:-1]
                    self.current_word = ''
                    return Token('=','symbol','=')
                elif self.current_word == '{':
                    if self.token_stack and self.token_stack[-1].name == ' ':   # 删除无用空格
                        self.token_stack = self.token_stack[:-1]
                    self.current_word = ''
                    return Token('{','symbol','{')
            token = Token(self.current_word,
                          token_dict[self.current_word][0],
                          token_dict[self.current_word][1])
            self.current_word = ''
            return token
        if self.current_word in keyword_list and (self.get_near() not in varcharlist):
            if self.current_word == 'true':token = Token('bool','bool',True)
            elif self.current_word == 'false':token = Token('bool','bool',False)
            elif self.current_word == 'null':token = Token('null','NoneType',None)
            else:token = Token(self.current_word,'keyword',self.current_word)
            if self.current_word == 'if' and self.token_stack and (not self.token_stack[-1].tp=='EOF'):
                self.position -= 2;self.lineposition -= 2
                token = Token('\n','EOF','\n')
            self.current_word = ''
            return token
        if (self.current_word in namespace) and (self.get_near() not in varcharlist):   # 使用命名空间中的statement
            # if '=' not in self.code.split('\n')[self.line][self.lineposition:]:   # 如果不是赋值(=不在右侧)，就转化
            value = namespace[self.current_word]
            token = Token(self.current_word,'var',value[2])
            self.current_word = ''
            return token
        return self.get_next_token()
    def convert_var(self,var):
        varinfo = namespace[var.name]
        var.name = varinfo[0];var.tp = varinfo[1];var.value = varinfo[2]
        return var
    def calc_unary(self,name,expression):   # 一元运算
        if expression.name in namespace:expression = self.convert_var(expression)
        if name == '+':return (+expression, 'integer', 'int')
        if name == '-':return (-expression, 'integer', 'int')
        if name == '~':return (~expression, 'integer', 'int')
    def calc_binary(self,name,left,right):   # 二元运算
        global namespace
        if name == '=':
            if left.name == right.name == ' ':return
            if left.name[0].isdigit():self.error('变量名不能以数字开头')
            if not left.name.isascii():self.error('变量名不能含有非ascii字符')
            if right.name in namespace:
                namespace[left.name] = namespace[right.name]
                return
            namespace[left.name] = (right.name,right.tp,right.value)
            return
        if left.name in namespace:left = self.convert_var(left)
        if right.name in namespace:right = self.convert_var(right)
        if name == '!=':result = left.value != right.value
        elif name == '==':result = left.value == right.value
        elif name == '<=':result = left.value <= right.value
        elif name == '>=':result = left.value >= right.value
        elif name == '<':result = left.value < right.value
        elif name == '>':result = left.value > right.value
        elif name == '<<':result = left.value << right.value
        elif name == '>>':result = left.value >> right.value
        elif name == '+':result = left.value + right.value
        elif name == '-':result = left.value - right.value
        elif name == '*':result = left.value * right.value
        elif name == '/':result = left.value / right.value
        elif name == '//':result = left.value // right.value
        elif name == '%':result = left.value % right.value
        elif name == '**':result = left.value ** right.value
        else:self.error('解释器接收符号异常')
        tp = str(type(result))[8:-2]
        if tp == 'int':
            name = 'integer'
        elif tp == 'float':
            name = 'floating'
            result = round(result,15)
        elif tp == 'bool':
            name = 'bool'
        return (result,name,tp)
    def calc_ternary(self,name,expr1,expr2,expr3):pass
    def leftconnect(self,stack,level):  # 左结合
        token = -1
        while token < len(stack) - 1:
            token += 1
            tn = stack[token].name
            if tn in operatordict:
                if (level in operatordict[tn]):
                    left = stack[token-1]
                    right = stack[token+1]
                    while left.tp is 'space':
                        del stack[token-1]
                        token -= 1
                        left = stack[token-1]
                        right = stack[token+1]
                    while right.tp is 'space':
                        del stack[token+1]
                        left = stack[token-1]
                        right = stack[token+1]
                    result = self.calc_binary(tn,left,right)
                    stack[token].value, stack[token].name, stack[token].tp = result
                    stack.remove(left)
                    stack.remove(right)
                    token -= 1
        return stack
    def visit(self,stack):
        if stack == []:return []
        token = -1;leftstack = None;rightstack = None;condition_startposition = None;block_startposition = None;braceinside = 0
        did = False  # 是否执行过了
        while token < len(stack) - 1:    # 分支 左结合
            token += 1
            tn = stack[token].name
            if tn == 'if':
                did = False
                condition_startposition = token + 2
            elif tn == 'elif':condition_startposition = token + 2
            elif tn == 'else':condition_startposition = 'ELSE CON'
            elif tn == '{':
                if leftstack is None:
                    if type(condition_startposition) == int:
                        leftstack = stack[:condition_startposition-1]
                    else:
                        leftstack = stack[:token]
                braceinside += 1
                if braceinside == 1:    # 是最外层大括号{
                    block_startposition = token + 1
                    if did:    # 执行过了后面的直接跳过
                        continue
                    if condition_startposition == 'ELSE CON':    # 是else就直接执行
                        condition = True
                        continue
                    condition = stack[condition_startposition:token]
                    condition = self.visit(condition)[0]
                    if condition.name in namespace:
                        condition = self.convert_var(condition)
                    condition = condition.value
            elif tn == '}':
                rightstack = stack[token+1:]
                braceinside -= 1
                if braceinside == 0:    # 是最外层大括号}
                    if did:
                        continue
                    if condition:
                        blockcode = stack[block_startposition:token]
                        self.exprblock(blockcode)
                        did = True
        if leftstack and rightstack:stack = leftstack + rightstack
        token = -1
        parenthese_inside = 0;parenthese_beginpos = 0;parenthese_stack = []
        while token < len(stack)-1:
            token += 1
            tn = stack[token].name
            if parenthese_inside:
                parenthese_stack.append(stack[token])
            if tn in operatordict:
                if (9 in operatordict[tn]):
                    if tn == '(':
                        parenthese_inside += 1
                        if parenthese_inside == 1:
                            parenthese_beginpos = token
                    elif tn == ')':
                        parenthese_inside -= 1
                        if parenthese_inside == 0:
                            parenthese_stack.remove(parenthese_stack[-1])
                            result = self.visit(parenthese_stack)
                            if result:
                                stack[token] = result[0]
                                stack = stack[:parenthese_beginpos]+stack[token:]
                            else:
                                stack = stack[:parenthese_beginpos]+stack[token+1:]
                            token = -1
                            parenthese_stack = []
        token = len(stack)
        while token > 0:
            token -= 1
            tn = stack[token].name
            if tn in operatordict:
                if (8 in operatordict[tn]):
                    left = stack[token-1]
                    right = stack[token+1]
                    while left.tp is 'space':
                        del stack[token-1]
                        token -= 1
                        left = stack[token-1]
                        right = stack[token+1]
                    while right.tp is 'space':
                        del stack[token+1]
                        left = stack[token-1]
                        right = stack[token+1]
                    if left.tp == 'operator':
                        result = self.calc_unary(tn,right)
                        stack[token].value, stack[token].name, stack[token].tp = result
                        stack.remove(right)
        token = len(stack)
        while token > 0:
            token -= 1
            tn = stack[token].name
            if tn in operatordict:
                if (7 in operatordict[tn]):
                    left = stack[token-1]
                    while left.tp is 'space':
                        del stack[token-1]
                        token -= 1
                        left = stack[token-1]
                    right = stack[token+1]
                    result = self.calc_binary(tn,left,right)
                    stack[token].value, stack[token].name, stack[token].tp = result
                    stack.remove(left);stack.remove(right)
        stack = self.leftconnect(stack,6);stack = self.leftconnect(stack,5);stack = self.leftconnect(stack,4);stack = self.leftconnect(stack,3);stack = self.leftconnect(stack,2);token = -1 
        while token < len(stack)-1:
            token += 1
            tn = stack[token].name
            if tn in operatordict:
                if (1 in operatordict[tn]):
                    for i in range(token):
                        left = stack[i];right = stack[token+i+1]
                        self.calc_binary(tn,left,right)  # 赋值
                    stack.clear()
        return stack
    def add_token(self):
        self.current_token = self.get_next_token()
        self.token_stack.append(self.current_token)
        if self.current_token.name == 'ENDEOF':
            return False
        if self.get_near(0) == '\n':
            self.line += 1
            self.lineposition = -1
        return True
    def exprblock(self,stack):
        stack.append(Token('ENDEOF','EOF','ENDEOF'))
        stackline = [];inblocks = 0;totalindex = -1
        for i in stack:
            stackline.append(i)
            totalindex += 1
            if i.name == '{':
                inblocks += 1
            if i.name == '}':
                inblocks -= 1
            if i.name == '\n' and (not inblocks):
                if stack[totalindex+1].name in ['elif','else','\n']:
                    continue
                self.visit(stackline)
                stackline.clear()
        self.visit(stackline)
    def expr(self):
        while self.add_token():pass
        self.exprblock(self.token_stack)
    def run(self):self.expr()
code = 'a=1'
interpreter = Interpreter(code=code)
interpreter.run()
print(namespace)