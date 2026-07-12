from time import*
from sys import*
def xprint(text,wait=0.05,end="\n"):
    for i in text:
        stdout.write(i)
        stdout.flush()
        sleep(wait)
    print(end,end="")
while 1:
    xprint('''integer2.2.1语言教程
注意：integer2.2.1语言仅支持后缀表达式
0、结束运行
1、变量
2、输入输出
3、列表
4、函数
5、循环
6、条件分支
7、库
请选择：''',end="")
    ans=input()
    if ans=="0":
        break
    elif ans=="1":
        xprint('''
变量
定义：
    var 变量名=>用以定义一个变量
赋值：
    = 变量名 数字或变量或后缀表达式=>给变量赋值''')
    elif ans=="2":
        xprint('''
输入输出
输入：
    在后缀表达式中加入“input”，可将输入带入表达式
输出：
    put 变量名或列表名或后缀表达式=>输出变量或列表或后缀表达式
    put 列表名[下标]=>输出列表下标为n的元素
    put 值=>输出这个值（也可以是字符串或bool）''')
    elif ans=="3":
        xprint('''
列表
定义：
    list 列表名=>定义一个有0个元素的列表
元素赋值：
    = 列表名[下标] 值=>给列表的某一个元素赋值
操作：
    sizeup 列表名=>给列表增加一个元素
    sizedown 列表名=>删除列表最后一个元素''')
    elif ans=="4":
        xprint('''
函数
注意：
    1、函数调用可能产生大量没用的变量，可以使用 del 变量名 方法删除
    2、函数会直接改变参数的值
定义：
    定义函数：
    func 函数名(参数列表)
    函数的内容
    done
    函数的返回：return 变量或数字=
    就像这样：\033[1;47m\033[1;34m
    func plus(a,b)
    var _a
    = _a a.b.+
    return _a
    done\033[1;0m
使用：
    可以将函数放在后缀表达式中，对于不加入运算的函数，可以：
    var rf
    = rf 函数名(参数列表)''')
    elif ans=="5":
        xprint('''
循环
注意：
    循环使用递归实现，不能continue或break，也不能在循环内使用跳转语句或函数的返回
while循环：
    while 行数 条件
    ······（必须有n行）
    可以嵌套
for循环：
    for 行数 初值 终值 步长
    ······（必须有n行）''')
    elif ans=="6":
        xprint('''
条件分支
注意：
    可以在if语句内使用跳转或返回
模板：
    if 行数 条件
    ······（必须有n行）''')
    elif ans=="7":
        xprint('''
库
导入：
    #use 库名=>导库（库不是python做的，是用integer2.2.1做的，目前的版本的库是为了实验用的，没有使用的意义）
制作：
    在integer2.2.1中有制作教程和预留空间，做完可以发布（写上integer2.x.x+库名）或保存''')