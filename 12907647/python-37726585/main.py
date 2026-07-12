def make(size):     # 做幻方
    bigsize = size*2-1
    square = [[0 for i in range(bigsize)] for j in range(bigsize)]
    
    posx = 0   # 索引下标从0开始，比习惯少1
    posy = size - 1    # 同上
    
    for i in range(1,size**2+1):
        square[posx][posy] = i
        posx += 1
        posy -= 1
        if i % size == 0:
            posx = i // size
            posy = size + posx - 1
    
    return square

def show(square):     # 看幻方
    l = len(str(len(square)**2))  # 最大数字位数
    for x in square:
        for n in x:
            print('0'*l if not n else '\033[32m'+str(n).zfill(l)+'\033[0m',end=' ')
        print()

def move(size,square):     # 移幻方
    times = (size-1)/2   # 外圈层数
    go = int(times + 1)    # 移到对面通过几个0，非int索引会报错
    
    for n in range(len(square)):
        for m in range(len(square[n])):
            if int(square[n][m]):
                if n < times:
                    # print(square[n][m],'a')   # 分组输出
                    # 套用公式，go*2-1格，增高逼格
                    square[n+(go*2-1)][m] = square[n][m]
                    square[n][m] = 0
                elif m < times:
                    # print(square[n][m],'b')
                    square[n][m+(go*2-1)] = square[n][m]
                    square[n][m] = 0
                if n >= size+times:
                    # print(square[n][m],'c')
                    square[n-(go*2-1)][m] = square[n][m]
                    square[n][m] = 0
                elif m >= size+times:
                    # print(square[n][m],'d')
                    square[n][m-(go*2-1)] = square[n][m]
                    square[n][m] = 0
    return square

def noborder(size,square):     # 去边框
    newsq = [[0 for i in range(size)] for l in range(size)]
    x = 0
    for n in square:
        for m in n:
            if m:
                newsq[x//size][x%size] = m
                x += 1
    return newsq

print('''幻方，是一种数学游戏，具体玩法如下：
画一个[奇数x奇数]的方格图，如3x3
|x|0|0|   这里用0和x代替空格。
|0|x|0| ->这个叫做行
|0|0|x|
 |这个是列   连成x的线是对角线

每个个字里面填不同的数字:
|1|2|3| 就像这样
|4|5|6|  然而，这是个不成功的幻方
|7|8|9|   幻方的要求是：每行、列、对角线之和都要相等
而且，和就是中间的数（如5）的大小（如3）倍

现在我用2小时py算法做了个幻方处理器
输入大小（行数），必须是奇数，确保1<=n，会输出幻方
乱输会有问题，这里就不进行除错了

请输入:''',end='')
size = int(input())
square = make(size)
# show(square)
square = move(size,square)
# show(square)
square = noborder(size,square)
show(square)
print('\n\n谢谢观看。这样就能去卷过手写11阶幻方的二年级时的自己，以及现在手写21阶的初一同学了')