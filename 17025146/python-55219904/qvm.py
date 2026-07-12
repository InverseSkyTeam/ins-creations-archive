import copy

def run(code):
    stack = []
    temporary = []
    scope = []
    pos = 0
    BINARY = {
        "ADD": lambda a, b: a + b,
        "SUB": lambda a, b: a - b,
        "MUL": lambda a, b: a * b,
        "DIV": lambda a, b: a / b,
        "MOD": lambda a, b: a % b,
        "EQ": lambda a, b: a == b,
        "NEQ": lambda a, b: a != b,
        "GT": lambda a, b: a > b,
        "LT": lambda a, b: a < b,
        "GE": lambda a, b: a >= b,
        "LE": lambda a, b: a <= b,
        "RSH": lambda a, b: a >> b,
        "LSH": lambda a, b: a << b,
        "BITAND": lambda a, b: a & b,
        "BITOR": lambda a, b: a | b,
        "XOR": lambda a, b: a ^ b,
        "AND": lambda a, b: a and b,
        "OR": lambda a, b: a or b,
        "GET_ITEM": lambda a, b: a[b]
    }
    UNARY = {
        "NOT": lambda a: not a,
        "BITNOT": lambda a: ~a
    }
    while pos < len(code):
        instruction, arg = code[pos]
        if instruction == "LOAD_CONST":
            stack.append(arg)
        elif instruction == "LOAD_VAR":
            value = scope[arg]
            stack.append(value)
        elif instruction == "STORE":
            value = stack.pop()
            scope.append(value)
        elif instruction == "SET_VAR":
            value = stack.pop()
            scope[arg] = value
        elif instruction in BINARY:
            right = stack.pop()
            left = stack.pop()
            value = BINARY[instruction](left, right)
            stack.append(value)
        elif instruction in UNARY:
            val = stack.pop()
            value = UNARY[instruction](val)
            stack.append(value)
        elif instruction == "JMP":
            pos = arg - 1
        elif instruction == "JZ":
            cond = stack.pop()
            if not cond:
                pos = arg - 1
        elif instruction == "JNZ":
            cond = stack.pop()
            if cond:
                pos = arg - 1
        elif instruction == "GOTO": # GOTO和JMP的区别在于,GOTO是根据栈顶的值进行跳转而非参数
            value = stack.pop()
            pos = value - 1
        elif instruction == "QUIT":
            del scope[arg]
        elif instruction == "STAGE":
            value = stack.pop()
            temporary.append(value)
        elif instruction == "LOAD_TEMP":
            value = temporary[arg]
            stack.append(value)
        elif instruction == "SET_TEMP":
            value = stack.pop()
            temporary[arg] = value
        elif instruction == "LIST":
            values = [stack.pop() for _ in range(arg)]
            stack.append(values)
        elif instruction == "OBJECT":
            values = {stack.pop(): stack.pop() for _ in range(arg)}
            stack.append(values)
        elif instruction == "SET_ITEM":
            value = stack.pop()
            item = stack.pop()
            obj = stack.pop()
            new = copy.deepcopy(obj)
            new[item] = value
            stack.append(new)
        elif instruction == "PRINT":
            value = stack.pop()
            print(value)
        pos += 1