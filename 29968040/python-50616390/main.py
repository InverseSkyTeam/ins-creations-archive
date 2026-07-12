import text_break_iterator as text_break
string = '123-456abc def -345--678'
res = text_break.test(string)
for i in range(len(res)-1):
    print('\033[1;37;45m' + string[res[i]:res[i+1]])
print('\033[0m')
