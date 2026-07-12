#-*-coding:utf8;-*-
def check(string):
    string=string.swapcase()
    import codecs
    f2 = codecs.open('./ce.txt','r','utf-8')
    up = f2.read()
    f2.close()
    up=eval(up)
    #print(up)
    res=[]
    for i in up.keys():
        if str(i).find(string)==0:
            #print(up[i])
            res.extend(up[i])
    #print(up.keys())
    return res
def fen(array):
    array1=[]
    arr=[]
    for i in array:
        try:
            i.encode('gb2312')
            array1.append(i)
        except:
            arr.append(i)
    array1.extend(arr)
    array=array1
    res=[]
    res1=[]
    for i in array:
        if len(res1)==3:
            res.append(res1)
            res1=[]
        res1.append(i)
    if res1!=[]:
        for i in range(3-len(res1)):
            res1.append('')
        res.append(res1)
    if res==[]:
        res.append(['','',''])
    return res