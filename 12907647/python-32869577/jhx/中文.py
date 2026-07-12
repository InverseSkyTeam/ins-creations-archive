输入 = input
输出 = print
def 中文跑路(codes,run='直接运行'):
    codes = codes.replace('$输出','print') \
                 .replace('$打印','print') \
                 .replace('$输入','input') \
                 .replace('$如果','if') \
                 .replace('$再如','elif') \
                 .replace('$否则','else') \
                 .replace('$定义函数','def') \
                 .replace('$定义类','class') \
                 .replace('$返回','return') \
                 .replace('$游戏库','pygame') \
                 .replace('$操作系统库','os') \
                 .replace('$时间库','time') \
                 .replace('$数学库','math') \
                 .replace('$海龟库','turtle') \
                 .replace('$随机库','random') \
                 .replace('$随机取整','randint') \
                 .replace('$系统库','sys') \
                 .replace('$数字库','numpy') \
                 .replace('$高精度数学库','sympy') \
                 .replace('$机器学习库','sklearn') \
                 .replace('$百度库','aip') \
                 .replace('$wx库','wx') \
                 .replace('$tk库','tkinter') \
                 .replace('$，',',') \
                 .replace('$（','(') \
                 .replace('$）',')') \
                 .replace('$循环|f','for') \
                 .replace('$循环|w','while') \
                 .replace('$在','in') \
                 .replace('$：',':') \
                 .replace('$化整','int') \
                 .replace('$化字符串','str') \
                 .replace('$化浮点','float') \
                 .replace('$化列表','list') \
                 .replace('$化字典','dict') \
                 .replace('$化元组','tuple') \
                 .replace('$与','and') \
                 .replace('$和','and') \
                 .replace('$或','or') \
                 .replace('$非','not') \
                 .replace('$不在','not in') \
                 .replace('$中的','.') \
                 .replace('$。。。','.') \
                 .replace('$导入','import') \
                 .replace('$从','from') \
                 .replace('$休眠','sleep') \
                 .replace('$系统','system') \
                 .replace('$开始','start') \
                 .replace('$执行','exec') \
                 .replace('$转命令','eval') \
                 .replace('$是','True') \
                 .replace('$否','False') \
                 .replace('$空空如也','pass') \
                 .replace('$时间戳','time()') \
                 .replace('$事件','event') \
                 .replace('$获取','get')
    if run == '直接运行':
        exec(codes)
    else:
        return codes   # 间接跑路