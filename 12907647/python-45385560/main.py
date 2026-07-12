def fun(func):
    def inner():
        print('开始测试')
        func()
        print('结束测试\n')
    return inner

@fun
def test1():
    print('测试1')

@fun
def test2():
    print('测试2')

@fun  # 嵌套
@fun
def s():
    print('中间')

test1()
s()
test2()