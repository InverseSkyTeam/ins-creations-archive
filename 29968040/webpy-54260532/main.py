#-*-coding:utf8;-*-
#qpy:console

class PriorityQueue:
    def __init__(self):
        self.heap = []  # 初始化堆
        
    @staticmethod
    def compare(a, b):
        return a < b
    
    @staticmethod
    def get_value(element):
        return element  # [0]
    
    @staticmethod
    def l_child_index(p_index):  # 获取左子节点的索引
        return (p_index << 1) + 1
    
    @staticmethod
    def r_child_index(p_index):  # 获取右子节点的索引
        return (p_index << 1) + 2
   
    @staticmethod
    def parent_index(c_index):  # 获取父节点索引
        return (c_index - 1) >> 1
    
    def swap(self, i1, i2):
        self.heap[i1], self.heap[i2] = self.heap[i2], self.heap[i1]
    
    def size(self):
        return len(self.heap)
    
    def empty(self):
        return len(self.heap) == 0
        
    def heapify_up(self):
        index = len(self.heap) - 1
        while index > 0:
            element = self.heap[index]
            p_index = self.parent_index(index)
            parent = self.heap[p_index]
            if self.compare(self.get_value(element), self.get_value(parent)):
                self.swap(index, p_index)
                index = p_index
            else:
                break
    
    def heapify_down(self):
        index = 0
        length = len(self.heap)
        element = self.heap[index]
        while 1:
            l_index, r_index = self.l_child_index(index), self.r_child_index(index)
            swap_index = None
            if l_index < length:
                l_child = self.heap[l_index]
                if self.compare(self.get_value(l_child), self.get_value(element)):
                    swap_index = l_index
            if r_index < length:
                r_child = self.heap[r_index]
                if (swap_index is None and self.compare(self.get_value(r_child), self.get_value(element))) or \
                        (swap_index is not None and self.compare(self.get_value(r_child), self.get_value(l_child))):
                    swap_index = r_index
            if swap_index is None:
                break
            self.swap(index, swap_index)
            index = swap_index
    
    def get_median(self):
        size = self.size()
        if size == 0:
            return None
        return self.heap[size//2]
    
    def push(self, obj):
        self.heap.append(obj)
        self.heapify_up()
    
    def top(self):
        return self.heap[0]
    
    def pop(self):
        min_element = self.heap[0]
        last_element = self.heap.pop()
        if len(self.heap):
            self.heap[0] = last_element
            self.heapify_down()
        return min_element


queue = PriorityQueue()
# n = int(input())
for i in map(int, input('输入要排序的数字（以空格分隔）: ').split()):
    queue.push(i)
print('排序结果:', end=' ')
while not queue.empty():
    print(queue.pop(), end=' ')         
