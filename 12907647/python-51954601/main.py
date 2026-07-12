built_in = {
    '+': (lambda a, b: a + b),
    '-': (lambda a, b: a - b),
    '*': (lambda a, b: a * b),
    '/': (lambda a, b: a / b),
}

def compile_(stream):
    code = []
    define = [{}]
    p = 0
    q = 0
    while p < len(stream):
        symbol = stream[p]
        if symbol in built_in:
            code.append(('blt',built_in[symbol]))
        elif symbol == 'let':
            p += 1
            name = stream[p]
            define[-1][name] = q
            q += 1
            code.append(('store',None))
        elif symbol == 'set':
            p += 1
            var = stream[p]
            site = define[-1][var]
            code.append(('set',site))
        elif symbol == 'get':
            p += 1
            var = stream[p]
            site = define[-1][var]
            code.append(('get',site))
        elif type(symbol) == int:
            code.append(('const',symbol))
        p += 1
    return code

stream = [1,1,'+','let','a','get','a','let','b',6,'set','b',6,'set','a']
code = compile_(stream)

def output_code(code):
    for line in code:
        print(f'{line[0]}: {line[1]}')

print(f'{stream}\n\n')
output_code(code)

from es_runtime import run
stack, scope = run(code)
print(f'\n\nstack: {stack}\nscope: {scope}')