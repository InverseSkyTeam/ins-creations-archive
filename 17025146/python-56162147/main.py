from copy import deepcopy

class Token:
    def __init__(self, token):
        self.token = token

class Error:
    def __init__(self, message=None):
        self.message = message

class Env:
    def __init__(self, text, pos=0, packrat=None):
        self.text = text
        self.pos = pos
        self.packrat = packrat if packrat else {}
        self.res = None

class Combinator:
    def __add__(self, other):
        return And([self, other])
    def __or__(self, other):
        return Or([self, other])
    def many(self):
        return Many(self)
    def some(self):
        return Some(self)

class Epsilon(Combinator):
    def __init__(self):
        pass

    def parse(self, env):
        env.pos += 1
        return env

class Text(Combinator):
    def __init__(self, text):
        self.text = text
    
    def parse(self, env):
        text, pos = env.text, env.pos
        if pos >= len(text):
            env.res = Error()
            return env
        for i in range(pos, len(self.text)):
            if self.text[i] != text[i]:
                env.res = Error()
                return env
        env.pos += len(self.text)
        env.res = Token(self.text)
        return env

class Or(Combinator):
    def __init__(self, patterns):
        self.patterns = patterns

    def parse(self, env):
        res = deepcopy(env)
        for pattern in self.patterns:
            res = pattern.parse(res)
            if isinstance(res.res, Error):
                res = deepcopy(env)
                continue
            else:
                return res
        env.res = Error()
        return env

class And(Combinator):
    def __init__(self, patterns):
        self.patterns = patterns

    def parse(self, env):
        tree = []
        res = env
        for pattern in self.patterns:
            res = pattern.parse(res)
            if isinstance(res.res, Error):
                return res
            else:
                tree.append(res.res)
        res.res = tree
        return res

class Many(Combinator):
    def __init__(self, pattern):
        self.pattern = pattern

    def parse(self, env):
        res = env
        tree = []
        while True:
            res = self.pattern.parse(res)
            if isinstance(res.res, Error):
                break
            else:
                tree.append(res.res)
        res.res = tree
        return env

class Some(Combinator):
    def __init__(self, pattern):
        self.pattern = pattern

    def parse(self, env):
        res = deepcopy(env)
        res = self.pattern.parse(res)
        if isinstance(res.res, Error):
            env.res = Error()
            return env
        tree = [res.res]
        while True:
            res = self.pattern.parse(res)
            if isinstance(res.res, Error):
                break
            else:
                tree.append(res.res)
        res.res = tree
        return res

class Fn(Combinator):
    def __init__(self, fn):
        self.fn = fn
    
    def parse(self, env):
        if (env.pos, self.fn.__name__) in env.packrat:
            env = env.packrat[(env.pos, self.fn.__name__)]
            return env
        res =  self.fn().parse(env)
        env.packrat[(env.pos, self.fn.__name__)] = res
        return res

def A():
    return (Text("a") + Fn(A)) | Text("a")

print(Fn(A).parse(Env("aaa")).res)