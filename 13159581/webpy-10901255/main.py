from drone import *
print("a. 水果  b. 糖果  c. 老师")
ans = input("请领取你想要配送的任务: ")
if ans == "a":
    add("fruit.png","juice.png")
if ans == "b":    
    add("candy.png","candyshop.png")
if ans == "c":
    add("teacher.png","school.png")
key = input("请输入切换快递的按键：")
change(key)
print("a.简单  b.一般  c.困难")
ans = input("请设置游戏模式，输入a、b、或c：")
if ans == "a":
    mode("easy")
if ans == "b":    
    mode("normal")
if ans == "c":
    mode("hard")
drop("space")