import enum
import types
import copy

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value
    def __str__(self):
        return f"Token({self.type}: {self.value})"
    __repr__ = __str__

class NFA:
    def __init__(self):
        self.edge = "EPSILON"
        self.next_1 = None
        self.next_2 = None
        self.function = None
class DFA:
    STATUS = -1
    def __init__(self, nfas):
        self.nfas = nfas
        self.accepted = False
        self.function = None
        for i in nfas:
            if i.next_1 is None and i.next_2 is None:
                self.accepted = True
            if i.function is not None and self.function is None:
                self.function = i.function
        DFA.STATUS += 1
        self.status = DFA.STATUS
    def __eq__(self, other):
        return self.status == other.status
class DFAGroup:
    STATUS = -1
    def __init__(self, dfas, status = None):
        self.dfas = dfas
        self.function = None
        for i in dfas:
            if i.function is not None and self.function is None:
                self.function = i.function
        if status is None:
            DFAGroup.STATUS += 1
            self.status = DFAGroup.STATUS
        else:
            self.status = status
    def get(self, index):
        return self.dfas[index] if index < len(self.dfas) else None
    def __str__(self):
        return str(list(map(lambda x:x.status, self.dfas)))
    __repr__ = __str__
    def __eq__(self, other):
        return self.dfas == other.dfas

def closure_nfa(input_set):
    output_set = []
    if not len(input_set) > 0:
        return None
    stack = []
    for i in input_set:
        stack.append(i)
        output_set.append(i)
    while len(stack) > 0:
        current = stack.pop()
        if current.edge == "EPSILON":
            if current.next_1 and current.next_1 not in output_set:
                output_set.append(current.next_1)
                stack.append(current.next_1)
            if current.next_2 and current.next_2 not in output_set:
                output_set.append(current.next_2)
                stack.append(current.next_2)
    return output_set
def move(input_set, char):
    output_set = []
    for i in input_set:
        if i.edge == char if isinstance(i.edge, str) else char in i.edge:
            output_set.append(i.next_1)
    return output_set
def nfa_to_dfa(nfa):
    dfa_list = []
    dfa_list.append(DFA(closure_nfa([nfa])))
    jump_table = [{}]
    index = 0
    while index < len(dfa_list):
        current = dfa_list[index]
        for i in range(127):
            char = chr(i)
            moved = move(current.nfas, char)
            if not moved:
                continue
            nfa_closure = closure_nfa(moved)
            for j in dfa_list:
                if j.nfas == nfa_closure:
                    new_dfa = j
                    break
            else:
                new_dfa = DFA(nfa_closure)
                dfa_list.append(new_dfa)
                jump_table.append({})
            jump_table[current.status][char] = new_dfa.status
            if new_dfa.accepted:
                jump_table[new_dfa.status]["ACCEPT"] = True
        index += 1
    return dfa_list, jump_table
def dfa_in_group(dfa_node, group_list):
    for group in group_list:
        for dfa in group.dfas:
            if dfa.status == dfa_node:
                output = group
                return output
def minimize_dfa(dfa_list, jump_table):
    accept = []
    non_accept = []
    for i in dfa_list:
        if i.accepted:
            accept.append(i)
        else:
            non_accept.append(i)
    group_list = []
    if non_accept:
        group_list.append(DFAGroup(non_accept))
    if accept:
        group_list.append(DFAGroup(accept))
    index = 0
    group = group_list[index]
    while group:
        if len(group.dfas) == 1:
            index += 1
            group = group_list[index] if index < len(group_list) else None
            continue
        group_keys = []
        group_values = []
        for x in group.dfas:
            if x.accepted:
                gotos = x.function
            else:
                gotos = []
                for i in range(127):
                    char = chr(i)
                    goto = jump_table[x.status].get(char)
                    goto_group = dfa_in_group(goto, group_list)
                    gotos.append(goto_group.status if goto_group is not None else None)
            if gotos in group_keys:
                group_values[group_keys.index(gotos)].append(x)
            else:
                group_keys.append(gotos)
                group_values.append([x])
        if len(group_values) == 1 and group_values[0] == group.dfas:
            index += 1
            group = group_list[index] if index < len(group_list) else None
            continue
        group.__init__(group_values[0], group.status)
        for groups in group_values[1:]:
            new_group = DFAGroup(groups)
            group_list.insert(index, new_group)
            index -= 1
        index += 1
        group = group_list[index] if index < len(group_list) else None
    return group_list
def create_transition_table(dfa_list, jump_table, group_list):
    transition_table = [{} for _ in range(len(group_list))]
    for dfa in dfa_list:
        from_group = dfa_in_group(dfa.status, group_list)
        for i in range(127):
            char = chr(i)
            to = jump_table[dfa.status].get(char)
            if to is None:
                continue
            to_group = dfa_in_group(to, group_list)
            transition_table[from_group.status][char] = to_group.status
        if dfa.accepted:
            transition_table[from_group.status]["ACCEPT"] = from_group.function
    return transition_table


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
    def __hash__(self):
        return hash((self.product, self.pos, self.follow))

class LRState:
    STATUS = -1
    def __init__(self, items):
        LRState.STATUS += 1
        self.status = LRState.STATUS
        self.items = items

class LALRState:
    STATUS = -1
    def __init__(self, lr_state):
        LALRState.STATUS += 1
        self.status = LALRState.STATUS
        self.kernel = lr_state.items
        self.items = lr_state.items
        self.lr_states = [lr_state.status]

def first(product, terminal, nonterminal):
    if product[0] == "ε":
        product = product[1]
    else:
        product = product[0]
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

def state_closure(items, terminal, nonterminal):
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
                for b in first((next_char, next_.follow), terminal, nonterminal):
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
    return state_closure(goto_set, terminal, nonterminal)

def make_lr_states(terminal, nonterminal):
    goto_table = {}
    I0 = LRState(state_closure([Item(Product("S'", ["S"]), 0, "$")], terminal, nonterminal))
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
                    new_state = LRState(goto_set)
                    goto_table[(state.status, char)] = new_state.status
                    state_list.append(new_state)
    return state_list, goto_table

def is_concertric(state, merged):
    if len(state.items) != len(merged.kernel):
        return False
    res = True
    for item1, item2 in zip(state.items, merged.kernel):
        if item1.product != item2.product or item1.pos != item2.pos:
            res = False
            break
    return res

def merge(state_list):
    merged_list = []
    for state in state_list:
        for merged in merged_list:
            if is_concertric(state, merged):
                merged.items.extend(state.items)
                merged.lr_states.append(state.status)
                break
        else:
            merged_list.append(LALRState(state))
    return merged_list

def lrstate_in_lalrstate(lr_state, state_list):
    for lalr_state in state_list:
        if lr_state in lalr_state.lr_states:
            return lalr_state

def make_goto_table(terminal, nonterminal, state_list, goto_table, merged_list):
    res = {}
    keys = terminal + list(nonterminal.keys())
    for state in state_list:
        for char in keys:
            if (state.status, char) in goto_table:
                from_state = lrstate_in_lalrstate(state.status, merged_list)
                to_state = lrstate_in_lalrstate(goto_table[(state.status, char)], merged_list)
                res[(from_state.status, char)] = to_state.status
    return res

def make_action_table(terminal, priority, goto_table, state_list):
    action_table = {}
    shift_reduce = []
    shifts = {}
    reduces = {}
    for state in state_list:
        for item in state.items:
            if item.pos < len(item.product.body):
                for char in terminal:
                    if (state.status, char) in goto_table:
                        goto_state = goto_table[(state.status, char)]
                        if (state.status, char) in action_table:
                            action = action_table[(state.status, char)]
                            if action[0] == "REDUCE":
                                shift_reduce.append((state.status, char, item, reduces[(state.status, char)], ("SHIFT", goto_state), action))
                                continue
                        action_table[(state.status, char)] = ("SHIFT", goto_state)
                        shifts[(state.status, char)] = item
            elif item.product.name != "S'":
                if (state.status, item.follow) in action_table:
                    action = action_table[(state.status, item.follow)]
                    if action[0] == "SHIFT":
                        shift_reduce.append((state.status, item.follow, shifts[(state.status, item.follow), item, action, ("REDUCE", item.product)]))
                        continue
                action_table[(state.status, item.follow)] = ("REDUCE", item.product)
                reduces[(state.status, item.follow)] = item
            elif item.follow == "$":
                action_table[(state.status, "$")] = ("ACCEPT", None)
    for status, character, shift_item, reduce_item, shift_action, reduce_action in shift_reduce:
        shift_priority, shift_associativity = priority.get(shift_item.product.body[shift_item.pos], None)
        for term in reduce_item.product.body[::-1]:
            if term in terminal:
                reduce_priority, reduce_associativity = priority.get(term, None)
                break
        if shift_priority is None or reduce_priority is None:
            action_table[(status, character)] = shift_action
        if shift_priority < reduce_priority:
            action_table[(status, character)] = shift_action
        elif shift_priority > reduce_priority:
            action_table[(status, character)] = reduce_action
        else:
            if shift_associativity == "LEFT" and reduce_associativity == "LEFT":
                action_table[(status, character)] = shift_action
            elif shift_associativity == "RIGHT" and reduce_associativity == "RIGHT":
                action_table[(status, character)] = reduce_action
    return action_table

class EBNF:
    List = []
    Id = -1
    def __init__(self, body = None):
        self.bodies = [body] if body else []
        self.is_closure = False
    def __and__(self, other):
        new_pg = EBNF()
        if not (self.is_closure or other.is_closure):
            for i in self.bodies:
                for j in other.bodies:
                    new_pg.bodies.append(i + j)
        elif not self.is_closure:
            id_ = str(other.id)
            for i in self.bodies:
                new_pg.bodies.append([*i, id_])
        else:
            id_ = str(self.id)
            for i in other.bodies:
                new_pg.bodies.append([id_, *i])
        return new_pg
    def __or__(self, other):
        self.bodies += other.bodies
        if other in EBNF.List:
            EBNF.List.remove(other)
        return self
    def optional(self):
        self.bodies.append([])
        return self
    def one_to_n(self):
        EBNF.Id += 1
        self.id = EBNF.Id
        EBNF.List.append(self)
        id_ = str(self.id)
        for i in range(len(self.bodies)):
            self.bodies.append([id_] + self.bodies[i])
        self.is_closure = True
        return self
    def zero_to_n(self):
        return self.one_to_n().optional()
    
class LexTokenType(enum.Enum):
    EOS = 0
    ANY = 1
    AT_BOL = 2
    AT_EOL = 3
    CCL_END = 4
    CCL_START = 5
    CLOSE_CURLY = 6
    CLOSE_PAREN = 7
    CLOSURE = 8
    DASH = 9
    END_OF_INPUT = 10
    L = 11
    OPEN_CURLY = 12
    OPEN_PAREN = 13
    OPTIONAL = 14
    OR = 15
    PLUS_CLOSE = 16

class LexScanner:
    def __init__(self, pattern):
        self.pattern = pattern
        self.lexeme = ""
        self.pos = -1
        self.current_token = None
        self.ev = {
            '\0': '\\',
            'b': '\b',
            'f': '\f',
            'n': '\n',
            's': ' ',
            't': '\t',
            'e': '\033',
        }
        self.tokens = {
            '.': LexTokenType.ANY,
            '^': LexTokenType.AT_BOL,
            '$': LexTokenType.AT_EOL,
            ']': LexTokenType.CCL_END,
            '[': LexTokenType.CCL_START,
            '}': LexTokenType.CLOSE_CURLY,
            ')': LexTokenType.CLOSE_PAREN,
            '*': LexTokenType.CLOSURE,
            '-': LexTokenType.DASH,
            '{': LexTokenType.OPEN_CURLY,
            '(': LexTokenType.OPEN_PAREN,
            '?': LexTokenType.OPTIONAL,
            '|': LexTokenType.OR,
            '+': LexTokenType.PLUS_CLOSE,
        }
        self.advance()
    def advance(self):
        self.pos += 1
        if self.pos > len(self.pattern) - 1:
            self.current_token = LexTokenType.EOS
            self.lexeme = None
            return False
        self.lexeme = self.pattern[self.pos]
        if self.lexeme == "\\":
            self.pos += 1
            char = self.pattern[self.pos].lower()
            self.lexeme = self.ev.get(char, char)
            self.current_token = LexTokenType.L
        else:
            self.current_token = self.tokens.get(self.lexeme, LexTokenType.L)
class LexAnalyzer:
    """
    group ::= ("(" expr ")")*
    expr ::= factor_conn ("|" factor_conn)*
    factor_conn ::= factor | factor factor*
    factor ::= (term | term ("*" | "+" | "?"))*
    term ::= char | "[" char "-" char "]" | .
    """
    def __init__(self, lexer):
        self.lexer = lexer
        self.ascii_table = set([chr(i) for i in range(127)])
        
    def dodash(self):
        first = ""
        char_set = set()
        while self.lexer.current_token != LexTokenType.CCL_END:
            if self.lexer.current_token == LexTokenType.DASH:
                self.lexer.advance()
                for c in range(ord(first), ord(self.lexer.lexeme) + 1):
                    char_set.add(chr(c))
                self.lexer.advance()
            else:
                first = self.lexer.lexeme
                char_set.add(self.lexer.lexeme)
                self.lexer.advance()
        return char_set
    def term(self):
        start = NFA()
        if self.lexer.current_token == LexTokenType.L:
            start.edge = self.lexer.lexeme
            start.next_1 = NFA()
            end = start.next_1
            self.lexer.advance()
        elif self.lexer.current_token == LexTokenType.ANY:
            start.edge = self.ascii_table
            start.next_1 = NFA()
            end = start.next_1
            self.lexer.advance()
        elif self.lexer.current_token == LexTokenType.CCL_START:
            self.lexer.advance()
            if self.lexer.current_token == LexTokenType.AT_BOL:
                self.lexer.advance()
                char_set = self.dodash()
                self.lexer.advance()
                start.edge = self.ascii_table - char_set
                start.next_1 = NFA()
                end = start.next_1
            else:
                char_set = self.dodash()
                self.lexer.advance()
                start.edge = char_set
                start.next_1 = NFA()
                end = start.next_1
        elif self.lexer.current_token == LexTokenType.OPEN_PAREN:
            self.lexer.advance()
            start, end = self.expr()
            if self.lexer.current_token != LexTokenType.CLOSE_PAREN:
                raise ValueError("Missing closing parenthesis")
            self.lexer.advance()
        return start, end
    def factor(self):
        start, end = self.term()
        new_start = NFA()
        new_end = NFA()
        if self.lexer.current_token == LexTokenType.CLOSURE:
            new_start.next_1 = start
            new_start.next_2 = new_end
            end.next_1 = start
            end.next_2 = new_end
            start, end = new_start, new_end
            self.lexer.advance()
        elif self.lexer.current_token == LexTokenType.PLUS_CLOSE:
            new_start.next_1 = start
            end.next_1 = start
            end.next_2 = new_end
            self.lexer.advance()
            start, end = new_start, new_end
        elif self.lexer.current_token == LexTokenType.OPTIONAL:
            new_start.next_1 = start
            new_start.next_2 = new_end
            end.next_2 = new_end
            self.lexer.advance()
            start, end = new_start, new_end
        return start, end
    def factor_conn(self):
        start, end = self.factor()
        while self.lexer.current_token in (LexTokenType.L, LexTokenType.ANY, LexTokenType.CCL_START, LexTokenType.OPEN_PAREN):
            new_start, new_end = self.factor()
            end.next_1 = new_start
            end = new_end
        return start, end
    def expr(self):
        start, end = self.factor_conn()
        while self.lexer.current_token == LexTokenType.OR:
            self.lexer.advance()
            head = NFA()
            tail = NFA()
            new_start, new_end = self.factor_conn()
            head.next_1 = start
            head.next_2 = new_start
            end.next_1 = tail
            new_end.next_1 = tail
            start = head
            end = tail
        return start, end

class ParseTokenType(enum.Enum):
    CCL_END = 0
    CCL_START = 1
    OPEN_CURLY = 2
    CLOSE_CURLY = 3
    OPEN_PAREN = 4
    CLOSE_PAREN = 5
    CLOSURE = 6
    PLUS_CLOSE = 7
    OR = 8
    ID = 9
    OPTIONAL = 10
    COMMA = 11
    ARROW = 12
    SEMICOLON = 13
    RE = 16
    COLON = 17
    STRING = 18
    AT = 19
    NUMBER = 20
    EOF = 21

class ParseScanner:
    def __init__(self, pattern):
        self.pattern = pattern
        self.lexeme = ""
        self.pos = -1
        self.current_token = None
        self.tokens = {
            ']': ParseTokenType.CCL_END,
            '[': ParseTokenType.CCL_START,
            '{': ParseTokenType.OPEN_CURLY,
            '}': ParseTokenType.CLOSE_CURLY,
            '(': ParseTokenType.OPEN_PAREN,
            ')': ParseTokenType.CLOSE_PAREN,
            '*': ParseTokenType.CLOSURE,
            '+': ParseTokenType.PLUS_CLOSE,
            '|': ParseTokenType.OR,
            "?": ParseTokenType.OPTIONAL,
            ",": ParseTokenType.COMMA,
            ";": ParseTokenType.SEMICOLON,
            "/": ParseTokenType.RE,
            ":": ParseTokenType.COLON,
            "@": ParseTokenType.AT,
        }
        self.advance()
    def advance(self):
        self.pos += 1
        if self.pos > len(self.pattern) - 1:
            self.current_token = ParseTokenType.EOF
            self.lexeme = None
            return
        self.lexeme = self.pattern[self.pos]
        if self.lexeme.isspace():
            while self.pos < len(self.pattern) and self.pattern[self.pos].isspace():
                self.pos += 1
            self.pos -= 1
            self.advance()
            return
        if self.lexeme in self.tokens:
            self.current_token = self.tokens[self.lexeme]
        elif self.lexeme == "-" and self.pattern[self.pos + 1] == ">":
            self.pos += 1
            self.lexeme = "->"
            self.current_token = ParseTokenType.ARROW
        elif self.lexeme.isalpha():
            self.lexeme = ""
            while self.pattern[self.pos].isalnum() or self.pattern[self.pos] == "_":
                self.lexeme += self.pattern[self.pos]
                self.pos += 1
                if self.pos > len(self.pattern) - 1:
                    break
            self.pos -= 1
            self.current_token = ParseTokenType.ID
        elif self.lexeme == '"' or self.lexeme == "'":
            quote = self.lexeme
            self.lexeme = ""
            self.pos += 1
            while self.pattern[self.pos] != quote:
                self.lexeme += self.pattern[self.pos]
                self.pos += 1
            self.current_token = ParseTokenType.STRING
        elif self.lexeme.isdigit():
            self.lexeme = ""
            while self.pattern[self.pos].isdigit():
                self.lexeme += self.pattern[self.pos]
                self.pos += 1
                if self.pos > len(self.pattern) - 1:
                    break
            self.pos -= 1
            self.lexeme = int(self.lexeme)
            self.current_token = ParseTokenType.NUMBER
        else:
            raise ValueError(f"Invalid character: {self.lexeme}")

class ParseAnalyzer:
    def __init__(self, lexer):
        self.lexer = lexer
        self.anomynous_token = []

    def atom(self):
        if self.lexer.current_token == ParseTokenType.ID:
            product = EBNF([self.lexer.lexeme])
            self.lexer.advance()
        elif self.lexer.current_token == ParseTokenType.STRING:
            product = EBNF([self.lexer.lexeme])
            self.anomynous_token.append(self.lexer.lexeme)
            self.lexer.advance()
        elif self.lexer.current_token == ParseTokenType.OPEN_PAREN:
            self.lexer.advance()
            product = self.expr()
            if self.lexer.current_token != ParseTokenType.CLOSE_PAREN:
                raise ValueError("Missing closing parenthesis")
            self.lexer.advance()
        elif self.lexer.current_token == ParseTokenType.CCL_START:
            self.lexer.advance()
            product = self.expr().optional()
            if self.lexer.current_token != ParseTokenType.CCL_END:
                raise ValueError("Missing closing bracket")
            self.lexer.advance()
        return product
    def closure(self):
        atom = self.atom()
        if self.lexer.current_token == ParseTokenType.CLOSURE:
            self.lexer.advance()
            product = atom.zero_to_n()
        elif self.lexer.current_token == ParseTokenType.PLUS_CLOSE:
            self.lexer.advance()
            product = atom.one_to_n()
        elif self.lexer.current_token == ParseTokenType.OPTIONAL:
            self.lexer.advance()
            product = atom.optional()
        else:
            product = atom
        return product
    def closure_conn(self):
        closure = self.closure()
        while self.lexer.current_token in (ParseTokenType.ID, ParseTokenType.STRING, ParseTokenType.OPEN_PAREN, ParseTokenType.CCL_START):
            closure &= self.closure()
        return closure
    def expr(self):
        closure_conn = self.closure_conn()
        while self.lexer.current_token == ParseTokenType.OR:
            self.lexer.advance()
            closure_conn |= self.closure_conn()
        return closure_conn
    def product(self):
        if self.lexer.current_token == ParseTokenType.AT:
            self.lexer.advance()
            command = self.lexer.lexeme.lower()
            if command == "ignore":
                self.lexer.advance()
                if self.lexer.current_token != ParseTokenType.STRING:
                    raise ValueError("Missing string")
                ignore = self.lexer.lexeme
                self.lexer.advance()
                return ("ignore", ignore)
            elif command == "priority":
                self.lexer.advance()
                if self.lexer.current_token != ParseTokenType.STRING:
                    raise ValueError("Missing string")
                operator = self.lexer.lexeme
                self.lexer.advance()
                if self.lexer.current_token != ParseTokenType.NUMBER:
                    raise ValueError("Missing number")
                priority = self.lexer.lexeme
                self.lexer.advance()
                if self.lexer.current_token != ParseTokenType.ID:
                    raise ValueError("Missing ID")
                ass = self.lexer.lexeme.upper()
                self.lexer.advance()
                return ("priority", (operator, priority, ass))
        if self.lexer.current_token != ParseTokenType.ID:
            raise ValueError("Missing ID")
        name = self.lexer.lexeme
        self.lexer.advance()
        if self.lexer.current_token == ParseTokenType.ARROW:
            self.lexer.advance()
            grammars = []
            closure_conn = self.closure_conn()
            if not closure_conn.is_closure:
                EBNF.List.append(closure_conn)
                EBNF.Id += 1
                closure_conn.id = EBNF.Id
            if self.lexer.current_token == ParseTokenType.OPEN_CURLY:
                self.lexer.advance()
                if self.lexer.current_token != ParseTokenType.ID:
                    raise ValueError("Missing ID")
                grammars.append((closure_conn, self.lexer.lexeme))
                self.lexer.advance()
                if self.lexer.current_token != ParseTokenType.CLOSE_CURLY:
                    raise ValueError("Missing close curly")
                self.lexer.advance()
            else:
                grammars.append((closure_conn, None))
            while self.lexer.current_token == ParseTokenType.OR:
                self.lexer.advance()
                closure_conn = self.closure_conn()
                if not closure_conn.is_closure:
                    EBNF.List.append(closure_conn)
                    EBNF.Id += 1
                    closure_conn.id = EBNF.Id
                if self.lexer.current_token == ParseTokenType.OPEN_CURLY:
                    self.lexer.advance()
                    if self.lexer.current_token != ParseTokenType.ID:
                        raise ValueError("Missing ID")
                    grammars.append((closure_conn, self.lexer.lexeme))
                    self.lexer.advance()
                    if self.lexer.current_token != ParseTokenType.CLOSE_CURLY:
                        raise ValueError("Missing close curly")
                    self.lexer.advance()
                else:
                    grammars.append((closure_conn, None))
            return name, grammars
        elif self.lexer.current_token == ParseTokenType.COLON:
            self.lexer.advance()
            if self.lexer.current_token != ParseTokenType.RE:
                raise ValueError("Missing regular expression")
            self.lexer.advance()
            pos = self.lexer.pos
            regex = ""
            while self.lexer.pattern[pos] != "/":
                regex += self.lexer.pattern[pos]
                pos += 1
            self.lexer.pos = pos
            self.lexer.advance()
            return name, regex
            
    def rule(self):
        lex_rules = []
        parse_rules = {}
        ignores = ""
        priorities = {}
        while self.lexer.current_token in (ParseTokenType.ID, ParseTokenType.AT):
            ret = self.product()
            if ret[0] == "ignore":
                ignores = ret[1]
            elif ret[0] == "priority":
                op, pri, ass = ret[1]
                priorities[op] = (pri, ass)
            else:
                name, rule = ret
                if isinstance(rule, str):
                    lex_rules.append((name, rule))
                else:
                    parse_rules[name] = rule
            if self.lexer.current_token != ParseTokenType.SEMICOLON:
                raise ValueError("Missing semicolon")
            self.lexer.advance()
        return lex_rules, parse_rules, ignores, priorities
    
class Rule:
    def __init__(self, rules):
        analyzer = ParseAnalyzer(ParseScanner(rules))
        self.terminals, self.parse_rules, self.ignore, self.priorities = analyzer.rule()
        self.lex_rules = copy.deepcopy(self.terminals)
        for rule in analyzer.anomynous_token:
            pattern = rule if rule not in ("+", "-", "*", "?", "|", "(", ")", "[", "]", "{", "}", ".", "^", "$") else "\\" + rule
            self.lex_rules.append((rule, pattern))
        self.__generate_lexer()
        self.__generate_parser()
        

    def __generate_lexer(self):
        name, pattern = self.lex_rules[0]
        lexer = LexScanner(pattern)
        parser = LexAnalyzer(lexer)
        start, end = parser.expr()
        body = f"def fn(lexer):\n    return Token('{name}', lexer.buffer)"
        end.function = types.FunctionType(compile(body, "", "exec").co_consts[0], globals())
        root = NFA()
        root.next_1 = start
        for name, pattern in self.lex_rules[1:]:
            lexer = LexScanner(pattern)
            parser = LexAnalyzer(lexer)
            start, end = parser.expr()
            body = f"def fn(lexer):\n    return Token('{name}', lexer.buffer)"
            end.function = types.FunctionType(compile(body, "", "exec").co_consts[0], globals())
            root.next_2 = start
            new_root = NFA()
            new_root.next_1 = root
            root = new_root
        dfa_list, jump_table = nfa_to_dfa(root)
        group_list = minimize_dfa(dfa_list, jump_table)
        self.transition_table = create_transition_table(dfa_list, jump_table, group_list)

    def __generate_parser(self):
        lex_rules = [x[0] for x in self.lex_rules]
        terminals = [x[0] for x in self.terminals]
        nonterminals = list(self.parse_rules.keys())
        patterns = {}
        for pg in EBNF.List:
            id_ = str(pg.id)
            patterns[id_] = []
            for b in pg.bodies:
                rets = []
                for m in range(len(b)):
                    if b[m].isdigit():
                        rets.append(f"*args[{m}]")
                    elif b[m] in terminals or b[m] in nonterminals:
                        rets.append(f"args[{m}]")
                body = f"def fn(args):\n    return [{','.join(rets)}]"
                fn = types.FunctionType(compile(body, "", "exec").co_consts[0], {})
                patterns[id_].append(Product(id_, b, fn))
        for name, rules in self.parse_rules.items():
            patterns[name] = []
            for rule, func in rules:
                patterns[name].append(Product(name, [str(rule.id)], func))
        patterns["S'"] = [Product("S'", ["S"], None)]
        lr_states, lr_goto_table = make_lr_states(lex_rules, patterns)
        state_list = merge(lr_states)
        print("LR(1)状态数", len(lr_states))
        print("LALR(1)状态数", len(state_list))
        self.goto_table = make_goto_table(lex_rules, patterns, lr_states, lr_goto_table, state_list)
        self.action_table = make_action_table(lex_rules, self.priorities, self.goto_table, state_list)

class Parser:
    def __init__(self, rule: Rule):
        self.transition_table, self.action_table, self.goto_table = rule.transition_table, rule.action_table, rule.goto_table
        self.ignore = rule.ignore
    def advance(self):
        if self.char == "\n":
            self.line += 1
            self.column = 1
        else:
            self.column += 1
        self.pos += 1
        self.char = self.string[self.pos] if self.pos < len(self.string) else None

    def lex(self):
        while self.char is not None:
            if self.char in self.ignore and self.status == self.start:
                self.advance()
                continue
            self.buffer += self.char
            status = self.status = self.transition_table[self.status].get(self.char)
            if status is None:
                if not self.back:
                    raise SyntaxError(f"Unexpected character: {self.char}")
                else:
                    self.pos, function = self.back
                    self.buffer = self.buffer[:-1]
                    self.status = self.start
                    res = function(self)
                    self.buffer = ""
                    self.back = None
                    self.advance()
                    self.status = self.start
                    return res
            else:
                if "ACCEPT" in self.transition_table[status]:
                    function = self.transition_table[status]["ACCEPT"]
                    self.back = (self.pos, function)
                    if self.pos == len(self.string) - 1:
                        res = function(self)
                        self.advance()
                        self.status = self.start
                        return res
            self.advance()
        if self.char is None:
            if self.status != self.start:
                raise SyntaxError("Unexpected end of file")
            return Token("$", None)
    def __init_lexer(self, string):
        self.string = string
        self.pos = 0
        self.char = string[0] if string else None
        self.status = self.start = 0
        self.back = None
        self.buffer = ""
        self.line = 1
        self.column = 1
    def parse(self, string):
        self.__init_lexer(string)
        self.value_stack = []
        self.state_stack = [0]
        self.index = 0
        self.token = self.lex()
        self.tp = self.token.type
        goto_table = self.goto_table
        action_table = self.action_table
        while True:
            self.state = self.state_stack[-1]
            if (self.state, self.tp) in action_table:
                action, arg = action_table[(self.state, self.tp)]
            elif (self.state, self.tp) in goto_table:
                self.state_stack.append(goto_table[(self.state, self.tp)])
                self.tp = self.token.type
                continue
            elif (self.state, "ε") in action_table:
                action, arg = action_table[(self.state, "ε")]
            else:
                raise SyntaxError(f"Unexpected token: {self.token.value}")
            if action == "SHIFT":
                self.state_stack.append(arg)
                self.index += 1
                self.value_stack.append(self.token)
                self.token = self.lex()
                self.tp = self.token.type
            elif action == "REDUCE":
                num = len(arg.body)
                for _ in range(num):
                    self.state_stack.pop()
                if arg.function:
                    args = [self.value_stack.pop() for _ in range(num)][::-1]
                    if isinstance(arg.function, str):
                        res = getattr(self, arg.function)(*args)
                    else:
                        res = arg.function(args)
                    self.value_stack.append(res)
                self.tp = arg.name
            elif action == "ACCEPT":
                break
        return self.value_stack.pop()


rule = Rule("""
@ignore " \t\r\n";
number : /[0-9](\\.[0-9][0-9]?)?/;
@priority "+" 1 left;
@priority "-" 1 left;
@priority "*" 0 left;
@priority "/" 0 left;
S    ->   Expr {output};
Expr ->   Expr "+" Expr {add}
        | Expr "-" Expr {sub}
        | Expr "*" Expr {mul}
        | Expr "/" Expr {div}
        | "(" Expr ")" {group}
        | number {number}
        ;
""")

class Calclator(Parser):
    def output(self, args):
        print(args[0])
    def add(self, args):
        return args[0] + args[1]
    def sub(self, args):
        return args[0] - args[1]
    def mul(self, args):
        return args[0] * args[1]
    def div(self, args):
        return args[0] / args[1]
    def group(self, args):
        return args[0]
    def number(self, args):
        val = args[0].value
        return int(val) if val.isdigit() else float(val)

calc = Calclator(rule)
calc.parse("(1+2)*3")