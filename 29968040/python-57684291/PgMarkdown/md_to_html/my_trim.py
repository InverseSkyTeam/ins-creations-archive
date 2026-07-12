WhiteSpace = [
  # WhiteSpace defined in ECMA-262 5.1, 7.2
  0x0009,  # 制表符                  TAB
  0x000B,  # 垂直制表符               VT
  0x000C,  # Form Feed            FF
  0x0020,  # Space                SP
  0x00A0,  # No-break space       NBSP
  0xFEFF,  # Byte Order Mark      BOM

  # LineTerminator defined in ECMA-262 5.1, 7.3
  0x000A,  # Line Feed            LF
  0x000D,  # Carriage Return      CR
  0x2028,  # Line Separator       LS
  0x2029,  # Paragraph Separator  PS

  # Unicode 6.3.0 whitespaces (category 'Zs')
  0x1680,  # Ogham Space Mark
  0x2000,  # EN QUAD
  0x2001,  # EM QUAD
  0x2002,  # EN SPACE
  0x2003,  # EM SPACE
  0x2004,  # THREE-PER-EM SPACE
  0x2005,  # FOUR-PER-EM SPACE
  0x2006,  # SIX-PER-EM SPACE
  0x2007,  # FIGURE SPACE
  0x2008,  # PUNCTUATION SPACE
  0x2009,  # THIN SPACE
  0x200A,  # HAIR SPACE
  0x2028,  # LINE SEPARATOR
  0x2029,  # PARAGRAPH SEPARATOR
  0x202F,  # NARROW NO-BREAK SPACE
  0x205F,  # MEDIUM MATHEMATICAL SPACE
  0x3000,  # IDEOGRAPHIC SPACE
]
WhiteSpace = ''.join([chr(char_code) for char_code in WhiteSpace])