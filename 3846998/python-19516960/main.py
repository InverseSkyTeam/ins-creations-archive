print("每个数字中间请用‘,’隔开")
a=eval(input())
b=[]
for i in range(len(a)):
    b.append(int(a[i]))
c=[]
for i in range(len(b)):
    c.append(max(b))
    b.remove(max(b))
for i in range(len(c)):
    if i<len(c)-1:
        print(c[i],end=',')
    else:
        print(c[i])