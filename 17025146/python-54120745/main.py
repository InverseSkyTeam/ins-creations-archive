import enum

class NFA:
    def __init__(self):
        self.edge = "EPSILON"
        self.next_1 = None
        self.next_2 = None
class DFA:
    STATUS = -1
    def __init__(self, nfas):
        DFA.STATUS += 1
        self.nfas = nfas
        self.accepted = False
        for i in nfas:
            if i.next_1 is None and i.next_2 is None:
                self.accepted = True
        self.status = DFA.STATUS
class DFAGroup:
    STATUS = -1
    def __init__(self, dfas):
        DFAGroup.STATUS += 1
        self.status = DFAGroup.STATUS
        self.dfas = dfas
    def get(self, index):
        return self.dfas[index] if index < len(self.dfas) else None
    def __str__(self):
        return str(list(map(lambda x:x.status, self.dfas)))
    __repr__ = __str__
class Token(enum.Enum):
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

class Lexer:
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
            '.': Token.ANY,
            '^': Token.AT_BOL,
            '$': Token.AT_EOL,
            ']': Token.CCL_END,
            '[': Token.CCL_START,
            '}': Token.CLOSE_CURLY,
            ')': Token.CLOSE_PAREN,
            '*': Token.CLOSURE,
            '-': Token.DASH,
            '{': Token.OPEN_CURLY,
            '(': Token.OPEN_PAREN,
            '?': Token.OPTIONAL,
            '|': Token.OR,
            '+': Token.PLUS_CLOSE,
        }
        self.advance()
    def advance(self):
        self.pos += 1
        if self.pos > len(self.pattern) - 1:
            self.current_token = Token.EOS
            self.lexeme = None
            return False
        self.lexeme = self.pattern[self.pos]
        if self.lexeme == "\\":
            self.pos += 1
            char = self.pattern[self.pos].lower()
            self.lexeme = self.ev.get(char, char)
            self.current_token = Token.L
        else:
            self.current_token = self.tokens.get(self.lexeme, Token.L)
class Parser:
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
        while self.lexer.current_token != Token.CCL_END:
            if self.lexer.current_token == Token.DASH:
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
        if self.lexer.current_token == Token.L:
            start.edge = self.lexer.lexeme
            start.next_1 = NFA()
            end = start.next_1
            self.lexer.advance()
        elif self.lexer.current_token == Token.ANY:
            start.edge = self.ascii_table
            start.next_1 = NFA()
            end = start.next_1
            self.lexer.advance()
        elif self.lexer.current_token == Token.CCL_START:
            self.lexer.advance()
            if self.lexer.current_token == Token.AT_BOL:
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
        elif self.lexer.current_token == Token.OPEN_PAREN:
            self.lexer.advance()
            start, end = self.expr()
            if self.lexer.current_token != Token.CLOSE_PAREN:
                raise ValueError("Missing closing parenthesis")
            self.lexer.advance()
        return start, end
    def factor(self):
        start, end = self.term()
        new_start = NFA()
        new_end = NFA()
        if self.lexer.current_token == Token.CLOSURE:
            new_start.next_1 = start
            new_start.next_2 = new_end
            end.next_1 = start
            end.next_2 = new_end
            start, end = new_start, new_end
            self.lexer.advance()
        elif self.lexer.current_token == Token.PLUS_CLOSE:
            new_start.next_1 = start
            end.next_1 = start
            end.next_2 = new_end
            self.lexer.advance()
            start, end = new_start, new_end
        elif self.lexer.current_token == Token.OPTIONAL:
            new_start.next_1 = start
            new_start.next_2 = new_end
            end.next_2 = new_end
            self.lexer.advance()
            start, end = new_start, new_end
        return start, end
    def factor_conn(self):
        start, end = self.factor()
        while self.lexer.current_token in (Token.L, Token.ANY, Token.CCL_START, Token.OPEN_PAREN):
            new_start, new_end = self.factor()
            end.next_1 = new_start
            end = new_end
        return start, end
    def expr(self):
        start, end = self.factor_conn()
        while self.lexer.current_token == Token.OR:
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

def closure(input_set):
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
    dfa_list.append(DFA(closure([nfa])))
    jump_table = [{}]
    index = 0
    while index < len(dfa_list):
        current = dfa_list[index]
        for i in range(127):
            char = chr(i)
            moved = move(current.nfas, char)
            if not moved:
                continue
            nfa_closure = closure(moved)
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
    if accept:
        group_list.append(DFAGroup(accept))
    if non_accept:
        group_list.append(DFAGroup(non_accept))
    for group in group_list:
        if len(group.dfas) != 1:
            for i in range(127):
                group1 = []
                group2 = []
                group3 = []
                for x in group.dfas:
                    char = chr(i)
                    goto = jump_table[x.status].get(char)
                    goto_group = dfa_in_group(goto, group_list)
                    if goto_group is None and x not in group3:
                        group3.append(x)
                        continue
                    if goto_group == group and x not in group1:
                        group1.append(x)
                    if goto_group != group and x not in group2:
                        group2.append(x)
                if group1 and group2 and group3:
                    group.dfas = group1
                    group_list.append(DFAGroup(group2))
                    group_list.append(DFAGroup(group3))
    return group_list
def create_transition_table(dfa_list, jump_table, group_list):
    transition_table = [{} for i in range(len(group_list))]
    for dfa in dfa_list:
        for i in range(127):
            char = chr(i)
            to = jump_table[dfa.status].get(char)
            if to is None:
                continue
            from_group = dfa_in_group(dfa.status, group_list)
            to_group = dfa_in_group(to, group_list)
            transition_table[from_group.status][char] = to_group.status
        if dfa.accepted:
            from_group = dfa_in_group(dfa.status, group_list)
            transition_table[from_group.status]["ACCEPT"] = True
    return transition_table
def match(pattern, string):
    lexer = Lexer(pattern)
    parser = Parser(lexer)
    start, _end = parser.expr()
    dfa_list, jump_table = nfa_to_dfa(start)
    group_list = minimize_dfa(dfa_list, jump_table)
    transition_table = create_transition_table(dfa_list, jump_table, group_list)
    status = group_list[0].STATUS
    for i in string:
        status = transition_table[status].get(i)
        if status is None:
            return False
    return transition_table[status].get("ACCEPT") is not None

print(match("\\-?[0-9][0-9]?[0-9]?(,[0-9][0-9][0-9])*(\\.[0-9][0-9]?)?", "1.1"))