try:
    import requests,bs4,random
    import easygui as g

    aaaaa = ["x","y","z","j","k"]
    #aaaaa = ["k"]
    def get_name():  # 随机网名生成器
        url = "https://www.qmsjmfb.com"
        res = requests.get(url)
        res.encoding = "UTF-8"
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        data = soup.find("div", class_="name_box container").find_all("li")
        g.msgbox(random.choice(data).text)
    def get_gossips():  # 爬八卦
        all = ""
        url = "https://static0.xesimg.com/pythonweb/编程八卦/index.html"
        res = requests.get(url)
        res.encoding = "UTF-8"
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        data = soup.find_all("a", class_="title")
        for n in data:
            all += n.text + "\n\n"
        g.msgbox(all)
    def days():  # 输入出生年月日，查看自己活了多少天
        import datetime
        year = int(g.enterbox("请输入出生年份(例如2010)："))
        month = int(g.enterbox("请输入出生月份(例如2)："))
        day = int(g.enterbox("请输入出生日期(例如9):"))
        
        birthday = datetime.datetime.strptime(f"{year}-{month}-{day}", '%Y-%m-%d')
        lived = datetime.datetime.now() - birthday
        g.msgbox(f"你一共活了 {lived.days} 天！")
    def get_news():  # 爬新闻
        all = ""
        url = "https://static0.xesimg.com/pythonweb/可多新闻/index.html"
        res = requests.get(url)
        res.encoding = "UTF-8"
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        data = soup.find_all("a", class_="title")
        for n in data:
            all += n.text + "\n\n"
        g.msgbox(all)
    def BMI_BFR():  # 身体指数BMI、体脂率BFR计算器
        height = float(g.enterbox("请输入身高(m)："))
        weight = float(g.enterbox("请输入体重(kg)："))
        age = int(g.enterbox("请输入年龄:"))
        sex = g.buttonbox("请选择性别：", choices=["男", "女"])
        if sex == "男":
            sex = 1
        else:
            sex = 0
        #获取所需的数据
        BMI = (weight / (height * height))
        BFR = 1.2 * (round(BMI, 1)) + 0.23 * age - 5.4 - 10.8 * sex
        #获取的数据进行计算
        text = "你的BMI为:" + str(round(BMI, 1)) + "\n"
        if round(BMI, 1) <= 18.5:
            g.msgbox(text+"你的身材：偏瘦")
        elif 18.5 < round(BMI, 1) <= 24.0:
            g.msgbox(text+"你的身材：正常")
        elif 24.0 < round(BMI, 1) <= 28.0:
            g.msgbox(text+"你的身材：超重")
        elif round(BMI, 1) > 28.0:
            g.msgbox(text+"你的身材：肥胖")
        else:
            g.msgbox("计算错误，请重新输入")
        text = "你的体脂率BFR为" + str(round(BFR, 2)) + "\n"
        if round(BFR, 1) < 10.0:
            g.msgbox(text+"体脂率不足")
        elif 10.0 < round(BFR, 1) <= 20.0:
            g.msgbox(text+"体脂率正常")
        elif round(BFR, 1) > 20:
            g.msgbox(text+"体脂率偏高")
        else:
            g.msgbox("计算错误，请重新输入")

    bbbbb = random.choice(aaaaa)
    if bbbbb == "x":
        get_name()
    elif bbbbb == "y":
        get_gossips()
    elif bbbbb == "z":
        days()
    elif bbbbb == "j":
        get_news()
    elif bbbbb == "k":
        BMI_BFR()
except Exception as bug:
    g.msgbox("出错了\n"+str(bug))
