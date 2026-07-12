class stack:
    def __init__(self):
        self.s=[]
    def pop(self):
        return self.s.pop()
    def top(self):
        return self.s[-1]
    def push(self,s):
        self.s.append(s)
class VM:
    def __init__(self,code):
        self.code=code
        self.s=stack()
    def run(self):
        lb={}
        _i=0
        for i in self.code:
            if type(i)==str and i[-1]==":":
                lb[i]=_i
            _i+=1
        i=0
        while i<len(self.code):
            if i=="push":
                i+=1
                self.s.push(self.code[i])
            if i=="pop":
                self.s.pop()
            if i=="jz":
                i+=1
                name=self.code[i]
                if self.s.pop():
                    i=lb[name]
            if i in "+ - * / % == != > < >= <=":
                r=self.s.pop()
                l=self.s.pop()
                self.s.push(eval(str(l)+i+str(r)))
            i+=1