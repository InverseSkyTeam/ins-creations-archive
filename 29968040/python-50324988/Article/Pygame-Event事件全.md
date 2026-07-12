---
title: Pygame.Event事件全解
date: 2023-01-07 21:35:38
tags: [Code,Python,Pygame,Event]
categories: [Code,Python,Pygame,Event事件检测]
cover: https://jihulab.com/ZiXuanYuan/blogpic/-/raw/main/pictures/2022/08/17_16_39_43_tit3.svg
toc: true
comments: true
---

# 前言
本文整理了pygame中的各种事件
以下本文讲述的事件类型列表，如能帮助到你，请关注一下我

<!-- more -->

# 事件基础

### 一切的基石
- 一切的基础在于这个函数 **pygame.event.get()** 它的返回值是一个事件列表，而想要获得事件，就需要遍历这个列表，即
```` Python
for event in pygame.event.get():
    if eventA :
        ...
    elif eventB:
        ...
````
- 之后我们再来看一下每一个event
![alt 加载失败](https://jihulab.com/ZiXuanYuan/blogpic/-/raw/main/pictures/2023/01/17_12_42_19_%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20230117123624.png)

- 可以发现，每一个事件都有一个属性，叫type，这是事件的类型，而想要判断事件的发生，只需要知道每种事件的类型就好，这在pygame库中有对应的变量
- 如 最常见的退出事件 Quit 事件编号是256 可以用pygame.QUIT 获取到这个数字，那么检测事件的方法就很明确了。

```` Python
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
````

### 工作原理
Event说白了就是一个类，这个类里面好像是一个自动会储存信息，但有些还是没有储存的
一共有几万个事件，当然不能一一罗列，这边只挑选经常用上的事件

***

# 事件类型

**接下来列举事件类型**
**注意，以下所有时间调用时应该所有字母大写，以pygame.事件名调用**

> ### **QUIT 退出事件**

+ 代码：256
+ 目的：检测窗口的关闭按钮是否按下
+ 内置其他数据：{}，即无其他数据
+ 应该做：如果发生，应该关闭窗口
+ 代码示例：
```` Python 
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
````

***

> ### **Windows 窗口事件**

#### **WindowMinimized 最小化事件**
+ 代码：32780
+ 目的：检测窗口最小化按钮是否被按下
+ 内置其它数据 : WindowMinimized {'window': None} 目前我也不知道是干什么的
+ 应该做：这个要看写代码目的，因此没有代码示例

#### **WindowExposed 打开窗口事件**
+ 代码：32776
+ 内置其它数据 : WindowExposed {'window': None} 目前我也不知道是干什么的
+ 应该做：这个要看写代码目的，因此没有代码示例

#### **WindowMoved 窗口移动事件**
+ 代码：32777
+ 内置数据：x、y即为窗口移动到的整个电脑的坐标系

    ```` Python
    WindowMoved {'x': 724, 'y': 128, 'window': None} 
    ````

+ 应该做：这个要看写代码目的，因此没有代码示例

#### **WindowFocusLost 窗口被遮挡事件**
+ 代码：32786
+ 内置数据：WindowFocusLost {'window': None} 

#### **WindowLeave 鼠标离开窗口**
+ 代码：32784
+ 内置数据：WindowLeave {'window': None}

***

> ### **Mouse 鼠标事件**

#### **MouseButtonDown 鼠标按下**
+ 代码：1025
+ 内置数据： 即为按下位置；button：1左键，button：2 中键 button：3 右键，中间滚轮上划：4，中间滚轮下滑5； touch没研究明白

```` Python
MouseButtonDown {'pos': (59, 2), 'button': 1, 'touch': False, 'window': None})> pos
````

#### **MouseButtonUp鼠标松开**
+ 代码：1026 ；其余同上

#### **MouseMotion 鼠标移动**
+ 代码：1024
+ 内置数据：当前位置；rel[0]x轴移动，rel[1]y轴的移动；buttons移动时，鼠标左中右按键是否按下
```` Python
MouseMotion{'pos': (699, 497), 'rel': (3, 0), 'buttons': (0, 0, 0), 'touch': False, 'window': None})> 
````

***

> ### **Button 键盘事件**

#### **KeyDown 键盘按下**
+ 代码：768
+ 内置数据：unicode输入的unicode字符，mod不知道； key是在pygame中按键的编号，你可以使用pygame.K_按键名，获取这个编号
```` Python
KeyDown {'unicode': ' ', 'key': 32, 'mod': 0, 'scancode': 44, 'window': None pos} 
````

#### **KeyUp 键盘松开**
+ 代码：769
+ 内置数据：见上面


***

> ### Text 文本事件

#### TextEditing 文本编辑
+ 代码：770
+ 内置数据：text文本 start？长度？这个我不太清楚 length一直都是0 我也不太清楚
```` Python 
<Event(770-TextEditing {'text': '', 'start': 0, 'length': 0, 'window': None})>
````

#### TextInput 文本释放
+ 代码：771
+ 条件：按下Enter键，释放TextEditing的text，获取最终的text
+ 内置数据：text文本 start？长度？这个我不太清楚 length一直都是0 我也不太清楚

    ```` Python
    <Event(770-TextEditing {'text': '', 'start': 0, 'length': 0, 'window': None})>
    ````


# 总结

其实Event就是这么简单，当然，当你不知道Event的时候可以亲自尝试出各种event，我的这篇文章就是个佐证，祝大家兔年快乐，之后会有一个兔年的文章

