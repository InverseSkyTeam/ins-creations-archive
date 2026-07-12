from turtle import *
from random import randint
from tkinter import *
s = int(input('输入运行速度(从慢到快1-10,输入0则极限快)'))
class Disc(Turtle):
    def __init__(self, n, c, f):
        Turtle.__init__(self, shape="square", visible=False)
        self.c = c
        self.pu()
        self.speed(s)
        self.shapesize(1.5, n*1.5, 2) # square-->rectangle
        self.fillcolor(n/f, self.c, 1-n/f)
        self.st()

class Tower(list):
    "Hanoi tower, a subclass of built-in type list"
    def __init__(self, x):
        "create an empty tower. x is x-position of peg"
        self.x = x
    def push(self, d):
        d.setx(self.x)
        d.sety(-150+34*len(self))
        self.append(d)
    def pop(self):
        d = list.pop(self)
        d.sety(150)
        return d

def hanoi(n, from_, with_, to_):
    if n > 0:
        hanoi(n-1, from_, to_, with_)
        to_.push(from_.pop())
        hanoi(n-1, with_, from_, to_)

def play():
    onkey(None,"space")
    clear()
    try:
        hanoi(11, t1, t2, t3)
        done()
    except Terminator:
        pass  # turtledemo user pressed STOP

def main(f, c):
    global t1, t2, t3
    ht(); penup(); goto(0, -225)   # writer turtle
    t1 = Tower(-300)
    t2 = Tower(0)
    t3 = Tower(300)
    for i in range(f,0,-1):
        t1.push(Disc(i, c, f))
    # prepare spartanic user interface
    write("按空格键开始",
          align="center", font=("宋体", 16, "bold"))
    onkey(play, "space")
    listen()
    return "PROGRAM RUNNING...."

def ask():
    t = Tk()
    t.title("汉诺塔自定义设置")
    t.geometry("410x200")
    
    l1 = Label(t, text="层数？(请输入2~11任意一整数)", font=("宋体", 12))
    l1.grid(row=0, column=0, columnspan=2)
    
    e1 = Entry(t, font=("Consolas", 12), bd=5)
    e1.grid(row=1, column=0, columnspan=2)
    
    l2 = Label(t, text="请输入个性化颜色值（0~1000任意一整数）（非必填）", font=("宋体", 12))
    l2.grid(row=3, column=0, columnspan=2)
    
    e2 = Entry(t, font=("Consolas", 12), bd=5)
    e2.grid(row=4, column=0, columnspan=2)
    
    b = Button(t, text="我选好了", font=("黑体", 15), bg="gray", command=t.quit)
    b.grid(row=6, column=0, columnspan=2)
    
    t.mainloop()
    
    floor = e1.get()
    while not floor.isdigit() or int(floor) < 2 or int(floor) > 11:
        error = Label(t, text="输入有误！", fg="red", font=("宋体", 9))
        error.grid(row=6, column=1, columnspan=10)
        t.mainloop()
        floor = e1.get()
    floor = int(floor)
    
    col = e2.get()
    if col:
        while not col.isdigit() or int(col) < 0 or int(col) > 1000:
            error = Label(t, text="输入有误！", fg="red", font=("宋体", 9))
            error.grid(row=6, column=1, columnspan=10)
            t.mainloop()
            col = e2.get()
        col = int(col)/1000
    
    try:
        t.quit()
        t.destroy()
    except:
        pass
    return [floor, col]
if __name__=="__main__":
    result = ask()
    f = result[0]
    if result[1]:
        c = result[1]
    else:
        c = randint(0,1000)/1000
    msg = main(f, c)
    mainloop()