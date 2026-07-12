a=int(input())
b=0
for i in range(2,a//2):
    if a%i==0:
        print("合数")
        exit(0)
print("质数")