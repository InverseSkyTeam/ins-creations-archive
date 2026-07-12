from teacher import *

# 可以手动加载背景音乐,也可以自己上传背景音乐，背景音乐会循环播放。
# 如果不使用music("音乐名称")，则没有背景音乐
music("听我说谢谢你手势.mp4")

# 1、text("要显示的文字")可以显示不同的文字
#
# 2、img("图片名称")图片可以使用左侧素材栏当中的，也可以自己上传图片
#
# 3、t(时间)表示停留的时间，单位是秒
#    setTime(时间)作用与t(时间)一致
#
# 4、addMusic("音乐名称",播放时间)表示能够在背景音乐的基础上，播放其它音乐一次。
#    这个方法可以多次使用。
#    例如：text("你好")
#          t(1)
#          addMusic("我给老师录的语音1.mp3")
#          text("我是")
#          t(1)
#          text("可多")
#          t(1)
#          addMusic("我给老师录的语音2.mp3")
#
# 5、show() 显示最终效果
# 注意：（1）使用text()或者img()后面，都要加上停留时间
#       （2）全部写完后，在最后一行写上show()，
#            show()只需要在最后一行使用一次

text("这是我的老师罗老师")
setTime(2)
img("d.jpg")
t(2)
#addMusic("欢呼.mp3")
text("谢谢您的陪伴")
t(2)
text("我的一生")
t(2)
text("您陪我六年")
t(2)
text("但这六年")
t(2)
text("影响我一生")
t(2)
text("我")
t(2)
text("想要送您")
t(2)
addMusic("鼓掌.mp3")
text("一束鲜花")
t(2)
img("c.jpg")
t(2)
text("您")
t(2)
img("d.jpg")
t(2)
text("永远是")
t(2)
text("永远是")
t(2)
text("永远是")
t(2)
text("我心中")
t(2)
text("最")
t(2)
text("最")
t(2)
text("最")
t(2)
text("最可敬的人！！！")
t(2)
img("d.jpg")
t(2)

text("我")
t(2)
text("不会忘记")
t(2)
text("您的辛勤付出")
t(2)
img("d.jpg")
t(2)

text("您")
t(2)
img("d.jpg")
t(2)
text("永远是")
t(2)
text("永远是")
t(2)
text("永远是")
t(2)
text("我心中")
t(2)
text("最喜欢的老师！！！")
t(3)
text("祝您教师节快乐")
show()