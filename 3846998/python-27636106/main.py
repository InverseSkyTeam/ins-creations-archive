def getpair(st,pos):
    l=1
    r=0
    p=pos
    for i in st[pos+1:]:
        p+=1
        if i=="(":
            l+=1
        if i==")":
            r+=1
            if l>0:
                r-=1
                l-=1
        if l==0:
            return(p)
def js(st):
    c=" "
    #print("st=",st)
    for i in st:
        if i in "+-*/%":
            c=i
    st1,st2=st.split(c,1)
    st1=float(st1)
    st2=float(st2)
    if c=='+':
        return(st1+st2)
    if c=='-':
        return(st1-st2)
    if c=='*':
        return(st1*st2)
    if c=='/':
        return(st1/st2)
    if c=='%':
        return(st1%st2)
'''def expjs_j(exp):
    count=0
    op=[]
    for i in range(len(exp)):
        if exp[i] in "+-*/%":
            count+=1
            op.append(exp[i])
    if count==0:
        return(float(exp))
    '''
def expjs_j(exp):
    count=0
    pos=0
    for i in range(len(exp)):
        if exp[i] in "+-*/%":
            count+=1
        if count==2:
            pos=i
            break
    if count==1:
        if exp[0]=='-':
            return(float(exp))
        exp=exp.replace(exp,str(js(exp)))
        return(expjs_j(exp))
    if count==0:
        return(float(exp))
    exp=exp.replace(exp[0:pos],str(js(exp[0:pos])))
    return(expjs_j(exp))
print(expjs_j(input()))