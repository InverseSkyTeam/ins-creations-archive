---
title: Dp-背包问题
date: 2023-02-01 19:29:06
tags: [Code,算法，Dp动归]
categories: [Code,算法,Dp动归]
toc: true
cover: https://jihulab.com/ZiXuanYuan/blogpic/-/raw/main/pictures/2023/02/1_21_56_37_%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20230131215051.png
---

# 前言
开始提高八角猫dp的第一天，学习的是[代码随想录](https://programmercarl.com/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html#%E4%BB%80%E4%B9%88%E6%98%AF%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92)的教程
以下是学习心得与总结，还有我对背包问题的总结

# 各种背包
想要深刻理解背包问题的技巧首先要深刻理解背包问题
背包问题大体分为3类：01背包、完全背包、多重背包
1. 01背包：给定 n个物品的重量与价值，求最多容纳capacity容量的背包能装下的最大价值 **每个物品最多拿一次**
2. 完全背包 ： 给定 n个物品的重量与价值，求最多容纳capacity容量的背包能装下的最大价值 **每个物品可以拿无数次**
3.多重背包： 给定 n个物品的重量与价值和最多拿的个数，求最多容纳capacity容量的背包能装下的最大价值 **每个物品拿的次数有限制**

这些背包的具体讲解会在之后出一期文章，本次注意讲述其中技巧

***

<!-- more -->

# 解题技巧

+ 对于小白来说，即使告诉他这是背包问题，也可能不知道为什么这是个背包问题（说的就是我（ doge：（不是。
这就涉及到 背包问题的变种问题，目前我只接触到了一种，但这几题都是这样的套路。

## 背包问题的转化
举个栗子：[最后石头重量II](https://leetcode.cn/problems/last-stone-weight-ii/)、[分割等和子集](https://leetcode.cn/problems/partition-equal-subset-sum/)、[目标和](https://leetcode.cn/problems/target-sum/)

### 分割等和子集
![分割等和子集](https://jihulab.com/ZiXuanYuan/blogpic/-/raw/main/pictures/2023/02/2_13_48_15_%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20230202134726.png)

+ 这题乍一看？分类和dp有什么关系，但是仔细想一想就知道，这就是01背包

+ 其实我们把这个问题转化一下，问是否能分割成两个和相等的集合，是不是可以理解为用这些数字可不可以求得所有数字和的一半？
+ 我们把数字看成物品，所有数字和的一半看做背包容量，价值就是数字值的本身，这是不是就是一个背包问题了呢？
+ 如果最大能装的和，或者说价值，没有达到（不等于）所有数字和的一半，那么这个就是不行的，返回false，否则就是可行的 返回true

Ac代码
```` C++
class Solution {
public:
    int lastStoneWeightII(vector<int>& stones) {
        int sum =0;
        for(int i=0;i<stones.size();i++)
            sum+=stones[i];
        int alsum = sum; 
        sum/=2;
        vector<int> dp;
        dp.resize(1505,0);
        for(int i=0;i<stones.size();i++){
            for(int j = sum;j>=0;j--){
                if(j-stones[i]<0) continue;
                dp[j] = max(dp[j],dp[j-stones[i]]+stones[i]);
            }
        }
        for(int i=0;i<=sum;i++)
            cout<< dp[i]<<" ";
        return abs((alsum-dp[sum])-dp[sum]);
    }
};
````

### 最后石头重量II
![最后石头重量II](https://jihulab.com/ZiXuanYuan/blogpic/-/raw/main/pictures/2023/02/2_13_48_16_%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20230202134754.png)

+ 这题一看，好像是的确关系也不是很大，但同样的，我们来进行转换法
+ 每两个石头重量相减，减到不能减为止，我们仔细想一下其实就是把一堆数分成两堆，求这两堆数字最小差
+ 你看！这就和上一题差不多了。不过求的是最小值，如果两堆数字一样，一定就是最小的最小值 ———— 0
+ 所以本题就转换成了 求所有数字和的一半的背包，最多能装多少东西 然后再转换 总和减去这些东西就是另外一半的石子的重量
+ 两者相减就好了

Ac代码
```` C++
class Solution {
public:
    int lastStoneWeightII(vector<int>& stones) {
        int sum =0;
        for(int i=0;i<stones.size();i++)
            sum+=stones[i];
        int alsum = sum; 
        sum/=2;
        vector<int> dp;
        dp.resize(1505,0);
        for(int i=0;i<stones.size();i++){
            for(int j = sum;j>=0;j--){
                if(j-stones[i]<0) continue;
                dp[j] = max(dp[j],dp[j-stones[i]]+stones[i]);
            }
        }
        for(int i=0;i<=sum;i++)
            cout<< dp[i]<<" ";
        return abs((alsum-dp[sum])-dp[sum]);
    }
};

````

### 目标和
![目标和](https://jihulab.com/ZiXuanYuan/blogpic/-/raw/main/pictures/2023/02/2_14_4_27_%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20230202140415.png)

- 这题，看完也会比较懵，这个好像又不是划分数字，和上面的例子毫无关系，怎么就是dp了！？
- 这个时候就需要用到我们的**数学思维**了！

- 题目中 每个数我们是知道的 累加有数的和，这里我们记作 S，而题目其实就是让我们把数分为正负的两部分 一部分相加一部分相减，求最终=target的情况数量
- 那我们现在把这两个部分 分别称作 A和B  它们和一定是 S，而差一定是target
那么 可以列出方程 ：
````
A + B = S 
A - B = target
````
两式相加 2B = S+target 

**B  =  (S+target)÷2**

而求出一部分和为B，与另一部分A相减，就是target，因此求和为B的方案即可，方案类问题就在后文提到

Ac代码
```` C++
class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        int sum=0;
        for(int i=0;i<nums.size();i++) sum+=nums[i];
        int find = (sum+target)/2;
        if(target > sum || target < -sum || (sum+target)%2 == 1) return 0;
        vector<int> dp;
        dp.resize(1005,0);
        dp[0] = 1;
        for(int i=0;i<nums.size();i++){
            for(int j=find;j>=0;j--){
                if(j-nums[i]<0) continue;
                dp[j] += dp[j-nums[i]];
            }
        }
        return dp[find];
    }
};
````

## 方案数量类背包（装满背包方法）

典型例子： [目标和](https://leetcode.cn/problems/target-sum/) 、 [零钱兑换](https://leetcode.cn/problems/coin-change-ii/) 、 [组合总和](https://leetcode.cn/problems/combination-sum-iv/)

这种题目的 dp[j] 一般都指 ***可以组成数量为j的方案数量**
所以，转移方程一般都为 **`if(j - nums[i]>=0) dp[j] += dp[j - nums[i] ]`**,即如果可行就把当前方案和dp[j - nums[i] ]的方案累加

1. 而该类题目需要注意的要点 是 **遍历顺序** 其实也就是 **排列问题** 和**组合问题**的区别 ，这一点和编程 两层循环的嵌套息息相关

    1. 排列问题，注重方案是顺序，即为{1,3}与{3,1}是不同的集合比如说典型例子，[组合总和](https://leetcode.cn/problems/combination-sum-iv/)
    2. 组合问题，不注重方案顺序,即为{1,3}与{3,1}是相同的集合，栗子：[零钱兑换](https://leetcode.cn/problems/coin-change-ii/)

- 而要实现这两者的区别，其实就在我们常常被忽略的点上，这也是我感触较深的地方，那就是 物品i 和容量j 的循环层次的循序
<br>

- 我一开始以为，这个就是卡死的，就必须是像下面这样子进行dp，成为了思维定式。
```` C++
for(int i=0;i<coins.size();i++)
    for(int j=0;j<=amount;j++)
        ···
````
- 但是，这里，其实还可以这样写,其中···是相同的代码
```` C++
for(int j=0;j<=amount;j++)
    for(int i=0;i<coins.size();i++) 
        ···
````
- 这两个写法在一般的问题中是都可以的，但是，在特殊问题就比如刚才的两个题目就有天差地别了，比如刚刚两题
![零钱兑换](https://jihulab.com/ZiXuanYuan/blogpic/-/raw/main/pictures/2023/02/1_21_13_31_%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20230201211249.png)
这个是组合问题，不考虑顺序
![组合总和](https://jihulab.com/ZiXuanYuan/blogpic/-/raw/main/pictures/2023/02/1_21_13_31_%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20230201211249.png)
- 这个是排列问题，考虑顺序，应为求可能情况，所以两者有所区别

- 当 物品的遍历在内侧时（排列问题），我们发现 同一个容量 会同时统计两种情况 
如果求 求组成4这个数字 外层遍历背包容量，内层循环遍历物品(这里是数字)，会出现 dp[j] += dp[j-1] 和 dp[j] += dp[j-3] 两个情况 这两个情况分别对应1+3 和 3+1 等于4的情况，统计了两遍，这在排列问题里面是成立的

- 外层遍历物品(这里是数字)，内层循环遍历背包容量，每个数字单独处理，不回出现上述情况
这里借用代码随想录中Carl的一句话 :

- **如果求组合数就是外层for循环遍历物品，内层for遍历背包;**
- **如果求排列数就是外层for遍历背包，内层for循环遍历物品。**

<br>

2. 另外一个值得注意的事情，就是 dp的初始值即为dp[0]
一般来说 dp[0] 都是 0 但是特殊情况是 1 这是需要**按情况仔细斟酌**的 

***
***

## 最值背包(装满背包物品最小或最大价值)

典型例子：[完全平方数](https://leetcode.cn/problems/perfect-squares/) 、 [零钱兑换](https://leetcode.cn/problems/coin-change/) 、 [一和零](https://leetcode.cn/problems/ones-and-zeroes/)
这些栗子都是求多个物品组成一个容量的最大，最小装满次数或者最大装的个数

前两个求最小，后一个是求最大，但是它们的一般的状态转移方程一般都是 `dp[j] = max/min(dp[j],dp[j-nums[i]]+1);`
值得注意的是 这种题型的dp数组初始化的处理方式：如求最大值，赋值为INT_MIN最小值或者9，而求最小值，先赋值为INT_MAX；
而在中间累加的过程中是有可能越界的，所以需要加上特别判断，仔细思考dp[0]的初始值和意义，当遇到迷糊的时候，多思考dp[i]到底是什么意思，或许问题就会迎刃而解了。

而 《一和零》 本质上是01背包，但是价值有两个维度，这也是这道题的特别之处，但公式却没有改变，还是和01背包一样， 只不过纬度变化使之多了一层循环
![一和零](https://jihulab.com/ZiXuanYuan/blogpic/-/raw/main/pictures/2023/02/2_13_44_32_%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20230202134417.png)
所以状态转移方程改变为了 ：` dp[i][j] = max(dp[i][j], dp[m-nums1[i]][n-nums2[i]]+1)` 
注意：这道题里面价值就是使我们选择的组合中，多一个字符串，因此是 + 1
 

# 总结
代码随想录的教程很好，本教程也是看完代码随想录编撰的
我看完教程之后，才最终发现，dp原来也有这么多衍生的变形和细节。
