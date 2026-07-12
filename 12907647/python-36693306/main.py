import test
print(test.randint(1,100))
print(test.random())
print(test.randrange(1,100))
input('按回车查看源代码(含注释、空行、测试778行)')
with open('test.py','r',encoding='utf-8') as f:
    print(f.read())
    f.close()
print('\n\n\n懂python的知道，这里random的代码写出来的随机数并不是完全随机，而是靠一定的数学成分来计算一个随机的（虽然随机依靠了一些cmd的功劳），详细请看源代码与素材。题目只是闹梗，当然不是我做的，但是计算出来的随机库，我们还要吗？当然，因为只有一个随机库！！！')