class Product:
    def __init__(self, name, body, prob):
        self.name = name
        self.body = body
        self.prob = prob

class Token:
    def __init__(self, val):
        self.val = val
    def __str__(self):
        return f'"{self.val}"'
    __repr__ = __str__

class ProbNode:
    def __init__(self, name, children, prob):
        self.name = name
        self.children = children
        self.prob = prob
    def __str__(self):
        return f"{self.name}({', '.join([str(x) for x in self.children])})"
    __repr__ = __str__

def make_prob_table(text, nonterminals):
    table = [[{} for _ in range(len(text))] for _ in range(len(text))]
    for i in range(len(text)):
        for j in range(len(text)):
            for nonterm in nonterminals.keys():
                table[i][j][nonterm] = {"prob": 0.0, "paths": {"split": None, "rule": None}}
    for i in range(len(text)):
        for nonterm, products in nonterminals.items():
            for product in products:
                if product.body == text[i]:
                    table[i][i][nonterm]["prob"] = product.prob
                    table[i][i][nonterm]["path"] = {"split": None, "rule": text[i]}
                    for xnonterm, xproducts in nonterminals.items():
                        for xproduct in xproducts:
                            if xproduct.body == nonterm:
                                table[i][i][xnonterm]["prob"] = product.prob * xproduct.prob
                                table[i][i][xnonterm]["path"] = {"split": i, "rule": nonterm}
    for l in range(1, len(text)):
        for i in range(len(text) - l):
            j = i + l
            for nonterm, products in nonterminals.items():
                best = {"prob": 0.0, "path": None}
                for product in products:
                    if product.body[0] not in nonterminals:
                        continue
                    for s in range(i, j):
                        if isinstance(product.body, list):
                            tmp = product.prob * table[i][s][product.body[0]]["prob"] * table[s+1][j][product.body[1]]["prob"]
                        else:
                            tmp = 0
                        if tmp > best["prob"]:
                            best["prob"] = tmp
                            best["path"] = {"split": s, "rule": product.body}
                table[i][j][nonterm] = best
    return table

def build_prob_tree(table, i, j, root):
    node = table[i][j][root]
    if node["path"]["split"] is not None:
        if isinstance(node["path"]["rule"], list):
            left = build_prob_tree(table, i, node["path"]["split"], node["path"]["rule"][0])
            right = build_prob_tree(table, node["path"]["split"]+1, j, node["path"]["rule"][1])
            tree = ProbNode(root, [left, right], node["prob"])
            return tree
        else:
            child = build_prob_tree(table, i, node["path"]["split"], node["path"]["rule"])
            tree = ProbNode(root, [child], node["prob"])
            return tree
    else:
        token = Token(node["path"]["rule"])
        tree = ProbNode(root, [token], node["prob"])
        return tree

nonterminals = {
    "S": [
        Product("S", ["NP", "VP"], 0.9),
        Product("S", "VP", 0.1),
    ],
    "VP": [
        Product("VP", ["V", "NP"], 0.5),
        Product("VP", "V", 0.1),
        Product("VP", ["V", "@VP_V"], 0.3),
        Product("VP", ["V", "PP"], 0.1)
    ],
    "@VP_V": [
        Product("@VP_V", ["NP", "PP"], 1.0)
    ],
    "NP": [
        Product("NP", ["NP", "NP"], 0.1),
        Product("NP", ["NP", "PP"], 0.2),
        Product("NP", "N", 0.7)
    ],
    "PP": [
        Product("PP", ["P", "NP"], 1.0)
    ],
    "N": [
        Product("N", "people", 0.5),
        Product("N", "fish", 0.2),
        Product("N", "tanks", 0.2),
        Product("N", "rods", 0.1),
    ],
    "V": [
        Product("V", "people", 0.1),
        Product("V", "fish", 0.6),
        Product("V", "tanks", 0.3),
    ],
    "P": [
        Product("P", "with", 1.0)
    ]
}
text = "fish people fish tanks".split()

table = make_prob_table(text, nonterminals)
tree = build_prob_tree(table, 0, len(text)-1, "S")
print(tree)