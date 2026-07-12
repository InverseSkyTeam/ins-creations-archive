print('首页上的阶乘太水了，算不满17，C++算法果然菜，还是py来解决吧(py输入50000多都没问题(5秒)，每算10000多算1秒，多输出2.58秒)')
print('-'*60)
while True:
    try:
        n = int(input('输入n，将要阶乘至n'))
    except:
        product = '输入有误'
    else:
        product = 1
        if n > 0:
            for i in range(1,n+1):
                product *= i
    finally:
        print('答案是\033[1;32m{}\033[0m，可继续输入'.format(product))
        input('回车继续')
        print('\033[100A\033[2J\033[100A\033[3J')