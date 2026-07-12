import os
import sys
def get_py_path():
    return sys.executable
def install_library():
    try:
        import icu
    except ImportError:
        print("检测到环境尚未配置完全，正在自动配置（第一次运行常见）")
        import subprocess
        try:
            subprocess.check_call([get_py_path(), '-m', 'pip', 'install', "PyICU-2.8.1-cp37-cp37m-win32.whl"])
            print("\n环境配置成功！请重新运行程序\033[8m;")
            sys.exit(0)
        except subprocess.CalledProcessError:
            print("\n环境配置失败！\033[8m;")
            sys.exit(1)
install_library()


import text_break_iterator as text_break
from icu import Locale
from icu import BreakIterator
# BreakIterator.createCharacterInstance()
class Test:
    def __init__(self, string, Locale_ = Locale.getUS()):
        self.string = string
        self.Locale_ = Locale_
        print('test:', repr(self.string))
    def MatchLineBreaks(self, types, ans):
        res = text_break.test(self.string, types, self.Locale_)
        print(res == ans, res)
        assert res == ans


def test_Basic():
    test = Test("a b  c");
    test.MatchLineBreaks('kNormal', [2, 5, 6])
    print('----------------------')
def test_Newline():
    test = Test("a\nb\n\nc\n d");
    test.MatchLineBreaks('kNormal', [2, 5, 8, 9])
    print('----------------------')
def test_Tab():
    test = Test("a\tb\t\tc");
    test.MatchLineBreaks('kNormal', [2, 5, 6])
    print('----------------------')
def test_LatinPunctuation():
    test = Test("(ab) cd.");
    test.MatchLineBreaks('kNormal', [5, 8])
    test.MatchLineBreaks('kBreakAll', [2, 5, 6, 8])
    test.MatchLineBreaks('kKeepAll', [5, 8])
    print('----------------------')
def test_Chinese():
    test = Test("標準萬國碼");
    test.MatchLineBreaks('kNormal', [1, 2, 3, 4, 5])
    test.MatchLineBreaks('kBreakAll', [1, 2, 3, 4, 5])
    test.MatchLineBreaks('kKeepAll', [5])
    print('----------------------')
def test_ChineseMixed():
    test = Test("標（準）萬ab國.碼");
    test.MatchLineBreaks('kNormal', [1, 4, 5, 7, 9, 10])
    test.MatchLineBreaks('kBreakAll', [1, 4, 5, 6, 7, 9, 10])
    test.MatchLineBreaks('kKeepAll', [1, 4, 9, 10])
    print('----------------------')
def test_ChineseSpaces():
    test = Test("標  萬  a  國");
    test.MatchLineBreaks('kNormal', [3, 6, 9, 10])
    test.MatchLineBreaks('kBreakAll', [3, 6, 9, 10])
    test.MatchLineBreaks('kKeepAll', [3, 6, 9, 10])
    print('----------------------')
def test_KeepEmojiZWJFamilyIsolate():
    test = Test("\U0001F468\u200D\U0001F469\u200D\U0001F467\u200D\U0001F466");
    test.MatchLineBreaks('kNormal', [11])
    test.MatchLineBreaks('kBreakAll', [11])
    test.MatchLineBreaks('kKeepAll', [11])
    print('----------------------')
def test_KeepEmojiModifierSequenceIsolate():
    test = Test("\u261D\U0001F3FB");
    test.MatchLineBreaks('kNormal', [3])
    test.MatchLineBreaks('kBreakAll', [3])
    test.MatchLineBreaks('kKeepAll', [3])
    print('----------------------')
def test_KeepEmojiZWJSequence():
    test = Test("abc \U0001F469\u200D\U0001F469\u200D\U0001F467\u200D\U0001F467 def");
    test.MatchLineBreaks('kNormal', [4, 16, 19])
    test.MatchLineBreaks('kBreakAll', [1, 2, 4, 16, 17, 18, 19])
    test.MatchLineBreaks('kKeepAll', [4, 16, 19])
    print('----------------------')
def test_KeepEmojiModifierSequence():
    test = Test("abc \u261D\U0001F3FB def");
    test.MatchLineBreaks('kNormal', [4, 8, 11])
    test.MatchLineBreaks('kBreakAll', [1, 2, 4, 8, 9, 10, 11])
    test.MatchLineBreaks('kKeepAll', [4, 8, 11])
    print('----------------------')

test_Basic()
test_Newline()
test_Tab()
test_LatinPunctuation()
test_Chinese()
test_ChineseMixed()
test_ChineseSpaces()
test_KeepEmojiZWJFamilyIsolate()
test_KeepEmojiModifierSequenceIsolate()
test_KeepEmojiZWJSequence()
test_KeepEmojiModifierSequence()
