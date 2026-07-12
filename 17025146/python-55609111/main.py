class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value
    def __eq__(self, other):
        return self.type == other.type and self.value == other.value
class Node:
    def __init__(self, name, children):
        self.name = name
        self.children = children

    def __eq__(self, other):
        return self.name == other.name and self.children == other.children

class Visitor:
    def __init__(self):
        pass
    def visit(self, node):
        node_stack = [node]
        index_stack = [0]
        value_stack = []
        while node_stack:
            node, index = node_stack[-1], index_stack[-1]
            if isinstance(node, Token):
                value_stack.append(node)
                node_stack.pop()
                index_stack.pop()
                index_stack[-1] += 1
                continue
            if len(node.children) == index:
                args = [value_stack.pop() for _ in range(index)]
                res = getattr(self, f"visit_{node.name}")(*args)
                value_stack.append(res)
                node_stack.pop()
                index_stack.pop()
                if index_stack:
                    index_stack[-1] += 1
            else:
                node_stack.append(node.children[index])
                index_stack.append(0)
        return value_stack.pop()
    
class TreeVisitor(Visitor):
    def visit_add(self, left, right):
        return left + right
    def visit_sub(self, left, right):
        return left - right
    def visit_mul(self, left, right):
        return left * right
    def visit_div(self, left, right):
        return left / right
    def visit_num(self, token):
        return int(token.value)

tree = Node("add", [Node("num", [Token("number", 1)]), Node("mul", [Node("num", [Token("number", 2)]), Node("num", [Token("number", 3)])])])

visitor = TreeVisitor()
print(visitor.visit(tree))