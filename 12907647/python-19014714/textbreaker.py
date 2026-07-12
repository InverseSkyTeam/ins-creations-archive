def add_ASCLL(t,ti,ttype):
    text = ''
    for i in list(t.replace('#**&%:x66|of_SPACE_;;',' ')):
        if i != ' ':
            try:
                text += eval('chr(ord(i)'+ttype+'int(ti))')
            except:
                return '文中出现无法加密的新组合型繁体字'
        else:
            text += '#**&%:x66|of_SPACE_;;'
    if ttype == '-':
        text = text.replace('#**&%:x66|of_SPACE_;;',' ')
    return text

def add_INS_ec04(t,ti):    # INS-jhx font encode-04 of ASCLL add password
    text = ''
    for i in list(t):
        if i != ' ':
            try:
                text += str(oct(ord(i)+int(ti)))[2:] + ' '
            except:
                return '文中出现无法加密的新组合型繁体字'
        else:
            text += '100000000 '
    text = text.replace('0','#$') \
        .replace('1','%^') \
        .replace('2','|&') \
        .replace('3','!@$') \
        .replace('4','f-') \
        .replace('5','^&&') \
        .replace('6','~?!') \
        .replace('7','(*}') \
        .replace(' ','!?$%#&;;') \
        .replace('^!','^&*(#$%^') \
        .replace('$% ','(%[*-^') \
        .replace('-~','%#&;;') \
        .replace('^^','**^^((==') \
        .replace('^(','t&u%3v!?') \
        .replace('&f','I-NS|jh-x') \
        .replace('$|','fu%.x0;8') \
        .replace(';(','sah^%&') \
        .replace('-^','sah^%&!#@$!')
    text = text.replace('0','#$#').replace('1','%^%')
    return text

def readd_INS_ec04(t,ti):
    text = t.replace('%^%','1').replace('#$#','0')
    text = text.replace('sah^%&!#@$!','-^') \
        .replace('sah^%&',';(') \
        .replace('fu%.x0;8','$|') \
        .replace('I-NS|jh-x','&f') \
        .replace('t&u%3v!?','^(') \
        .replace('**^^((==','^^') \
        .replace('%#&;;','-~') \
        .replace('(%[*-^','$% ') \
        .replace('^&*(#$%^','^!') \
        .replace('!?$%#&;;',' ') \
        .replace('(*}','7') \
        .replace('~?!','6') \
        .replace('^&&','5') \
        .replace('f-','4') \
        .replace('!@$','3') \
        .replace('|&','2') \
        .replace('%^','1') \
        .replace('#$','0')
    text = text.replace('!?$-~',' ').split(' ')
    for i in range(len(text)):
        if text[i] == '100000000':
            text[i] = ' '
        else:
            try:
                text[i] = chr(eval('0o'+text[i])-int(ti))
            except:
                pass
    text = ''.join(text)
    return text