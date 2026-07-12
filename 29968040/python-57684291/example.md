# INS-PGM简介
INS-PGM是一个完全由逆天团队开发的pygame中的markdown渲染器  
并且除了数学公式和文本换行，其余排版格式和洛谷100%一致

需要的第三方库：

1. `markdown-it-py` : markdown 解析

2. `pygame`: 界面渲染

3. `PIL(Pillow)`: 图片模糊

4. `pygments`: 代码高亮

5. `bs4(BeautifulSoup4)`: html解析

6. `lxml`: bs4的html解析器

内置字体：

1. 普通字体：`HarmonyOS Sans SC`

2. 等宽字体：`Cascadia Code` + `HarmonyOS Sans SC` 的混合字体

## 1. 普通语法
### 1.1 标题

不同数量的`#`可以完成不同的标题，如下：

# 一级标题

## 二级标题

### 三级标题

### 1.2 字体

粗体、斜体、粗体和斜体，删除线，需要在文字前后加不同的标记符号。如下：

**这个是粗体**

*这个是斜体*

***这个是粗体加斜体***

~~这里想用删除线~~

注：如果想给字体换颜色、字体或者居中显示，需要使用内嵌HTML来实现。

### 1.3 无序列表

无序列表的使用，在符号`-`后加空格使用。如下：

- 无序列表 1
- 无序列表 2
- 无序列表 3

如果要控制列表的层级，则需要在符号`-`前使用空格。如下：

- 无序列表 1
- 无序列表 2
  - 无序列表 2.1
  - 无序列表 2.2

同时，还支持带间隔的列表：

- 无序列表 1

- 无序列表 2

- 无序列表 3

### 1.4 有序列表

有序列表的使用，在数字及符号`.`后加空格后输入内容，如下：

1. 有序列表 1
2. 有序列表 2
3. 有序列表 3

### 1.5 引用

> Markdown 标记区块引用的方法是在行的最前面加 `>`。
> 
> 也可以只在整个段落的第一行最前面加上 `>`。
> > 区块引用内部可以嵌套，只要根据层次加上不同数量的 `>` 即可。
> > 
> > *我是内部嵌套区块，我可以使用其他 Markdown 语法哦。*
> > 
> > ### 我是引用区块内使用 3 级标题语法。
> > 
> > ```java
> >     //在引用区块内可以加入代码块
> >     import java.net.URL;
> >     import java.util.Arrays;
> >     import java.util.Date;
> >     import java.util.Set;
> > ```

### 1.6 链接

在方块括号后面紧接着圆括号并插入网址链接即可，如果还想要加上链接的 title 文字，只要在网址后面，用双引号把 title 文字包起来即可，例如：

```markdown
[行内式链接标题](https://www.luogu.com.cn)
```

显示效果：这是 [行内式链接标题](https://www.luogu.com.cn) 内联方式。
使用方法如下所示：

### 1.7 图片

Markdown 使用一种和链接很相似的语法来标记图片。

行内式的图片语法如下：

`![图片下方文字](图片相对路径或绝对路径)`

`![图片下方文字](图片相对路径或绝对路径 "可选标题")`

例如：

```markdown
![logo](https://cdn.class.luogu.com.cn/fe/logo-full.png?27925f707b34b1472e135b1a2dd848e5)
```

将会显示图片：

![logo](https://cdn.class.luogu.com.cn/fe/logo-full.png?27925f707b34b1472e135b1a2dd848e5)

### 1.8 分割线

可以在一行中用三个以上的减号来建立一个分隔线，同时需要在分隔线的上面空一行。如下：

---

### 1.9 表格

可以使用冒号来定义表格的对齐方式，如下：

| 姓名   | 年龄 |     工作 |
| :----- | :--: | -------: |
| 小可爱 |  18  | 吃可爱多 |
| 小小勇敢 |  20  | 爬棵勇敢树 |
| 小小小机智 |  22  | 看一本机智书 |


## 2. 特殊语法

### 2.1 代码块

如果在一个行内需要引用代码，只要用反引号引起来就好，如下：

Use the `printf()` function.

在需要高亮的代码块的前一行及后一行使用三个反引号，同时**第一行反引号后面表示代码块所使用的语言**，如下：

```java
// FileName: HelloWorld.java
public class HelloWorld {
  // Java 入口程序，程序从此入口
  public static void main(String[] args) {
    System.out.println("Hello,World!"); // 向控制台打印一条语句
  }
}
```

支持以下语言种类：

```
bash
clojure，cpp，cs，css
dart，dockerfile, diff
erlang
go，gradle，groovy
haskell
java，javascript，json，julia
kotlin
lisp，lua
makefile，markdown，matlab
objectivec
perl，php，python
r，ruby，rust
scala，shell，sql，swift
tex，typescript
verilog，vhdl
xml
yaml
```

如果想要更换代码高亮样式，可在上方**代码主题**中挑选。


diff 不能同时和其他语言的高亮同时显示，使用效果如下:

```diff
+ 新增项
- 删除项
```

### 2.2 数学公式

行内公式使用方法，比如这个物理公式：$\vec{F}_g=-F\frac{m_1 m_2}{r^2} \vec{e}_r$

块公式使用方法如下：

$$H(D_2) = -\left(\frac{2}{4}\log_2 \frac{2}{4} + \frac{2}{4}\log_2 \frac{2}{4}\right) = 1$$

矩阵：

$$
  \begin{pmatrix}
  1 & a_1 & a_1^2 & \cdots & a_1^n \\
  1 & a_2 & a_2^2 & \cdots & a_2^n \\
  \vdots & \vdots & \vdots & \ddots & \vdots \\
  1 & a_m & a_m^2 & \cdots & a_m^n \\
  \end{pmatrix}
$$

### 2.3 插入 bilibili 视频

```markdown
![](bilibili:221107)

![](bilibili:av53851218)

![](bilibili:BV1GJ411x7h7)

![](bilibili:BV1bv411p7U5?page=4&t=82)
```

说明：
- av 号支持省略前缀  
- 可定义分 P 和起始播放位置，t 单位为秒（部分老页面不兼容）

效果如下：

![](bilibili:221107)

![](bilibili:av53851218)

![](bilibili:BV1GJ411x7h7)

![](bilibili:BV1bv411p7U5?page=4&t=82)

## 3. 特殊功能
按 `f12` 键可打开调试模式  
允许使用类似触摸屏滑动的方式移动界面（电脑端默认关闭）
