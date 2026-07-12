class Product:
    def __init__(self, name, body, function = None):
        self.name = name
        self.body = body
        self.function = function
    def __str__(self):
        return f"{self.name} -> {' '.join(self.body)}"
    __repr__ = __str__
    def _eq__(self, other):
        return self.name == other.name and self.body == other.body
    def __hash__(self):
        return hash((self.name, tuple(self.body)))

def first(product, terminal, nonterminal):
    if product == "ε":
        return {"ε"}
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
            if term != product.name:
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

def make_table(nonterminal, terminal):
    table = {}
    for name, experissions in nonterminal.items():
        for experission in experissions:
            first_set = first(name, terminal, nonterminal)
            for a in first_set - {"ε"}:
                table[(name, a)] = experission
            if "ε" in first_set:
                follow_set = follow(name, terminal, nonterminal)
                for a in follow_set:
                    table[(name, a)] = experission
    return table

def parse(text, nonterminal, terminal):
    table = make_table(nonterminal, terminal)
    stack = ["$", "S"]
    index = 0
    char = text[index]
    while True:
        x = stack[-1]
        if x in terminal:
            if char == x:
                stack.pop()
                index += 1
                char = text[index] if index < len(text) else "$"
            else:
                raise Exception(f"Syntax error at {index}: expected {x}, got {char}")
        else:
            if char == x and x == "$":
                return True
            if (x, char) in table:
                stack.pop()
                stack += table[(x, char)].body[::-1]
            else:
                raise Exception(f"Syntax error at {index}: expected {x}, got {char}")

terminal = ["a", "b"]
nonterminal = {
    "S": [Product("S", ["A", "B"])],
    "A": [Product("A", ["a"])],
    "B": [Product("B", ["b"])]
}
text = "ab"
print(parse(text, nonterminal, terminal))