from .unicode_trie import UnicodeTrie
from .classes import BK, CR, LF, NL, SG, WJ, SP, ZWJ, BA, HY, NS, AI, AL, CJ, HL, RI, SA, XX
from .pairs import DI_BRK, IN_BRK, CI_BRK, CP_BRK, PR_BRK, pairTable
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'classes.trie')
with open(file_path, 'rb') as f:
    data = f.read()  # 这不比 node.js 的 base64 好用多了

classTrie = UnicodeTrie(data)


def mapClass(c):
    if c == AI:
        return AL
    elif c == SA or c == SG or c == XX:
        return AL
    elif c == CJ:
        return NS
    else:
        return c


def mapFirst(c):
    if c == LF or c == NL:
        return BK
    elif c == SP:
        return WJ
    else:
        return c


class String:
    def __init__(self, data):
        self.data = data.encode('utf-16be')
    
    @property
    def length(self):
        return len(self.data) // 2
    
    def charCodeAt(self, index):
        if index * 2 + 1 >= len(self.data):
            return float('nan')
        return self.data[index * 2] * 0x100 + self.data[index * 2 + 1]


class Break:
    def __init__(self, position, required=False):
        self.position = position
        self.required = required


class LineBreaker:
    def __init__(self, string):
        self.string = string if isinstance(string, String) else String(string)
        self.pos = 0
        self.lastPos = 0
        self.curClass = None
        self.nextClass = None
        self.LB8a = False
        self.LB21a = False
        self.LB30a = 0

    def nextCodePoint(self):
        code = self.string.charCodeAt(self.pos)
        _next = self.string.charCodeAt(self.pos + 1)
        self.pos += 1

        # If a surrogate pair
        if (0xd800 <= code <= 0xdbff) and (0xdc00 <= _next <= 0xdfff):
            self.pos += 1
            return ((code - 0xd800) * 0x400) + (_next - 0xdc00) + 0x10000
        return code

    def nextCharClass(self):
        return mapClass(classTrie.get(self.nextCodePoint()))

    def getSimpleBreak(self):
        # handle classes not handled by the pair table
        c = self.nextClass
        if c == SP:
            return False

        elif c == BK or c == LF or c == NL:
            self.curClass = BK
            return False

        elif c == CR:
            self.curClass = CR
            return False

        return None

    def getPairTableBreak(self, lastClass):
        # if not handled already, use the pair table
        shouldBreak = False
        c = pairTable[self.curClass][self.nextClass]
        if c == DI_BRK: # Direct break
            shouldBreak = True

        elif c == IN_BRK: # possible indirect break
            shouldBreak = lastClass == SP

        elif c == CI_BRK:
            shouldBreak = lastClass == SP
            if not shouldBreak:
                shouldBreak = False
                return shouldBreak

        elif c == CP_BRK: # prohibited for combining marks
            if lastClass != SP:
                return shouldBreak

        elif c == PR_BRK:
            ...  # break

        if self.LB8a:
            shouldBreak = False

        # Rule LB21a
        if self.LB21a and (self.curClass == HY or self.curClass == BA):
            shouldBreak = False
            self.LB21a = False
        else:
            self.LB21a = (self.curClass == HL)

        # Rule LB30a
        if self.curClass == RI:
            self.LB30a += 1
            if self.LB30a == 2 and (self.nextClass == RI):
                shouldBreak = True
                self.LB30a = 0
        else:
            self.LB30a = 0

        self.curClass = self.nextClass

        return shouldBreak

    def nextBreak(self):
        # get the first char if we're at the beginning of the string
        if self.curClass is None:
            firstClass = self.nextCharClass()
            self.curClass = mapFirst(firstClass)
            self.nextClass = firstClass
            self.LB8a = (firstClass == ZWJ)
            self.LB30a = 0

        while self.pos < self.string.length:
            self.lastPos = self.pos
            lastClass = self.nextClass
            self.nextClass = self.nextCharClass()

            # explicit newline
            if (self.curClass == BK) or ((self.curClass == CR) and (self.nextClass != LF)):
                self.curClass = mapFirst(mapClass(self.nextClass))
                return Break(self.lastPos, True)

            shouldBreak = self.getSimpleBreak()

            if shouldBreak is None:
                shouldBreak = self.getPairTableBreak(lastClass)

            # Rule LB8a
            self.LB8a = (self.nextClass == ZWJ)

            if shouldBreak:
                return Break(self.lastPos)

        if self.lastPos < self.string.length:
            self.lastPos = self.string.length
            return Break(self.string.length)

        return None
