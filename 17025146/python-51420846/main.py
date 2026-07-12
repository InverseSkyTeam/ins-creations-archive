# 我已经打算把这个新结构语言写成静态语言了。
import copy
import time
# 面向对象
"""
class Duck{
    let name = "Duck"
    let age = 5
    fun constructor(age){
        this.age = age
    }
    fun out(){
        println(this.name)
        println(this.age)
    }
}
let duck = new Duck(10)
duck.name = "Bird"
duck.out()
"""
ast = ("BLOCK",
    ("CLASS", ("VARTERM", "Duck"), tuple(), ("BLOCK",
        ("LET", ("VARTERM", "name"), ("LITERAL", "Duck")),
        ("LET", ("VARTERM", "age"), ("LITERAL", 5)),
        ("FUN", ("VARTERM", "constructor"), (("VARTERM", "age"),), ("BLOCK",
            ("ASSIGN", ("DOT", ("VAR", "this"), ("VARTERM", "age")), ("VAR", "age"))
        )),
        ("FUN", ("VARTERM", "out"), tuple(), ("BLOCK",
            ("PRINT", ("DOT", ("VAR", "this"), ("VARTERM", "name"))),
            ("PRINT", ("DOT", ("VAR", "this"), ("VARTERM", "age")))
        ))
    )),
    ("LET", ("VARTERM", "duck"), ("NEW", ("VARTERM", "Duck"), ("ARRAY", ("LITERAL", 10)))),
    ("ASSIGN", ("DOT", ("VAR", "duck"), ("VARTERM", "name")), ("LITERAL", "Bird")),
    ("CALL", ("DOT", ("VAR", "duck"), ("VARTERM", "out")), ("ARRAY",))
)

# 注意:这里面不包含and和or运算,因其需要短路机制,故特殊处理
BINARY_TABLE = {
    "SUB": lambda a, b: ["BASE", a[1] - b[1]],
    "ADD": lambda a, b: ["BASE", a[1] + b[1]],
    "MUL": lambda a, b: ["BASE", a[1] * b[1]],
    "DIV": lambda a, b: ["BASE", a[1] / b[1]],
    "MOD": lambda a, b: ["BASE", a[1] % b[1]],
    "POWER": lambda a, b: ["BASE", a[1] ** b[1]],
    "EQ": lambda a, b: ["BASE", a[1] == b[1]],
    "LT": lambda a, b: ["BASE", a[1] < b[1]],
    "LE": lambda a, b: ["BASE", a[1] <= b[1]],
    "GT": lambda a, b: ["BASE", a[1] > b[1]],
    "GE": lambda a, b: ["BASE", a[1] >= b[1]],
    "LSH": lambda a, b: ["BASE", a[1] << b[1]],
    "RSH": lambda a, b: ["BASE", a[1] >> b[1]],
    "BITAND": lambda a, b: ["BASE", a[1] & b[1]],
    "BITOR": lambda a, b: ["BASE", a[1] | b[1]],
    "XOR": lambda a, b: ["BASE", a[1] ^ b[1]]
}
UNARY_TABLE = {
    "NOT": lambda a: ["BASE", not a[1]],
    "BITNOT": lambda a: ["BASE", ~ a[1]]
}

# 注意:所有在run函数中没有处理的边界情况,都是由parser和checker保证不会出现的.
def run(ast):
    callstack = [{}]
    typescope = {}
    value_stack = []
    op_stack = [[ast, 1]]
    while True:
        scope = callstack[-1]
        node = op_stack[-1][0]
        count = op_stack[-1][1]
        op = node[0]
        if op == "LITERAL" or op == "VARTERM":
            value = node[1]
            value_stack.append(["BASE", value])
            op_stack.pop()
            if op_stack:
                op_stack[-1][1] += 1
            else:
                break
        elif op == "ARRAY":
            num = len(node) - 1
            if count > num:
                args = [copy.deepcopy(value_stack.pop()) for _i in range(num)][::-1]
                value_stack.append(["BASE", args])
                op_stack.pop()
                if op_stack:
                    op_stack[-1][1] += 1
                else:
                    break
            else:
                op_stack.append([node[count], 1])
        elif op == "OBJECT":
            if count > 2:
                args = [value_stack.pop() for _i in range(2)][::-1]
                keys = args[0][1]
                values = args[1][1]
                target = {}
                for i in range(len(keys)):
                    key = keys[i]
                    value = values[i]
                    target[key[1]] = value
                value_stack.append(["OBJECT", target])
                op_stack.pop()
                if op_stack:
                    op_stack[-1][1] += 1
                else:
                    break
            else:
                op_stack.append([node[count], 1])
        elif op == "VAR":
            name = node[1]
            for table in callstack[::-1]:
                if name in table:
                    value = table[name]
                    break
            value_stack.append(value)
            op_stack.pop()
            if op_stack:
                op_stack[-1][1] += 1
            else:
                break
        elif op == "INDEX":
            if count > 2:
                args = [value_stack.pop() for _i in range(2)][::-1]
                obj = args[0][1]
                index = args[1][1]
                value = obj[index]
                value_stack.append(value)
                op_stack.pop()
                if op_stack:
                    op_stack[-1][1] += 1
                else:
                    break
            else:
                op_stack.append([node[count], 1])
        elif op == "DOT":
            if count > 2:
                args = [value_stack.pop() for _i in range(2)][::-1]
                obj = args[0]
                obj_value = obj[1]
                index = args[1][1]
                value = obj_value[index]
                if value[0] == "FUN":
                    value[3]["this"] = obj
                value_stack.append(value)
                op_stack.pop()
                if op_stack:
                    op_stack[-1][1] += 1
                else:
                    break
            else:
                op_stack.append([node[count], 1])
        elif op in BINARY_TABLE:
            if count > 2:
                args = [value_stack.pop() for _i in range(2)][::-1]
                value = BINARY_TABLE[op](*args)
                value_stack.append(value)
                op_stack.pop()
                if op_stack:
                    op_stack[-1][1] += 1
                else:
                    break
            else:
                op_stack.append([node[count], 1])
        elif op in UNARY_TABLE:
            if count > 1:
                args = [value_stack.pop()]
                value = UNARY_TABLE[op](*args)
                value_stack.append(value)
                op_stack.pop()
                if op_stack:
                    op_stack[-1][1] += 1
                else:
                    break
            else:
                op_stack.append([node[count], 1])
        elif op == "AND" or op == "OR":
            if count == 2:
                value = value_stack.pop()
                if (op == "AND" and not value[1]) or (op == "OR" and value[1]):
                    value_stack.append(value)
                    op_stack.pop()
                    if op_stack:
                        op_stack[-1][1] += 1
                    else:
                        break
                else:
                    if op_stack:
                        op_stack[-1][1] += 1
                    else:
                        break
                    op_stack.append([node[count], 1])
            elif count > 2:
                op_stack.pop()
                if op_stack:
                    op_stack[-1][1] += 1
                else:
                    break
            else:
                op_stack.append([node[count], 1])
        elif op == "ASSIGN":
            if count > 2:
                args = [value_stack.pop() for _i in range(2)][::-1]
                var = args[0]
                value = args[1]
                var[1] = copy.deepcopy(value[1])
                value_stack.append(copy.deepcopy(value))
                op_stack.pop()
                if op_stack:
                    op_stack[-1][1] += 1
                else:
                    break
            else:
                op_stack.append([node[count], 1])
        elif op == "BLOCK":
            num = len(node) - 1
            if count > num:
                op_stack.pop()
                if op_stack:
                    op_stack[-1][1] += 1
                else:
                    break
            else:
                if count > 1:
                    value_stack.pop()
                op_stack.append([node[count], 1])
        elif op == "LET":
            if count > 2:
                args = [value_stack.pop() for _i in range(2)][::-1]
                name = args[0][1]
                value = args[1]
                scope[name] = copy.deepcopy(value)
                value_stack.append(copy.deepcopy(value))
                op_stack.pop()
                if op_stack:
                    op_stack[-1][1] += 1
                else:
                    break
            else:
                op_stack.append([node[count], 1])
        elif op == "IF":
            if count == 2:
                cond = value_stack.pop()[1]
                callstack.append({})
                if cond:
                    op_stack.append([node[2], 1])
                else:
                    op_stack.append([node[3], 1])
            elif count < 2:
                op_stack.append([node[count], 1])
            else:
                callstack.pop()
                op_stack.pop()
                if op_stack:
                    op_stack[-1][1] += 1
                else:
                    break
        elif op == "WHILE":
            if count == 2:
                cond = value_stack.pop()[1]
                num = op_stack[-1][2]
                if cond:
                    if num == 0:
                        callstack.append({})
                    else:
                        value_stack.pop()
                    op_stack.append([node[2], 1])
                else:
                    if num != 0:
                        callstack.pop()
                    op_stack.pop()
                    if op_stack:
                        op_stack[-1][1] += 1
                    else:
                        break
            elif count > 2:
                op_stack[-1][1] = 1
            else:
                information = op_stack[-1]
                if len(information) < 3:
                    information.append(0)
                else:
                    information[2] += 1
                op_stack.append([node[count], 1])
        elif op == "LOOP":
            op_stack.append([node[1], 1])
        elif op == "BREAK":
            if count > 1:
                while op_stack[-1][0][0] not in ("WHILE", "FOR", "LOOP"):
                    op_stack.pop()
                op_stack.pop()
                if op_stack:
                    op_stack[-1][1] += 1
                else:
                    break
            else:
                op_stack.append([node[count], 1])
        elif op == "CONTINUE":
            while op_stack[-1][0][0] not in ("WHILE", "FOR", "LOOP"):
                op_stack.pop()
            op_stack[-1][2] += 1
        elif op == "FUN":
            funname = node[1][1]
            funargs = [i[1] for i in node[2]]
            funblock = node[3]
            funtable = callstack[-1]
            funobj = ("FUN", funargs, funblock, funtable)
            scope[funname] = funobj
            value_stack.append(funobj)
            op_stack.pop()
            if op_stack:
                op_stack[-1][1] += 1
            else:
                break
        elif op == "LAMBDA":
            fungreet = [i[1] for i in node[1]]
            funblock = node[2][1]
            funtable = callstack[-1]
            value_stack.append(("FUN", fungreet, funblock, funtable))
            op_stack.pop()
            if op_stack:
                op_stack[-1][1] += 1
            else:
                break
        elif op == "CALL":
            if count == 3:
                args = [value_stack.pop() for _i in range(2)][::-1]
                fun = args[0]
                fungreet = fun[1]
                funargs = copy.deepcopy(args[1][1])
                new_scope = fun[3]
                for i in range(len(fungreet)):
                    new_scope[fungreet[i]] = funargs[i]
                callstack.append(new_scope)
                op_stack.append([fun[2], 1])
            elif count > 3:
                value_stack.append(copy.deepcopy(value_stack.pop()))
                callstack.pop()
                op_stack.pop()
                if op_stack:
                    op_stack[-1][1] += 1
                else:
                    break
            else:
                op_stack.append([node[count], 1])
        elif op == "RETURN":
            if count > 1:
                callstack.pop()
                while op_stack[-1][0][0] != "CALL":
                    op_stack.pop()
                op_stack.pop()
                if op_stack:
                    op_stack[-1][1] += 1
                else:
                    break
            else:
                op_stack.append([node[count], 1])
        elif op == "CLASS":
            if count == 1:
                classname = node[1][1]
                classextends = [i[1] for i in node[2]]
                classcode = node[3]
                extendscontent = {}
                for name in classextends[::-1]:
                    extendscontent.update(typescope[name])
                typescope[classname] = extendscontent
                op_stack.append([classcode, 1])
                callstack.append({})
            elif count > 1:
                table = callstack.pop()
                typescope[classname].update(table)
                op_stack.pop()
                if op_stack:
                    op_stack[-1][1] += 1
                else:
                    break
        elif op == "NEW":
            if count == 3:
                args = [value_stack.pop() for _i in range(2)][::-1] # 取得参数
                classobj = typescope[classname] # 得到类属性和方法表
                init = classobj["constructor"] # 拿到构造函数
                fungreet = init[1] # 得到构造函数形参表
                funargs = copy.deepcopy(args[1][1]) # 得到构造函数实参表
                classscope = copy.deepcopy(classobj) # 通过类属性和方法表复制出this表
                new_scope = {"this": ["OBJECT", classscope]} # 构造带this的符号表
                for i in range(len(fungreet)): # 形参实参一一对应
                    new_scope[fungreet[i]] = funargs[i]
                callstack.append(new_scope)
                op_stack.append([init[2], 1])
            elif count > 3:
                value_stack.pop()
                obj = callstack.pop()["this"]
                value_stack.append(obj)
                op_stack.pop()
                if op_stack:
                    op_stack[-1][1] += 1
                else:
                    break
            else:
                op_stack.append([node[count], 1])
        elif op == "PRINT":
            if count > 1:
                print(value_stack.pop())
                value_stack.append(["BASE", None])
                op_stack.pop()
                if op_stack:
                    op_stack[-1][1] += 1
                else:
                    break
            else:
                op_stack.append([node[count], 1])
t1 = time.time()
run(ast)
t2 = time.time()
print(t2 - t1)