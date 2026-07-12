class Int:
    def __init__(self,number):
        self.value = number
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return str(self.value)
    
    def __add__(self,other):
        return self.value + other.value
    def __sub__(self,other):
        return self.value - other.value

class Str:
    def __init__(self,string):
        self.value = string
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return str(self.value)
    
    def __add__(self,other):
        return self.value + other.value
    def __sub__(self,other):
        return self.value.replace(other.value,'')

class Plus:
    def __init__(self,left,right):
        self.result = left + right
    def __str__(self):
        return str(self.result)
    def __repr__(self):
        return str(self.result)

class Minus:
    def __init__(self,left,right):
        self.result = left - right
    def __str__(self):
        return str(self.result)
    def __repr__(self):
        return str(self.result)

a = Int(3)
b = Str('abc')
c = Int(4)
d = a + c
e = a - c
f = Str('b')
b = Minus(b,f)
print(a,b,c,d,e)