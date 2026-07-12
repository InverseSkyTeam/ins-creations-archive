# 片头
import jhxGUI as jhx
import random
import data
jhx.start()
jhx.set(500,300,700,300,title='答题系统',bg='cyan')
subject = 1
jx = jhx.GUIX
root = jhx.root
db = data.database
question = random.randint(1,len(db)-1)
for i in db:
    if list(db).index(i) == question:
        question = i

def think():
    global db,question,subject
    choose = var.get()
    if choose == db[question][4]:
        exec('radio_button'+str(choose)+'["bg"] = "green"')
    else:
        exec('radio_button'+str(choose)+'["bg"] = "red"')
        exec('radio_button'+str(db[question][4])+'["bg"] = "green"')
    OKbutton['text'] = '继续，下一题'
    OKbutton['command'] = continue_
    subject += 1
def continue_():
    global db,question,radio_button1,radio_button2,radio_button3,radio_button4,OKbutton,ask,label
    del db[question]
    try:
        question = random.randint(0,len(db)-1)
    except:
        root.destroy()
    else:
        for i in db:
            if list(db).index(i) == question:
                question = i
        radio_button1['text'] = 'A.'+db[question][0]
        radio_button2['text'] = 'B.'+db[question][1]
        radio_button3['text'] = 'C.'+db[question][2]
        radio_button4['text'] = 'D.'+db[question][3]
        radio_button1['bg'] = 'cyan'
        radio_button2['bg'] = 'cyan'
        radio_button3['bg'] = 'cyan'
        radio_button4['bg'] = 'cyan'
        label['text'] = '第'+str(subject)+'题'
        ask['text'] = question
        OKbutton['text'] = 'OK'
        OKbutton['command'] = think
    finally:
        if subject == 9:
            root.destroy()

# jhx
nonelabel = jhx.add_text('');nonelabel['bg'] = 'cyan'
label = jhx.add_text('第'+str(subject)+'题');label['bg'] = 'cyan'
ask = jhx.add_text(question);ask['bg'] = 'cyan'

# tk
var = jx.IntVar()
radio_button1 = jx.Radiobutton(root,text='A.'+db[question][0],variable=var,value=1,bg='cyan')
radio_button2 = jx.Radiobutton(root,text='B.'+db[question][1],variable=var,value=2,bg='cyan')
radio_button3 = jx.Radiobutton(root,text='C.'+db[question][2],variable=var,value=3,bg='cyan')
radio_button4 = jx.Radiobutton(root,text='D.'+db[question][3],variable=var,value=4,bg='cyan')
radio_button1.pack();radio_button2.pack();radio_button3.pack();radio_button4.pack()
OKbutton = jx.Button(root,text='OK',command=think,bg='green')
OKbutton.pack()

# main
jhx.main()