class Queue(list):
    def push(self,x):
        self.append(x)
    def empty(self):
        return not self
    def front(self):
        return self[0]
    def pop(self):
        del self[0]
queue = Queue()
print(queue.empty())
queue.push(1)
queue.push(2)
queue.push(3)
queue.pop()
print(queue,queue.front(),sep='\n')
print('c++ bfs queue 魔怔')