import os
import sys
import ctypes
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
def gotoxy(x,y):
    print(f"\033[{x};{y}f",end="")
def getch():
    import msvcrt
    a=msvcrt.getch()
    #print(bytearray(a)[0])
    #sleep(1)
    return chr(bytearray(a)[0])
def choose(choices:list,msg=""):
    begin=0
    now=0
    while 1:
        if now<begin:
            begin=now
        if now>begin+14:
            begin=now-14
        print(msg,end="\n" if msg else "")
        for i in range(begin,min(begin+15,len(choices))):
            if i==now:
                print("\033[1;44m",flush=True,end="")
            print(str(choices[i])+"\033[1;0m")
        ch=getch()
        if ch=='\r':
            break
        if ch=='w':
            now-=1
        if ch=='s':
            now+=1
        if ch=='e':
            return
        now+=len(choices)
        now%=len(choices)
        os.system("cls")
    return choices[now]
def choose_file(dir):
    if dir==None:
        return
    os.system("cls")
    f=choose(list(map(lambda a:a+"\\" if "." not in a or a[0]=='.' else a,os.listdir(dir))),"当前文件夹： "+dir)
    if f==None:
        return
    if '.' in f and f[0]!='.':
        return dir+f
    f=choose_file(dir+f)
    if f==None:
        return choose_file(dir)
    return f
file=None
while file==None:
    os.system("cls")
    file=choose_file(choose(["C:\\","D:\\","E:\\","F:\\"],"此电脑"))
os.system("cls")
print("你的选择：",file)
print("内容：\n"+"".join(open(file,"r",encoding="utf-8").readlines()))