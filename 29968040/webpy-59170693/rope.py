
# Rope 数据结构的一个节点
class RopeNode:
    def __init__(self, *args):
        self.data = ''  # 叶子节点的数据
        self.weight = 0  # 左子树的 weight
        self.left = None  # 左子节点
        self.right = None  # 右子节点
        
        if len(args) == 1:
            self.init_leaf(*args)
        elif len(args) == 2:
            self.init_internal(*args)

    def init_leaf(self, string):  # 叶子节点构造函数
        self.data = string
        self.weight = len(string)
        self.left = self.right = None
        return self

    def init_internal(self, left_child, right_child):  # 非叶子节点构造函数
        self.data = ''
        self.weight = 0
        self.left, self.right = left_child, right_child
        
        self.weight += left_child.weight if left_child else 0
        self.weight += right_child.weight if right_child else 0
        return self


# 返回以给定节点为根的子树中的节点数。
def count_nodes(node):
    if not node:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


def _print(node):
    if not node:
        return
    if not node.left and not node.right:
        print(node.data, end='')
    else:
        _print(node.left)
        _print(node.right)


def concatenate_strings(node, result):
    if not node:
        return result
    if not node.left and not node.right:
        result += node.data
        return result
    else:
        result = concatenate_strings(node.left, result)
        result = concatenate_strings(node.right, result)
        return result


# Add these implementations before replace()
def split(node, index, left_part, right_part):
    if not node:
        left_part = right_part = None
        return left_part, right_part

    if not node.left and not node.right:  # Leaf node
        if index >= len(node.data):
            left_part = node
            right_part = RopeNode("")
        elif index <= 0:
            left_part = RopeNode("")
            right_part = node
        else:
            left_part = RopeNode(node.data[:index])
            right_part = RopeNode(node.data[index:])
    else:
        left_weight = node.left.weight if node.left else 0
        if index < left_weight:  # Split left subtree
            temp_right = RopeNode()
            left_part, temp_right = split(node.left, index, left_part, temp_right)
            right_part = concatenate(temp_right, node.right)
        else:  # Split right subtree
            temp_left = RopeNode()
            temp_left, right_part = split(node.right, index - left_weight, temp_left, right_part)
            left_part = concatenate(node.left, temp_left)
    return left_part, right_part


def concatenate(left, right):
    if not left or left.weight == 0:
        return right
    if not right or right.weight == 0:
        return left
    return RopeNode(left, right)


def collect_leaves(node, leaves):
    if not node:
        return
    if not node.left and not node.right:
        leaves.append(node.data)
    else:
        collect_leaves(node.left, leaves)
        collect_leaves(node.right, leaves)


# 一个 Rope 数据结构，用于高效字符串操作
class Rope:
    # Rope 类的构造函数
    def __init__(self, string):
        chunk_size = 10  # 每一个 chunk 的大小
        nodes = [RopeNode(string[i: i+chunk_size]) for i in range(0, len(string), chunk_size)]

        while len(nodes) > 1:
            new_nodes = []
            for i in range(0, len(nodes), 2):
                if i + 1 < len(nodes):
                    new_nodes.append(RopeNode(nodes[i], nodes[i + 1]))
                else:
                    new_nodes.append(nodes[i])
            nodes = new_nodes

        self.root = nodes[0]  # Rope的根节点
    
    def __len__(self):
        return self.root.weight if self.root else 0

    def _print(self):
        if not self.root:
            print("Empty Rope")
            return
        _print(self.root)
        print()

    def node_count(self):
        return count_nodes(self.root)
    
    def find_all_occurrences(self, old_str):
        occurrences = []
        leaves = []
        collect_leaves(self.root, leaves)
    
        current_pos = 0;
        _buffer = ''
    
        for leaf in leaves:
            for c in leaf:
                _buffer += c
                current_pos += 1
            
                # 滚动窗口机制
                if len(_buffer) > len(old_str):
                    _buffer = _buffer[1:]
            
                if len(_buffer) == len(old_str) and _buffer == old_str:
                    start = current_pos - len(old_str)
                    occurrences.append(start)

        return occurrences

    # Replace this existing implementation
    def replace(self, old_str, new_str):
        if not old_str or old_str == new_str or not self.root:
            return

        occurrences = self.find_all_occurrences(old_str)
    
        # Process from last to first to maintain correct indices
        for it in occurrences[::-1]:
            start = it
            end = start + len(old_str)

            left_part = RopeNode()
            right_part = RopeNode()
            middle_part = RopeNode()
        
            # Split at the end of the old string
            middle_part, right_part = split(self.root, end, middle_part, right_part)
            # Split at the start of the old string
            left_part, middle_part = split(middle_part, start, left_part, middle_part)
        
            # Create new node with replacement
            new_node = RopeNode(new_str)
        
            # Rebuild the rope
            self.root = concatenate(concatenate(left_part, new_node), right_part)

    def insert(self, index, string):
        left_part = RopeNode()
        right_part = RopeNode()
        left_part, right_part = split(self.root, index, left_part, right_part)
        
        new_node = RopeNode(string)
        self.root = concatenate(concatenate(left_part, new_node), right_part)


    def __reqr__(self):
        return concatenate_strings(self.root, '')
    
    def __str__(self):
        return concatenate_strings(self.root, '')
