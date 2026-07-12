from time import *
from random import *

def sp(time=1):
    sleep(time)

def rd(life=(0,10),st=False):
    rdi = randint(life[0],life[1])
    if st == True:
        rdi = str(rdi)
    return rdi

def cpt(text,time=0.04):
    for i in text:
        print('\033[1;'+rd(life=(31,36),st=True)+'m'+i,end='')
        sp(time)
    print('\n')

def clear():
    print('\033[2J\033[100A\033[3J\033[100A')

def line_up(text=''):
    print('-'*50)
    input(text)
    clear()