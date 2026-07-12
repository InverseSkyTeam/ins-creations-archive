# 存储每个html标签的信息
# h1, h2, h3, h4, h5, h6, code, blockquote, p, ul, ul_nest, ol, ol_nest, pre, hr


class Label:
    # 用于存储标签的属性
    def __init__(self):
        # 其他
        self.background_color = None

        # padding
        self.padding_top = (0, 'px')
        self.padding_right = (0, 'px')
        self.padding_bottom = (0, 'px')
        self.padding_left = (0, 'px')

        # margin
        self.margin_top = (0, 'px')
        self.margin_right = (0, 'px')
        self.margin_bottom = (0, 'px')
        self.margin_left = (0, 'px')

        # border
        self.border_top_width = (0, 'px')
        self.border_right_width = (0, 'px')
        self.border_bottom_width = (0, 'px')
        self.border_left_width = (0, 'px')
        self.border_top_color = None
        self.border_right_color = None
        self.border_bottom_color = None
        self.border_left_color = None

    def set_border(self, width, color):
        # 设置边框
        self.border_top_width = width
        self.border_right_width = width
        self.border_bottom_width = width
        self.border_left_width = width
        self.border_top_color = color
        self.border_right_color = color
        self.border_bottom_color = color
        self.border_left_color = color

    def set_margin(self, a, b=None, c=None, d=None):
        # 设置margin
        if b is None:
            self.margin_top = a
            self.margin_right = a
            self.margin_bottom = a
            self.margin_left = a
        elif c is None:
            self.margin_top = a
            self.margin_right = b
            self.margin_bottom = a
            self.margin_left = b
        elif d is None:
            self.margin_top = a
            self.margin_right = b
            self.margin_bottom = c
            self.margin_left = b
        else:
            self.margin_top = a
            self.margin_right = b
            self.margin_bottom = c
            self.margin_left = d

    def set_padding(self, a, b=None, c=None, d=None):
        # 设置padding
        if b is None:
            self.padding_top = a
            self.padding_right = a
            self.padding_bottom = a
            self.padding_left = a
        elif c is None:
            self.padding_top = a
            self.padding_right = b
            self.padding_bottom = a
            self.padding_left = b
        elif d is None:
            self.margin_top = a
            self.margin_right = b
            self.margin_bottom = c
            self.margin_left = b
        else:
            self.padding_top = a
            self.padding_right = b
            self.padding_bottom = c
            self.padding_left = d

    def calc_pos(self, pos, font_father_size, font_normal_size):
        if pos[1] == 'px':
            return pos[0]
        elif pos[1] == 'em':
            return pos[0] * font_father_size
        elif pos[1] == 'rem':
            return pos[0] * font_normal_size

    def calc_style(self, font_father_size, font_normal_size):
        # padding
        self.padding_top = self.calc_pos(self.padding_top, font_father_size, font_normal_size)
        self.padding_right = self.calc_pos(self.padding_right, font_father_size, font_normal_size)
        self.padding_bottom = self.calc_pos(self.padding_bottom, font_father_size, font_normal_size)
        self.padding_left = self.calc_pos(self.padding_left, font_father_size, font_normal_size)

        # margin
        self.margin_top = self.calc_pos(self.margin_top, font_father_size, font_normal_size)
        self.margin_right = self.calc_pos(self.margin_right, font_father_size, font_normal_size)
        self.margin_bottom = self.calc_pos(self.margin_bottom, font_father_size, font_normal_size)
        self.margin_left = self.calc_pos(self.margin_left, font_father_size, font_normal_size)

        # border
        self.border_top_width = self.calc_pos(self.border_top_width, font_father_size, font_normal_size)
        self.border_right_width = self.calc_pos(self.border_right_width, font_father_size, font_normal_size)
        self.border_bottom_width = self.calc_pos(self.border_bottom_width, font_father_size, font_normal_size)
        self.border_left_width = self.calc_pos(self.border_left_width, font_father_size, font_normal_size)


class h1:
    # background_color, padding, border, margin
    def __init__(self):
        self.data = Label()

        # border
        self.data.border_bottom_width = (1, 'px')
        self.data.border_bottom_color = (238, 238, 238)

        # margin
        self.data.set_margin((0.5, 'rem'), (0, 'px'))

        # padding
        self.data.padding_bottom = (0.2, 'em')

        # font-size
        self.font_size = (2, 'em')

        # color
        self.color = (0, 0, 0, 255 * 0.75)


class h2:
    # background_color, padding, border, margin
    def __init__(self):
        self.data = Label()

        # border
        self.data.border_bottom_width = (1, 'px')
        self.data.border_bottom_color = (238, 238, 238)

        # margin
        self.data.set_margin((0.5, 'rem'), (0, 'px'))

        # padding
        self.data.padding_bottom = (0.2, 'em')

        # font-size
        self.font_size = (1.5, 'em')

        # color
        self.color = (0, 0, 0, 255 * 0.75)


class h3:
    # background_color, padding, border, margin
    def __init__(self):
        self.data = Label()

        # margin
        self.data.set_margin((0.5, 'rem'), (0, 'px'))

        # font-size
        self.font_size = (1.17, 'em')

        # color
        self.color = (0, 0, 0, 255 * 0.75)


class h4:
    # background_color, padding, border, margin
    def __init__(self):
        self.data = Label()

        # margin
        self.data.set_margin((0.5, 'rem'), (0, 'px'))

        # font-size
        self.font_size = (1, 'em')  # 或(16, 'px')

        # color
        self.color = (0, 0, 0, 255 * 0.75)


class h5:
    # background_color, padding, border, margin
    def __init__(self):
        self.data = Label()

        # margin
        self.data.set_margin((0.5, 'rem'), (0, 'px'))

        # font-size
        self.font_size = (0.83, 'em')

        # color
        self.color = (0, 0, 0, 255 * 0.75)


class h6:
    # background_color, padding, border, margin
    def __init__(self):
        self.data = Label()

        # margin
        self.data.set_margin((0.5, 'rem'), (0, 'px'))

        # font-size
        self.font_size = (0.67, 'em')

        # color
        self.color = (0, 0, 0, 255 * 0.75)


class code:
    # 内联代码块
    # background_color, padding, border, margin
    def __init__(self):
        self.data = Label()

        # margin
        self.data.set_margin((0, 'px'), (0.2, 'em'))

        # padding
        self.data.set_padding((0.1, 'em'),(0.2, 'em'))

        # border
        self.data.set_border((1, 'px'), (232, 232, 232))

        # background-color
        self.data.background_color = (0xfa, 0xfa, 0xfa)

        # font-size
        self.font_size = (0.875, 'em')

        # color
        self.color = (0, 0, 0, 255 * 0.75)


class blockquote:
    # 区块引用
    # background_color, padding, border, margin
    def __init__(self):
        self.data = Label()

        # margin
        self.data.set_margin((0, 'px'), (0, 'px'), (20, 'px'))

        # padding
        self.data.set_padding((10, 'px'),(20, 'px'))

        # border
        self.data.border_left_width = (5, 'px')
        self.data.border_left_color = (238, 238, 238)

        # font-size
        self.font_size = (1, 'em')

        # color
        self.color = (0, 0, 0, 255 * 0.75)


class p:
    # 段落
    # background_color, padding, border, margin
    def __init__(self):
        self.data = Label()

        # margin
        self.data.set_margin((1, 'rem'), (0, 'px'))

        # font-size
        self.font_size = (1, 'em')

        # color
        self.color = (0, 0, 0, 255 * 0.75)


class ul:
    # 无序列表（外层）
    # background_color, padding, border, margin
    def __init__(self):
        self.data = Label()

        # margin
        self.data.set_margin((1, 'rem'), (0, 'px'))

        # padding
        self.data.padding_left = (1.5, 'em')

        # font-size
        self.font_size = (1, 'em')

        # color
        self.color = (0, 0, 0, 255 * 0.75)


class ul_nest:
    # 无序列表（内层，内层需取消margin）
    # background_color, padding, border, margin
    def __init__(self):
        self.data = Label()

        # padding
        self.data.padding_left = (1.5, 'em')

        # font-size
        self.font_size = (1, 'em')

        # color
        self.color = (0, 0, 0, 255 * 0.75)


class ol:
    # 有序列表（外层）
    # background_color, padding, border, margin
    def __init__(self):
        self.data = Label()

        # margin
        self.data.set_margin((1, 'rem'), (0, 'px'))

        # padding
        self.data.padding_left = (1.5, 'em')

        # font-size
        self.font_size = (1, 'em')

        # color
        self.color = (0, 0, 0, 255 * 0.75)


class ol_nest:
    # 有序列表（内层，内层需取消margin）
    # background_color, padding, border, margin
    def __init__(self):
        self.data = Label()

        # padding
        self.data.padding_left = (1.5, 'em')

        # font-size
        self.font_size = (1, 'em')

        # color
        self.color = (0, 0, 0, 255 * 0.75)


class pre:
    # 多行代码块
    # background_color, padding, border, margin
    def __init__(self):
        self.data = Label()

        # padding
        self.data.set_padding((1, 'em'))

        # border
        self.data.set_border((1, 'px'), (232, 232, 232))

        # background-color
        self.data.background_color = (0xfa, 0xfa, 0xfa)

        # font-size
        self.font_size = (1, 'em')

        # color
        self.color = (0, 0, 0, 255 * 0.75)


class hr:
    # 分割线
    # background_color, padding, border, margin
    def __init__(self):
        self.data = Label()

        # margin
        self.data.set_margin((1, 'em'), (0, 'px'))

        # border
        # self.data.set_border((1, 'px'), (232, 232, 232))
        self.data.border_bottom_width = (1, 'px')
        self.data.border_bottom_color = (238, 238, 238)

        # font-size
        self.font_size = (1, 'em')

        # color
        self.color = (0, 0, 0)

class li:
    # 有序列表（内层，内层需取消margin）
    # background_color, padding, border, margin
    def __init__(self):
        self.data = Label()

        # font-size
        self.font_size = (1, 'em')

        # color
        self.color = (0, 0, 0, 255 * 0.75)
