# 现在学习编程的有可多、小红、小明三名同学。
# 运行程序，并将你的学习编程的几位好朋友拉入群中；
# 小红由于生病退出了学习群，请运行程序请她出群。
# 按下其他按键时，退出程序

friends= ["可多","小红","小明"]
while True:
    choice = input("加好友进群请按“+”，请人出群请按“-”，完成请按其他键：")
    if choice == "+":
        c = input("进群好友姓名：")
        friends.append(c)
        print('当前群内成员：',friends)
#请你在下面补充程序，实现请人退群的功能
    if choice == "+":
        c = input("退群好友姓名：")
        friends.remove(c)
    
    
    if choice != "+" and choice != "-":
        print('当前群内成员：',friends)
        break