a=input()
a=a+' '
b=[]
i1=0
for i in range(len(a)):
    if a[i]==' ':
        if a[i]!=len(a)-1:
            b.append(a[i1:i])
            i1=i+1
        else:
            b.append(a[i1:-1])
print(b)
for i in b:
    print(i)