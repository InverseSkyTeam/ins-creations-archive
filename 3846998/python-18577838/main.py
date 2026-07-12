from random import*
d=0
a=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
b=int(input("次数："))
for i in range(b):
    c=randint(0,25)
    print("请输入字母表中的第",c+1,"个字母：",end='')
    e=input()
    if e==a[c]:
        d=d+1
        print("对了！")
    else:
        print("错了！答案是：",a[c])
print("得分是：",d)