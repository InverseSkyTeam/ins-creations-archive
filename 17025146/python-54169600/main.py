class Product:
    def __init__(self, name, body):
        self.name = name
        self.body = body
    def __str__(self):
        return f"{self.name} -> {''.join(self.body)}"
    __repr__ = __str__
    def _eq__(self, other):
        return self.name == other.name and self.body == other.body

class Item:
    STATUS = -1
    def __init__(self, product, pos, follow):
        Item.STATUS += 1
        self.status = Item.STATUS
        self.product = product
        self.pos = pos
        self.follow = follow
    def __str__(self):
        return f"{self.product} {self.pos} {self.follow}"
    __repr__ = __str__
    def __eq__(self, other):
        return self.product == other.product and self.pos == other.pos and self.follow == other.follow

class State:
    STATUS = -1
    def __init__(self, items):
        State.STATUS += 1
        self.status = State.STATUS
        self.items = items

def first(product, terminal, nonterminal):
    if product == "ε":
        return {"ε"}
    if product[0] == "ε":
        product = product[1:]
    if product[-1] == "$":
        product = product[:-1]
    if not product:
        return {"$"}
    if product in terminal:
        return {product}
    if product not in nonterminal:
        return {"ε"}
    products = nonterminal[product]
    first_set = set()
    for product in products:
        for term in product.body:
            if term in terminal:
                first_set.add(term)
                break
            term_set = first(term, terminal, nonterminal)
            first_set.update(term_set - {"ε"})
            if "ε" not in term_set:
                break
        else:
            first_set.add("ε")
    return first_set

def follow(product, terminal, nonterminal):
    follow_set = set()
    if product == "S":
        follow_set.add("$")
    for name, experissions in nonterminal.items():
        if name == product:
            continue
        for experission in experissions:
            for index, term in enumerate(experission.body):
                if term == product:
                    if index != len(experission.body) - 1:
                        first_set = first(experission.body[index+1], terminal, nonterminal)
                        follow_set.update(first_set - {"ε"})
                        if "ε" in first_set:
                            follow_set.update(follow(name, terminal, nonterminal))
                    else:
                        follow_set.update(follow(name, terminal, nonterminal))
    return follow_set

def closure(items, terminal, nonterminal):
    if not items:
        return []
    closure_set = [*items]
    index = 0
    next_ = closure_set[index]
    while next_ and next_.pos < len(next_.product.body):
        followed = next_.product.body[next_.pos]
        if followed in nonterminal and next_.pos < len(next_.product.body):
            terms = nonterminal[followed]
            for term in terms:
                next_char = next_.product.body[next_.pos + 1] if next_.pos + 1 < len(next_.product.body) else "ε"
                for b in first(next_char + next_.follow, terminal, nonterminal):
                    new_item = Item(term, 0, b)
                    if new_item not in closure_set:
                        closure_set.append(new_item)
        index += 1
        next_ = closure_set[index] if index < len(closure_set) else None
    return closure_set

def goto(items, char, terminal, nonterminal):
    goto_set = []
    for item in items:
        if item.pos < len(item.product.body) and item.product.body[item.pos] == char:
            new_item = Item(item.product, item.pos + 1, item.follow)
            if new_item not in goto_set:
                goto_set.append(new_item)
    return closure(goto_set, terminal, nonterminal)

def make_goto_table(terminal, nonterminal):
    goto_table = {}
    I0 = State(closure([Item(Product("S'", ["S"]), 0, "$")], terminal, nonterminal))
    keys = terminal + list(nonterminal.keys())
    state_list = [I0]
    for state in state_list:
        for char in keys:
            goto_set = goto(state.items, char, terminal, nonterminal)
            if goto_set:
                for s in state_list:
                    if s.items == goto_set:
                        goto_table[(state.status, char)] = s.status
                        break
                else:
                    new_state = State(goto_set)
                    state_list.append(new_state)
                    goto_table[(state.status, char)] = new_state.status
    return goto_table, state_list

def make_action_table(terminal, goto_table, state_list):
    action_table = {}
    for state in state_list:
        for item in state.items:
            if item.pos < len(item.product.body):
                for char in terminal:
                    if (state.status, char) in goto_table:
                        goto_state = goto_table[(state.status, char)]
                        action_table[(state.status, char)] = ("SHIFT", goto_state)
            elif item.product.name != "S'":
                action_table[(state.status, item.follow)] = ("REDUCE", item.product)
            elif item.follow == "$":
                action_table[(state.status, "$")] = ("ACCEPT", None)
    return action_table
"""
S' -> S
S -> Expr
Expr -> Term | Expr + Term | Expr - Term
Term -> Factor | Term * Factor | Term / Factor
Factor -> ( Expr ) | Num
Num -> 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
"""
terminal = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "*", "/", "(", ")"]
nonterminal = {
    "S'": [Product("S'", ["S"])],
    "S": [Product("S", ["Expr"])],
    "Expr": [Product("Expr", ["Term"]), Product("Expr", ["Expr", "+", "Term"]), Product("Expr", ["Expr", "-", "Term"])],
    "Term": [Product("Term", ["Factor"]), Product("Term", ["Term", "*", "Factor"]), Product("Term", ["Term", "/", "Factor"])],
    "Factor": [Product("Factor", ["(", "Expr", ")"]), Product("Factor", ["Num"])],
    "Num": [Product("Num", ["0"]), Product("Num", ["1"]), Product("Num", ["2"]), Product("Num", ["3"]), Product("Num", ["4"]), Product("Num", ["5"]), Product("Num", ["6"]), Product("Num", ["7"]), Product("Num", ["8"]), Product("Num", ["9"])]
}
goto_table, state_list = make_goto_table(terminal, nonterminal)
action_table = make_action_table(terminal, goto_table, state_list)
text = "1+1*2"
state_stack = [0]
index = 0
char = text[index]
x = char
while True:
    state = state_stack[-1]
    if x in terminal or x == "$":
        if (state, x) in action_table:
            action, arg = action_table[(state, x)]
            if action == "SHIFT":
                state_stack.append(arg)
                index += 1
                char = text[index] if index < len(text) else "$"
                x = char
            elif action == "REDUCE":
                for _ in range(len(arg.body)):
                    state_stack.pop()
                x = arg.name
            elif action == "ACCEPT":
                print("Accepted!")
                break
        else:
            print("Error!")
            break
    else:
        if (state, x) in goto_table:
            state_stack.append(goto_table[(state, x)])
            x = char
        else:
            print("Error!")
            break