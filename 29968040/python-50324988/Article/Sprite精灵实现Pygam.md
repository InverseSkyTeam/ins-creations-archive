---
title: Sprite精灵实现Pygame矩形、圆形、精细碰撞
date: 2022-08-20 18:05:33
tags: [Python,Pygame,Code]
categories: [Code,Python,Pygame]
toc: true
cover: https://jihulab.com/ZiXuanYuan/blogpic/-/raw/main/pictures/2022/08/23_22_5_46_016.webp
---

## 前言

+ 如果你有Pygame有一定的基础，并用过Pygame编写过游戏那么你一定有一个烦恼那就是当两个图像碰撞检测时，往往采用的是矩形碰撞检测这样就会导致，两个图案实际上还没有碰到，Pygame就识别为碰到了

+ 而Pygame中的Mask(遮罩)模块就是解决这个问题很好的方法，我们把这种用Mask实现碰撞检测的方法叫做精细碰撞，然而，这种方法实现的 __难度稍微有点大__ ，而且 __代码碎片很多__ ，__很凌乱__

+ 而在Pygame中有这么一个类，专门是为游戏角色而设置的，这个类就是 __Sprite精灵类__ ，这个类里面就有帮我们封装好的三种碰撞检测方法：Rect、Circle、Mask，其中Mask就是上面提到的遮罩
  
  <!-- more -->
  
  ## Sprite精灵类实现精细碰撞

+ 创建精灵
  
  - 这里是创建了一个名为s的类
    
    ```Python
    s = pygame.sprite.Sprite()
    s.image = pygame.transform.scale(pygame.image.load('file.png'),(width,height))
    s.rect = pygame.Rect(x,y,width,height)
    ```
  
  - 实例：创建两个待碰撞精灵，并为其image和rect属性赋值
    
    ```Python
      s = pygame.sprite.Sprite()
      s.image = pygame.transform.scale(pygame.image.load('A.png'),(350,350))
      s.rect = pygame.Rect(300,150,350,350)
    
      c = pygame.sprite.Sprite()
      c.image = pygame.transform.scale(pygame.image.load('B.png'),(200,200))
      c.rect = pygame.Rect(0,0,100,100)
    ```

+ 碰撞检测
  
  - 矩形碰撞检测
    sp1、sp2分别是两个Sprite精灵
    如果返回1为碰撞,0为没有碰撞
    
    ```Python
    pygame.sprite.collide_rect(sp1,sp2)
    ```
  
  - 外接圆碰撞检测
    sp1、sp2分别是两个Sprite精灵
    如果返回True为碰撞，False为没有碰撞
    
    ```Python
    pygame.sprite.collide_circle(sp1,sp2)
    ```
  
  - Mask像素碰撞(精细碰撞)
    sp1、sp2分别是两个Sprite精灵
    如果返回None为不碰撞，返回一个元组为碰撞
    
    ```Python
    pygame.sprite.collide_mask(sp1,sp2)
    ```
    
    ## 原理
    
    在上一篇文章中，我介绍了Mask遮罩，其实，这个Sprite精灵只是对它的封装，当然Sprite可不止只有这个功能，
    他的原来就是检测两个图案非透明部分有多上像素重叠，所以在物体1和物体2之间的碰撞难免还是会因为两个像素仅仅"接壤"而没有判断碰撞，但对比rect碰撞已经好了很多了

## Pygame演示

+ __这里是三种方式的对比，可见：外接圆碰撞精度>矩形碰撞>精细碰撞__
  ![alt 加载失败](https://jihulab.com/ZiXuanYuan/blogpic/-/raw/main/pictures/2022/08/20_19_20_52_Sprite%E4%BA%8B%E4%BE%8B%E7%A2%B0%E6%92%9E.png)
+ [原链接已开源](https://code.xueersi.com/home/project/detail?lang=code&pid=36709123&version=offline&form=python&langType=python)

## 总结

当然Sprite的功能远不止这些，这其实是pygame的一个游戏角色群的处理类，功能还是有非常之多的
