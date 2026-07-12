from time import*
from sys import*
def xprint(text,wait=0.05,end="\n"):
    for i in text:
        stdout.write(i)
        stdout.flush()
        sleep(wait)
    print(end,end="")
while 1:
    xprint('''integer语言教程
注意：integer语言不支持表达式
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
    var 变量名 （数字或变量）=>用以定义一个变量
赋值：
    = 变量名 数字或变量=>给变量赋值
    变量名 = 列表名 下标=>给变量赋值为列表的某个元素
运算：
    +、-、*、/或% 变量 变量或数字=>将两数字加减乘除模的结果赋值给第一个''')
    elif ans=="2":
        xprint('''
输入输出
输入：
    input 变量名=>将输入的一个数字赋值给变量
输出：
    print 变量名或列表名=>输出变量或列表
    print 列表名 下标=>输出列表下标为n的元素
    print 值=>输出这个值（也可以是字符串或bool）
    print 函数名=>输出生成的函数定义''')
    elif ans=="3":
        xprint('''
列表
定义：
    list 列表名 元素数量=>定义一个有n个元素的列表
元素赋值：
    列表名 下标 = 变量或数字=>给列表的某一个元素赋值
操作：
    sizeup 列表名=>给列表增加一个元素
    sizedown 列表名=>删除列表最后一个元素''')
    elif ans=="4":
        xprint('''
函数
定义：
    function 函数名(参数列表)
    函数的内容
    函数名.end=>定义函数
    注意：参数列表中有三种参数，一种是arg，就像python函数里的参数；
    一种是changable_arg，会在函数内被改变；
    一种是getret_var，只能有一个，接受传回的参数
    就像这样：\033[1;47m\033[1;34m
    function a(arg:a,changable_arg:b,getret_var:c)
    ······
    a.end\033[1;0m
    函数的返回：return 变量或数字=>返回
使用：
    use 函数名(参数列表)=>使用函数''')
    elif ans=="5":
        xprint('''
循环
无限循环：
    标签名:
    ······
    goto 标签名
    可以嵌套''')
    elif ans=="6":
        xprint('''
条件分支
模板：
    if 变量 ==、>=、<=、>或< 变量或数字 标签名
    ······
    标签名.end''')
    elif ans=="7":
        xprint('''
库
导入：
    #use 库名=>导库（库不是python做的，是用integer做的，目前的版本有的库都是为了实验用的，没有使用的意义）''')