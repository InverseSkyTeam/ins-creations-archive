# 小轩版权所有
import hashlib

def ASCII(t,ti,ttype):
    text = ''
    for i in list(t):
        try:
            text += eval('chr(ord(i)'+ttype+'int(ti))')
        except:
            return '文中出现无法加密的新组合型繁体字'
    return text

def sha2(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()