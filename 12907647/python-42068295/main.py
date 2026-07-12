print('''ij语言创作弃坑了。
读入、解析、运行三者性能只能选其一，但是总时间一直平衡无法突破
也就是说我一百个小时创想的新型语言结构破灭了，一共20多种，试过一些，有几种达到和传统结构差不多，但就是无法超越
《一直被模仿，从未被超越》
既然ij无法超过c++、python这样的语言，索性我放弃了，压力给到其他语言创造者

接下来描述我的理想语言：
1.比python好用，亲切，人性化，有一定智能的语言，接近自然语言，容错性强，但是也能显示warn和error
2.突破一些限制：递归、lexer限制，如一亿层括号也能执行，百万层作用域和递归也可以
3.效率接近c++，甚至超过
4.灵活性较高
等等

下面简单介绍一种我想象quoter数据结构，不知道有没有人能实现。可能不难，但是很麻烦:
a = `"hello"666 az +-*/`
a[4:6] = `"a"5`
<<现在a是`"hella"566 az +-*/`
1 a[10] 2
<<就是1+2，得3
del a[3:]
<<现在a是`"hel"`
list a
<<a=["hel"]

再写一个理想语言的样例:
a = 2
out (type of a)
b = 3 when a is 2
if b == 3 {
    a.son = b
    out (a, son of a)
} else {
    b.emmm = a
}
out (type of a)

cfg language "中文模式"
*:现在进入中文模式
a *= 2
a.son = 0
如果a的son的布尔值是false，*:那么:*删除a的son
输出a和a的类型
设置配置 语言 "English"

cfg get_info language *:可以使用help (cfg language)
a, b = b, a
del a, b
l = [1,2,3,4]
cycle l with each {
    l.append(each+4)
    out (each.index)
}
out l  *:可以是 out(l)

read all of time
out (now)
$ bye, my insjhx~

结果:
int(basic integer)
2 3
int(with special attr)
4 int(basic integer)
help------------
  how to use cfg language----------
    [use] cfg language s
    s is a string, it is the language you want.
    it can be:
      ·中文
      ·繁體中文
      ·古漢語
      ·English
      ·日本語
    Now you have these languages，you can go to (https://www.INSteam.com.cn/to_codes/insjhx/langpkgs) and download other language packages~
  tips-----------------
    [use] cfg get language
    to get language you are using.
end help------------
[1,2,3,4,5,6,7,8]
(输出了现在的时间对象)
(这是AI智能模式中的结束语)see you tomorrow~


恐怕起码要等到2050年才能看到这种有趣的语言了.
''')