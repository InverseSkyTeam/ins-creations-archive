#-*- coding: UTF-8 -*-
import curses
import curses.textpad
import locale
locale.setlocale(locale.LC_ALL, '')
from curses import textpad
import time



class notepad:
    def __init__(self, stdscr, topleft, bottomright, starttext = ""):
        self.topleft = topleft
        self.bottomright = bottomright
        self.stdscr = stdscr
        self.text = starttext
        self.curspos = 0

    def box(self):
        curses.textpad.rectangle(self.stdscr, self.topleft[0], self.topleft[1], self.bottomright[0], self.bottomright[1])

    def get_input(self, key):

        if not key == -1:

            if key == curses.KEY_LEFT:
                self.curspos -= 1

            elif key == curses.KEY_RIGHT:
                if self.curspos < len(self.text):
                    self.curspos += 1

            elif key == curses.KEY_UP:
                self.curspos -= self.width

            elif key == curses.KEY_DOWN:
                if self.curspos//self.width < len(self.text)//self.width:
                    self.curspos += self.width - (self.curspos%self.width - len(self.text)%self.width)

            elif key == curses.KEY_BACKSPACE:
                self.text = self.text[:self.curspos][:-1] + self.text[self.curspos:]
                self.curspos -= 1

            elif key == curses.KEY_ENTER or key == 10 or key == 13:
                self.text = self.text[:self.curspos] + " "*(self.width - (len(self.text[:self.curspos])%self.width)) + self.text[self.curspos:]
                self.curspos += 1
                self.curspos += self.width - (self.curspos%self.width - len(self.text)%self.width)

            else:
                self.text = self.text[:self.curspos] + chr(key) + self.text[self.curspos:]
                self.curspos += 1

    def display(self):
        self.width = (self.bottomright[1]-1) - (self.topleft[1]+1)

        if self.curspos < 0:
            self.curspos = 0

        for i in range(len(self.text)):
            self.stdscr.addstr( self.topleft[0]+1 + (i//self.width) , 
                                self.topleft[1]+1 +i%self.width  , 
                                self.text[i]
                                )
        if self.curspos < len(self.text):
            self.stdscr.addstr(self.topleft[0]+1 + (self.curspos//self.width) , self.topleft[1]+1 + self.curspos%self.width, self.text[self.curspos], curses.A_REVERSE)
        else:
            self.stdscr.addstr(self.topleft[0]+1 + (self.curspos//self.width) , self.topleft[1]+1 + self.curspos%self.width, " ", curses.A_REVERSE)

            
def main():
    run = True
    stdscr = curses.initscr()
    stdscr.nodelay(True)
    stdscr.keypad(True)
    curses.curs_set(False)
    curses.start_color()
    curses.noecho()
    curses.cbreak()

    notepad1 = notepad(stdscr, [0,0], [stdscr.getmaxyx()[0]-2,stdscr.getmaxyx()[1]-2])

    try:
        while run:
            start = time.time()

            stdscr.erase()

            key = stdscr.getch()

            notepad1.box()
            notepad1.get_input(key)
            notepad1.display()

            stdscr.refresh()


            time.sleep(max(0.05 - (time.time() - start), 0))
    finally:
        curses.echo()
        curses.nocbreak()
        curses.curs_set(True)
        stdscr.keypad(False)
        stdscr.nodelay(False)
        curses.endwin()
if __name__ == "__main__":
    print("这是一个简单的文本编辑器。只能保证能打字，能回显，修复了enter键的bug。由于C站打印输出问题，请自行本地运行。第三方Windows版curses库：https://www.lfd.uci.edu/~gohlke/pythonlibs/#curses")
    # main()   
