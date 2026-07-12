'''
用c_print("里面写你想逐字输出的字")
'''
import time,sys

def replace(strname,*w):
    for x in w:
        strname=strname.replace(x[0],x[1])
    return strname

def c_print(*w,t=0.05,end="\n",sepr=" "):
    str_all=""
    
    for x in w:
        
        if w.index(x)==len(w)-1:
            str_all+=str(x)
        else:
            str_all+=str(x)+sepr
    str_all=replace(str_all,("\\红","\033[41m"),
                ("\\绿","\033[42m"),
                ("\\黄","\033[43m"),
                ("\\蓝","\033[44m"),
                ("\\紫","\033[45m"),
                ("\\青""\033[46m"),
                ("\\白","\033[47m"),
                ("\\黑","\033[40m"),
                ("\\","\033[0m"))
    
    for y in str_all:
        sys.stdout.write(y)
        sys.stdout.flush()
        time.sleep(t)
    sys.stdout.write(end)

if __name__ == 'main':
    c_print("陈锦奕最帅！")
    