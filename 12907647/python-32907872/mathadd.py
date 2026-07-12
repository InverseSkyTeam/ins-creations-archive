letterlist = [chr(i) for i in range(65,91)]+[chr(i) for i in range(97,123)]+['(','[','{'] # A-Z,a-z代数字母的ASCLL符号转译
symlist = ['+','-','*','/','%','^','(','[','{']
def addmulti(text):
    text = list(text) + ['' for i in range(5)]
    x = -1
    for i in text:
        x += 1
        try:
            if (i not in symlist) and (text[x+1] in letterlist):
                text.insert(x+1,'*')
        except IndexError:
            break
    text = ''.join(text)
    print(text)
    text = \
    text.replace('s*q*r*t*','sqrt') \
        .replace('s*i*n*','sin') \
        .replace('c*o*s*','cos') \
        .replace('t*a*n*','tan') \
        .replace('c*o*t*','cot') \
        .replace('m*o*d','mod') \
        .replace('l*o*g','log') \
        .replace('e*x*p','exp') \
        .replace('f*f*','ff')
    return text