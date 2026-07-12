# 轩 list
class Queue(list):
    def push(self,x):
        self.append(x)
    def empty(self):
        return not self
    def front(self):
        return self[0]
    def pop(self):
        del self[0]
import time
queue = Queue()
t = time.time()
for i in range(100):
    for i in range(100):queue.push(1)
    for i in range(100):queue.pop()
print(time.time()-t)
t = time.time()
for i in range(10000):
    queue.push(1)
    queue.pop()
print(time.time()-t)




# 付 链表
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
import time
queue = Queue()
t = time.time()
for i in range(100):
    for i in range(100):queue.push(1)
    for i in range(100):queue.pop()
print(time.time()-t)
t = time.time()
for i in range(10000):
    queue.push(1)
    queue.pop()
print(time.time()-t)