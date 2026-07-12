def hws(a):
    b=' '+str(a)
    for i in range(1,len(b)//2):
        if b[i]!=b[-i]:
            return(False)
    return(True)
print(hws(input()))