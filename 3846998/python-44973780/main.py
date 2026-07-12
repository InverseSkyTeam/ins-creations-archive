from typing import NamedTuple
import re
import sys
'''import ctypes
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)'''



def gotoxy(y: int, x: int):  # y: ln, x: col
    print(f"\033[{y};{x}f", end="", flush=True)


class Token(NamedTuple):
    tp: str
    color: str
    value: str
    ln: int
    col: int


def tokenize(code: str):
    keywords = [
        'if',
        'define',
        'lambda',
        'macro',
        'quote',
        'set!',
        'begin'
    ]
    syntax = {
        'COMMENT': r';[^\n]*',
        'NUM': r'\d+(\.\d*)?',
        'STRING': r'\"([^"\n\\]|(\\([rtafvbn\\\'\"]|[0-9][0-9][0-9])))*\"',
        'ID': r'[^0-9\s\'\(\),\"][^\s\(\)\";]*',
        'NEWLINE': r'\n',
        'SKIP': r'[ \t]+',
        'LPAREN': r'\(',
        'RPAREN': r'\)',
        'QUOTE': r"'",
        'NOQUOTE': r',',
        'OTHERS': r'.'
    }
    paren_color = [
        "\033[1;0m",
        "\033[1;31m",
        "\033[1;34m",
        "\033[1;35m",
        "\033[1;36m"
    ]
    regex = '|'.join('(?P<%s>%s)' % pair for pair in syntax.items())
    ln = 1
    ln_start = 0
    cnt = 0
    for mo in re.finditer(regex, code):
        tp = mo.lastgroup
        value = mo.group()
        col = mo.start() - ln_start
        if tp == "NUM":
            yield Token(tp, '\033[1;33m', value, ln, col)
        elif tp == 'ID' and value in keywords:
            yield Token(tp, '\033[1;35m', value, ln, col)
        elif tp == 'ID' or tp == 'OTHERS':
            yield Token(tp, '\033[1;0m', value, ln, col)
        elif tp in ('LPAREN', 'RPAREN', 'QUOTE', 'NOQUOTE'):
            if tp == 'RPAREN':
                cnt -= 1
            yield Token(tp, paren_color[cnt%len(paren_color)], value, ln, col)
            if tp == 'LPAREN':
                cnt += 1
        elif tp == 'STRING':
            yield Token(tp, '\033[0;32m', value, ln, col)
        elif tp == 'COMMENT':
            yield Token(tp, '\033[38;5;242m', value, ln, col)
        elif tp == 'NEWLINE':
            ln_start = mo.end()
            ln += 1
            continue
        elif tp == 'SKIP':
            continue


code = '''
; A program
(define fac (lambda (a)
    (if a
        (* (fac (- a 1)) a)
        1)))

(define add (lambda (a b)
    (print a " " b "\\n")
    (+ a b)))

(define MACRO-GREET (macro (name)
    '(print "Hello, " ,name "!\\n")))
'''
for token in tokenize(code):
    gotoxy(token.ln, token.col + 1)
    print(token.color, token.value, end="\033[1;0m", flush=True, sep="")
    # print(token)
print("\033[1;0m")
