from random import*
print("石头剪刀布，九局五胜")
a1=0
b1=0
for i in range(9):
    a=int(input('请输入你要出的手势（石头1，剪刀2，布3）'))
    b=randint(1,3)
    if b==1:
        print('电脑出的是石头')
        if a==3:
            print('你赢了')
            a1=a1+1
        else:
            print('你输了')
            b1=b1+1
    if b==2:
        print("电脑出的是剪刀")
        if a==1:
            a1=a1+1
            print("你赢了")
        else:
            print("你输了")
            b1=b1+1
    if b==3:
        print("电脑出的是布")
        if a==2:
            print("你赢了")
            a1=a1+1
        else:
            print("你输了")
            b1=b1+1
print('你的得分是',a1,'\n电脑的得分是',b1)
if a1>b1:
    print('你赢了')
else:
    print('你输了')