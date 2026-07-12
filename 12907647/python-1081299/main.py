phone = input("请输入挑战者的电话号码{11位！}")

print(phone[0:2],"******",phone[8:11],"手机号已登录完毕，欢迎参加成语接龙挑战！")
a = "人山人海"
print("成语接龙：" + a)

num = 0
number = 0

while True:
    b = input("输入下一个成语：")

    if len(b) != 4:
        print("不是四字成语，游戏结束！")
        print("一共接对了",num,"个成语！")
        print("金币共是：",number,"个！")
        break
    elif a[3] == b[0]:
        print("挑战成功！加两个金币！")
        a = b
        num = num + 1
        number = number + 2
        print("目前金币是：",number,"个！")
    else:
        print("回答错误，挑战失败！")
        print("一共接对了",num,"个成语！")
        print("金币共是：",number,"个！")
        break