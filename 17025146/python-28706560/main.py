import json
global file
file = {
    "C:":{
        "Users":{
            "Admin":{
                "Desktop":{"welcome.txt":"welcome!"},
                "Pictures":{},
                "Videos":{},
                "Musics":{},
                "Downloads":{},
                "Documents":{}
            }
        },
        "System":{}
    },
    "D:":{} 
} #初始化电脑磁盘
nowfile = "C:/Users/Admin"
nonamelist = ["/","\\","*",":","<",">","|","?","'","\""]

def use(usefile,files = None):
    global file
    if usefile[0:2] == "C:" or usefile[0:2] == "D:":#如果为绝对路径
        flist = usefile.split("/")
        a = file
        for i in flist:
            a = a[i]
        return a
    else: #如果为相对路径
        flist0 = files.split("/")
        x = file
        for w in flist0:
            x = x[w]
        flist = usefile.split("/")
        a = x
        for i in flist:
            a = a[i]
        return a

def istrue(filenm,nfile = None):
    global file
    if filenm[0:2] == "C:" or filenm[0:2] == "D:":
        flist1 = filenm.split("/")
        x = file
        for i in flist1:
            if i in x:
                x = x[i]
            else:
                return i
        return True
    else:
        flist0 = nfile.split("/")
        x = file
        for w in flist0:
            x = x[w]
        flist1 = filenm.split("/")
        for i in flist1:
            if i in x:
                x = x[i]
            else:
                return i
        return True
    
def fileor(filenm,nfile = None):
    global file
    if filenm[0:2] == "C:" or filenm[0:2] == "D:":
        flist1 = filenm.split("/")
        x = file
        for i in flist1:
            x = x[i]
        if type(x) == type({}):
            return True
        else:
            return False
        
    else:
        flist0 = nfile.split("/")
        x = file
        for w in flist0:
            x = x[w]
        flist1 = filenm.split("/")
        for i in flist1:
            x = x[i]
        if type(x) == type({}):
            return True
        else:
            return False
        
def addfile(filenm,nfile = None):
    global file
    f1 = filenm.split("/")[-1]
    for i in nonamelist:
        if i in f1:
            return False
    if filenm[0:2] == "C:" or filenm[0:2] == "D:":
        flist1 = filenm.split("/")
        x = file
        for i in flist1[0:-1]:
            x = x[i]
        x[flist1[-1]] = ""
        return True
        
    else:
        flist0 = nfile.split("/")
        x = file
        for w in flist0:
            x = x[w]
        flist1 = filenm.split("/")
        if len(flist1) == 1:
            x[flist1[0]] = ""
        elif len(flist1) > 1 :
            for i in flist1[0:-1]:
                x = x[i]
            x[flist1[-1]] = ""
            return True
            
def revices(filenm,reviced,nfile = None):
    global file
    if filenm[0:2] == "C:" or filenm[0:2] == "D:":
        flist1 = filenm.split("/")
        x = file
        for i in flist1[0:-1]:
            x = x[i]
        x[flist1[-1]] = reviced
        
    else:
        flist0 = nfile.split("/")
        x = file
        for w in flist0:
            x = x[w]
        flist1 = filenm.split("/")
        if len(flist1) == 1:
            x[flist1[0]] = reviced
        elif len(flist1) > 1 :
            for i in flist1[0:-1]:
                x = x[i]
            x[flist1[-1]] = reviced
            
def delfile(filenm,nfile):
    global file
    if filenm[0:2] == "C:" or filenm[0:2] == "D:":#如果为绝对路径
        flist = filenm.split("/")
        a = "file"
        for i in flist:
            a = a + "['" + i + "']"
        exec("del " + a)
    else: #如果为相对路径
        flist0 = nfile.split("/")
        x = "file"
        for w in flist0:
            x = x + "['" + w + "']"
        flist = filenm.split("/")
        a = x
        for i in flist:
            a = a + "['" + i + "']"
        exec("del " + a)
    

while True:
    command = input(nowfile+">")
    if command[0:6] == "check ":
        if istrue(command[6:len(command)],nowfile) == True:
            if fileor(command[6:len(command)],nowfile) == False:
                print(use(command[6:len(command)],nowfile))
            else:
                print("路径'" + command[6:len(command)] + "'不是一个可查看文件！")
        else:
            print("路径或文件'" + command[6:len(command)] + "'不存在!")
                
    elif command[0:7] == "revice ":
        if istrue(command[7:len(command)],nowfile) == True:
            if fileor(command[7:len(command)],nowfile) == False:
                itext = ""
                print("输入要修改的内容，键入%end%退出。")
                while True:
                    ints = input("")
                    if ints == "%end%":
                        break
                    else:
                        itext = itext + "\n" + ints
                revices(command[7:len(command)],itext[1:len(itext)],nowfile)
                    
            else:
                print("路径'" + command[7:len(command)] + "'不是一个可修改文件！")
        else:
            print("路径'" + istrue(command[3:len(command)]) + "'不存在!")
    elif command[0:4] == "add ":
        x = addfile(command[4:len(command)],nowfile)
        if x == False:
            print(f"文件名不能包含{''.join(nonamelist)}")
    elif command[0:3] == "cd ":
        if istrue(command[3:len(command)],nowfile) == True:
            if fileor(command[3:len(command)],nowfile) == True:
                if command[3:len(command)][0:2] == "C:" or command[3:len(command)][0:2] == "D:":
                    nowfile = command[3:len(command)]
                else:
                    nowfile = nowfile + "/" + command[3:len(command)]
            else:
                print("路径'" + command[3:len(command)] + "'不是一个文件夹！")
        else:
            print("路径'" + istrue(command[3:len(command)]) + "'不存在!")
    elif command[0:5] == "clear":
        print("\033[2J")
        print("\033[9999A")
    elif command[0:4] == "run ":
        if istrue(command[4:len(command)],nowfile) == True:
            if fileor(command[4:len(command)],nowfile) == False:
                if command[4:len(command)].split(".")[-1] == "py":
                    exec(use(command[4:len(command)],nowfile))
                else:
                    print("只能运行Python文件！")
            else:
                print("路径'" + command[4:len(command)] + "'不是一个可运行文件！")
        else:
            print("路径或文件'" + command[4:len(command)] + "'不存在!")
    elif command[0:4] == "del ":
        delfile(command[4:len(command)],nowfile)
    elif command[0:7] == "rename ":
        if istrue(command[7:len(command)],nowfile) == True:
            xxx = use(command[7:len(command)],nowfile)
            delfile(command[7:len(command)],nowfile)
            if len(command[7:len(command)].split("/")) > 1:
                y = input("请输入你想修改的文件名:")
                refile = "/".join(command[7:len(command)].split("/")[0:-1]) + "/" + y
                addfile(refile,nowfile)
                revices(refile,xxx,nowfile)
            else:
                y = input("请输入你想修改的文件名:")
                refile = nowfile + "/" + y
                addfile(refile,nowfile)
                revices(refile,xxx,nowfile)
        else:
            print("路径'" + istrue(command[3:len(command)]) + "'不存在!")
    elif command[0:4] == "dir ":
        if istrue(command[4:len(command)],nowfile) == True:
            if fileor(command[4:len(command)],nowfile) == True:
                for f in use(command[4:len(command)],nowfile):
                    print(f)
            else:
                print("路径'" + command[4:len(command)] + "'不是一个文件夹！")
        else:
            print("路径或文件'" + command[4:len(command)] + "'不存在!")    
    print()