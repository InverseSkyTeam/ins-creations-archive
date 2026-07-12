import sys

stack = [] # 栈
var_table = {} # 变量表
func_table = {} # 函数表
label_table = {} # 标签表

expr = """
var n,result,i
push 10
pop n
push 1
pop result
push 0
pop i
label:
push i
push 1
add
pop i
push result
push i
mul
pop result
print result
push n
push i
lt
jnz label
"""
def is_var_name(name):
    if name[0].isalpha():
        for char in name:
            if char.isalnum() or char == "_":
                pass
            else:return False
        return True
    else:return False

opdict = {
    "add":lambda a,b: a + b,
    "sub":lambda a,b: a - b,
    "mul":lambda a,b: a * b,
    "div":lambda a,b: a / b,
    "mod":lambda a,b: a % b,
    "eq":lambda a,b: int(a == b),
    "gt":lambda a,b: int(a > b),
    "ge":lambda a,b: int(a >= b),
    "lt":lambda a,b: int(a < b),
    "le":lambda a,b: int(a <= b),
    "ne":lambda a,b: int(a != b),
    "and":lambda a,b: int(a and b),
    "or":lambda a,b: int(a or b),
    "xor":lambda a,b: int(a ^ b)
}

codelist = expr.split("\n") # 以行为单位分解为逐条指令
i = -1
while i + 1 < len(codelist):
    i += 1
    code = codelist[i]
    if not code:
        continue
    code = code.strip() # 消除行首和行尾的空格
    if code[-1] == ":": # 判定定义标签或函数
        command,space,name = code[:-1].partition(" ")
        command = command.lower()
        if command == "func":
            pass
        else:
            name = code[:-1]
            if is_var_name(name) and name not in label_table:
                label_table[name] = i
            else:
                print("错误")
                sys.exit(0)
    else:
        command,space,arg = code.partition(" ") # 获取指令名和参数
        command = command.lower() # 将指令转换为全小写
        if space: # 当存在参数时
            if command == "push":
                if arg.isdigit():
                    value = int(arg)
                elif is_var_name(arg) and arg in var_table:
                    value = stack[var_table[arg]]
                elif (arg[0] == "'" and arg[-1] == "'") or (arg[0] == '"' and arg[-1] == '"'):
                    value = arg[1:-1]
                else:
                    print("错误")
                    sys.exit(0)
                stack.append(value)
            elif command == "pop":
                if is_var_name(arg) and arg in var_table:
                    value = stack.pop()
                    stack[var_table[arg]] = value
            elif command == "print":
                if (arg[0] == "'" and arg[-1] == "'") or (arg[0] == '"' and arg[-1] == '"'):
                    value = arg[1:-1]
                    argc = value.count("{}")
                    value = value.format(*stack[len(stack) - argc:])
                    print(value)
                elif is_var_name(arg) and arg in var_table:
                    print(stack[var_table[arg]])
                else:
                    print("错误")
                    sys.exit(0)
            elif command == "var":
                for var in arg.split(","):
                    var = var.strip()
                    if is_var_name(var) and var not in var_table:
                        var_table[var] = len(stack)
                        var_table[len(stack)] = var
                        stack.append("/")
                    else:
                        print("错误")
                        sys.exit(0)
            elif command == "jmp":
                if is_var_name(arg) and arg in label_table:
                    i = label_table[arg]
                else:
                    print("错误")
                    sys.exit(0)
            elif command == "jz":
                value = stack.pop()
                if value == 0:
                    if is_var_name(arg) and arg in label_table:
                        i = label_table[arg]
                    else:
                        print("错误")
                        sys.exit(0)
            elif command == "jnz":
                value = stack.pop()
                if value:
                    if is_var_name(arg) and arg in label_table:
                        i = label_table[arg]
                    else:
                        print("错误")
                        sys.exit(0)
        else:
            if command == "pop":
                stack.pop()
            elif command in opdict:
                value1 = stack.pop()
                value2 = stack.pop()
                ret = opdict[command](value1,value2)
                stack.append(ret)