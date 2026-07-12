food_list = ["0西冷牛扒","1美食烤鸡","2三文鱼","3意大利面","4牛排","5凯撒沙拉","6英式炸鱼排","7西兰花","8烤布丁","9草莓冰淇淋","10原味冰淇淋","11巧克力冰淇淋","12香草冰淇淋","13蘑菇汤","14玉米汤","15佐料","16果汁","17蛋汤炒绝味菜炒饭炒暴风","18饭","19菜","20汤","21零食","22三明治","23披萨","24奶茶"]
order = []
print("欢迎来到我们的餐厅！！！！！")
print("这是我们的菜单:",food_list)
choice = input("按A开始点菜：")
while True:
    if choice == "A":
        food_num = int(input("请输入想点菜品的序号(不可一次输入2个！！！):"))
        food_name = food_list[food_num]
        order.append(food_name)
        choice = input("继续点餐请输入A，删除菜品请输入B，停止点餐开始Eat请输入其他字符:")
    elif choice == "B":
        print("您点了这些菜品:",order)
        food_num = int(input("请输入想删除菜品的序号:"))
        food_name = food_list[food_num]
        order.remove(food_name)
        choice = input("继续点餐请输入A，删除菜品请输入B，停止点餐开始Eat请输入其他字符:")
    else:
        break
print("您点了这些菜:",order)