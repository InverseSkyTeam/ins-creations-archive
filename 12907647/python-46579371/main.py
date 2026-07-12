import re

code = '2%1//10+0.05*2-1.+.1+1/5'
print('py:',eval(code))

def calc_expr(expr):
    expr = str(expr)
    if not expr:
        return None
    if (expr.isdigit()) or (expr[0] == '-' and expr[1:].isdigit()):
        return int(expr)
    if (expr.replace('.','').isdigit()) or (expr[0] == '-' and expr[1:].replace('.','').isdigit()):
        if expr.count('.') < 2:
            return round(float(expr),12)
        else:
            raise Exception('数字中不能超过一个小数点！')
    
    if re.findall('\(.*\)',expr):
        a = re.findall('\(.*\)',expr)[0]
        raise Exception(f"暂不支持括号，括号内容标记: {a}")
    
    expr_symbol_list = re.findall('[\+-]',expr)
    if expr_symbol_list:
        expr_list = re.split('[\+-]',expr)
        result = calc_expr(expr_list.pop(0))
        if type(result) not in ['int','float']:
            result = 0
        for i in range(len(expr_list)):
            if expr_symbol_list[i] == '+':
                result += calc_expr(expr_list[i])
            else:
                result -= calc_expr(expr_list[i])
        return calc_expr(result)
    
    expr_symbol_list = re.findall('//|[\*/%]',expr)
    if expr_symbol_list:
        expr_list = re.split('//|[\*/%]',expr)
        result = calc_expr(expr_list.pop(0))
        for i in range(len(expr_list)):
            if expr_symbol_list[i] == '*':
                result *= calc_expr(expr_list[i])
            elif expr_symbol_list[i] == '/':
                result /= calc_expr(expr_list[i])
            elif expr_symbol_list[i] == '//':
                result //= calc_expr(expr_list[i])
            else:
                result %= calc_expr(expr_list[i])
        return calc_expr(result)

code = calc_expr(code)
print('ij:',code)
print('三小时手搓，才50行，原因是因为对算法犹豫多次删改。支持整数、小数的六则运算(+ - / * % //)，不支持括号')