def xtype(a):
    try:
        int(a)
    except:
        return("string")
    else:
        return("int")
a=1
b=1
c=1
d=1
while 1:
    e=input().split()
    f=e[0]
    g=e[1]
    h=e[2]
    if g=="+=":
        if f=="a":
            if xtype(h)=="int":
                a=a+int(h)
            else:
                if h=="a":
                    a+=a
                elif h=='b':
                    a+=b
                elif h=='c':
                    a+=c
                elif h=="d":
                    a+=d
        elif f=="b":
            if xtype(h)=="int":
                i=int(h)
                b+=i
            else:
                if f=="a":
                    b+=a
                elif f=='b':
                    b+=b
                elif f=='c':
                    b+=c
                elif f=="d":
                    b+=d
        elif f=="c":
            if xtype(h)=="int":
                i=int(h)
                c+=i
            else:
                if h=="a":
                    c+=a
                elif h=='b':
                    c+=b
                elif h=='c':
                    c+=c
                elif h=="d":
                    c+=d
        elif f=="d":
            if xtype(h)=="int":
                i=int(h)
                d+=i
            else:
                if h=="a":
                    d+=a
                elif h=='b':
                    d+=b
                elif h=='c':
                    d+=c
                elif h=="d":
                    d+=d
    elif g=="-=":
        if f=='a':
            if xtype(h)=="int":
                a-=int(h)
            else:
                if h=="a":
                    a-=a
                elif h=='b':
                    a-=b
                elif h=='c':
                    a-=c
                elif h=="d":
                    a-=d
        elif f=="b":
            if xtype(h)=="int":
                i=int(h)
                b-=i
            else:
                if h=="a":
                    b-=a
                elif h=='b':
                    b-=b
                elif h=='c':
                    b-=c
                elif h=="d":
                    b-=d
        elif f=="c":
            if xtype(h)=="int":
                i=int(h)
                c-=i
            else:
                if h=="a":
                    c-=a
                elif h=='b':
                    c-=b
                elif h=='c':
                    c-=c
                elif h=="d":
                    c-=d
        elif f=="d":
            if xtype(h)=="int":
                i=int(h)
                d-=i
            else:
                if h=="a":
                    d-=a
                elif h=='b':
                    d-=b
                elif h=='c':
                    d-=c
                elif h=="d":
                    d-=d
    elif g=="/=":
        if f=="a":
            if xtype(h)=="int":
                a/=int(h)
            else:
                if h=="a":
                    a/=a
                elif h=='b':
                    a+=b
                elif h=='c':
                    a/=c
                elif h=="d":
                    a/=d
        elif f=="b":
            if xtype(h)=="int":
                i=int(h)
                b/=i
            else:
                if h=="a":
                    b/=a
                elif h=='b':
                    b/=b
                elif h=='c':
                    b/=c
                elif h=="d":
                    b/=d
        elif f=="c":
            if xtype(h)=="int":
                i=int(h)
                c/=i
            else:
                if h=="a":
                    c/=a
                elif h=='b':
                    c/=b
                elif h=='c':
                    c/=c
                elif h=="d":
                    c/=d
        elif f=="d":
            if xtype(h)=="int":
                i=int(h)
                d/=i
            else:
                if h=="a":
                    d/=a
                elif h=='b':
                    d/=b
                elif h=='c':
                    d/=c
                elif h=="d":
                    d/=d
    elif g=="*=":
        if f=="a":
            if xtype(h)=="int":
                a*=int(h)
            else:
                if h=="a":
                    a*=a
                elif h=='b':
                    a*=b
                elif h=='c':
                    a*=c
                elif h=="d":
                    a*=d
        elif f=="b":
            if xtype(h)=="int":
                i=int(h)
                b*=i
            else:
                if h=="a":
                    b+=a
                elif h=='b':
                    b+=b
                elif h=='c':
                    b+=c
                elif h=="d":
                    b+=d
        elif f=="c":
            if xtype(h)=="int":
                i=int(h)
                c*=i
            else:
                if h=="a":
                    c*=a
                elif h=='b':
                    c*=b
                elif h=='c':
                    c*=c
                elif h=="d":
                    c*=d
        elif f=="d":
            if xtype(h)=="int":
                i=int(h)
                d*=h
            else:
                if h=="a":
                    d*=a
                elif h=='b':
                    d*=b
                elif h=='c':
                    d*=c
                elif h=="d":
                    d*=d
    elif f=="print":
        if g=="%d":
            print(int(h))
        elif g=="%s":
            print(h)
        elif g=="&d":
            if h=="a":
                print(a)
            elif h=="b":
                print(b)
            elif h=="c":
                print(c)
            elif h=="d":
                print(d)
    elif f=="=":
        if xtype(h)=="int":
            if f=="a":
                a=int(h)
            elif f==b:
                b=int(h)
            elif f=="c":
                c=int(h)
            elif f=="d":
                d=int(h)
        else:
            if h=='a':
                if f=="a":
                    a=a
                elif f==b:
                    b=a
                elif f=="c":
                    c=a
                elif f=="d":
                    d=a
            elif h=="b":
                if f=="a":
                    a=b
                elif f==b:
                    b=b
                elif f=="c":
                    c=b
                elif f=="d":
                    d=b
            elif h=="c":
                if f=="a":
                    a=c
                elif f==b:
                    b=c
                elif f=="c":
                    c=c
                elif f=="d":
                    d=c
            elif h=="d":
                if f=="a":
                    a=d
                elif f==b:
                    b=d
                elif f=="c":
                    c=d
                elif f=="d":
                    d=d