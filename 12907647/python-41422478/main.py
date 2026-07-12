print('需要用到pynput三方库')
from pynput import (keyboard,mouse)

# 打表法
# help(keyboard.Key)
# for i in range(97,123):
#     print("    \"\'"+chr(i)+"\'\": \""+chr(i)+"\",")
# for i in range(1,25):
#     print("    \"Key.f"+str(i)+"\": \"f"+str(i)+"\",")

keydic = {
    "'0'": "0",
    "'1'": "1",
    "'2'": "2",
    "'3'": "3",
    "'4'": "4",
    "'5'": "5",
    "'6'": "6",
    "'7'": "7",
    "'8'": "8",
    "'9'": "9",
    "<96>": "0",
    "<97>": "1",
    "<98>": "2",
    "<99>": "3",
    "<100>": "4",
    "<101>": "5",
    "<102>": "6",
    "<103>": "7",
    "<104>": "8",
    "<105>": "9",
    "<110>": ".",
    "'+'": "'+'",
    "'-'": "'-'",
    "'*'": "'*'",
    "'/'": "'/'",
    "'='": "'='",
    
    "'a'": "a",
    "'b'": "b",
    "'c'": "c",
    "'d'": "d",
    "'e'": "e",
    "'f'": "f",
    "'g'": "g",
    "'h'": "h",
    "'i'": "i",
    "'j'": "j",
    "'k'": "k",
    "'l'": "l",
    "'m'": "m",
    "'n'": "n",
    "'o'": "o",
    "'p'": "p",
    "'q'": "q",
    "'r'": "r",
    "'s'": "s",
    "'t'": "t",
    "'u'": "u",
    "'v'": "v",
    "'w'": "w",
    "'x'": "x",
    "'y'": "y",
    "'z'": "z",
    "'\\x01'": "a",
    "'\\x02'": "b",
    "'\\x03'": "c",
    "'\\x04'": "d",
    "'\\x05'": "e",
    "'\\x06'": "f",
    "'\\x07'": "g",
    "'\\x08'": "h",
    "'\\x09'": "i",
    "'\\x0a'": "j",
    "'\\x0b'": "k",
    "'\\x0c'": "l",
    "'\\x0d'": "m",
    "'\\x0e'": "n",
    "'\\x0f'": "o",
    "'\\x10'": "p",
    "'\\x11'": "q",
    "'\\x12'": "r",
    "'\\x13'": "s",
    "'\\x14'": "t",
    "'\\x15'": "u",
    "'\\x16'": "v",
    "'\\x17'": "w",
    "'\\x18'": "x",
    "'\\x19'": "y",
    "'\\x1a'": "z",
    
    "':'": ":",
    "';'": ";",
    "'<'": "<",
    "'>'": ">",
    "','": ",",
    "'.'": ".",
    "'?'": "?",
    "'!'": "!",
    "'~'": "~",
    "'`'": "`",
    "'@'": "@",
    "'#'": "#",
    "'$'": "$",
    "'%'": "%",
    "'^'": "^",
    "'&'": "&",
    "'('": "(",
    "')'": ")",
    "'_'": "_",
    "'|'": "|",
    "'\\'": "\\",
    "'['": "[",
    "']'": "]",
    "'{'": "{",
    "'}'": "}",
    '"\'"': "'",
    '\'"\'': "\"",
    
    "Key.f1": "f1",
    "Key.f2": "f2",
    "Key.f3": "f3",
    "Key.f4": "f4",
    "Key.f5": "f5",
    "Key.f6": "f6",
    "Key.f7": "f7",
    "Key.f8": "f8",
    "Key.f9": "f9",
    "Key.f10": "f10",
    "Key.f11": "f11",
    "Key.f12": "f12",
    "Key.f13": "f13",
    "Key.f14": "f14",
    "Key.f15": "f15",
    "Key.f16": "f16",
    "Key.f17": "f17",
    "Key.f18": "f18",
    "Key.f19": "f19",
    "Key.f20": "f20",
    "Key.f21": "f21",
    "Key.f22": "f22",
    "Key.f23": "f23",
    "Key.f24": "f24",
    
    "Key.tab": "tab",
    "Key.space": "space",
    "Key.ctrl": "ctrl",
    "Key.ctrl_l": "ctrl-left",
    "Key.ctrl_r": "ctrl-right",
    "Key.alt": "alt",
    "Key.alt_l": "alt-left",
    "Key.alt_r": "alt-right",
    "Key.alt_gr": "alt-gr",
    "Key.cmd": "command-left",
    "Key.cmd_r": "command-right",
    "Key.shift": "shift-left",
    "Key.shift_r": "shift-right",
    "Key.esc": "esc",
    "Key.enter": "enter",
    "Key.backspace": "backspace",
    "Key.menu": "menu",
    
    "Key.insert": "insert",
    "Key.delete": "delete",
    "Key.home": "home",
    "Key.end": "end",
    "Key.page_up": "pg-up",
    "Key.page_down": "pg-down",
    
    "Key.left": "left",
    "Key.right": "right",
    "Key.up": "up",
    "Key.down": "down",
    
    "Key.caps_lock": "capslock",
    "Key.num_lock": "numlock",
    "Key.scroll_lock": "scrolllock",
    "Key.print_screen": "psc",
}

def convert_key(key):
    key = str(key)
    if key in keydic:
        key = keydic[key]
    else:
        key = 'undefined'
    return key

def down(key):
    key = convert_key(key)
    print('按下',key)

def up(key):
    key = convert_key(key)
    print('抬起',key)
    if key == 'q':
        return False
    return True

print('按下任意键显示结果，q退出')
with keyboard.Listener(on_press=down,on_release=up) as listener:
    listener.join()
print('感谢观看')
