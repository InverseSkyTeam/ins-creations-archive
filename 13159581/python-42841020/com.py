from easygui import *
import c
import d
import e

def main():
    a = buttonbox(choices=("C盘","D盘","E盘"))
    if a == "C盘":
        c.main()
    if a == "D盘":
        d.main()
    if a == "E盘":
        e.main()
main()

