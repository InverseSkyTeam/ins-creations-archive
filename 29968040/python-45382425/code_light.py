import keyword

# 获取内置函数和关键字列表
builtins = ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
keywords = keyword.kwlist
# 定义 Token 类，包含类型(tp)、值(value)和颜色(color)属性
class Token():
    def __init__(self, tp, value):
        self.tp = tp
        self.value = value
        self.color = None
    def __str__(self):
        return f"({self.tp} , {self.value})"
    
    __repr__ = __str__

                
            
# 定义 Scanner 类，用于将代码解析成一系列 Token，并返回 Token 列表
class Scanner():
    def __init__(self,code):
        self.code = code
        self.pos = 0
        self.char = code[0]
    
    # 将指针向前移动一位
    def advance(self):
        self.pos += 1
        if self.pos < len(self.code):
            self.char = self.code[self.pos]
        else:
            self.char = None
    # 读取一个 Token，并返回
    def get_token(self):
        while self.char:
            #print(self.char)
            # 数字类型 Token
            if self.char.isdigit():
                res = ""
                while self.char and(self.char.isdigit() or self.char == "."):
                    res += self.char
                    self.advance()
                return Token('NUMBER', res)
            
            # 字符串类型 Token
            elif self.char == '"' or self.char == "'":
                quot = self.char
                is_row=False#是否是原始字符串
                is_duo=False#是否是多行字符串
                if self.code[self.pos-1]=='r':
                    is_row=True
                res = ''
                is_zhuanyi=False
                num=0
                can_check=1
                while self.char:
                    #print(res)
                    if can_check==1:
                        if self.char==quot and num<3:
                            num+=1
                        else:
                            can_check=2
                            if num>=3:
                                is_duo=True
                            elif num==2:
                                return Token('STRING', res)
                            else:
                                is_duo=False
                    if can_check==3:
                        if self.char==quot and not is_zhuanyi and num>0:
                            is_zhuanyi=False
                            num-=1
                        else:
                            if num>0:
                                can_check=2
                                if is_duo:
                                    num=3
                                else:
                                    num=1
                            elif num==0:
                                return Token('STRING', res)
                    if can_check==2:
                        if self.char==quot and not is_zhuanyi:
                            is_zhuanyi=False
                            num-=1
                            can_check=3
                    
                    if is_duo==False and self.char=='\n':
                        return Token('STRING', res)
                    if not is_zhuanyi and self.char=='\\' and not is_row:
                        is_zhuanyi=True
                    else:
                        is_zhuanyi=False
                    res += self.char
                    self.advance()
                return Token('STRING', res)
            #注释
            elif self.char=='#':
                res=""
                while self.char and self.char!='\n':
                    res += self.char
                    self.advance()
                return Token('ZHUSHI', res)
            # 其它类型 Token，包括关键字、内置函数和标识符等
            elif self.char.isalpha() or self.char=='_':
                res = ""
                while self.char and self.char.isalnum() or self.char=='_':
                    res += self.char
                    self.advance()
                if res in builtins:
                    return Token('BUILTIN', res)
                elif res in keywords:
                    return Token('KEYWORD', res)
                else:
                    return Token('OTHER', res)
            
            # 其它类型 Token，包括运算符、标点符号等
            else:
                char = self.char
                self.advance()
                return Token('OTHER', char)
    
    # 将输入代码解析成 Token 列表
    def tokens(self):
        ret = []
        while self.char:
            ret.append(self.get_token())
        return ret
# 颜色表，用于在控制台中将不同类型的 Token 显示为不同颜色
colortable = {
    'NUMBER': (0,0,255/2),#数字
    'STRING': (0,255,0),#字符串
    'BUILTIN': (218, 165, 32),#内置函数
    'KEYWORD': (0,0,255),#关键字
    'OTHER': (0,0,0),#其他
    'ZHUSHI':(255/2,255/2,255/2),#注释
}

# 为 Token 着色
def color(tokens):
    #print(tokens)
    res=[[]]
    for token in tokens:
        #print(token)
        token.color = colortable[token.tp]
        for i in token.value:
            if i=='\n':
                res.append([])
            else:
                res[-1].append(token.color)
    return res
    