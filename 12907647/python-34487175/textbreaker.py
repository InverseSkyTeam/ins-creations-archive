def add_ASCLL(t,ti,ttype):
    text = ''
    for i in list(t):
        try:
            text += eval('chr(ord(i)'+ttype+'int(ti))')
        except:
            return '文中出现无法加密的新组合型繁体字'
    return text

def add_ASCLL_number(t,ti,ttype):
    text = ''
    if ttype == '+':
        for i in list(t):
            try:
                text += str(oct(eval('ord(i)+int(ti)')))[2:] + ' '
            except:
                return '文中出现无法加密的新组合型繁体字'
    else:
        for i in t.split(' ')[:-1]:
            text += chr(eval('0o'+i)-int(ti))
    return text

def add_INS_ec79(t,ti,ttype):    # INS-jhx font encode-79 of ASCLL add password
    if ttype == '+':
        text = add_ASCLL_number(t,ti,'+').replace(' ','8')
        text = int(text)
    else:
        text = str(t).replace('8',' ')
        text = add_ASCLL_number(text,ti,'-')
    return text