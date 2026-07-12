def xint(a):
    try:
        return(int(a))
    except:
        return(None)
operator=["+","-","*","/","%","==","!=",">","<",">=","<="]
def hz_js(ml):
    ml=ml.split(".")
    stack=[]
    for i in ml:
        if xint(i)!=None:
            stack.append(xint(i))
        else:
            if i not in operator:
                return(None)
            if len(stack)<2:
                return(None)
            a=stack[-2]
            b=stack[-1]
            stack=stack[0:-2]
            stack.append(eval(str(a)+i+str(b)))
            if stack[-1]==True:
                stack[-1]=1
            if stack[-1]==False:
                stack[-1]=0
    if len(stack)==1:
        return(stack[0])
    return(None)
print(hz_js(input("请输入一个后缀表达式（形如1.2.+.1.-）：")))