from msvcrt import getwch as getch, kbhit
from os import (system, get_terminal_size as get_termsize,
                getcwd, chdir,
                name as osname)
from edcmd import EdCmd, read_cmd
from typing import Literal
import copy
from pyperclip import copy, paste


class Line:
    def __init__(self, is_end: bool, width: int, text: list[str]):
        self.is_end, self.width, self.text = is_end, width, text

    def __str__(self): return f"Line({self.is_end}, {self.width}, {self.text})"

    def __repr__(self): return str(self)


widths = [
    (126, 1), (159, 0), (687, 1), (710, 0), (711, 1),
    (727, 0), (733, 1), (879, 0), (1154, 1), (1161, 0),
    (4347, 1), (4447, 2), (7467, 1), (7521, 0), (8369, 1),
    (8426, 0), (9000, 1), (9002, 2), (11021, 1), (12350, 2),
    (12351, 1), (12438, 2), (12442, 0), (19893, 2), (19967, 1),
    (55203, 2), (63743, 1), (64106, 2), (65039, 1), (65059, 0),
    (65131, 2), (65279, 1), (65376, 2), (65500, 1), (65510, 2),
    (120831, 1), (262141, 2), (1114109, 1),
]


def get_width(o):  # 参考了https://wenku.baidu.com/view/da48663551d380eb6294dd88d0d233d4b14e3f18.html?fr=sogou&_wkts_=1687573107734
    """Return the screen column width for unicode ordinal o."""
    global widths
    o = ord(o)
    if o == 0xe or o == 0xf:
        return 0
    if o == 0x9:
        return 8
    for num, wid in widths:
        if o <= num:
            return wid
    return 1


def get_term_width():
    return get_termsize().columns


def get_term_height():
    return get_termsize().lines


def get_str_width(s: list[str]):
    res = 0
    for i in s:
        res += get_width(i)
    return res


def get_pos(s: list[str]) -> tuple[int, int]:
    y, x = 0, 0
    cw = 0
    tw = get_term_width()
    for i in s:
        w = get_width(i)
        if cw + w > tw:
            y += 1
            cw = w
            x = 1
        else:
            cw += w
            x += 1
    return y, x


def clear_screen():
    """清屏"""
    system("cls")


def gotoxy(y: int, x: int):
    """
    主动移动光标
    y: ln, x: col
    """
    print(f"\033[{y};{x}f", end="", flush=True)


def clean_line(real: int):
    gotoxy(real, 1)
    print(" " * get_term_width(), end="", flush=True)
    gotoxy(real, 1)


def rangecmp_2D(p1: tuple[int, int], p2: tuple[int, int]):
    if p1[0] < p2[0]:
        return -1
    elif p1[0] > p2[0]:
        return 1
    elif p1[1] < p2[1]:
        return -1
    elif p1[1] > p2[1]:
        return 1
    else:
        return 0


def inrange_2D(pos: tuple[int, int], begin: tuple[int, int], end: tuple[int, int]):
    if rangecmp_2D(begin, end) > 0:
        begin, end = end, begin
    # begin <= pos <= end
    return rangecmp_2D(begin, pos) <= 0 and rangecmp_2D(pos, end) <= 0


def edit():
    def insert_text(y: int, x: int, text: list[str]) -> tuple[int, int]:
        """ 可以多字符，但不能插入换行 """
        need_update.add(y)
        code[y].width += get_str_width(text)
        w = code[y].width
        code[y].text = code[y].text[:x] + text + code[y].text[x:]
        nxt_str = []
        while code[y].width > term_width:
            nxt_str = [code[y].text.pop()] + nxt_str
            code[y].width -= get_width(nxt_str[0])
        if nxt_str:
            if y < len(code) - 1 and not code[y].is_end:
                insert_text(y + 1, 0, nxt_str)
            else:
                code[y].is_end = False
                code.insert(y + 1, Line(True, 0, []))
                insert_text(y + 1, 0, nxt_str)
        py, px = get_pos(code[y].text[:x] + text)
        return y + py, px

    def fill_blank(y: int):
        """ 相当于反向的insert """
        # show_text()
        need_update.add(y)
        if y < len(code) - 1 and not code[y].is_end:
            while len(code[y + 1].text):
                cur = code[y + 1].text[0]
                width = get_width(cur)
                if code[y].width + width <= term_width:
                    code[y + 1].text = code[y + 1].text[1:]
                    code[y + 1].width -= width
                    code[y].width += width
                    code[y].text.append(cur)
                else:
                    break
            if len(code[y + 1].text):
                fill_blank(y + 1)

    def insert_enter(y: int, x: int) -> tuple[int, int]:
        need_update.add(y)
        text = code[y].text[:x]
        code.insert(y, Line(True, get_str_width(text), text))
        y += 1
        code[y].text = code[y].text[x:]
        code[y].width = get_str_width(code[y].text)
        fill_blank(y)
        return y, 0

    def insert(ch: str):
        nonlocal ln, col, ideal_x
        if ch in '\n\r':
            ln, col = insert_enter(ln, col)
        else:
            ln, col = insert_text(ln, col, [ch])
        ideal_x = col

    def insert_any(text: str):
        nonlocal ln, col, ideal_x
        if osname == "nt":
            text = text.replace('\r\n', '\n')
        s = text.split('\n')
        for i in s[:-1]:
            ln, col = insert_text(ln, col, list(i))
            ln, col = insert_enter(ln, col)
        if s:
            ln, col = insert_text(ln, col, list(s[-1]))
        ideal_x = col

    def nor_put_p():
        nonlocal col
        if code[ln].text:
            col += 1
        text = paste()
        insert_any(text)
        if col >= len(code[ln].text):
            col -= 1
        if col < 0:
            col = 0

    def nor_put_P():
        nonlocal col
        text = paste()
        insert_any(text)
        if col >= len(code[ln].text):
            col -= 1
        if col < 0:
            col = 0

    def vis_yank_y():
        copy(get_visual())

    def quit_editor():
        nonlocal need_quit
        need_quit = True

    def update():
        nonlocal need_update
        for i in need_update:
            if scr_y <= i < scr_y + term_height:
                clean_line(i - scr_y + 1)
                if 0 <= i < len(code):
                    if mode == 'Visual':
                        for j in range(len(code[i].text)):
                            if inrange_2D((i, j), (ln, col), (v_ln, v_col)):
                                print(
                                    "\033[1;47m" + code[i].text[j] + "\033[1;0m", end="")
                            else:
                                print(code[i].text[j], end="")
                        print(end="", flush=True)
                    else:
                        print("".join(code[i].text), end="", flush=True)
        need_update = set()
        clean_line(term_height + 1)
        if mode == 'Visual':
            print(
                f"{mode}  ln: {ln}, col: {col}, v_ln: {v_ln}, v_col: {v_col}", end="", flush=True)
        else:
            print(f"{mode}  ln: {ln}, col: {col}", end="", flush=True)

    def show_cursor():
        gotoxy(ln - scr_y + 1, get_str_width(code[ln].text[:col]) + 1)

    def update_all():
        nonlocal need_update
        need_update = {i for i in range(scr_y, scr_y + term_height)}

    def scroll():
        nonlocal ln, scr_y
        if ln < scr_y:
            scr_y = ln
            update_all()
        if ln >= scr_y + term_height - 1:
            scr_y = ln - term_height + 1
            update_all()

    def ins2nor():
        nonlocal mode
        mode = "Normal"
        # Vim式的Normal Mode移动
        if col:
            move_cursor('left')

    def nor2ins_i():
        nonlocal mode
        mode = "Insert"

    def nor2ins_a():
        nonlocal mode
        mode = "Insert"
        move_cursor('right')

    def backspace():
        nonlocal ln, col, ideal_x
        if col > 0:
            col -= 1
            ideal_x = col
            code[ln].width -= get_width(code[ln].text[col])
            del code[ln].text[col]
            fill_blank(ln)
        elif ln > 0:
            ln -= 1
            col = len(code[ln].text)
            if not code[ln].is_end:
                backspace()
                fill_blank(ln)
            else:
                code[ln].is_end = False
                # show_text()
                insert_text(ln, col, code[ln + 1].text)
                del code[ln + 1]
                update_all()

    def del_visual():
        nonlocal ln, col, v_ln, v_col, mode
        # 当前光标在前
        if rangecmp_2D((ln, col), (v_ln, v_col)) > 0:
            (ln, col), (v_ln, v_col) = (v_ln, v_col), (ln, col)
        if ln == v_ln:
            code[ln].width -= get_str_width(code[ln].text[col: v_col + 1])
            del code[ln].text[col: v_col + 1]
        else:
            code[ln].width -= get_str_width(code[ln].text[col:])
            del code[ln].text[col:]
            code[v_ln].width -= get_str_width(code[v_ln].text[:v_col + 1])
            del code[v_ln].text[:v_col + 1]
            code[ln].text += code[v_ln].text
            # code[v_ln].lnnum.val = code[ln].lnnum.val
            if code[ln + 1: v_ln + 1]:
                code[ln].is_end = False
                del code[ln + 1: v_ln + 1]
        fill_blank(ln)
        vis2nor()
        if col >= len(code[ln].text):
            col -= 1
        if col < 0:
            col = 0

    def get_visual():
        begin, end = (ln, col), (v_ln, v_col)
        if rangecmp_2D(begin, end) > 0:
            begin, end = end, begin
        if begin[0] == end[0]:
            return "".join(code[begin[0]].text[begin[1]: end[1] + 1])
        res = ''.join(code[begin[0]].text[begin[1]:])
        for i in range(begin[0] + 1, end[0]):
            if code[i - 1].is_end:
                res += '\n'
            res += ''.join(code[i].text)
        if code[end[0] - 1].is_end:
            res += '\n'
        res += ''.join(code[end[0]].text[:end[1] + 1])
        return res

    def show_visual():
        """ Debug功能 """
        clear_screen()
        print(get_visual())
        input()
        update_all()

    def move_cursor(d: str):
        nonlocal ln, col, ideal_x
        if d == 'up':
            if ln > 0:
                need_update.add(ln)
                ln -= 1
                need_update.add(ln)
                col = min(ideal_x, len(code[ln].text))
        elif d == 'down':
            if ln < len(code) - 1:
                need_update.add(ln)
                ln += 1
                need_update.add(ln)
                col = min(ideal_x, len(code[ln].text))
        elif d == 'left':
            if col > 0:
                if mode == 'Visual':
                    need_update.add(ln)
                col = ideal_x = col - 1
        elif d == 'right':
            if col < len(code[ln].text):
                if mode == 'Visual':
                    need_update.add(ln)
                col = ideal_x = col + 1
        elif d == 'head':
            if mode == 'Visual':
                need_update.add(ln)
            col = ideal_x = 0
        elif d == 'home':
            if mode == 'Visual':
                need_update.add(ln)
            col = 0
            while col < len(code[ln].text) and code[ln].text[col].isspace():
                col += 1
        elif d == 'end':
            if mode == 'Visual':
                need_update.add(ln)
            col = ideal_x = len(code[ln].text)
        elif d == 'pageup':
            ln -= term_height
            if ln < 0:
                ln = 0
            scroll()
        elif d == 'pagedown':
            ln += term_height
            if ln >= len(code):
                ln = len(code) - 1
            scroll()
        if mode == 'Normal' and col >= len(code[ln].text):
            col = len(code[ln].text) - 1
        if col < 0:
            col = 0

    def show_text():
        """ Debug功能 """
        clear_screen()
        print(code)
        input()
        clear_screen()
        update_all()

    def nor2vis():
        nonlocal v_ln, v_col, mode
        mode = 'Visual'
        v_ln, v_col = ln, col

    def vis2nor():
        nonlocal mode
        mode = 'Normal'
        if col >= len(code[ln].text):
            move_cursor('left')
        update_all()

    def ask_sth(s: str):
        clean_line(term_height + 2)
        try:
            res = input(s)
            show_cursor()
            return res
        except:
            return ""

    def echo(s: str):
        clean_line(term_height + 2)
        print(s, end="", flush=True)
        show_cursor()

    def write_file(path: str | None = None):
        nonlocal save_path
        if path is not None:
            save_path = path
        if save_path is None:
            while not save_path:
                save_path = ask_sth("Save path> ")
        try:
            with open(save_path, 'w', encoding='utf-8') as f:
                f.write("\n".join(map(lambda a: "".join(a.text), code)))
            echo(f"{save_path} written.")
        except:
            echo("Failed to write.")

    def open_file(path: str | None = None):
        nonlocal save_path, ln, col, code
        if path is not None:
            save_path = path
        if save_path is None:
            while not save_path:
                save_path = ask_sth("Save path> ")
        try:
            with open(save_path, 'r', encoding='utf-8') as f:
                text = f.read()
                ln, col = 0, 0
                code = [Line(True, 0, [])]
                if osname == "nt":
                    text = text.replace('\n\r', '\n')
                insert_any(text)
        except:
            echo("Failed to open.")

    def run_cmd():
        cmd = ask_sth(":")
        try:
            w = read_cmd(cmd)
            if w is None:
                return
            res = w.run(cmdmap)
            if res is not None:
                echo(res)
        except Exception as e:
            echo(f"Failed to run '{cmd}': {e}.")

    def go_line_G():
        nonlocal ln, col
        try:
            ln = min(int(ask_sth('G')), len(code) - 1)
            if mode == 'Insert':
                col = min(len(code[ln].text), ideal_x)
            else:
                col = min(len(code[ln].text) - 1, ideal_x)
        except:
            pass

    term_width = get_term_width()  # 这个不能变
    term_height = get_term_height() - 3
    ln, col = 0, 0
    v_ln, v_col = 0, 0
    # 选择区域和Vim一样，是闭区间
    ideal_x = 0
    scr_y = 0
    code: list[Line] = [Line(True, 0, [])]
    need_update: set[int] = set()
    need_quit = False
    mode = "Normal"
    save_path = None
    cmdmap = {
        'w': write_file,
        'o': open_file,
        'q': lambda *_: quit_editor(),
    }
    keys = {
        "Normal": {
            ':': run_cmd,
            # '\x03': quit_editor,
            'i': nor2ins_i,
            'a': nor2ins_a,
            'v': nor2vis,
            'p': nor_put_p,
            'P': nor_put_P,
            # 't': show_text,
            'h': lambda: move_cursor('left'),
            'j': lambda: move_cursor('down'),
            'k': lambda: move_cursor('up'),
            'l': lambda: move_cursor('right'),
            '0': lambda: move_cursor('head'),
            '^': lambda: move_cursor('home'),
            '$': lambda: move_cursor('end'),
            '\x15': lambda: move_cursor('pageup'),  # C-u
            '\x04': lambda: move_cursor('pagedown'),  # C-d
            'G': go_line_G,
            '\xe0': {
                '\x4b': lambda: move_cursor('left'),
                '\x50': lambda: move_cursor('down'),
                '\x48': lambda: move_cursor('up'),
                '\x4d': lambda: move_cursor('right'),
                '\x49': lambda: move_cursor('pageup'),
                '\x51': lambda: move_cursor('pagedown'),
                '\x47': lambda: move_cursor('home'),
                '\x4f': lambda: move_cursor('end'),
            },
            '\x00': {
                '\x4b': lambda: move_cursor('left'),
                '\x50': lambda: move_cursor('down'),
                '\x48': lambda: move_cursor('up'),
                '\x4d': lambda: move_cursor('right'),
                '\x49': lambda: move_cursor('pageup'),
                '\x51': lambda: move_cursor('pagedown'),
                '\x47': lambda: move_cursor('home'),
                '\x4f': lambda: move_cursor('end'),
            },
        },
        "Insert": {
            '\x1b': ins2nor,
            '\x03': ins2nor,
            '\x08': backspace,
            '\xe0': {
                '\x4b': lambda: move_cursor('left'),
                '\x50': lambda: move_cursor('down'),
                '\x48': lambda: move_cursor('up'),
                '\x4d': lambda: move_cursor('right'),
                '\x49': lambda: move_cursor('pageup'),
                '\x51': lambda: move_cursor('pagedown'),
                '\x47': lambda: move_cursor('home'),
                '\x4f': lambda: move_cursor('end'),
            },
            '\x00': {
                '\x4b': lambda: move_cursor('left'),
                '\x50': lambda: move_cursor('down'),
                '\x48': lambda: move_cursor('up'),
                '\x4d': lambda: move_cursor('right'),
                '\x49': lambda: move_cursor('pageup'),
                '\x51': lambda: move_cursor('pagedown'),
                '\x47': lambda: move_cursor('home'),
                '\x4f': lambda: move_cursor('end'),
            },
        },
        "Visual": {
            '\x1b': vis2nor,
            '\x03': vis2nor,
            'd': del_visual,
            'y': vis_yank_y,
            # 't': show_visual,
            'h': lambda: move_cursor('left'),
            'j': lambda: move_cursor('down'),
            'k': lambda: move_cursor('up'),
            'l': lambda: move_cursor('right'),
            '0': lambda: move_cursor('head'),
            '^': lambda: move_cursor('home'),
            '$': lambda: move_cursor('end'),
            '\x15': lambda: move_cursor('pageup'),  # C-u
            '\x04': lambda: move_cursor('pagedown'),  # C-d
            'G': go_line_G,
            '\xe0': {
                '\x4b': lambda: move_cursor('left'),
                '\x50': lambda: move_cursor('down'),
                '\x48': lambda: move_cursor('up'),
                '\x4d': lambda: move_cursor('right'),
                '\x49': lambda: move_cursor('pageup'),
                '\x51': lambda: move_cursor('pagedown'),
                '\x47': lambda: move_cursor('home'),
                '\x4f': lambda: move_cursor('end'),
            },
            '\x00': {
                '\x4b': lambda: move_cursor('left'),
                '\x50': lambda: move_cursor('down'),
                '\x48': lambda: move_cursor('up'),
                '\x4d': lambda: move_cursor('right'),
                '\x49': lambda: move_cursor('pageup'),
                '\x51': lambda: move_cursor('pagedown'),
                '\x47': lambda: move_cursor('home'),
                '\x4f': lambda: move_cursor('end'),
            },
        },
    }

    while not need_quit:
        scroll()
        update()
        show_cursor()

        key = getch()
        if key in keys[mode]:
            fn = keys[mode][key]
            while isinstance(fn, dict):
                key = getch()
                if key in fn:
                    fn = fn[key]
                else:
                    break
            if callable(fn):
                fn()
        elif mode == 'Insert':
            insert(key)


clear_screen()
edit()
