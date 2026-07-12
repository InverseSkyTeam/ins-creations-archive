print("三子棋，规则：两名玩家，A玩家先走，共下九步后，将三子连成一条线者胜")
a=["-","1","2","3","4","5","6","7","8","9"]
def b():
    print(a[1],a[2],a[3])
    print(a[4],a[5],a[6])
    print(a[7],a[8],a[9])
b()
for i in range(9):
    if i %2==0:
        A=int(input("A玩家走（输入点位）"))
        a[A]="X"
    else:
        B=int(input("B玩家走（输入点位）"))
        a[B]="O"
    b()
if a[1]==a[2]==a[3]=="O" or a[1]==a[4]==a[7]=="O" or a[2]==a[5]==a[8]=="O" or a[3]==a[6]==a[9]=="O" or a[4]==a[5]==a[6]=="O" or a[7]==a[8]==a[9]=="O":
    print("A玩家胜！")    
elif a[1]==a[2]==a[3]=="X" or a[1]==a[4]==a[7]=="X" or a[2]==a[5]==a[8]=="X" or a[3]==a[6]==a[9]=="X" or a[4]==a[5]==a[6]=="X" or a[7]==a[8]==a[9]=="X":
    print("B玩家胜！")
else:
    print("平局！")