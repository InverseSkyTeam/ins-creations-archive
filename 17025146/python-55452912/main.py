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

class Item:
    STATUS = -1
    def __init__(self, product, pos):
        Item.STATUS += 1
        self.status = Item.STATUS
        self.product = product
        self.pos = pos
    def __str__(self):
        return f"{self.product.name} -> {' '.join(self.product.body[:self.pos])}·{' '.join(self.product.body[self.pos:])}"
    __repr__ = __str__
    def __eq__(self, other):
        return self.product == other.product and self.pos == other.pos
    def __hash__(self):
        return hash((self.product, self.pos))
    
_terminals = ["a", "b"]
patterns = {
    "S": [
        Product("S", ["T"]),
        Product("S", ["A", "B"]),
    ],
    "T": [
        Product("T", ["a", "T", "b"]),
        Product("T", ["a", "b"]),
    ],
    "A":[
        Product("A", ["a", "A"]),
        Product("A", ["a"]),
    ],
    "B":[
        Product("B", ["b", "B"]),
        Product("B", ["b"]),
    ],
}

def recognize(patterns, text):
    I0 = [(Item(p, 0), 0) for p in patterns["S"]]
    for x, _k in I0:
        if x.product.body[0] in patterns:
            for y in patterns[x.product.body[0]]:
                I0.append((Item(y, 0), 0))
    I_list = [I0]
    for i in range(len(text)):
        c = text[i]
        I = []
        I_list.append(I)
        for x, k in I_list[-2]:
            if x.pos < len(x.product.body) and x.product.body[x.pos] == c:
                    I.append((Item(x.product, x.pos+1), k))
        for x, k in I:
            if x.pos == len(x.product.body):
                for s, n in I_list[k]:
                    if s.pos < len(s.product.body) and s.product.body[s.pos] == x.product.name:
                        I.append((Item(s.product, s.pos+1), n))            
            elif x.product.body[x.pos] in patterns:
                for y in patterns[x.product.body[x.pos]]:
                    I.append((Item(y, 0), i+1))
    for x, _k in I_list[-1]:
        if x.product.name == "S" and x.pos == len(x.product.body):
            return True
    return False

print(recognize(patterns, "aabb"))