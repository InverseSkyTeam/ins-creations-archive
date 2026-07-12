print("下周三我要一模(emo的反义词)了")
a="""
exec(\"\"\"print('''快小学毕业考了，所以不经常来社区
来的越来越少
没空
少发消息，一看就是99+，不重要的别发，否则。。。你懂的
优质作品做不完了~~~
暑假再见！！！！！
''')
\"\"\")
"""
b = 'exec("exec(\'exec(a)\')")'
c = 'exec("exec(\'exec(b)\')")'
d = 'exec("exec(\'exec(c)\')")'
e = 'exec("exec(\'exec(d)\')")'
f = 'exec("exec(\'exec(e)\')")'
g = 'exec("exec(\'exec(f)\')")'
P0 = 'exec("exec(\'exec(g)\')")'
for i in range(100):
    exec('P'+str(i+1)+' = "exec(P'+str(i)+')"')
print(exec(P100))
del a,b,c,d,e,f,g
for i in range(101):
    exec("exec('del P'+str(i))")
print('\033[1A886!\033[1A\033[10Dbye~')