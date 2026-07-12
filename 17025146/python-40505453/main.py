def lex(code):
    tokens = []
    pos = 0
    char = code[pos]
    def advance(num=1):
        nonlocal code,pos,char
        for _i in range(num):
            pos += 1
            if pos < len(code):
                char = code[pos]
            else:
                char = None
                break
    def peek():
        return code[pos + 1] if pos+1 < len(code) else ""
    symbol = ["+","-","*","/","%","**","==","!=",">","<",">=","<=","=",";","\n",":",";",",",".","->","(",")","[","]","{","}"]
    while char:
        if char.isspace() and char != "\n":
            advance()
            continue
        elif char == "/" and peek() == "/":
            while char != "\n":
                advance()
        elif char == "/"  and peek() == "*":
            while char != "*" or peek() != "/":
                advance()
            advance(2)
        elif char.isdigit():
            res = ""
            while char.isdigit() or char == ".":
                res += char
                advance()
            if "." in res:
                tokens.append(("number",float(res)))
            else:
                tokens.append(("number",int(res)))
        elif char == '"' or char == "'":
            quote = char
            advance()
            res = ""
            while char != quote:
                res += char
                advance()
            advance()
            tokens.append(("str",res))
        elif char.isalpha() or char == "_":
            res = ""
            while char.isalnum() or char == "_":
                res += char
                advance()
            if res == "true" or res == "false":
                tokens.append(("bool",res))
            elif res == "null":
                tokens.append(("nil","null"))
            else:
                tokens.append(("var",res))
        elif char+peek() in symbol:
            res = char+peek()
            advance(2)
            tokens.append((res,res))
        elif char in symbol:
            res = char
            advance()
            tokens.append((res,res))
        else:
            raise Exception("无法识别的Token")
    tokens.append(("end","end"))
    return tokens

def parse(tokens):
    pos = 0
    token = tokens[pos]
    def eat(tp=None):
        nonlocal tokens,pos,token
        if tp:
            if token[0] == tp:
                pos += 1
                token = tokens[pos]
            else:
                raise Exception("语法错误")
        else:
            pos += 1
            token = tokens[pos]
    def back(num):
        nonlocal tokens,pos,token
        pos -= num
        token = tokens[pos]
    def factor():
        if token[1] in ("+","-","not"):
            op = token[1]
            eat()
            return {"name":"UnaryOp","attr":{"op":op,"expr":factor()}}
        elif token[0] in ("number","str","bool"):
            tp,value = token
            eat()
            return {"name":"BaseLiterial","attr":{"type":tp,"value":value}}
        elif token[0] == "(":
            eat("(")
            node = expr()
            eat(")")
            return node
        elif token[0] == "[":
            eat("[")
            while token[0] == "\n":
                eat()
            res = []
            while token[0] != "]":
                node = expr()
                res.append(node)
                num = 0
                while token[0] == "\n":
                    num += 1
                    eat()
                if token[0] == "]":
                    break
                else:
                    back(num)
                    eat(",")
                    while token[0] == "\n":
                        eat()
            eat("]")
            return {"name":"ArrayLiterial","attr":{"type":"array","value":res}}
        elif token[0] == "{":
            eat("{")
            while token[0] == "\n":
                eat()
            if token[0] == "}":
                return {"name":"ObjectLiterial","attr":{"type":"object","value":{}}}
            node = expr()
            if (node["name"] == "Variable" or (node["name"] == "BaseLiterial" and node["attr"]["type"] == "str")) and token[0] == ":":
                back(1)
                res = {}
                while token[0] != "}":
                    if token[0] == "str" or token[0] == "var":
                        key = token[1]
                        eat()
                    else:
                        eat("string")
                    eat(":")
                    value = expr()
                    res[key] = value
                    num = 0
                    while token[0] == "\n":
                        num += 1
                        eat()
                    if token[0] == "}":
                        break
                    else:
                        back(num)
                        eat(",")
                        while token[0] == "\n":
                            eat()
                eat("}")
                return {"name":"ObjectLiterial","attr":{"type":"object","value":res}}
            stmtlist = [node]
            while token[0] == ";" or token[0] == "\n":
                eat()
                stmtlist.append(expr())
            eat("}")
            return {"name":"Block","attr":{"children":stmtlist}}
        elif token[0] == "}":
            return {"name":"EmpytStmt","attr":{}}
        elif token[1] == "if":
            eat()
            condition = expr()
            stmt = expr()
            elsestmt = None
            if token[1] == "else":
                eat()
                elsestmt = expr()
            return {"name":"IfStmt","attr":{"condition":condition,"root":stmt,"else":elsestmt}}
        elif token[1] == "while":
            eat()
            condition = expr()
            stmt = expr()
            return {"name":"WhileStmt","attr":{"condition":condition,"root":stmt}}
        elif token[1] == "fun":
            eat()
            name = {"name":"Variable","attr":{"name":token[1]}}
            eat("var")
            eat("(")
            if token[0] == ")":
                params = []
            else:
                first = token[1]
                eat("var")
                params = [first]
                while token[0] == ",":
                    eat()
                    params.append(token[1])
                    eat("var")
            eat(")")
            stmt = expr()
            return {"name":"FunStmt","attr":{"name":name,"params":params,"root":stmt}}

        elif token[1] == "print":
            eat()
            value = expr()
            return {"name":"PrintStmt","attr":{"value":value}}
        elif token[1] == "len":
            eat()
            value = expr()
            return {"name":"LenStmt","attr":{"value":value}}
        elif token[0] == "var":
            name = token[1]
            eat()
            return {"name":"Variable","attr":{"name":name}}
        else:
            return {"name":"EmptyStmt","attr":{}}
    def method():
        node = factor()
        while token[0] in ("[",".","("):
            if token[0] == "[":
                eat()
                index = expr()
                eat("]")
                node = {"name":"IndexOp","attr":{"left":node,"right":index}}
            elif token[0] == ".":
                eat()
                attr = token[1]
                eat("var")
                node = {"name":"DotOp","attr":{"left":node,"right":attr}}
            elif token[0] == "(":
                eat()
                if token[0] == ")":
                    params = []
                else:
                    params = [expr()]
                    while token[0] == ",":
                        eat()
                        params.append(expr())
                eat(")")
                node = {"name":"CallOp","attr":{"left":node,"params":params}}
        return node
    def term():
        node = method()
        while token[0] in ("**"):
            op = token[1]
            eat()
            node = {"name":"BinOp","attr":{"op":op,"left":node,"right":method()}}
        return node
    def xterm():
        node = term()
        while token[0] in ("*","/","%"):
            op = token[1]
            eat()
            node = {"name":"BinOp","attr":{"op":op,"left":node,"right":term()}}
        return node
    def addsub():
        node = xterm()
        while token[0] in ("+","-"):
            op = token[1]
            eat()
            node = {"name":"BinOp","attr":{"op":op,"left":node,"right":xterm()}}
        return node
    def compare():
        node = addsub()
        while token[0] in (">",">=","<","<=","==","!="):
            op = token[1]
            eat()
            node = {"name":"BinOp","attr":{"op":op,"left":node,"right":addsub()}}
        return node
    def andor():
        node = compare()
        while token[1] in ("and","or"):
            op = token[1]
            eat()
            node = {"name":"BinOp","attr":{"op":op,"left":node,"right":compare()}}
        return node
    def expr():
        node = andor()
        while token[0] in ("=","+=","-=","*=","/=","**=","%="):
            if node["name"] not in ("Variable","AssignStmt","DotOp","IndexOp"):
                raise Exception("语法错误")
            op = token[1]
            eat()
            node = {"name":"AssignStmt","attr":{"left":node,"op":op,"right":andor()}}
        return node
    stmts = [expr()]
    while  token[0] in ("\n",";"):
        eat()
        stmts.append(expr())
    block = {"name":"Block","attr":{"children":stmts}}
    return {"name":"Program","attr":{"name":"main","block":block}}
def formatout(expr):
    if isinstance(expr,list):
        return {"value":[formatout(i) for i in expr]}
    elif isinstance(expr,dict):
        return {"value":{k:formatout(v) for k,v in expr.items()}}
    else:
        return {"value":expr}
def formatin(expr):
    if isinstance(expr,list):
        return [formatin(v["value"]) for v in expr]
    elif isinstance(expr,dict):
        return {k:formatin(v["value"]) for k,v in expr.items()}
    else:
        return expr
def interpreter(ast):
    symbol={"member":{},"enclosing":None,"closure":{}}
    def interpret(ast):
        nonlocal symbol
        anothersymbol = None
        ast = ast["value"]
        tp = ast["name"]["value"]
        value = ast["attr"]["value"]
        if tp == "Program":
            symbol["member"]["__ast__"] = {"value":ast}
            interpret(value["block"])
        elif tp == "Block":
            stmts = value["children"]["value"]
            i = 0
            while i < len(stmts):
                stmt = stmts[i]
                res = interpret(stmt)
                stmts = value["children"]["value"]
                i += 1
            return res
        elif tp == "Variable":
            name = value["name"]["value"]
            anothersymbol = symbol
            while True:
                if name in symbol["member"]:
                    ptr = symbol["member"][name]
                    symbol = anothersymbol
                    return ptr
                elif symbol["enclosing"]:
                    symbol = symbol["enclosing"]
                else:
                    symbol = anothersymbol
                    break
            symbol["member"][name] = {"value":None}
            return symbol["member"][name]
        elif tp == "AssignStmt":
            left = interpret(value["left"])
            right = interpret(value["right"])
            left["value"] = right["value"]
            return right
        elif tp == "FunStmt":
            fun = interpret(value["name"])
            function = {"params":value["params"]["value"],"root":value["root"]["value"]}
            fun["value"] = function
            return function
        elif tp == "CallOp":
            function = interpret(value["left"])["value"]
            paramlist = value["params"]["value"]
            params =  function["params"]
            if len(paramlist) != len(params):
                raise Exception("函数调用错误")
            newsymbol = {}
            for i in range(len(params)):
                newsymbol[params[i]["value"]] = {"value":interpret(paramlist[i])["value"]} # 此处提取value再封装value是为了避免传递引用
            symbol = {"member":newsymbol,"enclosing":symbol}
            ret = interpret({"value":function["root"]})
            symbol = symbol["enclosing"]
            return ret
        elif tp == "BinOp":
            opdict = {
                "+":lambda a,b:a+b,
                "-":lambda a,b:a-b,
                "*":lambda a,b:a*b,
                "/":lambda a,b:a/b,
                "**":lambda a,b:a**b,
                "%":lambda a,b:a%b,
                ">":lambda a,b:a>b,
                "==":lambda a,b:a==b,
                ">=":lambda a,b:a>=b,
                "<":lambda a,b:a<b,
                "<=":lambda a,b:a<=b,
                "!=":lambda a,b:a!=b,
                "and":lambda a,b:a and b,
                "or":lambda a,b:a or b
            }
            op = value["op"]["value"]
            left = interpret(value["left"])["value"]
            right = interpret(value["right"])["value"]
            return {"value":opdict[op](left,right)}
        elif tp == "UnaryOp":
            opdict = {
                "+":lambda a:a,
                "-":lambda a:-a,
                "not":lambda a:not a
            }
            op = value["op"]["value"]
            expr = interpret(value["expr"])["value"]
            return {"value":opdict[op](expr)}
        elif tp == "IndexOp":
            left = interpret(value["left"])["value"]
            index = interpret(value["right"])["value"]
            return left[index]
        elif tp == "DotOp":
            left = interpret(value["left"])["value"]
            attr = value["right"]["value"]
            return left[attr]
        elif tp == "BaseLiterial":
            return {"value":value["value"]["value"]}
        elif tp == "ArrayLiterial":
            return {"value":[interpret(expr) for expr in value["value"]["value"]]}
        elif tp == "ObjectLiterial":
            res = {}
            for k,v in value["value"]["value"].items():
                res[k] = interpret(v)
            return {"value":res}
        elif tp == "IfStmt":
            condition = value["condition"]
            root = value["root"]
            elseroot = value["else"]
            if interpret(condition)["value"]:
                return interpret(root)
            else:
                return interpret(elseroot)
        elif tp == "WhileStmt":
            condition = value["condition"]
            root = value["root"]
            while interpret(condition)["value"]:
                res = interpret(root)
            return res
        elif tp == "PrintStmt":
            expr = interpret(value["value"])["value"]
            print(formatin(expr))
            return {"value":None}
        elif tp == "LenStmt":
            expr = interpret(value["value"])["value"]
            return {"value":len(expr)}
        elif tp == "EmptyStmt":
            pass
    interpret(ast)
code = """
fun add(left,right){
    print left+right
}
add(1,2)
"""
tokens = lex(code)
ast = parse(tokens)
interpreter(formatout(ast))