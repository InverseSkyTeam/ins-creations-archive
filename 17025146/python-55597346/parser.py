
class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value
    def __str__(self):
        return "Token(" + self.type + ", " + str(self.value) + ")"
    __repr__ = __str__

class Lexer:
    def __init__(self, string):
        self.string = string
        self.pos = 0
        self.char = string[0] if string else None
        self.status = self.start = 0
        self.back = None
        self.buffer = ""
        self.line = 1
        self.column = 1
        self.ignore = " \t\r\n"
        self.transition_table = [{'(': 1, ')': 4, '*': 5, '+': 6, '-': 7, '/': 8, '0': 9, '1': 9, '2': 9, '3': 9, '4': 9, '5': 9, '6': 9, '7': 9, '8': 9, '9': 9}, {'ACCEPT': '('}, {'\x00': 3, '\x01': 3, '\x02': 3, '\x03': 3, '\x04': 3, '\x05': 3, '\x06': 3, '\x07': 3, '\x08': 3, '\t': 3, '\n': 3, '\x0b': 3, '\x0c': 3, '\r': 3, '\x0e': 3, '\x0f': 3, '\x10': 3, '\x11': 3, '\x12': 3, '\x13': 3, '\x14': 3, '\x15': 3, '\x16': 3, '\x17': 3, '\x18': 3, '\x19': 3, '\x1a': 3, '\x1b': 3, '\x1c': 3, '\x1d': 3, '\x1e': 3, '\x1f': 3, ' ': 3, '!': 3, '"': 3, '#': 3, '$': 3, '%': 3, '&': 3, "'": 3, '(': 3, ')': 3, '*': 3, '+': 3, ',': 3, '-': 3, '.': 3, '/': 3, '0': 3, '1': 3, '2': 3, '3': 3, '4': 3, '5': 3, '6': 3, '7': 3, '8': 3, '9': 3, ':': 3, ';': 3, '<': 3, '=': 3, '>': 3, '?': 3, '@': 3, 'A': 3, 'B': 3, 'C': 3, 'D': 3, 'E': 3, 'F': 3, 'G': 3, 'H': 3, 'I': 3, 'J': 3, 'K': 3, 'L': 3, 'M': 3, 'N': 3, 'O': 3, 'P': 3, 'Q': 3, 'R': 3, 'S': 3, 'T': 3, 'U': 3, 'V': 3, 'W': 3, 'X': 3, 'Y': 3, 'Z': 3, '[': 3, '\\': 3, ']': 3, '^': 3, '_': 3, '`': 3, 'a': 3, 'b': 3, 'c': 3, 'd': 3, 'e': 3, 'f': 3, 'g': 3, 'h': 3, 'i': 3, 'j': 3, 'k': 3, 'l': 3, 'm': 3, 'n': 3, 'o': 3, 'p': 3, 'q': 3, 'r': 3, 's': 3, 't': 3, 'u': 3, 'v': 3, 'w': 3, 'x': 3, 'y': 3, 'z': 3, '{': 3, '|': 3, '}': 3, '~': 3}, {'0': 9, '1': 9, '2': 9, '3': 9, '4': 9, '5': 9, '6': 9, '7': 9, '8': 9, '9': 9}, {'ACCEPT': ')'}, {'ACCEPT': '*'}, {'ACCEPT': '+'}, {'ACCEPT': '-'}, {'ACCEPT': '/'}, {'\\': 2, 'ACCEPT': 'number', '0': 9, '1': 9, '2': 9, '3': 9, '4': 9, '5': 9, '6': 9, '7': 9, '8': 9, '9': 9}]
    
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
                    raise SyntaxError("Unexpected character: " + self.char)
                else:
                    self.pos, tp = self.back
                    res = Token(tp, self.buffer[:-1])
                    self.status = self.start
                    self.buffer = ""
                    self.back = None
                    self.advance()
                    self.status = self.start
                    return res
            else:
                if "ACCEPT" in self.transition_table[status]:
                    tp = self.transition_table[status]["ACCEPT"]
                    self.back = (self.pos, tp)
                    if self.pos == len(self.string) - 1:
                        res = Token(tp, self.buffer)
                        self.advance()
                        self.status = self.start
                        return res
            self.advance()
        if self.char is None:
            if self.status != self.start:
                raise SyntaxError("Unexpected end of file")
            return Token("$", None)


class Parser:
    def anomynous_0(self, args):
        return [args[0]]
    def anomynous_1(self, args):
        return [args[0],args[2]]
    def anomynous_2(self, args):
        return [args[0],args[2]]
    def anomynous_3(self, args):
        return [args[0],args[2]]
    def anomynous_4(self, args):
        return [args[0],args[2]]
    def anomynous_5(self, args):
        return [args[1]]
    def anomynous_6(self, args):
        return [args[0]]

    def __init__(self, lexer):
        self.lexer = lexer
        self.value_stack = []
        self.state_stack = [0]
        self.index = 0
        self.token = self.lexer.lex()
        self.tp = self.token.type
        self.goto_table = {(0, 'number'): 1, (0, '('): 2, (0, '0'): 3, (0, '1'): 4, (0, '2'): 5, (0, '3'): 6, (0, '4'): 7, (0, '5'): 8, (0, '6'): 9, (0, 'S'): 10, (0, 'Expr'): 11, (2, 'number'): 12, (2, '('): 13, (2, '1'): 14, (2, '2'): 15, (2, '3'): 16, (2, '4'): 17, (2, '5'): 18, (2, '6'): 19, (2, 'Expr'): 20, (11, '+'): 21, (11, '-'): 22, (11, '*'): 23, (11, '/'): 24, (13, 'number'): 25, (13, '('): 26, (13, '1'): 27, (13, '2'): 28, (13, '3'): 29, (13, '4'): 30, (13, '5'): 31, (13, '6'): 32, (13, 'Expr'): 33, (20, '+'): 34, (20, '-'): 35, (20, '*'): 36, (20, '/'): 37, (20, ')'): 38, (21, 'number'): 1, (21, '('): 2, (21, '1'): 4, (21, '2'): 5, (21, '3'): 6, (21, '4'): 7, (21, '5'): 8, (21, '6'): 9, (21, 'Expr'): 39, (22, 'number'): 1, (22, '('): 2, (22, '1'): 4, (22, '2'): 5, (22, '3'): 6, (22, '4'): 7, (22, '5'): 8, (22, '6'): 9, (22, 'Expr'): 40, (23, 'number'): 1, (23, '('): 2, (23, '1'): 4, (23, '2'): 5, (23, '3'): 6, (23, '4'): 7, (23, '5'): 8, (23, '6'): 9, (23, 'Expr'): 41, (24, 'number'): 1, (24, '('): 2, (24, '1'): 4, (24, '2'): 5, (24, '3'): 6, (24, '4'): 7, (24, '5'): 8, (24, '6'): 9, (24, 'Expr'): 42, (26, 'number'): 25, (26, '('): 26, (26, '1'): 27, (26, '2'): 28, (26, '3'): 29, (26, '4'): 30, (26, '5'): 31, (26, '6'): 32, (26, 'Expr'): 43, (33, '+'): 44, (33, '-'): 45, (33, '*'): 46, (33, '/'): 47, (33, ')'): 48, (34, 'number'): 12, (34, '('): 13, (34, '1'): 14, (34, '2'): 15, (34, '3'): 16, (34, '4'): 17, (34, '5'): 18, (34, '6'): 19, (34, 'Expr'): 49, (35, 'number'): 12, (35, '('): 13, (35, '1'): 14, (35, '2'): 15, (35, '3'): 16, (35, '4'): 17, (35, '5'): 18, (35, '6'): 19, (35, 'Expr'): 50, (36, 'number'): 12, (36, '('): 13, (36, '1'): 14, (36, '2'): 15, (36, '3'): 16, (36, '4'): 17, (36, '5'): 18, (36, '6'): 19, (36, 'Expr'): 51, (37, 'number'): 12, (37, '('): 13, (37, '1'): 14, (37, '2'): 15, (37, '3'): 16, (37, '4'): 17, (37, '5'): 18, (37, '6'): 19, (37, 'Expr'): 52, (39, '+'): 21, (39, '-'): 22, (39, '*'): 23, (39, '/'): 24, (40, '+'): 21, (40, '-'): 22, (40, '*'): 23, (40, '/'): 24, (41, '+'): 21, (41, '-'): 22, (41, '*'): 23, (41, '/'): 24, (42, '+'): 21, (42, '-'): 22, (42, '*'): 23, (42, '/'): 24, (43, '+'): 44, (43, '-'): 45, (43, '*'): 46, (43, '/'): 47, (43, ')'): 53, (44, 'number'): 25, (44, '('): 26, (44, '1'): 27, (44, '2'): 28, (44, '3'): 29, (44, '4'): 30, (44, '5'): 31, (44, '6'): 32, (44, 'Expr'): 54, (45, 'number'): 25, (45, '('): 26, (45, '1'): 27, (45, '2'): 28, (45, '3'): 29, (45, '4'): 30, (45, '5'): 31, (45, '6'): 32, (45, 'Expr'): 55, (46, 'number'): 25, (46, '('): 26, (46, '1'): 27, (46, '2'): 28, (46, '3'): 29, (46, '4'): 30, (46, '5'): 31, (46, '6'): 32, (46, 'Expr'): 56, (47, 'number'): 25, (47, '('): 26, (47, '1'): 27, (47, '2'): 28, (47, '3'): 29, (47, '4'): 30, (47, '5'): 31, (47, '6'): 32, (47, 'Expr'): 57, (49, '+'): 34, (49, '-'): 35, (49, '*'): 36, (49, '/'): 37, (50, '+'): 34, (50, '-'): 35, (50, '*'): 36, (50, '/'): 37, (51, '+'): 34, (51, '-'): 35, (51, '*'): 36, (51, '/'): 37, (52, '+'): 34, (52, '-'): 35, (52, '*'): 36, (52, '/'): 37, (54, '+'): 44, (54, '-'): 45, (54, '*'): 46, (54, '/'): 47, (55, '+'): 44, (55, '-'): 45, (55, '*'): 46, (55, '/'): 47, (56, '+'): 44, (56, '-'): 45, (56, '*'): 46, (56, '/'): 47, (57, '+'): 44, (57, '-'): 45, (57, '*'): 46, (57, '/'): 47}
        self.action_table = {(0, 'number'): ('SHIFT', 1), (0, '('): ('SHIFT', 2), (1, '$'): ('REDUCE', ('6', 1, 'anomynous_6')), (1, '+'): ('REDUCE', ('6', 1, 'anomynous_6')), (1, '-'): ('REDUCE', ('6', 1, 'anomynous_6')), (1, '*'): ('REDUCE', ('6', 1, 'anomynous_6')), (1, '/'): ('REDUCE', ('6', 1, 'anomynous_6')), (1, 'ε'): ('REDUCE', ('6', 1, 'anomynous_6')), (2, 'number'): ('SHIFT', 12), (2, '('): ('SHIFT', 13), (3, '$'): ('REDUCE', ('S', 1, 'output')), (4, '$'): ('REDUCE', ('Expr', 1, 'add')), (4, '+'): ('REDUCE', ('Expr', 1, 'add')), (4, '-'): ('REDUCE', ('Expr', 1, 'add')), (4, '*'): ('REDUCE', ('Expr', 1, 'add')), (4, '/'): ('REDUCE', ('Expr', 1, 'add')), (4, 'ε'): ('REDUCE', ('Expr', 1, 'add')), (5, '$'): ('REDUCE', ('Expr', 1, 'sub')), (5, '+'): ('REDUCE', ('Expr', 1, 'sub')), (5, '-'): ('REDUCE', ('Expr', 1, 'sub')), (5, '*'): ('REDUCE', ('Expr', 1, 'sub')), (5, '/'): ('REDUCE', ('Expr', 1, 'sub')), (5, 'ε'): ('REDUCE', ('Expr', 1, 'sub')), (6, '$'): ('REDUCE', ('Expr', 1, 'mul')), (6, '+'): ('REDUCE', ('Expr', 1, 'mul')), (6, '-'): ('REDUCE', ('Expr', 1, 'mul')), (6, '*'): ('REDUCE', ('Expr', 1, 'mul')), (6, '/'): ('REDUCE', ('Expr', 1, 'mul')), (6, 'ε'): ('REDUCE', ('Expr', 1, 'mul')), (7, '$'): ('REDUCE', ('Expr', 1, 'div')), (7, '+'): ('REDUCE', ('Expr', 1, 'div')), (7, '-'): ('REDUCE', ('Expr', 1, 'div')), (7, '*'): ('REDUCE', ('Expr', 1, 'div')), (7, '/'): ('REDUCE', ('Expr', 1, 'div')), (7, 'ε'): ('REDUCE', ('Expr', 1, 'div')), (8, '$'): ('REDUCE', ('Expr', 1, 'group')), (8, '+'): ('REDUCE', ('Expr', 1, 'group')), (8, '-'): ('REDUCE', ('Expr', 1, 'group')), (8, '*'): ('REDUCE', ('Expr', 1, 'group')), (8, '/'): ('REDUCE', ('Expr', 1, 'group')), (8, 'ε'): ('REDUCE', ('Expr', 1, 'group')), (9, '$'): ('REDUCE', ('Expr', 1, 'number')), (9, '+'): ('REDUCE', ('Expr', 1, 'number')), (9, '-'): ('REDUCE', ('Expr', 1, 'number')), (9, '*'): ('REDUCE', ('Expr', 1, 'number')), (9, '/'): ('REDUCE', ('Expr', 1, 'number')), (9, 'ε'): ('REDUCE', ('Expr', 1, 'number')), (10, '$'): ('ACCEPT', None), (11, '$'): ('REDUCE', ('0', 1, 'anomynous_0')), (11, '+'): ('SHIFT', 21), (11, '-'): ('SHIFT', 22), (11, '*'): ('SHIFT', 23), (11, '/'): ('SHIFT', 24), (12, ')'): ('REDUCE', ('6', 1, 'anomynous_6')), (12, 'ε'): ('REDUCE', ('6', 1, 'anomynous_6')), (13, 'number'): ('SHIFT', 25), (13, '('): ('SHIFT', 26), (14, ')'): ('REDUCE', ('Expr', 1, 'add')), (14, 'ε'): ('REDUCE', ('Expr', 1, 'add')), (15, ')'): ('REDUCE', ('Expr', 1, 'sub')), (15, 'ε'): ('REDUCE', ('Expr', 1, 'sub')), (16, ')'): ('REDUCE', ('Expr', 1, 'mul')), (16, 'ε'): ('REDUCE', ('Expr', 1, 'mul')), (17, ')'): ('REDUCE', ('Expr', 1, 'div')), (17, 'ε'): ('REDUCE', ('Expr', 1, 'div')), (18, ')'): ('REDUCE', ('Expr', 1, 'group')), (18, 'ε'): ('REDUCE', ('Expr', 1, 'group')), (19, ')'): ('REDUCE', ('Expr', 1, 'number')), (19, 'ε'): ('REDUCE', ('Expr', 1, 'number')), (20, '+'): ('SHIFT', 34), (20, '-'): ('SHIFT', 35), (20, '*'): ('SHIFT', 36), (20, '/'): ('SHIFT', 37), (20, ')'): ('SHIFT', 38), (21, 'number'): ('SHIFT', 1), (21, '('): ('SHIFT', 2), (22, 'number'): ('SHIFT', 1), (22, '('): ('SHIFT', 2), (23, 'number'): ('SHIFT', 1), (23, '('): ('SHIFT', 2), (24, 'number'): ('SHIFT', 1), (24, '('): ('SHIFT', 2), (25, 'ε'): ('REDUCE', ('6', 1, 'anomynous_6')), (26, 'number'): ('SHIFT', 25), (26, '('): ('SHIFT', 26), (27, 'ε'): ('REDUCE', ('Expr', 1, 'add')), (28, 'ε'): ('REDUCE', ('Expr', 1, 'sub')), (29, 'ε'): ('REDUCE', ('Expr', 1, 'mul')), (30, 'ε'): ('REDUCE', ('Expr', 1, 'div')), (31, 'ε'): ('REDUCE', ('Expr', 1, 'group')), (32, 'ε'): ('REDUCE', ('Expr', 1, 'number')), (33, '+'): ('SHIFT', 44), (33, '-'): ('SHIFT', 45), (33, '*'): ('SHIFT', 46), (33, '/'): ('SHIFT', 47), (33, ')'): ('SHIFT', 48), (34, 'number'): ('SHIFT', 12), (34, '('): ('SHIFT', 13), (35, 'number'): ('SHIFT', 12), (35, '('): ('SHIFT', 13), (36, 'number'): ('SHIFT', 12), (36, '('): ('SHIFT', 13), (37, 'number'): ('SHIFT', 12), (37, '('): ('SHIFT', 13), (38, '$'): ('REDUCE', ('5', 3, 'anomynous_5')), (38, '+'): ('REDUCE', ('5', 3, 'anomynous_5')), (38, '-'): ('REDUCE', ('5', 3, 'anomynous_5')), (38, '*'): ('REDUCE', ('5', 3, 'anomynous_5')), (38, '/'): ('REDUCE', ('5', 3, 'anomynous_5')), (38, 'ε'): ('REDUCE', ('5', 3, 'anomynous_5')), (39, '$'): ('REDUCE', ('1', 3, 'anomynous_1')), (39, '+'): ('SHIFT', 21), (39, '-'): ('SHIFT', 22), (39, '*'): ('SHIFT', 23), (39, '/'): ('SHIFT', 24), (39, 'ε'): ('REDUCE', ('1', 3, 'anomynous_1')), (40, '$'): ('REDUCE', ('2', 3, 'anomynous_2')), (40, '+'): ('SHIFT', 21), (40, '-'): ('SHIFT', 22), (40, '*'): ('SHIFT', 23), (40, '/'): ('SHIFT', 24), (40, 'ε'): ('REDUCE', ('2', 3, 'anomynous_2')), (41, '$'): ('REDUCE', ('3', 3, 'anomynous_3')), (41, '+'): ('SHIFT', 21), (41, '-'): ('SHIFT', 22), (41, '*'): ('SHIFT', 23), (41, '/'): ('SHIFT', 24), (41, 'ε'): ('REDUCE', ('3', 3, 'anomynous_3')), (42, '$'): ('REDUCE', ('4', 3, 'anomynous_4')), (42, '+'): ('SHIFT', 21), (42, '-'): ('SHIFT', 22), (42, '*'): ('SHIFT', 23), (42, '/'): ('SHIFT', 24), (42, 'ε'): ('REDUCE', ('4', 3, 'anomynous_4')), (43, '+'): ('SHIFT', 44), (43, '-'): ('SHIFT', 45), (43, '*'): ('SHIFT', 46), (43, '/'): ('SHIFT', 47), (43, ')'): ('SHIFT', 53), (44, 'number'): ('SHIFT', 25), (44, '('): ('SHIFT', 26), (45, 'number'): ('SHIFT', 25), (45, '('): ('SHIFT', 26), (46, 'number'): ('SHIFT', 25), (46, '('): ('SHIFT', 26), (47, 'number'): ('SHIFT', 25), (47, '('): ('SHIFT', 26), (48, ')'): ('REDUCE', ('5', 3, 'anomynous_5')), (48, 'ε'): ('REDUCE', ('5', 3, 'anomynous_5')), (49, ')'): ('REDUCE', ('1', 3, 'anomynous_1')), (49, 'ε'): ('REDUCE', ('1', 3, 'anomynous_1')), (49, '+'): ('SHIFT', 34), (49, '-'): ('SHIFT', 35), (49, '*'): ('SHIFT', 36), (49, '/'): ('SHIFT', 37), (50, ')'): ('REDUCE', ('2', 3, 'anomynous_2')), (50, 'ε'): ('REDUCE', ('2', 3, 'anomynous_2')), (50, '+'): ('SHIFT', 34), (50, '-'): ('SHIFT', 35), (50, '*'): ('SHIFT', 36), (50, '/'): ('SHIFT', 37), (51, ')'): ('REDUCE', ('3', 3, 'anomynous_3')), (51, 'ε'): ('REDUCE', ('3', 3, 'anomynous_3')), (51, '+'): ('SHIFT', 34), (51, '-'): ('SHIFT', 35), (51, '*'): ('SHIFT', 36), (51, '/'): ('SHIFT', 37), (52, ')'): ('REDUCE', ('4', 3, 'anomynous_4')), (52, 'ε'): ('REDUCE', ('4', 3, 'anomynous_4')), (52, '+'): ('SHIFT', 34), (52, '-'): ('SHIFT', 35), (52, '*'): ('SHIFT', 36), (52, '/'): ('SHIFT', 37), (53, 'ε'): ('REDUCE', ('5', 3, 'anomynous_5')), (54, 'ε'): ('REDUCE', ('1', 3, 'anomynous_1')), (54, '+'): ('SHIFT', 44), (54, '-'): ('SHIFT', 45), (54, '*'): ('SHIFT', 46), (54, '/'): ('SHIFT', 47), (55, 'ε'): ('REDUCE', ('2', 3, 'anomynous_2')), (55, '+'): ('SHIFT', 44), (55, '-'): ('SHIFT', 45), (55, '*'): ('SHIFT', 46), (55, '/'): ('SHIFT', 47), (56, 'ε'): ('REDUCE', ('3', 3, 'anomynous_3')), (56, '+'): ('SHIFT', 44), (56, '-'): ('SHIFT', 45), (56, '*'): ('SHIFT', 46), (56, '/'): ('SHIFT', 47), (57, 'ε'): ('REDUCE', ('4', 3, 'anomynous_4')), (57, '+'): ('SHIFT', 44), (57, '-'): ('SHIFT', 45), (57, '*'): ('SHIFT', 46), (57, '/'): ('SHIFT', 47)}
        self.nonterminals = ['S', 'Expr']

    def parse(self):
        action_table = self.action_table
        goto_table = self.goto_table
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
                raise SyntaxError("Unexpected token: " + str(self.token))
            if action == "SHIFT":
                self.state_stack.append(arg)
                self.index += 1
                self.value_stack.append(self.token)
                self.token = self.lexer.lex()
                self.tp = self.token.type
            elif action == "REDUCE":
                name, num, function = arg
                for _ in range(num):
                    self.state_stack.pop()
                if function:
                    args = [self.value_stack.pop() for _ in range(num)][::-1]
                    if name in self.nonterminals:
                        res = getattr(self, function)(*args)
                    else:
                        res = getattr(self, function)(args)
                    self.value_stack.append(res)
                self.tp = name
            elif action == "ACCEPT":
                break
        return self.value_stack.pop()

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