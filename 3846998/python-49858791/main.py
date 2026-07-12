import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.scrolledtext import ScrolledText
import re
from enum import Enum
from keyword import kwlist as py_kwlist


class PyTokenType(Enum):
    OPERATOR = 0
    KEYWORD = 1
    NUMBER = 2
    IDENT = 3
    SYMBOL = 4
    STRING = 7
    ESCAPE = 8
    COMMENT = 9


py_tokentp_map = {
    PyTokenType.OPERATOR: "op",
    PyTokenType.KEYWORD: "kw",
    PyTokenType.NUMBER: "num",
    PyTokenType.IDENT: "id",
    PyTokenType.SYMBOL: "sym",
    PyTokenType.STRING: "str",
    PyTokenType.ESCAPE: "esc",
    PyTokenType.COMMENT: "cmt",
}
py_colorscheme = {
    "op": "gray",
    "kw": "blue",
    "num": "blue",
    "id": "black",
    "sym": "black",
    "str": "green",
    "esc": "blue",
    "cmt": "green",
}
py_operators = {
    '+', '-', '**', '*', '/', '%',
    '==', '!=', '>', '<', '>=', '<=',
    '<<', '>>', '&', '|', '^'
    '!', '~',
}
py_symbols = {
    '(', ')', '[', ']', '{', '}',
    ',', '.', ':', ';',
    '=', '+=', '-=', '*=', '/=', '%=',
    '>>=', '<<=', '&=', '|=', '^=',
}


class Token:
    def __init__(self, tp: PyTokenType, y1: int, x1: int, y2: int, x2: int):
        self.tp, self.y1, self.x1, self.y2, self.x2 = tp, y1, x1, y2, x2


def py_tokenize(text: str):
    # NOTE: Tkinter的高亮是前开后闭区间，tokenizer得到的是前闭后开区间
    # 解决：减一
    def next():
        nonlocal x, y, pos
        if text[pos] == "\n":
            y += 1
            x = 1
        else:
            x += 1
        pos += 1

    pos = 0
    res = []
    y, x = 1, 1

    while pos < len(text):
        while pos < len(text) and text[pos] in ' \n\t#':
            if text[pos] in ' \n\t':
                next()
            else:
                y1, x1 = y, x
                while pos < len(text) and text[pos] != '\n':
                    next()
                res.append(Token(PyTokenType.COMMENT, y1, x1, y, x))
        if pos >= len(text):
            break
        elif text[pos].isdigit():
            y1, x1 = y, x
            while pos < len(text) and (text[pos].isdigit() or text[pos] in '.box'):
                next()
            res.append(Token(PyTokenType.NUMBER, y1, x1, y, x))
        elif text[pos].isalpha() or text[pos] == '_':
            y1, x1 = y, x
            ident = ""
            while pos < len(text) and (text[pos].isalnum() or text[pos] == '_'):
                ident += text[pos]
                next()
            if ident in py_kwlist:
                res.append(Token(PyTokenType.KEYWORD, y1, x1, y, x))
            else:
                res.append(Token(PyTokenType.IDENT, y1, x1, y, x))
        elif text[pos] in '\'"':
            xx = text[pos]
            y1, x1 = y, x
            next()
            escapes = []
            while pos < len(text) and text[pos] not in (xx, '\n'):
                if text[pos] == '\\':
                    ey1, ex1 = y, x
                    next()
                    if pos >= len(text):
                        break
                    if text[pos] == '\n':
                        next()
                    elif text[pos] == 'u':
                        next()
                        for i in range(4):
                            if pos < len(text):
                                next()
                            else:
                                break
                        escapes.append(
                            Token(PyTokenType.ESCAPE, ey1, ex1, y, x))
                    elif text[pos] == 'x':
                        next()
                        for i in range(2):
                            if pos < len(text):
                                next()
                            else:
                                break
                        escapes.append(
                            Token(PyTokenType.ESCAPE, ey1, ex1, y, x))
                    elif text[pos].isdigit():
                        for i in range(3):
                            if pos < len(text) and text[pos].isdigit():
                                next()
                            else:
                                break
                        escapes.append(
                            Token(PyTokenType.ESCAPE, ey1, ex1, y, x))
                    else:
                        next()
                        escapes.append(
                            Token(PyTokenType.ESCAPE, ey1, ex1, y, x))
                else:
                    next()
            if pos >= len(text):
                break
            next()
            res.append(Token(PyTokenType.STRING, y1, x1, y, x))
            res.extend(escapes)
        elif text[pos: pos + 3] in py_symbols:
            y1, x1 = y, x
            next()
            next()
            next()
            res.append(Token(PyTokenType.SYMBOL, y1, x1, y, x))
        elif text[pos: pos + 2] in py_operators:
            y1, x1 = y, x
            next()
            next()
            res.append(Token(PyTokenType.OPERATOR, y1, x1, y, x))
        elif text[pos: pos] in py_operators:
            y1, x1 = y, x
            next()
            res.append(Token(PyTokenType.OPERATOR, y1, x1, y, x))
        elif text[pos] in py_symbols:
            y1, x1 = y, x
            next()
            res.append(Token(PyTokenType.SYMBOL, y1, x1, y, x))
        else:
            next()

    return res


class CodeArea(ScrolledText):
    def __init__(self, master=None):
        super().__init__(master)
        self.bind("<KeyRelease>", self.test_pyhighlight)

    def load(self, text: str):
        self.delete(0.0, tk.END)
        self.insert(0.0, text)
        self.test_pyhighlight()

    def cleartag(self):
        for i in py_colorscheme:
            self.tag_remove(i, 0.0, tk.END)

    def test_pyhighlight(self, _=None):
        self.cleartag()
        text = self.get(0.0, tk.END)
        tokens = py_tokenize(text)
        for token in tokens:
            if token.tp in py_tokentp_map:
                self.tag_add(py_tokentp_map[token.tp],
                             f"{token.y1}.{token.x1 - 1}", f"{token.y2}.{token.x2 - 1}")
        for k, v in py_colorscheme.items():
            self.tag_config(k, foreground=v)
        self.update()
        self.master.update()


class CodeEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("untitled - TestEd")
        self.save_path = "untitled"
        self.top_frame = tk.Frame(self)
        self.save_button = tk.Button(
            self.top_frame, text="Save", command=self.save)
        self.save_button.pack(side=tk.LEFT)
        self.save_as_button = tk.Button(
            self.top_frame, text="Save as", command=self.save_as)
        self.save_as_button.pack(side=tk.LEFT)
        self.open_button = tk.Button(
            self.top_frame, text="Open", command=self.open)
        self.open_button.pack(side=tk.LEFT)
        self.top_frame.pack(side=tk.TOP, fill=tk.BOTH)
        self.codearea = CodeArea(self)
        self.codearea.pack(fill=tk.BOTH)

    def retitle(self, title: str):
        self.title(title)
        self.update()

    def save(self):
        if self.save_path == "":
            self.save_path = asksaveasfilename()
        if self.save_path == "":
            return
        with open(self.save_path, "w", encoding="utf-8") as f:
            f.write(self.codearea.get(1.0, tk.END))
        self.retitle(self.save_path + " - TestEd")

    def save_as(self):
        self.save_path = ""
        self.save()

    def open(self):
        self.save_path = askopenfilename()
        if self.save_path == "":
            return
        with open(self.save_path, "r", encoding="utf-8") as f:
            self.codearea.load(f.read())
        self.retitle(self.save_path + " - TestEd")


root = CodeEditor()

root.mainloop()
