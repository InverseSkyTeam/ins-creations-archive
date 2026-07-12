read all of basic
read time

var name = in "输入你的名字"
out name
if name == '小轩' {
    out '欢迎大佬'
} else {
    out '欢迎新人'
}

*:下面的函数是time库里的，because和*:会被认作注释
*:调用语法 [函数名][*特殊表达式][*参数列表][*承接表达式][*语法注释][*语言注释]
*:带*表示可以没有
wait 1 second because I am so happy

fun calc [n1=6,n2=1] (t1->if n2 is 6 stop;t2->if n1 is 100 stop;) {
    if n1 == 6 {
        ret n1*n2
    } elif n1 == 0 {
        ret n1+n2
    } else {
        out n1+n2 'not gald' because that's bad -_- ...
    }
    out 'ok'
    try {
        ret n1/n2
    } except {
        out 666 because it is cool!
    } else {
        out 111
    } finally {
        ret 'end.'
    }
}

out 'I know 6*3 is ' (calc n2=3) '.'
del t2 of calc
db add calc
del calc
db del db[0]

name = 'p'

class P [obj] {
    fun init ($ basic special) [self,value] {
        readin name
        self.value = value
        self.name = name
    }
    fun str ($ basic special) [self] {
        ret [self.value,self.name]
    }
    fun eat [self] {
        self.value++
    }
}

p = P 15
p eat
out (str p)

d = [1,2,3]
let p range d {out p}

for (i=1,i<=10,++i){
    out i;
}

out (from 1 to 10) because it is sampler than for-loop/let-loop/while-loop

out (sort [2,3,1] 'up')

struct hello{
    a = 1, b = 2, c = 3
}
fun outt (hello) [a,b] {
    out a b;
}

h = hello[]
h outt
out (c of h)
xxx



运行结果：
输入你的名字
[Stdin]:小轩
小轩
欢迎大佬
[System]:(等待一秒，不会输出)
I know 6*3 is 18.
[16,'p']
1
2
3
1
2
3
4
5
6
7
8
9
10
[1,2,3,4,5,6,7,8,9,10]
[1,2,3]
1 2
3
[System]:
    SysInfo:
        Error
    Message:
        Variable [xxx] is not defined.
    Ch-Message:
        变量[xxx]没有被定义，但在代码中出现。
    InfoLine:
        <Line 84>
    LineShow:
        84|xxx
           ^ [xxx] Not defined.
    Better Way:
        change [xxx].
        Way 1:
            84|because xxx
        Way 2:
            84|[var xxx = 1]
        Way 3:
            84|read math
            85|math xxcalc 1 1
    Others:
        Hope you can use insjhx well one day!
        by ins小轩
[System]:
    End with statu-code:
        [1,'Error']