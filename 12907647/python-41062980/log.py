[可能还有用的资料]
早期资料|自制解释器 https://zhuanlan.zhihu.com/p/377521560
临时资料|C语言运算优先级 https://blog.csdn.net/yuliying/article/details/72898132
临时资料|python语言运算优先级 https://blog.csdn.net/gongxiaxx/article/details/125236226
随意参考资料|python控制ast https://blog.csdn.net/u010786109/article/details/44832301

[简写]
新骗局简写: ĳ lJ lj Ĳ
正确的简写: ij

[等级编号]
Lv.0 Air                  O 1.0 start
Lv.1 Cell                 | 1.0 build 100 (1 to 100)
Lv.2 Bacteria             | 0.0 build 200
Lv.3 Ant                  | 0.0 build 300
Lv.4 Cake                 | 0.0 build 450
Lv.5 Paper                  0.0 build 500
Lv.6 Pen                    0.0 build 680
Lv.7 ButterflyX             0.0 build 1000
Lv.8 Bee                    0.0 build 1200
Lv.9 Pragonfly              0.0 build 1400
Lv.10 StringCotton          0.0 build 1500
Lv.11 DictBottle            0.0 build dev-note
Lv.12 Intplate              0.0 build 1800
Lv.13 FInteger--            0.0 build 2023
Lv.14 IntegerX              0.0 build 2600
Lv.15 Elephant              0.0 build 3000
Lv.16 Dragon                0.0 build 3500
Lv.17 Plane                 0.0 build 3700
Lv.18 Universe              0.0 build pre
Lv.19 L03                   0.0 build 4500
Lv.20 CBlock                0.0 build 5000
Lv.21 Javaprec              0.0 build 6000
Lv.22 Python++              0.0 build 8000
Lv.23 Cking                 0.0 build 9000
Lv.24 NightCommon           0.0 build dev-note2
Lv.25 insjhx                0.0 build 10000
Lv.26 insjhx-plus           0.0 build plus
Lv.27 insjhx script ++      0.0 build 12000
Lv.28 inspace               0.0 build 15000
Lv.29 UniverseMaster        0.0 build 20000
Lv.30 Linkall               0.0 build 30000
Top.i DreamSky              0.0 build 100000

[比较]
10^(3*10^6)个2组合成的大数字
py     1.40s
ij     1.51s
i32    1.68s
df1.8  7.21s

10^(5*10^6)个2组合成的大数字
py     4.21s
ij     4.53s
i32    12.89s
df1.8  63.40s

10^(7*10^6)个2组合成的大数字
py     8.54s
ij     9.002s
i32    48.71s
df1.8  *s(未能在100s内正常运行出结果)

((((()括号递归300层()))))
py     栈内存错误 s_push: parser stack overflow
ij     0.89s
i32    递归限制错误
df1.8  递归限制错误

[强度测试样例]
1
> ((a) = (111)) (if) (((a)-110)()((666)()()))()()() {if true{((a)=(6))}} (666)()()
> out a
< 6

2
> a b = b a (a=1) (b=2)
> out a b
> swap a b (a=1) (b=2)
> out a b
< 2 2
< 2 1

3
> a=1 if true {if a {if a {if a {if a {if a {if a {if a {if a {if a {a=6}}}}}}}}}}
> out a
< 6

4
>  a = true (c=null)
> b d = a+a c
> a = 1
> ()()()()()()()()()()()()()()()()e=1+1
> ()()f((())())=(())e()(())(((()()(())((())))())())(()())+(())e()()()
> age = 3
> if age < 10 {
>     age = 10
>     if false {
>         age = 1000
>     } elif (age>100) {
>         age = 0
>     } else {
>         age = age + 3
>     } if age > 10 {
>         age = age + 2
>     }
> }
> out c age e
< null 15 2

5
> a=1.2
> l = 0
> while a {
>     while a<10 {
>         a = a + 1
>     }
>     l += 1
>     a = a + 1
>     if a>=30 {
>         break
>     }
> }
> out a l
< 30 20
