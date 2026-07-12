import copy

class Product:
    def __init__(self, name, body):
        self.name = name
        self.body = body
    def __str__(self):
        return f"{self.name} -> {' '.join(self.body)}"
    __repr__ = __str__

class Item:
    def __init__(self, product, pos, begin):
        self.product = product
        self.pos = pos
        self.begin = begin
    def __str__(self):
        return f"{self.product.name} -> {' '.join(self.product.body[:self.pos])}·{' '.join(self.product.body[self.pos:])}"
    __repr__ = __str__
    def __eq__(self, other):
        return self.product.name == other.product.name and self.product.body == other.product.body and self.pos == other.pos and self.begin == other.begin

class Token:
    def __init__(self, tp, value):
        self.tp = tp
        self.value = value
    def __str__(self):
        return f"{self.tp} {self.value}"
    __repr__ = __str__

class TreeNode:
    def __init__(self, name):
        self.name = name
        self.products = []
class ProductNode:
    def __init__(self, item):
        self.item = item
        self.children = []

class Group:
    def __init__(self, pos, state, group, token_num):
        self.pos = pos
        self.state = state
        self.group = group
        self.token_num = token_num

def nullable(name, patterns):
    if name not in patterns:
        return False
    res = True
    for product in patterns[name]:
        is_null = True
        for term in product.body:
            is_null &= nullable(term, patterns)
        res |= is_null

def recognize(patterns, lexer):
    state0 = [Item(p, 0, 0) for p in patterns["S"]]
    for item in state0:
        if item.pos == len(item.product.body):
            for completed in state0:
                if completed.pos < len(completed.product.body) and completed.product.body[completed.pos] == item.product.name:
                    new_item = Item(completed.product, completed.pos+1, completed.begin)
                    if new_item not in state0:
                        state0.append(new_item)
            continue
        if item.product.body[0] in patterns:
            for product in patterns[item.product.body[0]]:
                    new_item = Item(product, 0, 0)
                    if new_item not in state0:
                        state0.append(new_item)
        if item.product.body[item.pos] in patterns:
            for product in patterns[item.product.body[item.pos]]:
                new_item = Item(product, 0, 0)
                if new_item not in state0:
                    state0.append(new_item)
    state_list = [state0]
    token = lexer.lex()
    index = 0
    token_list = [token]
    while token:
        index += 1
        state = []
        state_list.append(state)
        for item in state_list[-2]:
            if item.pos < len(item.product.body) and item.product.body[item.pos] == token.tp:
                new_item = Item(item.product, item.pos+1, item.begin)
                if new_item not in state:
                    state.append(new_item)
        for item in state:
            if item.pos == len(item.product.body):
                for completed in state_list[item.begin]:
                    if completed.pos < len(completed.product.body) and completed.product.body[completed.pos] == item.product.name:
                        new_item = Item(completed.product, completed.pos+1, completed.begin)
                        if new_item not in state:
                            state.append(new_item) 
            elif item.product.body[item.pos] in patterns:
                for product in patterns[item.product.body[item.pos]]:
                    new_item = Item(product, 0, 0)
                    if new_item not in state:
                        state.append(new_item)
                if nullable(item.product.body[item.pos], patterns):
                    new_item = Item(item.product, item.pos+1, item.begin)
                    if new_item not in state:
                        state.append(new_item)
        token = lexer.lex()
        if token:
            token_list.append(token)
    return state_list, token_list

def parse(state_list, token_list, terminals):
    table = [[] for _ in range(len(state_list))]
    for i, state in enumerate(state_list):
        for item in state:
            if item.pos == len(item.product.body):
                table[item.begin].append(Item(item.product, item.pos, i))
    main_tree = TreeNode("S")
    groups = [Group(0, 0, [main_tree], 0)]
    forest_pool = {}
    while groups:
        new_groups = []
        for group in groups:
            if group.token_num == len(token_list):
                continue
            if group.pos >= len(group.group):
                if group.group:
                    new_group = Group(0, 0, group.group, group.token_num)
                    new_groups.append(new_group)
                continue
            node = group.group[group.pos]
            if isinstance(node, Token):
                if node.tp == token_list[group.state].tp:
                    new_group = Group(group.pos+1, group.state+1, group.group, group.token_num+1)
                    new_groups.append(new_group)
            else:
                if (item.product.name, group.state) in forest_pool:
                    node.products = forest_pool[(item.product.name, group.state)].products
                    continue
                for item in table[group.state]:
                    if item.product.name == node.name:
                        item_node = ProductNode(item)
                        node.products.append(item_node)
                        new_nodes = [TreeNode(term) if term not in terminals else token_list[group.state] for term in item.product.body]
                        item_node.children = new_nodes
                        new_group = Group(group.pos+len(item.product.body), item.begin, group.group[:group.pos] + new_nodes + group.group[group.pos+1:], group.token_num)
                        new_groups.append(new_group)
                forest_pool[(item.product.name, group.state)] = node
        groups = new_groups
    return main_tree

text = ""
index = 0
class Lexer:
    def lex():
        global index
        if index >= len(text):
            return None
        else:
            res = Token(text[index], None)
            index += 1
            return res
terminals = []
patterns = {
    "S": [
        Product("S", ["A"])
    ],
    "A": [
        Product("A", ["A"]),
        Product("A", [])
    ]
}

state_list, token_list = recognize(patterns, Lexer)
tree = parse(state_list, token_list, terminals)
print(tree)