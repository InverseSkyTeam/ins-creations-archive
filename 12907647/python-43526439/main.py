from flask import Flask,render_template,request,redirect,session
app = Flask(__name__)

member_info = [
    {'name': '逆天小轩',
     'job': '团长兼室长',
     'introduce': '''INS逆天团队创始人及团长。会编程，对python中tkinter和pygame的造诣高深。
会进行GUI制作。还会scratch和c/c++，前端会html,js,css，操作系统会cmd,vbs,bat，对信息学有一定了解。
进行过一些数学研究，喜欢编程、科学。喜欢看科幻小说。''',
     'link': 'https://code.xueersi.com/space/12907647',
    },
    {'name': '吴宇航',
     'job': '副室长',
     'introduce': '''对编程的认知和学习较广泛，且有一定深度，会做各种程序。能很好地使用爬虫。
对科学和计算机有研究。广泛涉猎语数外、哲学、历史、物理等领域。''',
     'link': 'https://code.xueersi.com/space/17025146',
    },
    {'name': '胡锦辉',
     'job': '副室长',
     'introduce': '''主要涉猎于pygame开发。会c++的一些算法。学习优秀，喜欢物理。
文采也很好，是一个B站UP主，也非常会剪辑。为人比较友善。''',
     'link': 'https://code.xueersi.com/space/2739759',
    },
]
member_num = len(member_info)
member_checknum = 0

@app.route('/')
def main():
    return redirect('/index')
    
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/member")
def member():
    global member_checknum
    member = member_info[member_checknum].copy()
    return render_template('member.html',
                           name=member['name'],
                           uid=member_checknum+1,
                           job=member['job'],
                           introduce=member['introduce'],
                           link=member['link'],
           )

@app.route("/memberlast")
def memberlast():
    global member_checknum, member_num
    member_checknum -= 1
    if member_checknum == -1:
        member_checknum = member_num - 1
    return redirect('/member')

@app.route("/membernext")
def membernext():
    global member_checknum, member_num
    member_checknum += 1
    if member_checknum == member_num:
        member_checknum = 0
    return redirect('/member')

if __name__ == '__main__':
    app.run()