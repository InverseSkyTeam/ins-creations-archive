input('''我们可以用递归算法
def ok():
    ok()
ok()
结果：
...
  [Previous line repeated 996 more times]
RecursionError: maximum recursion depth exceeded
可以看到，无限递归让python报错了
一报错就是1000次错误（因为python最大递归限制是1000次）

回车继续
''')
input('''接下来我看看能不能超过递归限制：除错。
这种方法是让python意识不到我在递归
所以我来看看超级递归会发生神马
def ok():
    try:ok()
    except:hello()
def hello():
    print("666")
ok()
结果：
666
可以看到，无限递归后我使用了除错机制，让它去运行hello函数
成功突破限制

回车继续
''')
input('''然后我们就能刷内存了
能把1个函数刷到1000次递归，1000次出错后再来一千次重复效果
就是1000*1000=100w次，然后100w再滚上1000次，变10亿次，1w亿次，1000w亿次。。。
def ok():
    try:ok()
    except:hello()
def hello():
    ok()
ok()
结果运行到一半，出现了我几年以来从未发生过的报错！！！！！！

回车继续
''')
input('''\033[1;31mFatal Python error: Cannot recover from stack overflow.

Current thread 0x000020ac (most recent call first):
  File "路径/main.py", line 2 in ok
  File "路径/main.py", line 2 in ok
  File "路径/main.py", line 2 in ok
  File "路径/main.py", line 2 in ok
  File "路径/main.py", line 2 in ok
  File "路径/main.py", line 2 in ok
  File "路径/main.py", line 2 in ok
  ...

没错，python它崩溃了，
翻译：致命的Python错误:
无法从堆栈溢出中恢复。 
当前线程0x000020ac(最近的调用优先): 
文件"路径/main.py "，第2行ok

回车继续
''')
print('代码在改编里，在底下注释的部分，可以自行运行哟~')

# def ok():
#     try:ok()
#     except:hello()
# def hello():
#     ok()
# ok()