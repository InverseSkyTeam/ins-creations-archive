import sys,os,main


def choose_file():
    while 1:
        choice = main.choose(["Exit","C:","D:","E:","F:"],1)
        if choice=="Exit":
            exit(0)
        file=_choose_file(choice)
        if file:
            return file


def _choose_file(dir):
    ...
