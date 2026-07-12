---
title: Python常见报错代码
date: 2022-08-29 19:42:28
tags: [Python]
categories: [Code,Python,Python小技巧]
cover: https://jihulab.com/ZiXuanYuan/blogpic/-/raw/main/pictures/2022/08/23_22_5_46_002.webp
toc: true
comments: true
---

## 前言

- 在我们编写程序的时候，难免遇到报错，那这个时候有些人就去Baidu了，但是其实报错代码也是有迹可循的，看懂了报错代码就可以直接找到代码错误的根源
- 接下来我讲介绍常见的代码报错，
- 基本规律：会显示代码报错的行数，和这一行出现错误的具体位置，以及报错类型，一下我将仅针对报错的类型进行讲解

***

<!--more-->

## 缩进报错

- 报错代码
  
  ```Python
  IndentationError: expected an indented block
  ```
- 解决方案：
  根据摆错的行数确定缩进错误的行，直接进行调整就可以

***

## 语法错误

### 匹配错误

- 报错代码
  
  ```Python
  SyntaxError: unexpected EOF while parsing
  ```
- 解决方案：
  查看报错的那一行括号是否有缺漏，引号有没有缺漏、多行注释有没有缺漏

### 符号错误

- 报错代码
  
  ```Python
  File "C:\Users\dell\学而思直播\code\cache\asset\6/main.py", line 2
    if a=1:
        ^
  SyntaxError: invalid syntax
  ```

- 解决方案
  检查是否将== 写成= 把=写成==

***

## 变量名错误

- 报错代码
  
  ```Python
  line1, in <module>
    if a==1:
  NameError: name 'a' is not defined
  ```
- 解决方案：
  检查变量是否定义，在函数中的话检查是否标明为全局变量 即为global 全局变量名 #声明一个全局变量

### 变量命名规范

+ 只能是字母、下划线、和数字
+ 数字不能作为变量名的开头部分
+ 不能使用Python关键字，如print、input等

***

## 索引错误

- 报错代码
  
  ```Python
  Traceback (most recent call last):
  File "main.py", line 2, in <module>
    print(list[5])
  IndexError: list index out of range
  ```
- 解决方案：
  因为索引超过列表数量，所以检查是否索引是否过大或者过小(负索引)

## 文件查找错误

- 报错代码
  
  ```Python
  myImg = pygame.image.load("img1.png")
  FileNotFoundError: No file 'img1.png' found inworking directory
  ```
- 解决方案
  查看是否有这个文件，是否文件名拼写错误

## 类型错误

- 报错代码
  
  ```Python
  Traceback (most recent call last):
  File "main.py", line 1, in <module>
    print("123"+123)
  TypeError: must be str, not int
  ```

- 解决方案
  检查函数的每个参数的类型是否错误，不同变量不能相加

***

## 小结

有BUG并不可怕，仔细查看报错代码，仔细推敲就可以修复

***