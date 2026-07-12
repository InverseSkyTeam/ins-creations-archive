# ============随堂练习要求==========================================
#作答区域 第一：补充第23行代码，从pickle文件中读取数据；
#作答区域 第二：补充第45行代码，将数据存储到pickle文件中；
# =====================================================
from flask import Flask,render_template,request,redirect,session
from getnews import get_news
from savefile import save_path

# 引入pickle 模块
import pickle
app = Flask(__name__)

app.config['SECRET_KEY']='**##$$..tuiio23'


with open("works.pickle","rb") as f:
    works = pickle.load(f)

#作答区域===================补充第23行代码======================================
#作答区域 使用pickle模块中的load函数来读取messages.pickle文件中的数据，并赋值给变量messages
#作答区域 注意：load函数中有一个参数，是打开的文档（也就是变量f）
with open("messages.pickle",'rb') as f:
    messages = pickle.load(f)

@app.route('/')
def index():
    hot_news = get_news()
    return render_template("index.html", news = hot_news,works = works)

# ====呈现和处理的留言的路由和函数===========================================
@app.route("/messageboard")
def message_board():
    name = request.values.get("who")
    text = request.values.get("text")
    
    if name and text:
        message = {"name":name,"text":text}
        messages.append(message)
#作答区域 ==补充第45行代码,使用pickle的dump函数完成messages变量的永久性存储=====
#作答区域 ==注意：dump函数有两个参数:
#作答区域 ========第一个是传入的数据（变量messages)===========================
#作答区域 ========第二个是打开的文档(也就是变量f)==============================

        with open("messages.pickle",'wb') as f:
            pickle.dump(messages,f)
# =====================================================
    return render_template("messageboard.html",messages = messages)


@app.route("/permissionset")
def permission_set():
    return render_template('permissionset.html')


@app.route("/processpermission",methods=["POST"])
def process_permission():
    username = request.values.get("username")
    password = request.values.get("pwd")
    if username=="admin" and password=="123456":
        session["username"]="admin"
    return redirect("/")

@app.route("/delete") 
def del_work():
    work_title = request.values.get("worktitle")
    for work in works:
        if work["title"] == work_title:
            works.remove(work)
    with open("works.pickle","wb") as f:
        pickle.dump(works,f)
    return redirect("/")
   
@app.route('/privatepic')
def private():
    who = request.values.get("who")
    animal = request.values.get("animal")
    food = request.values.get("food")
    if who == "快乐星球" and animal == "狗" and food == "汉堡包":
        img_list = ["兔子.jpg", "小丸子.png", "小熊.jpg"]
        return render_template("privatepic.html",pictures = img_list)
    return render_template("privatepic.html")

@app.route("/uploadwork")
def upload_work():
    return render_template("uploadwork.html")


@app.route("/processwork",methods=["POST"])
def process_work():
    title = request.values.get("title")
    link = request.values.get("link")
    file = request.files.get("file")
    if title and link and file:
        fname = file.filename
        fpath = save_path(fname)
        file.save(fpath)
        
        new_work = {"title":title,"link":link,"file":fname}
        works.append(new_work)
        with open("works.pickle","wb") as f:
            pickle.dump(works,f)
        return redirect("/")
        
    else:
        return render_template("uploadwork.html")

app.run(debug="True")