text = '''insjhx语言更新日志
temp-0:2019/1 终端输入什么，就会输出什么 while 1:print(input())
temp-1 指定语言回复
aip-sp:2019/4 嵌套分支式回复
aip-sp2 改进成+-计算器
aip-sp3 添加*
aip-sp4:2019/5 添加/
mdl-aip:2019/6 结合各种小游戏，改进为《时光机》
aip-sp5:2019/10 添加平方根（pid 2515310）
aip-sp6:2019/12 添加除0错误
2020/1 弃坑

aip-sp7:2021/7 py编辑器
aip-sp8:2021/8 宇宙计算器
aip-sp9 windows cmd

0.-1:2022/8 开创insjhx语言，加入in和out代替print和input
0.0 使用类代替 pid=36310546
0.0s 优化算法，将字典改为列表，简化储存方式，精简类
V0.1 build 30 扩展关键词，区分类型：out in int str list cut help db，创建数据库
V0.1 build 36 添加除错机制，修复少量bug，pid=36670802，修改提示符ins:>为ins:
(ins可以理解为insjhx/install/insert/inscript/ink sans(这不是玩的吗)，一语多关)
V0.2 build 45 可以使用变量、双重变量承接，错误机制升级，增多指令，增加var/vars
V0.3 build 60 支持py混合
V0.3+ build 75 支持记录py
V0.4 build 94 支持开放pydb，$!enddo!$结束返回
V0.4+ build 100:2022/9 重新支持space，修复一些bug，pid=36798383
V0.3reverse build 135 重置版，重写了一部分内容，提高可读性，添加一些常量，修复大量bug，增加calc,calc-ex，提示符改回ins:>
V0.5+ build 176 添加了多层控制，比如var a = int str int '666'然后out a*2，同时修复少量bug，增加keywords字典，增加命名空间，开始写更新日志及问询、版本问询、清屏cs
V0.4reverse build 180 添加CONSTS列表，改变提示符为ins>，正式命名“$!!$”为高级指令
V0.5+ build 188 添加$!exit!$指令，添加结束语，添加runner状态
V0.5+ build 196 添加不用var直接space a=1或者a=1都行，同时去掉无用空格输出(不能支持a=3)
V0.5reverse build 203 space、OutWarn汇聚成一个情况，修改空格输出，支持输入15/1 5/a = 3
V0.5+ build 221 space、OutWarn修改回去，但是多功能，可以调控普通/严格模式，增加关键字cfg，同时增加退出指令$!exit!$
outversion 括号表达式1.0:2022/9/24 正则算括号
outversion 括号表达式1.1 踢掉正则，自家算法算括号
outversion 括号表达式1.2 改进多层括号
outversion 括号表达式1.3 改进多个括号
outversion 括号表达式2.0 改进半个括号引发错误
outversion 括号表达式2.1 改进引号内括号不算括号
outversion 括号表达式2.2 改进括号层级
outversion 括号表达式2.3 避免索引多算
outversion 括号表达式3.0 完善
V0.5+ build 222 增加parse类
outversion 括号表达式3.1 封装进parse
V0.5+ build 260 parse类完善，增加self和cls的区别，添加一堆复杂的处理，parse与后面复杂处理表达式衔接
V0.5+ build 263 复杂处理表达式出错，减掉多出的一个索引，更改半个括号错误机制
V0.5+ build 271 自动区分tuple和括号，分解函数完成
V0.5+ build 276 严格模式禁止out str 666，应改为out (str 666)，其他模式则可以用第一种方法
V0.6 build 277 ins>改为ins>>
V0.6 build 279 整理代码，添加repr
V0.6 build 286 添加find功能，改进index功能
V0.6 build 291 添加change功能，改进index、find功能到1行，删除无用代码，空行，增高可读性
V0.6 build 300 添加add,del功能，把outerror细化一些
V0.6 build 316 添加多行运行类，为if/for做准备
V0.6 build 318 el改成endl(有c那味了)
V0.6 build 342:2022/10/1 if检测，indent决定变量与pool定义，识别条件语句以及缩进，parse添加must_indent
V0.6 build 368 完善if检测，去掉注释在if中的占位错误，区分多行代码与缩进，添加非严格模式变量识别进if
V0.6 build 371 变量名不能以数字开头，cfg加限制
V0.6 build 400 完全支持if语句以及板块运行
V0.6 build 406 if语句后，修复a = 1被误识别报错的bug
V0.6 build 411 else特殊语义分析
V0.6 build 447 if-else完成
弃坑一段时间
V0.6 build 481 10/15 if-elif-else完成
V0.6 build 503 if-elif完成
V0.6reverse build 511 indentkeyword清空，修复条件语句bug
V0.6+ build 537 完善条件语句，防止elif双重误识别，可以实现：
                if if-elif if-else if-elif-else
                结构上：
                if 0
                elif 0
                elif 1
                elif -1
                ...
                else
V0.6+ build 542 indent标识符识别
V0.6+ build 546 增加range关键字，参数1个
'''