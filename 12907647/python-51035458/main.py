# notlisp、Firefly、storm、speciallang

import re

class Scanner:
    def __init__(self,code):
        self.code = code
        self.scanner = re.Scanner([
            (r'[0-9]+\.[0-9]*', lambda scanner, token: ['float',token]),
            (r'\.[0-9]+', lambda scanner, token: ['float',token]),
            (r'[0-9]+', lambda scanner, token: ['int',token]),
            (r'\\.', lambda scanner, token: ['escape',token]),
            ('["\']', lambda scanner, token: ['quoter',token]),
            (r'[A-Za-z_]\w*', lambda scanner, token: ['alpha',token]),
            (r'\(|\)|\[|\]|\{|\}', lambda scanner, token: ['paren',token]),
            (r',', lambda scanner, token: ['comma',token]),
            (r':', lambda scanner, token: ['colon',token]),
            (r'\.', lambda scanner, token: ['dot',token]),
            (r'[>=<!]=', lambda scanner, token: ['op',token]),
            (r'[+-]|[*/%=|^&<>]', lambda scanner, token: ['op',token]),
            (r'\n+', lambda scanner, token: ['ln',token]),
            (r' +', lambda scanner, token: ['space',token]),
            (r'.+', lambda scanner, token: ['unk',token]),
        ])
        self.warn = False
        while self.code[0] == '\n':
            self.code = self.code[1:]
        while self.code[-1] == '\n':
            self.code = self.code[:-1]
        if self.code[0] != '{':
            self.code = '{\n' + self.code
            self.warn = True
        if self.code[-1] != '}':
            self.code = self.code + '\n}'
            self.warn = True
    def scan(self):
        result, rest = self.scanner.scan(self.code)
        if rest: raise Exception(f'小丑吧，怎么解析不出来这代码！\n剩余:\n{rest}')
        return (result + [['EOF','']], self.warn)

class Tree:
    def __init__(self,*args):
        self.args=args
    def __getitem__(self,n):
        return self.args[n]
    def __str__(self):
        return type(self).__name__+"("+",".join(map(str,self.args))+")"
    __repr__=__str__
class Const(Tree):...
class Var(Tree):...
class Tuple(Tree):...
class List(Tree):...
class Let(Tree):...
class Def(Tree):...
class NewFn(Tree):...
class Binary(Tree):...
class Unary(Tree):...
class Block(Tree):...
class PublicBlock(Tree):...
class If(Tree):...
class While(Tree):...
class Break(Tree):...
class Return(Tree):...
class Continue(Tree):...
class Call(Tree):...
class Index(Tree):...
class Empty(Tree):...

class Parser:
    def __init__(self,stream):
        self.stream = stream
    
    def get_prio(self,op):
        return {
            '*': 10, '/': 10, '%': 10, '//': 10,
            '+': 9, '-': 9,
            '>>': 8, '<<': 8,
            '==': 7, '!=': 7, '<': 7, '>': 7, '>=': 7, '<=': 7,
        }[op]
    
    def escape(self,e):
        return {
            r'\n': '\n',
            r'\r': '\r',
            r'\t': '\t',
            r'\v': '\v',
            r'\s': ' ',
            r'\a': '\a',
            r'\b': '\b',
            r'\f': '\f',
            r'\\': '\\',
            r'\"': '"',
            r"\'": "'",
        }[e]
    
    def parse(self,stream):
        p = 0
        ttype, token = stream[p]
        
        # 返回此并指向下
        def eat(ex=None):
            nonlocal ttype, token, stream, p
            if ex in [None,token]:
                this = token
                p += 1
                while stream[p][0] == 'space':
                    p += 1
                ttype, token = stream[p]
                return this
            raise Exception(f'不匹配的单词{token}')
        
        def block(public=False):
            if token != '{':
                if public:
                    return PublicBlock(stmt())
                return Block(stmt())
            eat('{')
            l = []
            while token != '}':
                s = stmt()
                if s != None:
                    l.append(s)
                if ttype == 'ln':
                    eat()
            eat('}')
            if public:
                return PublicBlock(*l)
            return Block(*l)
        
        def stmt():
            if token == 'if':
                eat()
                eat('(')
                condition = expr()
                eat(')')
                body = block(True)
                else_body = Empty()
                if token == 'else':
                    eat()
                    else_body = block(True)
                return If(condition,body,else_body)
            if token == 'while':
                eat()
                eat('(')
                condition = expr()
                eat(')')
                body = block(True)
                else_body = Empty()
                if token == 'else':
                    eat()
                    else_body = block(True)
                return While(condition,body,else_body)
            if token == 'return':
                eat()
                return Return(expr())
            if token == 'break':
                eat()
                return Break()
            if token == 'continue':
                eat()
                return Continue()
            if token == 'def':
                eat()
                name = eat()
                return Def(name,parse_fn())
            if token == '{':
                return block()
            e = expr()
            return e
        
        def parse_fn():    # 定义函数
            eat('(')
            if token == ')':
                param_list = []
            else:
                param_list = [eat()]
                while token == ',':
                    eat()
                    param_list.append(eat())
            eat(')')
            return NewFn(param_list,block())
        
        def expr():
            res = factor()
            if token in ['+','-','*','/','%','>','<','>=','<=','==','!=',]:
                res = Binary(eat(),res,factor())
                while token in ['+','-','*','/','%','>','<','>=','<=','==','!=',]:
                    op = eat()
                    fac = factor()
                    if self.get_prio(res[0]) > self.get_prio(op):
                        res=Binary(op,res,fac)
                    else:
                        res=Binary(res[0],res[1],Binary(op,res[2],fac))
            if token == '=':
                eat()
                if type(res) in (Const,List,Tuple):
                    raise Exception(f'不可以给非变量赋值！\n错误:{res}')
                res = Let(res,expr())
            return res
        
        def factor():
            if token == 'true':
                eat()
                return Const(True)
            if token == 'false':
                eat()
                return Const(False)
            if token == 'null':
                eat()
                return Const(None)
            if ttype == 'int':
                return Const(int(eat()))
            if ttype == 'float':
                return Const(float(eat()))
            if ttype == 'alpha':
                return check_list(Var(eat()))
            if token == '(':
                lst, has_comma = get_list(0)
                llst = len(lst)
                if (llst == 1) and (not has_comma):
                    return lst[0]
                return check_list(Tuple(*lst))
            if token == '[':
                return check_list(List(*get_list(1)[0]))
            if token in ['"',"'"]:
                string = get_string()
                return Const(string)
            if token in ('+','-'):
                return Unary(eat(),factor())
        
        # 获取字符串
        def get_string():
            q = eat()
            text = ''
            while token != q:         # 没有遇到下一个相同引号
                if ttype == 'escape':    # 需要转义
                    text += self.escape(eat())
                else:
                    text += eat()
            eat(q)
            return text
        
        # 判断接下来的get_list,v:上一层token
        # 举例: func(...)[...](...)一个list后还有一个list
        def check_list(v):
            if token == '(':
                call_list = get_list(0)[0]
                return check_list(Call(v,call_list))
            if token == '[':
                call_list = get_list(1)[0]
                return check_list(Index(v,call_list))
            return v
        
        # 获取形如 括号+(*内容,)+括号的形式
        # 举例：(a,b,c,d) [a,b,c,d] {a,b,c,d}(目前不可用) <a,b,c,d>(目前不可用)
        def get_list(paren_tp):
            leftp, rightp = [('(',')'),('[',']'),('{','}'),('<','>')][paren_tp]
            eat(leftp)
            l = []
            has_comma = False
            while token != rightp:
                e = expr()
                l.append(e)
                if token == ',':
                    has_comma = True
                    eat()
            eat(rightp)
            return (l,has_comma)
        
        return block()
    
    def get_ast(self):
        return self.parse(self.stream)

class Fn:
    def __init__(self,param,body,closure):
        self.param, self.body, self.closure = param, body, closure
    def __call__(self,runner,*args):
        if len(args) != len(self.param):
            raise Exception('参数数量不匹配')
        ret = runner(self.body, self.closure + [dict(zip(self.param,args))])
        if ret == None:
            return None
        return ret[0]

class Interpreter:
    def __init__(self,ast):
        self.ast = ast
        self.global_scope = [{
            'out': print,
            'in': input,
            'int': int,
            'float': float,
            'str': str,
            'len': len,
            'round': round,
            'pow': pow,
            'ord': ord,
            'chr': chr,
            'insert': lambda l, a: l + [a,],
        }]
        self.dic_op_bin = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b,
            '%': lambda a, b: a % b,
            '==':lambda a, b: a == b,
            '!=':lambda a, b: a != b,
            '>': lambda a, b: a > b,
            '<': lambda a, b: a < b,
            '>=': lambda a, b: a >= b,
            '<=': lambda a, b: a <= b,
            '<<': lambda a, b: a << b,
            '>>': lambda a, b: a >> b,
            '&': lambda a, b: a & b,
            '|': lambda a, b: a | b,
            '^': lambda a, b: a ^ b,
        }
        self.dic_op_un = {
            '+': lambda expr: +expr,
            '-': lambda expr: -expr,
            '~': lambda expr: ~expr,
            # '!': lambda expr: not expr,
        }
    def get_var(self,name,scope):
        for level in reversed(scope):
            if name in level:
                return level[name]
        raise NameError(f'没有变量{name}')
    def run(self,tree,scope):
        tp = type(tree)
        if tp == Const:
            return tree[0]
        if tp == Var:
            return self.get_var(tree[0],scope)
        if tp == Tuple:
            return tuple(self.run(expr,scope) for expr in tree)
        if tp == List:
            return [self.run(expr,scope) for expr in tree]
        if tp == Unary:
            op = tree[0]
            expr = self.run(tree[1],scope)
            return self.dic_op_un[op](expr)
        if tp == Binary:
            op = tree[0]
            l = self.run(tree[1],scope)
            r = self.run(tree[2],scope)
            return self.dic_op_bin[op](l,r)
        if tp == Block:
            scope.append({})
            for son in tree:
                v = self.run(son,scope)
                if type(v) in [Return, Break, Continue]:
                    scope.pop(-1)
                    return v
            scope.pop(-1)
            return
        if tp == PublicBlock:
            for son in tree:
                v = self.run(son,scope)
                if type(v) in [Return, Break, Continue]:
                    return v
            return
        if tp == Let:
            left = tree[0]
            right = tree[1]
            if type(left) == Var:
                scope[-1][left[0]] = value = self.run(right,scope)
                return value
            if type(left) == Index:
                iter_ = self.run(left[0],scope)
                index_ = self.run(left[1][0],scope)
                value = self.run(right,scope)
                iter_[index_] = value
                return value
            raise Exception(f'不支持赋值的类型:{tree}')
        if tp == NewFn:
            return Fn(tree[0],tree[1],scope)
        if tp == Def:
            scope[-1][tree[0]] = self.run(tree[1],scope)
            return
        if tp == If:
            if self.run(tree[0],scope):
                return self.run(tree[1],scope)
            return self.run(tree[2],scope)
        if tp == While:
            while self.run(tree[0],scope):
                v = self.run(tree[1],scope)
                if type(v) == Break:
                    break
                if type(v) == Continue:
                    continue
            else:
                return self.run(tree[2],scope)
            return
        if tp == Return:
            return Return(self.run(tree[0],scope))
        if tp == Break:
            return tree
        if tp == Continue:
            return tree
        if tp == Call:
            func = self.run(tree[0],scope)
            if type(func) == Fn:
                return func(self.run,*[self.run(t,scope) for t in tree[1]])
            return func(*[self.run(t,scope) for t in tree[1]])
        if tp == Index:
            iter_ = self.run(tree[0],scope)
            index_ = self.run(tree[1][0],scope)
            return iter_[index_]
        if tp == Empty:
            return
            
    def execut(self):
        self.run(self.ast,self.global_scope)



awa = '''{
    code = "++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>."
    array = [0]
    p = 0
    i = 0
    while (i < len(code)) {
        if (code[i] == "<") {
            if (p > 0) p = p - 1
        }
        if (code[i] == ">") {
            p = p + 1
            if (len(array) <= p) array = insert(array,0)
        }
        if (code[i] == "+") {
            array[p] = array[p] + 1
        }
        if (code[i] == "-") {
            array[p] = array[p] - 1
        }
        if (code[i] == ".") {
            out(array[p],chr(array[p]))
        }
        if (code[i] == ",") {
            x = ord(in("input: "))
            array[p] = x
        }
        if (code[i] == "[") {
            if (array[p]==0) {
                while (code[i] != "]") i = i + 1
            }
        }
        if (code[i] == "]") {
            if (array[p]!=0) {
                while (code[i] != "[") i = i - 1
            }
        }
        i = i + 1
    }
}'''

scanner = Scanner(awa)
stream, warn = scanner.scan()
# print(stream)

parser = Parser(stream)
ast = parser.get_ast()
# print(ast)

print('\n\n结果:')

Interpreter = Interpreter(ast)
Interpreter.execut()

if warn:
    print('警告: 程序结构不完整: 开头或结尾没有{}表示域')