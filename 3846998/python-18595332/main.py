'''
0000E000EE
EEE0E0E000
EEE000EEE0
EEEEEEEEE0
0000000000
0EEEEEEEE0
0000000000
EEE0EEEEEE
EEE0000000
EEEEEEEEE0
'''
E="E"
map=[[0,0,0,0,E,0,0,0,E,E],
[E,E,E,0,E,0,E,0,0,0],
[E,E,E,0,0,0,E,E,E,0],
[E,E,E,E,E,E,E,E,E,0],
[0,0,0,0,0,0,0,0,0,0],
[0,E,E,E,E,E,E,E,E,0],
[0,0,0,0,0,0,0,0,0,0],
[E,E,E,0,E,E,E,E,E,E],
[E,E,E,0,0,0,0,0,0,0],
[E,E,E,E,E,E,E,E,E,0]]
def up(x,y):
    map[x][y]=0
    x=x-1
    map[x][y]="H"
    return(x)
def down(x,y):
    map[x][y]=0
    x=x+1
    map[x][y]="H"
    return(x)
def right(x,y):
    map[x][y]=0
    y=y+1
    map[x][y]="H"
    return(y)
def left(x,y):
    map[x][y]=0
    y=y-1
    map[x][y]="H"
    return(y)
def end(x,y):
    if (x==9 or x==-1) and (y==9 or y==-1):
        print("WIN!")
        exit(0)
def fail(e_xlist,e_ylist):
    for i in range(len(e_xlist)):
        if x==e_xlist[i] and y==e_ylist[i]:
            print("FAIL!")
            exit(0)
def show(map):
    print("H表示你自己，D表示终点，0表示空，地图如下")
    for i in range(10):
        for j in range(10):
            print(map[i][j],end="")
        print()
e_xlist=[]
e_ylist=[]
for i in range(10):
    for j in range(10):
        if map[i][j]=="E":
            e_xlist.append(i)
            e_ylist.append(j)
y_add=0
x=0
y=0
map[9][9]="D"
map[0][0]="H"
show(map)
while 1:
    a=input("请输入指令(1(上)、2(下)、3(左)或4(右))：")
    if a=="1":
        x=up(x,y)
    elif a=="2":
        x=down(x,y)
    elif a=="3":
        y=left(x,y)
    elif a=="4":
        y=right(x,y)
    fail(e_xlist,e_ylist)
    end(x,y)
    show(map)