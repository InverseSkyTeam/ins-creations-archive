> 这个文档来自[@袁梓轩](https://code.xueersi.com/space/59842528)的[博客（现已失效）](https://yzx-blog.tk)  
> 新版多进程渲染代码由[@吴宇航](https://code.xueersi.com/space/17025146)提供

# 前言

因为疫情，非常可惜，本应该在10月的上海如期举行的CSP-Junior第二轮，**它取消了**
这对于一个好不容易通过第一轮的考生来说万分悲痛。

对此，上海市在12月25日举办的*上海市中小学生人工智能算法设计复赛*中上海市专门将C++组的复赛设置为了CSP第一轮通过的选手参加的特权，我们称之为SHCSP

本次SHCSP 和CSP一样 一共4题 满分400 采用IOI赛制，可惜的是，我能力不足，只拿到了194分......排名的话：456/793

# 题面

### 入门 T1 - 串符字

#### 题目描述

给定 $n$ 个字符串，输出其中每种字符串出现次数的最大值。

这里在统计出现次数时，我们认为两个字符串 $s,t$ 是相同的，当且仅当 $s=t$ 或 $s=rev(t)$。

（$s=t$ 的定义即为字符串长度相等，且每一位的字符对应相等。$rev(s)$ 的定义为将字符串翻转。）

#### 输入格式

第一行，一个正整数 $n$。

接下来 $n$ 行，每行一个字符串 $s_i$。

#### 输出格式

一行，一个正整数，表示出现次数的最大值。

#### 样例 #1

##### 样例输入 #1

```
3
a
abc
cba
```

##### 样例输出 #1

```
2
```

#### 提示

【数据范围】

记 $L=\max_{i=1}^n|s_i|$。

对于 $30\%$ 的数据，$1\le n,L\le 20$。

对于 $50\%$ 的数据，$1\le n,L\le 50$。

对于 $100\%$ 的数据，$1\le n,L\le 100$，字符串均不为空。



***



### 入门 T2 - 将军棋

#### 题目描述

有一个 $n$ 行 $m$ 列的长方形网格，一开始每个格子上都写着数字 $0$。

接下来有 $q$ 次操作，每次给定一个格子 $(x,y)$（表示第 $x$ 行第 $y$ 列的格子），将它上面写着的数取反（$0$ 变成 $1$，$1$ 变成 $0$）。

如果在格子 $(i,j)$ 周围一圈加上它自己共 $9$ 个格子中（除去那些超出网格边界的），至少一个上面写着数字 $1$，那么就称格子 $(i,j)$ 是好的。

在每次操作过后，你需要输出整个网格中好的格子的数量。

#### 输入格式

第一行：三个整数 $n,m,q$。

接下来 $q$ 行：每行两个整数 $x,y$，表示对格子 $(x,y)$ 进行操作。

#### 输出格式

共 $q$ 行：每行一个整数表示答案。

#### 样例 #1

##### 样例输入 #1

```
3 3 4
1 1
3 3
2 1
3 3
```

##### 样例输出 #1

```
4
7
8
6
```

#### 提示

【样例 1 解释】

下图展示了每次操作后网格的情况，浅灰色的格子是好的，深灰色的格子不是好的。

![](https://cdn.luogu.com.cn/upload/image_hosting/l42ex6n5.png)

【数据范围】

对于 $100\%$ 的数据：$1\leq n,m\leq 1000,\ 1\leq q\leq 10^5,\ 1\leq x\leq n,\ 1\leq y\leq m$。

对于 $15\%$ 的数据：$1\leq n,m\leq 2,\ 1\leq q\leq 100$。

对于 $30\%$ 的数据：$1\leq n,m\leq 5,\ 1\leq q\leq 1000$。

对于 $45\%$ 的数据：$1\leq n,m\leq 20,\ 1\leq q\leq 2000$。

对于 $60\%$ 的数据：$1\leq n,m\leq 100,\ 1\leq q\leq 10000$。

对于另外 $20\%$ 的数据：$n=1$。



***

### 入门 T3 - 忙碌的小人

#### 题目描述

**13:00更新：请重新提交本题，之前没开O2。**

**13:55更新：小人连续两天可以待在同一个节点不动，但是必须遵从 Alice 或 Bob 的指示。**

有一张 $n$ 个点 $m$ 条边的无向图，图上有一个小人，初始站在点 $st$。

接下来的 $q$ 天里，第 $i$ 天将有 $k_i$ 个点提供住宿服务。小人需要在这一天内到达其中的某一个点，并过夜。

而由于小人非常的小，无法看到图的全貌，我们请来了 Alice 和 Bob 协助小人进行移动。

具体来说，Alice 和 Bob 会**轮流**告诉小人，当天应该前往哪个点过夜，然后让小人沿着最短路线进行移动。

这里最短路线的定义是经过的边数最少。

Alice 希望让小人经过的总边数最多，Bob 则恰好相反，希望经过的总边数最少。

请你求出，在 Alice 先手与 Bob 先手的两种情况下，小人最终经过的总边数分别会是多少？

#### 输入格式

第一行，四个正整数，$n,m,q,st$。

接下来 $m$ 行，每行两个正整数 $x,y$，表示一条连接 $x,y$ 的无向边。**可能有重边和自环。保证图联通。**

接下来 $q$ 行，每行首先有一个正整数 $k_i$，接着有 $k_i$ 个数，表示可以过夜的节点编号。**可能有重复的节点编号。**

#### 输出格式

一行，两个整数，分别表示 Alice 先手和 Bob 先手时的答案。

#### 样例 #1

##### 样例输入 #1

```
4 4 5 1
3 2
2 1
3 4
3 1
3 2 4 4 
1 1 
3 1 3 3 
3 2 2 2 
1 4
```

##### 样例输出 #1

```
8 5
```

#### 提示

###### 【数据范围】

对于 $20\%$ 的数据，$n,m,q\le 20$

对于另外 $20\%$ 的数据，$n\le 200,k_i=1$

对于 $60\%$ 的数据，$n\le 200$

对于 $100\%$ 的数据，$1\le n,m\le 5000,1\le k_i\le 20,1\le q\le 10^5$。

保证 $1\le st\le n$。

建议使用较快的输入方式（比如scanf）。



***



### 入门 T4 - 染色

#### 题目描述

有 $n$ 颗珠子，从左到右排成一行。

你想给它们染上颜色，共有红、蓝、黄三种颜色可选，分别需要染 $a,b,c$ 颗（$a+b+c=n$）。

假设第 $i$ 颗珠子染的颜色是 $d_i(1\le i\le n)$，那么你应该保证 $d_i\neq d_{i+1},d_1\neq d_n$。

求染色的方案数，对一个给定的模数取模。

#### 输入格式

一行，四个整数，$a,b,c,mod$。其中 $mod$ 表示模数。

#### 输出格式

一行，一个非负整数，表示答案。

你应当保证它在 $[0,mod)$ 范围内。

#### 样例 #1

##### 样例输入 #1

```
1 2 3 998244353
```

##### 样例输出 #1

```
6
```

#### 样例 #2

##### 样例输入 #2

```
2 3 4 998244353
```

##### 样例输出 #2

```
54
```

#### 提示

【数据范围】

本题为捆绑测试。

Subtask 1（10分）：$n\le 11$

Subtask 2（10分）：$a,b,c\le 50$

Subtask 3（4分）：$a,b\le 10^7,c=0$

Subtask 4（20分）：$a,b,c\le 150$

Subtask 5（25分）：$a,b,c\le 300$

Subtask 6（30分）：$a,b,c\le 1000$

Subtask 7（1 分）：$a,b,c\le 10^7$，保证 $mod$ 为质数

对于所有数据，$10^8\le mod\le 10^9+100,2\le n=a+b+c$

【时间限制】

前 $6$ 个 Subtask 为 $1s$，第 $7$ 个 Subtask 为 $3s$。

<br>

# 我的代码

## T1(AC)
```` C++
#include <bits/stdc++.h>
using namespace std;
string recs(string s){
	string ans="";
	for(int i=s.size()-1;i>=0;i--)
		ans+=s[i];
	return ans;
}
int main(){
	int n;
	scanf("%d",&n);
	map<string,int> mp;
	for(int i=1;i<=n;i++){
		string s1;
		cin >> s1;
		string s2 = recs(s1);
		if(mp.count(s1)>0){
			mp[s1]++;
		}
		else if(mp.count(s2)>0){
			mp[s2]++;
		}
		else{
			mp[s1] = 1;
		}
	}
	int max=0;
	map<string,int>::iterator it = mp.begin();
	for(;it!=mp.end();it++){
		if( it->second > max ) max = (it->second);
	}
	
	
	cout << max;
	
	
	return 0; 
} 
````

***

## T2(80分)
```` C++
#include <bits/stdc++.h>
using namespace std;

int n,m,q;
bool de[1005][1005];
int mp[1005][1005];

int wayx[8] = {1,-1,0,0,1,-1,1,-1};
int wayy[8] = {0,0,1,-1,-1,-1,1,1};

long long countgrey(){
	long long sum=0;
	for(int i=1;i<=n;i++)
		for(int j=1;j<=m;j++)
			if(mp[i][j]>0) sum++;
	return sum;
}
 

/*
void prtgrey(){
	long long sum=0;
	for(int i=1;i<=n;i++)
	{
		for(int j=1;j<=m;j++)
			cout << mp[i][j]<<" ";
		cout<<endl; 
	}

}
*/
int main(){
	
	cin >> n >> m >> q;
	for(int i=1;i<=q;i++){
		int x,y;
		scanf("%d %d",&x,&y);
		if(!de[x][y]) {
			de[x][y] = true;
			mp[x][y]++;
			for(int way=0;way<=7;way++){
				int nowx = x+wayx[way] ,nowy = y+wayy[way];
				if(nowx>=1 && nowy>=1 && nowx<=n && nowy<=m)
					mp[nowx][nowy]++;
			}
		}
		else{
			de[x][y] = false;
			mp[x][y]--;
			for(int way=0;way<=7;way++){
				int nowx = x+wayx[way] ,nowy = y+wayy[way];
				if(nowx>=1 && nowy>=1 && nowx<=n && nowy<=m)
					mp[nowx][nowy]--;
			}
		}
		//prtgrey();
		printf("%lld\n",countgrey());
	}
	return 0; 
} 
````
***

## T3(没来得及做完：0分)

## T4(Subtask 1、3骗分代码)
```` C++
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll a,b,c,mod;

ll simple(ll a,ll b,ll c){
	if(c==0){
		if(a!=b){return 0%mod;}
		else{return 2%mod;}
	}
	if(a==0){
		if(b!=c){return 0%mod;}
		else{return 2%mod;}
	}
	if(b==0){
		if(a!=c){return 0%mod;}
		else{return 2%mod;}
	}
}
set<string> isc;
ll ans=0;

void little(ll aa,ll bb,ll cc,string ns){
	ll siz = ns.size();
	if(siz==a+b+c){
		if(ns[0]!=ns[siz-1] &&isc.count(ns)<=0){//
			ans++;
			isc.insert(ns);
			//cout<< ns<<endl;
			ans = ans%mod;
		}
	}
	//if(aa==0 || bb==0||cc==0){
		//ll tans = simple(aa,bb,cc);
	//}
	if(siz==0){
		little(aa-1,bb,cc,ns+"1");
		little(aa,bb-1,cc,ns+"2");
		little(aa,bb,cc-1,ns+"3");
	}
	else{
		if(aa!=0 && ns[siz-1]!='1'){
			little(aa-1,bb,cc,ns+"1");
		}
		if(bb!=0 && ns[siz-1]!='2'){
			little(aa,bb-1,cc,ns+"2");
		}
		if(cc!=0 && ns[siz-1]!='3'){
			//cout<<endl<<ns[siz]<<endl<<endl<<ns+"3"<<endl<<endl;
			little(aa,bb,cc-1,ns+"3");
		}
	}
}

int main(){
	
	scanf("%lld %lld %lld %lld",&a,&b,&c,&mod);
	
	if(a==0|| b==0 || c==0){
		cout<<simple(a,b,c);
		return 0;
	}
	else{			
		little(a,b,c,"");
		cout<< ans;
		return 0;
	}
	
	return 0; 
}
````

***
<br>

# 总结
+ 对于此次比赛还是有很大的不足，至少T3没时间做就是个很大的问题，继续努力吧，只能说