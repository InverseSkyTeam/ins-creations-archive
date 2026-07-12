---
title: requests详解(1)
date: 2022-09-03 19:15:01
tags: [Code,Python,Spider爬虫,类库]
categories: [Code,Python,类库,Spider爬虫,requests]
cover: https://jihulab.com/ZiXuanYuan/blogpic/-/raw/main/pictures/2022/09/3_19_27_12_003.webp
toc: true
comments: true
---
# 前言
+ requests是Python中的一个网络请求库，可以用于实现调取api，获取网页源代码等功能
+ requests一共有很多种请求方式，我今天介绍最常用的2种，他们分别是get、post请求

<!--more-->

***

# get请求
### get请求特点概述

+ get请求是 __获取数据__(不建议用get提交数据)
+ 请求的参数将以````?name:val````的形式呈现，__不安全__
+ 请求的 __数据量有限制__  ，一般是 __8kb__
+ 速度快

### get请求基本使用方法

- 参数讲解
  第一个参数为请求网址，第二个是请求头，第三个是请求数据
  ```` Python
  response=requests.get(url,headers=head,params=params)
  ````
- 请求头的一般写法
  这是应对一般的反爬虫网站的措施，请求头的数据量有限制
  ```` Python
  head = {
      "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11"
  }
  ````
  应用实例：
  ![](https://jihulab.com/ZiXuanYuan/blogpic/-/raw/main/pictures/2022/09/3_19_49_23_get%E8%AF%B7%E6%B1%82web%E5%AE%9E%E4%BE%8B.png)
- 数据的格式
  数据以字典的方式呈现，以下是数据格式的实例：
  ```` Python
  params = {
      'type': 'python',
      'code': 'print(1)',
  }
  ````
  一般在网址上以?name1=val1&name2=val2形式出现,有数据量限制

***

# Post请求

### Post请求特点概述

+ post请求是 __提交数据__
+ __不限制__ 提交数据的 __大小__
+ __速度慢__ ,但是 __安全__

### Post请求方法
- 参数讲解：
  url为网址，headers请求头和上面的get请求一样，data是字典数据请求和get的params一样，json是json数据请求
  + 方法一：
    ```` Python
    response=requests.post(url,headers=head,data=payload)
    ````
  + 方法二：
    ```` Python
    response=requests.post(url,headers=head,json=payload)
    ````
***

# 其余的参数
+ ````requests.post/get(url,headers=head,timeout=second)````:
  设置接口连接的最大时间,单位为秒（超过该时间会抛出超时错误）
+ ````requests.post/get(url,headers=head,verify=False)````
  ````verify=True````(默认): 检查SSL证书认证  ````verify=False````(常用): 忽略SSl证书认证

***

# 其余的功能
+ ````res.status_code```` 获取状态码
+ ````res.request.headers```` 获取请求头
+ ````res.headers```` 获取响应头
+ ````res.content```` 获取响应内容的二进制
+ ````res.text```` url对应的页面内容，也就是网页源代码
+ ````res.apparent_encoding```` 猜测编码
+ ````res.json()```` 返回json数据