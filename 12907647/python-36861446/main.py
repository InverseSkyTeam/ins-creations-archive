calclist = []
s = input('请输入后缀表达式:').split()
for i in s:
    try:
        int(i)
    except:
        calclist.append(str(eval(calclist[-2]+i+calclist[-1])))
        for i in [1,2]:calclist.remove(calclist[-2])
    else:
        calclist.append(i)
print(calclist[0])