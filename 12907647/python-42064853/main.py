# https://blog.csdn.net/qq_40236497/article/details/125539436
import re

oplist = [
    '+','-','*','/','**','//','%','<<','>>','~','!','..',
    '==','!=','>=','<=','<','>',
    '=','+=','-=','*=','/=','**=','//=','%=','<<=','>>=',
    '&','|','^',
    ' ',
    ':',',',';','.',
]

class Int:
    def __init__(self,number):
        self.value = number
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return str(self.value)
    
    def __add__(self,other):
        return Int(self.value + other.value)
    def __sub__(self,other):
        return Int(self.value - other.value)
    def __mul__(self,other):
        return Int(self.value * other.value)
    def __truediv__(self,other):
        return Int(self.value / other.value)

class Str:
    def __init__(self,string):
        self.value = string
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return str(self.value)
    
    def __add__(self,other):
        return Str(self.value + other.value)
    def __sub__(self,other):
        return Str(self.value.replace(other.value,''))
    def __mul__(self,other):
        return Str(self.value * other.value)
    def __truediv__(self,other):
        if type(other) == Int:
            return Str(self.value[:round(len(self.value) / other.value) + 1])
        return Int(self.value.count(other.value))

class Operator:
    def __init__(self,value):
        self.value = value
    def calc(self,left,right):
        if self.value == '+':
            return left + right
        if self.value == '-':
            return left - right
        if self.value == '*':
            return left * right
        if self.value == '/':
            return left / right

def lexer(code):
    splitlist = []
    codelist = []
    for op in oplist:
        refind = re.finditer(char,string)
        for match in refind:
            splitlist.append(match.span())
    for span in splitlist:
        codelist.append(code)
    
a = Str('cake cola cook check')
b = Str('c')
c = a / Int(2.5)
a /= b
print(a,c)