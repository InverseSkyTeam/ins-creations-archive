---
title: Vercel+Github搭建Hexo博客
date: 2022-08-13 19:42:54
tags: [Html,Code,博客]
categories: [Code,Html,博客]
toc: true
cover: https://jihulab.com/ZiXuanYuan/blogpic/-/raw/main/pictures/2022/08/17_16_39_43_tit2.svg
---

### 工作原理

+ github是一个代码托管平台，缺点是加载的时候特别慢
+ vercel完美结局了这个问题，vercel加载速度相对快一些，可以和github绑定，而且根据github储存库实时拉取更新
+ Hexo一个快速、简洁且高效的博客框架,它支持几条简短的命令发布博客,因此是对于初学者比较友好的博客框架



<!-- more -->

### 准备工作

- github账号、vercel账号
- nodejs v12版本以上 、 git
  
  > 网站官网：
  > 
  > > [github官网](https://github.com/)、[vercel官网](https://vercel.com/)
  > > [git官网](https://git-scm.com/)、[nodejs官网](https://nodejs.org/en/)

* * *

### 创建Vercel项目并拉取

1. 首先进vercel官网，点击 New Project 按钮，然后点击 Browse All Templates 按钮 找到Hexo主题然后 修改项目名 把下面那个框勾掉（那个是创建私有储存库），然后你的github里会自动生成一个项目
2. 配置git :
   - 打开git-bush 输入ssh-keygen -t rsa -C "{{github的电子邮箱地址}}" 连续 3 次回车，最终会在用户目录下生成个包含公钥私钥等数据的目录 ( 一般是 C:/Users/{{你的用户名}}/.ssh/ ) 将刚复制的内容粘贴到 Key(你的github->setting->SSH) 中，Title 随便写一个，点击保存 ( Add SSH Key ) 
   - 运行下方命令 :
     
     ```
     git config --global user.name "{{你的 GitHub username}}"
     git config --global user.email "{{你的 GitHub 注册邮箱地址}}"
     ssh -T git@github.com # 邮箱地址不用改 如果提示 Are you sure you want to continue connecting (yes/no)? 请输入 yes 并回车。
     ```
3. 在本地选一个文件夹 打开git-bash 运行：git clone https://github.com/用户名/仓库名称

* * *

### 更换主题

1. 首先打开[hexo官网](https://hexo.io/themes/) 挑选一个心仪的主题 ，单击图片可以预览网页，点下面文字到github仓库
   __注意：不要选择indigo这个主题，这个主题有漏洞，配置起来很麻烦，有些主题预览不了的尽量不要选，避免一会的麻烦（作者一开始选的就是indigo）__
2. 到仓库之后 在主文件夹打开git-bash 然后输入 git clone 你刚才的主题的仓库的网址 themes/主题名
3. 打开主项目下的 _config.yml 文件 把 theme：lanspace 改为 theme:你的主题名 然后进到 themes文件夹里把landspace文件夹删了（也可以不删）

* * *

### 更改配置

__注意：这一步需要有较好的英文功底__

1. 进入 打开主项目下的 _config.yml 文件  修改
    __注意：这里冒号后面有空格 我之前就是应为这个找半天不知道报错在哪__
   
   ```
   title: 标题
   subtitle: 你的个性签名
   author: 你的名字
   language: zh-CN
   # URL
   url: 这里写你vercel预览的网址，我这边是：https://yzx-blog.vercel.app/
   ```
2. 进入你的主题文件夹里面的 _config.yml 文件 修改各项属性 由于每个主题各有不同 大家可以在网上搜索教程

* * *

### 生成网页

1. 万事俱备后再在（这一步其实应该提前做的）
    cmd运行：
   
   ```
   npm install -g hexo 
   ```
   
    主目录运行：
   
   ```
   npm install -g hexo 
   npm install hexo-cli --save
   npm install hexo-deployer-git --save
   ```
   
    这是在搭建hexo环境

2. 生成网页
   
   ```
   hexo clean
   hexo g
   hexo s
   ```
   
    hexo s之后会在http://localhost:4000/显示你的网页 如果这个时候你成功了那么就可以提交到github了
   
    __可能的报错：__
   
   ```
   error: RPC failed； curl 28 OpenSSL SSL_read: Connection was reset, errno 10054 fatal: expected
   ```
   
    __解决办法__
   
   ```
   git config --global http.sslVerify "false"
   ```

* * *

### 提交并成功部署博客

1. 主文件夹打开git-bush
2. 运行:以下代码
   
   ```
   git remote
   git remote 你vercel生成的那个github仓库网址
   git add .（可能要尝试两次）
   git commit -m "提交的备注"
   git push -u origin main
   ```

* * *

### 写文章

1. 运行 hexo new "文章名"
2. 在提示的目录打开文件使用markdown语法编辑 具体教程看[markdown教程用法](https://www.runoob.com/markdown/md-tutorial.html)转自菜鸟教程
3. 之后 clean g s三件套 再来一遍再提交就OK了

* * *

### 归档、分类里面是报错的

1. 检查一下你的yml配置文件
2. 按照这个[教程](https://blog.csdn.net/weixin_48927364/article/details/123295436)走
