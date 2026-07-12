from icu_simple import *


disable_soft_hyphen_ = False  # 是否禁用软连字符(U+00AD)

kAsciiLineBreakTableFirstChar = ord('!')
kAsciiLineBreakTableLastChar = 127
U_ICU_VERSION_MAJOR_NUM = 73
U_LB_COUNT = 43
BA_LB_COUNT = (U_LB_COUNT - 3) if U_ICU_VERSION_MAJOR_NUM >= 58 else U_LB_COUNT


def B(a, b, c, d, e, f, g, h):
    return a | (b << 1) | (c << 2) | (d << 3) | (e << 4) | (f << 5) | (g << 6) | (h << 7)


def fill(last_tuple, new_length):
    last_list = list(last_tuple)
    for i in range(len(last_list)):
        last_list[i] += (0,) * (new_length - len(last_list[i]))
    return tuple(last_list)


DI = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)  # 0-9 的换行矩阵
AL = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)  # (a-z A-Z) 的换行矩阵
F = 0xFF

# ascii 换行矩阵
# 此表中的断行机会如下：
# - 在某些字符之后，或在开放标点符号（如 '(', '<', '[', '{'）之前（与 Firefox 3.6 兼容）；
# - 在 '-' 和 '?' 之后（向后兼容，并与 Internet Explorer 兼容）。
# 有关不同浏览器和 ICU 标准的断行矩阵，请参考 https://bugs.webkit.org/show_bug.cgi?id=37698。
kAsciiLineBreakTable = fill((
    #  !  "  #  $  %  &  '  (     )  *  +  ,  -  .  /  0  1-8   9  :  ;  <  =  >  ?  @     A-X      Y  Z  [  \  ]  ^  _  `     a-x      y  z  {  |  }  ~  DEL
    (B(0, 0, 0, 0, 0, 0, 0, 1), B(0, 0, 0, 0, 0, 0, 0, 0), 0, B(0, 0, 0, 1, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 1, 0, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 1, 0, 0, 0, 0, 0)),  #  !
    (B(0, 0, 0, 0, 0, 0, 0, 1), B(0, 0, 0, 0, 0, 0, 0, 0), 0, B(0, 0, 0, 1, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 1, 0, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 1, 0, 0, 0, 0, 0)),  #  "
    (B(0, 0, 0, 0, 0, 0, 0, 1), B(0, 0, 0, 0, 0, 0, 0, 0), 0, B(0, 0, 0, 1, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 1, 0, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 1, 0, 0, 0, 0, 0)),  #  #
    (B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), 0, B(0, 0, 0, 0, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 0, 0, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 0, 0, 0, 0, 0, 0)),  #  $
    (B(0, 0, 0, 0, 0, 0, 0, 1), B(0, 0, 0, 0, 0, 0, 0, 0), 0, B(0, 0, 0, 1, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 1, 0, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 1, 0, 0, 0, 0, 0)),  #  %
    (B(0, 0, 0, 0, 0, 0, 0, 1), B(0, 0, 0, 0, 0, 0, 0, 0), 0, B(0, 0, 0, 1, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 1, 0, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 1, 0, 0, 0, 0, 0)),  #  &
    (B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), 0, B(0, 0, 0, 0, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 0, 0, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 0, 0, 0, 0, 0, 0)),  #  '
    (B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), 0, B(0, 0, 0, 0, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 0, 0, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 0, 0, 0, 0, 0, 0)),  #  (
    (B(0, 0, 0, 0, 0, 0, 0, 1), B(0, 0, 0, 0, 0, 0, 0, 0), 0, B(0, 0, 0, 1, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 1, 0, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 1, 0, 0, 0, 0, 0)),  #  )
    (B(0, 0, 0, 0, 0, 0, 0, 1), B(0, 0, 0, 0, 0, 0, 0, 0), 0, B(0, 0, 0, 1, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 1, 0, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 1, 0, 0, 0, 0, 0)),  #  *
    (B(0, 0, 0, 0, 0, 0, 0, 1), B(0, 0, 0, 0, 0, 0, 0, 0), 0, B(0, 0, 0, 1, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 1, 0, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 1, 0, 0, 0, 0, 0)),  #  +
    (B(0, 0, 0, 0, 0, 0, 0, 1), B(0, 0, 0, 0, 0, 0, 0, 0), 0, B(0, 0, 0, 1, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 1, 0, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 1, 0, 0, 0, 0, 0)),  #  ,
    (B(0, 1, 1, 0, 1, 1, 1, 1), B(0, 1, 1, 0, 1, 0, 0, 0), 0, B(0, 0, 0, 1, 1, 1, 0, 1), F, F, F, B(1, 1, 1, 1, 0, 1, 1, 1), F, F, F, B(1, 1, 1, 1, 0, 1, 1, 1)),  #  - 注意：在 shouldBreakAfter() 中硬编码处理 '0'-'9' 之前的中断
    (B(0, 0, 0, 0, 0, 0, 0, 1), B(0, 0, 0, 0, 0, 0, 0, 0), 0, B(0, 0, 0, 1, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 1, 0, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 1, 0, 0, 0, 0, 0)),  #  .
    (B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), 0, B(0, 0, 0, 0, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 0, 0, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 0, 0, 0, 0, 0, 0)),  #  /
    DI,  DI,  DI,  DI,  DI,  DI,  DI,  DI,  DI,  DI,  #  0-9
    (B(0, 0, 0, 0, 0, 0, 0, 1), B(0, 0, 0, 0, 0, 0, 0, 0), 0, B(0, 0, 0, 1, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 1, 0, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 1, 0, 0, 0, 0, 0)),  #  :
    (B(0, 0, 0, 0, 0, 0, 0, 1), B(0, 0, 0, 0, 0, 0, 0, 0), 0, B(0, 0, 0, 1, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 1, 0, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 1, 0, 0, 0, 0, 0)),  #  ;
    (B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), 0, B(0, 0, 0, 0, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 0, 0, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 0, 0, 0, 0, 0, 0)),  #  <
    (B(0, 0, 0, 0, 0, 0, 0, 1), B(0, 0, 0, 0, 0, 0, 0, 0), 0, B(0, 0, 0, 1, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 1, 0, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 1, 0, 0, 0, 0, 0)),  #  =
    (B(0, 0, 0, 0, 0, 0, 0, 1), B(0, 0, 0, 0, 0, 0, 0, 0), 0, B(0, 0, 0, 1, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 1, 0, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 1, 0, 0, 0, 0, 0)),  #  >
    (B(0, 0, 1, 1, 1, 1, 0, 1), B(0, 1, 1, 0, 1, 0, 0, 1), F, B(1, 0, 0, 1, 1, 1, 0, 1), F, F, F, B(1, 1, 1, 1, 0, 1, 1, 1), F, F, F, B(1, 1, 1, 1, 0, 1, 1, 0)),  #  ?
    (B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), 0, B(0, 0, 0, 0, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 0, 0, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 0, 0, 0, 0, 0, 0)),  #  @
    AL,  AL,  AL,  AL,  AL,  AL,  AL,  AL,  AL,  AL,  AL,  AL,  AL,  AL,  AL,  AL,  AL,  AL,  AL,  AL,  AL,  AL,  AL,  AL,  AL,  AL,  #  A-Z
    (B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), 0, B(0, 0, 0, 0, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 0, 0, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 0, 0, 0, 0, 0, 0)),  #  [
    (B(0, 0, 0, 0, 0, 0, 0, 1), B(0, 0, 0, 0, 0, 0, 0, 0), 0, B(0, 0, 0, 1, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 1, 0, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 1, 0, 0, 0, 0, 0)),  #  '\'
    (B(0, 0, 0, 0, 0, 0, 0, 1), B(0, 0, 0, 0, 0, 0, 0, 0), 0, B(0, 0, 0, 1, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 1, 0, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 1, 0, 0, 0, 0, 0)),  #  ]
    (B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), 0, B(0, 0, 0, 0, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 0, 0, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 0, 0, 0, 0, 0, 0)),  #  ^
    (B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), 0, B(0, 0, 0, 0, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 0, 0, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 0, 0, 0, 0, 0, 0)),  #  _
    (B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), 0, B(0, 0, 0, 0, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 0, 0, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 0, 0, 0, 0, 0, 0)),  #  `
    AL,  AL,  AL,  AL,  AL,  AL,  AL,  AL,  AL,  AL,  AL,  AL,  AL,  AL,  AL,  AL,  AL,  AL,  AL,  AL,  AL,  AL,  AL,  AL,  AL,  AL,  #  a-z
    (B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), 0, B(0, 0, 0, 0, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 0, 0, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 0, 0, 0, 0, 0, 0)),  #  {
    (B(0, 0, 0, 0, 0, 0, 0, 1), B(0, 0, 0, 0, 0, 0, 0, 0), 0, B(0, 0, 0, 1, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 1, 0, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 1, 0, 0, 0, 0, 0)),  #  |
    (B(0, 0, 0, 0, 0, 0, 0, 1), B(0, 0, 0, 0, 0, 0, 0, 0), 0, B(0, 0, 0, 1, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 1, 0, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 1, 0, 0, 0, 0, 0)),  #  }
    (B(0, 0, 0, 0, 0, 0, 0, 1), B(0, 0, 0, 0, 0, 0, 0, 0), 0, B(0, 0, 0, 1, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 1, 0, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 1, 0, 0, 0, 0, 0)),  #  ~
    (B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), 0, B(0, 0, 0, 0, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 0, 0, 0, 0, 0, 0), 0, 0, 0, B(0, 0, 0, 0, 0, 0, 0, 0)),  #  DEL
), (kAsciiLineBreakTableLastChar - kAsciiLineBreakTableFirstChar) // 8 + 1)

# CSS word-break: break-all 的断行表。该表与 asciiLineBreakTable 不同之处在于：
# - 索引是 UAX#14 Unicode Line Breaking Algorithm 中定义的断行类别：http://unicode.org/reports/tr14/#DescriptionOfProperties
# - 1 表示额外的断行机会。0 表示回退到正常的断行，而不是 "禁止断行"。
kBreakAllLineBreakClassTable = fill((
    # XX AI AL B2 BA BB BK CB    CL CM CR EX GL HY ID IN    IS LF NS NU OP PO PR QU    SA SG SP SY ZW NL WJ H2    H3 JL JT JV CP CJ HL RI
    (B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0)),  #  XX
    (B(0, 1, 1, 0, 1, 0, 0, 0), B(0, 0, 0, 0, 0, 1, 0, 0), B(0, 0, 0, 1, 1, 0, 1, 0), B(1, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 1, 0)),  #  AI
    (B(0, 1, 1, 0, 1, 0, 0, 0), B(0, 0, 0, 0, 0, 1, 0, 0), B(0, 0, 0, 1, 1, 0, 1, 0), B(1, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 1, 0)),  #  AL
    (B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0)),  #  B2
    (B(0, 1, 1, 0, 1, 0, 0, 0), B(0, 0, 0, 0, 0, 1, 0, 0), B(0, 0, 0, 1, 1, 0, 1, 0), B(1, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 1, 0)),  #  BA
    (B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0)),  #  BB
    (B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0)),  #  BK
    (B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0)),  #  CB
    (B(0, 1, 1, 0, 1, 0, 0, 0), B(0, 0, 0, 0, 0, 1, 0, 0), B(0, 0, 0, 1, 0, 0, 1, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 1, 0)),  #  CL
    (B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0)),  #  CM
    (B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0)),  #  CR
    (B(0, 1, 1, 0, 1, 0, 0, 0), B(0, 0, 0, 0, 0, 1, 0, 0), B(0, 0, 0, 1, 0, 1, 1, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 1, 0)),  #  EX
    (B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0)),  #  GL
    (B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 1, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0)),  #  HY
    (B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0)),  #  ID
    (B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0)),  #  IN
    (B(0, 1, 1, 0, 1, 0, 0, 0), B(0, 0, 0, 0, 0, 1, 0, 0), B(0, 0, 0, 1, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 1, 0)),  #  IS
    (B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0)),  #  LF
    (B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0)),  #  NS
    (B(0, 1, 1, 0, 1, 0, 0, 0), B(0, 0, 0, 0, 0, 1, 0, 0), B(0, 0, 0, 1, 1, 0, 1, 0), B(1, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 1, 0)),  #  NU
    (B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0)),  #  OP
    (B(0, 1, 1, 0, 1, 0, 0, 0), B(0, 0, 0, 0, 0, 1, 0, 0), B(0, 0, 0, 1, 0, 1, 1, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 1, 0)),  #  PO
    (B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 1, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0)),  #  PR
    (B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0)),  #  QU
    (B(0, 1, 1, 0, 1, 0, 0, 0), B(0, 0, 0, 0, 0, 1, 0, 0), B(0, 0, 0, 1, 1, 0, 1, 0), B(1, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 1, 0)),  #  SA
    (B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0)),  #  SG
    (B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0)),  #  SP
    (B(0, 1, 1, 0, 1, 0, 0, 0), B(0, 0, 0, 0, 0, 1, 0, 0), B(0, 0, 0, 1, 1, 0, 1, 0), B(1, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 1, 0)),  #  SY
    (B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0)),  #  ZW
    (B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0)),  #  NL
    (B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0)),  #  WJ
    (B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0)),  #  H2
    (B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0)),  #  H3
    (B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0)),  #  JL
    (B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0)),  #  JT
    (B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0)),  #  JV
    (B(0, 1, 1, 0, 1, 0, 0, 0), B(0, 0, 0, 0, 0, 1, 0, 0), B(0, 0, 0, 1, 0, 0, 1, 0), B(1, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 1, 0)),  #  CP
    (B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0)),  #  CJ
    (B(0, 1, 1, 0, 1, 0, 0, 0), B(0, 0, 0, 0, 0, 1, 0, 0), B(0, 0, 0, 1, 1, 0, 1, 0), B(1, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 1, 0)),  #  HL
    (B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0), B(0, 0, 0, 0, 0, 0, 0, 0)),  #  RI
), BA_LB_COUNT // 8 + 1)

del B, F, DI, AL

if len(kAsciiLineBreakTable) != kAsciiLineBreakTableLastChar - kAsciiLineBreakTableFirstChar + 1:
    print('#ERROR:', 'asciiLineBreakTable should be consistent')
if len(kBreakAllLineBreakClassTable) != BA_LB_COUNT:
    print('#ERROR:', 'breakAllLineBreakClassTable should be consistent')


def ShouldBreakAfter(last_ch, ch, next_ch):
    # 在某些上下文中，不允许在 '-' 和数字之间断行，因为'-'可能表示负号
    # 但允许在长 URL 中的 'ABCD-1234' 和 '1234-5678' 之间断行。
    if ch == '-' and IsASCIIDigit(next_ch):
        return IsASCIIAlphanumeric(last_ch)

    # 如果 ch 和 nextCh 都是 ASCII 字符
    # 则使用查找换行矩阵进行增强速度和与其他浏览器的兼容性（详见 asciiLineBreakTable 的注释）。
    if kAsciiLineBreakTableFirstChar <= ord(ch) <= kAsciiLineBreakTableLastChar and \
       kAsciiLineBreakTableFirstChar <= ord(next_ch) <= kAsciiLineBreakTableLastChar:
        table_row = kAsciiLineBreakTable[ord(ch) - kAsciiLineBreakTableFirstChar]
        next_ch_index = ord(next_ch) - kAsciiLineBreakTableFirstChar
        return table_row[next_ch_index // 8] & (1 << (next_ch_index % 8))
    # 否则根据 Unicode 算法返回 False
    return False


def LineBreakPropertyValue(last_ch, ch):
    if ch == '+':
        return U_LB_ALPHABETIC  # 当启用 break-all 时，IE将 "+" 处理为 AL 类别。
    ch32 = U16_GET_SUPPLEMENTARY(last_ch, ch) if (U16_IS_LEAD(last_ch) and U16_IS_TRAIL(ch)) else ord(ch)
    return u_getIntPropertyValue(ch32, UCHAR_LINE_BREAK)


def ShouldBreakAfterBreakAll(last_line_break, line_break):
    if 0 <= line_break < BA_LB_COUNT and 0 <= last_line_break < BA_LB_COUNT:
        table_row = kBreakAllLineBreakClassTable[last_line_break]
        return table_row[line_break // 8] & (1 << (line_break % 8))
    return False


# 计算使用 'word-break:keep-all' 时是否应该阻止换行。
# https://drafts.csswg.org/css-text-3/#valdef-word-break-keep-all
# 规范对这个工作原理的描述并不详细。根据规范，这个逻辑会阻止L/M通用类别和复杂的断行，
# 因为规范中提到了 "except some south east aisans".
# https://github.com/w3c/csswg-drafts/issues/1619
def ShouldKeepAfterKeepAll(last_ch, ch, next_ch):
    pre_ch = ord(last_ch) if U_MASK(u_charType(ch)) & U_GC_M_MASK else ord(ch)
    return U_MASK(u_charType(pre_ch)) & (U_GC_L_MASK | U_GC_N_MASK) and \
           not HasLineBreakingPropertyComplexContext(pre_ch) and \
           U_MASK(u_charType(next_ch)) & (U_GC_L_MASK | U_GC_N_MASK) and \
           not HasLineBreakingPropertyComplexContext(next_ch)


def NeedsLineBreakIterator(ch):  # 判断一个 Unicode 字符是否需要换行分割
    return ord(ch) > kAsciiLineBreakTableLastChar and ord(ch) != kNoBreakSpaceCharacter


class Context:  # 文本类
    def __init__(self, string, length, start_offset, index):
        self.current = None  # 当前字符
        self.last = self.ContextChar(chr(0))  # 上个字符
        self.last_last_ch = chr(0)  # 上上个字符

        if index > 0:  # index: 当前位置
            self.last = self.ContextChar(string[index - 1])  # 初始化上个字符
            if index > 1:
                self.last_last_ch = string[index - 2]  # 初始化上上个字符

    def fetch(self, string, length, index):
        if index >= length:  # 已经遍历完成
            return False
        self.current = self.ContextChar(string[index])  # 更新当前字符
        return True

    def advance(self, index):
        index += 1  # 当前位置增加
        self.last_last_ch = self.last.ch  # 更新上上个字符
        self.last = self.current  # 更新上个字符
        return index

    class ContextChar:  # 字符类
        def __init__(self, ch):
            self.ch = ch  # 字符
            self.is_space = ord(ch) in (0x20, 0x9, 0xA)  # 字符是否是空格


LineBreakType = ('kNormal', 'kBreakAll', 'kBreakCharacter', 'kKeepAll', 'kPhrase')
BreakSpaceType = ('kAfterSpaceRun', 'kAfterEverySpace')


def cpp_for(context, string, length, pos):
    i = pos
    while context.fetch(string, length, i):
        yield i
        i = context.advance(i)


def NextBreakablePosition(pos, string, length):
    start_offset_ = 0
    lineBreakType = 'kNormal'
    break_space = 'kAfterSpaceRun'

    context = Context(string, length, start_offset_, pos)
    next_break = -1
    last_line_break = 0
    if lineBreakType == 'kBreakAll':
        last_line_break = LineBreakPropertyValue(context.last_last_ch, context.last.ch)
    for i in cpp_for(context, string, length, pos):
        if break_space == 'kAfterSpaceRun':
            if context.current.is_space:
                continue
            if context.last.is_space:
                return i
        elif break_space == 'kAfterEverySpace':
            if context.last.is_space or ord(context.last.ch) == 0x3000:
                return i
            if (context.current.is_space or ord(context.current.ch) == 0x3000) and i + 1 < length:
                return i + 1

        if ShouldBreakAfter(context.last_last_ch, context.last.ch, context.current.ch):
            return i

        if lineBreakType == 'kBreakAll' and not U16_IS_LEAD(context.current.ch):
            line_break = LineBreakPropertyValue(context.last.ch, context.current.ch)
            if ShouldBreakAfterBreakAll(last_line_break, line_break):
                return i - 1 if i > pos and U16_IS_TRAIL(context.current.ch) else i
            if line_break != U_LB_COMBINING_MARK:
                last_line_break = line_break

        if lineBreakType == 'kKeepAll' and \
           ShouldKeepAfterKeepAll(context.last_last_ch, context.last.ch, context.current.ch):
            continue

        if NeedsLineBreakIterator(context.current.ch) or \
           NeedsLineBreakIterator(context.last.ch):
            if next_break < i and False:  # TODO: GetIterator 实现后，"and False" 应该删除
                if i:
                    break_iterator = GetIterator()
                    if break_iterator:
                        next_break = i - 1
                        while True:
                            next_break = break_iterator.following(next_break - start_offset_)
                            if next_break >= 0:
                                next_break = next_break + start_offset_
                                if disable_soft_hyphen_ and next_break > 0 and \
                                   string[next_break - 1] == kSoftHyphenCharacter:
                                    continue
                            break
            if i == next_break and not context.last.is_space:
                return i
    return length


def test(string):
    # string = input()
    pos = 0
    res = [0, ]
    while True:
        pos = NextBreakablePosition(pos, string, len(string))
        res.append(pos)
        # print(pos, pos1)
        if pos >= len(string):
            break
        pos += 1
    return res
