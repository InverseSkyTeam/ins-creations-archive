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


queue = Queue()
print(queue.empty())
queue.push(1)
queue.push(2)
queue.push(3)
queue.pop()
print(queue,queue.front(),sep='\n')
print('c++ bfs queue 魔怔')
