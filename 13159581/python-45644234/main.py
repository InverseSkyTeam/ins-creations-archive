from flask import *
from getmusic import *
from getimg import *
from getmovie import *
app = Flask(__name__)

@app.route("/guanwang")
def guanwang():
    return render_template("guanwang.html",guanwang_list =  guanwang)

#"/movie"路由
@app.route("/movie")
def movie():
    movie = get_movie()
    return render_template("movie.html",movie_list =  movie )
    
#"/music"路由
@app.route("/music")
def music():
    music = get_music()
    return render_template("music.html",music_list=music)
    
#"/photo"路由
@app.route("/photo")
def photo():
    img = get_img()
    return render_template("photo.html",img_list=img)
    
#"/"路由
#{
@app.route('/')
def index():
    try:
        with open("dress.txt","r",encoding="UTF-8") as file:
            pic = file.read()
    except:
        pic = "/static/images/g25.gif"
    try:
        with open("music.txt","r",encoding="UTF-8") as file:
            music = file.read()
    except:
        music ="https://static0.xesimg.com/talcode/webprotect/孤勇者.mp3"
    return render_template("index.html",x = pic,music=music)
#}



#"/dress"路由
#{   
@app.route("/dress")
def dress():
    return render_template("dress.html")
#}

#"/set_music"路由
#{
@app.route("/set_music")
def set_music():
    global music
    index_music = request.values.get("music")
    with open("music.txt","w",encoding="UTF-8") as file:
        file.write(index_music)
    return redirect("/")
#}

#"/show_img"路由
#{
@app.route("/show_img")
def show_img():
    index_img = request.values.get("img")
    with open("dress.txt","w",encoding="UTF-8") as file:
        file.write(index_img)
    return redirect("/")
#}


app.run()