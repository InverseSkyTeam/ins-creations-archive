from flask import *
import pickle
import random

app = Flask(__name__,static_folder='',static_url_path='')

try:      # 读取已登录用户
    with open("names.pickle","rb") as f:
        names = pickle.load(f)
        f.close()
except:
    names = {}

# 随机加密私钥
app.config['SECRET_KEY'] = '**##$$..tuiio23'+str(random.randint(0,9999))

@app.route("/")
def MA():
    return redirect("/login")

@app.route("/login")
def log():
    return render_template("登录.html")

@app.route("/tomain")
def tomain():
    return render_template("主页.html")

@app.route("/logout")
def lou():
    session.clear()
    return redirect("/login")    # 退出的时候重定向回去

@app.route("/pic",methods = ["POST"])
def pic():
    who = request.values.get("who")
    how = request.values.get("how")
    newhost_check = request.values.get("newhost")
    login_check = request.values.get("login")
    # 特殊对待--start--
    if (who == "尹鹏皓" and how == "091008") or (who == "方块人子墨" and how == "091008YPH") or (who == "lyl_coder_mcplayer" and how == "1234"):
        session["name"] = who
        return render_template("登录.html",lod=6)
    # 特殊对待--end--
    if len(who) > 15:
        return render_template("登录.html",lod=1)   # 名字长
    if len(how) < 6:
        return render_template("登录.html",lod=2)   # 密码短
    if newhost_check == 'nocheck':   # 已经注册过了
        return render_template("登录.html",lod=8)  # 不要再注册了！
    if newhost_check == 'checked':
        if who in names:
            return render_template("登录.html",lod=3)  # 用户已经存在
        else:
            names[who] = how
            with open("names.pickle","wb") as f:
                pickle.dump(names,f)
                f.close()
            session["name"] = who
            return render_template("登录.html",lod=6)  # 注册成功
    if login_check == 'checked':
        if who in names:
            if names[who] == how:
                session["name"] = who
                return render_template("登录.html",lod=7)  # 登录成功
            else:
                return render_template("登录.html",lod=5)  # 账号或密码错误
        else:
            return render_template("登录.html",lod=4)  # 用户不存在

app.run()     # 跑起来才有活力