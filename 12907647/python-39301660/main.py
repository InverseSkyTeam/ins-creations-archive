import keyword as k,time
kwdict = {}
for i in dir(__builtins__):
    if i[-5:] == 'Error':
        kwdict[i] = '#d22e1e'
    elif i[-7:] == 'Warning':
        kwdict[i] = '#d28f1e'
    else:
        kwdict[i] = '#dddddd'
for i in k.kwlist:
    kwdict[i] = '#1f1ed2'
kwdict['True'] = '#b061e5'
kwdict['False'] = '#b061e5'
kwdict['None'] = '#b061e5'
kwdict['...'] = '#b061e5'
kwdict['Ellipsis'] = '#b061e5'
kwdict['BaseException'] = '#f1d984'
kwdict['KeyboardInterrupt'] = '#f1d984'
kwdict['StopAsyncIteration'] = '#f1d984'
kwdict['StopIteration'] = '#f1d984'
kwdict['SystemExit'] = '#f1d984'
kwdict['GeneratorExit'] = '#f1d984'
kwdict['Exception'] = '#d22e1e'
kwdict['print'] = 'purple'
kwdict['input'] = 'purple'
kwdict['debugger'] = 'red'
kwdict['self'] = 'cyan'
kwdict['cls'] = 'cyan'
symbolshowlist = [
    '+','-','*','/','(',')','=',
    '[',']','{','}','|','\\',
    '!=','@','#','$','%','^','&','?',
    '\'','\"',
    ':',';','<','>',',','.',
    '~',
    ' ','','\n',
]
for i in symbolshowlist:
    kwdict[i] = '#cccccc'
del kwdict['"']
del kwdict["'"]
del kwdict[" "]
del kwdict[""]
del kwdict["\n"]

for i in kwdict:
    print(i,kwdict[i])