---
title: FastAPI的使用(一)
tags:
  - 编程语言
  - Python
  - Web开发
categories:
  - Python
  - Web框架
  - FastAPI
abbrlink: 38548
date: 2022-08-19 22:56:47
---

# 前言

在开发项目的过程中，我们可能会遇到想要快速开发一个API应用，却不想要去了解Web框架底层运作的原理，只想提供一个可以用网络访问的API服务这种情况。Python无疑是这种快速应用开发最好的选择，而Python的Web框架百花齐放，Django完整而成熟，却太过臃肿；Flask简洁优雅，却难以屏蔽底层细节......这种情况，我们就需要FastAPI出场了。

# FastAPI简介

FastAPI是用Node.js写的一个高性能Web服务器框架，提供了对应的Python接口，由于是使用Node.js开发的，所以它的速度比Django或者Flask这种基于Python开发的框架都要快，而且FastAPI非常简单而易于上手，几乎是采用的声明式开发，所以你可以无需考虑其它，而专心的开发你的API接口，FastAPI还自带Swagger（OpenAPI）文档生成，这样你就不用手动写API文档了，FastAPI会自动为你生成，听起来很棒，是吗？那就开始吧！

# 安装

好的模块从来都是大道至简，只需要一行代码就好：

```bash
pip install "fastapi[all]"
```

解释一下，这是pip的一个高级用法，平时我们都是`pip install xxx`，这样只会安装xxx这个库，有可能xxx的依赖库没有安装到，而`pip install "xxx[all]"`代表安装xxx及xxx的所有依赖库。所以，通过上述代码我们安装了**fastapi**及其所有依赖库（主要是**uvicorn**）。

# HelloWorld

## 示例

看到这眼熟的大字标题，你应该明白我要讲什么了。是的，所有新知识都是从一行**HelloWorld**开始的，不管你是在开发一个惊天动地的大工程还是一个微不足道的小测试。闲话少说，上代码：

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

解释一下这些代码的用途，会Flask的小伙伴们应该感觉很熟悉。

```python
from fastapi import FastAPI
```

这一行很简单，我们从`fastapi`这个库中导入了`FastAPI`这个类，这个类即将在下面用到。

```python
app = FastAPI()
```

这也很简单，我们实例化了一个FastAPI对象并命名为app。

```python
@app.get("/")
async def root():
    return {"message": "Hello World"}
```

这三行我们需要连在一起解释。首先，`@app.get("/")`这是Python独有的语法——装饰器，装饰器是什么我在这里不过多的描述了，以后我会写一篇文章专门讲解的。简单来说，对于装饰器的理解可以望文生义，就是用来装饰一个函数的功能的，也就是给函数增加一些新功能，在此处，它是用来声明下面的函数对应的路由的。此处的**app**是我们上面实例化好的对象，**get**是**app**的一个方法，用来声明这个API是通过get方法请求的，如果需要其他方法，直接将**get**改为其它的HTTP方法，如**post**或者**put**就可以了。这里get方法的参数是`"/"`，这里`/`代表根目录，也就是通过get方法访问根目录，就会执行下面的函数，并返回一个值。

第二行`async def root()`，定义一个名为**root**的函数，后面的`def root()`很容易理解，前面的`async`不用过多的理解，只需要理解为这是**fastapi**必须的语法就够了，我们以后会说明它的用处的。

第三行`return {"message": "Hello World"}`很简单吧，就是返回一个字典格式的数据。键为`message`，值为`Hello World`

这样，我们就写好了自己的第一个**FastAPI**程序，并且完全理解了它，怎么样，是不是很有成就感？

## 运行

写好了程序，我们需要运行它。**FastAPI**程序的运行有些特别，并不是直接运行`main.py`文件，而是：

```bash
uvicorn main:app --reload
```

这里的**unicorn**已经在安装**FastAPI**的时候安装了，运行后，终端会出现以下输出：

```bash
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [28720]
INFO:     Started server process [28722]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

这里的输出告诉我们：FastAPI已经在`http://127.0.0.1:8000`运行着了，按下`CTRL+C`可以终止运行。

这时候，我们通过浏览器访问`http://127.0.0.1:8000`，就可以看到如下的 JSON 响应：

```json
{"message": "Hello World"}
```

这就代表，我们的第一个程序成功了！！！

如果我们访问`http://127.0.0.1:8000/docs`，你就可以看到如下界面：

![Swagger UI](https://jihulab.com/wuyuhangxyz/picturebed/-/raw/main/pictures/2022/08/19_23_35_56_index-01-swagger-ui-simple.png)

这就是Swagger（OpenAPI）自动为我们生成的API文档，非常详细，还有自动测试，以后再也不用自己写文档啦！

最后，解释一下运行的命令的含义，这里的`main:app`是制定FastAPI应用的，`main`是**.py**文件名，我们的是**main.py**，所以是`main`，`app`就是程序里面实例化的**FastAPI**的名字，`--reload`代表每次修改**main.py**文件里的内容后不用重启服务器，只需要保存更改，就会自动识别，然后自动修改服务器的响应，非常智能好用。

# 总结

这一篇文章，我带大家入门了FastAPI的开发，大家也感受到了FastAPI的简洁与方便，以后我还会更新相关文章，敬请期待。
