from robot import *
question = "tart的中文是？"
a = "蛋挞"
b = "蛋糕"
c = "地图"
def click(answer):
    if answer == a:
        say("答对啦！")
    if answer == b:
        say("再想一想吧！")
    if answer == c:
        say("呜呜-o-答错了-o-")
def btnclick(x,y):
    say = btn1(x,y,a,b,c)
    click(say)
write(question)
draw_button_list(a,b,c)
screen.onscreenclick(btnclick,1)
screen.listen()
screen.mainloop()