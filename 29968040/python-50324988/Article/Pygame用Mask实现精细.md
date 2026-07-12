---
title: Pygame用Mask实现精细碰撞
date: 2022-08-19 18:22:16
tags: [Python,Pygame,Code]
categories: [Code,Python,Pygame]
cover: https://jihulab.com/ZiXuanYuan/blogpic/-/raw/main/pictures/2022/08/23_22_5_46_daily_pic.png
toc: true
comments: true
---

如果你有Pygame有一定的基础，并用过Pygame编写过游戏那么你一定有一个烦恼那就是当两个图像碰撞检测时，往往采用的是矩形碰撞检测，这样就会导致，两个图案实际上还没有碰到，Pygame就识别为碰到了

而Pygame中的Mask(遮罩)模块就是解决这个问题很好的方法，我们把这种用Mask实现碰撞检测的方法叫做精细碰撞，当然，这篇文章中实现的是背景色为透明度图片，而并非白色

<!--more-->

## Pygame.Mask模块实现精细碰撞

### 分步骤实现

+ 创建发生碰撞的图片对象和矩形
  
  - 参数讲解:
    这里的Rect函数中的参数分别为x、y坐标，和长、宽
    pygame.transform.scale(pygame.image.load("gib.png"),(200,200))：这是改变图片gib.png大小为200*200
    
    ```Python
      big = pygame.transform.scale(pygame.image.load("gib.png"),(200,200))
      small = pygame.transform.scale(pygame.image.load("mal.png"),(100,100))
      rectbig=pygame.Rect(200,200,200,200)
      rectsmall=pygame.Rect(0,0,100,100)
    ```

+ 创建发生碰撞的图片对象所对应的遮罩
  
  - 参数讲解:
    这里的big和small都是一个图片的对象
    
    ```
      maskbig=pygame.mask.from_surface(big)
      masksmall=pygame.mask.from_surface(small)
    ```

+ Mask遮罩碰撞检测
  
  - 参数讲解
    maskA和maskB都是两个遮罩
    其中offset是一个元组，格式如下：(maskB的x坐标.-maskA的x坐标,maskB的y坐标-maskA的y坐标)
    这里元组的两个元素应该都是整形，所以如果坐标是小数的话请使用int()函数转为整数
    
    ```Python
      maskA.overlap(maskB,offset)
    ```
  
  - 参数讲解
    maskA.overlap(maskA,offset)：这个函数是检测mask遮罩碰撞的函数
    如果返回值为None表示没有碰撞，否则返回一个元组，所以这边用!=None表示已经碰撞
    
    ```Python
      if masksmall.overlap(maskbig,offset)!=None: # 已经碰撞
          print(masksmall.overlap(maskbig,offset))
    ```
  
  - 实例
    
    ```Python
      offset=(int(200-sx),int(200-sy))
      if masksmall.overlap(maskbig,offset)!=None: # 已经碰撞
          print(masksmall.overlap(maskbig,offset))
      else: #没有碰撞
          print("NO-Collide")
    ```

### Pygame做一个演示

+ Mask碰撞检测和矩形碰撞的比较
    这里我在使用Mask方法检测出没有碰撞的同时，检测用常规方法是否碰撞
    ![alt 加载失败](https://jihulab.com/ZiXuanYuan/blogpic/-/raw/main/pictures/2022/08/19_22_11_35_MaskRect%E5%AE%9E%E4%BE%8B.png)
    [代码原链接：C站](https://code.xueersi.com/home/project/detail?lang=code&pid=36703416&version=offline&form=python&langType=python)
+ 结论
    从图中我们明显发现这位清洁工阿姨很明显没有碰到小怪物，在Mask方法中是没有碰撞的即为：Mask:NO
    但是在Mask：NO的同时用普通的矩形检测确实相撞的，这说明确实Mask遮罩是有用的

## Mask的其他函数

+ 返回Mask的大小 ````pygame.maskA.Mask.get_size() ````
+ Mask 重叠的像素数量 pygame.maskA.Mask.overlap_area(othermask, offset) 
+ 更多函数请自行查阅

## 总结

其实Mask的功能还有很多，而Pygame实现精准碰撞也不止这一种，以后会有第二篇精准碰撞的文章，敬请期待！
