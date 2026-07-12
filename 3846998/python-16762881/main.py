a=int(input())
b=0
c=0
for i in range(2,a//2):
    if a%i==0:
        for j in range(2,i//2):
            if i%j==0:
                break
            else:
                c+=1
        if c==i//2-2:
            b=i
print(b)