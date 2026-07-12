from renderer import Parser
from enum import Enum  # , unique
from keyword import kwlist
from typing import List


builtins = dir(__builtins__)


# @unique
class PyStatus(Enum):  # 每行尾状态的枚举类型
    Unknown = -1
    Null = 0
    StrPass = 1  # 单引号单行字符串
    Str2Pass = 2  # 双引号单行字符串
    StrLong = 3  # 单引号多行字符串
    Str2Long = 4  # 双引号多行字符串


# @unique
class PyToken(Enum):
    Unknown = -1
    Id = 0
    Num = 1
    Builtin = 2
    Keyword = 3
    Str = 4
    Comment = 5
    Operator = 6
    Other = 7


PyTokenDict = [
    "id",
    "num",
    "builtin",
    "kw",
    "str",
    "comment",
    "op",
    "text",
]

pyOpSet = set("~!%^&*/()-+=[{}]|;:,.<>")


class PythonParser(Parser):
    def __init__(self, text: List[str]):
        super().__init__(text)
        self.status = [PyStatus.Unknown for _ in range(len(self.text))]
        self.cache = [[] for _ in range(len(self.text))]

    # 还没改完
    '''def change(self, line: int):
        super().change(line)
        self.status[line] = PyStatus.Unknown

    def add(self, begin: int, end: int):
        super().add(begin, end)
        self.status = (
            self.status[:begin]
            + [PyStatus.Unknown for _ in range(begin, end + 1)]
            + self.status[begin:]
        )
        self.cache = (
            self.cache[:begin] + [[] for _ in range(begin, end + 1)] + self.cache[begin:]
        )

    def remove(self, begin: int, end: int):
        super().remove(begin, end)
        del self.status[begin : end + 1]
        del self.cache[begin : end + 1]'''
    
    @staticmethod
    def is_vaild_char(char):
        return char.isalnum() or char == '_'
    
    @staticmethod
    def get_quote(text, pos):  # 确定是字符串时，可以获取字符串的引号
        if text[pos: pos+3] in ('"""', "'''"):
            return text[pos: pos+3]
        return text[pos]
    
    @staticmethod
    def is_quote(text, pos, quote):
        return text[pos: pos + len(quote)] == quote
    
    @staticmethod
    def status_to_quote(status):
        data = {
            PyStatus.StrPass: "'",
            PyStatus.Str2Pass: '"',
            PyStatus.StrLong: "'''",
            PyStatus.Str2Long: '"""'
        }
        return data[status]
    
    @staticmethod
    def quote_to_status(quote):
        data = {
            "'": PyStatus.StrPass,
            '"': PyStatus.Str2Pass,
            "'''": PyStatus.StrLong,
            '"""': PyStatus.Str2Long
        }
        return data[quote]
    
    def parse_word(self, text, pos):
        begin = pos
        while pos < len(text) and self.is_vaild_char(text[pos]):
            pos += 1
        
        word = text[begin: pos]
        if word in kwlist:
            token = PyToken.Keyword
        elif word in builtins:
            token = PyToken.Builtin
        elif word.isdecimal():
            token = PyToken.Num
        else:
            token = PyToken.Id
        return token, len(word)
    
    def parse_string(self, text, pos, status):
        quote = self.status_to_quote(status)
        warp = len(quote) == 3  # 是否是多行字符串
        
        begin = pos
        while pos < len(text):
            char = text[pos]
            if char == '\\':  # 转义字符
                if pos + 1 == len(text):  # 转义字符在行尾
                    return len(text) - begin, status
                else:
                    pos += 2
            elif self.is_quote(text, pos, quote):  # 字符串结束
                return pos - begin + len(quote), PyStatus.Null
            else:  # 普通字符
                pos += 1
        return len(text) - begin, (status if warp else PyStatus.Null)

    def render_line(self, line: int):
        status = self.status[line - 1] if line > 0 else PyStatus.Null 
        assert status != PyStatus.Unknown
        text = self.text[line]
        self.cache[line] = [PyToken.Unknown] * len(text)
        cache = self.cache[line]
        
        pos = 0

        if status != PyStatus.Null:
            length, status = self.parse_string(text, pos, status)
            cache[pos: pos + length] = [PyToken.Str] * length
            pos += length
            if status != PyStatus.Null:
                return status

        # 词进式，每次一个单词
        while pos < len(text):
            char = text[pos]
            if self.is_vaild_char(char):
                token, length = self.parse_word(text, pos)
                cache[pos: pos + length] = [token] * length
                pos += length
            elif char in "\"'":
                quote = self.get_quote(text, pos)
                status = self.quote_to_status(quote)
                
                cache[pos: pos + len(quote)] = [PyToken.Str] * len(quote)
                pos += len(quote)
                
                length, status = self.parse_string(text, pos, status)
                cache[pos: pos + length] = [PyToken.Str] * length
                pos += length
                
                if status != PyStatus.Null:
                    return status
            elif char in pyOpSet:
                cache[pos] = PyToken.Operator
                pos += 1
            elif char.isspace():
                cache[pos] = PyToken.Other
                pos += 1
            elif char == "#":
                length = len(text) - pos
                cache[pos:] = [PyToken.Comment] * length
                break
            else:
                cache[pos] = PyToken.Other
                pos += 1
        return PyStatus.Null

    def render(self, target: int):
        assert target < len(self.text)
        while target >= self.unk_begin and self.unk_begin < len(self.text):
            old_st = self.status[self.unk_begin]
            self.status[self.unk_begin] = self.render_line(self.unk_begin)
            self.changes[self.unk_begin] = False
            # 上一行尾状态不变且本行未改变
            while (
                self.status[self.unk_begin] == old_st
                and not self.changes[self.unk_begin]
                and self.unk_begin < len(self.text) - 1
            ):
                old_st = self.status[self.unk_begin]
                self.unk_begin += 1
            self.unk_begin += 1

    def get(self, y: int, x: int) -> str:
        assert y < len(self.text)
        self.render(y)
        return PyTokenDict[self.cache[y][x].value]


colortable = {
    'num': "\033[96m",
    'str': "\033[92m",
    'builtin': "\033[94m",
    'kw': "\033[95m",
    'text': "\033[97m",
    'op': "\033[93m",
    'id': "\033[97m",
    'comment': "\033[90m",
}
import time
text = r"""
r'\'', fr'x', ur'x\
hhh', 114
'2345
514
'''123
456
7''
'''1145
"""
with open('test.py', 'r', encoding='utf-8') as f:
    text = (f.read() + '\n') * 1
code = text.split('\n')

a = PythonParser(code)

b = time.time()
for i in range(len(code)):
    if len(code[i]) > 0:
        a.get(i, 0)
c = time.time()


for i, line in enumerate(code):
    for j, char in enumerate(line):
        color = colortable[a.get(i, j)]
        print(color, end='')
        print(char, end='')
    print()

print('\033[97m', end='')

print('代码行数:', len(code))
print('高亮用时:', c-b)

