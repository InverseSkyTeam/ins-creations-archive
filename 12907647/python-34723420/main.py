def vertical_type_calc(n1,n2,tp='*'):
    string = ''
    if n1 > n2:
        big = n1
        small = n2
    else:
        big = n2
        small = n1
    zero = 0
    while str(big)[-1] == '0':
        big = int(str(big)[:-1])
        zero += 1
    while str(small)[-1] == '0':
        small = int(str(small)[:-1])
        zero += 1
    all_length = len(str(big))*2
    small_empty = (all_length-len(str(small))-1)*' '
    string += int(all_length/2)*' '+str(big)+'\n'
    string += '×'+small_empty+str(small)+'\n'
    string += '—'*all_length+'\n'
    x = -1
    for i in str(small)[::-1]:
        x += 1
        next_result = str(int(i)*big)
        if next_result != '0':
            string += (all_length-len(next_result)-x)*' '+next_result+'\n'
    string += '—'*all_length+'\n'
    total = str(big*small)
    string += (all_length-len(total))*' '+total+'\n'
    if zero != 0:
        string += total+'×10^'+str(zero)+'='+str(int(total)*10**zero)
    return string

print(vertical_type_calc(int(input('输入乘数1:')),int(input('输入乘数2:'))))