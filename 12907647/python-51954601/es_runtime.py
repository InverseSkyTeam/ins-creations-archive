def run(code):
    stack = []
    scope = []
    p = 0
    while p < len(code):
        cmd, arg = code[p]
        if cmd == 'const':
            stack.append(arg)
        elif cmd == 'blt':
            b = stack.pop()
            a = stack.pop()
            stack.append(arg(a,b))
        elif cmd == 'store':
            scope.append(stack.pop())
        elif cmd == 'set':
            scope[arg] = stack.pop()
        elif cmd == 'get':
            stack.append(scope[arg])
        p += 1
    return stack, scope