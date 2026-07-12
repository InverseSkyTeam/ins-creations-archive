class NFA:
    Id = 0
    def __init__(self, next_1=None, next_2=None, edge=None):
        self.id = NFA.Id
        NFA.Id += 1
        self.edge = ("EPSILON", None) if edge is None else edge
        self.next_1 = next_1
        self.next_2 = next_2
        self.accepted = False
        self.mark = None
    def __hash__(self):
        return hash(self.id)

class Pair:
    def __init__(self, start, end):
        self.start = start
        self.end = end

def regex_to_suffix(text):
    output = []
    op_stack = []
    op = {
        "^": 1,
        "+": 2,
        "*": 2,
        "?": 2,
        "=": 3,
        "<=": 3,
        "!": 3,
        "<!": 3,
        "|": 4,
    }
    escape = {
        "n": set("\n"),
        "t": set("\t"),
        "r": set("\r"),
        "f": set("\f"),
        "v": set("\v"),
        "s": set("\n\t\r\f\v"),
        "d": set("0123456789"),
        "w": set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"),
    }
    regex = list(text)
    index = 0
    while index < len(regex):
        char = regex[index]
        if index and regex[index-1] not in "([|\\^" and char not in op and char != ")":
            regex.insert(index, "^")
            char = "^"
        if char == "(":
            op_stack.append(char)
        elif char == ")":
            while op_stack[-1] != "(":
                output.append(op_stack.pop())
            op_stack.pop()
        elif char in op:
            while op_stack and op_stack[-1] != "(" and op[char] <= op[op_stack[-1]]:
                output.append(op_stack.pop())
            op_stack.append(char)
        elif char == "[":
            index += 1
            char = regex[index]
            is_opp = False
            if char == "^":
                is_opp = True
                index += 1
                char = regex[index]
            chars = set()
            while char != "]":
                if char == "\\":
                    index += 1
                    char = regex[index]
                    if char in escape:
                        chars.add(escape[char])
                    else:
                        chars.add(char)
                else:
                    chars.add(char)
                index += 1
                char = regex[index]
            if is_opp:
                chars = ("EXCEPT", chars)
            else:
                chars = ("IN", chars)
            output.append(chars)
        else:
            if char == "\\":
                index += 1
                char = regex[index]
                if char in escape:
                    output.append(("IN", escape[char]))
                else:
                    output.append(("IN", set(char)))
            elif char == ".":
                output.append(("ALL", None))
            else:
                output.append(("IN", set(char)))
        index += 1
    while op_stack:
        output.append(op_stack.pop())
    return output

def suffix_to_nfa(expr):
    stack = []
    for char in expr:
        if char == "^":
            second, first = stack.pop(), stack.pop()
            first.end.next_1 = second.start
            stack.append(Pair(first.start, second.end))
        elif char == "*":
            pair = stack.pop()
            end = NFA()
            start = NFA(pair.start, end)
            pair.end.next_1 = start
            pair.end.next_2 = end
            stack.append(Pair(start, end))
        elif char == "+":
            pair = stack.pop()
            start = NFA(pair.start)
            end = NFA()
            pair.end.next_1 = start
            pair.end.next_2 = end
            stack.append(Pair(start, end))
        elif char == "?":
            pair = stack.pop()
            end = NFA()
            start = NFA(pair.start, end)
            pair.end.next_1 = end
            stack.append(Pair(start, end))
        elif char == "|":
            second, first = stack.pop(), stack.pop()
            start = NFA()
            end = NFA()
            start.next_1 = first.start
            start.next_2 = second.start
            first.end.next_1 = end
            second.end.next_1 = end
            stack.append(Pair(start, end))
        else:
            end = NFA()
            start = NFA(end, None, char)
            stack.append(Pair(start, end))
    pair = stack.pop()
    pair.end.accepted = True
    return pair

def closure(nfa_set):
    output = set(nfa_set)
    stack = list(nfa_set)
    while stack:
        current = stack.pop()
        if current.edge[0] == "EPSILON":
            if current.next_1 and current.next_1 not in output:
                output.add(current.next_1)
                stack.append(current.next_1)
            if current.next_2 and current.next_2 not in output:
                output.add(current.next_2)
                stack.append(current.next_2)
    return output

def match(pattern, text):
    expr = regex_to_suffix(pattern)
    nfa = suffix_to_nfa(expr).start
    nfa_set = set()
    nfa_set.add(nfa)
    for char in text:
        nfa_set = closure(nfa_set)
        new_nfa_set = set()
        for nfa in nfa_set:
            if nfa.edge[0] == "ALL":
                new_nfa_set.add(nfa.next_1)
            elif nfa.edge[0] == "IN" and char in nfa.edge[1]:
                new_nfa_set.add(nfa.next_1)
            elif nfa.edge[0] == "EXCEPT" and char not in nfa.edge[1]:
                new_nfa_set.add(nfa.next_1)
        nfa_set = new_nfa_set
    nfa_set = closure(nfa_set)
    for nfa in nfa_set:
        if nfa.accepted:
            return True
    return False
    
print(match("a*b", "aaaab"))