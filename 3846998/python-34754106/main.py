print("请将屏幕拉到最大")
input("准备好了吗？")
print('''注意：
表达式均为中缀表达式
0、注释：
    和C++相同
1、Hello,world!程序及其解释：
	{//注意大括号是必须的
		import builtin;
		/*
		导入builtin模块（builtin模块中有一些必须的内置函数）
		注意行尾的分号是必须的
		*/
		println("Hello,world");
		/*
		调用println函数
		println是builtin模块中的函数
		格式：println(arg1,arg2...)
		会逐个输出传入的参数，并在行尾输出换行
		如果没有导入builtin模块就要写
		builtin::println("Hello,world!")
		*/
	}
2、模块（或类）：
    定义：
        module 模块名称{
            ...//可以是模块、函数、变量的定义
        }
    导入：
        import 模块名称;//分号不能少！
        注意：如果没导入模块调用模块内定义的函数（或变量、模块）就必须写
        模块名称::名称
        如果导入了就可以不写
    实例：
        实例是仅对于类的概念
        模块不能被实例化！
        语法：
        类名(...)
        会返回这个类的实例
        其余大部分内容都和Python和C++相似，自己摸索吧！
3、函数：
    定义：
        func 函数名(参数列表（和Python很像）){
            ...
        }
    调用：
        函数名(参数列表)
    对于函数和列表还有一个append_code语句，自己研究吧！
4、变量：
    定义：
        var 变量1(=表达式1),变量2(=表达式2)...;
        定义一堆变量
        并给它们赋初值（没有则为None）
    使用：
        直接用即可
    integer3支持列表和字典，自己去想吧！
5、分支结构：
    和C++一样，但不用加括号
    比如：
    if 0{
        builtin::println(0);
    }
    else if 1{
        builtin::println(1);
    }
    else{
        builtin::println(2);
    }
    输出是1
6、循环结构：
    （1）、for循环：
        for 语句1;条件;语句2{
            ...
        }
        和C++基本一样，但不能加括号
        比如：
        for var i=0;i<10;i=i+1{
            builtin::print(i);
        }
        会输出0123456789
    （2）、while循环：
        和C++一样，但不用加括号
    （3）、foreach循环：
        foreach 变量名 in 值{
            ...
        }
        比如：
        foreach i in [1,2,3]{
            builtin::print(i);
        }
        输出123
7、异常：
    （1）、抛出异常：
        throw(值)
        注意：throw是函数！必须有小括号！
    （2）、try-except结构：
        try{
            ...
        }
        except{
            ...
        }
        注意：except后面不能写任何东西
        执行顺序和python一样
8、示例代码：
    显然，刚刚那段空洞的教程并不能让人会用integer3
    所以，我将用实例解释
    代码：
    {//大括号不能省
        module Rectangle{//定义长方形类
            var length,width;//长和宽两个属性
            func __init__(length,width){//实例化方法
                this.length=length;
                this.width=width;
            }
            func circumference(){//周长方法
                return (this.length+this.width)*2;//周长=(长+宽)*2
            }
            func area(){//面积方法
                return this.length*this.width;//面积=长*宽
            }
        }
        func print_rectangle(rect){//输出长方形的长、宽、周长、面积
            import builtin;//建议在每个函数的第一行都加上这个
            println("该长方形的长是",rect.length,"，宽是",rect.width,"，周长是",rect.circumference(),"，面积是",rect.area(),"。");
        }
        import builtin;//导入builtin
        var rect=Rectangle(6,3);//rect是一个长6宽3的长方形实例
        print_rectangle(rect);//调用自定义函数
        rect.width=5;//将rect的宽度设为5
        print_rectangle(rect);//再次调用
    }
    输出：
    该长方形的长是6，宽是3，周长是18，面积是18。
    该长方形的长是6，宽是5，周长是22，面积是30。''')