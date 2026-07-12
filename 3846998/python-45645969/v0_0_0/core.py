import re
from msvcrt import getwch as getch, kbhit
from time import time, sleep
import sys
import os
from copy import deepcopy
from pyperclip import copy, paste
import typing
import ctypes
import ConfigLang
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)


themes: dict[str, dict[str, str]] = {
    "default": {
        "unknown": "\033[1;0m",
        "number": "\033[1;33m",
        "keyword": "\033[1;35m",
        "string": "\033[32m",
        "comment": "\033[38;5;242m",
        "word": "\033[1;0m",
        "newline": "",
        "line-number": "\033[1;33m",
    }
}


def get_file_dir(filename: str):
    return filename[:filename.rfind("\\")]


def file_type_of(filename: str):
    return filename[filename.rfind('.')+1:]

def file_name_of(filename: str):
    return filename[:filename.rfind('.')]


class Char(typing.NamedTuple):
    type: str
    char: str


def gotoxy(y: int, x: int):
    print(f"\033[{y};{x}f", end="", flush=True)


def clear():
    os.system("cls")


def error():
    print("\a")


def default_tokenizer(text: str) -> list[list[Char]]:
    res: list[list[Char]] = [[]]
    for i in text:
        if i == '\n':
            res.append([])
        else:
            res[-1].append(Char("unknown", i))
    return res


def in_range(point: tuple[int, int], start: tuple[int, int], end: tuple[int, int]) -> bool:
    if start[0] > end[0] or start[0] == end[0] and start[1] > end[1]:
        start, end = end, start
    if point[0] < start[0] or point[0] > end[0]:
        return False
    if point[0] == start[0] and point[1] < start[1]:
        return False
    if point[0] == end[0] and point[1] > end[1]:
        return False
    return True


def generate_tokenizer(syntax: dict[str, str], keyword: list[str]):
    def tokenize(code: str) -> list[list[Char]]:
        regex = '|'.join('(?P<%s>%s)' % pair for pair in syntax.items())
        res: list[list[Char]] = [[]]
        for mo in re.finditer(regex, code):
            tp = mo.lastgroup
            value = mo.group()
            if tp == 'newline':
                res.append([])
            elif tp == 'word' and value in keyword:
                for i in value:
                    if i == '\n':
                        res.append([])
                    else:
                        res[-1].append(Char("keyword", i))
            else:
                for i in value:
                    if i == '\n':
                        res.append([])
                    else:
                        res[-1].append(Char(tp, i))
        return res

    return tokenize


def edit():
    def bind(mode: str, key: str, func):
        kb = key_bind[mode]
        while len(key) > 1:
            if key[0] not in kb:
                kb[key[0]] = {}
            kb = kb[key[0]]
            key = key[1:]
        kb[key] = func

    def get_text():
        return "\n".join(map(lambda a: "".join([i.char for i in a]), text))
    
    def cursor_up():
        nonlocal x, y
        if x > 0:
            x -= 1
            y = min(y_history, len(text[x]))
            if mode == 'Select':
                update_line(x)
                update_line(x + 1)

    def cursor_down():
        nonlocal x, y
        if x < len(text) - 1:
            if mode == 'Select':
                update_line(x)
                update_line(x + 1)
            x += 1
            y = min(y_history, len(text[x]))

    def cursor_left():
        nonlocal y, y_history
        if y > 0:
            if mode == 'Select':
                update_line(x)
            y_history = y = y - 1

    def cursor_right():
        nonlocal y, y_history
        if y < len(text[x]):
            if mode == 'Select':
                update_line(x)
            y_history = y = y + 1

    def cursor_PageUp():
        nonlocal x, y
        x = max(x - x_size, 0)
        y = min(y_history, len(text[x]))
        update_all()

    def cursor_PageDown():
        nonlocal x, y
        x = min(x + x_size, len(text) - 1)
        y = min(y_history, len(text[x]))
        update_all()

    def cursor_Home():
        nonlocal y, y_history
        y = y_history = 0
        if mode == 'Select':
            update_line(x)

    def cursor_End():
        nonlocal y, y_history
        y = y_history = len(text[x])
        if mode == 'Select':
            update_line(x)

    def insert(string: str):
        nonlocal x, y, y_history
        for i in string:
            if i == '\r':
                text.insert(x + 1, text[x][y:])
                text[x] = text[x][:y]
                x += 1
                y = y_history = 0
                update_all()
            elif i == '\n':
                ...
            elif i == '\t':
                for i in range(tab_size):
                    text[x].insert(y, Char("unknown", " "))
                    y = y_history = y + 1
                update_line(x)
            else:
                text[x].insert(y, Char("unknown", i))
                y = y_history = y + 1
                update_line(x)
        re_tokenize()
        not_saved()

    def delete():
        nonlocal x, y, y_history
        if y == 0:
            if x:
                x -= 1
                y = y_history = len(text[x])
                text[x] += text[x+1]
                del text[x+1]
                update_all()
        else:
            y = y_history = y - 1
            del text[x][y]
            update_line(x)
        re_tokenize()
        not_saved()

    def re_tokenize():
        nonlocal text
        text = tokenizer(get_text())

    def update_all():
        nonlocal need_update
        need_update = {i for i in range(x_start, x_size + x_start)}

    def update_line(line: int):
        need_update.add(line)

    def is_selected(i, j):
        '''if select_x < x:
            if select_x < i < x:
                return True
            elif select_x == i and j >= select_y:
                return True
            elif x == i and j < y:
                return True
            else:
                return False
        elif x < select_x:
            if x < i < select_x:
                return True
            elif x == i and j > y:
                return True
            elif select_x == i and j <= select_y:
                return True
            else:
                return False
        else:
            if select_y < y:
                return select_y <= j < y
            elif y < select_y:
                return y < j <= select_y
            else:
                return False'''
        return in_range((i, j), (x, y), (select_x, select_y))

    def clean_line(ln: int):
        gotoxy(ln, 1)
        if show_number:
            print(" " * (y_size + 5), end="", flush=True)
        else:
            print(" " * y_size, end="", flush=True)

    def refresh_screen():
        for i in need_update:
            if x_start <= i < x_start + x_size:
                clean_line(i - x_start + 1)
                if i < len(text):
                    gotoxy(i - x_start + 1, 1)
                    if show_number:
                        print(theme["line-number"] + "%4d " % (i + 1), end="\033[1;0m")
                    for j in range(y_start, min(y_start + y_size, len(text[i]))):
                        if mode == 'Select' and is_selected(i, j):
                            print(theme[text[i][j].type] + "\033[1;44m" + text[i][j].char, end="\033[1;0m")
                        else:
                            print(theme[text[i][j].type] + text[i][j].char, end="")
                    print("\033[1;0m", end="", flush=True)
        gotoxy(x_size + 1, 1)
        print(mode, end="")
        if show_number:
            gotoxy(x - x_start + 1, y - y_start + 6)
        else:
            gotoxy(x - x_start + 1, y - y_start + 1)

    def exit_editor(a=""):
        nonlocal need_exit
        need_exit = True

    def mode_insert():
        nonlocal mode
        mode = 'Insert'

    def mode_normal():
        nonlocal mode
        if mode == 'Select':
            update_all()
        mode = 'Normal'

    def mode_select():
        nonlocal mode, select_x, select_y
        mode = 'Select'
        select_x = x
        select_y = y

    def run_cmd(cmd: str):
        while cmd and cmd[0] in ' \t':
            cmd = cmd[1:]
        if cmd == "":
            return
        if ' ' in cmd:
            cmd_name = cmd[:cmd.find(' ')]
            cmd_body = cmd[cmd.find(' ')+1:]
            if cmd_name in command:
                command[cmd_name](cmd_body)
                return
        else:
            cmd_name = cmd
            if cmd_name in command:
                command[cmd_name]("")
                return
        message(f"\033[1;31mUnknown command '{cmd_name}'!\033[1;0m")

    def new_cmd(name: str, func):
        command[name] = func
        return func

    def read_sth(msg: str):
        clean_line(x_size + 1)
        gotoxy(x_size + 1, 1)
        v = input(msg)
        clean_line(x_size + 1)
        return v
    
    def message(msg: str):
        clean_line(x_size + 2)
        gotoxy(x_size + 2, 1)
        print(msg, end="", flush=True)

    def select_delete():
        nonlocal select_y, y, select_x, x, text
        if select_x > x or select_x == x and select_y > y:
            x, y, select_x, select_y = select_x, select_y, x, y
        if x == select_x:
            del text[x][select_y: y+1]
        else:
            del text[x][:y+1]
            del text[select_x][select_y:]
            del text[select_x+1: x]
            text[select_x] += text[select_x+1]
            del text[select_x+1]
        x, y = select_x, select_y
        mode_normal()
        update_all()
        not_saved()

    def delete_after_cursor():
        if y < len(text[x]):
            del text[x][y]
            update_line(x)
            not_saved()

    def show_number_on():
        nonlocal show_number, y_size
        if not show_number:
            show_number = True
            y_size -= 5

    def show_number_off():
        nonlocal show_number, y_size
        if show_number:
            show_number = False
            y_size += 5

    def get_selected_text():
        if x == select_x:
            if y < select_y:
                return "".join(map(lambda a: a.char, text[x][y: select_y+1]))
            return "".join(map(lambda a: a.char, text[x][select_y: y+1]))
        elif x < select_x:
            res = "".join(map(lambda a: a.char, text[x][y:])) + '\n'
            # res += "\n".join(map("".join, text[x+1: select_x+1])) + '\n'
            for i in text[x+1: select_x]:
                res += "".join(map(lambda a: a.char, i)) + '\n'
            res += "".join(map(lambda a: a.char, text[select_x][:select_y]))
            return res
        else:
            res = "".join(map(lambda a: a.char, text[select_x][select_y:])) + '\n'
            # res += "\n".join(map("".join, text[select_x+1: x])) + '\n'
            for i in text[select_x+1: x]:
                res += "".join(map(lambda a: a.char, i)) + '\n'
            res += "".join(map(lambda a: a.char, text[x][:y]))
            return res
        
    def select_yank():
        copy(get_selected_text())

    def put_after_cursor():
        cursor_right()
        insert(paste())

    def put_before_cursor():
        insert(paste())

    def select_cut():
        copy(get_selected_text())
        select_delete()
        mode_insert()

    def set_tokenizer(func):
        nonlocal tokenizer
        tokenizer = func
        re_tokenize()

    def new_theme(name: str, theme: dict[str, str]):
        themes[name] = theme

    def set_theme(name: str):
        if name in themes:
            theme = themes[name]
            update_all()

    def save(input_path=""):
        nonlocal save_path, saved
        saved = True
        if input_path:
            save_path = input_path
        if save_path == "":
            save_path = read_sth("Save path: ")
        open(save_path, "w", encoding='utf-8').write(get_text())
        re_tokenize()
        update_all()
        load_extension_for_now()

    def load_string(string: str):
        nonlocal text
        text = [[]]
        for ch in string:
            if ch == '\n':
                text.append([])
            elif ch == '\r':
                ...
            else:
                text[-1].append(Char("unknown", ch))
        re_tokenize()
        update_all()
        not_saved()
        load_extension_for_now()

    def open_file(input_path):
        nonlocal save_path, saved
        if input_path:
            save_path = input_path
            load_string(open(save_path, 'r', encoding='utf-8').read())
            saved = True

    def test_saved():
        if not saved:
            message("\033[1;31mFile is not saved!\033[1;0m")

    def not_saved():
        nonlocal saved
        saved = False

    def reset():
        nonlocal key_bind
        key_bind = basic_key_bind
        set_tokenizer(default_tokenizer())

    def load_extension(lang: str):
        if lang in extension:
            for ext in extension[lang]:
                ext()

    def load_extension_for_now():
        load_extension('*')
        load_extension(file_type_of(save_path))

    def new_extension(lang: str, func):
        if lang not in extension:
            extension[lang] = []
        extension[lang].append(func)

    def get_char_at(x: int, y: int):
        return text[x][y].char

    x = 0
    y = 0
    select_x = 0
    select_y = 0
    x_start = 0
    y_start = 0
    x_size = os.get_terminal_size().lines - 2
    y_size = os.get_terminal_size().columns
    tab_size = 4
    text: list[list[Char]] = [[]]
    y_history = 0
    theme = themes["default"]
    basic_key_bind = {
        'Normal': {
            '\xe0': {
                'H': cursor_up,
                'P': cursor_down,
                'K': cursor_left,
                'M': cursor_right,
                'G': cursor_Home,
                'O': cursor_End,
                'I': cursor_PageUp,
                'Q': cursor_PageDown,
            },
            '\x03': exit_editor,
            'h': cursor_left,
            'j': cursor_down,
            'k': cursor_up,
            'l': cursor_right,
            'v': mode_select,
            'i': mode_insert,
            'x': delete_after_cursor,
            'p': put_after_cursor,
            'P': put_before_cursor,
            ':': lambda: run_cmd(read_sth(':')),
        },
        'Insert': {
            '\xe0': {
                'H': cursor_up,
                'P': cursor_down,
                'K': cursor_left,
                'M': cursor_right,
                'G': cursor_Home,
                'O': cursor_End,
                'I': cursor_PageUp,
                'Q': cursor_PageDown,
            },
            '\x08': delete,
            '\x1b': mode_normal,
            '\x03': mode_normal,
        },
        'Select': {
            '\xe0': {
                'H': cursor_up,
                'P': cursor_down,
                'K': cursor_left,
                'M': cursor_right,
                'G': cursor_Home,
                'O': cursor_End,
                'I': cursor_PageUp,
                'Q': cursor_PageDown,
            },
            'h': cursor_left,
            'j': cursor_down,
            'k': cursor_up,
            'l': cursor_right,
            'd': select_delete,
            'y': select_yank,
            'c': select_cut,
            '\x1b': mode_normal,
            '\x03': mode_normal,
        },
    }
    need_exit = False
    key_bind = deepcopy(basic_key_bind)
    command = {}
    tokenizer = default_tokenizer
    need_update: set[int] = set()
    mode = 'Normal'
    show_number = False
    save_path = ""
    saved = True
    extension: dict[str, list] = {
        '*': [],
    }
    ConfigLang.scope.define('editor', {
        'getch': getch,
        'kbhit': kbhit,
        'gotoxy': gotoxy,
        'cursor_up': cursor_up,
        'cursor_down': cursor_down,
        'cursor_right': cursor_right,
        'cursor_left': cursor_left,
        'cursor_Home': cursor_Home,
        'cursor_End': cursor_End,
        'cursor_PageUp': cursor_PageUp,
        'cursor_PageDown': cursor_PageDown,
        'bind': bind,
        'key_bind': lambda: key_bind,
        'basic_key_bind': lambda: basic_key_bind,
        'default_tokenizer': lambda: default_tokenizer,
        'set_tokenizer': set_tokenizer,
        'tokenizer': lambda: tokenizer,
        'get_text': get_text,
        'insert': insert,
        'text': lambda: text,
        'show_number_on': show_number_on,
        'show_number_off': show_number_off,
        're_tokenize': re_tokenize,
        'new_theme': new_theme,
        'set_theme': set_theme,
        'update_line': update_line,
        'update_all': update_all,
        'refresh_screen': refresh_screen,
        'delete': delete,
        'delete_after_cursor': delete_after_cursor,
        'is_selected': is_selected,
        'select_delete': select_delete,
        'mode_select': mode_select,
        'mode_insert': mode_insert,
        'mode_normal': mode_normal,
        'run_cmd': run_cmd,
        'read_sth': read_sth,
        'get_selected_text': get_selected_text,
        'select_yank': select_yank,
        'put_after_cursor': put_after_cursor,
        'put_before_cursor': put_before_cursor,
        'select_cut': select_cut,
        'copy': copy,
        'paste': paste,
        'newChar': Char,
        'char_char': lambda a: a.char,
        'char_type': lambda a: a.type,
        'file_type_of': file_type_of,
        'get_file_dir': get_file_dir,
        'file_name_of': file_name_of,
        'open_file': open_file,
        'load_string': load_string,
        'save': save,
        'x': lambda: x,
        'y': lambda: y,
        'message': message,
        'command': lambda: command,
        'new_cmd': new_cmd,
        'test_saved': test_saved,
        'extension': lambda: extension,
        'load_extension': load_extension,
        'new_extension': new_extension,
        'generate_tokenizer': generate_tokenizer,
        'get_char_at': get_char_at,
        'tab_size': lambda: tab_size,
    })
    show_number_on()
    update_all()

    new_cmd('w', save)
    new_cmd('o', open_file)
    new_cmd('q', exit_editor)
    new_cmd('show-nu-on', show_number_on)
    new_cmd('show-nu-off', show_number_off)

    ConfigLang.run_code(open(get_file_dir(__file__) + "/config.cfgl", 'r', encoding='utf-8').read(), ConfigLang.scope)
    while not need_exit:
        if x >= x_start + x_size - 1:
            x_start = x - x_size + 1
            update_all()
        elif x < x_start:
            x_start = x
            update_all()
        if y >= y_start + y_size - 1:
            y_start = y - y_size + 1
            update_all()
        elif y < y_start:
            y_start = y
            update_all()
        refresh_screen()
        need_update = set()
        key = getch()
        if key in key_bind[mode]:
            func = key_bind[mode][key]
            while isinstance(func, dict):
                key = getch()
                if key not in func:
                    break
                func = func[key]
            if callable(func):
                func()
        elif mode == 'Insert':
            insert(key)


clear()
edit()
