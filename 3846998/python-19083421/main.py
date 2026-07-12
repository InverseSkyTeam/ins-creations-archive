h=0
h2=0
a=int(input("你想要几以内的完全数？"))
def ys(i,j):
    if i%j==0:
        return(j)
    else:
        return(0)
for i in range(2,a+1):
    h=0
    for j in range(2,i//2+1):
        y=ys(i,j)
        h=h+y
    if h+1==i:
        print(i)
        h2=h2+1
print(a,"里面共有",h2,"个完全数")