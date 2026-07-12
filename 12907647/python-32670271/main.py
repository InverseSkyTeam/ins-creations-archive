from random import choice as c
text = c(['w','a','d'])
print(text)
while input() == text:
    print('程序继续')
    text = c(['w','a','d'])
    print(text)
print('程序终止')