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
