# 轩 list
class Queue(list):
    def push(self,x):
        self.append(x)
    def empty(self):
        return not self
    def front(self):
        return self[0]
    def pop(self):
        self.remove(self[0])
print("小轩测试")
print('占用空间少，用完即废除(适用中小型bfs)')
import time
queue = Queue()
t = time.time()
for i in range(100):
    for i in range(100):queue.push(1)
    for i in range(100):queue.pop()
print(f'{round((time.time()-t)*1000,4)}ms')
t = time.time()
for i in range(10000):
    queue.push(1)
    queue.pop()
print(f'{round((time.time()-t)*1000,4)}ms')

queue = Queue()
t = time.time()
for i in range(100):
    for i in range(100):queue.push(1)
    for i in range(100):queue.pop()
print(f'{round((time.time()-t)*1000,4)}ms')
t = time.time()
for i in range(100000):
    queue.push(1)
for i in range(100000):
    queue.pop()
print(f'{round((time.time()-t)*1000,4)}ms')

t = time.time()
queue.push(1)
for i in range(100000):
    a = queue.empty()
for i in range(100000):
    a = queue.front()
print(f'{round((time.time()-t)*1000,4)}ms')

# 付 链表
print()
class Node:
    def __init__(self, value, next=None):
        self.value, self.next = value, next
class Queue:
    def __init__(self):
        self.node = None
        self.end_node = None
    def push(self, value):
        if self.node == None:
            self.node = Node(value, None)
            self.end_node = self.node
        else:
            self.end_node.next = Node(value, None)
            self.end_node = self.end_node.next
    def pop(self):
        if self.node != None:
            self.node = self.node.next
        else:
            raise Exception()
    def empty(self):
        return self.node == None
    def front(self):
        return self.node.value
print("付开霁测试")
print('占用空间中等，用完可以转换，直接删除链表会断(适用快速查删，大型bfs)')
import time
queue = Queue()
t = time.time()
for i in range(100):
    for i in range(100):queue.push(1)
    for i in range(100):queue.pop()
print(f'{round((time.time()-t)*1000,4)}ms')
t = time.time()
for i in range(10000):
    queue.push(1)
    queue.pop()
print(f'{round((time.time()-t)*1000,4)}ms')

queue = Queue()
t = time.time()
for i in range(100):
    for i in range(100):queue.push(1)
    for i in range(100):queue.pop()
print(f'{round((time.time()-t)*1000,4)}ms')
t = time.time()
for i in range(100000):
    queue.push(1)
for i in range(100000):
    queue.pop()
print(f'{round((time.time()-t)*1000,4)}ms')

t = time.time()
queue.push(1)
for i in range(100000):
    a = queue.empty()
for i in range(100000):
    a = queue.front()
print(f'{round((time.time()-t)*1000,4)}ms')

#林 爆（内存）表
print()
class Queue:
    def __init__(self,a=[]):
        self.bl   = 0
        self.dl   = 0
        self.data = a
    def push(self,a):
        self.data.append(a)
        self.dl+= 1
    def pop(self):
        if self.empty():
            self.bl+= 1
    def empty(self):
        return self.dl-self.bl==0
    def front(self):
        return self.data[self.bl]
print("林林测试")
print('占用空间巨大，只能移动指针，非真正的删除(在不需要极限算力情况下不推荐)')
import time
queue = Queue()
t = time.time()
for i in range(100):
    for i in range(100):queue.push(1)
    for i in range(100):queue.pop()
print(f'{round((time.time()-t)*1000,4)}ms')
t = time.time()
for i in range(10000):
    queue.push(1)
    queue.pop()
print(f'{round((time.time()-t)*1000,4)}ms')

queue = Queue()
t = time.time()
for i in range(100):
    for i in range(100):queue.push(1)
    for i in range(100):queue.pop()
print(f'{round((time.time()-t)*1000,4)}ms')
t = time.time()
for i in range(100000):
    queue.push(1)
for i in range(100000):
    queue.pop()
print(f'{round((time.time()-t)*1000,4)}ms')

t = time.time()
queue.push(1)
for i in range(100000):
    a = queue.empty()
for i in range(100000):
    a = queue.front()
print(f'{round((time.time()-t)*1000,4)}ms')

#王 内置
print()
class Queue:
    def __init__(self):
        self.__r = 0
        self.__l = 0
        self.__list = []
        self.__length = 0
    def push(self,x):
        self.__list.append(x)
        self.__l += 1
        self.__length += 1
    def pop(self):
        if self.__length > 0:
            self.__r += 1
            self.__length -= 1
    def front(self):
        try:
            return self.__list[self.__r]
        except:
            return None
    def back(self):
        try:
            return self.__list[self.__l]
        except:
            return None
    def size(self):
        return self.__length
    def empty(self):
        return not self.__list
print("王祎嘉测试")
print('占用空间爆炸，只能移动指针，非真正的删除(功能多，速度快，内置list，但内存效率不高)')
import time
queue = Queue()
t = time.time()
for i in range(100):
    for i in range(100):queue.push(1)
    for i in range(100):queue.pop()
print(f'{round((time.time()-t)*1000,4)}ms')
t = time.time()
for i in range(10000):
    queue.push(1)
    queue.pop()
print(f'{round((time.time()-t)*1000,4)}ms')

queue = Queue()
t = time.time()
for i in range(100):
    for i in range(100):queue.push(1)
    for i in range(100):queue.pop()
print(f'{round((time.time()-t)*1000,4)}ms')
t = time.time()
for i in range(100000):
    queue.push(1)
for i in range(100000):
    queue.pop()
print(f'{round((time.time()-t)*1000,4)}ms')

t = time.time()
queue.push(1)
for i in range(100000):
    a = queue.empty()
for i in range(100000):
    a = queue.front()
print(f'{round((time.time()-t)*1000,4)}ms')

print('\n\n\n全部用xes服务器linux标准计算')