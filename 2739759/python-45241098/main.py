print("""思考下列问题：

1.开头作者为什么要使用“tent-like thing”，而不换用更准确的“pavilion”？
2.体会歌词三处细微的变化“I've got”、"You had"和“I've had”，写出了女主人公怎样的心情变化？
3.作者描写曾经妇女和老人对男女主的感情变化有何作用？
4.结合全文，思考男女主是否最终在一起，并说明理由？
5.积累下列短语：
（1） pay for sth.  （2） skeleton in one's closet
（2）hang form    (4) hustling for
其他问题也欢迎讨论\n""")
n = input("\033[33m请选择：1.英文字幕版 2.中英字幕版")
import webbrowser as w
link = "https://livefile.xesimg.com/programme/python_assets/f9a3113bb5b857aa4d914eadded75343.mp4"
link2 = "https://livefile.xesimg.com/programme/python_assets/a7e19805aa701992f24636f0f00a322b.mp4"
if "1" in n or "一" in n or "yi" in n or "one" in n:
    w.open(link2)
else:
    w.open(link)