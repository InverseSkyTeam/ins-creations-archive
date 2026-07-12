import sys
import tty
import termios
import os
def getchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
def readkey():
    c1 = getchar()
    if ord(c1) != 0x1b:
        return c1
    c2 = getchar()
    if ord(c2) != 0x5b:
        return c2
    c3 = getchar()
    return chr(0x10 + ord(c3) - 65)
text = ""
while True:
    key=readkey()
    if key:
        os.system("clear")
        num = ord(key)
        if num == 127:
            text = text[:-1]
        elif num == 13:
            text = text + "\n"
        else:
            text += key
        print(text)