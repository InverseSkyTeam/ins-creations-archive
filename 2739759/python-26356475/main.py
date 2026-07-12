import turtle
import time
turtle.setup(800,600)
t = turtle.Pen()
t.shape('turtle')
t.color('red')
t.pensize(5)
t.speed(0)  # 加快小乌龟绘画速度
t.up()
t.backward(300)
t.down()


def drawgap():  # 想把显示的数字更加美观一点，想添加空格
    t.up()
    t.fd(5)


def drawline(flag):
    drawgap()  # 在开始落笔前就开始插入空格
    if flag:
        t.down()
    else:
        t.up()
    t.fd(40)
    drawgap()  # 同理前进后也要间隔
    t.right(90)


def drawdigit(num):
    drawline(True) if num in [2, 3, 4, 5, 6, 8, 9] else drawline(False)
    drawline(True) if num in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawline(False)
    drawline(True) if num in [0, 2, 3, 5, 6, 8, 9] else drawline(False)
    drawline(True) if num in [0, 2, 6, 8] else drawline(False)
    t.left(90)
    drawline(True) if num in [0, 4, 5, 6, 8, 9] else drawline(False)
    drawline(True) if num in [0, 2, 3, 5, 6, 7, 8, 9] else drawline(False)
    drawline(True) if num in [0, 1, 2, 3, 4, 6, 8, 9] else drawline(False)
    t.up()  # 这三步小乌龟向前移动
    t.left(180)
    t.forward(20)


def drawdate(date):  # 为了方便区分，我们把日期格式设为%Y-%m=%d+,此时要利用到time.gmtime()以及time.strftime()
    t.color('red')
    for i in date:
        if i == "-":
            t.write('年', font=("Arial", 25, "normal"))
            t.color('blue')
            t.fd(40)
        elif i == "/":
            t.write('月', font=("Arial", 25, "normal"))
            t.color('black')
            t.fd(40)
        elif i == "+":
            t.write('日', font=("Arial", 25, "normal"))
        else:
            drawdigit(eval(i))

def programmer():
    t.up()
    t.goto(-280, 100)
    t.down()
    t.color('black')
    # t.write('广大程序员节日快乐，真牛皮！！！', font=("Arial", 25, "normal"))
    t.up()
    t.goto(0, 0)
    t.down()#将画笔返回原位

programmer()



def main():

    t.color('red')
    t.pensize(5)
    t.speed(0)  # 加快小乌龟绘画速度
    t.up()
    t.backward(300)
    t.down()

    drawdate(time.strftime("%Y-%m/%d+", time.gmtime()))
    t.hideturtle()

main()

turtle.done()
#实现完成