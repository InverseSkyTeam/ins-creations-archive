import pickle
from icu import UnicodeString, BreakIterator, Locale, Char

# ascii_ctype
def IsASCII(c):
    return not(ord(c) & ~0x7F)


def IsASCIIAlpha(c):
    return ord('a') <= (ord(c) | 0x20) <= ord('z')


def IsASCIIDigit(c):
    return ord('0') <= ord(c) <= ord('9')


def IsASCIIAlphanumeric(c):
    return IsASCIIDigit(c) or IsASCIIAlpha(c)


# uchar
U_LB_ALPHABETIC = 2
UCHAR_LINE_BREAK = 0x1008


def U_MASK(x):
    if isinstance(x, int):
        return 1 << x
    else:
        return 1 << ord(x)


U_UPPERCASE_LETTER = 1
U_LOWERCASE_LETTER = 2
U_TITLECASE_LETTER = 3
U_MODIFIER_LETTER = 4
U_OTHER_LETTER = 5
U_NON_SPACING_MARK = 6
U_ENCLOSING_MARK = 7
U_COMBINING_SPACING_MARK = 8
U_DECIMAL_DIGIT_NUMBER = 9
U_LETTER_NUMBER = 10
U_OTHER_NUMBER = 11
U_GC_LU_MASK = U_MASK(U_UPPERCASE_LETTER)
U_GC_LL_MASK = U_MASK(U_LOWERCASE_LETTER)
U_GC_LT_MASK = U_MASK(U_TITLECASE_LETTER)
U_GC_LM_MASK = U_MASK(U_MODIFIER_LETTER)
U_GC_LO_MASK = U_MASK(U_OTHER_LETTER)
U_GC_MN_MASK = U_MASK(U_NON_SPACING_MARK)
U_GC_ME_MASK = U_MASK(U_ENCLOSING_MARK)
U_GC_MC_MASK = U_MASK(U_COMBINING_SPACING_MARK)
U_GC_ND_MASK = U_MASK(U_DECIMAL_DIGIT_NUMBER)
U_GC_NL_MASK = U_MASK(U_LETTER_NUMBER)
U_GC_NO_MASK = U_MASK(U_OTHER_NUMBER)
U_GC_L_MASK = (U_GC_LU_MASK | U_GC_LL_MASK | U_GC_LT_MASK | U_GC_LM_MASK | U_GC_LO_MASK)
U_GC_M_MASK = (U_GC_MN_MASK | U_GC_ME_MASK | U_GC_MC_MASK)
U_GC_N_MASK = (U_GC_ND_MASK | U_GC_NL_MASK | U_GC_NO_MASK)
U_LB_COMBINING_MARK = 9
U_LB_COMPLEX_CONTEXT = 24


def u_charType(x):
    if isinstance(x, int):
        return Char.charType(UnicodeString(chr(x)))
    else:
        return Char.charType(UnicodeString(x))


# utf16
U16_SURROGATE_OFFSET = (0xd800 << 10) + 0xdc00 - 0x10000


def U16_IS_LEAD(c):
    return ord(c) & 0xfffffc00 == 0xd800


def U16_IS_TRAIL(c):
    return ord(c) & 0xfffffc00 == 0xdc00


def U16_GET_SUPPLEMENTARY(lead, trail):
    return (ord(lead) << 10) + (ord(trail) - U16_SURROGATE_OFFSET)


# uprops
def u_getIntPropertyValue(x, b):
    if isinstance(x, int):
        return Char.getIntPropertyValue(UnicodeString(chr(x)), b)
    else:
        return Char.getIntPropertyValue(UnicodeString(x), b)


# unicode
def HasLineBreakingPropertyComplexContext(c):
    return u_getIntPropertyValue(c, UCHAR_LINE_BREAK) == U_LB_COMPLEX_CONTEXT


# character_names
kNoBreakSpaceCharacter = 0x00A0
kSoftHyphenCharacter = 0x00AD


# text_break_iterator

def GetIterator(string, Locale_, lineBreakType):
    boundary = BreakIterator.createLineInstance(Locale_)
    boundary.setText(string)
    res = []
    for end in boundary:
        res.append(end)
    return res
