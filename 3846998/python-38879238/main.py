from os import system
import sys
def gotoxy(x,y):
    print(f"\033[{x};{y}f",end="")
def getch():#C站最流行的一种
    system("stty -icanon")
    system("stty -echo")
    res=sys.stdin.read(1)
    system("stty icanon")
    system("stty echo");
    return res
class Terminal:
    def __init__(self):
        self.buttons={"Exit":[(49,40),"Exit",lambda:exit(0)]}
        self.button_name=["Exit"]
        self.button_now="Exit"
    def make_button(self,name,x,y,text,do=lambda:0):
        self.buttons[name]=[(x,y),text,do]
        self.button_name.append(name)
    def show(self):
        system("clear")
        gotoxy(0,0)
        for k,v in self.buttons.items():
            if k==self.button_now:
                gotoxy(v[0][0],v[0][1])
                print("\033[1;46m"+v[1]+"\033[1;0m",flush=True,end="")
                print()
            else:
                gotoxy(v[0][0],v[0][1])
                print(v[1],flush=True,end="")
        gotoxy(0,0)
    def click(self):
        a=getch()
        if a=='\t':
            self.button_now=self.button_name[(self.button_name.index(self.button_now)+1)%len(self.button_name)]
        if a=="\n":
            self.buttons[self.button_now][2]()
def button1():
    system("clear")
    print("Hello!")
    getch()
a=Terminal()
a.make_button("button1",10,20,"click",button1)
while 1:
    a.show()
    a.click()
    system("clear")