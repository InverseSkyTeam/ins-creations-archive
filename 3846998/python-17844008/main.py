a=input()
c=len(a)-1
for i in range(len(a)//2):
    b=a[i]
    d=a[c]
    if b!=d:
        print("NO")
        exit(0)
    c=c-1
print("YES")