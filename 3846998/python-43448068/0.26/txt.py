def run(save):
    print("无法运行.txt文件！")
def render(code:str,theme:dict):
    res=list(code)
    rr=[]
    tmp=[]
    for i in res:
        if "\n" in i:
            rr.append(tmp)
            tmp=[]
        else:
            tmp.append(i)
    return rr+[tmp]