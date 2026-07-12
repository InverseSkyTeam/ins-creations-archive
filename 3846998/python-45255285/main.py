LINE_SIZE = 20000000  # 自动换行被我吃了
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


def getch():
    import sys, termios, tty
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def gotoxy(y: int, x: int):  # y: ln, x: col
    print(f"\033[{y};{x}f", end="", flush=True)


def clear():
    print("\033c", end="")


def nth2pos(line: str, n: int) -> tuple:
    now_ln, now_col = 0, 0
    for i in line[:n]:
        if now_col + get_width(i) <= LINE_SIZE:
            now_col += get_width(i)
        else:
            now_ln += 1
            now_col = get_width(i)
    return now_ln, now_col


def edit_line():
    line = []
    n = 0
    while 1:
        clear()
        print("".join(line))
        pos = nth2pos(line, n)
        gotoxy(pos[0] + 1, pos[1] + 1)
        key = getch()
        if key == '\r':  # Enter: confirm
            clear()
            return "".join(line)
        elif key == '\x7f':  # Backspace: delete
            if n > 0:
                n -= 1
                del line[n]
        elif key == '\x03':  # C-c: quit
            return None
        elif key == '\x1b':  # Esc: quit
            return None
        elif key == '\x07':  # C-g: left
            if n > 0:
                n -= 1
        elif key == '\x08':  # C-h: right
            if n < len(line):
                n += 1
        else:
            line.insert(n, key)
            n += 1
    clear()
    return "".join(line)


print('''LineEditor
可能主要用途是在社区当input用
最大的优点是支持左右移动光标''')
getch()
clear()
print(edit_line())
#print(ord(getch()))
#print(ord(getch()))
#print(ord(getch()))


# import os
# import sys
# import msvcrt
# LINE_SIZE = os.get_terminal_size().columns
# widths = [
# (126, 1), (159, 0), (687, 1), (710, 0), (711, 1),
# (727, 0), (733, 1), (879, 0), (1154, 1), (1161, 0),
# (4347, 1), (4447, 2), (7467, 1), (7521, 0), (8369, 1),
# (8426, 0), (9000, 1), (9002, 2), (11021, 1), (12350, 2),
# (12351, 1), (12438, 2), (12442, 0), (19893, 2), (19967, 1),
# (55203, 2), (63743, 1), (64106, 2), (65039, 1), (65059, 0),
# (65131, 2), (65279, 1), (65376, 2), (65500, 1), (65510, 2),
# (120831, 1), (262141, 2), (1114109, 1),
# ]


# def get_width(o):  # 参考了https://wenku.baidu.com/view/da48663551d380eb6294dd88d0d233d4b14e3f18.html?fr=sogou&_wkts_=1687573107734
#     """Return the screen column width for unicode ordinal o."""
#     global widths
#     o = ord(o)
#     if o == 0xe or o == 0xf:
#         return 0
#     if o == 0x9:
#         return 8
#     for num, wid in widths:
#         if o <= num:
#             return wid
#     return 1


# def getch():
#     return msvcrt.getwch()


# def gotoxy(y: int, x: int):  # y: ln, x: col
#     print(f"\033[{y};{x}f", end="", flush=True)


# def clear():
#     os.system("cls")


# def nth2pos(line: str, n: int) -> tuple[int, int]:
#     now_ln, now_col = 0, 0
#     for i in line[:n]:
#         if now_col + get_width(i) <= LINE_SIZE:
#             now_col += get_width(i)
#         else:
#             now_ln += 1
#             now_col = get_width(i)
#     return now_ln, now_col


# def edit_line() -> str | None:
#     line = []
#     n = 0
#     while 1:
#         clear()
#         print("".join(line))
#         pos = nth2pos(line, n)
#         gotoxy(pos[0] + 1, pos[1] + 1)
#         key = getch()
#         if key == '\r':
#             clear()
#             return "".join(line)
#         elif key == '\x08':
#             if n > 0:
#                 n -= 1
#                 del line[n]
#         elif key == '\x03' or key == '\x1b':
#             return None
#         elif key == '\xe0':
#             key = getch()
#             if key == 'K':
#                 if n > 0:
#                     n -= 1
#             if key == 'M':
#                 if n < len(line):
#                     n += 1
#         else:
#             line.insert(n, key)
#             n += 1
#     clear()
#     return "".join(line)


# clear()
# print(edit_line())
