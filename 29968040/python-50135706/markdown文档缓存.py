<h1>[春季测试 2023] 涂色游戏</h1>
<h2>题目描述</h2>
<p>有一天，小 D 在刷朋友圈时看到了一段游戏视频。</p>
<p>这个游戏的名字叫涂色游戏，视频中的游戏界面是一个 <span class="math inline">n</span> 行 <span class="math inline">m</span> 列的网格，初始时每一个格子都是白色（用数字 <span class="math inline">0</span> 表示）。其中每一行的左侧、每一列的上方都有一把带颜色的刷子。玩家点击某个刷子后，这个刷子会将其右侧（或下方）的一整行（或一整列）涂上同一种颜色，<strong>该行（或该列）格子原有的颜色都会被覆盖成新涂上的颜色。</strong></p>
<p>下图展示的情况可以通过先将第一列涂成红色，然后将第一行涂成蓝色得到，若此时选择将第三列涂成绿色，则图中绿色方框中的格子都会变成绿色。</p>
<p><img src="https://cdn.luogu.com.cn/upload/image_hosting/dc71alkw.png" /></p>
<p>小 D 想用他自己编写的程序来进行视频中的游戏。在编程的过程中，小 D 在涂色逻辑的实现上却遇到了一些困难，于是他向你求助，希望你能帮他完成实现涂色逻辑部分的代码。</p>
<p>首先，小 D 会给你网格的行数和列数 <span class="math inline">n, m</span>，然后给出 <span class="math inline">q</span> 次操作，每次操作用三个整数 <span class="math inline">opt_i, x_i, c_i</span> 表示：</p>
<ul>
<li>如果 <span class="math inline">opt_i=0</span>，那么这次操作会将第 <span class="math inline">x_i</span> <strong>行</strong>涂成颜色 <span class="math inline">c_i</span>。</li>
<li>如果 <span class="math inline">opt_i=1</span>，那么这次操作会将第 <span class="math inline">x_i</span> <strong>列</strong>涂成颜色 <span class="math inline">c_i</span>。</li>
</ul>
<p>在所有涂色操作结束以后，你需要输出网格中每个位置的颜色是什么。</p>
<h2>输入格式</h2>
<p><strong>本题有多组测试数据。</strong></p>
<p>第一行包含一个正整数 <span class="math inline">T</span>，表示数据组数。</p>
<p>接下来一共 <span class="math inline">T</span> 组数据，每组数据格式如下：</p>
<p>第一行包含三个整数 <span class="math inline">n, m, q</span>，分别表示涂色板的行数、列数，以及小 D 进行涂色操作的次数。</p>
<p>接下来 <span class="math inline">q</span> 行，每行包含三个整数 <span class="math inline">opt_i, x_i, c_i</span>，表示一次操作。</p>
<h2>输出格式</h2>
<p>对于每组数据，输出 <span class="math inline">n</span> 行，每行 <span class="math inline">m</span> 个由单个空格隔开的整数。</p>
<p>其中第 <span class="math inline">i</span> 行第 <span class="math inline">j</span> 个整数表示涂色完成后网格中第 <span class="math inline">i</span> 行第 <span class="math inline">j</span> 列的方格是什么颜色。</p>
<h2>样例 #1</h2>
<h3>样例输入 #1</h3>
<pre><code>2
5 5 9
1 5 1
0 4 0
1 4 1
0 3 0
1 3 1
0 2 0
1 2 1
0 1 0
1 1 1
3 3 3
0 1 2
0 3 1
1 1 3</code></pre>
<h3>样例输出 #1</h3>
<pre><code>1 0 0 0 0
1 1 0 0 0
1 1 1 0 0
1 1 1 1 0
1 1 1 1 1
3 2 2
3 0 0
3 1 1</code></pre>
<h2>提示</h2>
<p><strong>【样例 1 解释】</strong></p>
<p>注意当一个格子没有被涂色时，其颜色为白色，用数字 <span class="math inline">0</span> 表示。</p>
<p><strong>【样例 2】</strong></p>
<p>见选手目录下的 paint/paint2.in 与 paint/paint2.ans。</p>
<p><strong>【数据范围】</strong></p>
<p>对于所有数据，保证：</p>
<ul>
<li><span class="math inline">1 \leq T \leq 10</span>，<span class="math inline">1 \leq n,m \leq 10^5</span>，<span class="math inline">0 \leq q \leq 10^5</span>，<span class="math inline">0 \leq c_i \leq 10^9</span>。</li>
<li>若 <span class="math inline">opt_i=0</span>，则 <span class="math inline">1 \leq x_i \leq n</span>；若 <span class="math inline">opt_i=1</span>，则 <span class="math inline">1 \leq x_i \leq m</span>。</li>
<li>单个测试点中所有数据的 <span class="math inline">n \cdot m</span> 的总和不超过 <span class="math inline">10^6</span>，<span class="math inline">q</span> 的总和不超过 <span class="math inline">10^6</span>。</li>
</ul>
<table>
<thead>
<tr class="header">
<th style="text-align: center;">测试点</th>
<th style="text-align: center;"><span class="math inline">n \le</span></th>
<th style="text-align: center;"><span class="math inline">m \le</span></th>
<th style="text-align: center;"><span class="math inline">q \le</span></th>
<th style="text-align: center;">性质 A</th>
<th style="text-align: center;">性质 B</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: center;">1</td>
<td style="text-align: center;"><span class="math inline">1</span></td>
<td style="text-align: center;"><span class="math inline">1</span></td>
<td style="text-align: center;"><span class="math inline">0</span></td>
<td style="text-align: center;">√</td>
<td style="text-align: center;">√</td>
</tr>
<tr class="even">
<td style="text-align: center;">2</td>
<td style="text-align: center;"><span class="math inline">1</span></td>
<td style="text-align: center;"><span class="math inline">1</span></td>
<td style="text-align: center;"><span class="math inline">1</span></td>
<td style="text-align: center;">√</td>
<td style="text-align: center;">√</td>
</tr>
<tr class="odd">
<td style="text-align: center;">3</td>
<td style="text-align: center;"><span class="math inline">1</span></td>
<td style="text-align: center;"><span class="math inline">10</span></td>
<td style="text-align: center;"><span class="math inline">20</span></td>
<td style="text-align: center;">√</td>
<td style="text-align: center;">√</td>
</tr>
<tr class="even">
<td style="text-align: center;">4</td>
<td style="text-align: center;"><span class="math inline">1</span></td>
<td style="text-align: center;"><span class="math inline">10^5</span></td>
<td style="text-align: center;"><span class="math inline">10^5</span></td>
<td style="text-align: center;">×</td>
<td style="text-align: center;">√</td>
</tr>
<tr class="odd">
<td style="text-align: center;">5</td>
<td style="text-align: center;"><span class="math inline">1</span></td>
<td style="text-align: center;"><span class="math inline">10^5</span></td>
<td style="text-align: center;"><span class="math inline">10^5</span></td>
<td style="text-align: center;">×</td>
<td style="text-align: center;">√</td>
</tr>
<tr class="even">
<td style="text-align: center;">6</td>
<td style="text-align: center;"><span class="math inline">1</span></td>
<td style="text-align: center;"><span class="math inline">10^5</span></td>
<td style="text-align: center;"><span class="math inline">10^5</span></td>
<td style="text-align: center;">×</td>
<td style="text-align: center;">×</td>
</tr>
<tr class="odd">
<td style="text-align: center;">7</td>
<td style="text-align: center;"><span class="math inline">10</span></td>
<td style="text-align: center;"><span class="math inline">10</span></td>
<td style="text-align: center;"><span class="math inline">20</span></td>
<td style="text-align: center;">√</td>
<td style="text-align: center;">√</td>
</tr>
<tr class="even">
<td style="text-align: center;">8</td>
<td style="text-align: center;"><span class="math inline">50</span></td>
<td style="text-align: center;"><span class="math inline">50</span></td>
<td style="text-align: center;"><span class="math inline">100</span></td>
<td style="text-align: center;">√</td>
<td style="text-align: center;">√</td>
</tr>
<tr class="odd">
<td style="text-align: center;">9</td>
<td style="text-align: center;"><span class="math inline">50</span></td>
<td style="text-align: center;"><span class="math inline">50</span></td>
<td style="text-align: center;"><span class="math inline">100</span></td>
<td style="text-align: center;">√</td>
<td style="text-align: center;">×</td>
</tr>
<tr class="even">
<td style="text-align: center;">10</td>
<td style="text-align: center;"><span class="math inline">1000</span></td>
<td style="text-align: center;"><span class="math inline">1000</span></td>
<td style="text-align: center;"><span class="math inline">2000</span></td>
<td style="text-align: center;">×</td>
<td style="text-align: center;">√</td>
</tr>
<tr class="odd">
<td style="text-align: center;">11</td>
<td style="text-align: center;"><span class="math inline">1000</span></td>
<td style="text-align: center;"><span class="math inline">1000</span></td>
<td style="text-align: center;"><span class="math inline">2000</span></td>
<td style="text-align: center;">×</td>
<td style="text-align: center;">×</td>
</tr>
<tr class="even">
<td style="text-align: center;">12</td>
<td style="text-align: center;"><span class="math inline">1000</span></td>
<td style="text-align: center;"><span class="math inline">1000</span></td>
<td style="text-align: center;"><span class="math inline">2000</span></td>
<td style="text-align: center;">×</td>
<td style="text-align: center;">×</td>
</tr>
<tr class="odd">
<td style="text-align: center;">13</td>
<td style="text-align: center;"><span class="math inline">1000</span></td>
<td style="text-align: center;"><span class="math inline">1000</span></td>
<td style="text-align: center;"><span class="math inline">10^5</span></td>
<td style="text-align: center;">×</td>
<td style="text-align: center;">×</td>
</tr>
<tr class="even">
<td style="text-align: center;">14</td>
<td style="text-align: center;"><span class="math inline">1000</span></td>
<td style="text-align: center;"><span class="math inline">1000</span></td>
<td style="text-align: center;"><span class="math inline">10^5</span></td>
<td style="text-align: center;">×</td>
<td style="text-align: center;">×</td>
</tr>
<tr class="odd">
<td style="text-align: center;">15</td>
<td style="text-align: center;"><span class="math inline">10^5</span></td>
<td style="text-align: center;"><span class="math inline">10^5</span></td>
<td style="text-align: center;"><span class="math inline">10^5</span></td>
<td style="text-align: center;">√</td>
<td style="text-align: center;">√</td>
</tr>
<tr class="even">
<td style="text-align: center;">16</td>
<td style="text-align: center;"><span class="math inline">10^5</span></td>
<td style="text-align: center;"><span class="math inline">10^5</span></td>
<td style="text-align: center;"><span class="math inline">10^5</span></td>
<td style="text-align: center;">√</td>
<td style="text-align: center;">√</td>
</tr>
<tr class="odd">
<td style="text-align: center;">17</td>
<td style="text-align: center;"><span class="math inline">10^5</span></td>
<td style="text-align: center;"><span class="math inline">10^5</span></td>
<td style="text-align: center;"><span class="math inline">10^5</span></td>
<td style="text-align: center;">√</td>
<td style="text-align: center;">×</td>
</tr>
<tr class="even">
<td style="text-align: center;">18</td>
<td style="text-align: center;"><span class="math inline">10^5</span></td>
<td style="text-align: center;"><span class="math inline">10^5</span></td>
<td style="text-align: center;"><span class="math inline">10^5</span></td>
<td style="text-align: center;">√</td>
<td style="text-align: center;">×</td>
</tr>
<tr class="odd">
<td style="text-align: center;">19</td>
<td style="text-align: center;"><span class="math inline">10^5</span></td>
<td style="text-align: center;"><span class="math inline">10^5</span></td>
<td style="text-align: center;"><span class="math inline">10^5</span></td>
<td style="text-align: center;">×</td>
<td style="text-align: center;">×</td>
</tr>
<tr class="even">
<td style="text-align: center;">20</td>
<td style="text-align: center;"><span class="math inline">10^5</span></td>
<td style="text-align: center;"><span class="math inline">10^5</span></td>
<td style="text-align: center;"><span class="math inline">10^5</span></td>
<td style="text-align: center;">×</td>
<td style="text-align: center;">×</td>
</tr>
</tbody>
</table>
<p>特殊性质 A：保证测试点中所有的 <span class="math inline">q \cdot \max(n, m)</span> 之和不超过 <span class="math inline">10^7</span>。</p>
<p>特殊性质 B：保证 <span class="math inline">opt_i = 1</span>。</p>
<p><strong>【提示】</strong></p>
<p>数据千万条，清空第一条。多测不清空，爆零两行泪。</p>