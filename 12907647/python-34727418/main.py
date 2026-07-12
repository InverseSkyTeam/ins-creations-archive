def vertical_type_calc(n1,n2,tp='+'):
    string = ''
    stringlist = []
    if n1 > n2:
        big = n1
        small = n2
    else:
        big = n2
        small = n1
    empty_length = len(str(big))-len(str(small))+2
    string += '  '+str(big)+'\n'
    string += '+ '+(empty_length-2)*' '+str(small)+'\n'
    string += '-'*(len(str(big))+2)+'\n'
    lib = list(str(big))[::-1]
    lis = list(str(small))[::-1]
    next_ = 0
    for i in range(len(lib)):
        try:
            ans = int(lib[i])+int(lis[i])+next_
        except:
            ans = int(lib[i])+next_
        if ans > 9:
            ans -= 10
            next_ = 1
        else:
            next_ = 0
        stringlist.append(ans)
    if next_ == 1:
        stringlist.append(1)
    for i in range(len(stringlist)):
        stringlist[i] = str(stringlist[i])
    stringlist = ''.join(stringlist[::-1])
    if len(stringlist) > len(str(big)):
        stringlist = ' '+stringlist
    else:
        stringlist = '  '+stringlist
    string += stringlist
    return string
print(vertical_type_calc(int(input('输入加数1:')),int(input('输入加数2:'))))