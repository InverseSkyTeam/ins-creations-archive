---
title: 一些好用的Python标准库
tags:
  - 编程语言
  - Python
  - 类库
categories:
  - Python
  - 标准库
abbrlink: 33721
date: 2022-08-16 23:20:36
---

# 前言

Python作为一门简洁优美、功能强大的脚本语言，很多实用的函数和功能都无需安装三方库或自己实现，在Python内置的标准库中就有不少很实用但知道的人不多的标准库，今天就分享一些，希望能帮到大家。

# itertools

## 介绍

itertools是一个用于快速生成各种迭代的标准库，它为一些需要枚举、遍历的场合提供了一种简单而高性能的迭代方式。

## 调用示例：

```python
import itertools # 导入itertools库

itertools.permutations('abcde') # 生成abcde的所有组合
itertools.combinations('abcde', 3) # 在abcde中选3个的所有组合
itertools.product('abcde', '123') # 生成abcde与123的笛卡尔积
itertools.cycle(('a', 'b', 'c')) # 生成abcde的无限循环队列
```

## 注意事项

这些函数返回的不是常见的列表和元组，而是迭代器，可以直接遍历，效率更高，当然你也可以使用`list()` 函数来进行转换。

# glob

## 介绍

glob库用于从目录通配符搜索中生成文件列表，简单来说就是可以根据你给出的表达式在当前下搜索文件，有了它，你自己也可以写一个文件搜索工具。

## glob方法

调用示例：

```python
import glob
glob.glob("*.py") # 获取当前目录下所有后缀为.py的文件列表
```

这里的 ***.py** 叫做通配符，形式类似正则表达式，使用特殊的字符来匹配制定的字符。

glob的通配符语法如下：

![](https://jihulab.com/wuyuhangxyz/picturebed/-/raw/main/pictures/2022/08/16_23_39_5_20220816233904.png)

这里面其它的不多说了，对正则有了解的应该会觉得比较熟悉，重点介绍一下 ****** 这个通配符，原先的匹配是无法深入到子目录中去的，但是使用 ****** 搭配另外一个参数 `recursive=True`就可以实现这个效果，示例代码如下：

```python
import glob
glob.glob("**/*.py",recursive=True) # 此处的**/用于指定深入所有子目录
```

## iglob方法

iglob使用方法与glob函数并无二异，只是glob方法返回一个列表，而iglob方法返回一个**generator(译作迭代器或生成器)** ，遍历效率更高，在文件很多的时候可以使用。

# timeit

timeit使用起来简单粗暴，就是用于计算一段代码的运行时间。

```python
import timeit
timeit.repeat("print(1)",number=1) # number参数为执行次数
```

通过上述代码我们计算了执行一次 **print(1)** 代码的时间，如果我们想要计算执行10000次的时间，只需将number参数改为10000即可。

但是真正的计算时间没有这么简单，电脑永远都有其他程序也在占用着资源，你的程序不可能最高效的执行，所以一般我们都会尝试多次，以求得更加精准。这在timeit中也很容易实现。

```python
import timeit
timeit.repeat("print(1)",number=1,repeat=5)
```

此示例将测试5次 **print(1)** 这段代码的时间，并取最小的一次时间作为返回值。

## 注意事项

timeit函数的number参数默认为1000000，这显然不太合理，所以一般我们都会进行修改。

# heapq

## 介绍

`heapq`模块实现了堆排序算法，如果希望使用堆排序，尤其是要解决**TopK问题**（从序列中找到K个最大或最小元素），直接使用该模块即可。

## 示例代码

```python
import heapq

l = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
print(heapq.nlargest(3, l)) # 找出l中最大的三个元素
print(heapq.nsmallest(3, l)) # 找出l中最小的三个元素
```

这非常简单且容易理解，几乎不用我解释了。

# 总结

这些Python标准库平时都用的不多，但是在某个特定场合却能起到大用处，希望能够帮到你们。
