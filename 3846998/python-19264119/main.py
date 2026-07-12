a=[]
for i in range(3):
    a.append([])
    for j in range(10):
        a[i].append([])
        for k in range(10):
            a[i][j].append(0)
'''
0000000000
0000000*00
000*000*00
00*0000*00
0*0*******
*0*0000*00
00*0**0*00
00*0000*00
00*000**00
0000000000
'''
j2=3
for i in range(2,6):
    a[0][i][j2]='█'
    j2=j2-1
j2=2
for i in range(5,9):
    a[0][i][j2]='█'
j2=3
for i in range(7):
    a[0][4][j2]='▁'
    j2=j2+1
j2=7
for i in range(1,9):
    a[0][i][j2]='█'
a[0][8][6]='█'
a[0][6][4]='█'
a[0][6][5]='█'
'''
0000000000
00******00
000*00*000
000*00*000
**********
000*00*000
00*000*000
0*0000*000
000000*000
0000000000
'''
j2=1
for i in range(2,8):
    a[1][j2][i]='▁'
j2=4
for i in range(10):
    a[1][j2][i]='▁'
j2=2
for i in range(4):
    a[1][j2][3]='█'
    j2=j2+1
a[1][6][2]='█'
a[1][7][1]='█'
j2=2
for i in range(7):
    a[1][j2][6]='█'
    j2=j2+1
for i in a:
    for j in i:
        for k in j:
            print(k,end='')
        print()
    print()