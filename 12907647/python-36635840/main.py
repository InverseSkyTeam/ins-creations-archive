symbols = ['(',')','+','-','*','/','^','%','//','=','.']
numbers = [str(i) for i in range(10)]

def math_to_python(text):
    text = text.replace('^','**') \
               .replace('×','*') \
               .replace('÷','/') \
               .replace('mod','%') \
               .replace('|','//') \
               .replace('[','(') \
               .replace(']',')')
    return text

def find_formula(command):        # 过滤算法复杂度:O(n log n)
    command = command + ' '
    formulalist = []
    formula = ''
    
    for i in range(len(command)):  # 找出所有连续的数字、算式
        if command[i] in numbers:
            formula += command[i]
        elif command[i] in symbols:
            formula += command[i]
        else:
            if formula:
                formulalist.append(formula)
                formula = ''
    
    finalformulalist = []
    for i in formulalist:   # 只有数字没有符号的删掉
        is_formula = 0
        for symbol in symbols:
            if symbol in i:
                is_formula = 1
                break
        if is_formula:
            finalformulalist.append(i)
    
    formulalist = finalformulalist
    finalformulalist = []
    for i in formulalist:   # 只有浮点数没有运算符号的删掉
        try:
            float(i)
        except:
            if i not in symbols:
                finalformulalist.append(i)
    return finalformulalist

def calc_formula(commandlist):  # O(n) 
    answerlist = ''
    for i in commandlist:
        try:
            answerlist += i + '的答案是:' + str(round(eval(i.replace('=','')),4)) + '\n'
        except:
            'Edit Calc Error'
            # 1/0
            # 1+2+3+
            # +1+
            # ++(心脏骤停)
    if answerlist:
        answerlist = answerlist.replace('%','mod') \
                               .replace('//','|') \
                               .replace('**','^') \
                               .replace('*','×') \
                               .replace('/','÷') \
                               .replace('=','')
        return answerlist
    return False

print('''这个程序可以计算输入的算式
可以输入的符号：
数字
()[]
+-*/ 四则运算
^ 幂
mod 取模
| 整除

可以同时计算多个算式
输入的非数字、数学符号将会被屏蔽

输入格式：
(3+6)*3/9
计算1+1
告诉我(3+6*2)之后/5的计算结果
请问(1.1+2.2)*3、5*6和(1+2+3)/2的结果分别是什么
''')
text = input('>>')
text = math_to_python(text)
text = find_formula(text)
text = calc_formula(text)
if text:
    print(text)
else:
    print('未发现算式')
print('体验完毕，该功能以后将会加到我那个人工智障的作品里！')