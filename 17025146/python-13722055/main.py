#导库
from tkinter import*
from time import*
from sys import*
from random import*
from xes import*
from tkinter import messagebox
import urllib.request
import requests
import json

#定义游戏

def 三国杀():
    root.destroy()
    sleep(1)
    clear()
    pai = ["桃","酒","杀","闪","万箭齐发","南蛮入侵","顺手牵羊","过河拆桥","釜底抽薪","无中生有","无懈可击","火杀","雷杀"]
    wopai = []
    dipai = []
    wokill = 1
    dikill = 1
    woxue = 3
    dixue = 3
    print("欢迎进入三国杀游戏！")
    print("开局随机抽牌4张")
    print("正在抽取己方卡牌")
    for i in range(4):
        aa = choice(pai)
        wopai.append(aa)
    sleep(0.5)
    print("正在抽取敌方卡牌")
    for i in range(4):
        bb = choice(pai)
        dipai.append(bb)
    sleep(0.5)
    print("抽牌完成！")
    while True:
        if woxue == 0:
            print("敌方获胜！")
            break
        if dixue == 0:
            print("我方获胜！")
            break
        print("我方回合")
        k = ""
        while k != "结束":
            clear()
            print("我方血量：",woxue,"敌方血量：",dixue)
            print("我方回合")
            print("我方所拥有的牌：")
            for i in wopai:
                print(i)
            k = input("请输入你想出的牌，输入“结束”以结束出牌")
            if k == "结束":
                break
            if k in wopai:
                if k == "杀":
                    if "闪" in dipai:
                        input("敌方使用了闪，你的杀失效了！按下回车以进入下一轮出牌")
                        dipai.remove("闪")
                    else:
                        dixue -= 1
                        input("出牌成功！敌方血量减少1点，按下回车以进入下一轮出牌")
                    wopai.remove(k)
                    if woxue == 0:
                        print("敌方获胜！")
                        break
                    if dixue == 0:
                        print("我方获胜！")
                        break
                if k == "火杀" or k == "雷杀":
                    if "闪" in dipai:
                        input("敌方使用了闪，你的杀失效了！按下回车以进入下一轮出牌")
                        dipai.remove("闪")
                    else:
                        dixue -= 2
                        input("出牌成功！敌方血量减少2点，按下回车以进入下一轮出牌")
                    wopai.remove(k)
                    if woxue == 0:
                        print("敌方获胜！")
                        break
                    if dixue == 0:
                        print("我方获胜！")
                        break
                if k == "无中生有":
                    if "无懈可击" in dipai:
                        dipai.remove("无懈可击")
                        input("敌方使用了无懈可击，你的牌失效了！按下回车以进入下一轮出牌")
                    else:
                        for i in range(2):
                            g = choice(pai)
                            wopai.append(g)
                        sleep(0.25)
                        input("抽牌成功！按下回车以进入下一轮出牌")
                    wopai.remove(k)
                    if woxue == 0:
                        print("敌方获胜！")
                        break
                    if dixue == 0:
                        print("我方获胜！")
                        break
                if k == "桃":
                    if "无懈可击" in dipai:
                        dipai.remove("无懈可击")
                        input("敌方使用了无懈可击，你的牌失效了！按下回车以进入下一轮出牌")
                    elif woxue == 3:
                        input("我方血量已达上限！按下回车以进入下一轮出牌")
                    else:
                        woxue += 1
                        sleep(0.25)
                        input("回血成功！按下回车以进入下一轮出牌")
                    wopai.remove(k)
                    if woxue == 0:
                        print("敌方获胜！")
                        break
                    if dixue == 0:
                        print("我方获胜！")
                        break
                if k == "酒":
                    if "无懈可击" in dipai:
                        dipai.remove("无懈可击")
                        input("敌方使用了无懈可击，你的牌失效了！按下回车以进入下一轮出牌")
                    else:
                        wokill += 1
                        sleep(0.25)
                        input("使用成功！我方攻击加1！按下回车以进入下一轮出牌")
                    wopai.remove(k)
                    if woxue == 0:
                        print("敌方获胜！")
                        break
                    if dixue == 0:
                        print("我方获胜！")
                        break
                if k == "南蛮入侵":
            
                    if "杀" in dipai:
                        dipai.remove("杀")
                        input("敌方使用了杀，你的牌失效了！按下回车以进入下一轮出牌")
                    else:
                        dixue -= wokill
                        sleep(0.25)
                        input("使用成功！敌方血量减一！按下回车以进入下一轮出牌")
                    wopai.remove(k)
                    if woxue == 0:
                        print("敌方获胜！")
                        break
                    if dixue == 0:
                        print("我方获胜！")
                        break
                if k == "顺手牵羊":
                    if len(dipai) > 0:
                        if "无懈可击" in dipai:
                            dipai.remove("无懈可击")
                            input("敌方使用了无懈可击，你的牌失效了！按下回车以进入下一轮出牌")
                        else:
                            for i in range(len(dipai)):
                                print(i + 1)
                            u = int(input("请输入你想抽的牌序号："))
                            er = dipai[u - 1]
                            dipai.remove(er)
                            wopai.append(er)
                            print("你抽了敌方的",er)
                            input("抽牌成功！按下回车以进入下一轮出牌")
                        wopai.remove(k)  
                    else:
                        input("敌方已无手牌，按下回车以进入下一轮出牌")
                    if woxue == 0:
                        print("敌方获胜！")
                        break
                    if dixue == 0:
                        print("我方获胜！")
                        break
                if k == "过河拆桥" or k == "釜底抽薪":
                    if "无懈可击" in dipai:
                        dipai.remove("无懈可击")
                        input("敌方使用了无懈可击，你的牌失效了！按下回车以进入下一轮出牌")
                    else:
                        for i in range(len(dipai)):
                            print(i + 1)
                        u = int(input("请输入你想废掉的牌序号："))
                        er = dipai[u - 1]
                        dipai.remove(er)
                        print("你废了敌方的",er)
                        input("废牌成功！按下回车以进入下一轮出牌")
                    wopai.remove(k)  
                    if woxue == 0:
                        print("敌方获胜！")
                        break
                    if dixue == 0:
                        print("我方获胜！")
                        break
                if k == "万箭齐发":
                    if "闪" in dipai:
                        input("敌方使用了闪，你的牌失效了！按下回车以进入下一轮出牌")
                        dipai.remove("闪")
                    else:
                        dixue -= wokill
                        input("出牌成功！敌方血量减少" + str(wokill) + "点，按下回车以进入下一轮出牌")
                    wopai.remove(k)
                    if woxue == 0:
                        print("敌方获胜！")
                        break
                    if dixue == 0:
                        print("我方获胜！")
                        break
            elif k != "结束":
                input("你没有这张牌！按下回车以进入下一轮出牌")
        if woxue == 0:
            print("敌方获胜！")
            break
        if dixue == 0:
            print("我方获胜！")
            break    
        print("下一回合，双方各随机抽牌两张！")
        for i in range(2):
            wopai.append(choice(pai))
            dipai.append(choice(pai))
        print("敌方出牌阶段")
        for k in dipai:
            clear()
            print("敌方血量：",dixue,"我方血量：",woxue)
            if k == "杀":
                print("敌方出了",k)
                if "闪" in wopai:
                    e = input("监测到你有闪，是否使用？是/否")
                    if e == "是":
                        wopai.remove("闪")
                        print("我方使用了闪，敌方的杀失效了！")
                    else:
                        woxue -= 1
                        print("敌方出牌成功！我方血量减少1点!")
                else:
                    woxue -= 1
                    print("敌方出牌成功！我方血量减少1点!")
                dipai.remove(k)
                if woxue == 0:
                    print("敌方获胜！")
                    break
                if dixue == 0:
                    print("我方获胜！")
                    break    
            if k == "火杀" or k == "雷杀":
                print("敌方出了",k)
                if "闪" in wopai:
                    e = input("监测到你有闪，是否使用？是/否")
                    if e == "是":
                        wopai.remove("闪")
                        print("我方使用了闪，敌方的牌失效了！")
                    else:
                        woxue -= 2
                        print("敌方出牌成功！我方血量减少2点!")
                else:
                    woxue -= 2
                    print("敌方出牌成功！我方血量减少2点!")
                dipai.remove(k)
                if woxue == 0:
                    print("敌方获胜！")
                    break
                if dixue == 0:
                    print("我方获胜！")
                    break 
            if k == "无中生有":
                print("敌方出了",k)
                if "无懈可击" in wopai:
                    t = input("监测到你有无懈可击，是否使用？是/否")
                    if t == "是":
                        wopai.remove("无懈可击")
                        print("我方使用了无懈可击，敌方的牌失效了！")
                    else:
                        for i in range(2):
                            g = choice(pai)
                            dipai.append(g)
                        sleep(0.25)
                        print("敌方抽牌成功！")
                else:
                    for i in range(2):
                        g = choice(pai)
                        dipai.append(g)
                    sleep(0.25)
                    print("敌方抽牌成功！")
                dipai.remove(k)
                if woxue == 0:
                    print("敌方获胜！")
                    break
                if dixue == 0:
                    print("我方获胜！")
                    break 
            if k == "桃" and dixue < 3:
                print("敌方出了",k)
                if "无懈可击" in wopai:
                    t = input("监测到你有无懈可击，是否使用？是/否")
                    if t == "是":
                        wopai.remove("无懈可击")
                        print("我方使用了无懈可击，敌方的牌失效了！")
                    else:
                        dixue += 1
                        sleep(0.25)
                        print("敌方回血成功！")
                else:
                    dixue += 1
                    sleep(0.25)
                    print("敌方回血成功！")
                dipai.remove(k)
                if woxue == 0:
                    print("敌方获胜！")
                    break
                if dixue == 0:
                    print("我方获胜！")
                    break 
            if k == "酒":
                print("敌方出了",k)
                if "无懈可击" in wopai:
                    t = input("监测到你有无懈可击，是否使用？是/否")
                    if t == "是":
                        wopai.remove("无懈可击")
                        print("我方使用了无懈可击，敌方的牌失效了！")
                    else:
                        dikill += 1
                        sleep(0.25)
                        print("敌方攻击增加成功！")
                else:
                    dikill += 1
                    sleep(0.25)
                    print("敌方攻击增加成功！")
                dipai.remove(k)
                if woxue == 0:
                    print("敌方获胜！")
                    break
                if dixue == 0:
                    print("我方获胜！")
                    break 
            if k == "南蛮入侵":
                print("敌方出了",k)
                if "杀" in wopai:
                    t = input("监测到你有杀，是否使用？是/否")
                    if t == "是":
                        wopai.remove("杀")
                        print("我方使用了杀，敌方的牌失效了！")
                    else:
                        woxue -= dikill
                        sleep(0.25)
                        print("敌方出牌成功！我方血量减",dikill)
                else:
                    woxue -= dikill
                    sleep(0.25)
                    print("敌方出牌成功！我方血量减",dikill)
                dipai.remove(k)
                if woxue == 0:
                    print("敌方获胜！")
                    break
                if dixue == 0:
                    print("我方获胜！")
                    break 
            if k == "顺手牵羊":
                print("敌方出了",k)
                if len(wopai) > 0:
                    if "无懈可击" in wopai:
                        t = input("监测到你有无懈可击，是否使用？是/否")
                        if t == "是":
                            wopai.remove("无懈可击")
                            print("我方使用了无懈可击，敌方的牌失效了！")
                        else:
                            wopai.remove(randint(0,len(wopai)-1))
                            dipai.append(randint(0,len(wopai)-1))
                            print("敌方抽牌成功！")
                    else:
                        wopai.remove(randint(0,len(wopai)-1))
                        dipai.append(randint(0,len(wopai)-1))
                        print("敌方抽牌成功！")
                    dipai.remove(k)  
                else:
                    print("我方已无手牌，顺手牵羊无效")
                    
                if woxue == 0:
                    print("敌方获胜！")
                    break
                if dixue == 0:
                    print("我方获胜！")
                    break 
            if k == "过河拆桥" or k == "釜底抽薪":
                print("敌方出了",k)
                if "无懈可击" in wopai:
                    t = input("监测到你有无懈可击，是否使用？是/否")
                    if t == "是":
                        wopai.remove("无懈可击")
                        print("我方使用了无懈可击，敌方的牌失效了！")
                    else:
                        wopai.remove(randint(0,len(wopai)-1))
                        print("敌方废牌成功！")
                else:
                    dipai.append(randint(0,len(wopai)-1))
                    print("敌方废牌成功！")  
                dipai.remove(k)
                if woxue == 0:
                    print("敌方获胜！")
                    break
                if dixue == 0:
                    print("我方获胜！")
                    break 
            if k == "万箭齐发":
                print("敌方出了",k)
                if "闪" in wopai:
                    e = input("监测到你有闪，是否使用？是/否")
                    if e == "是":
                        wopai.remove("闪")
                        print("我方使用了闪，敌方的牌失效了！")
                    else:
                        woxue -= dikill
                        print("敌方出牌成功！我方血量减少",dikill)
                else:
                    woxue -= dikill
                    print("敌方出牌成功！我方血量减少",dikill)
                dipai.remove(k)
                if woxue == 0:
                    print("敌方获胜！")
                    break
                if dixue == 0:
                    print("我方获胜！")
                    break 
            sleep(2)
        print("敌方出牌结束！")
        print("下一回合，双方各随机抽牌两张！")
        for i in range(2):
            wopai.append(choice(pai))
            dipai.append(choice(pai))
            
            
def 三国英雄志():
    root.destroy()
    sleep(1)
    clear()
    wujiang = {}
    shangzhen = []
    wujiangshu = 0
    shilian = 1
    jinbi = 1000000000
    zhuangbei = {}
    zhuangbeishu = 0
    qiandao = 0
    dianquan = 0
    shuijing = 0
    zaizhuang = []
    wujianglist=["5星刘备","5星曹操","5星孙权","4星周瑜","4星张飞","4星关羽","4星诸葛亮","3星小乔","3星貂蝉","3星黄盖"]
    while True:
        clear()
        print("欢迎进入三国游戏！")
        print("你现在的金币数：",jinbi,"试炼关卡：",shilian,"武将数量：",wujiangshu,"装备数量：",zhuangbeishu)
        a=input("你现在要干什么？1、抽武将 2、参与试炼 3、查看武将属性 4、打造装备 5、背包")
        if a == "1":
            clear()
            print("你现在有金币",jinbi,"枚，水晶",shuijing,"个，点券",dianquan,"张。")
            b = input("你要选择哪种方式？1、金币抽武将 2、点券抽武将 3、水晶抽武将")
            if b == "1":
                jinbichoushu = int(input("你要抽几次？"))
                if jinbi >= jinbichoushu * 1000:
                    for i in range(jinbichoushu):
                        x=choice(wujianglist)
                        wujiang[x] = int(x[0:1])
                        wujiangshu = wujiangshu + 1 
                        jinbi = jinbi - 1000
                else:
                    print("金币不够！")
            if b == "2":
                dianquanchoushu = int(input("你要抽几次？"))
                if dianquan >= dianquanchoushu * 200:
                    for i in range(dianquanchoushu):
                        x=choice(wujianglist)
                        wujiang[x] = int(x[0:1])
                        wujiangshu = wujiangshu + 1 
                        dianquan = dianquan - 200
                else:
                    print("点券不够！")
            if b == "3":
                shuijingchoushu = int(input("你要抽几次？"))
                if shuijing >= shuijingchoushu * 50:
                    for i in range(shuijingchoushu):
                        x=choice(wujianglist)
                        wujiang[x] = int(x[0:1])
                        wujiangshu = wujiangshu + 1 
                        shuijing = shuijing - 50
                else:
                    print("水晶不够！")
        if a == "2":
            direnxueliang = 100
            heroxueliang = 100
            print("目前试炼关卡：第",shilian,"关。")
            print("目前上阵武将：",end = "")
            for i in shangzhen:
                print(i,end = "")
            print("")
            input("回车进入试炼。")
            
            
                
            print("正在攻打第",shilian,"层...")
            sleep(1)
            gongdahero = input("前方出现了敌人！你要派谁去攻打？")
            if gongdahero in shangzhen:
                print(gongdahero + "与敌人短兵相接，战斗开始了！")
                while heroxueliang > 0 or direnxueliang > 0:
                    clean(1.5)
                    print("己方血量："+str(heroxueliang)+"敌方血量："+str(direnxueliang))
                    heroble=input("己方回合：请输入您想发出的大招：1. 伤害15滴血 2. 伤害20滴血，自己掉血在1~10之间 3. 伤害25滴血，自己掉血在5~15之间 4.大招：伤害40滴血，自己掉血15~25之间")
                    if heroble == "1":
                        direnxueliang = direnxueliang - 15
                    elif heroble == "2":
                        direnxueliang = direnxueliang - 20
                        heroxueliang = heroxueliang - randint(1,10)
                    elif heroble == "3":
                        direnxueliang = direnxueliang - 25
                        heroxueliang = heroxueliang - randint(5,15)
                    elif heroble == "4":
                        direnxueliang = direnxueliang - 40
                        heroxueliang = heroxueliang - randint(15,25)
                    direnble = randint(1,4)
                    print("敌方回合：敌人使用了第",direnble,"招")
                    if direnble == 1:
                        heroxueliang = heroxueliang - 15
                    elif direnble == 2:
                        heroxueliang = heroxueliang - 20
                        direnxueliang = direnxueliang - randint(1,10)
                    elif direnble == 3:
                        heroxueliang = heroxueliang - 25
                        direnxueliang = direnxueliang - randint(5,15)
                    elif direnble == 4:
                        heroxueliang = heroxueliang - 40
                        direnxueliang = direnxueliang - randint(15,25)
                   
                    if direnxueliang <= 0:
                        jinbi = jinbi + shilian * 1000
                        input("恭喜通关试炼第"+str(shilian)+"层！")
                        shilian = shilian + 1
                    elif heroxueliang <= 0:
                        input("你输了！回车退出试炼")
        if a == "3":
            print("所有武将：")
            for i in wujiang:
                print(i,"战斗力：",wujiang[i] * 1000)
            print("已上阵武将：")
            for i in shangzhen:
                print(i,"战斗力：",wujiang[i] * 1000)
            shangxia = input("1、上阵武将 2、下阵武将 3、返回")
            if shangxia == "1":
                xxx = input("你要上阵哪个武将？")
                if xxx in wujiang and len(shangzhen)<= 6:
                    shangzhen.append(xxx)
                else:
                    input("不存在该武将或上阵武将数已达上限！")
            elif shangxia == "2":
                xxx = input("你要下阵哪个武将？")
                if xxx in shangzhen and len(shanzhen)>= 1:
                    shangzhen.remove(xxx)
                else:
                    input("不存在该武将或上阵武将数已达下限！")
                
        if a == "4":
            ss = input("你想打造哪种装备？1、武器 2、盔甲 3、法宝")
            if ss == "1":
                dengji = input("你要打造哪种级别的武器？1、普通 2、稀有 3、史诗 4、传说 5、神器")
                
                qq = ["木质","石制","铁质","精钢","神铁"]
                
                print("恭喜你获得" + qq[int(dengji)-1] + "剑一把！")
                zhuangbei[qq[int(dengji)-1] + "剑"] = str(dengji) + "级"
                jinbi = jinbi - int(dengji) * 300
                zhuangbeishu = zhuangbeishu + 1
            if ss == "2":
                dengji = input("你要打造哪种级别的盔甲？1、普通 2、稀有 3、史诗 4、传说 5、神器")
                
                qq = ["木质","石制","铁质","精钢","神铁"]
                
                print("恭喜你获得" + qq[int(dengji)-1] + "盔甲一副！")
                zhuangbei[qq[int(dengji)-1] + "盔甲"] = str(dengji) + "级"
                jinbi = jinbi - int(dengji) * 500
                zhuangbeishu = zhuangbeishu + 1
            if ss == "3":
                dengji = input("你要打造哪种级别的法宝？1、普通 2、稀有 3、史诗 4、传说 5、神器")
                
                qq = ["阴阳镜","轩辕剑","八卦炉","紫金红葫芦","九品莲台"]
                
                print("恭喜你获得" + qq[int(dengji)-1] + "！")
                zhuangbei[qq[int(dengji)-1]] = str(dengji) + "级"
                jinbi = jinbi - int(dengji) * 1000
                zhuangbeishu = zhuangbeishu + 1
                
        if a == "5":
            print("现有装备：",zhuangbeishu,"件")
            for i in zhuangbei:
                print(i)
            sd = input("1、使用装备 2、取下装备 3、返回")
            if sd == "1":
                shiyong = input("你想使用哪件装备？")
                if shiyong in zhuangbei:
                    duixiang = input("你想将它装备在哪位武将身上？")
                    if duixiang in shangzhen:
                        wujiang[duixiang] = wujiang[duixiang] * 20
                        zaizhuang.append(shiyong)
                    else:
                        input("输入错误")
                else:
                    input("输入错误")
            if sd == "2":
                sse = input("你想取下哪位武将所使用的装备？")
                if sse in shangzhen:
                    ssr = input("你想去掉哪一件装备？")
                    if ssr in zaizhuang:
                        zaizhuang.remove(ssr)
                        wujiang[sse] = wujiang[sse] / 20  
                        
                        
def 三国英雄帖():
    root.destroy()
    sleep(1)
    clear()
    sanguo = {"曹操下江南":"来得凶，败得惨",
    "张飞扔鸡毛":"有劲难使",
    "诸葛亮征孟获":"收收放放",
    "曹操吃鸡肋":"食之无味，弃之可惜",
    "张飞使计谋":"粗中有细",
    "诸葛亮弹琴":"计上心来",
    "曹操遇蒋干":"倒了大霉",
    "张飞贩私盐":"谁敢检查",
    "诸葛亮的鹅毛扇":"神妙莫测",
    "曹操作事":"干干净净",
    "张飞卖秤锤":"人强货硬",
    "诸葛亮三气周瑜":"略施小技",
    "曹操杀华佗":"讳疾忌医",
    "张飞卖肉":"光说不割",
    "诸葛亮借箭":"有借无还",
    "曹操用计":"又奸又滑",
    "张飞战关公":"忘了旧情",
    "诸葛亮挥泪斩马谡":"顾全大局",
    "曹操战宛城":"大败而逃",
    "张飞吃豆芽":"一盘小莱",
    "诸葛亮要丑妻":"为事业着想",
    "曹操杀吕伯奢":"将错就错",
    "诸葛亮招亲":"才重于貌",
    "曹操败走华客道":"不出所料",
    "张飞穿针":"大眼瞪小眼",
    "诸葛亮用兵":"神出鬼没",
    "诸葛亮的锦羹":"神机妙算",
    "曹操诸葛亮":"脾气不一样",
    "草船借箭":"多多益善",
    "阿斗当皇帝":"软弱无能",
    "关公开凤眼":"要杀人",
    "董卓戏貂蝉":"死在花下",
    "关羽卖肉":"没人敢来",
    "草船借箭":"满载而归",
    "貂蝉唱歌":"有声有色",
    "关帝庙求子":"踏错了门",
    "关公射黄忠":"手下留情",
    "诸葛亮吊孝":"装模作样",
    "鲁肃宴请关云长":"暗藏杀机",
    "关公照镜子":"自觉脸红",
    "诸葛亮用空城计":"不得已",
    "东吴招亲":"弄假成真",
    "关云长走麦城":"大难临头",
    "诸葛亮唱空城计":"没办法",
    "司马懿破八卦阵":"不懂装懂",
    "周瑜讨荆州":"费力不讨好",
    "鲁肃讨荆州":"空手而去，空手而回",
    "三个臭皮匠":"顶个诸葛亮",
    "吃曹操的饭，想刘备的事":"人在心不在",
    "关胜战李遣":"大刀阔斧",
    "关云长刮骨疗毒":"全无痛苦之色",
    "董卓进京":"来者不善",
    "周瑜打黄盖":"两相情愿；一个愿打，一个愿挨",
    "看三国掉泪":"替古人担忧",
    "黄忠射箭":"百发百中",
    "刘备摔孩子":"收买人心",
    "孔明练琴":"老生常谈",
    "张飞上阵":"横冲直撞",
    "阿斗当官":"有名无实",
    "周瑜病倒在芦花荡":"气煞",
    "张飞捉蚂蚱":"有劲使不上",
    "张飞战马超":"不分胜负",
    "鲁肃服孔明":"五体投地",
    "赵子龙出兵":"回回胜",
    "曹操用人":"唯才是举",
    "关羽进皇宫":"单刀直入",
    "关羽开刀铺":"货真价实",
    "关羽守嫂嫂":"情谊为重",
    "司马夸诸葛":"甘拜下风",
    "赵云大战长坂坡":"大显神威",
    "黄忠叫阵":"不服老",
    "张飞睡觉":"不闭眼",
    "黄忠射箭":"百发百中 ",
    "孔明皱眉头":"计上心头",
    "孔明借东风":"巧用天时",
    "关羽看《春秋》":"一目了然",
    "刘备编草鞋":"内行",
    "吕布戏貂蝉":"英雄难过美人关",
    "蒋干盗书":"聪明反被聪明误",
    "诸葛亮玩狗":"聪明一世糊涂一时",
    "张飞拆桥":"有勇无谋",
    "关公面前耍大刀":"自不量力",
    "关羽赴宴":"有胆有魄",
    "孔明弹琴退仲达":"临危不乱",
    "刘备三顾茅庐":"好难请",
    "诸葛亮弹琴":"计上心来",
    "庞统当知县":"大材小用",
    "黄忠抡大锤":"老当益壮",
    "关羽打喷嚏":"自我吹嘘",
    "诸葛亮隆中对策":"有先见之明",
    "关公喝酒":"不怕脸红",
    "曹操转胎":"疑心重",
    "许褚斗马超":"赤膊上阵"}
    while True:
        clear()
        y = input("你需要哪种功能？1、查询某条歇后语 2、查询全部歇后语")
        if y == "1":
            uu = ""
            while uu != "返回":
                clear()
                uu = input("请输入谜面,输入返回及返回选择区：")
                if uu == "返回":
                    break
                elif uu in sanguo:
                    print("对应的歇后语是",sanguo[uu])
                    input("按下回车以进入下一轮搜索")
                else:
                    print("暂未查询到相关歇后语")
                    input("按下回车以进入下一轮搜索")
        if y == "2":
            for k,y in sanguo.items():
                print(k,":",y)
                sleep(0.05)
            input("按下回车以返回选择区")
            
#定义工具函数
            
def _nice(emoji_str):
	import struct
	return ''.join(
		c if c <= '\uffff' else ''.join(chr(x) for x in struct.unpack('>2H', c.encode('utf-16be'))) for c in emoji_str)


def __init__(self,pid):
    self.pid=pid


def getCookies():
    cookies = ""
    if len(sys.argv) > 1:
        try:
            cookies = json.loads(sys.argv[1])["cookies"]
        except:
            pass
    return cookies


def __init__(self, id):
		s = requests.Session()
		id = str(id)
		url = "http://code.xueersi.com/api/space/index?user_id=" + id
		headers ={'Accept': 'application/json, text/plain, */*', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'Cookie': 'xesId=b524835904a4a420cba3dde34890bade; user-select=scratch; userGrade=8; wx=408f3d126b6e5da40f1231f4a8e82cecmqx0f94f4q; Hm_lvt_a8a78faf5b3e92f32fe42a94751a74f1=1600492811,1600492816; xes-code-id=87f66376f1afd34f70339baeca61b7a1.8dbd833da9122d69a17f91054066dbb3; prelogid=82f1c3968c8ff01ee151a0413f56aa84; xes_run_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiIuY29kZS54dWVlcnNpLmNvbSIsImF1ZCI6Ii5jb2RlLnh1ZWVyc2kuY29tIiwiaWF0IjoxNjAxODA5NDg4LCJuYmYiOjE2MDE4MDk0ODgsImV4cCI6MTYwMTgyMzg4OCwidXNlcl9pZCI6bnVsbCwidWEiOiJNb3ppbGxhXC81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXRcLzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZVwvODUuMC40MTgzLjEyMSBTYWZhcmlcLzUzNy4zNiBFZGdcLzg1LjAuNTY0LjY4IiwiaXAiOiIxMTIuNDkuNzIuMTc1In0.Depgg9J-Hbe5RDeQvQwn59Aj0aa4CnndKeOKad-5WTY; X-Request-Id=db987fe27cbc7c51525a99c6419a34c7; Hm_lpvt_a8a78faf5b3e92f32fe42a94751a74f1=1601810095', 'Host': 'code.xueersi.com', 'Proxy-Connection': 'keep-alive', 'Referer': 'http://code.xueersi.com/space/11909587', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.68'}
		a = s.get(url=url, headers=headers)
		a = json.loads(_nice(a.text))
		a = a["data"]
		self.data = a
		self.works = a["works"]["total"]
		self.fans = a["fans"]["total"]
		self.follows = a["follows"]["total"]
		self.overview = a["overview"]
		self.like_num = self.overview["likes"]
		self.view_num = self.overview["views"]
		self.work_num = self.overview["works"]
		self.favorites = self.overview["favorites"]


def get_info(id):
	s = requests.Session()
	headers = {'Accept': 'application/json, text/plain, */*', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'Cookie': 'xesId=b524835904a4a420cba3dde34890bade; user-select=scratch;  xes_run_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiIuY29kZS54dWVlcnNpLmNvbSIsImF1ZCI6Ii5jb2RlLnh1ZWVyc2kuY29tIiwiaWF0IjoxNjAxODA5NDcxLCJuYmYiOjE2MDE4MDk0NzEsImV4cCI6MTYwMTgyMzg3MSwidXNlcl9pZCI6bnVsbCwidWEiOiJNb3ppbGxhXC81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXRcLzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZVwvODUuMC40MTgzLjEyMSBTYWZhcmlcLzUzNy4zNiBFZGdcLzg1LjAuNTY0LjY4IiwiaXAiOiIxMTIuNDkuNzIuMTc1In0.9bXcb813GhSPhoUJkezZpV8O50ynm0hhYvszNyczznQ; prelogid=ef8f6d12febabf75bf9599744b73c6f5; xes-code-id=87f66376f1afd34f70339baeca61b7a1.8dbd833da9122d69a17f91054066dbb3; X-Request-Id=82f1c3968c8ff01ee151a0413f56aa84; Hm_lpvt_a8a78faf5b3e92f32fe42a94751a74f1=1601809487', 'Host': 'code.xueersi.com', 'Proxy-Connection': 'keep-alive', 'Referer': 'http://code.xueersi.com/space/11909587', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.68'}

	total = json.loads(
		_nice(s.get("http://code.xueersi.com/api/space/profile?user_id=" + str(id), headers=headers).text))[
		"data"]
	return {
		# "user_id": total["user_id"],
		"name": total["realname"],
		"slogan": total["signature"],
		"fans": total["fans"],
		"follows": total["follows"],
		"icon": total["avatar_path"]
	}


def getnowuser():
    try:
        a = getCookies()
        num = a.index("stu_id=") + 7
        id = ""
        for i in range(num, num + 100):
            if a[i] != ";":
                id = id + a[i]
            else:
                break
        try:
            user_info = get_info(id)
        except:
            user_info={"name":id+"号未知用户"}
            # 获取这个人的大部分信息，返回一个字典
            #:返回这个人的名字
        return {'state':True,'user_id':id, "user_name":user_info["name"]}
    except:
        return {"state":False,'user_id':"未登录","user_name":"未登录"}


def clear(time = 0):
    sleep(time)
    stdout.write('\033[2J\033[00H')


def logo(a):
    for i in range(len(a)):
        if a[i] == "0":
            print("\033[0m ",end="")
            sleep(0.01)
        elif a[i] == "1":
            print("\033[41m ",end="")
            sleep(0.01)
        elif a[i] == "2":
            print("\033[42m ",end="")
            sleep(0.01)
        elif a[i] == "3":
            print("\033[43m ",end="")
            sleep(0.01)
        elif a[i] == "4":
            print("\033[44m ",end="")
            sleep(0.01)
        elif a[i] == "5":
            print("\033[45m ",end="")
            sleep(0.01)
        elif a[i] == "6":
            print("\033[46m ",end="")
            sleep(0.01)
        elif a[i] == "7":
            print("\033[47m ",end="")
            sleep(0.01)
        elif a[i] == "d":
            print("\033[1;30m",end="")
            sleep(0.01)
        elif a[i] == "r":
            print("\033[1;31m",end="")
            sleep(0.01)
        elif a[i] == "g":
            print("\033[1;32m",end="")
            sleep(0.01)
        elif a[i] == "y":
            print("\033[1;33m",end="")
            sleep(0.01)
        elif a[i] == "b":
            print("\033[1;34m",end="")
            sleep(0.01)
        elif a[i] == "p":
            print("\033[1;35m",end="")
            sleep(0.01)
        elif a[i] == "c":
            print("\033[1;36m",end="")
            sleep(0.01)
        elif a[i] == "w":
            print("\033[1;37m",end="")
            sleep(0.01)
        else:
            print(a[i],end="")
            sleep(0.01)
    print("\033[0m")
    
#开头    

messagebox.showinfo("欢迎:","尊敬的" + getnowuser()["user_name"] + "，您好!")
messagebox.showinfo("欢迎:","欢迎进入三国游戏专区！")


#主体
root = Tk()
root.geometry("300x265")
root.title("三国专区")
button1 = Button(root,text="三国杀",command=三国杀,width=17,height=1,fg="#00FFFF",bg="#FEF5AA",font=("楷体", 25))
button1.place(x = 0,y = 100)
button2 = Button(root,text="三国英雄志",command=三国英雄志,width=17,height=1,fg="#FF00F6",bg="#FEF5AA",font=("楷体", 25))
button2.place(x = 0,y = 150)
button3 = Button(root,text="三国英雄帖",command=三国英雄帖,width=17,height=1,fg="#00FA9A",bg="#FEF5AA",font=("楷体", 25))
button3.place(x = 0,y = 200)
s = Label(root,text = "模式如下",fg="white",bg="blue",font = ("黑体",25),height = 2)
s.place(x = 80,y = 25)
root.mainloop()