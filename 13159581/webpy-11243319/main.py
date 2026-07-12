from drone import *
print("a. 水果  b. 糖果  c. 老师")
ans = input("请领取你想要配送的任务: ")
if ans == "a":
    add("fruit.png","juice.png")
if ans == "b":    
    add("candy.png","candyshop.png")
if ans == "c":
    add("teacher.png","school.png")
drop("space")