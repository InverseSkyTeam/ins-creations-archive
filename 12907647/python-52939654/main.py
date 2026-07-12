import pygame,sys
pygame.init()
pygame.key.stop_text_input()

a = pygame.Rect(0,0,100,100)
b = pygame.Rect(100,0,100,100)

print(a.right,b.left,b.colliderect(a))
print('被恶心到了，之前写的碰撞箱一直不好就是因为这个！')
print('能否这么理解：a占有0px~99px,所以长度为100px，但是因为左闭右开，a.right不是99而是100')