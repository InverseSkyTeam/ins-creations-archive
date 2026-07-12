input('xes linux安装了py3.6，不支持最新queue库，所以只能勉强使用高阶的3.7运行\nEnter开始(由于非服务器运行可能导致不同人的的电脑结果偏差较大)')
# 轩 list
print()
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

# 付 杂交
print()
class Queue:
    def __init__(self):
        self.data = []
        self.start = 0
        self.CONST = 1024
        
    def push(self, v):
        self.data.append(v)
        
    def empty(self):
        return self.start == len(self.data)
        
    def pop(self):
        self.start += 1
        if self.start > self.CONST:
            del self.data[:self.start]
            self.start = 0
        
    def front(self):
        return self.data[self.start]
print("付开霁杂法测试")
print('总评：不错，但你永远打不过真神再现（而且有最大限度，超过就自动删除，不稳定）')
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

print()
from queue import Queue
print('标准库queue测试')
import time
queue = Queue()
t = time.time()
for i in range(100):
    for i in range(100):queue.put_nowait(1)
    for i in range(100):queue.get_nowait()
print(f'{round((time.time()-t)*1000,4)}ms')
t = time.time()
for i in range(10000):
    queue.put_nowait(1)
    queue.get_nowait()
print(f'{round((time.time()-t)*1000,4)}ms')

queue = Queue()
t = time.time()
for i in range(100):
    for i in range(100):queue.put_nowait(1)
    for i in range(100):queue.get_nowait()
print(f'{round((time.time()-t)*1000,4)}ms')
t = time.time()
for i in range(100000):
    queue.put_nowait(1)
for i in range(100000):
    queue.get_nowait()
print(f'{round((time.time()-t)*1000,4)}ms')

for i in range(100000):queue.put_nowait(1)
t = time.time()
for i in range(100000):
    a = queue.empty()
for i in range(100000):
    a = queue.get()
print(f'{round((time.time()-t)*1000,4)}ms')

print()
from queue import SimpleQueue as Queue
print('标准库queue.simplequeue测试')
import time
queue = Queue()
t = time.time()
for i in range(100):
    for i in range(100):queue.put_nowait(1)
    for i in range(100):queue.get_nowait()
print(f'{round((time.time()-t)*1000,4)}ms')
t = time.time()
for i in range(10000):
    queue.put_nowait(1)
    queue.get_nowait()
print(f'{round((time.time()-t)*1000,4)}ms')

queue = Queue()
t = time.time()
for i in range(100):
    for i in range(100):queue.put_nowait(1)
    for i in range(100):queue.get_nowait()
print(f'{round((time.time()-t)*1000,4)}ms')
t = time.time()
for i in range(100000):
    queue.put_nowait(1)
for i in range(100000):
    queue.get_nowait()
print(f'{round((time.time()-t)*1000,4)}ms')

for i in range(100000):queue.put_nowait(1)
t = time.time()
for i in range(100000):
    a = queue.empty()
for i in range(100000):
    a = queue.get()
print(f'{round((time.time()-t)*1000,4)}ms')

print()
from collections import deque
print('小轩化简queue.simplequeue(相当于直接使用collections的deque，没有资源节约，速度稍慢)')
import time
class Queue:
    def __init__(self):
        self._queue = deque()
    def push(self, item):
        self._queue.append(item)
    def pop(self):
        return self._queue.popleft()
    def empty(self):
        return not self._queue

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

for i in range(100000):queue.push(1)
t = time.time()
for i in range(100000):
    a = queue.empty()
for i in range(100000):
    a = queue.pop()
print(f'{round((time.time()-t)*1000,4)}ms')

print()
from collections import deque
print('真神再现collections.deque(最佳辅助:c++)速度爆杀')
queue = deque()
t = time.time()
for i in range(100):
    for i in range(100):queue.append(1)
    for i in range(100):queue.popleft()
print(f'{round((time.time()-t)*1000,4)}ms')
t = time.time()
for i in range(10000):
    queue.append(1)
    queue.popleft()
print(f'{round((time.time()-t)*1000,4)}ms')

queue = deque()
t = time.time()
for i in range(100):
    for i in range(100):queue.append(1)
    for i in range(100):queue.popleft()
print(f'{round((time.time()-t)*1000,4)}ms')
t = time.time()
for i in range(100000):
    queue.append(1)
for i in range(100000):
    queue.popleft()
print(f'{round((time.time()-t)*1000,4)}ms')

for i in range(100000):queue.append(1)
t = time.time()
for i in range(100000):
    a = not queue
for i in range(100000):
    a = queue.popleft()
print(f'{round((time.time()-t)*1000,4)}ms')

print('\n\n\n备选：collections.deque(5项全部碾压)')