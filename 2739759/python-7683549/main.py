import random
import math
import sys
import tkinter
if (sys.version_info > (3, 0)):
    from tkinter import *
    from tkinter import messagebox
else:
    from Tkinter import *
def 脑筋急转弯快乐机器():    
    # 黑客爬新闻（二）脑筋急转弯快乐机器
    global listb, List, Num
    root = tkinter.Tk()
    root.geometry("600x500")
    root.configure(background="black")
    root.title("脑筋急转弯快乐机器")
    root.resizable(False,False)
    #自己补充更多脑筋急转弯到List列表当中，让快乐机器更丰富
    List = [
        "什么动物天天熬夜？",
        "熊猫",
        "什么东西咬牙切齿？",
        "拉链","谁天天去看病？",
        "医生",
         "早餐时从来不吃的是什么？",
         "午餐和晚餐","什么桥下没有水？",
         "立交桥","什么数字减去一半等于0？",
         "8",
         "木字多一撇是什么字？",
         "移",
         "狐狸为什么容易摔跤？",
         "狐狸狡猾（脚滑）",
         "为什么飞机飞再高都撞不到星星？",
         "因为星星会闪",
         "白鸡和黑鸡哪只比较厉害？",
         "黑鸡（黑鸡能生白蛋，白鸡无法生黑蛋）",
         "大雁为什么飞到南方过冬？",
         "因为大雁走不到南方，所以飞",
         "什么样的老鼠用两只脚走路？",
         "米老鼠",
         "鱼为什么活在水里？",
         "因为岸上有猫",
         "太平洋的中间是什么？",
         "是平字",
         "布跟纸怕什么？",
         "布怕一万，纸怕万一（不怕一万，只怕万一）"]
    Num = 0
    # 向列表框中添加数据
    def renew():
        global listb, List, Num
        #在下一行借助索引Num从列表框的首行开始插入List中的数据
        listb.insert(0, List[Num])
        Num = Num+1
    # 创建宽width为60，高height为20，背景颜色bg自定义，字体颜色fg为自定义颜色的列表框        
    listb = tkinter.Listbox(root,width = 60,height = 20,bg = "black",fg = "white")
    listb.pack()
    # 设置按钮，按钮上文字是"黑客更新",绑定的函数是renew
    button1 = tkinter.Button(root,text = "更新脑经急转弯", command=renew)
    button1.pack()     
    root.mainloop()
def 游戏2048():
    _map_data = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    
    
    # -------------------------以下为2048游戏的基本算法---------------------------
    
    # 重置
    def reset():
        '''重新设置游戏数据,将地图恢复为初始状态，并加入两个数据 2 作用初始状态'''
        _map_data[:] = []  # _map_data.clear()
        _map_data.append([0, 0, 0, 0])
        _map_data.append([0, 0, 0, 0])
        _map_data.append([0, 0, 0, 0])
        _map_data.append([0, 0, 0, 0])
        # 在空白地图上填充两个2
        fill2()
        fill2()
    
    
    # 获取 0 个数
    def get_space_count():
        """获取没有数字的方格的数量,如果数量为0则说有无法填充新数据，游戏即将结束
        """
        count = 0
        for r in _map_data:
            count += r.count(0)
        return count
    
    
    # 计算分数
    def get_score():
        '''获取游戏的分数,得分规则是每次有两个数加在一起则生成相应的分数。
        如 2 和 2 合并后得4分, 8 和 8 分并后得 16分.
        根据一个大于2的数字就可以知道他共合并了多少次，可以直接算出分数:
        如:
           4 一定由两个2合并，得4分
           8 一定由两个4合并,则计:8 + 4 + 4 得32分
           ... 以此类推
        '''
        score = 0
        for r in _map_data:
            for c in r:
                score += 0 if c < 4 else c * int((math.log(c, 2) - 1.0))
        return score  # 导入数学模块
    
    
    # 随机数生成
    def fill2():
        '''填充2到空位置，如果填度成功返回True,如果已满，则返回False'''
        blank_count = get_space_count()  # 得到地图上空白位置的个数
        if 0 == blank_count:
            return False
        # 生成随机位置, 如，当只有四个空时，则生成0~3的数，代表自左至右，自上而下的空位置
        pos = random.randrange(0, blank_count)
        offset = 0
        for row in _map_data:  # row为行row
            for col in range(4):  # col 为列，column
                if 0 == row[col]:
                    if offset == pos:
                        # 把2填充到第row行，第col列的位置，返回True
                        row[col] = 2
                        return True
                    offset += 1
    
    
    # 结束判定
    def is_gameover():
        """判断游戏是否结束,如果结束返回True,否是返回False
        """
        for r in _map_data:
            # 如果水平方向还有0,则游戏没有结束
            if r.count(0):
                return False
            # 水平方向如果有两个相邻的元素相同，应当是可以合并的，则游戏没有结束
            for i in range(3):
                if r[i] == r[i + 1]:
                    return False
        for c in range(4):
            # 竖直方向如果有两个相邻的元素相同，应当可以合并的，则游戏没有结束
            for r in range(3):
                if _map_data[r][c] == _map_data[r + 1][c]:
                    return False
        # 以上都没有，则游戏结束
        return True
    
    
    # 移动合并分数
    def _left_move_number(line):
        '''左移一行数字,如果有数据移动则返回True，否则返回False:
        如: line = [0, 2, 0, 8] 即表达如下一行:
            +---+---+---+---+
            | 0 | 2 | 0 | 8 |      <----向左移动
            +---+---+---+---+
        此行数据需要左移三次:
          第一次左移结果:
            +---+---+---+---+
            | 2 | 0 | 8 | 0 |
            +---+---+---+---+
          第二次左移结果:
            +---+---+---+---+
            | 2 | 8 | 0 | 0 |
            +---+---+---+---+
          第三次左移结果:
            +---+---+---+---+
            | 2 | 8 | 0 | 0 |  # 因为最左则为2,所以8不动
            +---+---+---+---+
         最终结果: line = [4, 8, 0, 0]
        '''
        moveflag = False  # 是否移动的标识,先假设没有移动
        for _ in range(3):  # 重复执行下面算法三次
            for i in range(3):  # i为索引
                if 0 == line[i]:  # 此处有空位，右侧相邻数字向左侧移动，右侧填空白
                    moveflag = True
                    line[i] = line[i + 1]
                    line[i + 1] = 0
        return moveflag
    
    
    # 移动位置
    def _left_marge_number(line):
        '''向左侧进行相同单元格合并,合并结果放在左侧,右侧补零
        如: line = [2, 2, 4, 4] 即表达如下一行:
            +---+---+---+---+
            | 2 | 2 | 4 | 4 |
            +---+---+---+---+
        全并后的结果为:
            +---+---+---+---+
            | 4 | 0 | 8 | 0 |
            +---+---+---+---+
        最终结果: line = [4, 8, 8, 0]
        '''
        for i in range(3):
            if line[i] == line[i + 1]:
                moveflag = True
                line[i] *= 2  # 左侧翻倍
                line[i + 1] = 0  # 右侧归零
    
    
    # 移动逻辑
    def _left_move_aline(line):
        '''左移一行数据,如果有数据移动则返回True，否则返回False:
        如: line = [2, 0, 2, 8] 即表达如下一行:
            +---+---+---+---+
            | 2 |   | 2 | 8 |      <----向左移动
            +---+---+---+---+
        左移算法分为三步:
            1. 将所有数字向左移动来填补左侧空格,即:
                +---+---+---+---+
                | 2 | 2 | 8 |   |
                +---+---+---+---+
            2. 判断是否发生碰幢，如果两个相临且相等的数值则说明有碰撞需要合并,
               合并结果靠左，右则填充空格 
                +---+---+---+---+
                | 4 |   | 8 |   |
                +---+---+---+---+
            3. 再重复第一步，将所有数字向左移动来填补左侧空格,即:
                +---+---+---+---+
                | 4 | 8 |   |   |
                +---+---+---+---+
            最终结果: line = [4, 8, 0, 0]
        '''
        moveflag = False
        if _left_move_number(line):
            moveflag = True
        if _left_marge_number(line):
            moveflag = True
        if _left_move_number(line):
            moveflag = True
        return moveflag
    
    
    def left():
        """游戏左键按下时或向左滑动屏幕时的算法"""
        moveflag = False  # moveflag 是否成功移动数字标志位,如果有移动则为真值,原地图不变则为假值
    
        # 将第一行都向左移动.如果有移动就返回True
        for line in _map_data:
            if _left_move_aline(line):
                moveflag = True
        return moveflag
    
    
    def right():
        """游戏右键按下时或向右滑动屏幕时的算法
        选将屏幕进行左右对调，对调后，原来的向右滑动即为现在的向左滑动
        滑动完毕后，再次左右对调回来
        """
        # 左右对调
        for r in _map_data:
            r.reverse()
        moveflag = left()  # 向左滑动
        # 再次左右对调
        for r in _map_data:
            r.reverse()
        return moveflag
    
    
    def up():
        """游戏上键按下时或向上滑动屏幕时的算法
        先把每一列都自上而下放入一个列表中line中，然后执行向滑动，
        滑动完成后再将新位置摆回到原来的一列中
        """
        moveflag = False
        line = [0, 0, 0, 0]  # 先初始化一行，准备放入数据
        for col in range(4):  # 先取出每一列
            # 把一列中的每一行数入放入到line中
            for row in range(4):
                line[row] = _map_data[row][col]
            # 将当前列进行上移，即line 左移
            if (_left_move_aline(line)):
                moveflag = True
            # 把左移后的 line中的数据填充回原来的一列
            for row in range(4):
                _map_data[row][col] = line[row]
        return moveflag
    
    
    def down():
        """游戏下键按下时或向下滑动屏幕时的算法
        选将屏幕进行上下对调，对调后，原来的向下滑动即为现在的向上滑动
        滑动完毕后，再次上下对调回来
        """
        _map_data.reverse()
        moveflag = up()  # 上滑
        _map_data.reverse()
        return moveflag
    
    
    # -------------------------以下为2048游戏的操作界面---------------------------
    
    
    
    
    def main():
        reset()  # 先重新设置游戏数据
    
        root = Tk()  # 创建tkinter窗口
        root.title('2048游戏')  # 设置标题文字
        root.resizable(width=False, height=False)  # 固定宽和高
    
        # 以下是键盘映射
        keymap = {
            'a': left,
            'd': right,
            'w': up,
            's': down,
            'Left': left,
            'Right': right,
            'Up': up,
            'Down': down,
            'q': root.quit,
        }
    
        game_bg_color = "#bbada0"  # 设置背景颜色
    
        # 设置游戏中每个数据对应色块的颜色
        mapcolor = {
            0: ("#cdc1b4", "#776e65"),
            2: ("#eee4da", "#776e65"),
            4: ("#ede0c8", "#f9f6f2"),
            8: ("#f2b179", "#f9f6f2"),
            16: ("#f59563", "#f9f6f2"),
            32: ("#f67c5f", "#f9f6f2"),
            64: ("#f65e3b", "#f9f6f2"),
            128: ("#edcf72", "#f9f6f2"),
            256: ("#edcc61", "#f9f6f2"),
            512: ("#e4c02a", "#f9f6f2"),
            1024: ("#e2ba13", "#f9f6f2"),
            2048: ("#ecc400", "#f9f6f2"),
            4096: ("#ae84a8", "#f9f6f2"),
            8192: ("#b06ca8", "#f9f6f2"),
            # ----其它颜色都与8192相同---------
            2 ** 14: ("#b06ca8", "#f9f6f2"),
            2 ** 15: ("#b06ca8", "#f9f6f2"),
            2 ** 16: ("#b06ca8", "#f9f6f2"),
            2 ** 17: ("#b06ca8", "#f9f6f2"),
            2 ** 18: ("#b06ca8", "#f9f6f2"),
            2 ** 19: ("#b06ca8", "#f9f6f2"),
            2 ** 20: ("#b06ca8", "#f9f6f2"),
        }
    
        def on_key_down(event):
            '键盘按下处理函数'
            keysym = event.keysym
            if keysym in keymap:
                if keymap[keysym]():  # 如果有数字移动
                    fill2()  # 填充一个新的2
            update_ui()
            if is_gameover():
                mb = messagebox.askyesno(
                    title="gameover", message="游戏结束!\n是否退出游戏!")
                if mb:
                    root.quit()
                else:
                    reset()
                    update_ui()
    
        def update_ui():
            '''刷新界面函数
            根据计算出的f地图数据,更新各个Label的设置
            '''
            for r in range(4):
                for c in range(len(_map_data[0])):
                    number = _map_data[r][c]  # 设置数字
                    label = map_labels[r][c]  # 选中Lable控件
                    label['text'] = str(number) if number else ''
                    label['bg'] = mapcolor[number][0]
                    label['foreground'] = mapcolor[number][1]
            label_score['text'] = str(get_score())  # 重设置分数
    
        # 创建一个frame窗口，此创建将容纳全部的widget 部件
        frame = Frame(root, bg=game_bg_color)
        frame.grid(sticky=N + E + W + S)
        # 设置焦点能接收按键事件
        frame.focus_set()
        frame.bind("<Key>", on_key_down)
    
        # 初始化图形界面
        map_labels = []
        for r in range(4):
            row = []
            for c in range(len(_map_data[0])):
                value = _map_data[r][c]
                text = str(value) if value else ''
                label = Label(frame, text=text, width=4, height=2,
                              font=("黑体", 30, "bold"))
                label.grid(row=r, column=c, padx=5, pady=5, sticky=N + E + W + S)
                row.append(label)
            map_labels.append(row)
    
        # 设置显示分数的Lable
        label = Label(frame, text='分数', font=("黑体", 30, "bold"),
                      bg="#bbada0", fg="#eee4da")
        label.grid(row=4, column=0, padx=5, pady=5)
        label_score = Label(frame, text='0', font=("黑体", 30, "bold"),
                            bg="#bbada0", fg="#ffffff")
        label_score.grid(row=4, columnspan=2, column=1, padx=5, pady=5)
    
        # 以下设置重新开始按钮
        def reset_game():
            reset()
            update_ui()
    
        restart_button = Button(frame, text='重新开始', font=("黑体", 16, "bold"),
                                bg="#8f7a66", fg="#f9f6f2", command=reset_game)
        restart_button.grid(row=4, column=3, padx=5, pady=5)
    
        update_ui()  # 更新界面
    
        root.mainloop()  # 进入tkinter主事件循环
    
    
    main()  # 启动游戏
def 计算器():
    import math
    
    
    class calculator():
    
        def __init__(self):
            global tk
            tk = Tk()  # 注意不能用self = Tk(),相当于将子类重新赋值了
            tk.geometry('480x500')
            tk.title('计算器')
    
            show = Frame(width=600, height=300, bg='#dddddd')
            show.pack()
            self.sv = StringVar()
            self.sv.set('初始状态')
    
            show_label = Label(show, textvariable=self.sv, bg='#eeeeee', width=34, height=4,
                               font=('黑体', 18, 'bold',), justify=LEFT, anchor='e')
            show_label.pack(padx=10, pady=10)
    
            k_area = Frame(width=600, height=350, bg='#cccccc')
            k_area.pack()
    
            # 数据初始化
            self.num1 = ''
            self.num2 = ''
            self.pms1 = []
            self.pms2 = []
            self.num1_list = []
            self.num2_list = []
            self.operat = []
    
            w = 5
            h = 1
    
            key_1 = Button(k_area, text='1', width=w, height=h, command=lambda: self.num_in('1'),
                           bg='yellow', font=('黑体', 30, 'bold'))
            key_1.grid(row=1, column=0)
    
            key_2 = Button(k_area, text='2', width=w, height=h, command=lambda: self.num_in('2'),
                           bg='yellow', font=('黑体', 30, 'bold'))
            key_2.grid(row=1, column=1)
    
            key_3 = Button(k_area, text='3', width=w, height=h, command=lambda: self.num_in('3'),
                           bg='yellow', font=('黑体', 30, 'bold'))
            key_3.grid(row=1, column=2)
    
            key_4 = Button(k_area, text='4', width=w, height=h, command=lambda: self.num_in('4'),
                           bg='yellow', font=('黑体', 30, 'bold'))
            key_4.grid(row=2, column=0)
    
            key_5 = Button(k_area, text='5', width=w, height=h, command=lambda: self.num_in('5'),
                           bg='yellow', font=('黑体', 30, 'bold'))
            key_5.grid(row=2, column=1)
    
            key_6 = Button(k_area, text='6', width=w, height=h, command=lambda: self.num_in('6'),
                           bg='yellow', font=('黑体', 30, 'bold'))
            key_6.grid(row=2, column=2)
    
            key_7 = Button(k_area, text='7', width=w, height=h, command=lambda: self.num_in('7'),
                           bg='yellow', font=('黑体', 30, 'bold'))
            key_7.grid(row=3, column=0)
    
            key_8 = Button(k_area, text='8', width=w, height=h, command=lambda: self.num_in('8'),
                           bg='yellow', font=('黑体', 30, 'bold'))
            key_8.grid(row=3, column=1)
    
            key_9 = Button(k_area, text='9', width=w, height=h, command=lambda: self.num_in('9'),
                           bg='yellow', font=('黑体', 30, 'bold'))
            key_9.grid(row=3, column=2)
    
            key_0 = Button(k_area, text='0', width=w, height=h, command=lambda: self.num_in('0'),
                           bg='yellow', font=('黑体', 30, 'bold'))
            key_0.grid(row=4, column=1)
    
            key_point = Button(k_area, text='.', width=w, height=h, command=lambda: self.num_in('.'),
                               bg='yellow', font=('黑体', 30, 'bold'))
            key_point.grid(row=4, column=2)
    
            key_pms = Button(k_area, text='±', width=w, height=h, command=self.pms,
                             bg='yellow', font=('黑体', 30, 'bold'))
            key_pms.grid(row=3, column=3)
    
            key_close = Button(k_area, text='Close', width=w, height=h, bg='red', command=self.close,
                               font=('黑体', 30, 'bold'))
            key_close.grid(row=4, column=0)
    
            key_plus = Button(k_area, text='+', width=w, height=h, command=lambda: self.operat_in('+'),
                              bg='yellow', font=('黑体', 30, 'bold'))
            key_plus.grid(row=1, column=3)
    
            key_minus = Button(k_area, text='-', width=w, height=h, command=lambda: self.operat_in('-'),
                               bg='yellow', font=('黑体', 30, 'bold'))
            key_minus.grid(row=2, column=3)
    
            key_multiply = Button(k_area, text='x', width=w, height=h, command=lambda: self.operat_in('x'),
                                  bg='yellow', font=('黑体', 30, 'bold'))
            key_multiply.grid(row=0, column=2)
    
            key_divide = Button(k_area, text='÷', width=w, height=h, command=lambda: self.operat_in('÷'),
                                bg='yellow', font=('黑体', 30, 'bold'))
            key_divide.grid(row=0, column=1)
    
            key_equal = Button(k_area, text='=', width=w, height=h, command=self.result,
                               bg='yellow', font=('黑体', 30, 'bold'))
            key_equal.grid(row=4, column=3)
    
            key_c = Button(k_area, text='Clear', width=w, height=h, command=self.data_empty,
                           bg='yellow', font=('黑体', 30, 'bold'))
            key_c.grid(row=0, column=0)
    
            key_del = Button(k_area, text='←', width=w, height=h, command=self.str_delete,
                             bg='yellow', font=('黑体', 30, 'bold'))
            key_del.grid(row=0, column=3)
    
            tk.mainloop()
    
        def pms(self):
            if self.operat == []:
                self.num1_pms()
            else:
                self.num2_pms()
    
        def num1_pms(self):
            if self.pms1 == []:
                self.pms1 = ['-']
                self.sv.set(self.pms1 + self.num1_list + self.operat + self.pms2 + self.num2_list)
            else:
                self.pms1 = []
                self.sv.set(self.pms1 + self.num1_list + self.operat + self.pms2 + self.num2_list)
    
        def num2_pms(self):
            if self.pms2 == []:
                self.pms2 = ['-']
                self.sv.set(self.pms1 + self.num1_list + self.operat + self.pms2 + self.num2_list)
            else:
                self.pms2 = []
                self.sv.set(self.pms1 + self.num1_list + self.operat + self.pms2 + self.num2_list)
    
        def num_in(self, n):
            if self.operat == []:
                self.num1_in(n)
            else:
                self.num2_in(n)
    
        def num1_in(self, n):
            if n == '.' and n in self.num1_list:
                pass
            else:
                self.num1_list.append(n)
                self.sv.set(self.pms1 + self.num1_list + self.operat + self.pms2 + self.num2_list)
    
        def num2_in(self, n):
            if n == '.' and n in self.num2_list:
                pass
            else:
                self.num2_list.append(n)
                self.sv.set(self.pms1 + self.num1_list + self.operat + self.pms2 + self.num2_list)
    
        def operat_in(self, op):
            if self.num1_list == [] or self.num1_list == ['.']:
                pass
            else:
                if self.operat == []:
                    self.operat.append(op)
                    self.sv.set(self.pms1 + self.num1_list + self.operat + self.pms2 + self.num2_list)
                else:
                    pass
    
        def data_empty(self):
            self.num1 = ''
            self.num2 = ''
            self.pms1 = []
            self.pms2 = []
            self.num1_list = []
            self.num2_list = []
            self.operat = []
            self.sv.set(self.pms1 + self.num1_list + self.operat + self.pms2 + self.num2_list)
    
        def str_delete(self):
            if self.num2_list != []:
                l = len(self.num2_list)
                self.num2_list.remove(self.num2_list[l - 1])
                self.sv.set(self.pms1 + self.num1_list + self.operat + self.pms2 + self.num2_list)
            elif self.num2_list == [] and self.pms2 != []:
                self.pms2 = []
                self.sv.set(self.pms1 + self.num1_list + self.operat + self.pms2 + self.num2_list)
            elif self.num2_list == [] and self.pms2 == [] and self.operat != []:
                self.operat = []
                self.sv.set(self.pms1 + self.num1_list + self.operat + self.pms2 + self.num2_list)
            elif self.operat == [] and self.num1_list != []:
                l = len(self.num1_list)
                self.num1_list.remove(self.num1_list[l - 1])
                self.sv.set(self.pms1 + self.num1_list + self.operat + self.pms2 + self.num2_list)
            elif self.num1_list == [] and self.pms1 != []:
                self.pms1 = []
                self.sv.set(self.pms1 + self.num1_list + self.operat + self.pms2 + self.num2_list)
            else:
                pass
    
        def num_pro(self, n):
            if n == self.num1:
                if self.pms1 != []:
                    self.num1 = self.pms1[0]
                else:
                    self.num1 = ''
                for i in self.num1_list:
                    self.num1 += i
                if '.' in self.num1_list:
                    self.num1 = float(self.num1)
                else:
                    self.num1 = int(self.num1)
            else:
                if self.pms2 != []:
                    self.num2 = self.pms2[0]
                else:
                    self.num2 = ''
                for i in self.num2_list:
                    self.num2 += i
                if '.' in self.num2_list:
                    self.num2 = float(self.num2)
                else:
                    self.num2 = int(self.num2)
    
        def result(self):
    
            if self.num2_list == [] or self.num2_list == ['.']:
                pass
    
            else:
                self.num_pro(self.num1)
                self.num_pro(self.num2)
                if self.operat == ['+']:
                    r = self.num1 + self.num2
                    self.data_empty()
                    self.num1_list = list(str(r))
                    self.sv.set(self.pms1 + self.num1_list + self.operat + self.pms2 + self.num2_list)
    
                elif self.operat == ['-']:
                    r = self.num1 - self.num2
                    self.data_empty()
                    self.num1_list = list(str(r))
                    self.sv.set(self.pms1 + self.num1_list + self.operat + self.pms2 + self.num2_list)
    
                elif self.operat == ['x']:
                    r = self.num1 * self.num2
                    self.data_empty()
                    self.num1_list = list(str(r))
                    self.sv.set(self.pms1 + self.num1_list + self.operat + self.pms2 + self.num2_list)
    
                elif self.operat == ['÷']:
                    try:
                        r = self.num1 / self.num2
                        self.data_empty()
                        self.num1_list = list(str(r))
                        self.sv.set(self.pms1 + self.num1_list + self.operat + self.pms2 + self.num2_list)
                    except ZeroDivisionError:
                        self.sv.set('除数不能为0')
                    except Exception:
                        pass
    
        def close(self):
            tk.destroy()
    
    if __name__ == '__main__':
        cc = calculator()
from tkinter.messagebox import *
def 五子棋():
    class Chess(object):
     
     def __init__(self):
      #############
      # param #
      #######################################
      self.row, self.column = 15, 15
      self.mesh = 25
      self.ratio = 0.9
      self.board_color = "#CDBA96"
      self.header_bg = "#CDC0B0"
      self.btn_font = ("黑体", 12, "bold")
      self.step = self.mesh / 2
      self.chess_r = self.step * self.ratio
      self.point_r = self.step * 0.2
      self.matrix = [[0 for y in range(self.column)] for x in range(self.row)]
      self.is_start = False
      self.is_black = True
      self.last_p = None
     
      ###########
      # GUI #
      #######################################
      self.root = Tk()
      self.root.title("Gobang By Young")
      self.root.resizable(width=False, height=False)
     
      self.f_header = Frame(self.root, highlightthickness=0, bg=self.header_bg)
      self.f_header.pack(fill=BOTH, ipadx=10)
     
      self.b_start = Button(self.f_header, text="开始", command=self.bf_start, font=self.btn_font)
      self.b_restart = Button(self.f_header, text="重来", command=self.bf_restart, state=DISABLED, font=self.btn_font)
      self.l_info = Label(self.f_header, text="未开始", bg=self.header_bg, font=("楷体", 18, "bold"), fg="white")
      self.b_regret = Button(self.f_header, text="悔棋", command=self.bf_regret, state=DISABLED, font=self.btn_font)
      self.b_lose = Button(self.f_header, text="认输", command=self.bf_lose, state=DISABLED, font=self.btn_font)
     
      self.b_start.pack(side=LEFT, padx=20)
      self.b_restart.pack(side=LEFT)
      self.l_info.pack(side=LEFT, expand=YES, fill=BOTH, pady=10)
      self.b_lose.pack(side=RIGHT, padx=20)
      self.b_regret.pack(side=RIGHT)
     
      self.c_chess = Canvas(self.root, bg=self.board_color, width=(self.column + 1) * self.mesh,
            height=(self.row + 1) * self.mesh, highlightthickness=0)
      self.draw_board()
      self.c_chess.bind("<Button-1>", self.cf_board)
      self.c_chess.pack()
     
      self.root.mainloop()
     
     # 画x行y列处的网格
     def draw_mesh(self, x, y):
      # 一个倍率，由于tkinter操蛋的GUI，如果不加倍率，悔棋的时候会有一点痕迹，可以试试把这个改为1，就可以看到
      ratio = (1 - self.ratio) * 0.99 + 1
      center_x, center_y = self.mesh * (x + 1), self.mesh * (y + 1)
      # 先画背景色
      self.c_chess.create_rectangle(center_y - self.step, center_x - self.step,
              center_y + self.step, center_x + self.step,
              fill=self.board_color, outline=self.board_color)
      # 再画网格线，这里面a b c d是不同的系数，根据x,y不同位置确定，需要一定推导。
      a, b = [0, ratio] if y == 0 else [-ratio, 0] if y == self.row - 1 else [-ratio, ratio]
      c, d = [0, ratio] if x == 0 else [-ratio, 0] if x == self.column - 1 else [-ratio, ratio]
      self.c_chess.create_line(center_y + a * self.step, center_x, center_y + b * self.step, center_x)
      self.c_chess.create_line(center_y, center_x + c * self.step, center_y, center_x + d * self.step)
     
      # 有一些特殊的点要画小黑点
      if ((x == 3 or x == 11) and (y == 3 or y == 11)) or (x == 7 and y == 7):
       self.c_chess.create_oval(center_y - self.point_r, center_x - self.point_r,
              center_y + self.point_r, center_x + self.point_r, fill="black")
     
     # 画x行y列处的棋子，color指定棋子颜色
     def draw_chess(self, x, y, color):
      center_x, center_y = self.mesh * (x + 1), self.mesh * (y + 1)
      # 就是画个圆
      self.c_chess.create_oval(center_y - self.chess_r, center_x - self.chess_r,
             center_y + self.chess_r, center_x + self.chess_r,
             fill=color)
     
     # 画整个棋盘
     def draw_board(self):
      [self.draw_mesh(x, y) for y in range(self.column) for x in range(self.row)]
     
     # 在正中间显示文字
     def center_show(self, text):
      width, height = int(self.c_chess['width']), int(self.c_chess['height'])
      self.c_chess.create_text(int(width / 2), int(height / 2), text=text, font=("黑体", 30, "bold"), fill="red")
     
     # 开始的时候设置各个组件，变量的状态，初始化matrix矩阵，初始化棋盘，初始化信息
     def bf_start(self):
      self.set_btn_state("start")
      self.is_start = True
      self.is_black = True
      self.matrix = [[0 for y in range(self.column)] for x in range(self.row)]
      self.draw_board()
      self.l_info.config(text="黑方下棋")
     
     # 重来跟开始的效果一样
     def bf_restart(self):
      self.bf_start()
     
     # 用last_p来标识上一步的位置。先用网格覆盖掉棋子，操作相应的变量，matrix[x][y]要置空，只能悔一次棋
     def bf_regret(self):
      if not self.last_p:
       showinfo("提示", "现在不能悔棋")
       return
      x, y = self.last_p
      self.draw_mesh(x, y)
      self.matrix[x][y] = 0
      self.last_p = None
      self.trans_identify()
     
     # 几个状态改变，还有显示文字，没什么说的
     def bf_lose(self):
      self.set_btn_state("init")
      self.is_start = False
      text = self.ternary_operator("黑方认输", "白方认输")
      self.l_info.config(text=text)
      self.center_show("蔡")
     
     # Canvas的click事件
     def cf_board(self, e):
      # 找到离点击点最近的坐标
      x, y = int((e.y - self.step) / self.mesh), int((e.x - self.step) / self.mesh)
      # 找到该坐标的中心点位置
      center_x, center_y = self.mesh * (x + 1), self.mesh * (y + 1)
      # 计算点击点到中心的距离
      distance = ((center_x - e.y) ** 2 + (center_y - e.x) ** 2) ** 0.5
      # 如果距离不在规定的圆内，退出//如果这个位置已经有棋子，退出//如果游戏还没开始，退出
      if distance > self.step * 0.95 or self.matrix[x][y] != 0 or not self.is_start:
       return
      # 此时棋子的颜色，和matrix中该棋子的标识。
      color = self.ternary_operator("black", "white")
      tag = self.ternary_operator(1, -1)
      # 先画棋子，在修改matrix相应点的值，用last_p记录本次操作点
      self.draw_chess(x, y, color)
      self.matrix[x][y] = tag
      self.last_p = [x, y]
      # 如果赢了，则游戏结束，修改状态，中心显示某方获胜
      if self.is_win(x, y, tag):
       self.is_start = False
       self.set_btn_state("init")
       text = self.ternary_operator("黑方获胜", "白方获胜")
       self.center_show(text)
       return
      # 如果游戏继续，则交换棋手
      self.trans_identify()
     
     def is_win(self, x, y, tag):
      # 获取斜方向的列表
      def direction(i, j, di, dj, row, column, matrix):
       temp = []
       while 0 <= i < row and 0 <= j < column:
        i, j = i + di, j + dj
       i, j = i - di, j - dj
       while 0 <= i < row and 0 <= j < column:
        temp.append(matrix[i][j])
        i, j = i - di, j - dj
       return temp
     
      four_direction = []
      # 获取水平和竖直方向的列表
      four_direction.append([self.matrix[i][y] for i in range(self.row)])
      four_direction.append([self.matrix[x][j] for j in range(self.column)])
      # 获取斜方向的列表
      four_direction.append(direction(x, y, 1, 1, self.row, self.column, self.matrix))
      four_direction.append(direction(x, y, 1, -1, self.row, self.column, self.matrix))
     
      # 一一查看这四个方向，有没有满足五子连珠
      for v_list in four_direction:
       count = 0
       for v in v_list:
        if v == tag:
         count += 1
         if count == 5:
          return True
        else:
         count = 0
      return False
     
     # 设置四个按钮是否可以点击
     def set_btn_state(self, state):
      state_list = [NORMAL, DISABLED, DISABLED, DISABLED] if state == "init" else [DISABLED, NORMAL, NORMAL, NORMAL]
      self.b_start.config(state=state_list[0])
      self.b_restart.config(state=state_list[1])
      self.b_regret.config(state=state_list[2])
      self.b_lose.config(state=state_list[3])
     
     # 因为有很多和self.black相关的三元操作，所以就提取出来
     def ternary_operator(self, true, false):
      return true if self.is_black else false
     
     # 交换棋手
     def trans_identify(self):
      self.is_black = not self.is_black
      text = self.ternary_operator("黑方下棋", "白方下棋")
      self.l_info.config(text=text)
     
     
    if __name__ == '__main__':
     Chess()
root = tkinter.Tk()
root.geometry("500x750")
root.title("随堂测")
root.resizable(False,False)
word = tkinter.Label(root,text = "创意随堂测",font = ("kaiti",70))
word.pack()
word1 = tkinter.Label(root,text = "给大敏",font = ("kaiti",20))
word1.pack()
button1 = tkinter.Button(root,text = "脑筋急转弯快乐机器", command=脑筋急转弯快乐机器)
button1.pack()     
button2 = tkinter.Button(root,text = "五子棋", command=五子棋)
button2.pack()     
button3 = tkinter.Button(root,text = "游戏2048(上下左右键控制)", command=游戏2048)
button3.pack()     
button1 = tkinter.Button(root,text = "计算器", command=计算器)
button1.pack()     
root.mainloop()